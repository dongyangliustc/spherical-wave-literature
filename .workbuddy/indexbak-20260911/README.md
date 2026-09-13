# 球面波基组与光电离截面计算 —— 文献索引

> 建立日期：2026-07-15
> 目录结构最近同步：2026-09-11（对齐实际文件树，67 篇；论文明细表同步完成）
> 对应项目：动量空间球面波基组光致电离截面计算（GTO 傅里叶变换 + IBP 处理偶极规范）

---

## 目录结构

```
spherical_wave_literature/
├── index/                      ← 索引层（人类可读视图 + 受控 registry）
│   ├── README.md               ← 本文件：总索引与目录结构
│   ├── by_topic.md             ← 按主题分类的索引
│   ├── by_relevance.md         ← 按相关度分级的阅读清单
│   ├── download_script.py      ← 批量下载脚本
│   └── registry/               ← 受控 registry（机器可读事实来源）
│       ├── README.md           ← registry 编辑规则
│       ├── core.yaml           ← 已复核、允许影响主索引与项目决策的来源
│       ├── candidates.yaml     ← 已发现/已筛选、尚未升级为 core 的来源
│       ├── benchmarks.yaml     ← 基准证据（系统 / 可观测量 / 代码阶段映射）
│       ├── risks.yaml          ← 方法局限、反证与实现风险
│       └── claims.yaml         ← 主张级 registry（clm-XXXX，双轴打标）
├── papers/                     ← PDF 按主题子目录存放（67 篇）
│   ├── GTO_continuum/          ← GTO 连续态方法（Cacelli-Moccia-Rizzo 系列 + 递归积分）【13】
│   ├── B_spline_continuum/     ← B-spline 连续态（Decleva 学派 / Tiresia）【9】
│   ├── Schwinger_L2/           ← Schwinger 变分原理与 L2 分离势（Lucchese-McKoy 系列）【7】
│   ├── R_matrix/               ← R-matrix 分区理论（UKRmol+ 系）【2】
│   ├── spherical_wave/         ← 球面波展开与格林函数【17】
│   ├── complex_scaling/        ← 复缩放与围道积分方法【1】
│   ├── general_review/         ← 综述与背景文献【8】
│   └── Dyson_orbital/          ← Dyson 轨道获取方法（MCDE / 时域 EKT / 相对论 EOM-CC）【10】
├── notes/                      ← 阅读笔记（主题笔记 + 深度调查报告 + 自产知识）【15】
├── docs/
│   ├── literature_harness/     ← metadata schema、状态机、promotion 规则、周报模板
│   └── superpowers/            ← plans/ 与 specs/
├── outputs/                    ← 派生产出
│   ├── review_packets/         ← 周度文献审查包
│   ├── sw_context/             ← SW 代码上下文注入包
│   ├── citation_network/       ← 引文网络数据
│   └── download_manifests/     ← 下载清单
├── tools/                      ← 主张抽取/锚定、registry 校验、三方一致性核对、审查包生成、内容推送
└── tests/                      ← registry 与工具链测试
```

> 索引分层原则：`index/registry/` 是受控事实来源，`index/*.md` 是其人类可读派生视图；
> 候选来源不得直接改写主索引，须经 promotion 规则复核。详见 `index/registry/README.md`
> 与 `docs/literature_harness/`。

---

## 核心论文学术索引（按相关度分档，2026-09-11 统一重定级）

> 档位口径见 `by_relevance.md`（⭐ = 当前阶段阅读优先级，不等价于 registry 的 `relevance` 字段）；
> 主题归类见 `by_topic.md`。本表额外给出 **PDF 文件名**，用于定位物理存放位置。
> 判据锚点：Born 残差谱范数 ≈776.2 不收敛（交换 K=4.83 主导、非球性四极 41.5）。

| 档位 | 文献 | 年 | 出处 | PDF 文件 |
|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | Cacelli et al. | 1993 | J. Chem. Phys. | `Cacelli_1993_H2_photoionization_JCP.pdf` |
|  | Cacelli et al. | 1998 | Phys. Rev. A | `Cacelli_1998_N2_differential_PRA.pdf` |
|  | Cacelli et al. | 2000 | Chem. Phys. | `Cacelli_2000_C2H2_differential_CP.pdf` |
|  | Carmona-Novillo et al. | 1996 | Chem. Phys. | `CarmonaNovillo_1996_LiH_photoionization_CP.pdf` |
|  | Huang et al. | 2026 | J. Chem. Phys. | `Huang_2026_recursive_Gaussian_PDCS_JCP.pdf` |
|  | Mahato & Skomorowski | 2026 | arXiv:2605.18564 | `Mahato_Skomorowski_2026_free_particle_Green_SGTO_arXiv.pdf` |
| ⭐⭐⭐⭐ | Obara & Saika | 1986 | J. Chem. Phys. | `Obara_Saika_1986_recursive_Cartesian_Gaussian_integrals_JCP.pdf` |
|  | Obara & Saika | 1988 | J. Chem. Phys. | `Obara_Saika_1988_general_recurrence_Cartesian_Gaussian_JCP.pdf` |
|  | McMurchie & Davidson | 1978 | J. Chem. Phys. | `McMurchie_Davidson_1978_cartesian_gaussian_integrals_JCP.pdf` |
|  | Domcke | 1983 | Phys. Rev. A | `Domcke_1983_projection_scattering_PRA.pdf` |
|  | Lucchese & McKoy | 1979 | J. Phys. B | `Lucchese_McKoy_1979_Schwinger_eHe_JPB.pdf` |
|  | Lucchese et al. | 1986 | Phys. Rep. | `Lucchese_Takatsuka_McKoy_1986_Schwinger_review_PhysRep.pdf` |
|  | Lucchese & McKoy | 1983 | Phys. Rev. A | `Lucchese_McKoy_1983_Pade_CO_photoionization_PRA.pdf` |
|  | Wilhelmy et al. | 1994 | J. Chem. Phys. | `Wilhelmy_1994_Lobatto_photoionization_JCP.pdf` |
|  | Moccia & Montuoro | 2003 | Chem. Phys. Lett. | `Moccia_Montuoro_2003_Li2_differential_CPL.pdf` |
|  | Cacelli | 1997 | J. Phys. B | `Cacelli_1997_polynomial_Gaussian_continuum_JPB.pdf` |
|  | Gozem et al. | 2015 | J. Phys. Chem. Lett. | `Gozem_2015_photoelectron_wavefunction_JPCL.pdf` |
|  | Marante et al. | 2014 | Phys. Rev. A | `Marante_2014_hybrid_GTO_BSpline_PRA.pdf` |
|  | Felderhof & Jones | 1987 | J. Math. Phys. | `Felderhof_1987_addition_theorems_JMP.pdf` |
|  | Gharibnejad et al. | 2021 | Comput. Phys. Commun. | `Gharibnejad_2021_multicenter_quadrature_CPC.pdf` |
|  | Gil et al. | 1990 | Phys. Scr. | `Gil_1990_FeshbachFano_Mulliken_PhysScr.pdf` |
|  | Toffoli et al. | 2024 | Comput. Phys. Commun. | `Toffoli_2024_Tiresia_CPC.pdf` |
|  | Schio et al. | 2026 | J. Chem. Phys. | `Schio_2026_Cooper_minimum_Dyson_orbitals_JCP_arXiv.pdf` |
|  | Keizer et al. | 2026 | arXiv:2608.25669 | `Keizer_2026_MCDE_ADC_benchmark_arXiv.pdf` |
| ⭐⭐⭐ | Brosolo & Decleva | 1992 | Chem. Phys. | `Brosolo_Decleva_1992_H2plus_BSpline_CP.pdf` |
|  | Decleva et al. | 2022 | Molecules | `Decleva_2022_Tiresia_continuum_Molecules.pdf` |
|  | Stener et al. | 2005 | J. Chem. Phys. | `Stener_2005_TDDFT_photoionization_JCP.pdf` |
|  | Tenorio et al. | 2022 | Molecules | `Tenorio_2022_Dyson_photoionization_Molecules.pdf` |
|  | Moitra et al. | 2021 | J. Chem. Theory Comput. | `Moitra_2021_EOMCC_Dyson_TDDFT_JCTC.pdf` |
|  | Ruberti | 2019 | J. Chem. Theory Comput. | `Ruberti_2019_RCS_ADC_Bspline_JCTC.pdf` |
|  | Bachau et al. | 2001 | Rep. Prog. Phys. | `Bachau_2001_BSplines_atomic_molecular_RepProgPhys.pdf` |
|  | Zatsarinny & Bartschat | 2013 | J. Phys. B | `Zatsarinny_Bartschat_2013_Bspline_Rmatrix_JPB.pdf` |
|  | Mašín et al. | 2020 | Comput. Phys. Commun. | `Masin_2020_UKRmol_plus_CPC_arXiv.pdf` |
|  | Fang et al. | 2026 | J. Chem. Phys. | `Fang_2026_CO_electron_scattering_orbital_optimization_JCP.pdf` |
|  | Natalense & Lucchese | 1999 | J. Chem. Phys. | `Natalense_Lucchese_1999_SF6_photoionization_JCP.pdf` |
|  | Gianturco et al. | 1994 | J. Chem. Phys. | `Gianturco_Lucchese_Sanna_1994_CF4_scattering_JCP.pdf` |
|  | McCurdy & Martin | 2004 | J. Phys. B | `McCurdy_Martin_2004_ECS_BSpline_JPB.pdf` |
|  | Matsuzaki & Yabushita | 2017 | J. Comput. Chem. | `Matsuzaki_Yabushita_2017_cGTO_photoionization_JCC.pdf` |
|  | Ammar et al. | 2021 | J. Comput. Chem. | `Ammar_2021_complex_Gaussian_photoionization_JCC.pdf` |
|  | Jagau et al. | 2017 | Annu. Rev. Phys. Chem. | `Jagau_2017_electronic_resonances_ARPC.pdf` |
|  | Hazi | 1978 | J. Phys. B | `Hazi_1978_L2_resonance_widths_JPB.pdf` |
|  | Ota et al. | 2021 | J. Phys. B | `Ota_2021_full_potential_MFPAD_JPB.pdf` |
|  | Borras et al. | 2021 | J. Chem. Theory Comput. | `Borras_2021_MFPAD_Feshbach_XCHEM_JCTC.pdf` |
|  | Borras et al. | 2023 | Comput. Phys. Commun. | `Borras_2023_XCHEM2_CPC.pdf` |
|  | Duan et al. | 2024 | Phys. Rev. A | `Duan_2024_multicenter_continuum_MFPAD_PRA.pdf` |
|  | Huang et al. | 2026 | arXiv:2603.13995 | `Huang_2026_TSW_NAO_basis_arXiv.pdf` |
|  | Moroz | 2006 | J. Phys. A | `Moroz_2006_quasi_periodic_Green_JPDA.pdf` |
|  | Hughes | 1994 | J. Math. Phys. | `Hughes_1994_spherical_wave_expansion_any_spin_JMP.pdf` |
|  | Gonis & Butler | 2000 | Springer（专著） | `Gonis_Butler_2000_multiple_scattering_solids_Springer.pdf` |
|  | Eyert | 2000 | Int. J. Quantum Chem. | `Eyert_2000_augmented_spherical_wave_IJQC.pdf` |
|  | Vanroose et al. | 2006 | Phys. Rev. A | `Vanroose_2006_H2_double_photoionization_PRA.pdf` |
|  | Paggi et al. | 2026 | arXiv:2607.20070 | `Paggi_2026_MCDE_photoemission_arXiv.pdf` |
|  | Romaniello & Berger | 2026 | arXiv:2603.27329 | `Romaniello_2026_screened_MCDE_arXiv.pdf` |
|  | Zhang et al. | 2026 | Phys. Rev. Lett. | `Zhang_2026_time_dependent_Dyson_EKT_PRL_arXiv.pdf` |
|  | Yuwono et al. | 2025 | J. Chem. Phys. | `Yuwono_2025_relativistic_EOMCC_ionization_JCP.pdf` |
|  | Thapa & Dutta | 2026 | arXiv:2602.21834 | `Thapa_2026_relativistic_EOMCC_triples_arXiv.pdf` |
| ⭐⭐ | Nisoli et al. | 2017 | Chem. Rev. | `Nisoli_2017_attosecond_electron_dynamics_ChemRev.pdf` |
|  | Calegari et al. | 2016 | J. Phys. B | `Calegari_2016_charge_migration_attosecond_JPB.pdf` |
|  | Ruckenbauer et al. | 2016 | Sci. Rep. | `Ruckenbauer_2016_trPES_SciRep.pdf` |
|  | Hrodmarsson & van Dishoeck | 2023 | Astron. Astrophys. | `Hrodmarsson_2023_VUV_database_AA.pdf` |
|  | Djajaputra & Cooper | 2003 | Phys. Status Solidi B | `Djajaputra_Cooper_2003_tight_binding_LMTO_NiAl_pssb.pdf` |
|  | Dziedzic et al. | 2013 | J. Chem. Phys. | `Dziedzic_Hill_Skylaris_2013_linear_scaling_HF_Wannier_JCP.pdf` |
|  | Corsaro et al. | 2026 | IEEE Trans. Antennas Propag. | `Corsaro_2026_MLFMA_metasurfaces_IEEE_TAP.pdf` |
|  | Asadova et al. | 2025 | J. Quant. Spectrosc. Radiat. Transf. | `Asadova_2025_Tmatrix_data_format_JQSRT.pdf` |
|  | Sellié et al. | 2026 | Phys. Rev. B | `Sellie_2026_MCDE_double_ionization_PRB_arXiv.pdf` |
|  | Misael & Gomes | 2024 | arXiv:2412.08403 | `Misael_2024_CVS_EOMCC_actinide_arXiv.pdf` |
|  | Mukhopadhyay et al. | 2026 | J. Chem. Theory Comput. | `Mukhopadhyay_2026_relativistic_DIP_EOMCC_JCTC.pdf` |

**分布**：⭐⭐⭐⭐⭐ 6 · ⭐⭐⭐⭐ 18 · ⭐⭐⭐ 32 · ⭐⭐ 11 = **67 篇**（全文可用）。

### 待下载（`state: discovered`，2 条 · 均无 PDF）

**A. 本次反向核实发现（2 条）** —— 原仅存在于 2026-07-22 手写清单，从未落地：

| 文献 | 出处 | DOI |
|---|---|---|
| Cacelli, Carravetta, Rizzo, Moccia | MOTECC-90（Springer 书章，pp. 639-691） | 10.1007/978-94-009-2219-8_12 |
| Majety, Zielinski, Scrinzi | New J. Phys. 17(6), 063002（OA） | 10.1088/1367-2630/17/6/063002 |

**B. 并行调研新增（10 条）** —— 已于 2026-09-11 补齐全文（`papers/Dyson_orbital/`），升级为 `fulltext_available`
并纳入上述星级分级（⭐⭐⭐⭐ 2 / ⭐⭐⭐ 5 / ⭐⭐ 3），详见 `by_topic.md` **T12**。来源：`outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`。

---

## 课本对应（来自你之前的知识地图）

| 课本 | 覆盖板块 | 对应论文主题 |
|------|---------|-------------|
| Helgaker JJO | B: GTO 积分 | Cacelli-Moccia-Rizzo 的 GTO 连续态方法 |
| Starace 综述 | A+C: 光致电离+连续态 | 截面公式、长度/速度规范 |
| Cohen-Tannoudji | A: 光相互作用 | 规范问题 |
| Taylor | C: 散射理论 | 格林函数、连续态 |

---

## 下载状态

> 论文 PDF 存放于 `../papers/` 各子目录下
> 使用浏览器（Chrome CDP）从各期刊网站下载
>
> **2026-09-11 状态**：三方一致（`papers/` 67 篇 = registry `paths.pdf` 67 = `sources.yaml` 67），由 `tools/check_three_way.py` 核对（PASS）。
> 已完成全量元数据核实（Crossref/arXiv），纠正 5 篇名实不符、迁移 2 篇主题错位、补下载 2 篇缺失全文（Ota 2021、Hazi 1978），
> 并于 2026-09-11 采纳 Dyson 轨道方法调研 10 条（补全全文 + 定级 + 三方对齐）。
> 清退 `papers/scansci_test/` 测试残留。另有 2 篇待下载（见上，均为 `state: discovered`）。
