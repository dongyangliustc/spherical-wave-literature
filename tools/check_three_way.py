#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Three-way consistency check for the literature corpus.

Compares the *basename* sets of:
  A. papers/**/*.pdf                        (files actually on disk)
  B. index/registry/{core,candidates}.yaml  (paths.pdf, controlled source of truth)
  C. spherical_wave_mcp/config/sources.yaml (entries with format: pdf, i.e. what gets ingested)

Rationale: the project has historically had gaps in BOTH directions -- PDFs never
entered into the registry, and registry entries that were never ingested. Any
diff printed here is a real defect unless explicitly waived.

Usage:
    python tools/check_three_way.py            # report only
    python tools/check_three_way.py --strict   # exit 2 when any diff exists
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAPERS = REPO / "papers"
REGISTRY = REPO / "index" / "registry"
SOURCES = Path(r"D:\WORK\workbuddy\spherical_wave_mcp\config\sources.yaml")


def disk_pdfs() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in sorted(PAPERS.rglob("*.pdf")):
        out[p.name] = str(p.relative_to(REPO)).replace("\\", "/")
    return out


def registry_pdfs() -> dict[str, str]:
    """name -> 'file: entry_id'  (flattened YAML: nested paths.pdf surfaces as 'pdf:')"""
    out: dict[str, str] = {}
    for fname in ("core.yaml", "candidates.yaml"):
        path = REGISTRY / fname
        if not path.exists():
            continue
        cur_id = None
        for raw in path.read_text(encoding="utf-8").split("\n"):
            s = raw.strip()
            m = re.match(r'^-\s*id:\s*"([^"]+)"', s)
            if m:
                cur_id = m.group(1)
                continue
            m = re.match(r'^pdf:\s*(.+)$', s)
            if m:
                val = m.group(1).strip()
                if val in ("null", "", "~"):
                    continue
                val = val.strip('"')
                name = val.split("/")[-1]
                out[name] = f"{fname}: {cur_id}"
    return out


def sources_pdfs() -> dict[str, str]:
    out: dict[str, str] = {}
    if not SOURCES.exists():
        return out
    lines = SOURCES.read_text(encoding="utf-8").split("\n")
    cur_id = None
    cur_path = None
    cur_fmt = None

    def flush() -> None:
        if cur_path and cur_fmt == "pdf":
            name = cur_path.strip('"').split("/")[-1]
            out[name] = f"sources.yaml: {cur_id}"

    for raw in lines:
        s = raw.strip()
        m = re.match(r'^-\s*source_id:\s*"([^"]+)"', s)
        if m:
            flush()
            cur_id, cur_path, cur_fmt = m.group(1), None, None
            continue
        m = re.match(r'^path:\s*(.+)$', s)
        if m:
            cur_path = m.group(1).strip()
            continue
        m = re.match(r'^format:\s*(.+)$', s)
        if m:
            cur_fmt = m.group(1).strip().strip('"')
            continue
    flush()
    return out


def diff(a: dict[str, str], b: dict[str, str]) -> set[str]:
    return set(a) - set(b)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 2 if any diff exists")
    args = ap.parse_args()

    A, B, C = disk_pdfs(), registry_pdfs(), sources_pdfs()

    print(f"A. papers/**/*.pdf          : {len(A)} unique basenames")
    print(f"B. registry paths.pdf        : {len(B)} unique basenames")
    print(f"C. sources.yaml format=pdf   : {len(C)} unique basenames")

    problems = False
    checks = [("A-B", A, B, "on disk but MISSING from registry"),
              ("B-A", B, A, "in registry but NO file on disk"),
              ("C-B", C, B, "in sources.yaml but MISSING from registry"),
              ("B-C", B, C, "in registry but NEVER ingested (not in sources.yaml)"),
              ("A-C", A, C, "on disk but not ingested"),
              ("C-A", C, A, "in sources.yaml but no file on disk")]

    for label, x, y, desc in checks:
        d = sorted(diff(x, y))
        if not d:
            continue
        problems = True
        print(f"\n[{label}] {desc}  ({len(d)})")
        for name in d:
            print(f"   - {name}   <- {x[name]}")

    if not problems:
        print("\nOK: three-way consistency holds (A == B == C).")
        return 0

    print("\nNOTE: diffs above are defects unless explicitly waived.")
    return 2 if args.strict else 1


if __name__ == "__main__":
    raise SystemExit(main())
