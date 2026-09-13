# 按主题分类索引（2026-09-11 重写）

> 数据源：`registry/core.yaml`（6）+ `registry/candidates.yaml`（63）→ 全文可用 **67 篇**；另 2 条 `state: discovered`（无 PDF，见文末附录）。>   
> 星级口径见 `by_relevance.md`；本文件按**主题归属**组织，故同一文献只出现在其最贴切的一组。>   
> 分组说明：`papers/<子目录>` 为物理存放位置，本文件的 12 个主题组为**语义归类**，二者不必一一对应。>   
> 计数时点：2026-09-11 11:05（registry 可能被并行调研追加，若数字不符请以 registry 为准）。

| 组   | 主题                                  | 篇数 |
| --- | ----------------------------------- | -- |
| T1  | GTO/L2 连续态母体与基准                     | 4  |
| T2  | 动量空间积分核与递推积分                        | 4  |
| T3  | 可分势与 Schwinger/变分散射理论               | 4  |
| T4  | 连续态表示层增强                            | 7  |
| T5  | 球面波展开、加法定理与格林函数                     | 7  |
| T6  | 多中心连续态与 MFPAD                       | 5  |
| T7  | 共振与交换                               | 3  |
| T8  | 平行路线：B-spline 连续态                   | 8  |
| T9  | 平行路线：R-matrix / UKRmol+ / ePolyScat | 5  |
| T10 | 平行路线：复缩放 ECS                        | 1  |
| T11 | 光电离物理、阿秒与天体背景                       | 5  |
| T12 | Dyson 轨道与多体关联方法                     | 10 |
| T13 | 边缘与存档                               | 4  |

---

## T1 · GTO/L2 连续态母体与基准（4 篇）

本项目方法学的**直接母体**。Cacelli-Moccia-Rizzo 团队在 1990s 建立了用高斯型轨道（GTO）展开连续态、以 L² 技术计算光电离截面的范式，是本项目动量空间球面波路线的前身。

| 星级    | 文献                                                   | 方法贡献                           | 对应本项目模块                                              |
| ----- | ---------------------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo (1993) — JCP                  | GTO 基组 + L² 技术算 H₂ 光电离截面       | `momentum_gto`、`sw_matrix_element`、`benchmark_h2`    |
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo (1998) — PRA                  | 推广至微分截面与不对称参数 β                | `angular_reduction`、`frame_transform`、`benchmark_n2` |
| ⭐⭐⭐⭐⭐ | Cacelli, Moccia, Rizzo (2000) — Chem. Phys.          | 非对称/多原子分子（C₂H₂）处理              | `frame_transform`、`benchmark_c2h2`                   |
| ⭐⭐⭐⭐⭐ | Carmona-Novillo, Moccia, Spizzo (1996) — Chem. Phys. | 混合 GTO/STOCOS L² 基组，LiH 截面 + β | `momentum_gto`、`angular_reduction`、`benchmark_lih`   |

---

## T2 · 动量空间积分核与递推积分（4 篇）

**积分核是本项目的计算底座**：把 GTO 变换到动量空间、再把矩阵元约化到可递推的形式，直接决定 `SW_integral` 的正确性与成本。

| 星级    | 文献                                           | 方法贡献                                 | 对应本项目模块                                                     |
| ----- | -------------------------------------------- | ------------------------------------ | ----------------------------------------------------------- |
| ⭐⭐⭐⭐⭐ | Huang, Li, Luo, Wu, Duan, Zhang (2026) — JCP | **与项目同题**：递归 Gaussian 积分高效计算阴离子光脱附截面 | `PW_integral`、`GTO_integral`、`momentum_gto`、`CS_calculator` |
| ⭐⭐⭐⭐  | Obara, Saika (1986) — JCP                    | Cartesian Gaussian 积分的递归计算（OS 递推）    | `GTO_integral`、`momentum_gto`                               |
| ⭐⭐⭐⭐  | Obara, Saika (1988) — JCP                    | 广义递推公式，**含 Fourier 变换核**             | `GTO_integral`、`momentum_gto`、`SW_integral`                 |
| ⭐⭐⭐⭐  | McMurchie, Davidson (1978) — JCP             | Hermite 辅助函数展开的一/二电子积分方案             | `GTO_integral`、`momentum_gto`                               |

---

## T3 · 可分势与 Schwinger/变分散射理论（4 篇）

本项目用**可分展开**把散射振幅化为矩阵求逆。这一组是 `separable_potential` / `tau_matrix` / `schwinger_amplitude` 三个模块的理论来源；其中 Lucchese-McKoy 1983 的 Padé 修正直接关系到变分表达的收敛性风险。

| 星级   | 文献                                             | 方法贡献                             | 对应本项目模块                                                                          |
| ---- | ---------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------- |
| ⭐⭐⭐⭐ | Domcke (1983) — PRA                            | 投影算符方法处理势散射，可分势构造                | `separable_potential`、`green_function_matrix`、`tau_matrix`                       |
| ⭐⭐⭐⭐ | Lucchese, McKoy (1979) — J. Phys. B            | Schwinger 变分原理用于电子-原子散射（原始文献）    | `separable_potential`、`tau_matrix`、`schwinger_amplitude`                         |
| ⭐⭐⭐⭐ | Lucchese, Takatsuka, McKoy (1986) — Phys. Rep. | Schwinger 变分在电子-分子碰撞与分子光电离中的系统综述 | `separable_potential`、`green_function_matrix`、`tau_matrix`、`schwinger_amplitude` |
| ⭐⭐⭐⭐ | Lucchese, McKoy (1983) — PRA                   | 变分表达的 Padé 逼近修正（CO 5σ 应用）        | `tau_matrix`、`schwinger_amplitude`、`benchmark_strategy`                          |

---


## T4 · 连续态表示层增强（7 篇）

**与当前活跃瓶颈直接相关**。当 Born 残差谱范数 ≈776.2 不收敛时，需判定精度瓶颈是否落在"表示的靶侧"。这一组给出四类表示层增强范式（Lobatto 形状函数混合、STO/B-spline 混合、多项式高斯、复高斯 cGTO），以及波函数近似（平面波 vs Coulomb 波）的定量评估。

| 星级   | 文献                                                           | 方法贡献                              | 对应本项目模块                                              |
| ---- | ------------------------------------------------------------ | --------------------------------- | ---------------------------------------------------- |
| ⭐⭐⭐⭐ | Wilhelmy, Ackermann, Görling, Rösch (1994) — JCP             | Lobatto 形状函数 + GTO 混合基组算光电离截面     | `angular_reduction`、`continuum_wave`                 |
| ⭐⭐⭐⭐ | Moccia, Montuoro (2003) — Chem. Phys. Lett.                  | STO + B-spline 混合 L² 基组算 Li₂ 微分截面 | `momentum_gto`、`angular_reduction`                   |
| ⭐⭐⭐⭐ | Cacelli (1997) — J. Phys. B                                  | **评估多项式高斯对电子连续态的描述能力**            | `GTO_integral`、`continuum_wave`、`benchmark_strategy` |
| ⭐⭐⭐⭐ | Gozem, Gunina, Ichino, Osborn, Stanton, Krylov (2015) — JPCL | 光电子波函数取平面波还是 Coulomb 波的定量评估       | `continuum_wave`、`CS_calculator`、`frame_transform`   |
| ⭐⭐⭐⭐ | Marante, Argenti, Martín (2014) — PRA                        | 混合 Gaussian-B-spline 连续态（原子氢）     | `continuum_wave`、`GTO_integral`、`benchmark_strategy` |
| ⭐⭐⭐  | Matsuzaki, Yabushita (2017) — J. Comput. Chem.               | 复 GTO（cGTO）算光电离微分截面，双势公式          | `PW_integral`、`continuum_wave`、`benchmark_strategy`  |
| ⭐⭐⭐  | Ammar, Ancarani, Leclerc (2021) — J. Comput. Chem.           | 复高斯 + Coulomb 连续态，长度/速度规范讨论       | `PW_integral`、`continuum_wave`、`SW_integral`         |

---

## T5 · 球面波展开、加法定理与格林函数（7 篇）

球面波基的**数学底座**：展开的加法定理、自由粒子格林函数在该基下的矩阵元，以及球面波基在固体/多重散射语境中的经典用法。

| 星级    | 文献                                                    | 方法贡献                                | 对应本项目模块                                                           |
| ----- | ----------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| ⭐⭐⭐⭐⭐ | Mahato, Skomorowski (2026) — arXiv:2605.18564         | **球高斯与平面波调制高斯基上的自由粒子格林函数矩阵元（解析递推）** | `continuum_wave`、`SW_integral`、`momentum_gto`、`sw_matrix_element` |
| ⭐⭐⭐⭐  | Felderhof, Jones (1987) — J. Math. Phys.              | 矢量 Helmholtz 方程球面波解的加法定理            | `spherical_multipole`、`sw_matrix_element`                         |
| ⭐⭐⭐   | Huang, Jin, Zhang, Chen, Li (2026) — arXiv:2603.13995 | 收缩截断球面波构造可系统改进的数值原子轨道基              | `spherical_multipole`、`sw_matrix_element`                         |
| ⭐⭐⭐   | Moroz (2006) — J. Phys. A                             | 准周期 Helmholtz/Laplace 格林函数的格点求和     | `green_function_matrix`、`spherical_multipole`                     |
| ⭐⭐⭐   | Hughes (1994) — J. Math. Phys.                        | 任意自旋的球面波展开                          | `spherical_multipole`、`sw_matrix_element`                         |
| ⭐⭐⭐   | Gonis, Butler (2000) — Springer（专著）                   | 固体中的多重散射理论与 t 矩阵                    | `spherical_multipole`、`green_function_matrix`                     |
| ⭐⭐⭐   | Eyert (2000) — Int. J. Quantum Chem.                  | 增广球面波（ASW）方法基础与应用                   | `spherical_multipole`                                             |

---

## T6 · 多中心连续态与 MFPAD（5 篇）

Phase K **多中心扩展**的候选方案库。当前求解器以单中心球面波展开为基础；这一组给出把连续态扩展到多中心的几条技术路径，以及分子坐标系角分布（MFPAD）的完整处理链。

| 星级   | 文献                                              | 方法贡献                          | 对应本项目模块                                                     |
| ---- | ----------------------------------------------- | ----------------------------- | ----------------------------------------------------------- |
| ⭐⭐⭐⭐ | Gharibnejad, Douguet, Schneider (2021) — CPC    | 多中心求积方案直接构造分子连续态              | `continuum_wave`、`separable_potential`、`benchmark_strategy` |
| ⭐⭐⭐  | Ota, Yamazaki, Sebilleau (2021) — J. Phys. B    | 全势方法算极化平均核级 MFPAD             | `frame_transform`、`angular_reduction`、`continuum_wave`      |
| ⭐⭐⭐  | Borràs, González-Vázquez, Argenti (2021) — JCTC | XCHEM：Feshbach 共振附近的 CO MFPAD | `angular_reduction`、`frame_transform`、`continuum_wave`      |
| ⭐⭐⭐  | Borràs, Fernández-Milán, Argenti (2023) — CPC   | XCHEM-2.0：截面与光电子角分布           | `continuum_wave`、`frame_transform`、`benchmark_strategy`     |
| ⭐⭐⭐  | Duan, Gong, Cheng, Zhang (2024) — PRA           | 多中心连续态 → MFPAD，从平面波到扭曲光子      | `continuum_wave`、`angular_reduction`、`frame_transform`      |

---

## T7 · 共振与交换（3 篇）

**直接对应当前 Born 残差诊断**：交换项 K=4.83 为主导不收敛来源，非球性四极 41.5。这一组提供交换项的 Fano 分解视角、电子共振的现代量化处理综述，以及纯 L² 方法算共振宽度的源头文献。

| 星级   | 文献                                                     | 方法贡献                                 | 对应本项目模块                                                                       |
| ---- | ------------------------------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------- |
| ⭐⭐⭐⭐ | Gil, Winstead, Sheehy, McKoy (1990) — Phys. Scr.       | Feshbach-Fano 方法 + Mulliken 轨道分析形状共振 | `separable_potential`、`tau_matrix`、`schwinger_amplitude`、`benchmark_strategy` |
| ⭐⭐⭐  | Jagau, Bravaya, Krylov (2017) — Annu. Rev. Phys. Chem. | 束缚态量化方法扩展到电子共振（CAP/复能量）综述            | `correlation_strategy`、`continuum_wave`、`benchmark_strategy`                  |
| ⭐⭐⭐  | Hazi (1978) — J. Phys. B                               | 纯 L² 方法计算共振宽度（线性代数途径）                | `continuum_wave`、`separable_potential`、`benchmark_strategy`                   |

---


## T8 · 平行路线：B-spline 连续态（8 篇）

Decleva 学派为代表的多中心 B-spline 路线，是当前连续态计算的**主流对照路线**。用途是交叉验证与叙事定位，不是实现依据。

> 2026-09-11 起，Toffoli 2024（Tiresia）与 Brosolo 1992 已由 `papers/GTO_continuum/` 迁入 `papers/B_spline_continuum/`，与同路线文献归并。

| 星级   | 文献                                                                 | 方法贡献                                    | 对应本项目模块                                                  |
| ---- | ------------------------------------------------------------------ | --------------------------------------- | -------------------------------------------------------- |
| ⭐⭐⭐⭐ | Toffoli, Coriani, Stener, Decleva (2024) — CPC                     | Tiresia 代码：分子电子连续态与光电离                  | `method_comparison`、`benchmark_strategy`                 |
| ⭐⭐⭐  | Brosolo, Decleva (1992) — Chem. Phys.                              | B-spline 基下变分连续态轨道（H₂⁺）                 | `continuum_wave`、`benchmark_h2`                          |
| ⭐⭐⭐  | Decleva, Stener, Toffoli (2022) — Molecules                        | Tiresia 代码综述                            | `method_comparison`、`benchmark_strategy`                 |
| ⭐⭐⭐  | Stener, Fronzoni, Decleva (2005) — JCP                             | 非迭代 TD-DFT + 多中心 B-spline（CS₂、C₆H₆）     | `method_comparison`、`continuum_wave`、`angular_reduction` |
| ⭐⭐⭐  | Tenorio, Ponzi, Coriani, Decleva (2022) — Molecules                | 多参考 Dyson 轨道 + B-spline DFT/TD-DFT 连续态  | `correlation_strategy`、`method_comparison`               |
| ⭐⭐⭐  | Moitra, Coriani, Decleva (2021) — JCTC                             | EOM-CC Dyson 轨道 + B-spline TDDFT 捕获关联效应 | `correlation_strategy`、`method_comparison`               |
| ⭐⭐⭐  | Ruberti (2019) — JCTC                                              | 受限关联空间（RCS）B-spline ADC 方法              | `method_comparison`、`correlation_strategy`               |
| ⭐⭐⭐  | Bachau, Cormier, Decleva, Hansen, Martín (2001) — Rep. Prog. Phys. | B-spline 在原子分子物理中的应用综述                  | `method_comparison`、`continuum_wave`                     |

---

## T9 · 平行路线：R-matrix / UKRmol+ / ePolyScat（5 篇）

分区理论（R-matrix）与 Schwinger 变分代码化（ePolyScat）两条成熟路线的代表工作。Fang 2026 为本研究组的表示层标定尝试，**应用前须先做瓶颈归因 A/B 实验**（见 `notes/R_matrix_Fang2026_CO_OTMO_阅读笔记.md`）。

| 星级  | 文献                                                      | 方法贡献                          | 对应本项目模块                                                        |
| --- | ------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------- |
| ⭐⭐⭐ | Zatsarinny, Bartschat (2013) — J. Phys. B               | B-spline R-matrix 方法综述（原子过程）  | `method_comparison`、`benchmark_strategy`、`separable_potential` |
| ⭐⭐⭐ | Mašín, Benda, Gorfinkiel, Harvey, Tennyson (2020) — CPC | UKRmol+：R-matrix 全套建模套件       | `method_comparison`、`benchmark_strategy`、`workflow_design`     |
| ⭐⭐⭐ | Fang, Su, Tennyson, Fan, Fan, Zhang, Cheng (2026) — JCP | CO 电子散射的靶分子轨道优化（表示层标定）        | `method_comparison`、`benchmark_strategy`                       |
| ⭐⭐⭐ | Natalense, Lucchese (1999) — JCP                        | SF₆ 1s 光电离截面与不对称参数（ePolyScat） | `benchmark_strategy`、`angular_reduction`、`frame_transform`     |
| ⭐⭐⭐ | Gianturco, Lucchese, Sanna (1994) — JCP                 | 电子-CF₄ 低能弹性散射截面（静态交换）         | `separable_potential`、`benchmark_strategy`                     |

---

## T10 · 平行路线：复缩放 ECS（1 篇）

外复缩放（ECS）是本项目已调研但未采用的备选路线（见 `notes/复缩放方法发展脉络深度调查.md`）。保留源头实现文献以备对照。

| 星级  | 文献                                  | 方法贡献                | 对应本项目模块                              |
| --- | ----------------------------------- | ------------------- | ------------------------------------ |
| ⭐⭐⭐ | McCurdy, Martín (2004) — J. Phys. B | B-spline 框架下外复缩放的实现 | `continuum_wave`、`sw_matrix_element` |

---

## T11 · 光电离物理、阿秒与天体背景（5 篇）

背景与叙事定位。仅 Vanroose 2006（H₂ 双电离精确基准）与数值验证有直接关系，其余为概念性引用。

| 星级  | 文献                                                                                              | 方向                    | 对应本项目模块                                  |
| --- | ----------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------- |
| ⭐⭐⭐ | Vanroose, Horner, Martín, Rescigno, McCurdy (2006) — PRA                                        | 取向 H₂ 双光电离（ECS）       | `benchmark_h2`、`method_comparison`       |
| ⭐⭐  | Nisoli, Decleva, Calegari, Palacios, Martín (2017) — Chem. Rev.                                 | 分子阿秒电子动力学综述           | `method_comparison`、`historical_context` |
| ⭐⭐  | Calegari, Trabattoni, Palacios, Ayuso, Castrovilli, Decleva, Martín, Nisoli (2016) — J. Phys. B | 阿秒脉冲诱导的电荷迁移           | `method_comparison`、`historical_context` |
| ⭐⭐  | Ruckenbauer, Mai, Marquetand, González (2016) — Sci. Rep.                                       | 时间分辨光电子谱中的去活化通道       | `method_comparison`、`dyson_orbital`      |
| ⭐⭐  | Hróðmarsson, van Dishoeck (2023) — A\&A                                                         | Leiden 光解离/光电离截面数据库更新 | `benchmark_strategy`、`method_comparison` |

---


## T12 · Dyson 轨道与多体关联方法（10 篇）

**并行路线：Dyson 轨道从哪来。** 本项目的光电离截面需要 Dyson 轨道作为出发点；这一组是 2026 年三条新主线（多通道 Dyson 方程 MCDE、时域 Dyson / 扩展 Koopmans 定理、相对论 EOM-CC）的代表工作。

> **引用陷阱（勿踩）**：MCDE 家族的增益在**束缚态谱函数侧**，**不能**用于解决本项目 J.3.5 的连续态瓶颈（Born 谱范数 776.2）。MCDE 全部出自 Toulouse 单学派（Romaniello / Berger），无公开代码，验证限于小分子 + 体相 Si。>   
> **已被质疑的近似**：`nD-ADC(3)` ≠ `Dyson-ADC(3)`（差 ~0.1 eV，强关联 >0.25 eV）；引用 ADC(3) 精度须注明分支。>   
> **硬反证**：瞬时自然轨道**不能**替代 Dyson 轨道（PRL 136, 013204 (2026)，H⁻ 通道分辨 PMD 出假峰）。

| 星级   | 文献                                                                                                         | 方法贡献                                                                                           | 对应本项目模块                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| ⭐⭐⭐⭐ | Schio, Alagia, Moitra, Toffoli, Ponzi, Stener, Coriani, Decleva et al. (2026) — J. Chem. Phys. 164, 204301 | 环氧氯丙烷 Cooper 极小处轨道混合；**附左右 Dyson 轨道与 γ^L·γ^R 谱强度完整公式**，HF/DFT 无法解释的 β 振荡仅 EOM-CCSD Dyson 轨道可重现 | `frame_transform`、`momentum_gto`、`method_comparison`            |
| ⭐⭐⭐⭐ | Keizer, Paggi, Berger, Romaniello, Förster (2026) — arXiv:2608.25669                                       | MCDE 与 ADC(3)/nD-ADC(3) 的系统基准（精度边界与分支差异）                                                       | `correlation_strategy`、`method_comparison`、`benchmark_strategy` |
| ⭐⭐⭐  | Paggi, Berger, Romaniello (2026) — arXiv:2607.20070                                                        | MCDE 计算原子分子芯/价光发射谱（束缚态侧）                                                                       | `correlation_strategy`、`method_comparison`                      |
| ⭐⭐⭐  | Romaniello, Berger (2026) — arXiv:2603.27329                                                               | 屏蔽 MCDE：体相 Si 的 plasmon 卫星，MCDE 屏蔽处理起点                                                         | `correlation_strategy`、`method_origin`                          |
| ⭐⭐⭐  | Zhang, Li, Pathak, Sato, Ishikawa, He (2026) — Phys. Rev. Lett. 136(1)                                     | 时域扩展 Koopmans 定理（MCTDHF 空穴态）；"自然轨道替代 Dyson 轨道"的边界证据                                            | `correlation_strategy`、`continuum_wave`                         |
| ⭐⭐⭐  | Yuwono, Li, Zhang, Li, DePrince (2025) — J. Chem. Phys. 162(8)                                             | 双分量相对论 EOM-CC 计算电子电离（3h2p、自旋轨道、X2C）                                                            | `correlation_strategy`、`method_comparison`                      |
| ⭐⭐⭐  | Thapa, Dutta (2026) — arXiv:2602.21834                                                                     | 相对论 EOM-CC 的三体修正（X2CAMF，MAE 0.01–0.08 eV）                                                      | `correlation_strategy`、`benchmark_strategy`                     |
| ⭐⭐   | Sellié, Berger, Romaniello (2026) — Phys. Rev. B 114(12)                                                   | MCDE 双电离谱（pp 通道耦合 3h1e/3e1h，Auger 方向）                                                          | `correlation_strategy`、`method_comparison`                      |
| ⭐⭐   | Misael, Gomes (2024) — arXiv:2412.08403                                                                    | 相对论嵌入式 CVS-EOM-CC 处理锕系芯电离态（Cs₂UO₂Cl₄ 铀酰）                                                       | `correlation_strategy`、`method_comparison`                      |
| ⭐⭐   | Mukhopadhyay, Mukherjee, Gururangan, Piecuch, Dutta (2026) — J. Chem. Theory Comput. 22, 3233              | 降成本四分量相对论 DIP-EOM-CC（4h2p + 三体簇）                                                               | `correlation_strategy`                                          |

物理存放：`papers/Dyson_orbital/`（2026-09-11 补齐全文并三方对齐）。

---

## T13 · 边缘与存档（4 篇）

与当前计算路线无实质耦合。其中 Djajaputra 2003、Corsaro 2026、Asadova 2025 三篇系上一轮**错下载产物的更正结果**（原始文件名所指文献不存在），保留作动量空间/多极展开技巧的概念借鉴。

| 星级 | 文献                                                               | 方向                           | 对应本项目模块                                   |
| -- | ---------------------------------------------------------------- | ---------------------------- | ----------------------------------------- |
| ⭐⭐ | Djajaputra, Cooper (2003) — Phys. Status Solidi B                | 全势 LMTO 的紧束缚参数（NiAl）         | `momentum_gto`、`method_comparison`        |
| ⭐⭐ | Dziedzic, Hill, Skylaris (2013) — JCP                            | 非正交广义 Wannier 函数的线性标度 HF 交换能 | `method_comparison`、`separable_potential` |
| ⭐⭐ | Corsaro, Miano, Tamburrino, Ventre, Forestiere (2026) — IEEE TAP | 超表面电磁散射的多层快速多极子算法            | `spherical_multipole`、`method_comparison` |
| ⭐⭐ | Asadova, Achouri, Arjas, Auguié, Aydin, Rockstuhl (2025) — JQSRT | 光学散射响应 T 矩阵的数据格式建议           | `spherical_multipole`、`method_comparison` |

---

## 附：待下载（`state: discovered`，2 条 · 均无 PDF，不参与星级分级）

### A. 本次反向核实发现（2 条，原仅存在于 2026-07-22 手写清单）

| 文献                                                                                                                | 出处                                | DOI                           | 可得性          |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------------- | ------------ |
| Cacelli, Carravetta, Rizzo, Moccia (1990) — "Continuum by L2 Methods: Molecular Photoionization Cross Section"    | MOTECC-90，Springer 书章，pp. 639-691 | 10.1007/978-94-009-2219-8_12  | 书章，全文可获取性待评估 |
| Majety, Zielinski, Scrinzi (2015) — "Photoionization of few electron systems: a hybrid coupled channels approach" | New J. Phys. 17(6), 063002        | 10.1088/1367-2630/17/6/063002 | OA（IOP），可下载  |

### B. 并行调研新增（10 条）—— 已结清

原"Dyson 轨道方法调研"10 条（MCDE / 时域 EKT / 相对论 EOM-CC）已于 2026-09-11 补齐全文、升级为 `fulltext_available` 并完成定级，归入正文 **T12**，不再列为待下载。
