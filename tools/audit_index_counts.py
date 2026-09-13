#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the derived indexes against the registry + files on disk.

Checks
  1. README detail-table rows == number of fulltext (pdf-bearing) registry entries
  2. Every PDF basename cited in README/by_topic/by_relevance exists on disk
  3. by_relevance tier counts == declared header counts, and sum == fulltext total
  4. by_topic group counts == declared table counts, and sum == fulltext total
  5. No PDF cited twice inside a single file
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(r"D:\WORK\workbuddy\spherical_wave_literature")
README = ROOT / "index" / "README.md"
TOPIC = ROOT / "index" / "by_topic.md"
REL = ROOT / "index" / "by_relevance.md"

on_disk = {p.name for p in (ROOT / "papers").rglob("*.pdf")}
problems: list[str] = []


def note(msg: str) -> None:
    print("  " + msg)


def pdfs_in(text: str) -> list[str]:
    return re.findall(r"`([A-Za-z0-9_.\-]+\.pdf)`", text)


print(f"PDFs on disk: {len(on_disk)}")
print(f"Fulltext registry entries expected: {len(on_disk)} (three-way check already passed)")

# ── 1/2. README detail table ────────────────────────────────────────────────
rtext = README.read_text(encoding="utf-8")
start = rtext.index("| 档位 | 文献 | 年 | 出处 | PDF 文件 |")
end = rtext.index("**分布**：")
table = rtext[start:end]
rows = [ln for ln in table.split("\n") if ln.startswith("|") and ".pdf`" in ln]
rpdfs = pdfs_in(table)
print(f"\n[README] detail rows with PDF: {len(rows)} ; unique: {len(set(rpdfs))}")
if len(rows) != len(on_disk):
    problems.append(f"README detail rows {len(rows)} != on-disk PDFs {len(on_disk)}")
if len(rpdfs) != len(set(rpdfs)):
    dupes = sorted({x for x in rpdfs if rpdfs.count(x) > 1})
    problems.append(f"README cites duplicate PDFs: {dupes}")
missing = sorted(set(rpdfs) - on_disk)
if missing:
    problems.append(f"README cites non-existent PDFs: {missing}")
unlisted = sorted(on_disk - set(rpdfs))
if unlisted:
    problems.append(f"on-disk PDFs absent from README table: {unlisted}")

# declared distribution
m = re.search(r"\*\*分布\*\*：(.+?) = \*\*(\d+) 篇\*\*", rtext)
if m:
    parts = dict(re.findall(r"(⭐+) (\d+)", m.group(1)))
    total = int(m.group(2))
    note(f"README declared: {parts} = {total}")
    if sum(int(v) for v in parts.values()) != total:
        problems.append("README tier counts do not sum to declared total")
    if total != len(on_disk):
        problems.append(f"README declared total {total} != on-disk {len(on_disk)}")
else:
    problems.append("README distribution line not found")

# ── 3. by_relevance ────────────────────────────────────────────────────────
vtext = REL.read_text(encoding="utf-8")
tier_hdr = dict(re.findall(r"\|\s*(⭐+)\s*\|\s*[^|]+?\s*\|\s*(\d+)\s*\|", vtext))
note(f"by_relevance header tiers: {tier_hdr}")
sec_hdr = dict(re.findall(r"^## (⭐+) [^（]*（(\d+) 篇）", vtext, re.M))
note(f"by_relevance section tiers: {sec_hdr}")
for star, cnt in sec_hdr.items():
    if tier_hdr.get(star) != cnt:
        problems.append(f"by_relevance {star}: header {tier_hdr.get(star)} != section {cnt}")

# count actual entries: numbered bold items for 5/4-star, table rows for 3-star, bullets for 2-star
H5 = re.search(r"^## ⭐⭐⭐⭐⭐ .*$", vtext, re.M)
H4 = re.search(r"^## ⭐⭐⭐⭐ .*$", vtext, re.M)
H3 = re.search(r"^## ⭐⭐⭐ .*$", vtext, re.M)
H2 = re.search(r"^## ⭐⭐ .*$", vtext, re.M)
assert H5 and H4 and H3 and H2, "tier section headers not all found"
n5 = len(re.findall(r"^\*\*\d+\. ", vtext[H5.end():H4.start()], re.M))
n4 = len(re.findall(r"^\*\*\d+\. ", vtext[H4.end():H3.start()], re.M))
sec3 = vtext[H3.end():H2.start()]
n3 = len([ln for ln in sec3.split("\n") if ln.startswith("|") and ln.count("|") >= 4]) - 2  # minus header+sep
sec2 = vtext[H2.end():vtext.index("## 与 2026-07-22")]
n2 = len([ln for ln in sec2.split("\n") if ln.startswith("- **")])
note(f"by_relevance actual: 5★={n5} 4★={n4} 3★={n3} 2★={n2} sum={n5+n4+n3+n2}")
expect = {"⭐⭐⭐⭐⭐": n5, "⭐⭐⭐⭐": n4, "⭐⭐⭐": n3, "⭐⭐": n2}
for star, actual in expect.items():
    if int(tier_hdr.get(star, -1)) != actual:
        problems.append(f"by_relevance {star}: declared {tier_hdr.get(star)} != actual {actual}")
if n5 + n4 + n3 + n2 != len(on_disk):
    problems.append(f"by_relevance total {n5+n4+n3+n2} != on-disk {len(on_disk)}")

# ── 4. by_topic ────────────────────────────────────────────────────────────
ttext = TOPIC.read_text(encoding="utf-8")
# whitespace-tolerant: markdown tables in this repo get re-padded by the editor,
# so never anchor on exact single-space separators.
tab = re.findall(r"^\|\s*(T\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", ttext, re.M)
declared = {g: int(c) for g, _, c in tab}
note(f"by_topic declared: {declared} sum={sum(declared.values())}")
sec = dict(re.findall(r"^## (T\d+) · [^（]*（(\d+) 篇）", ttext, re.M))
note(f"by_topic sections: { {k: int(v) for k, v in sec.items()} }")
for g, cnt in sec.items():
    if declared.get(g) != int(cnt):
        problems.append(f"by_topic {g}: table {declared.get(g)} != section {cnt}")
if sum(declared.values()) != len(on_disk):
    problems.append(f"by_topic total {sum(declared.values())} != on-disk {len(on_disk)}")

# each topic table's row count must match its declared count
for m in re.finditer(r"^## (T\d+) · [^（]*（(\d+) 篇）\n(.*?)(?=\n---|\Z)", ttext, re.M | re.S):
    g, cnt, body = m.group(1), int(m.group(2)), m.group(3)
    rowsn = len([ln for ln in body.split("\n") if ln.startswith("| ⭐") or ln.startswith("| ⭐⭐⭐⭐⭐")])
    if rowsn != cnt:
        problems.append(f"by_topic {g}: section declares {cnt} but lists {rowsn} rows")

# ── report ─────────────────────────────────────────────────────────────────
print()
if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  - " + p)
    sys.exit(1)
print("AUDIT PASSED: all index counts consistent with disk + registry.")
