# 定向文献检索清单：多中心连续态 × 交换K/Feshbach

- 日期：2026-08-29
- 引擎：OpenAlex 多源（CrossRef/PubMed/arXiv 索引），relevance 排序
- 目的：Phase K 备选（多中心参考）与 Born 残差收敛（‖V_res G_ref W‖₂≈776，交换 K 主导）的文献支撑

---

## A. 多中心连续态 / MFPAD 方向

**核心（直接可用于实现决策，建议优先下载全文）**

| 优先级 | 文献 | 期刊/年 | DOI | 被引 | 与项目的关系 |
|---|---|---|---|---|---|
| ★★★ | Gharibnejad, Douguet, Schneider et al. — *A multi-center quadrature scheme for the molecular continuum* | CPC 2021 | 10.1016/j.cpc.2021.107889 | 10 | **多中心求积/连续态实现**，与 Phase K 多中心参考直接对应 |
| ★★★ | Marante, Argenti, Martín — *Hybrid Gaussian-B-spline basis for the electronic continuum: Photoionization of atomic hydrogen* | PRA 90, 012506 (2014) | 10.1103/physreva.90.012506 | 77 | GTO+B-spline 混合基连续态，与现有的 GTO 层 + 连续态方案强相关 |
| ★★★ | Borràs, González-Vázquez, Argenti et al. — *MFPAD of CO in the Vicinity of Feshbach Resonances: An XCHEM Approach* | JCTC 2021 | 10.1021/acs.jctc.1c00480 | 14 | **同时覆盖两方向**：分子框架 PAD + Feshbach 共振 |
| ★★☆ | Borràs et al. — *Photoionization cross sections and PAD of molecules with XCHEM-2.0* | CPC 2023 | 10.1016/j.cpc.2023.109033 | 6 | XCHEM 多中心连续态代码（升级版），实现参考 |
| ★★☆ | Ota, Yamazaki, Sébilleau et al. — *Theory of polarization-averaged core-level MFPAD: I. A full-potential method* | JPB 2020 | 10.1088/1361-6455/abd06d | 22 | 全势多中心 MFPAD，角分布方法学参考 |
| ★★☆ | Decleva, Stener, Toffoli — *Continuum Electronic States: The Tiresia Code* | Molecules 2022 | 10.3390/molecules27062026 | 20 | Tiresia 代码综述（延续已入库的 Toffoli 2023） |

**已在本库（无需重复下载）**：Duan 2024 多中心 MFPAD（PRA 109.063114）、Toffoli 2023 Tiresia CPC、Tenorio 2022 MR-Dyson（Molecules）、Nisoli 2017 ChemRev 综述。

---

## B. 交换 K 与 Feshbach 方向

**核心**

| 优先级 | 文献 | 期刊/年 | DOI | 被引 | 与项目的关系 |
|---|---|---|---|---|---|
| ★★★ | Gil, Winstead, Sheehy, McKoy — *New Theoretical Perspectives on Molecular Shape Resonances: Feshbach–Fano Methods for Mulliken Orbital Analysis of Photoionization Continua* | Physica Scripta 1990 | 10.1088/0031-8949/1990/t31/025 | 14 | **Feshbach–Fano 投影框架处理光电离连续态**，McKoy 谱系（与库内 Lucchese/McKoy 同源） |
| ★★★ | Jagau, Bravaya, Krylov — *Extending Quantum Chemistry of Bound States to Electronic Resonances* | Annu. Rev. Phys. Chem. 2017 | 10.1146/annurev-physchem-052516-050622 | 196 | **电子谐振（含形状/Feshbach）方法综述**，谐振态描述权威参考 |
| ★★★ | Zatsarinny, Bartschat — *The B-spline R-matrix method for atomic processes: application to atomic structure, electron collisions and photoionization* | JPB 46, 112001 (2013) | 10.1088/0953-4075/46/11/112001 | 198 | B-spline R-matrix（含交换处理）综述，交换/K 实现参照 |
| ★★☆ | Hazi — *A purely L2 method for calculating resonance widths* | JPB 1978 | 10.1088/0022-3700/11/8/001 | 107 | L² 方法直接算谐振宽度——与 L2 连续态残差收束问题相关 |

**背景/综述（视需要）**：Fano 1983 *Correlations of two excited electrons*（Rep. Prog. Phys., 519 被引）— 双激发/Feshbach 背景理论；Åberg 1992 *Unified theory of Auger* — 共振衰变背景。

**已在本库（无需重复下载）**：Lucchese–McKoy 1986 Schwinger 综述、Lucchese 1979/1983、Domcke 1983 投影散射（PRA）、Bachau 2001 B-spline 综述。

---

## C. 去重与冗余核查说明

- XCHEM（Borràs 2021/2023）被两方向查询同时命中，归入 A 但明确标注跨方向价值。
- Marante 2017（XCHEM-Ne 基态）、Moitra 2020（JPCL 精确参数）、Plésiat 2012（N2/CO 振动分支）为次相关，未列入核心表。
- 多中心方向与现货库重叠项（Duan/Toffoli/Tenorio）已剔除。

## D. 下一步建议

1. **优先下载 3 篇 ★★★**：Gharibnejad 2021（CPC）、Gil 1990（PhysScr）、Jagau 2017（ARPC）；Borràs 2021（JCTC）因跨方向性价比高可一并取。
2. DOI 均可走 USTC WebVPN / 机构通道获取（AIP/AIP Publishing / IOP / APS / Annual Reviews）。
3. 是否将上述候选追加进 `index/registry/candidates.yaml`（state: discovered）并生成下载 manifest，等待 DY 确认。
