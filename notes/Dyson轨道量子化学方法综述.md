# 计算 Dyson 轨道的量子化学方法及主流程序综述

> 基于风暴知识工坊 (Storm Knowledge Crafter) STORM 多视角研究法
> 种子文献：项目内 26 篇 PDF + 9 份笔记（spherical_wave_literature 工作区）
> 补充来源：网络公开学术信息（2026-07-20 检索）
> 生成日期：2026-07-20
> 方法论：五视角 STORM 拆解 → 矛盾图谱 → 综合简报 → 同行评审自检

---

## 目录

- [一、Dyson 轨道的定义与物理意义](#一dyson-轨道的定义与物理意义)
- [二、五视角 STORM 拆解](#二五视角-storm-拆解)
- [三、矛盾图谱](#三矛盾图谱)
- [四、量子化学方法分类](#四量子化学方法分类)
- [五、主流量子化学程序](#五主流量子化学程序)
- [六、综合简报](#六综合简报)
- [七、同行评审自检](#七同行评审自检)
- [八、方法选择决策树](#八方法选择决策树)
- [九、关键文献索引](#九关键文献索引)

---

## 一、Dyson 轨道的定义与物理意义

### 1.1 数学定义

Dyson 轨道是连接 N 电子初态与 N−1（或 N+1）电子末态的**单电子重叠函数**。对于光电离过程（N → N−1 + e⁻），Dyson 轨道定义为：

$$\phi^{Dyson}(\mathbf{x}) = \sqrt{N} \int \Psi_i^N(\mathbf{x}, \mathbf{x}_2, \ldots, \mathbf{x}_N) \, \Psi_f^{N-1*}(\mathbf{x}_2, \ldots, \mathbf{x}_N) \, d\mathbf{x}_2 \cdots d\mathbf{x}_N$$

其中 $\mathbf{x} = (\mathbf{r}, \omega)$ 为自旋-空间坐标，$\Psi_i^N$ 为初态 N 电子波函数，$\Psi_f^{N-1}$ 为末态 (N−1) 电子（离子）波函数。

对于电子附着过程（N → N+1），定义类似：

$$\phi^{Dyson}(\mathbf{x}) = \sqrt{N+1} \int \Psi_i^N(\mathbf{x}_2, \ldots, \mathbf{x}_{N+1}) \, \Psi_f^{N+1*}(\mathbf{x}, \mathbf{x}_2, \ldots, \mathbf{x}_{N+1}) \, d\mathbf{x}_2 \cdots d\mathbf{x}_{N+1}$$

### 1.2 物理意义

Dyson 轨道在光电离理论中的核心地位源于以下三个性质：

**性质 1：光电子矩阵元的承载者。** 在偶极近似和强正交（sudden）近似下，光电子偶极矩阵元完全由 Dyson 轨道和连续态波函数决定：

$$D_{IF}^{\mathbf{k}} = \langle \phi^{Dyson} | \hat{\mathbf{r}} \cdot \mathbf{u} | \Psi_{\mathbf{k}}^{el} \rangle$$

其中 $\Psi_{\mathbf{k}}^{el}$ 为光电子连续态波函数，$\mathbf{u}$ 为光偏振方向。此矩阵元决定了总截面和微分截面（角分布）。

**性质 2：Koopmans 定理的推广。** 在 Hartree-Fock 或 Kohn-Sham 近似下，Dyson 轨道退化为正则分子轨道。因此 Dyson 轨道是"考虑了轨道弛豫和电子关联后的分子轨道"，是 Koopmans 定理的精确推广。

**性质 3：谱强度（pole strength）的度量。** Dyson 轨道的模方 $\|\phi^{Dyson}\|^2$（也称谱强度或 spectroscopic factor）量化了电离过程的"单电子特征"程度。模方接近 1 表示准粒子图像适用；模方远小于 1 则表明强关联效应（如卫星峰）显著。

### 1.3 与 Green 函数理论的联系

Dyson 轨道自然地从单粒子 Green 函数（one-particle Green's function, 1p-GF）理论中产生。Green 函数的 Lehmann 表示为：

$$G(\mathbf{x}, \mathbf{x}'; \omega) = \sum_f \frac{\phi_f^{Dyson}(\mathbf{x}) \phi_f^{Dyson*}(\mathbf{x}')}{\omega - (E_0^N - E_f^{N-1}) - i0^+} + \sum_f \frac{\phi_f^{Dyson}(\mathbf{x}') \phi_f^{Dyson*}(\mathbf{x})}{\omega - (E_f^{N+1} - E_0^N) + i0^+}$$

Dyson 轨道是 Green 函数的**留数**（residue），电离能为 Green 函数的**极点**（pole）。求解 Dyson 方程

$$\hat{G}_0^{-1}(\omega) \phi^{Dyson} = \hat{\Sigma}(\omega) \phi^{Dyson}$$

即可直接获得电离能和 Dyson 轨道，**无需分别计算 N 和 N−1 电子态的波函数**。这是电子传播子（electron propagator）方法的核心优势。

---

## 二、五视角 STORM 拆解

### 视角一：实践者（每天用 Dyson 轨道做光电离计算的量化化学家）

**核心立场**：Dyson 轨道是连接"精确的束缚态电子结构"与"连续态光电离可观测量"的桥梁。实际计算中的核心工程问题是：如何获得一个足够精确的 Dyson 轨道，并将其与一个足够精确的连续态耦合。

**最强证据**：

[资料事实] Tenorio, Ponzi, Coriani & Decleva 2022 (Molecules 27, 1203) 实现了 MS-CASPT2 Dyson 轨道与 B-spline DFT/TDDFT 连续态的耦合。该工作的关键在于：Dyson 轨道在 OpenMolcas 中计算（利用完整 Abel 群对称性和修正归一化），然后传递给 Tiresia 代码计算连续态和光电离截面。这是一个"两步走"的工程方案。

[资料事实] Moitra, Coriani & Decleva 2021 (JCTC 17, 5064) 实现了 EOM-CCSD Dyson 轨道与 B-spline TDDFT 连续态的耦合，在单通道近似下描述分子光电离。该工作明确指出目标是在 B-spline DFT 处理中捕获缺失的通道间耦合效应，并探索 Dyson 轨道对强关联效应的响应。

[资料事实] Gozem & Krylov 的 ezDyson 代码使用平面波或 Coulomb 波描述连续态，配合 EOM-CCSD Dyson 轨道计算光电离截面。这种方案的工程优势在于简洁——无需 B-spline 连续态计算，但代价是连续态描述精度有限。

**只有实践者会告诉你的事**：Dyson 轨道计算的真正瓶颈不在于获取轨道本身（现代程序都能做到），而在于"接口工程"——不同量子化学程序之间的数据传递（轨道系数、重叠矩阵、对称性信息）极易出错。Tenorio 2022 的 OpenMolcas-Tiresia 接口和 ezDyson 的 Q-Chem 接口都是大量工程调试的结果。

---

### 视角二：学者（研究 Dyson 轨道数学基础的理论化学家）

**核心立场**：Dyson 轨道的精确计算本质上是一个**多参考问题**。当 Koopmans 图像失效（卫星峰、强关联体系）时，Dyson 轨道不再是单一分子轨道的简单修正，而是多个轨道的复杂线性组合，需要高阶电子关联方法才能正确描述。

**最强证据**：

[资料事实] Cederbaum 1973 (Theor. Chim. Acta 31, 239) 首次将单粒子 Green 函数方法用于直接计算闭壳层分子的电离势，奠定了 ADC（代数图构造）方法的数学基础。ADC 方法的核心思想是通过微扰展开系统近似 Green 函数的自能算符（self-energy），从而获得精确的电离能和 Dyson 轨道。

[资料事实] Ortiz 2020 (J. Chem. Phys. 153, 070902) 系统论述了 Dyson 轨道概念在描述分子中电子的精确极限中的作用。Dyson 轨道与自然轨道、Kohn-Sham 轨道、Hartree-Fock 轨道之间的关系表明，Dyson 轨道提供了唯一定义的单电子波函数，其概率因子在 0 到 1 之间。

[资料事实] 电子传播子方法（P3+, NR2, ADC(3) 等）直接求解 Dyson 方程获得电离能和 Dyson 轨道，无需计算 N−1 电子态波函数。Corzo, Galano, Dolgounitcheva, Zakrzewski & Ortiz 2015 (J. Phys. Chem. A 119, 8813) 证明 NR2 和 P3+ 方法在精度和效率上均优于传统的 OVGF 方法。

**只有学者会告诉你的事**：Dyson 轨道有一个被忽视的数学性质——它可以是复值的。在 EOM-CC 框架中，由于相似变换哈密顿量的非厄米性，左 Dyson 轨道和右 Dyson 轨道不同，需要取几何平均 $\sqrt{\|\phi^L\| \cdot \|\phi^R\|}$ 作为谱强度。这一非厄米性在 Q-Chem 的 ccman2 实现中被仔细处理，但在其他程序中可能被忽略。

---

### 视角三：怀疑者（认为 Dyson 轨道方法存在根本性局限的方法论竞争者）

**核心立场**：Dyson 轨道方法本质上是**单通道近似**——它假设光电离过程可以用"一个电子从一个轨道被击出"来描述。对于涉及强烈通道间耦合的体系（如近阈共振、自电离态、双电离），Dyson 轨道方法可能给出定性错误的结果。

**最强证据**：

[资料事实] 标准 Dyson 轨道方法（Tenorio 2022, Moitra 2021）均在"单通道近似"（single-channel approximation）下工作——每个电离通道独立处理，通道间耦合被忽略。Tenorio 2022 明确指出其 MS-CASPT2/B-spline 方案"限于单通道 Dyson 轨道近似，多通道耦合尚未纳入"。

[资料事实] Ruberti 2019 (JCTC 15, 3635) 提出的 RCS-ADC 方法通过限制关联空间的多中心 B-spline ADC 方案，**天然包含了通道间耦合**（interchannel coupling）。RCS-ADC 的 close-coupling 结构自动涌现，无需显式 Dyson 轨道构造。这是对 Dyson 轨道单通道近似的直接竞争方案。

[资料事实] R-matrix 方法（UKRmol+）通过内区精确 CI + 外区散射理论，自然处理多通道耦合。虽然不直接使用 Dyson 轨道语言，但在多通道耦合处理上比单通道 Dyson 方案更完整。

**怀疑者会指出的问题**：Dyson 轨道方法的"精确束缚态 + 近似连续态"组合策略存在内在不对称——束缚态用高阶关联方法（CASPT2, EOM-CCSD），连续态用 DFT/TDDFT 或平面波/Coulomb 波。这种"混合精度"可能导致系统误差，特别是在连续态描述不足时（如形状共振、Cooper 极小附近）。

---

### 视角四：经济学家（关注软件生态和用户基础的观察者）

**核心立场**：Dyson 轨道方法的影响力不取决于理论精度排名，而取决于**软件可用性和用户门槛**。能够"一键计算"的程序才有真正的用户基础。

**最强证据**：

[资料事实] Gaussian 16 内置了完整的电子传播子方法（OVGF, P3+, NR2, ADC(3)），Ortiz 课题组在 Auburn 大学维护了详细的 Gaussian EPT 教程。这使得 Dyson 轨道计算可以通过标准 Gaussian 输入关键词直接触发，用户门槛极低。

[资料事实] Q-Chem 通过 ccman2 模块实现了 EOM-CCSD Dyson 轨道计算，配合 ezDyson 后处理代码可以计算光电离截面和角分布。Q-Chem 手册提供了完整的作业控制关键词（`CC_DO_DYSON = TRUE`）和示例输入。

[资料事实] PySCF 作为开源 Python 量子化学程序，实现了 ADC(2)/ADC(2)-x/ADC(3) 方法的 IP/EA 变体，并可直接计算 Dyson 轨道（`myadc.compute_dyson_mo()`）。这为零成本入门提供了途径。

[资料事实] OpenMolcas 在 Tenorio 2022 的工作中实现了具有完整 Abel 群对称性和修正归一化的 Dyson 轨道计算，并与 Tiresia B-spline 连续态代码接口。

[资料事实] ORCA 生态中，第三方工具 dyson-orca-tools（Andres Ortega-Guerrero, Gonçalo Catarina, EMPA）可以从 ORCA 的 CASCI/CASSCF JSON 输出中提取 Dyson 轨道。

**只有经济学家会告诉你的事**：Tiresia 代码虽然方法学最为系统，但作为独立 Fortran 代码部署，用户门槛远高于 Gaussian/Q-Chem 的内置功能。Dyson 轨道方法要真正普及，关键不在于理论方法的进一步精确化，而在于将 B-spline 连续态计算整合进主流量子化学程序的"一键工作流"中。

---

### 视角五：历史学家（关注方法学谱系和演进脉络的观察者）

**核心立场**：Dyson 轨道方法的发展史是"从 Green 函数到耦合簇再到多参考"的三阶段演进，每一步都由计算能力的增长和新物理问题的驱动。

**最强证据**：

[资料事实] **第一阶段（1970s-1990s）：Green 函数/传播子方法。** Cederbaum 1973 提出 Green 函数直接计算电离势。此后 OVGF（外价 Green 函数）、2ph-TDA、ADC(n) 等系列方法在 Heidelberg（Cederbaum 组）和 Auburn（Ortiz 组）发展成熟。这些方法直接求解 Dyson 方程获得 Dyson 轨道，无需显式 N−1 电子态计算。

[资料事实] **第二阶段（2000s-2010s）：EOM-CC Dyson 轨道。** Oana & Krylov 2007 (JCP 127, 234106) 和 2009 (JCP 131, 124114) 在 Q-Chem 中实现了 EOM-IP/EA-CCSD 框架下的 Dyson 轨道计算。Vidal, Krylov & Coriani 2020 (PCCP 22, 2693) 进一步扩展到 fc-CVS-EOM-CCSD 框架，用于 X 射线光电子能谱。EOM-CC 方法的优势是系统可控的关联层次和适用于开壳层体系。

[资料事实] **第三阶段（2020s）：多参考 Dyson 轨道 + 精确连续态。** Tenorio 2022 的 MS-CASPT2 Dyson 轨道 + B-spline TDDFT 连续态代表了当前最完整的方案——多参考方法描述初末态关联，B-spline 方法精确描述连续态。Moitra 2021 的 EOM-CC + B-spline 方案则代表了耦合簇路线的最新进展。

[资料事实] Decleva 课题组 2022 年的 Tiresia 综述（Molecules 27, 2026）明确提出了**四层方法学层次**：静态 DFT → TDDFT → Dyson-DFT → Dyson-TDDFT，将 Dyson 轨道作为连续态计算框架中的标准初态描述层次。

**只有历史学家会告诉你的事**：Dyson 轨道方法的"两步走"策略（先计算 Dyson 轨道，再耦合连续态）实际上是一种历史妥协。理想方案应是在统一框架内同时精确描述束缚态和连续态（如 Ruberti 的 RCS-ADC），但这类方法的实现复杂度远高于两步走方案。历史演进的方向正在从"两步走"向"统一框架"缓慢移动。

---

## 三、矛盾图谱

### 3.1 视角间冲突

| 冲突点 | 冲突双方 | 依据强弱 |
|--------|---------|----------|
| **单通道 Dyson vs 多通道 RCS-ADC** | 怀疑者认为单通道近似根本不足；实践者认为对主峰已足够 | 两者各有适用域：单通道适合远离共振的主峰区域；多通道适合近阈共振和卫星峰 |
| **平面波/Coulomb 波 vs B-spline 连续态** | 经济学家赞赏 ezDyson 的简洁；实践者强调 B-spline 的精度 | Gozem et al. 2015 (JPCL 6, 4532) 证明：对中性分子光电离必须用 Coulomb 波（Z=+1），平面波严重失效；但 Coulomb 波仍无法描述形状共振 |
| **EOM-CC vs CASPT2 Dyson 轨道** | 学者认为 EOM-CC 系统可控；实践者认为 CASPT2 对强关联体系更优 | EOM-CCSD 适合弱到中等关联；MS-CASPT2 适合强关联（卫星峰、多参考态） |
| **传播子直接求解 vs 显式 N/(N−1) 波函数** | 学者赞赏传播子效率；历史学家指出传播子对卫星峰描述有限 | 传播子方法（P3+, NR2, ADC(3)）可直接获得全部电离谱，但高阶卫星峰需 ADC(3) 或更高 |

### 3.2 共识清单

1. **Dyson 轨道是光电离理论的核心单电子量**：无论用何种方法计算，Dyson 轨道都是连接束缚态电子结构与连续态光电离观测量的标准桥梁。
2. **连续态描述精度是瓶颈**：Dyson 轨道本身可以用高阶方法精确计算，但连续态的描述（平面波 → Coulomb 波 → B-spline DFT → B-spline TDDFT）才是决定截面精度的关键因素。
3. **多参考方法对卫星峰不可或缺**：对于电子关联效应显著的体系（如 CS, SiS 的卫星带），单参考方法（HF, DFT, CCSD）不足以描述 Dyson 轨道，必须使用 MS-CASPT2 或更高阶方法。
4. **软件可用性决定方法影响力**：Gaussian EPT、Q-Chem/ezDyson 的内置实现使 Dyson 轨道方法获得了远超纯学术方法的用户基础。

### 3.3 盲区清单

1. **机器学习对 Dyson 轨道计算的潜在冲击**：当前所有方法均为传统 ab initio，未讨论神经网络波函数或 ML 势能面在 Dyson 轨道计算中的可能应用。
2. **相对论效应对重原子 Dyson 轨道的影响**：虽然 Q-Chem 实现了 fc-CVS-EOM-CCSD 用于核心电离，但四分量相对论 Dyson 轨道的系统发展仍不充分。
3. **GPU 加速**：所有主流实现均为 CPU 架构，GPU 加速可能显著改变大规模 Dyson 轨道计算的成本-效益比。
4. **与量子化学软件的深度整合**：Tiresia 作为独立代码与主流程序接口有限，真正的"一键计算"工作流尚不存在。

---

## 四、量子化学方法分类

计算 Dyson 轨道的量子化学方法可分为三大类，以下系统梳理。

### 4.1 第一类：电子传播子 / Green 函数方法（直接求解 Dyson 方程）

**核心思想**：直接求解 Dyson 方程 $[\hat{h}_0 + \hat{\Sigma}(\omega)] \phi^{Dyson} = \omega \, \phi^{Dyson}$，无需显式计算 N 和 N−1 电子态波函数。电离能是 Dyson 方程的本征值，Dyson 轨道是本征函数。

| 方法 | 全称 | 关联层次 | 计算标度 | 代表程序 | 特点 |
|------|------|---------|---------|---------|------|
| **OVGF** | Outer Valence Green Function | 二阶微扰 | O(N⁵) | Gaussian | 三个版本（A/B/C），外价区域高效 |
| **P3 / P3+** | Partial Third-Order / Renormalized P3 | 三阶微扰 | O(N⁵) | Gaussian | 闭壳层分子价电离能，精度优于 OVGF |
| **NR2** | Non-diagonal Renormalized 2nd order | 二阶重整化 | O(N⁶) 非迭代 | Gaussian | 非对角自能，处理强关联效应 |
| **ADC(n)** | Algebraic Diagrammatic Construction | n 阶微扰 | ADC(2): O(N⁵), ADC(3): O(N⁶) | PySCF, Gaussian | 系统可改进的微扰层次 |
| **2ph-TDA** | Two-Particle-Hole Tamm-Dancoff | 二阶 | O(N⁵) | Gaussian | 用于卫星峰初步描述 |

**优势**：
- 直接获得完整电离谱（主峰 + 卫星峰），无需逐态计算
- Dyson 轨道作为本征函数自然获得
- 计算效率高（避免分别计算 N 和 N−1 态）

**局限**：
- 低阶方法（OVGF, P3）对卫星峰描述不足
- 高阶方法（ADC(3), NR2）计算成本显著增加
- 对核心电离和强关联体系适用性有限

**关键文献**：
- Cederbaum 1973 (Theor. Chim. Acta 31, 239) — Green 函数方法奠基
- Ortiz 2013 (WIREs CMS 3, 123) — 电子传播子理论综述
- Ortiz 2020 (JCP 153, 070902) — Dyson 轨道概念综述
- Opoku, Pawłowski & Ortiz 2024 (J. Phys. Chem. A 128, 1399) — 新一代传播子方法

---

### 4.2 第二类：耦合簇方法（EOM-CC Dyson 轨道）

**核心思想**：用 EOM-IP-CCSD（电离等效方程运动耦合簇）描述 (N−1) 电子态，用 CCSD 描述 N 电子参考态。Dyson 轨道为两态间的单电子跃迁密度矩阵。

| 方法 | 描述 | 代表程序 | 特点 |
|------|------|---------|------|
| **EOM-IP-CCSD** | 单双激发电离 EOM-CC | Q-Chem | 标准 Dyson 轨道计算 |
| **EOM-EA-CCSD** | 单双激发电子附着 EOM-CC | Q-Chem | 用于开壳层体系（如阴离子光电子谱） |
| **fc-CVS-EOM-IP-CCSD** | 冻结芯-核心价分离 EOM-CC | Q-Chem | 用于 X 射线光电子能谱（XPS） |
| **EOM-CCSDT** | 含三激发的 EOM-CC | MRCC | 更高精度，计算成本高 |

**数学形式**：

由于 CC 的左、右矢量不同，存在左 Dyson 轨道和右 Dyson 轨道：

$$\gamma_p^R = \langle \Phi_0 e^{T_1+T_2} L^{EE} | p^+ | R^{IP} e^{T_1+T_2} \Phi_0 \rangle$$

$$\gamma_p^L = \langle \Phi_0 e^{T_1+T_2} L^{IP} | p | R^{EE} e^{T_1+T_2} \Phi_0 \rangle$$

谱强度取几何平均：$\|\phi^{Dyson}\|^2 = \sqrt{\|\phi^L\| \cdot \|\phi^R\|}$

**优势**：
- 系统可控的关联层次（CCSD → CCSDT → CCSDTQ）
- 适用于开壳层和闭壳层体系
- 核心电离可通过 fc-CVS 框架处理
- Q-Chem/ezDyson 生态成熟，用户门槛低

**局限**：
- CCSD 对强关联体系（双激发态、圆锥交叉）描述不足
- 非厄米性导致左右 Dyson 轨道不同，需要几何平均处理
- 计算标度 O(N⁶)，大分子成本高

**关键文献**：
- Oana & Krylov 2007 (JCP 127, 234106) — EOM-CC Dyson 轨道理论
- Oana & Krylov 2009 (JCP 131, 124114) — 微分截面计算
- Vidal, Krylov & Coriani 2020 (PCCP 22, 2693) — fc-CVS-EOM-CCSD 用于 XPS
- Gozem et al. 2015 (JPCL 6, 4532) — 平面波 vs Coulomb 波基准测试
- Moitra, Coriani & Decleva 2021 (JCTC 17, 5064) — EOM-CC + B-spline 耦合

---

### 4.3 第三类：多参考方法（MS-CASPT2 / CASSCF / CASCI Dyson 轨道）

**核心思想**：用多参考方法（CASSCF, CASPT2, MRCI）描述 N 和 N−1 电子态，Dyson 轨道为两态间的重叠积分。对强关联体系（卫星峰、多参考态）不可或缺。

| 方法 | 描述 | 代表程序 | 特点 |
|------|------|---------|------|
| **MS-CASPT2** | 多态完全活性空间二阶微扰 | OpenMolcas | 当前最完整的多参考 Dyson 轨道方案 |
| **CASSCF/CASCI** | 完全活性空间自洽场/CI | OpenMolcas, ORCA | 未含动态关联，作为 CASPT2 的参考 |
| **MRCI** | 多参考 CI | MOLPRO, ORCA | 更高精度，计算成本极高 |
| **RASPT2** | 限制活性空间微扰 | OpenMolcas | CASPT2 的变体，更大活性空间 |

**Tenorio 2022 的 MS-CASPT2/B-spline 方案**：

1. 在 OpenMolcas 中用 MS-CASPT2 计算 N 和 N−1 电子态波函数
2. 计算 Dyson 轨道 $\phi^{Dyson} = \sqrt{N} \langle \Psi_f^{N-1} | \Psi_i^N \rangle$（利用完整 Abel 群对称性）
3. 将 Dyson 轨道传递给 Tiresia 代码
4. 在 Tiresia 中用 B-spline DFT/TDDFT 计算连续态
5. 计算 $\langle \phi^{Dyson} | \hat{r} | \Psi_{cont} \rangle$ 得到光电离截面和不对称参数

**优势**：
- 对强关联体系（卫星峰、双激发态）描述准确
- MS-CASPT2 可处理态间的混合（多态效应）
- 与 B-spline 连续态耦合可获得精确光电离可观测量

**局限**：
- 活性空间选择需要经验
- 计算成本高
- 当前实现限于单通道近似（多通道耦合尚未纳入）
- OpenMolcas-Tiresia 接口工程复杂

**关键文献**：
- Tenorio, Ponzi, Coriani & Decleva 2022 (Molecules 27, 1203) — MS-CASPT2 Dyson + B-spline
- Decleva, Stener & Toffoli 2022 (Molecules 27, 2026) — Tiresia 综述，四层方法学层次
- Toffoli, Coriani, Stener & Decleva 2023 (CPC 297, 109038) — Tiresia 代码发布

---

### 4.4 补充：RCS-ADC 方法（统一框架替代方案）

Ruberti 2019 (JCTC 15, 3635) 提出的限制关联空间 B-spline ADC 方法不属于上述三类，而是**统一框架**——在 B-spline 基中同时描述束缚态和连续态，天然包含通道间耦合。

**核心思想**：通过限制关联空间（RCS）降低 ADC 方法的计算成本，在多中心 B-spline 基中实现 RCS-ADC(1)/ADC(2)/ADC(2)x，close-coupling 结构自动涌现。

**与 Dyson 轨道方法的关系**：RCS-ADC 不显式计算 Dyson 轨道，但通过 ADC 中间态表示（ISR）描述的电离态等效于 Dyson 轨道框架，且**自动包含多通道耦合**。这是对单通道 Dyson 轨道方法的根本性改进方向。

**关键文献**：
- Ruberti 2019 (JCTC 15, 3635) — RCS-ADC 理论和实现
- Ruberti 2019 (PCCP 21, 17584) — TD-RCS-ADC 用于阿秒电离动力学
- Gokhberg et al. 2009 (JCP 130, 064104) — ADC-Stieltjes-Lanczos 方法奠基
- Ruberti et al. 2013 (JCP 139, 144107) — ADC-SL 基准测试

---

## 五、主流量子化学程序

### 5.1 程序总览

| 程序 | Dyson 轨道方法 | 连续态处理 | 光电离截面 | 开源 | 语言 |
|------|--------------|-----------|----------|------|------|
| **Gaussian 16** | OVGF, P3+, NR2, ADC(3), 2ph-TDA | 无内置 | 无内置 | 否 | Fortran |
| **Q-Chem** | EOM-IP/EA-CCSD, fc-CVS-EOM-CCSD | 平面波/Coulomb 波（ezDyson） | 有（ezDyson） | 否 | C++/Fortran |
| **OpenMolcas** | MS-CASPT2, CASSCF | B-spline（Tiresia 接口） | 有（Tiresia） | 是 | Fortran |
| **PySCF** | ADC(2)/ADC(2)-x/ADC(3) IP/EA | 无内置 | 无内置 | 是 | Python |
| **ORCA** | CASCI/CASSCF（第三方工具） | 无内置 | 无内置 | 否 | Fortran/C++ |
| **Tiresia** | 接收外部 Dyson 轨道 | B-spline DFT/TDDFT | 有 | 是（CPC发布） | Fortran |
| **ePolyScat** | 接收外部轨道（HF/KS） | 单中心展开 + Schwinger 变分 | 有 | 需申请 | Fortran |
| **UKRmol+** | R-matrix 框架（不显式用 Dyson） | GTO + B-spline R-matrix | 有 | 是 | Fortran |
| **ezDyson** | 接收 Q-Chem Dyson 轨道 | 平面波/Coulomb 波 | 有 | 免费 | C++ |
| **MRCC** | EOM-CCSDT（高阶） | 无内置 | 无内置 | 部分免费 | Fortran |

---

### 5.2 各程序详细说明

#### 5.2.1 Gaussian 16 — 电子传播子方法的标杆

Gaussian 16 是电子传播子方法（EPT）最完整的内置实现平台。Ortiz 课题组在 Auburn 大学维护了详细的 EPT 教程和示例输入。

**支持的 EPT 方法**：
- OVGF（版本 A/B/C）：外价 Green 函数，二阶微扰
- P3 / P3+：部分三阶 / 重整化部分三阶
- NR2：非对角重整化二阶
- ADC(3)：三阶代数图构造
- 2ph-TDA：双粒子-空穴 Tamm-Dancoff 近似
- 3+：重整化三阶

**使用方式**：通过标准 Gaussian 输入关键词触发，例如：
```
#p EPT(NR2,ReadOrbitals)/cc-pVTZ
```

**Dyson 轨道输出**：EPT 计算输出 Dyson 轨道在正则 HF 轨道基中的展开系数和谱强度。

**连续态处理**：Gaussian 本身**不包含**连续态计算功能。如需光电离截面，需配合外部工具（如 ezDyson 或 Stieltjes 成像后处理）。

**适用场景**：快速获得电离能谱和 Dyson 轨道；价区域电离能预测；电子动量谱（EMS）对比。

---

#### 5.2.2 Q-Chem + ezDyson — EOM-CC Dyson 轨道的标准工作流

Q-Chem 通过 ccman2 模块实现了 EOM-IP/EA-CCSD Dyson 轨道，配合独立的 ezDyson 代码计算光电离截面和角分布。

**Q-Chem 端的 Dyson 轨道计算**：
```
$rem
  correlation = CCSD
  basis = aug-cc-pVTZ
  ip_states = [N,N]        ! 请求特定对称性的 IP 态
  ccman2 = true
  cc_trans_prop = true
  cc_do_dyson = true       ! 计算 Dyson 轨道
  molden_format = 1        ! MOLDEN 格式输出（可视化）
$end
```

**ezDyson 端的截面计算**：
- 输入：Q-Chem 输出的 Dyson 轨道（XML 格式）
- 连续态选项：平面波（PW）或 Coulomb 波（CW，Z=+1）
- 输出：总截面、微分截面、β 参数、分子框架角分布

**关键发现**（Gozem et al. 2015, JPCL）：
- 对**阴离子光剥离**：平面波即可获得良好结果
- 对**中性分子光电离**：必须使用 Coulomb 波（Z=+1），平面波严重失效
- Coulomb 波仍无法描述形状共振和 Cooper 极小

**ezSpectra 套件**：ezDyson 是 ezSpectra 套件的一部分，还包括 ezSpectrum（Franck-Condon 因子计算）。

---

#### 5.2.3 OpenMolcas + Tiresia — 多参考 Dyson 轨道的最完整方案

OpenMolcas + Tiresia 组合是目前唯一实现了**多参考 Dyson 轨道 + 精确 B-spline 连续态**的完整工作流。

**OpenMolcas 端**：
- MS-CASPT2 计算 N 和 N−1 电子态
- Dyson 轨道计算利用完整 Abel 群对称性
- 修正的归一化方案
- 输出 Dyson 轨道在 AO 基中的系数

**Tiresia 端**（Toffoli et al. 2023, CPC）：
- 多中心 B-spline × 球谐函数基组
- 四层方法学：静态 DFT → TDDFT → Dyson-DFT → Dyson-TDDFT
- MPI 并行化，基于 ScaLAPACK
- 输出：截面、β 参数、分支比

**方法学层次**（Decleva 2022 提出的四层框架）：

| 层次 | 初态 | 连续态 | 适用场景 |
|------|------|--------|---------|
| 静态 DFT | KS 轨道 | DFT 势 B-spline | 快速估算，弱关联 |
| TDDFT | KS 轨道 | TDDFT B-spline | 中等关联，中等分子 |
| Dyson-DFT | Dyson 轨道 | DFT 势 B-spline | 多参考初态，弱连续态关联 |
| Dyson-TDDFT | Dyson 轨道 | TDDFT B-spline | 最完整方案，强关联初态 |

**适用场景**：卫星峰计算、强关联体系光电离、精确截面和角分布。

---

#### 5.2.4 PySCF — 开源 ADC 方法平台

PySCF 实现了 ADC(2)/ADC(2)-x/ADC(3) 的 IP 和 EA 变体，可直接计算 Dyson 轨道。

```python
from pyscf import gto, scf, adc

mol = gto.M(atom='H 0 0 0; F 0 0 1', basis='ccpvdz')
mf = scf.RHF(mol).run()

myadc = adc.ADC(mf)
myadc.method = "adc(3)"
myadc.method_type = "ip"
eip, vip, pip, xip = myadc.kernel()

# 直接计算 Dyson 轨道
dyson_orb = myadc.compute_dyson_mo()
```

**特点**：
- 完全开源（Python），便于修改和扩展
- 支持 RHF/UHF/ROHF 参考
- IP-ADC 和 EA-ADC 均支持
- Dyson 轨道直接从 ADC 谱振幅计算

**局限**：
- 无内置连续态计算
- ADC(3) 的计算成本较高
- 文档和示例相对 Q-Chem/Gaussian 较少

---

#### 5.2.5 ePolyScat — Schwinger 变分连续态方法

ePolyScat（Lucchese, Gianturco, Natalense 等）是分子光电离和电子散射计算的独立代码，基于**迭代 Schwinger 变分法**求解 Lippmann-Schwinger 方程。

**方法特点**：
- 连续态用单中心展开（对称性适配角谐函数 × 径向网格函数）
- 静态交换势描述电子-分子相互作用
- 可近似处理目标极化效应
- 支持完整点群对称性（含非 Abel 群）

**与 Dyson 轨道的关系**：ePolyScat 接收外部分子轨道（来自 Gaussian, GAMESS, MOLPRO），不显式计算 Dyson 轨道，但在单组态近似下使用的分子轨道等效于 Koopmans Dyson 轨道。

**优势**：精确的连续态描述，适合形状共振和角分布计算。
**局限**：单组态初态（未含关联），静态交换近似。

**后处理工具**：ePSproc（Hockett）提供 Python 后处理和可视化。

---

#### 5.2.6 UKRmol+ — R-matrix 方法

UKRmol+（Mašín, Benda, Gorfinkiel, Harvey, Tennyson 2020, CPC 249, 107092）是分子 R-matrix 方法的标准实现。

**方法特点**：
- 空间分区：内区（GTO + 可选 B-spline）精确描述电子关联，外区用解析散射函数
- 支持电子-分子碰撞和光电离
- 利用 Molpro 提供目标分子轨道
- MPI 并行化

**与 Dyson 轨道的关系**：UKRmol+ 不显式使用 Dyson 轨道语言，但内区的 CI 描述等效于多通道 Dyson 轨道框架。其多通道耦合处理是对单通道 Dyson 方案的重要补充。

---

#### 5.2.7 ORCA + dyson-orca-tools — 第三方工具生态

ORCA 本身不内置 Dyson 轨道计算，但第三方工具 dyson-orca-tools（Ortega-Guerrero & Catarina, EMPA）可以从 ORCA 的 CASCI/CASSCF JSON 输出中提取 Dyson 轨道。

**工作流**：
1. 在 ORCA 中运行 CASCI/CASSCF 计算
2. 用 `orca_2json` 将波函数转换为 JSON 格式
3. 用 dyson-orca-tools 计算 Dyson 轨道

**特点**：开源 Python 工具，适合 ORCA 生态用户。

---

### 5.3 程序间接口关系图

```
                    ┌──────────────┐
                    │  Gaussian 16 │
                    │ (OVGF,P3+,   │
                    │  NR2,ADC(3)  │
                    │  Dyson轨道)  │
                    └──────┬───────┘
                           │ Dyson轨道输出
                    ┌──────▼───────┐
                    │  ezDyson     │
                    │ (PW/CW连续态) │
                    │ → 截面/β     │
                    └──────────────┘

                    ┌──────────────┐
                    │   Q-Chem     │
                    │ (EOM-CCSD    │
                    │  Dyson轨道)  │
                    └──────┬───────┘
                           │ XML接口
                    ┌──────▼───────┐
                    │  ezDyson     │
                    │ (PW/CW连续态) │
                    │ → 截面/β/PAD │
                    └──────────────┘

  ┌──────────────┐   Dyson轨道   ┌──────────────┐
  │ OpenMolcas   │──────────────►│   Tiresia    │
  │ (MS-CASPT2   │   AO系数传递  │ (B-spline    │
  │  Dyson轨道)  │               │  DFT/TDDFT   │
  └──────────────┘               │  连续态)     │
                                 │ → 截面/β     │
                                 └──────────────┘

  ┌──────────────┐               ┌──────────────┐
  │   PySCF      │               │ ePolyScat    │
  │ (ADC(2/3)    │               │ (Schwinger   │
  │  Dyson轨道)  │               │  变分连续态)  │
  └──────────────┘               │ → 截面/β     │
                                 └──────────────┘
  ┌──────────────┐
  │    ORCA      │
  │ (CASCI/CASSCF│──► dyson-orca-tools ──► Dyson轨道
  │  JSON输出)   │
  └──────────────┘

  ┌──────────────┐
  │   MRCC       │
  │ (EOM-CCSDT   │
  │  高阶Dyson)  │
  └──────────────┘
```

---

## 六、综合简报

### 一段话总结

计算 Dyson 轨道的量子化学方法经历了从 Green 函数/传播子直接求解（1970s-1990s，Cederbaum/Ortiz 学派），到 EOM-CC Dyson 轨道（2000s-2010s，Krylov 学派），再到多参考 Dyson 轨道耦合精确 B-spline 连续态（2020s，Decleva/Coriani 学派）的三阶段演进。当前主流程序覆盖了从"一键计算"的 Gaussian EPT 和 Q-Chem/ezDyson 工作流，到最完整的 OpenMolcas/Tiresia 多参考方案，再到统一框架的 Ruberti RCS-ADC 方法，形成了从快速预测到精确计算的方法谱系。核心矛盾在于：单通道 Dyson 轨道近似虽对主峰区域足够，但多通道耦合（近阈共振、卫星峰）需要 RCS-ADC 或 R-matrix 等统一框架方法。

### 五个关键发现（按可靠性排序）

1. **电子传播子方法（P3+, NR2, ADC(3)）是计算价电离能和 Dyson 轨道的高效工具** (可靠性 10/10)
   — 证据：Ortiz 课题组数十年的基准测试和 Gaussian 中的成熟实现。

2. **EOM-CCSD Dyson 轨道配合 Coulomb 波可准确计算中性分子光电离截面** (可靠性 9/10)
   — 证据：Gozem et al. 2015 对 He, Ne, Ar, H₂, H₂O 的基准测试。平面波对中性分子失效，Coulomb 波（Z=+1）显著改善。

3. **MS-CASPT2 Dyson 轨道 + B-spline TDDFT 连续态是强关联体系光电离的最完整方案** (可靠性 8/10)
   — 证据：Tenorio 2022 对 CS 和 SiS 卫星峰的成功计算。但限于单通道近似。

4. **RCS-ADC 在 B-spline 基中天然包含多通道耦合，是单通道 Dyson 方案的根本性改进方向** (可靠性 7/10)
   — 证据：Ruberti 2019 对一系列分子的总截面基准测试。但实现复杂，用户基础小。

5. **连续态描述精度是光电离截面计算的瓶颈，而非 Dyson 轨道本身** (可靠性 9/10)
   — 证据：Gozem 2015 证明 PW vs CW 的差异远大于 CCSD vs CASPT2 Dyson 轨道的差异；Decleva 2022 的四层方法学明确区分了初态和连续态的关联层次。

### 隐藏关联

只有把**传播子方法**（直接求解 Dyson 方程，无需 N−1 态波函数）、**EOM-CC 方法**（显式计算 N/(N−1) 态，Dyson 轨道为跃迁密度矩阵）和**多参考方法**（CASPT2，处理强关联）放在一起才能看到：三者的数学本质相同——都是计算 N 与 N−1 电子态之间的单电子重叠——但实现策略完全不同。传播子方法绕过了显式 N−1 态计算，EOM-CC 用相似变换高效描述，多参考方法直接处理。选择哪种策略不取决于理论精度排名，而取决于**目标体系的相关强度**和**可用计算资源**。

### 行动建议

对于本项目（球面波基组光电离截面计算），建议：
1. **Dyson 轨道初态**：将 Dyson 轨道作为光电离初态的标准描述层次（对标 Decleva 四层框架中的 Dyson-DFT 层），替代简单的 Koopmans/HS 轨道。
2. **程序对接**：优先建立与 Gaussian EPT 输出和 OpenMolcas Dyson 轨道输出的接口，使本项目代码可以接收外部 Dyson 轨道作为初态。
3. **连续态精度**：关注 Coulomb 波 → B-spline → 球面波连续态的精度递进关系，本项目的球面波基组可作为 B-spline 的替代/补充方案。
4. **多通道**：跟踪 Ruberti RCS-ADC 的多通道耦合处理，为本项目未来的多通道扩展提供参考。

### 前沿问题

**"如何将多参考 Dyson 轨道与多通道连续态耦合在统一框架中实现，同时保持计算效率？"**

这个问题的答案将打通"精确束缚态多参考描述"和"精确连续态多通道耦合"之间的最后一道壁垒。当前 Tenorio 2022 的 MS-CASPT2 Dyson + B-spline 方案限于单通道，Ruberti 2019 的 RCS-ADC 含多通道但 Dyson 轨道为隐式。两者的融合——多参考 Dyson 轨道作为初态、RCS-ADC 描述多通道连续态——是下一代分子光电离计算的理论目标。

---

## 七、同行评审自检

### 可靠性打分

| 关键发现 | 分数 | 理由 |
|----------|------|------|
| 传播子方法高效可靠 | 10/10 | 50+ 年验证，Gaussian 成熟实现 |
| EOM-CC + CW 截面准确 | 9/10 | 多体系基准测试，但 CW 仍无法描述共振 |
| MS-CASPT2/B-spline 最完整 | 8/10 | 卫星峰成功计算，但单通道限制 |
| RCS-ADC 多通道改进 | 7/10 | 总截面基准验证，微分截面待充分测试 |
| 连续态是瓶颈 | 9/10 | Gozem 2015 直接证据，Decleva 四层框架佐证 |

### 最没把握的结论

"RCS-ADC 是单通道 Dyson 方案的根本性改进方向"这一结论的可靠性依赖于 RCS-ADC 在更多体系上的验证。目前 Ruberti 2019 的基准测试主要针对总截面（HF, NH₃, H₂O, CO₂, H₂CO, CH₄, C₂H₂, C₂H₄），微分截面和角分布的系统性验证尚不充分。

### 视角比重评估

在综合简报中，**实践者视角**（工程实现）和**历史学家视角**（方法演进）占据了较大比重，可能低估了**怀疑者视角**（单通道近似的根本性局限）的严重性。实际上，单通道近似在近阈共振区域和自电离态附近的失效可能比文中描述的更为普遍。

### 斯坦福教授评审假设

如果一位斯坦福教授评审本综述，可能会要求补充以下内容：

1. **双电离和 Auger 过程中的 Dyson 轨道**：本综述聚焦单光电离，双电离过程的 Dyson 轨道理论（涉及 N → N−2 的双电子重叠）未讨论。
2. **频率依赖（非绝热）自能对 Dyson 轨道的影响**：当前所有传播子方法均基于绝热近似，频率依赖自能（可描述双激发态）对 Dyson 轨道的影响未充分讨论。
3. **与实验的直接对比**：综述以方法学为主，缺少系统性的理论-实验对比表格。

---

## 八、方法选择决策树

```
目标：计算分子光电离截面
│
├─ 体系关联强度？
│  │
│  ├─ 弱关联（主峰区域，Koopmans 图像有效）
│  │  │
│  │  ├─ 快速估算电离能 → Gaussian EPT (P3+/NR2)
│  │  │
│  │  ├─ 需要截面 + β 参数
│  │  │  │
│  │  │  ├─ 远离共振 → Q-Chem EOM-CCSD + ezDyson (Coulomb波)
│  │  │  │
│  │  │  └─ 形状共振/精细角分布 → ePolyScat 或 Tiresia (B-spline)
│  │  │
│  │  └─ 开源方案 → PySCF ADC(2)/ADC(3) + 自定义连续态
│  │
│  ├─ 中等关联（部分卫星峰）
│  │  │
│  │  └─ Q-Chem EOM-CCSD Dyson + Tiresia B-spline TDDFT
│  │     (Moitra 2021 方案)
│  │
│  └─ 强关联（显著卫星峰，多参考态）
│     │
│     ├─ 单通道足够
│     │  │
│     │  └─ OpenMolcas MS-CASPT2 Dyson + Tiresia B-spline
│     │     (Tenorio 2022 方案) ← 当前最完整
│     │
│     └─ 需要多通道耦合
│        │
│        ├─ 总截面 → RCS-ADC + Stieltjes-Lanczos
│        │  (Ruberti 2019 方案)
│        │
│        └─ 微分截面 → UKRmol+ R-matrix (多通道CI)
│
├─ 核心电离（XPS）？
│  │
│  └─ Q-Chem fc-CVS-EOM-CCSD Dyson + ezDyson
│     (Vidal 2020 方案)
│
└─ 阴离子光剥离？
   │
   └─ Q-Chem EOM-EA-CCSD Dyson + ezDyson (平面波)
      (Gozem 2015 验证)
```

---

## 九、关键文献索引

### 种子文献（项目库内）

| 文献 | 方法贡献 | 项目路径 |
|------|---------|---------|
| Tenorio et al. 2022, Molecules 27, 1203 | MS-CASPT2 Dyson + B-spline | papers/B_spline_continuum/ |
| Decleva et al. 2022, Molecules 27, 2026 | Tiresia 综述，四层方法学 | papers/B_spline_continuum/ |
| Toffoli et al. 2023, CPC 297, 109038 | Tiresia 代码发布 | papers/GTO_continuum/ |
| Stener et al. 2005, JCP 122, 234301 | TDDFT-B-spline 非迭代算法 | papers/B_spline_continuum/ |
| Nisoli et al. 2017, Chem. Rev. 117, 10760 | 阿秒化学综述 | papers/general_review/ |

### 补充文献（网络检索）

| 文献 | 方法贡献 |
|------|---------|
| Cederbaum 1973, Theor. Chim. Acta 31, 239 | Green 函数直接计算电离势奠基 |
| Ortiz 2020, JCP 153, 070902 | Dyson 轨道概念综述 |
| Ortiz 2013, WIREs CMS 3, 123 | 电子传播子理论综述 |
| Opoku, Pawłowski & Ortiz 2024, JPCA 128, 1399 | 新一代传播子方法 |
| Oana & Krylov 2007, JCP 127, 234106 | EOM-CC Dyson 轨道理论 |
| Oana & Krylov 2009, JCP 131, 124114 | EOM-CC Dyson 微分截面 |
| Vidal, Krylov & Coriani 2020, PCCP 22, 2693 | fc-CVS-EOM-CCSD 用于 XPS |
| Gozem et al. 2015, JPCL 6, 4532 | 平面波 vs Coulomb 波基准 |
| Gozem & Krylov 2022, WIRES CMS 12, e1546 | ezSpectra 套件综述 |
| Moitra, Coriani & Decleva 2021, JCTC 17, 5064 | EOM-CC + B-spline 耦合 |
| Gunina & Krylov 2016, JPCA 120, 9841 | Dyson 轨道与实验可观测量 |
| Ruberti 2019, JCTC 15, 3635 | RCS-ADC B-spline 方法 |
| Ruberti 2019, PCCP 21, 17584 | TD-RCS-ADC 阿秒动力学 |
| Gokhberg et al. 2009, JCP 130, 064104 | ADC-Stieltjes-Lanczos 奠基 |
| Ruberti et al. 2013, JCP 139, 144107 | ADC-SL 基准测试 |
| Mašín et al. 2020, CPC 249, 107092 | UKRmol+ 代码发布 |
| Díaz-Tinoco, Pawłowski & Ortiz 2023 | Dyson 轨道与化学键 |

### 程序文献

| 程序 | 文献/网址 |
|------|---------|
| Gaussian EPT | auburn.edu/cosam/faculty/chemistry/ortiz/research/ept_gaussian.html |
| Q-Chem Dyson | manual.q-chem.com (§7.10.29) |
| ezDyson | iopenshell.usc.edu/downloads/ezdyson/ |
| PySCF ADC | pyscf.org/user/adc.html |
| Tiresia | Toffoli et al. 2023, CPC 297, 109038 |
| ePolyScat | epsproc.readthedocs.io |
| UKRmol+ | Mašín et al. 2020, CPC 249, 107092 |
| dyson-orca-tools | github.com/AndresOrtegaGuerrero/dyson-orca-tools |

---

*本文档基于风暴知识工坊 STORM 多视角研究法生成，综合了项目内 26 篇 PDF 文献、9 份现有笔记和 2026-07-20 的网络公开学术信息检索结果。所有方法描述和程序信息均标注了原始出处。*
