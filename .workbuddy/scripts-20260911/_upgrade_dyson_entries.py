#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulk-upgrade the 10 Dyson_orbital entries in candidates.yaml.

Sets identifiers/paths/state/confidence/review_status/actionability and adds a
metadata_note recording venue provenance. Idempotent (safe to re-run).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REG = Path(r"D:\WORK\workbuddy\spherical_wave_literature\index\registry\candidates.yaml")

# id -> (pdf_basename, doi, arxiv, actionability, venue_note)
UPDATES = {
    "lit-keizer-2026-mcde-adc-benchmark": (
        "Keizer_2026_MCDE_ADC_benchmark_arXiv.pdf",
        None,
        "2608.25669",
        "direct_benchmark",
        "arXiv:2608.25669 (preprint, 2026-08; MCDE vs ADC/nD-ADC(3) benchmark, no journal DOI yet at fetch time)",
    ),
    "lit-paggi-2026-mcde-photoemission": (
        "Paggi_2026_MCDE_photoemission_arXiv.pdf",
        None,
        "2607.20070",
        "reading_candidate",
        "arXiv:2607.20070 (preprint, 2026-07; core+valence photoemission from MCDE)",
    ),
    "lit-sellie-2026-mcde-double-ionization": (
        "Sellie_2026_MCDE_double_ionization_PRB_arXiv.pdf",
        "10.1103/jcfy-vdm8",
        "2604.01085",
        "reading_candidate",
        "Phys. Rev. B 114(12), 2026-08-19 (APS new-style DOI); PDF = arXiv:2604.01085 preprint",
    ),
    "lit-romaniello-2026-screened-mcde": (
        "Romaniello_2026_screened_MCDE_arXiv.pdf",
        None,
        "2603.27329",
        "reading_candidate",
        "arXiv:2603.27329 (preprint, 2026-03; screened MCDE, bulk Si plasmon satellite)",
    ),
    "lit-zhang-2026-time-dependent-dyson-eom": (
        "Zhang_2026_time_dependent_Dyson_EKT_PRL_arXiv.pdf",
        "10.1103/dcdw-ly16",
        "2505.11290",
        "risk_update",
        "Phys. Rev. Lett. 136(1), 2026-01-08 (APS new-style DOI); PDF = arXiv:2505.11290 preprint",
    ),
    "lit-thapa-2026-relativistic-eomcc-triples": (
        "Thapa_2026_relativistic_EOMCC_triples_arXiv.pdf",
        None,
        "2602.21834",
        "reading_candidate",
        "arXiv:2602.21834 (preprint, 2026-02; relativistic EOM-CC with three-body corrections)",
    ),
    "lit-yuwono-2025-two-component-relativistic-eomcc": (
        "Yuwono_2025_relativistic_EOMCC_ionization_JCP.pdf",
        "10.1063/5.0248535",
        None,
        "reading_candidate",
        "J. Chem. Phys. 162(8), 2025-02-28",
    ),
    "lit-schio-2026-cooper-minimum-dyson-orbitals": (
        "Schio_2026_Cooper_minimum_Dyson_orbitals_JCP_arXiv.pdf",
        "10.1063/5.0333577",
        "2602.23223",
        "formula_reference",
        "J. Chem. Phys. 164, 204301 (2026); PDF = arXiv:2602.23223 preprint. DOI resolved via Crossref title search (registry previously had doi=null).",
    ),
    "lit-misael-2024-cvs-eomcc-actinide": (
        "Misael_2024_CVS_EOMCC_actinide_arXiv.pdf",
        None,
        "2412.08403",
        "reading_candidate",
        "arXiv:2412.08403 (preprint, 2024-12; CVS-EOM-CC core ionization of uranyl in Cs2UO2Cl4)",
    ),
    "lit-mukhopadhyay-2026-relativistic-dip-eomcc": (
        "Mukhopadhyay_2026_relativistic_DIP_EOMCC_JCTC.pdf",
        "10.1021/acs.jctc.5c01791",
        None,
        "reading_candidate",
        "J. Chem. Theory Comput. 22, 3233-3246 (2026). DOI resolved via Crossref title search (registry previously had doi=null and arxiv=null).",
    ),
}


def q(value: str | None) -> str:
    return "null" if value in (None, "") else f'"{value}"'


def main() -> int:
    text = REG.read_text(encoding="utf-8")
    lines = text.split("\n")
    out: list[str] = []
    current_id: str | None = None
    touched: dict[str, int] = {k: 0 for k in UPDATES}
    note_inserted = False

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^  - id:\s*"([^"]+)"\s*$', line)
        if m:
            current_id = m.group(1)
            note_inserted = False
            out.append(line)
            i += 1
            continue

        upd = UPDATES.get(current_id) if current_id else None
        if upd is None:
            out.append(line)
            i += 1
            continue

        pdf, doi, arxiv, actionability, note = upd

        if re.match(r"^\s+pdf:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}pdf: \"papers/Dyson_orbital/{pdf}\"")
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+doi:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}doi: {q(doi)}")
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+arxiv:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}arxiv: {q(arxiv)}")
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+state:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f'{indent}state: "fulltext_available"')
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+review_status:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f'{indent}review_status: "machine_screened"')
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+confidence:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f'{indent}confidence: "fulltext_available"')
            touched[current_id] += 1
            i += 1
            continue

        if re.match(r"^\s+actionability:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f'{indent}actionability: "{actionability}"')
            touched[current_id] += 1
            i += 1
            continue

        # insert metadata_note right after the year line
        if re.match(r"^\s+year:\s*", line) and not note_inserted:
            indent = line[: len(line) - len(line.lstrip())]
            out.append(line)
            out.append(f'{indent}metadata_note: "{note}"')
            touched[current_id] += 1
            note_inserted = True
            i += 1
            continue

        if re.match(r"^\s+metadata_note:\s*", line):
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f'{indent}metadata_note: "{note}"')
            note_inserted = True
            i += 1
            continue

        out.append(line)
        i += 1

    problems = [k for k, v in touched.items() if v < 8]
    if problems:
        print("WARNING: low replacement count for:", problems, file=sys.stderr)
        for k in problems:
            print(f"  {k}: {touched[k]} fields", file=sys.stderr)

    REG.write_text("\n".join(out), encoding="utf-8")
    print("Updated entries:", len(UPDATES))
    for k, v in touched.items():
        print(f"  {k}: {v} fields set")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
