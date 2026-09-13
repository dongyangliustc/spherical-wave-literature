#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the 10 newly-downloaded Dyson-orbital papers into the three derived indexes.

Touches: index/README.md, index/by_topic.md, index/by_relevance.md
All replacements are exact-substring with assertions, so a silent miss is impossible.
Run AFTER registry + sources.yaml are updated and the three-way check passes.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(r"D:\WORK\workbuddy\spherical_wave_literature")
README = ROOT / "index" / "README.md"
TOPIC = ROOT / "index" / "by_topic.md"
REL = ROOT / "index" / "by_relevance.md"

EDITS: list[tuple[Path, str, str, str]] = []


def edit(path: Path, old: str, new: str, tag: str) -> None:
    EDITS.append((path, old, new, tag))


# ─────────────────────────────── README.md ───────────────────────────────
edit(README,
     "> 目录结构最近同步：2026-09-11（对齐实际文件树，57 篇；论文明细表同步完成）",
     "> 目录结构最近同步：2026-09-11（对齐实际文件树，67 篇；论文明细表同步完成）",
     "R1 header")

edit(README,
     "├── papers/                     ← PDF 按主题子目录存放（57 篇）",
     "├── papers/                     ← PDF 按主题子目录存放（67 篇）",
     "R2 papers count")

edit(README,
     "│   ├── complex_scaling/        ← 复缩放与围道积分方法【1】\n│   └── general_review/         ← 综述与背景文献【8】",
     "│   ├── complex_scaling/        ← 复缩放与围道积分方法【1】\n"
     "│   ├── general_review/         ← 综述与背景文献【8】\n"
     "│   └── Dyson_orbital/          ← Dyson 轨道获取方法（MCDE / 时域 EKT / 相对论 EOM-CC）【10】",
     "R3 add Dyson dir")

edit(README,
     "├── tools/                      ← 主张抽取/锚定、registry 校验、审查包生成、内容推送",
     "├── tools/                      ← 主张抽取/锚定、registry 校验、三方一致性核对、审查包生成、内容推送",
     "R4 tools desc")

edit(README,
     "|  | Toffoli et al. | 2024 | Comput. Phys. Commun. | `Toffoli_2024_Tiresia_CPC.pdf` |\n",
     "|  | Toffoli et al. | 2024 | Comput. Phys. Commun. | `Toffoli_2024_Tiresia_CPC.pdf` |\n"
     "|  | Schio et al. | 2026 | J. Chem. Phys. | `Schio_2026_Cooper_minimum_Dyson_orbitals_JCP_arXiv.pdf` |\n"
     "|  | Keizer et al. | 2026 | arXiv:2608.25669 | `Keizer_2026_MCDE_ADC_benchmark_arXiv.pdf` |\n",
     "R5 add 2 four-star rows")

edit(README,
     "|  | Vanroose et al. | 2006 | Phys. Rev. A | `Vanroose_2006_H2_double_photoionization_PRA.pdf` |\n",
     "|  | Vanroose et al. | 2006 | Phys. Rev. A | `Vanroose_2006_H2_double_photoionization_PRA.pdf` |\n"
     "|  | Paggi et al. | 2026 | arXiv:2607.20070 | `Paggi_2026_MCDE_photoemission_arXiv.pdf` |\n"
     "|  | Romaniello & Berger | 2026 | arXiv:2603.27329 | `Romaniello_2026_screened_MCDE_arXiv.pdf` |\n"
     "|  | Zhang et al. | 2026 | Phys. Rev. Lett. | `Zhang_2026_time_dependent_Dyson_EKT_PRL_arXiv.pdf` |\n"
     "|  | Yuwono et al. | 2025 | J. Chem. Phys. | `Yuwono_2025_relativistic_EOMCC_ionization_JCP.pdf` |\n"
     "|  | Thapa & Dutta | 2026 | arXiv:2602.21834 | `Thapa_2026_relativistic_EOMCC_triples_arXiv.pdf` |\n",
     "R6 add 5 three-star rows")

edit(README,
     "|  | Asadova et al. | 2025 | J. Quant. Spectrosc. Radiat. Transf. | `Asadova_2025_Tmatrix_data_format_JQSRT.pdf` |\n",
     "|  | Asadova et al. | 2025 | J. Quant. Spectrosc. Radiat. Transf. | `Asadova_2025_Tmatrix_data_format_JQSRT.pdf` |\n"
     "|  | Sellié et al. | 2026 | Phys. Rev. B | `Sellie_2026_MCDE_double_ionization_PRB_arXiv.pdf` |\n"
     "|  | Misael & Gomes | 2024 | arXiv:2412.08403 | `Misael_2024_CVS_EOMCC_actinide_arXiv.pdf` |\n"
     "|  | Mukhopadhyay et al. | 2026 | J. Chem. Theory Comput. | `Mukhopadhyay_2026_relativistic_DIP_EOMCC_JCTC.pdf` |\n",
     "R7 add 3 two-star rows")

edit(README,
     "**分布**：⭐⭐⭐⭐⭐ 6 · ⭐⭐⭐⭐ 16 · ⭐⭐⭐ 27 · ⭐⭐ 8 = **57 篇**（全文可用）。",
     "**分布**：⭐⭐⭐⭐⭐ 6 · ⭐⭐⭐⭐ 18 · ⭐⭐⭐ 32 · ⭐⭐ 11 = **67 篇**（全文可用）。",
     "R8 distribution")

edit(README,
     "### 待下载（`state: discovered`，12 条 · 均无 PDF）",
     "### 待下载（`state: discovered`，2 条 · 均无 PDF）",
     "R9 pending header")

edit(README,
     """**B. 并行调研新增（10 条）** —— 2026-09-11 11:01 由 Dyson 轨道方法调研写入（MCDE / 时域 EKT / 相对论 EOM-CC）：

| 文献 | 年 | arXiv | relevance |
|---|---|---|---|
| Keizer, Paggi, Berger, Romaniello, Förster — MCDE 与 ADC 基准 | 2026 | 2608.25669 | high |
| Paggi, Berger, Romaniello — 多通道 Dyson 方程光发射谱 | 2026 | 2607.20070 | high |
| Sellie 等 — MCDE 双电离 | 2026 | — | medium |
| Romaniello 等 — 屏蔽 MCDE | 2026 | — | medium |
| Zhang 等 — 时域 Dyson 与 EOM | 2026 | — | high |
| Thapa 等 — 相对论 EOM-CC 三重激发 | 2026 | — | medium |
| Yuwono 等 — 双分量相对论 EOM-CC | 2025 | — | medium |
| Schio 等 — Cooper 极小 Dyson 轨道 | 2026 | — | high |
| Misael 等 — CVS-EOM-CC 锕系 | 2024 | — | low |
| Mukhopadhyay 等 — 相对论 DIP-EOM-CC | 2026 | — | low |

> 来源：`outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`。该 12 条均不参与上述星级分级（无全文）；下载后需补入。""",
     """**B. 并行调研新增（10 条）** —— 已于 2026-09-11 补齐全文（`papers/Dyson_orbital/`），升级为 `fulltext_available`
并纳入上述星级分级（⭐⭐⭐⭐ 2 / ⭐⭐⭐ 5 / ⭐⭐ 3），详见 `by_topic.md` **T12**。来源：`outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`。""",
     "R10 drop downloaded list")

edit(README,
     "> **2026-09-11 状态**：三方一致（`papers/` 57 篇 = registry `paths.pdf` 57 = `sources.yaml` 57）。\n"
     "> 已完成全量元数据核实（Crossref/arXiv），纠正 5 篇名实不符、迁移 2 篇主题错位、补下载 2 篇缺失全文（Ota 2021、Hazi 1978），\n"
     "> 清退 `papers/scansci_test/` 测试残留。另有 2 篇待下载（见上）。",
     "> **2026-09-11 状态**：三方一致（`papers/` 67 篇 = registry `paths.pdf` 67 = `sources.yaml` 67），"
     "由 `tools/check_three_way.py` 核对（PASS）。\n"
     "> 已完成全量元数据核实（Crossref/arXiv），纠正 5 篇名实不符、迁移 2 篇主题错位、补下载 2 篇缺失全文（Ota 2021、Hazi 1978），\n"
     "> 并于 2026-09-11 采纳 Dyson 轨道方法调研 10 条（补全全文 + 定级 + 三方对齐）。\n"
     "> 清退 `papers/scansci_test/` 测试残留。另有 2 篇待下载（见上，均为 `state: discovered`）。",
     "R11 download status")

# ─────────────────────────────── by_topic.md ───────────────────────────────
edit(TOPIC,
     "> 数据源：`registry/core.yaml`（6）+ `registry/candidates.yaml`（63）→ 全文可用 **57 篇**；另 12 条 `state: discovered`（无 PDF，见文末附录）。",
     "> 数据源：`registry/core.yaml`（6）+ `registry/candidates.yaml`（63）→ 全文可用 **67 篇**；另 2 条 `state: discovered`（无 PDF，见文末附录）。",
     "T1 header")

edit(TOPIC,
     "| T12 | 边缘与存档 | 4 |",
     "| T12 | Dyson 轨道与多体关联方法 | 10 |\n| T13 | 边缘与存档 | 4 |",
     "T2 count table")

DYSON_SECTION = """## T12 · Dyson 轨道与多体关联方法（10 篇）

**并行路线：Dyson 轨道从哪来。** 本项目的光电离截面需要 Dyson 轨道作为出发点；这一组是 2026 年三条新主线（多通道 Dyson 方程 MCDE、时域 Dyson / 扩展 Koopmans 定理、相对论 EOM-CC）的代表工作。

> **引用陷阱（勿踩）**：MCDE 家族的增益在**束缚态谱函数侧**，**不能**用于解决本项目 J.3.5 的连续态瓶颈（Born 谱范数 776.2）。MCDE 全部出自 Toulouse 单学派（Romaniello / Berger），无公开代码，验证限于小分子 + 体相 Si。
> **已被质疑的近似**：`nD-ADC(3)` ≠ `Dyson-ADC(3)`（差 ~0.1 eV，强关联 >0.25 eV）；引用 ADC(3) 精度须注明分支。
> **硬反证**：瞬时自然轨道**不能**替代 Dyson 轨道（PRL 136, 013204 (2026)，H⁻ 通道分辨 PMD 出假峰）。

| 星级 | 文献 | 方法贡献 | 对应本项目模块 |
|---|---|---|---|
| ⭐⭐⭐⭐ | Schio, Alagia, Moitra, Toffoli, Ponzi, Stener, Coriani, Decleva et al. (2026) — J. Chem. Phys. 164, 204301 | 环氧氯丙烷 Cooper 极小处轨道混合；**附左右 Dyson 轨道与 γ^L·γ^R 谱强度完整公式**，HF/DFT 无法解释的 β 振荡仅 EOM-CCSD Dyson 轨道可重现 | `frame_transform`、`momentum_gto`、`method_comparison` |
| ⭐⭐⭐⭐ | Keizer, Paggi, Berger, Romaniello, Förster (2026) — arXiv:2608.25669 | MCDE 与 ADC(3)/nD-ADC(3) 的系统基准（精度边界与分支差异） | `correlation_strategy`、`method_comparison`、`benchmark_strategy` |
| ⭐⭐⭐ | Paggi, Berger, Romaniello (2026) — arXiv:2607.20070 | MCDE 计算原子分子芯/价光发射谱（束缚态侧） | `correlation_strategy`、`method_comparison` |
| ⭐⭐⭐ | Romaniello, Berger (2026) — arXiv:2603.27329 | 屏蔽 MCDE：体相 Si 的 plasmon 卫星，MCDE 屏蔽处理起点 | `correlation_strategy`、`method_origin` |
| ⭐⭐⭐ | Zhang, Li, Pathak, Sato, Ishikawa, He (2026) — Phys. Rev. Lett. 136(1) | 时域扩展 Koopmans 定理（MCTDHF 空穴态）；"自然轨道替代 Dyson 轨道"的边界证据 | `correlation_strategy`、`continuum_wave` |
| ⭐⭐⭐ | Yuwono, Li, Zhang, Li, DePrince (2025) — J. Chem. Phys. 162(8) | 双分量相对论 EOM-CC 计算电子电离（3h2p、自旋轨道、X2C） | `correlation_strategy`、`method_comparison` |
| ⭐⭐⭐ | Thapa, Dutta (2026) — arXiv:2602.21834 | 相对论 EOM-CC 的三体修正（X2CAMF，MAE 0.01–0.08 eV） | `correlation_strategy`、`benchmark_strategy` |
| ⭐⭐ | Sellié, Berger, Romaniello (2026) — Phys. Rev. B 114(12) | MCDE 双电离谱（pp 通道耦合 3h1e/3e1h，Auger 方向） | `correlation_strategy`、`method_comparison` |
| ⭐⭐ | Misael, Gomes (2024) — arXiv:2412.08403 | 相对论嵌入式 CVS-EOM-CC 处理锕系芯电离态（Cs₂UO₂Cl₄ 铀酰） | `correlation_strategy`、`method_comparison` |
| ⭐⭐ | Mukhopadhyay, Mukherjee, Gururangan, Piecuch, Dutta (2026) — J. Chem. Theory Comput. 22, 3233 | 降成本四分量相对论 DIP-EOM-CC（4h2p + 三体簇） | `correlation_strategy` |

物理存放：`papers/Dyson_orbital/`（2026-09-11 补齐全文并三方对齐）。

---

## T13 · 边缘与存档（4 篇）"""

edit(TOPIC,
     "## T12 · 边缘与存档（4 篇）",
     DYSON_SECTION,
     "T3 insert T12 + rename T13")

edit(TOPIC,
     "## 附：待下载（`state: discovered`，12 条 · 均无 PDF，不参与星级分级）",
     "## 附：待下载（`state: discovered`，2 条 · 均无 PDF，不参与星级分级）",
     "T4 appendix header")

edit(TOPIC,
     """### B. 并行调研新增（10 条，2026-09-11 11:01 由 Dyson 轨道方法调研追加）

来源：`outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`（MCDE / 时域 EKT / 相对论 EOM-CC 三类，均为 2026 新主线）。

| 文献 | 年 | arXiv | registry relevance |
|---|---|---|---|
| Keizer, Paggi, Berger, Romaniello, Förster — MCDE 与 ADC 方法基准 | 2026 | 2608.25669 | high |
| Paggi, Berger, Romaniello — 多通道 Dyson 方程的芯/价光发射谱 | 2026 | 2607.20070 | high |
| Sellie 等 — MCDE 双电离 | 2026 | — | medium |
| Romaniello 等 — 屏蔽 MCDE | 2026 | — | medium |
| Zhang 等 — 时域 Dyson 与 EOM | 2026 | — | high |
| Thapa 等 — 相对论 EOM-CC 三重激发 | 2026 | — | medium |
| Yuwono 等 — 双分量相对论 EOM-CC | 2025 | — | medium |
| Schio 等 — Cooper 极小 Dyson 轨道 | 2026 | — | high |
| Misael 等 — CVS-EOM-CC 锕系元素 | 2024 | — | low |
| Mukhopadhyay 等 — 相对论 DIP-EOM-CC | 2026 | — | low |

> 该批条目由并行工作流写入 `candidates.yaml`，与本次索引重写无冲突（不影响 PDF 三方一致性）。待下载后需补入星级分级。""",
     """### B. 并行调研新增（10 条）—— 已结清

原"Dyson 轨道方法调研"10 条（MCDE / 时域 EKT / 相对论 EOM-CC）已于 2026-09-11 补齐全文、升级为 `fulltext_available` 并完成定级，归入正文 **T12**，不再列为待下载。""",
     "T5 appendix B")

# ─────────────────────────────── by_relevance.md ───────────────────────────────
edit(REL,
     "> **范围**：57 篇（全文可用，参与分级）。另 12 条 `state: discovered`（无 PDF）不参与分级，见 `by_topic.md` 附录。",
     "> **范围**：67 篇（全文可用，参与分级）。另 2 条 `state: discovered`（无 PDF）不参与分级，见 `by_topic.md` 附录。",
     "V1 header")

edit(REL,
     "| ⭐⭐⭐⭐ | 中耦合：能改变实现细节或架构选择，或需交叉验证的平行路线领头工作 | 16 |\n"
     "| ⭐⭐⭐ | 弱耦合：特定专题或平行路线的实现细节，定向查阅 | 27 |\n"
     "| ⭐⭐ | 无耦合：主题偏离，仅作概念/引用背景 | 8 |",
     "| ⭐⭐⭐⭐ | 中耦合：能改变实现细节或架构选择，或需交叉验证的平行路线领头工作 | 18 |\n"
     "| ⭐⭐⭐ | 弱耦合：特定专题或平行路线的实现细节，定向查阅 | 32 |\n"
     "| ⭐⭐ | 无耦合：主题偏离，仅作概念/引用背景 | 11 |",
     "V2 tier table")

edit(REL,
     "## ⭐⭐⭐⭐ 重要参考（16 篇）",
     "## ⭐⭐⭐⭐ 重要参考（18 篇）",
     "V3 four-star header")

edit(REL,
     """**22. Toffoli, Coriani, Stener, Decleva (2024)** — *Comput. Phys. Commun.*
→ Tiresia 代码：平行路线（B-spline）领头代码，交叉验证与叙事定位的主要对照
→ 注：DOI 后缀为 2023（注册年），出版年为 2024（CPC 297, 109038）

---""",
     """**22. Toffoli, Coriani, Stener, Decleva (2024)** — *Comput. Phys. Commun.*
→ Tiresia 代码：平行路线（B-spline）领头代码，交叉验证与叙事定位的主要对照
→ 注：DOI 后缀为 2023（注册年），出版年为 2024（CPC 297, 109038）

### Dyson 轨道与多体关联（2 篇）

**23. Schio, Alagia, Moitra, Toffoli, Ponzi, Stener, Coriani, Decleva et al. (2026)** — *J. Chem. Phys.* **164**, 204301
→ 手性分子（环氧氯丙烷）Cooper 极小处光电子动力学：HF/DFT 无法解释的 β 振荡，**仅 EOM-CCSD Dyson 轨道（同对称性单空穴组态混合）可重现**
→ **附左右 Dyson 轨道与谱强度 γ^L·γ^R 完整公式** —— Dyson 轨道侧与本项目同题的公式来源 + 直接可比对的 β 基准
→ 对应模块：`frame_transform`、`momentum_gto`、`method_comparison`
→ 注：registry 原 `doi: null`，2026-09-11 经 Crossref 题名检索补为 `10.1063/5.0333577`

**24. Keizer, Paggi, Berger, Romaniello, Förster (2026)** — *arXiv:2608.25669*
→ MCDE 与 ADC(3) / nD-ADC(3) 的系统基准：**引用 ADC(3) 精度时必须注明分支**（`nD-ADC(3)` ≠ `Dyson-ADC(3)`，差 ~0.1 eV，强关联 >0.25 eV）
→ **边界提示**：MCDE 家族的增益在束缚态谱函数侧，**不能**用于本项目的连续态瓶颈（Born 谱范数 776.2）
→ 对应模块：`correlation_strategy`、`method_comparison`、`benchmark_strategy`

---""",
     "V4 add 2 four-star")

edit(REL,
     "## ⭐⭐⭐ 专题与扩展（27 篇）",
     "## ⭐⭐⭐ 专题与扩展（32 篇）",
     "V5 three-star header")

edit(REL,
     "| Vanroose, Horner, Martín, Rescigno, McCurdy (2006) | PRA | H₂ 双电离 ECS 精确基准，H₂ 体系扩展参考 |\n",
     "| Vanroose, Horner, Martín, Rescigno, McCurdy (2006) | PRA | H₂ 双电离 ECS 精确基准，H₂ 体系扩展参考 |\n"
     "| Paggi, Berger, Romaniello (2026) | arXiv:2607.20070 | MCDE 芯/价光发射谱（束缚态侧），方法边界参照 |\n"
     "| Romaniello, Berger (2026) | arXiv:2603.27329 | 屏蔽 MCDE（体相 Si plasmon 卫星），MCDE 屏蔽起点 |\n"
     "| Zhang, Li, Pathak, Sato, Ishikawa, He (2026) | PRL 136(1) | 时域扩展 Koopmans 定理；**自然轨道不能替代 Dyson 轨道**的边界证据 |\n"
     "| Yuwono, Li, Zhang, Li, DePrince (2025) | JCP 162(8) | 双分量相对论 EOM-CC 电子电离，相对论化实现对照 |\n"
     "| Thapa, Dutta (2026) | arXiv:2602.21834 | 相对论 EOM-CC 三体修正，精度基准（MAE 0.01–0.08 eV） |\n",
     "V6 add 5 three-star rows")

edit(REL,
     "## ⭐⭐ 边缘与存档（8 篇）",
     "## ⭐⭐ 边缘与存档（11 篇）",
     "V7 two-star header")

edit(REL,
     "- **Asadova, Achouri, Arjas, Auguié, Aydin, Rockstuhl (2025)** — *JQSRT*，T 矩阵数据格式建议\n",
     "- **Asadova, Achouri, Arjas, Auguié, Aydin, Rockstuhl (2025)** — *JQSRT*，T 矩阵数据格式建议\n"
     "- **Sellié, Berger, Romaniello (2026)** — *Phys. Rev. B* 114(12)，MCDE 双电离谱（Auger 方向，与当前路线无耦合）\n"
     "- **Misael, Gomes (2024)** — *arXiv:2412.08403*，相对论嵌入式 CVS-EOM-CC 处理锕系芯电离（体系偏离）\n"
     "- **Mukhopadhyay, Mukherjee, Gururangan, Piecuch, Dutta (2026)** — *JCTC* 22, 3233，相对论 DIP-EOM-CC（双电离势，体系偏离）\n",
     "V8 add 3 two-star bullets")

edit(REL,
     "## 附：未参与分级的待下载条目（12 条，`state: discovered`）\n\n### A. 旧版遗留的两个\"幽灵条目\"（2026-09-11 反向核实后登记）",
     "## 附：未参与分级的待下载条目（2 条，`state: discovered`）\n\n### 旧版遗留的两个\"幽灵条目\"（2026-09-11 反向核实后登记）",
     "V9 appendix header")

edit(REL,
     """### B. 并行调研新增的 10 条（Dyson 轨道方法，2026-09-11 11:01 写入）

来源 `outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`：MCDE / 时域 EKT / 相对论 EOM-CC 三类，均为 2026 新主线。
按 registry 的 `relevance` 标记，其中 `high` 4 条（Keizer 2026 MCDE-ADC 基准、Paggi 2026 MCDE 光发射谱、Zhang 2026 时域 Dyson、Schio 2026 Cooper 极小 Dyson 轨道）建议**优先补齐全文**——若后续采纳 Dyson 轨道路线，这批将直接进入分级体系。

> 边界说明：本清单的 ⭐ 分级**只覆盖有全文的 57 篇**。无全文条目先补文献、再定级，避免"凭摘要定优先级"。""",
     """### B. 并行调研新增的 10 条 —— 已结清

来源 `outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`：MCDE / 时域 EKT / 相对论 EOM-CC 三类。2026-09-11 已补齐全文（`papers/Dyson_orbital/`）并完成定级：**⭐⭐⭐⭐ 2 篇（Schio、Keizer）· ⭐⭐⭐ 5 篇 · ⭐⭐ 3 篇**，归入 `by_topic.md` **T12**。

> 边界说明：本清单的 ⭐ 分级**只覆盖有全文的 67 篇**。无全文条目先补文献、再定级，避免"凭摘要定优先级"。""",
     "V10 appendix B")


def main() -> int:
    # group edits by file for a single read/write pass each
    by_file: dict[Path, list[tuple[str, str, str]]] = {}
    for path, old, new, tag in EDITS:
        by_file.setdefault(path, []).append((old, new, tag))

    failures: list[str] = []
    for path, jobs in by_file.items():
        text = path.read_text(encoding="utf-8")
        for old, new, tag in jobs:
            n = text.count(old)
            if n != 1:
                failures.append(f"{path.name} [{tag}]: matched {n} times (expected 1)")
                continue
            text = text.replace(old, new, 1)
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
