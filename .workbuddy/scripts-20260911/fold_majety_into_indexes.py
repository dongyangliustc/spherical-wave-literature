#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold Majety 2015 (newly supplied fulltext) into the three derived indexes and
retire the two-ghost appendix. Exact/regex anchors with assertions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(r"D:\WORK\workbuddy\spherical_wave_literature")
README = ROOT / "index" / "README.md"
TOPIC = ROOT / "index" / "by_topic.md"
REL = ROOT / "index" / "by_relevance.md"

JOBS: list[tuple[Path, str, str, str, bool]] = []  # (path, old, new, tag, is_regex)


def sub(path: Path, pat: str, new: str, tag: str) -> None:
    JOBS.append((path, pat, new, tag, True))


def lit(path: Path, old: str, new: str, tag: str) -> None:
    JOBS.append((path, old, new, tag, False))


# ─────────────────────────── by_topic.md ───────────────────────────
lit(TOPIC,
    "> 数据源：`registry/core.yaml`（6）+ `registry/candidates.yaml`（63）→ 全文可用 **67 篇**；另 2 条 `state: discovered`（无 PDF，见文末附录）。",
    "> 数据源：`registry/core.yaml`（6）+ `registry/candidates.yaml`（63）→ 全文可用 **68 篇**；另 1 条 `state: paywalled`（书章，暂缓获取，见文末附录）。",
    "T-header")

lit(TOPIC, "| T4 | 连续态表示层增强 | 7 |", "| T4 | 连续态表示层增强 | 8 |", "T-count")

lit(TOPIC, "## T4 · 连续态表示层增强（7 篇）", "## T4 · 连续态表示层增强（8 篇）", "T4-hdr")

sub(TOPIC,
    r"^(\| ⭐⭐⭐\s+\| Ammar, Ancarani, Leclerc \(2021\).*)$",
    r"\1\n| ⭐⭐⭐ | Majety, Zielinski, Scrinzi (2015) — New J. Phys. | 量子化学高斯 CI 核 × 有限元/球谐单中心活性电子基的**反对称化耦合通道**混合表示（tSURFF 提取谱） | `continuum_wave`、`angular_reduction`、`method_comparison` |",
    "T4-row")

lit(TOPIC,
    "## 附：待下载（`state: discovered`，2 条 · 均无 PDF，不参与星级分级）\n\n### A. 本次反向核实发现（2 条，原仅存在于 2026-07-22 手写清单）\n\n| 文献 | 出处 | DOI | 可得性 |\n|---|---|---|---|\n| Cacelli, Carravetta, Rizzo, Moccia (1990) — \"Continuum by L2 Methods: Molecular Photoionization Cross Section\" | MOTECC-90，Springer 书章，pp. 639-691 | 10.1007/978-94-009-2219-8_12 | 书章，全文可获取性待评估 |\n| Majety, Zielinski, Scrinzi (2015) — \"Photoionization of few electron systems: a hybrid coupled channels approach\" | New J. Phys. 17(6), 063002 | 10.1088/1367-2630/17/6/063002 | OA（IOP），可下载 |",
    "## 附：未纳入分级的条目（1 条 · `state: paywalled`，暂缓获取）\n\n### 旧版遗留\"幽灵条目\"（原仅存在于 2026-07-22 手写清单，2026-09-11 反向核实后登记）\n\n| 文献 | 出处 | DOI | 处置 |\n|---|---|---|---|\n| Cacelli, Carravetta, Rizzo, Moccia (1990) — \"Continuum by L2 Methods: Molecular Photoionization Cross Section\" | MOTECC-90，Springer 书章，pp. 639-691 | 10.1007/978-94-009-2219-8_12 | **暂缓**：DY 2026-09-11 确认无法获取全文（书章付费墙、馆藏无）→ `state: paywalled`，不阻塞主线 |",
    "T-appendix")

lit(TOPIC,
    "### B. 并行调研新增（10 条）—— 已结清\n\n原\"Dyson 轨道方法调研\"10 条（MCDE / 时域 EKT / 相对论 EOM-CC）已于 2026-09-11 补齐全文、升级为 `fulltext_available` 并完成定级，归入正文 **T12**，不再列为待下载。",
    "### 已结清的待下载批次\n\n- **Dyson 轨道方法调研 10 条**（MCDE / 时域 EKT / 相对论 EOM-CC）：2026-09-11 补齐全文、定级、并入正文 **T12**。\n- **Majety, Zielinski, Scrinzi (2015)**：2026-09-11 由 DY 提供全文，落位 `papers/GTO_continuum/`，并入正文 **T4**（⭐⭐⭐）。",
    "T-appendixB")

# ─────────────────────────── by_relevance.md ───────────────────────────
lit(REL,
    "> **范围**：67 篇（全文可用，参与分级）。另 2 条 `state: discovered`（无 PDF）不参与分级，见 `by_topic.md` 附录。",
    "> **范围**：68 篇（全文可用，参与分级）。另 1 条 `state: paywalled`（书章，暂缓获取）不参与分级，见 `by_topic.md` 附录。",
    "V-header")

lit(REL,
    "| ⭐⭐⭐ | 弱耦合：特定专题或平行路线的实现细节，定向查阅 | 32 |",
    "| ⭐⭐⭐ | 弱耦合：特定专题或平行路线的实现细节，定向查阅 | 33 |",
    "V-tier")

lit(REL, "## ⭐⭐⭐ 专题与扩展（32 篇）", "## ⭐⭐⭐ 专题与扩展（33 篇）", "V3-hdr")

sub(REL,
    r"^(\| Ammar, Ancarani, Leclerc \(2021\) \| J\. Comput\. Chem\. \|.*)$",
    r"\1\n| Majety, Zielinski, Scrinzi (2015) | New J. Phys. | 量子化学芯 + 有限元/球谐单中心活性电子基的反对称化耦合通道（tSURFF）；单中心展开与多通道构造思路可借鉴 |",
    "V3-row")

lit(REL,
    "## 附：未参与分级的待下载条目（2 条，`state: discovered`）\n\n### 旧版遗留的两个\"幽灵条目\"（2026-09-11 反向核实后登记）\n\n`README.md` 明细表曾列入但从未落地（无 registry、无 PDF）：\n\n| 文献 | 出处 | 处置 |\n|---|---|---|\n| Cacelli, Carravetta, Rizzo, Moccia (1990) | MOTECC-90，Springer 书章 pp. 639-691 | 已登记；书章全文可获取性待评估 |\n| Majety, Zielinski, Scrinzi (2015) | New J. Phys. 17(6), 063002 | 已登记；OA 可下载 |",
    "## 附：未参与分级的条目（1 条，`state: paywalled`）\n\n### 旧版遗留的\"幽灵条目\"（2026-09-11 反向核实后登记）\n\n`README.md` 明细表曾列入但从未落地（无 registry、无 PDF）：\n\n| 文献 | 出处 | 处置 |\n|---|---|---|\n| Cacelli, Carravetta, Rizzo, Moccia (1990) | MOTECC-90，Springer 书章 pp. 639-691 | **暂缓**：无法获取全文（付费墙，馆藏无）→ `state: paywalled`；若日后取得可直接升级 |\n| Majety, Zielinski, Scrinzi (2015) | New J. Phys. 17(6), 063002 | ✅ 2026-09-11 取得全文 → **T4，⭐⭐⭐** |",
    "V-appendix")

lit(REL,
    "### B. 并行调研新增的 10 条 —— 已结清\n\n来源 `outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`：MCDE / 时域 EKT / 相对论 EOM-CC 三类。2026-09-11 已补齐全文（`papers/Dyson_orbital/`）并完成定级：**⭐⭐⭐⭐ 2 篇（Schio、Keizer）· ⭐⭐⭐ 5 篇 · ⭐⭐ 3 篇**，归入 `by_topic.md` **T12**。\n\n> 边界说明：本清单的 ⭐ 分级**只覆盖有全文的 67 篇**。无全文条目先补文献、再定级，避免\"凭摘要定优先级\"。",
    "### 已结清的两批\n\n- **Dyson 轨道方法调研 10 条**（MCDE / 时域 EKT / 相对论 EOM-CC）：2026-09-11 补齐全文（`papers/Dyson_orbital/`）并定级 **⭐⭐⭐⭐ 2（Schio、Keizer）· ⭐⭐⭐ 5 · ⭐⭐ 3**，归入 `by_topic.md` **T12**。\n- **Majety, Zielinski, Scrinzi (2015)**：2026-09-11 由 DY 提供全文，归入 **T4**（⭐⭐⭐）。\n\n> 边界说明：本清单的 ⭐ 分级**只覆盖有全文的 68 篇**。无全文条目先补文献、再定级，避免\"凭摘要定优先级\"。",
    "V-appendixB")

# ─────────────────────────── README.md ───────────────────────────
lit(README,
    "> 目录结构最近同步：2026-09-11（对齐实际文件树，67 篇；论文明细表同步完成）",
    "> 目录结构最近同步：2026-09-11（对齐实际文件树，68 篇；论文明细表同步完成）",
    "R-sync")

lit(README,
    "├── papers/                     ← PDF 按主题子目录存放（67 篇）",
    "├── papers/                     ← PDF 按主题子目录存放（68 篇）",
    "R-count")

lit(README,
    "│   ├── GTO_continuum/          ← GTO 连续态方法（Cacelli-Moccia-Rizzo 系列 + 递归积分）【13】",
    "│   ├── GTO_continuum/          ← GTO 连续态方法（Cacelli-Moccia-Rizzo 系列 + 递归积分）【14】",
    "R-gto")

sub(README,
    r"^(\|  \| Ammar et al\. \| 2021 \| J\. Comput\. Chem\. \|.*)$",
    r"\1\n|  | Majety et al. | 2015 | New J. Phys. | `Majety_2015_hybrid_coupled_channels_NJP.pdf` |",
    "R-row")

lit(README,
    "**分布**：⭐⭐⭐⭐⭐ 6 · ⭐⭐⭐⭐ 18 · ⭐⭐⭐ 32 · ⭐⭐ 11 = **67 篇**（全文可用）。",
    "**分布**：⭐⭐⭐⭐⭐ 6 · ⭐⭐⭐⭐ 18 · ⭐⭐⭐ 33 · ⭐⭐ 11 = **68 篇**（全文可用）。",
    "R-dist")

lit(README,
    "### 待下载（`state: discovered`，2 条 · 均无 PDF）\n\n**A. 本次反向核实发现（2 条）** —— 原仅存在于 2026-07-22 手写清单，从未落地：\n\n| 文献 | 出处 | DOI |\n|---|---|---|\n| Cacelli, Carravetta, Rizzo, Moccia | MOTECC-90（Springer 书章，pp. 639-691） | 10.1007/978-94-009-2219-8_12 |\n| Majety, Zielinski, Scrinzi | New J. Phys. 17(6), 063002（OA） | 10.1088/1367-2630/17/6/063002 |",
    "### 待下载 / 暂缓获取（原 2 条\"幽灵条目\"，均已结清处置）\n\n原仅存在于 2026-07-22 手写清单、从未落地的 2 条，2026-09-11 反向核实后登记，现已各有处置：\n\n| 文献 | 出处 | DOI | 处置 |\n|---|---|---|---|\n| Majety, Zielinski, Scrinzi | New J. Phys. 17(6), 063002（OA） | 10.1088/1367-2630/17/6/063002 | ✅ 取得全文 → `GTO_continuum/`，T4 ⭐⭐⭐ |\n| Cacelli, Carravetta, Rizzo, Moccia | MOTECC-90（Springer 书章，pp. 639-691） | 10.1007/978-94-009-2219-8_12 | ⏸ **暂缓**：付费墙、馆藏无 → `state: paywalled` |",
    "R-pending")

lit(README,
    "> **2026-09-11 状态**：三方一致（`papers/` 67 篇 = registry `paths.pdf` 67 = `sources.yaml` 67），由 `tools/check_three_way.py` 核对（PASS）。\n> 已完成全量元数据核实（Crossref/arXiv），纠正 5 篇名实不符、迁移 2 篇主题错位、补下载 2 篇缺失全文（Ota 2021、Hazi 1978），\n> 并于 2026-09-11 采纳 Dyson 轨道方法调研 10 条（补全全文 + 定级 + 三方对齐）。\n> 清退 `papers/scansci_test/` 测试残留。另有 2 篇待下载（见上，均为 `state: discovered`）。",
    "> **2026-09-11 状态**：三方一致（`papers/` 68 篇 = registry `paths.pdf` 68 = `sources.yaml` 68），由 `tools/check_three_way.py` 核对（PASS）。\n> 已完成全量元数据核实（Crossref/arXiv），纠正 5 篇名实不符、迁移 2 篇主题错位、补下载 2 篇缺失全文（Ota 2021、Hazi 1978），\n> 采纳 Dyson 轨道方法调研 10 条（补全全文 + 定级 + 三方对齐），并由 DY 提供 Majety 2015 全文补入 `GTO_continuum/`。\n> 清退 `papers/scansci_test/` 测试残留。2 条\"幽灵条目\"已全部结清：1 条取得、1 条 `state: paywalled` 暂缓。",
    "R-status")


def main() -> int:
    by_file: dict[Path, list[tuple[str, str, str, bool]]] = {}
    for path, old, new, tag, is_re in JOBS:
        by_file.setdefault(path, []).append((old, new, tag, is_re))

    failures: list[str] = []
    for path, jobs in by_file.items():
        text = path.read_text(encoding="utf-8")
        for old, new, tag, is_re in jobs:
            if is_re:
                newtext, n = re.subn(old, new, text, count=1, flags=re.M)
            else:
                n = text.count(old)
                newtext = text.replace(old, new, 1) if n >= 1 else text
            if n != 1:
                failures.append(f"{path.name} [{tag}]: matched {n} times (expected 1)")
                continue
            text = newtext
            print(f"  OK  {path.name}  {tag}")
        path.write_text(text, encoding="utf-8")

    if failures:
        print("\nFAILURES:", file=sys.stderr)
        for f in failures:
            print("  " + f, file=sys.stderr)
        return 1
    print("\nAll edits applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
