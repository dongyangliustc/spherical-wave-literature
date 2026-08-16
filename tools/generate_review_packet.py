#!/usr/bin/env python3
"""Generate a weekly literature review packet from registry files."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

try:
    from tools.validate_registry import REGISTRY_DIR, REPO_ROOT, parse_registry, validate
except ModuleNotFoundError:
    from validate_registry import REGISTRY_DIR, REPO_ROOT, parse_registry, validate


REVIEW_DIR = REPO_ROOT / "outputs" / "review_packets"


def row(values: list[str]) -> str:
    return "| " + " | ".join(value.replace("\n", " ") for value in values) + " |"


def generate_packet(packet_date: date, output_dir: Path = REVIEW_DIR) -> Path:
    errors = validate(REGISTRY_DIR)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"Registry validation failed before packet generation:\n{joined}")

    candidates = parse_registry(REGISTRY_DIR / "candidates.yaml", "items")
    benchmarks = parse_registry(REGISTRY_DIR / "benchmarks.yaml", "benchmarks")
    risks = parse_registry(REGISTRY_DIR / "risks.yaml", "risks")

    review_needed = [
        item for item in candidates if item.get("state") == "needs_human_review"
    ]
    recommended_rejects = [
        item
        for item in candidates
        if item.get("state") in {"duplicate", "out_of_scope", "low_quality"}
    ]
    recommended_upgrades = [
        item
        for item in candidates
        if item.get("state") in {"extracted", "reviewed"}
        or item.get("actionability") in {"direct_benchmark", "implementation_guidance"}
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{packet_date.isoformat()}_literature_review_packet.md"
    path.write_text(
        build_packet(
            packet_date,
            candidates,
            recommended_upgrades,
            recommended_rejects,
            review_needed,
            benchmarks,
            risks,
        ),
        encoding="utf-8",
    )
    return path


def build_packet(
    packet_date: date,
    candidates: list[dict],
    recommended_upgrades: list[dict],
    recommended_rejects: list[dict],
    review_needed: list[dict],
    benchmarks: list[dict],
    risks: list[dict],
) -> str:
    lines = [
        f"# Literature Review Packet: {packet_date.isoformat()}",
        "",
        "## Summary",
        "",
        f"- Week: {packet_date.isoformat()}",
        "- Automation run IDs: manual/local generation",
        f"- New candidates: {len(candidates)}",
        f"- Recommended upgrades: {len(recommended_upgrades)}",
        f"- Recommended rejects: {len(recommended_rejects)}",
        f"- Items needing human review: {len(review_needed) + len(recommended_upgrades)}",
        "",
        "## Recommended Upgrades",
        "",
        "| ID | Source | Proposed State | Reason | Human Action |",
        "|----|--------|----------------|--------|--------------|",
    ]
    if recommended_upgrades:
        for item in recommended_upgrades:
            lines.append(
                row(
                    [
                        str(item.get("id", "")),
                        str(item.get("title", "")),
                        "reviewed/indexed",
                        str(item.get("actionability", "")),
                        "Approve promotion or keep as candidate",
                    ]
                )
            )
    else:
        lines.append(row(["", "", "", "", ""]))

    lines.extend(
        [
            "",
            "## Recommended Rejects",
            "",
            "| ID | Source | Reject Reason | Evidence |",
            "|----|--------|---------------|----------|",
        ]
    )
    if recommended_rejects:
        for item in recommended_rejects:
            lines.append(
                row(
                    [
                        str(item.get("id", "")),
                        str(item.get("title", "")),
                        str(item.get("state", "")),
                        str(item.get("confidence", "")),
                    ]
                )
            )
    else:
        lines.append(row(["", "", "", ""]))

    lines.extend(
        [
            "",
            "## Needs Human Review",
            "",
            "| ID | Question | Options | Suggested Decision |",
            "|----|----------|---------|--------------------|",
        ]
    )
    if review_needed:
        for item in review_needed:
            lines.append(
                row(
                    [
                        str(item.get("id", "")),
                        "Resolve candidate state or metadata conflict",
                        "promote / reject / keep candidate",
                        "keep candidate until reviewed",
                    ]
                )
            )
    else:
        lines.append(row(["", "", "", ""]))

    lines.extend(
        [
            "",
            "## Benchmark Updates",
            "",
            "| Benchmark ID | System | Observable | Status Change | Code Impact |",
            "|--------------|--------|------------|---------------|-------------|",
        ]
    )
    for item in benchmarks:
        lines.append(
            row(
                [
                    str(item.get("id", "")),
                    str(item.get("system", "")),
                    str(item.get("observable", "")),
                    str(item.get("status", "")),
                    str(item.get("target_phase", "")),
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Risk Updates",
            "",
            "| Risk ID | Claim | Evidence | Project Impact |",
            "|---------|-------|----------|----------------|",
        ]
    )
    for item in risks:
        lines.append(
            row(
                [
                    str(item.get("id", "")),
                    str(item.get("claim", "")),
                    str(item.get("evidence", "")),
                    str(item.get("project_impact", "")),
                ]
            )
        )

    lines.extend(
        [
            "",
            "## SW Code Context Candidates",
            "",
            "| Claim | Source ID | Target Phase | Target Module |",
            "|-------|-----------|--------------|---------------|",
            row(["", "", "", ""]),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Packet date in YYYY-MM-DD format.",
    )
    args = parser.parse_args()
    packet_date = date.fromisoformat(args.date)
    path = generate_packet(packet_date)
    print(f"Review packet written: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
