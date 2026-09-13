# 相关度统一重定级草案（2026-09-11）

> **状态：草案 · 待 DY 裁决。本文件不修改任何索引文件。**
> 目标：为 `index/by_topic.md`、`index/by_relevance.md`、`index/README.md` 论文明细表三者的重写提供**单一口径的定级依据**。
> 覆盖范围：`index/registry/{core,candidates}.yaml` 全部 57 篇（PDF 与 registry 三方一致，2026-09-11 复核通过）。

---

## 0. 为什么要重定级（动机：三个问题并存）

**问题一：三个索引互相矛盾。** `by_relevance.md`（19 篇）与 `README.md` 论文明细表（20 篇）对同一篇文献给出不同档位：

| 文献 | by_relevance.md | README 明细表 | 偏差 |
|---|---|---|---|
| Moccia & Montuoro (2003) | ⭐⭐⭐ | 第 I 类 ★★★★★ | **差 2 档** |
| Brosolo & Decleva (1992) | ⭐⭐⭐ | 第 II 类 ★★★★ | 差 1 档 |
| Stener et al. (2005) | ⭐⭐⭐ | 第 II 类 ★★★★ | 差 1 档 |
| Moroz (2006) | 未收录 | 第 III 类 ★★★★ | 缺失 |
| Gonis & Butler | 未收录 | 第 III 类 ★★★★ | 缺失 |
| Domcke (1983) | 未收录 | 第 III 类 ★★★★ | 缺失 |
| Cacelli et al. (1990) MOTECC | 未收录 | 第 I 类 ★★★★★ | 缺失（且无 PDF/无 registry） |
| Majety et al. (2015) | 未收录 | 第 IV 类 ★★★ | 缺失（且无 PDF/无 registry） |

**问题二：覆盖率仅 19/57 ≈ 33%。** 两份清单均停留在 2026-07-22，38 篇后入库文献（含 2026 年新文献、Schwinger/Lucchese 系列、积分核系列、多中心 MFPAD 系列）完全未定级。

**问题三：无显式口径。** 旧清单未声明"星级"的判据，导致同档内混装（例：把"方法学母体"与"平行路线综述"并列为 ⭐⭐⭐⭐）。

因此本草案的定级**不是对旧判断的推翻，而是把两套互相矛盾的旧视图放到同一 rubric 下重新对齐**。任何与旧版的差异均在 §4 逐项列出，供逐条裁定或驳回。

---

## 1. 分级 rubric（单一口径）

判据锚定**当前活跃技术路径**：J.3.5 已完成（H₂ 基准 σ/Cacelli ≈ 1×，消除 J.2 自由 GF 约 3× 过校正）；J.4 待选方向。当前活跃瓶颈为 **Born 残差谱范数 ‖V_res G_ref W‖₂ ≈ 776.2 不收敛**，其中交换项 K = 4.83 主导、非球性四极 41.5（Spec §15.7 J-R 判据）。由此，"高相关" = 能直接影响以下四类决策之一：

1. **连续态表示层**（基组构造、表示对精度瓶颈的归因）；
2. **积分核**（动量空间/Fourier 变换/递推积分）；
3. **交换与共振处理**（K 项、Feshbach/形状共振、变分收敛控制）；
4. **基准比对**（可直接对照的截面/不对称参数数值）。

| 档位 | 定义 | 耦合强度 | 处置方式 |
|---|---|---|---|
| ⭐⭐⭐⭐⭐ | 本路线方法学母体、与项目同题的公式直接来源、或直接可比对的基准。不读会犯方向性错误 | 紧耦合 | 精读，进 SW 代码上下文候选池（须过 epistemic 门槛） |
| ⭐⭐⭐⭐ | 能改变实现细节或架构选择（积分核、表示层、收敛控制、交换项），或代表需交叉验证的平行路线领头工作 | 中耦合 | 精读方法节 + 按需复现 |
| ⭐⭐⭐ | 特定专题（共振宽度、复缩放、MFPAD、多中心、天体）或平行路线的具体实现细节 | 弱耦合 | 定向查阅（读摘要 + 关键公式节） |
| ⭐⭐ | 主题偏离（固体能带、电磁散射、线性标度、阿秒综述） | 无耦合 | 存档；仅作概念或引用背景 |

> 说明：**⭐ 表示"本项目当前阶段的阅读优先级"，不等价于 registry 的 `relevance` 字段**（后者表"与项目主题的相关性"）。二者可以不一致，例如 Nisoli 2017 在 registry 为 `medium` 但在本清单为 ⭐⭐（因属综述背景而非实现依据）。该差异不是矛盾，是不同轴。

---

## 2. 建议分级总览

| 档位 | 篇数 | 说明 |
|---|---|---|
| ⭐⭐⭐⭐⭐ | 6 | 母体 + 同题 + 基准 |
| ⭐⭐⭐⭐ | 16 | 实现级影响 / 交叉验证领头工作 |
| ⭐⭐⭐ | 27 | 专题与平行路线细节 |
| ⭐⭐ | 8 | 边缘存档 |
| **合计** | **57** | 与 registry 全等 |

---

## 3. 逐篇分级明细（按主题分组，12 组）

> `registry` 列为 `core.yaml`/`candidates.yaml` 中的 `relevance` 原值，供对照。

### T1 · GTO/L2 连续态母体与基准（4 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo（H₂ 截面） | 1993 | J. Chem. Phys. | core | 本路线方法学母体；H₂ 光致电离截面基准，与 J.3.5 H₂ 验证直接对照 | lit-cacelli-1993-h2-gto-continuum |
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo（N₂ 微分截面） | 1998 | Phys. Rev. A | core | 推广到微分截面与不对称参数 β；`angular_reduction` 的原始依据 | lit-cacelli-1998-n2-differential |
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo（C₂H₂ 微分截面） | 2000 | Chem. Phys. | core | 非对称/多原子分子处理；`frame_transform` 的依据 | lit-cacelli-2000-c2h2-differential |
| ⭐⭐⭐⭐⭐ | Carmona-Novillo, Moccia, Spizzo（LiH） | 1996 | Chem. Phys. | high | 混合 GTO/STOCOS L2 基组；表示层混合策略的直接先例 + LiH 基准 | lit-carmona-novillo-1996-lih-mixed-basis |

### T2 · 动量空间积分核与递推积分（4 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | Huang, Li, Luo et al.（递归高斯积分算阴离子光脱附截面） | 2026 | J. Chem. Phys. | core | **与项目同题**：递归 Gaussian 积分 + 阴离子光脱附截面，可直接复现比对 | lit-huang-li-luo-2026-recursive-gaussian-pdcs |
| ⭐⭐⭐⭐ | Obara, Saika（Cartesian Gaussian 积分递推） | 1986 | J. Chem. Phys. | high | OS 递推原始文献，`GTO_integral`/`momentum_gto` 的实现底座 | lit-obara-saika-1986-recursive-cartesian-gaussian-integrals |
| ⭐⭐⭐⭐ | Obara, Saika（广义递推，含 Fourier 变换核） | 1988 | J. Chem. Phys. | high | 广义递推给出 Fourier 变换核，动量空间积分直接依据 | lit-obara-saika-1988-general-recurrence-cartesian-gaussian |
| ⭐⭐⭐⭐ | McMurchie, Davidson（辅助函数积分） | 1978 | J. Chem. Phys. | high | Hermite 辅助函数方案，与 OS 递推互补的实现路线 | lit-mcmurchie-davidson-1978-cartesian-gaussian-integrals |

### T3 · 可分势与 Schwinger/变分散射理论（4 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐ | Domcke（投影算符势散射） | 1983 | Phys. Rev. A | core | 投影算符 + 可分势散射；`separable_potential`/`tau_matrix` 的理论母体 | lit-domcke-1983-projection-scattering |
| ⭐⭐⭐⭐ | Lucchese, McKoy（Schwinger 变分电子散射） | 1979 | J. Phys. B | high | Schwinger 变分原理用于电子散射的原始文献，`schwinger_amplitude` 母体 | lit-lucchese-mckoy-1979-schwinger-electron-scattering |
| ⭐⭐⭐⭐ | Lucchese, Takatsuka, McKoy（Schwinger 综述） | 1986 | Phys. Rep. | high | 电子-分子碰撞与分子光电离的 Schwinger 变分系统综述，实现的主要参照 | lit-lucchese-takatsuka-mckoy-1986-schwinger-review |
| ⭐⭐⭐⭐ | Lucchese, McKoy（Padé 修正，CO 5σ） | 1983 | Phys. Rev. A | high | 变分表达式的 Padé 加速；**变分收敛风险的直接证据** | lit-lucchese-mckoy-1983-pade-co-photoionization |

### T4 · 连续态表示层增强（混合基组 / 多项式高斯 / 复高斯 / 波函数近似）（7 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐ | Wilhelmy, Ackermann, Görling, Rösch（Lobatto 技术） | 1994 | J. Chem. Phys. | high | Lobatto 形状函数 + GTO 混合基组；表示层构造的直接先例 | lit-wilhelmy-1994-lobatto-photoionization |
| ⭐⭐⭐⭐ | Moccia, Montuoro（STO + B-spline 混合 L2，Li₂） | 2003 | Chem. Phys. Lett. | high | 混合 L2 基组算微分截面；"表示层拼装"策略的成熟范例 | lit-moccia-2003-sto-bspline-li2-differential |
| ⭐⭐⭐⭐ | Cacelli（多项式高斯描述电子连续态的性能） | 1997 | J. Phys. B | high | **直接评估 GTO 类表示对连续态的adequacy**，正对 J.4 表示层归因问题 | lit-cacelli-1997-polynomial-gaussian-continuum |
| ⭐⭐⭐⭐ | Gozem, Gunina, Ichino et al.（平面波 vs Coulomb 波） | 2015 | J. Phys. Chem. Lett. | high | 光电子波函数近似选择的定量评估；归一化与规范（L/V）风险的直接证据 | lit-gozem-2015-plane-wave-coulomb-wave-photoionization |
| ⭐⭐⭐⭐ | Marante, Argenti, Martín（混合 Gaussian-B-spline 连续态） | 2014 | Phys. Rev. A | high | 混合表示的显式构造；跨基组拼装的实操参考 | lit-marante-2014-hybrid-gaussian-bspline |
| ⭐⭐⭐ | Matsuzaki, Yabushita（复 GTO 算微分截面） | 2017 | J. Comput. Chem. | medium | 复 GTO（cGTO）连续态 + 双势公式；表示层备选方案 | lit-matsuzaki-yabushita-2017-cgto-photoionization |
| ⭐⭐⭐ | Ammar, Ancarani, Leclerc（复高斯分子光电离） | 2021 | J. Comput. Chem. | medium | cGTO + Coulomb 连续态 + 长度/速度规范讨论 | lit-ammar-ancarani-leclerc-2021-complex-gaussian-photoionization |

### T5 · 球面波展开、加法定理与格林函数（7 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | Mahato, Skomorowski（球高斯上自由粒子格林函数矩阵元） | 2026 | arXiv:2605.18564 | core | **`SW_integral`/`continuum_wave` 的公式直接来源**（球高斯 + 平面波调制高斯的解析递推） | lit-mahato-skomorowski-2026-free-particle-green-sgto |
| ⭐⭐⭐⭐ | Felderhof, Jones（矢量 Helmholtz 球面波加法定理） | 1987 | J. Math. Phys. | high | 加法定理是 `spherical_multipole` 展开合并的数学底座 | lit-felderhof-1987-addition-theorems-vector-helmholtz |
| ⭐⭐⭐ | Huang, Jin, Zhang et al.（收缩截断球面波 NAO 基） | 2026 | arXiv:2603.13995 | high | 截断球面波作为可系统改进的数值基；基组设计思路借鉴 | lit-huang-2026-contracted-truncated-spherical-waves |
| ⭐⭐⭐ | Moroz（准周期 Helmholtz/Laplace 格林函数） | 2006 | J. Phys. A | high | 准周期格林函数的格点求和技术，周期性延拓时备用 | lit-moroz-2006-quasi-periodic-green-helmholtz |
| ⭐⭐⭐ | Hughes（任意自旋的球面波展开） | 1994 | J. Math. Phys. | high | 自旋推广的球面波展开；自旋分辨扩展时查阅 | lit-hughes-1994-spherical-wave-expansion-any-spin |
| ⭐⭐⭐ | Gonis, Butler（固体中的多重散射，专著） | 2000 | Springer | medium | 多重散射/MST 与 t 矩阵的系统论述，概念性参照 | lit-gonis-butler-2000-multiple-scattering-solids |
| ⭐⭐⭐ | Eyert（增广球面波方法基础） | 2000 | Int. J. Quantum Chem. | medium | ASW 方法的清晰导论，球面波基在固体中的经典用法 | lit-eyert-2000-augmented-spherical-wave |

### T6 · 多中心连续态与 MFPAD（5 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐ | Gharibnejad, Douguet, Schneider（多中心求积构造分子连续态） | 2021 | Comput. Phys. Commun. | high | 多中心求积直接构造连续态；**Phase K 多中心扩展的首选备选方案** | lit-gharibnejad-2021-multicenter-quadrature |
| ⭐⭐⭐ | Ota, Yamazaki, Sebilleau（全势 MFPAD 理论 I） | 2021 | J. Phys. B | medium | 全势多中心 MFPAD；角分布完整处理参照 | lit-ota-2021-full-potential-mfpad |
| ⭐⭐⭐ | Borràs, González-Vázquez, Argenti（XCHEM 算 Feshbach 附近 MFPAD） | 2021 | J. Chem. Theory Comput. | high | Feshbach 共振 + MFPAD 的 XCHEM 实现，共振角分布对照 | lit-borras-2021-xchem-mfpad-feshbach |
| ⭐⭐⭐ | Borràs, Fernández-Milán, Argenti（XCHEM-2.0） | 2023 | Comput. Phys. Commun. | medium | XCHEM 代码化版本，工作流设计参照 | lit-borras-2023-xchem2 |
| ⭐⭐⭐ | Duan, Gong, Cheng, Zhang（多中心连续态 → MFPAD，含扭曲光子） | 2024 | Phys. Rev. A | high | 平面波→扭曲光子推广的多中心连续态；前沿方向 | lit-duan-2024-multicenter-continuum-mfpad |

### T7 · 共振与交换（Feshbach / 形状共振 / L² 共振宽度）（3 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐ | Gil, Winstead, Sheehy, McKoy（Feshbach-Fano + Mulliken 轨道分析） | 1990 | Phys. Scr. | high | 交换项与形状共振的 Fano 分析；**直接对应 J.3.5 交换 K=4.83 主导的诊断** | lit-gil-1990-feshbach-fano-mulliken |
| ⭐⭐⭐ | Jagau, Bravaya, Krylov（束缚态量化扩展至电子共振，综述） | 2017 | Annu. Rev. Phys. Chem. | high | 电子共振（CAP/复能量）系统综述，共振处理选型参考 | lit-jagau-2017-electronic-resonances |
| ⭐⭐⭐ | Hazi（纯 L² 方法算共振宽度） | 1978 | J. Phys. B | medium | L² 方法算共振宽度的原始文献，与本路线同源 | lit-hazi-1978-l2-resonance-widths |

### T8 · 平行路线：B-spline 连续态（8 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐⭐ | Toffoli, Coriani, Stener, Decleva（Tiresia 代码） | 2023 | Comput. Phys. Commun. | high | 平行路线领头代码，交叉验证与叙事定位的主要对照 | lit-toffoli-coriani-stener-decleva-2024-tiresia-code |
| ⭐⭐⭐ | Brosolo, Decleva（B-spline 变分连续态，H₂⁺） | 1992 | Chem. Phys. | high | B-spline 连续态开端；H₂⁺ 基准与基组无关性论据 | lit-brosolo-1992-variational-continuum-spline-h2plus |
| ⭐⭐⭐ | Decleva, Stener, Toffoli（Tiresia 综述） | 2022 | Molecules | high | Tiresia 路线总览，快速定位 | lit-decleva-2022-tiresia-review |
| ⭐⭐⭐ | Stener, Fronzoni, Decleva（非迭代 TD-DFT + 多中心 B-spline） | 2005 | J. Chem. Phys. | high | 多中心 B-spline 的 TD-DFT 实现细节 | lit-stener-2005-tddft-noniterative-bspline |
| ⭐⭐⭐ | Tenorio, Ponzi, Coriani, Decleva（多参考 Dyson + B-spline DFT/TD-DFT） | 2022 | Molecules | high | 多参考 Dyson 与连续态耦合，关联处理对照 | lit-tenorio-ponzi-coriani-decleva-2022-mr-dyson-b-spline |
| ⭐⭐⭐ | Moitra, Coriani, Decleva（EOM-CC Dyson + B-spline TDDFT） | 2021 | J. Chem. Theory Comput. | high | 关联效应捕获的对照实现 | lit-moitra-coriani-decleva-2021-correlation-photoionization |
| ⭐⭐⭐ | Ruberti（RCS-ADC B-spline） | 2019 | J. Chem. Theory Comput. | high | 受限关联空间 ADC + B-spline，全截面计算对照 | lit-ruberti-2019-rcs-adc-b-spline |
| ⭐⭐⭐ | Bachau, Cormier, Decleva et al.（B-splines 应用综述） | 2001 | Rep. Prog. Phys. | high | B-spline 在原子分子物理中的权威综述，方法史定位 | lit-bachau-2001-bsplines-atomic-molecular |

### T9 · 平行路线：R-matrix / UKRmol+ / ePolyScat（5 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐ | Zatsarinny, Bartschat（B-spline R-matrix 综述） | 2013 | J. Phys. B | high | B-spline R-matrix 系统综述，分区理论对照 | lit-zatsarinny-bartschat-2013-bspline-rmatrix |
| ⭐⭐⭐ | Mašín, Benda, Gorfinkiel, Harvey, Tennyson（UKRmol+） | 2020 | Comput. Phys. Commun. | high | R-matrix 主流代码包，工作流与验证链设计参照 | lit-masin-benda-gorfinkiel-2020-ukrmol-plus |
| ⭐⭐⭐ | Fang, Su, Tennyson et al.（CO 电子散射靶轨道优化） | 2026 | J. Chem. Phys. | medium | 表示层标定（参考态权重）的前沿尝试；**应用前提须先做瓶颈归因 A/B**，见 memory 记录 | lit-fang-2026-co-electron-scattering-orbital-optimization |
| ⭐⭐⭐ | Natalense, Lucchese（SF₆ 1s 光电离截面与 β） | 1999 | J. Chem. Phys. | medium | ePolyScat 的截面+β 算例，基准数据来源 | lit-natalense-lucchese-1999-sf6-photoionization |
| ⭐⭐⭐ | Gianturco, Lucchese, Sanna（CF₄ 低能弹性散射） | 1994 | J. Chem. Phys. | medium | 静态交换近似的 ePolyScat 算例，可分势应用实例 | lit-gianturco-lucchese-sanna-1994-cf4-scattering |

### T10 · 平行路线：复缩放 ECS（1 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐ | McCurdy, Martín（B-spline 外复缩放实现） | 2004 | J. Phys. B | high | ECS + B-spline 的关键实现（复缩放为本项目已调研的备选路线） | lit-mccurdy-2004-ecs-bspline |

### T11 · 光电离物理、阿秒与天体背景（5 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐⭐ | Vanroose, Horner, Martín et al.（取向 H₂ 双光电离） | 2006 | Phys. Rev. A | medium | H₂ 双电离的 ECS 精确基准，H₂ 体系扩展参考 | lit-vanroose-2006-h2-double-photoionization-aligned |
| ⭐⭐ | Nisoli, Decleva, Calegari et al.（阿秒电子动力学综述） | 2017 | Chem. Rev. | medium | 领域综述，背景与引用定位 | lit-nisoli-2017-attosecond-electron-dynamics |
| ⭐⭐ | Calegari, Trabattoni, Palacios et al.（阿秒脉冲诱导电荷迁移） | 2016 | J. Phys. B | medium | 生物分子电荷迁移，与截面计算无直接耦合 | lit-calegari-2016-charge-migration-attosecond |
| ⭐⭐ | Ruckenbauer, Mai, Marquetand, González（trPES 去活化通道） | 2016 | Sci. Rep. | medium | trPES + Dyson 范数，方法论旁支 | lit-ruckenbauer-2016-trpes-deactivation-dyson |
| ⭐⭐ | Hróðmarsson, van Dishoeck（Leiden VUV 截面数据库更新） | 2023 | Astron. Astrophys. | medium | 天体 VUV 数据库；**与本项目当前计算路线无耦合**（C₂ₙH⁻ 方向若需实验比对再启用） | lit-hrodmarsson-2023-leiden-vuv-database |

### T12 · 边缘与存档（4 篇）

| 星级 | 文献 | 年 | 出处 | registry | 判据 | id |
|---|---|---|---|---|---|---|
| ⭐⭐ | Djajaputra, Cooper（LMTO 紧束缚参数，NiAl） | 2003 | Phys. Status Solidi B | low | 固体能带紧束缚；仅动量空间 Fourier 变换技巧可借鉴 | lit-djajaputra-2003-tight-binding-lmto-nial |
| ⭐⭐ | Dziedzic, Hill, Skylaris（线性标度 HF 交换，Wannier） | 2013 | J. Chem. Phys. | medium | 线性标度交换能；仅作交换项加速的概念参照 | lit-dziedzic-2013-linear-scaling-hf-wannier |
| ⭐⭐ | Corsaro, Miano, Tamburrino et al.（MLFMA 电磁散射超表面） | 2026 | IEEE Trans. Antennas Propag. | medium | 电磁多极快速算法；与本项目无实质耦合（原为错下载产物） | lit-corsaro-2026-mlfma-metasurfaces |
| ⭐⭐ | Asadova, Achouri, Arjas et al.（T 矩阵数据格式建议） | 2025 | J. Quant. Spectrosc. Radiat. Transf. | medium | 光学散射 T 矩阵数据格式；仅"数据格式规范化"思路可借鉴 | lit-asadova-2025-tmatrix-data-format |

---

## 4. 与 2026-07-22 旧版的差异（**需逐项裁定**）

### 4.1 新增定级：38 篇（旧版两份清单均未收录）

按本草案分别落于：⭐⭐⭐⭐⭐ 2 篇、⭐⭐⭐⭐ 9 篇、⭐⭐⭐ 19 篇、⭐⭐ 8 篇（合计 38）
（明细见 §3；其中 T2/T3/T4/T6/T7 五组、以及 Lucchese 系列、积分核系列为本次新增的主体）

### 4.2 上调：2 项

| 文献 | 旧 | 新 | 理由 |
|---|---|---|---|
| Moccia & Montuoro (2003) | ⭐⭐⭐（by_relevance）／★★★★★（README） | ⭐⭐⭐⭐ | 旧版自相矛盾；按 rubric 定为"表示层拼装的成熟范例"（中耦合） |
| Gozem et al. (2015) | ⭐⭐⭐ | ⭐⭐⭐⭐ | 归一化与规范（L/V）风险的直接证据，影响前因子链与波函数近似选择 |

### 4.3 下调：10 项

| 文献 | 旧 | 新 | 理由 |
|---|---|---|---|
| Toffoli et al. (2023) Tiresia | ⭐⭐⭐⭐ | ⭐⭐⭐ | 平行路线领头工作 → 归"需交叉验证"档；GTO/L2 路线已锁定 |
| Decleva et al. (2022) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 同上（综述性质） |
| McCurdy & Martín (2004) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 复缩放备选路线，非实现依据 |
| Tenorio et al. (2022) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 平行路线的关联处理细节 |
| Moitra et al. (2021) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 同上 |
| Ruberti (2019) | ⭐⭐⭐⭐ | ⭐⭐⭐ | 同上 |
| Nisoli et al. (2017) | ⭐⭐⭐ | ⭐⭐ | 领域综述，无实现耦合 |
| Calegari et al. (2016) | ⭐⭐⭐ | ⭐⭐ | 生物分子阿秒，无耦合 |
| Ruckenbauer et al. (2016) | ⭐⭐⭐ | ⭐⭐ | trPES 旁支 |
| Hróðmarsson & van Dishoeck (2023) | ⭐⭐⭐ | ⭐⭐ | 天体数据库，与当前路线无耦合 |

### 4.4 保持不变：9 项

Cacelli 1993／1998／2000、Carmona-Novillo 1996（均 ⭐⭐⭐⭐⭐）；Wilhelmy 1994、Brosolo 1992、Stener 2005（⭐ 档位不变，Brosolo/Stener 由 README 的 4★ 与 by_relevance 的 3★ 统一为 **⭐⭐⭐**）。

> **裁决选项**
> - **方案 A（本草案）**：按 rubric 统一重定级，接受上表 10 项下调。
> - **方案 B（最小改动）**：保留旧版 19 项的全部星级，仅对 38 篇新增文献定级；代价是旧矛盾（Moccia 2003 差 2 档、三篇 README 独有项）继续存在。
> - **方案 C（折中）**：接受上调 2 项与 B-spline 块（6 项）保持 ⭐⭐⭐⭐，仅将 4 篇综述降为 ⭐⭐。
>
> 请指定方案，或在 §4.3 表内逐行裁定。

---

## 5. 顺带发现（独立于分级，需单独裁决）

### 5.1 幽灵条目：README 论文明细表有、registry 与 papers 均无（2 篇）

| 文献 | 出处 | DOI | 现状 |
|---|---|---|---|
| Cacelli, Carravetta, Rizzo, Moccia，"Continuum by L2 Methods: Molecular Photoionization Cross Section" | MOTECC-90（书章） | 10.1007/978-94-009-2219-8_12 | **无 registry、无 PDF、无 sources.yaml 条目**；仅存在于 README 表格（列为第 I 类 ★★★★★） |
| Majety, Zielinski, Scrinzi，"Photoionization of few electron systems: a hybrid coupled channels approach" | New J. Phys. 17, 063002 | 10.1088/1367-2630/17/6/063002 | 同上（README 列为第 IV 类 ★★★） |

已核查：registry、`papers/`、`sources.yaml`、`notes/` 均无对应记录 → 确认是 2026-07-22 依"知识地图"手写清单时的**未落地条目**。

**建议**：按发现态登记（`state: discovered`、`paths.pdf: null`、`review_status: unreviewed`、`actionability: reading_candidate`），再由你决定是否下载。
- Majety 2015（New J. Phys.）为 OA，可下载；
- Cacelli 1990 为 Springer 书章，可能仅有章节 DOI、无独立全文 PDF。

> 注：这与上一轮 Ota 2021 / Hazi 1978 的情形互为镜像——那两篇是"registry 有、PDF 无"（已补下载），这两篇是"README 有、registry 与 PDF 皆无"。

### 5.2 主题归类错误：2 篇 B-spline 文献错放在 GTO_continuum/（建议迁出）

| 文件 | 现位置 | 建议位置 | 理由 |
|---|---|---|---|
| `Toffoli_2023_Tiresia_CPC.pdf` | `papers/GTO_continuum/` | `papers/B_spline_continuum/` | Tiresia 是纯 B-spline 代码；同系列（Decleva 2022、Stener 2005、Moitra 2021、Tenorio 2022、Ruberti 2019、Bachau 2001、Zatsarinny 2013）全部在 B_spline_continuum/ |
| `Brosolo_Decleva_1992_H2plus_BSpline_CP.pdf` | `papers/GTO_continuum/` | `papers/B_spline_continuum/` | 纯 spline 基组变分连续态。**若当初系有意与 Cacelli 系列并置作方法对照，可保留原位并加注说明** |

同时需同步：`candidates.yaml` 的 `paths.pdf`、`sources.yaml` 的 `path` → 迁移后重跑三方一致性检查与索引重建。

> 边界的两种情形已评估但**建议维持原位**：`Marante_2014_hybrid_GTO_BSpline_PRA.pdf`（Gaussian+B-spline 混合，归属 GTO 侧合理）、`Moccia_Montuoro_2003_Li2_differential_CPL.pdf`（STO+B-spline 混合）。

### 5.3 年份口径不一致：1 项 —— **经核实后判断方向已更正**

> **更正说明（2026-09-11 同日）**：本节初稿建议"统一为 2023（DOI 年）"。经 Crossref 核实后该方向**被推翻**，正确结论如下。

- `lit-toffoli-coriani-stener-decleva-2024-tiresia-code`
  - Crossref 记录：`Computer Physics Communications`，**vol 297, 109038, published-print 2024-04**
  - 即 **registry 的 `year: 2024` 是正确的**；错的是 **PDF 文件名 `Toffoli_2023_…`**（2023 仅为 DOI 注册年）
  - **处置**：保留 `year: 2024`；文件按核实年改名为 `Toffoli_2024_Tiresia_CPC.pdf`；`metadata_note` 记录该 DOI 后缀陷阱
  - **教训**：本次差点按"DOI 后缀年"反向改错 registry。DOI 后缀年份 ≠ 出版年，必须以 Crossref 的 `published-print` / 卷号为准
- `lit-gonis-butler-2000-multiple-scattering-solids`：registry 已注明 Crossref 为 2000、文件名旧为 1999（已改名解决）；**README 表格已同步更正为 2000**

---

## 8. 执行记录（2026-09-11，用户确认后落地）

### 8.1 已执行项

| 项 | 动作 | 校验 |
|---|---|---|
| §5.1 幽灵条目 | 2 条按 `state: discovered` / `confidence: metadata_only` / `pdf: null` 登记进 `candidates.yaml`；registry 条目数 57 → 59 | `validate_registry.py` PASSED |
| §5.2 迁移 | `Toffoli_2024_Tiresia_CPC.pdf`、`Brosolo_Decleva_1992_H2plus_BSpline_CP.pdf` 由 `papers/GTO_continuum/` 迁至 `papers/B_spline_continuum/` | MD5 迁移前后一致（`a3bcbd90…` / `49ea0688…`） |
| §5.2 引用同步 | `candidates.yaml` 2 处 `paths.pdf`、`sources.yaml` 2 处 `path`；`source_id` `paper-toffoli-2023-bspline` → `paper-toffoli-2024`；清理 sources.yaml 陈旧注释 | 旧路径残留 0；`source_id` 无重复 |
| §5.3 年份 | 保留 `year: 2024`，文件名 2023 → 2024（见上更正说明） | Crossref `published-print 2024-04` |
| 目录清理 | 删除 `papers/scansci_test/`（非空，含 `test_dois.txt` 测试残留） | 无悬空引用 |
| 索引重写 | `by_topic.md`（12 主题组）、`by_relevance.md`（4 档）、`README.md` 明细表（57 行 + 待下载 2 行）全部按草案 §3 重写 | 脚本校验 57/57 覆盖，无遗漏/多余/重复 |
| 笔记同步 | `notes/GTO_continuum.md` §6/§7 标注迁出与重定级；`notes/B_spline_continuum.md` 年份更正 | — |

### 8.2 执行后状态

| 指标 | 值 |
|---|---|
| `papers/**/*.pdf` | 57 |
| registry 条目 | 59（57 有 PDF + 2 discovered 无 PDF） |
| registry `paths.pdf` basename | 57 |
| `sources.yaml` `format: pdf` basename | 57 |
| 三方 basename 全等 | ✅ True |
| `source_id` | 87，无重复；`paper-*` = 57 |
| 向量索引 | 重建后核实（见 §8.3） |

### 8.3 待复核项

- 索引重建后 chunk / source 计数，以及 `paper-toffoli-2024` 与 `paper-brosolo-1992` 的命中抽检


---

## 6. 重写结构建议（供 `by_topic.md` / `by_relevance.md` 落笔用）

**`by_topic.md`**：采用 §3 的 12 个主题组（T1–T12），每组一段导语 + 表格（文献 / 贡献 / 对应本项目模块）。相比旧版 5 组，新增 T2 积分核、T3 Schwinger、T4 表示层、T6 多中心、T7 共振、T9 R-matrix、T10 复缩放、T12 存档 —— 使"方法学母体"与"平行路线"不再混在一组。

**`by_relevance.md`**：分层呈现以保持可用性——
- ⭐⭐⭐⭐⭐ 与 ⭐⭐⭐⭐：**逐条列出**（含出处、判据、对应模块）→ 22 条，即实际精读队列；
- ⭐⭐⭐：**紧凑表格**（一行一篇）→ 27 条；
- ⭐⭐：**单行归档段**（仅列作者-年份）→ 8 条。

**`README.md` 论文明细表**：改用与 `by_relevance.md` 相同档位，§3 表格即为数据源；同时删除 §5.1 的两个幽灵条目（或改为"待下载"小节）。

---

## 7. 审计信息

| 项 | 值 |
|---|---|
| 数据源 | `index/registry/core.yaml`（6）+ `candidates.yaml`（51）= 57 |
| 三方一致性 | papers 57 = registry 57 = sources.yaml 57（✅ 全等，2026-09-11 复核） |
| registry 校验 | `tools/validate_registry.py` → PASSED |
| 本文件性质 | **草案**；未修改任何索引文件、registry 或 sources.yaml |
| 待裁决项 | §4.4 方案 A/B/C 或逐项裁定；§5.1 幽灵条目处置；§5.2 迁移 2 篇；§5.3 年份统一 |
