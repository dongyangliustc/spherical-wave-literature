"""Capture atomic claim cards from a self-generated knowledge document and anchor
them against the local evidence index (epistemic anchor step).

Part of the "同流不同信" v0.1 pipeline:
    own_note (T2, unverified)  --capture_claims-->  claims.yaml  +  initial anchor

For each candidate claim the tool:
  1. classifies claim_kind  (fact / derivation / hypothesis / workflow)
  2. searches the evidence index for anchors
  3. proposes an epistemic_status:
        literature_supported  <- anchored to a T0/T0* chunk (primary source)
        consistent            <- anchored only to a T1 synth_summary (single-hop, needs primary)
        unverified            <- no anchor found

The proposed status is machine-screened. Human review happens at the weekly
review packet gate before anything becomes `literature_supported`/`benchmark_verified`
for code-context injection.

Usage:
    python tools/capture_claims.py --file notes/对话知识_核实试点_2026-08-26.md \
        --index D:/WORK/workbuddy/spherical_wave_mcp/data/index/materials.sqlite \
        --out index/registry/claims.yaml [--dry-run] [--module schwinger_amplitude]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# course_material_mcp is an editable install in the spherical_wave_mcp venv.
from course_material_mcp.retrieval import search_sources
from course_material_mcp.store import SourceStore

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / ".." / "spherical_wave_mcp" / "data" / "index" / "materials.sqlite"
DEFAULT_OUT = ROOT / "index" / "registry" / "claims.yaml"

_BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s*(.*)$")
_HYPO_RE = re.compile(r"(是否正确|是否成立|是否能够|假设|有待验证|待验证|未验证|是否.*正确|猜想|需要验证)")
_DERIV_RE = re.compile(r"(推导|等于|等价|递推|积分|展开|演算|参照|依据|由.*得到|可化为|约化为|近似为)")
_WORKFLOW_RE = re.compile(r"(应当|必须|禁止|规则|规范|流程|策略|方案|建议|门控|放置|采用|落点|存档于|继承)")
_HARD_NO_RE = re.compile(r"(^#|^>|^```|^---|^目标|^contents|^内容|^来源|^建立日期)")

# Lightweight keyword -> project_module hints (heuristic; override after capture).
_MODULE_HINTS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"schwinger|可分展开变分"), "schwinger_amplitude"),
    (re.compile(r"tau"), "tau_matrix"),
    (re.compile(r"separable|可分"), "separable_potential"),
    (re.compile(r"green|格林"), "green_function_matrix"),
    (re.compile(r"lb94|势|x[cs]|交换相关|变分|h[fe] 势"), "momentum_gto"),
    (re.compile(r"角向|lmax|partial|部分波|球面谐|光电子角"), "angular_reduction"),
    (re.compile(r"1/s|taylor|小.?s|中性"), "momentum_gto"),
    (re.compile(r"长度规范|速度规范|规范"), "sw_matrix_element"),
    (re.compile(r"基准|benchmark|h2|n2|c2h2|section|截面"), "benchmark_strategy"),
    (re.compile(r"non-s|p-type|高角动量|分子测试|frame|坐标变换"), "frame_transform"),
    (re.compile(r"knowledge|知识库|claim|主张|核实|同流|gate|门控|schema|registry"), "workflow_design"),
]


def _next_id(existing: list[str], prefix: str = "clm") -> str:
    numbers = [int(i[len(prefix) + 1:]) for i in existing if i.startswith(f"{prefix}-")]
    return f"{prefix}-{max(numbers, default=0) + 1:04d}"


def _classify(text: str) -> str:
    if _HYPO_RE.search(text):
        return "hypothesis"
    if _DERIV_RE.search(text):
        return "derivation"
    if _WORKFLOW_RE.search(text):
        return "workflow"
    return "fact"


def _module_hint(text: str) -> list[str]:
    matched = [name for pattern, name in _MODULE_HINTS if pattern.search(text)]
    return matched[:2]


def extract_candidates(path: Path) -> list[str]:
    """Pull declarative bullet-style statements from a conversation knowledge doc."""
    candidates: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or _HARD_NO_RE.search(line):
            continue
        bullet = _BULLET_RE.match(raw)
        if not bullet:
            continue
        statement = bullet.group(1).strip().rstrip("。；;.")
        if len(statement) < 6 or statement.endswith(":"):
            continue
        candidates.append(statement)
    return candidates


def _anchor(store: SourceStore, statement: str, top_k: int = 5) -> tuple[str, list[dict[str, Any]]]:
    """Return (proposed_status, evidence).

    Conservative three-level anchoring:
      - skip the claim's own ideation chunks (cannot be its own evidence)
      - literature_supported  <- a T0/T0* chunk literally contains the claim (score >= 100)
      - consistent            <- some non-ideation anchor exists but match is weak
      - unverified            <- no external anchor found
    The result is always machine-screened; human review happens at the weekly gate.
    """
    response = search_sources(store, statement, top_k=top_k)
    external = [
        r for r in response.results
        if r.provenance != "ideation" and r.source_id != "own-note-pilot-2026-08-26"
    ]
    evidence = [
        {
            "source_id": r.source_id,
            "source_title": r.source_title,
            "provenance": r.provenance,
            "epistemic_status": r.epistemic_status,
            "locator": r.locator,
            "score": r.score,
        }
        for r in external
    ]
    if not external:
        return "unverified", []
    best = external[0]
    if best.provenance in {"literature", "own_publication"} and best.score >= 100:
        return "literature_supported", evidence
    if best.score > 0:
        return "consistent", evidence
    return "unverified", evidence


def _load_existing(out: Path) -> tuple[list[dict[str, Any]], set[str]]:
    if not out.is_file():
        return [], set()
    claims: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line in out.read_text(encoding="utf-8").splitlines():
        if line.startswith("claims:"):
            continue
        if line.startswith("  - id:"):
            if current is not None:
                claims.append(current)
            current = {"id": line.split(":", 1)[1].strip().strip('"')}
        elif current is not None and line.startswith("    "):
            key, _, value = line.strip().partition(":")
            value = value.strip()
            if key in {"project_module", "evidence_chain"} and value.startswith("["):
                current[key] = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
            elif key in {"project_module", "evidence_chain"}:
                current[key] = []
            else:
                current[key] = value.strip('"').strip("'") or None
    if current is not None:
        claims.append(current)
    return claims, {str(c.get("id")) for c in claims if c.get("id")}


def _emit_yaml(claims: list[dict[str, Any]]) -> str:
    lines = [
        "# 自产主张 Claim Registry（v0.1, 2026-08-26）",
        "# 门控：仅 literature_supported / benchmark_verified 可注入代码上下文。",
        "# 增量来源：tools/capture_claims.py（对话知识 → 主张卡 + 自动锚定）。",
        "claims:",
    ]
    for c in claims:
        lines.append(f"  - id: \"{c['id']}\"")
        lines.append(f"    statement: \"{c.get('statement', '')}\"")
        lines.append(f"    source_context: \"{c.get('source_context', '')}\"")
        lines.append(f"    claim_kind: \"{c.get('claim_kind', 'unclassified')}\"")
        lines.append(f"    provenance: \"{c.get('provenance', 'ideation')}\"")
        lines.append(f"    epistemic_status: \"{c.get('epistemic_status', 'unverified')}\"")
        modules = c.get("project_module") or []
        lines.append("    project_module: [" + ", ".join(f'"{m}"' for m in modules) + "]")
        chain = c.get("evidence_chain") or []
        lines.append("    evidence_chain: [" + ", ".join(f'"{e}"' for e in chain) + "]")
        anchor = c.get("anchor_locator") or "null"
        lines.append(f"    anchor_locator: {anchor}")
        lines.append(f"    last_verified: \"{c.get('last_verified', '2026-08-26')}\"")
        lines.append(f"    reviewer: \"{c.get('reviewer', 'DY')}\"")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture claims and anchor against evidence index")
    parser.add_argument("--file", required=True, type=Path, help="source own_note document")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--source-context", default="2026-08-26 对话知识试点")
    parser.add_argument("--dry-run", action="store_true", help="print new cards without writing")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"error: source file not found: {args.file}", file=sys.stderr)
        return 2

    store = SourceStore(args.index)
    existing, existing_ids = _load_existing(args.out)
    new_id = _next_id(list(existing_ids))

    candidates = extract_candidates(args.file)
    print(f"extracted {len(candidates)} candidate claims from {args.file.name}\n")

    added: list[dict[str, Any]] = []
    for statement in candidates:
        status, evidence = _anchor(store, statement, top_k=args.top_k)
        card = {
            "id": new_id,
            "statement": statement,
            "source_context": args.source_context,
            "claim_kind": _classify(statement),
            "provenance": "ideation",
            "epistemic_status": status,
            "project_module": _module_hint(statement),
            "evidence_chain": [e["source_id"] for e in evidence],
            "anchor_locator": f'"{evidence[0]["locator"]}"' if evidence else "null",
            "last_verified": "2026-08-26",
            "reviewer": "DY",
        }
        new_id = _next_id(list(existing_ids) + [card["id"]])
        added.append(card)
        print(f"[{status:<20}] {card['id']} ({card['claim_kind']}) "
              f"{'-> '.join(card['project_module']) or '-'}: {statement[:60]}{'…' if len(statement) > 60 else ''}")
        for e in evidence[: args.top_k]:
            print(f"      anchor: {e['source_id']} ({e['provenance']}/{e['epistemic_status']}, score={e['score']:.0f})")

    if args.dry_run:
        print("\n[DRY-RUN] " + _emit_yaml(existing + added))
        return 0

    merged = existing + added
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(_emit_yaml(merged), encoding="utf-8")
    print(f"\nwrote {len(added)} new claim(s) -> {args.out} (total {len(merged)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
