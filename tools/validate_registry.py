#!/usr/bin/env python3
"""Validate the literature registry files without third-party YAML deps."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = REPO_ROOT / "index" / "registry"

LITERATURE_REQUIRED = {
    "id",
    "title",
    "authors",
    "year",
    "source_type",
    "state",
    "review_status",
    "relevance",
    "role",
    "confidence",
    "actionability",
}

BENCHMARK_REQUIRED = {
    "id",
    "literature_id",
    "system",
    "observable",
    "data_availability",
    "source_location",
    "target_phase",
    "status",
}

RISK_REQUIRED = {
    "id",
    "claim",
    "evidence",
    "project_impact",
    "status",
}

ENUMS = {
    "source_type": {
        "paper",
        "review",
        "book",
        "chapter",
        "dataset",
        "software",
        "thesis",
    },
    "state": {
        "discovered",
        "metadata_verified",
        "abstract_screened",
        "fulltext_available",
        "extracted",
        "reviewed",
        "indexed",
        "injected_to_code_context",
        "duplicate",
        "out_of_scope",
        "paywalled",
        "metadata_conflict",
        "low_quality",
        "needs_human_review",
    },
    "review_status": {
        "unreviewed",
        "machine_screened",
        "human_review_needed",
        "reviewed",
        "rejected",
    },
    "relevance": {"core", "high", "medium", "low"},
    "role": {
        "foundation",
        "method_origin",
        "method_comparison",
        "benchmark",
        "code_reference",
        "review",
        "frontier",
        "risk_evidence",
        "historical_context",
    },
    "confidence": {
        "metadata_only",
        "abstract_only",
        "fulltext_available",
        "fulltext_extracted",
        "fulltext_or_primary_index",
        "benchmark_verified",
    },
    "actionability": {
        "none",
        "reading_candidate",
        "formula_reference",
        "implementation_guidance",
        "direct_benchmark",
        "risk_update",
        "code_context_candidate",
    },
    "observable": {
        "total_cross_section",
        "differential_cross_section",
        "beta_parameter",
        "phase_shift",
        "partial_wave_cross_section",
        "MFPAD",
        "time_delay",
        "matrix_element",
    },
    "data_availability": {
        "table",
        "figure_digitizable",
        "raw_data",
        "text_only",
        "not_available",
    },
    "status": {
        "candidate",
        "digitized",
        "unit_checked",
        "ready_for_gate",
        "used_in_gate",
        "rejected",
        "active",
        "mitigated",
    },
}


def strip_comment(line: str) -> str:
    in_quote = False
    quote_char = ""
    for idx, char in enumerate(line):
        if char in {"'", '"'} and (idx == 0 or line[idx - 1] != "\\"):
            if in_quote and char == quote_char:
                in_quote = False
                quote_char = ""
            elif not in_quote:
                in_quote = True
                quote_char = char
        if char == "#" and not in_quote:
            return line[:idx]
    return line


def parse_scalar(value: str):
    value = value.strip()
    if value in {"null", "None", ""}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if re.fullmatch(r"\d{4}", value):
        return int(value)
    return value


def parse_registry(path: Path, top_key: str) -> list[dict]:
    records: list[dict] = []
    current: dict | None = None
    in_top_key = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = strip_comment(raw_line).rstrip()
        if not line.strip():
            continue
        if line.startswith(f"{top_key}:"):
            in_top_key = True
            if line.strip() == f"{top_key}: []":
                return []
            continue
        if not in_top_key:
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if current is not None:
                records.append(current)
            current = {}
            stripped = stripped[2:].strip()
            if stripped:
                key, value = split_field(stripped, path)
                current[key] = parse_scalar(value)
            continue
        if current is None:
            continue
        if ":" in stripped and not stripped.endswith(":"):
            key, value = split_field(stripped, path)
            current[key] = parse_scalar(value)

    if current is not None:
        records.append(current)
    return records


def split_field(text: str, path: Path) -> tuple[str, str]:
    if ":" not in text:
        raise ValueError(f"{path}: invalid field line: {text}")
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def validate_records(
    records: list[dict],
    required: set[str],
    seen_ids: set[str],
    seen_identifiers: dict[str, str],
    label: str,
) -> list[str]:
    errors: list[str] = []
    for index, record in enumerate(records, start=1):
        record_id = record.get("id")
        if not record_id:
            errors.append(f"{label}[{index}] missing id")
        elif record_id in seen_ids:
            errors.append(f"duplicate id: {record_id}")
        else:
            seen_ids.add(str(record_id))

        missing = sorted(required - set(record))
        if missing:
            errors.append(f"{label}[{record_id or index}] missing fields: {', '.join(missing)}")

        for field, allowed in ENUMS.items():
            if field not in record:
                continue
            value = record[field]
            values = value if isinstance(value, list) else [value]
            for item in values:
                if item is not None and item not in allowed:
                    errors.append(
                        f"{label}[{record_id or index}] invalid {field}: {item}"
                    )
        errors.extend(validate_unique_identifiers(record, seen_identifiers, label))
    return errors


def validate_unique_identifiers(
    record: dict, seen_identifiers: dict[str, str], label: str
) -> list[str]:
    errors: list[str] = []
    record_id = str(record.get("id") or "<missing-id>")
    for field in ("doi", "arxiv", "isbn"):
        value = record.get(field)
        if value in {None, ""}:
            continue
        key = f"{field}:{str(value).strip().lower()}"
        owner = seen_identifiers.get(key)
        if owner is not None:
            errors.append(
                f"{label}[{record_id}] duplicate {field}: {value} already used by {owner}"
            )
        else:
            seen_identifiers[key] = record_id
    return errors


def validate(registry_dir: Path = REGISTRY_DIR) -> list[str]:
    seen_ids: set[str] = set()
    seen_identifiers: dict[str, str] = {}
    errors: list[str] = []

    literature_files = [
        (registry_dir / "candidates.yaml", "items"),
        (registry_dir / "core.yaml", "items"),
    ]
    for path, top_key in literature_files:
        errors.extend(
            validate_records(
                parse_registry(path, top_key),
                LITERATURE_REQUIRED,
                seen_ids,
                seen_identifiers,
                display_path(path),
            )
        )

    errors.extend(
        validate_records(
            parse_registry(registry_dir / "benchmarks.yaml", "benchmarks"),
            BENCHMARK_REQUIRED,
            seen_ids,
            seen_identifiers,
            "benchmarks",
        )
    )
    errors.extend(
        validate_records(
            parse_registry(registry_dir / "risks.yaml", "risks"),
            RISK_REQUIRED,
            seen_ids,
            seen_identifiers,
            "risks",
        )
    )
    return errors


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--registry-dir",
        type=Path,
        default=REGISTRY_DIR,
        help="Directory containing registry YAML files.",
    )
    args = parser.parse_args()

    errors = validate(args.registry_dir)
    if errors:
        print("Registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Registry validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
