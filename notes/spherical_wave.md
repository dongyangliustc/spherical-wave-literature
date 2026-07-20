# 球面波展开与散射理论 — 读书笔记

> 目录: `papers/spherical_wave/` | 共 10 篇
> 主题: 球面波基组的数学基础、散射理论应用、TSW/ASW 等新型基组发展

---

## 1. Wilhelmy, Ackermann, Görling, Rösch — 1994 — Lobatto 技术

**文件**: `Wilhelmy_1994_Lobatto_photoionization_JCP.pdf`
**DOI**: `10.1063/1.466475`
**期刊**: J. Chem. Phys. 100, 2808
**优先级**: ⭐⭐⭐⭐

### 原理推导
- **Lobatto 形状函数** + GTO 混合基组描述连续态
- 基于 LDK（Logarithmic Derivative Kohn）变分原理
- 球谐函数 GTO（sGTO）作为角向基组，Lobatto 作为径向基组
- 局域有效势来自 DFT

### 方法创新
- Lobatto 函数：一种有限元基函数，在边界处精确满足波函数连续性
- 混合基组：GTO 描述内区、Lobatto 描述外区（连续区）
- LDKL（LDK Lobatto）方法：兼具变分精度和数值效率
- 对比 Stieltjes-Tchebychev (ST) 成像方法和 CMS 方法

### 程序拓展值得借鉴
- Lobatto 函数的实现（与 B-spline 的对比）
- 混合基组的分区策略（内区/外区）
- LDK 变分原理的数值实现
- 对本项目 continuum_wave.py 的三种连续态模型有参考价值

---

## 2. Domcke — 1983 — 投影算符散射

**文件**: `Domcke_1983_projection_scattering_PRA.pdf`
**DOI**: `10.1103/physreva.28.2777`
**期刊**: Phys. Rev. A 28, 2777
**优先级**: ⭐⭐⭐⭐

### 原理推导
- 投影算符形式理论（Feshbach 方法）应用于势散射
- 将 Hilbert 空间分为 P（束缚/共振态）和 Q（连续态）子空间
- 有效哈密顿量：$H_{\text{eff}} = PHP + PHQ(E - QHQ)^{-1}QHP$
- 共振的能量和宽度从 $H_{\text{eff}}$ 的复极点得到

### 方法创新
- 将 Feshbach 投影技术从核物理引入分子散射
- 提供共振-连续耦合的解析框架
- 给出 $i\varepsilon$ 极限的数学严格处理

### 程序拓展值得借鉴
- 投影算符的构造方法（对应本项目格林函数的投影分解）
- 共振参数提取的数值方法
- 与格林函数方法的内在联系（$G(E) = (E - H_{\text{eff}})^{-1}$）
- **本项目 $i\varepsilon$ 极限的处理可直接参考此处的形式理论**

---

## 3. Huang, Jin, Zhang, Chen, Li — 2026 — TSW NAO 基组

**文件**: `Huang_2026_TSW_NAO_basis_arXiv.pdf`
**DOI**: arXiv:2603.13995
**期刊**: arXiv 预印本
**优先级**: ⭐⭐⭐⭐⭐

### 原理推导
- **截断球面波（Truncated Spherical Wave, TSW）**：在有限半径 $R_c$ 处归零的球面 Bessel 函数
- TSW 满足：$j_l(k_{ln}r/R_c) \to 0$ 在 $r=R_c$ 处
- 截断消除了周期性边界条件下的虚假相互作用
- 动能算符迹极小化（Trace Minimization）优化 TSW 参数

### 方法创新
- TSW 作为 NAO 的原始函数：$|\phi_i\rangle = \sum_{l,n} c_{ln} |\text{TSW}_{ln}\rangle$
- 系统可改进性（Systematic Improvability）：通过增加 $R_c$ 可系统逼近完备基
- 对比传统平面波的局限：消除真空层镜像相互作用
- 在 ABACUS 软件包中的实现
- TD-DFT 光吸收谱计算结果展示了激发态描述精度的提升

### 程序拓展值得借鉴
- TSW 的构造与优化算法
- **本项目的球面波基组与 TSW 高度相似**：都使用截断球面波
- 区别：TSW 直接在实空间截断，本项目在动量空间表示
- 收敛性分析框架可直接借鉴
- ABACUS 开源实现可参考

---

## 4. Eyert — ASW 综述

**文件**: `Eyert_ASW_review.pdf`
**期刊**: Universität Augsburg 技术报告
**优先级**: ⭐⭐⭐⭐

### 原理推导
- **Augmented Spherical Wave (ASW)**：缀加球面波方法的历史综述
- MTO（Muffin-Tin Orbital）构造：原子球内的数值解 + 球 Hankel 函数缀加
- KKR 方法与 ASW 的关系：多重散射理论 → ASW → LAPW 的演进

### 方法创新
- ASW 到全势（Full-Potential）方法的演变
- 球面波基组的三大优势：局域性、可加性、原子轨道直观性
- 线性化方法（LMTO）：将能量依赖的 ASW 转化为线性基组

### 程序拓展值得借鉴
- Muffin-tin 分区策略
- 球面波缀加的数学细节
- **本项目的球面波基组可视为 ASW 的动量空间变体**
- ASW → LAPW → LCAO 的演进路径提供了方法学定位

---

## 5. Felderhof — 1987 — 矢量球面波加法定理

**文件**: `Felderhof_1987_addition_theorems_JMP.pdf`
**DOI**: `10.1063/1.527277`
**期刊**: J. Math. Phys. 28, 836
**优先级**: ⭐⭐⭐⭐

### 原理推导
- 矢量 Helmholtz 方程的球面波解在坐标平移下的变换
- 加法定理：$j_l(kr)Y_{lm}(\hat{\mathbf{r}}) = \sum_{l'm'} C_{lml'm'} j_{l'}(kr')Y_{l'm'}(\hat{\mathbf{r}}')$
- 标量→矢量推广：考虑矢量球面谐波 M, N, L 三种模式
- 位移系数用 Gaunt 系数和 Clebsch-Gordan 系数表示

### 方法创新
- 统一推导标量和矢量加法定理
- 解决了多中心球面波展开的核心数学工具问题
- 适用于 T-matrix 方法和多粒子散射

### 程序拓展值得借鉴
- **本项目中 angular_reduction.py 的 Bessel 函数展开直接依赖此理论**
- 多中心 GTO 的球面波展开需要加法定理
- 位移算子的数值实现

---

## 6. Weinberg — 1994 — 任意自旋球面波

**文件**: `Weinberg_1994_spinor_spherical_wave_JMP.pdf`
**DOI**: `10.1063/1.531282`
**期刊**: J. Math. Phys. 35, 5000
**优先级**: ⭐⭐⭐

### 原理推导
- 将球面波展开推广到任意自旋和质量的相对论性粒子
- 螺旋度本征态的球面波展开
- 自旋-轨道耦合的自然纳入

### 方法创新
- 普遍性自旋球谐函数的构造
- 任意自旋粒子的多极辐射场形式

### 程序拓展值得借鉴
- 本项目的非相对论性框架暂不直接需要
- 但为未来相对论性延伸提供了理论基础

---

## 7. Gonis, Butler — 1999 — 多重散射理论（书）

**文件**: `Gonis_Butler_1999_multiple_scattering_Springer.pdf`
**DOI**: `10.1007/978-1-4612-1290-4`
**出版社**: Springer
**优先级**: ⭐⭐⭐

### 原理推导
- 多重散射理论的完整形式体系
- Green 函数法和 KKR 方法
- 球面波展开在周期性体系中的应用
- 能带结构计算中的 MTO/ASW 方法

### 程序拓展值得借鉴
- 多重散射的数学框架（可能对本项目的多中心问题有参考价值）
- KKR 中 Green 函数的球面波表示（联系本项目的动量空间 Green 函数）
- **参考章节**：第 2 章（Green 函数）、第 4 章（球面波展开）

---

## 8. Moroz — 2006 — 准周期 Green 函数

**文件**: `Moroz_2006_quasi_periodic_Green_JPDA.pdf`
**DOI**: `10.1088/0305-4470/39/36/009`
**期刊**: J. Phys. A: Math. Gen. 39, 11247
**优先级**: ⭐⭐⭐

### 原理推导
- Helmholtz 方程准周期 Green 函数的级数表示
- 在部分维度具有周期性的情况下，Green 函数的 Schwinger 表示
- 格子求和（Lattice Sums）的球面波展开

### 方法创新
- 指数收敛的 Schlömilch 级数表示
- 任意 Bloch 动量下的快速数值求值

### 程序拓展值得借鉴
- 球面波格林函数在周期体系中的处理
- 对数奇点 / 极点分离的数值技巧
- **本项目的 $1/(p^2-k^2-i\varepsilon)$ 极点处理与 lattice sum 的极点处理有共同数学结构**

---

## 9. Egel et al. — 2024 — MLFMA 超表面

**文件**: `Egel_2024_MLFMA_metasurfaces_arXiv.pdf`
**DOI**: arXiv:2407.21724
**优先级**: ⭐⭐

### 原理推导
- 多级快速多极子算法（MLFMA）在电磁超表面散射中的应用
- 球面波平移算子的对角化
- 静态模式的低秩表示

### 方法创新
- MLFMA 中球面波展开的加速策略
- 超表面的远场/近场统一处理

### 程序拓展值得借鉴
- 对角化平移算子的数值技巧
- 快速多极子方法在声学/电磁学中的应用

---

## 10. Fruhnert et al. — 2024 — T-matrix 数据格式

**文件**: `Fruhnert_2024_Tmatrix_data_format_arXiv.pdf`
**DOI**: arXiv:2408.10727
**优先级**: ⭐⭐

### 原理推导
- T-matrix 方法的标准化数据格式提案
- 过渡矩阵（T-matrix）在球面波基下的表示
- Daphona 平台的数据模型

### 方法创新
- 标准化的 T-matrix 数据格式
- 与机器学习框架（PyTorch）的接口

### 程序拓展值得借鉴
- 球面波基下的数据存储格式
- 开放数据平台理念

---

## 本目录核心贡献总结

| 主题 | 关键论文 | 与本项目关联度 |
|------|---------|--------------|
| GTO+球面波混合基组 | Wilhelmy 1994 (Lobatto) | ⭐⭐⭐⭐ |
| 投影算符/格林函数 | Domcke 1983 | ⭐⭐⭐⭐ |
| 截断球面波基组 (TSW) | Huang 2026 (arXiv) | ⭐⭐⭐⭐⭐ |
| 缀加球面波方法 (ASW) | Eyert ASW Review | ⭐⭐⭐⭐ |
| 球面波加法定理 | Felderhof 1987 | ⭐⭐⭐⭐ |
| 多重散射理论 | Gonis & Butler 1999 | ⭐⭐⭐ |
| 准周期格林函数 | Moroz 2006 | ⭐⭐⭐ |

---

## 术语表

> 按本笔记中出现的顺序整理。出处为本目录所列对应论文（"#编号"指上文小节序号）。

1. **Lobatto 形状函数** (Lobatto shape functions) — 基于 Lobatto 求积节点构造的有限元基函数，在单元边界处为非零，从而精确保证相邻单元波函数连续性。出处：Wilhelmy 1994 #1。
2. **LDK / LDKL** (Logarithmic Derivative Kohn) — 以波函数对数导数为变分对象的 Kohn 变分版本；LDKL 指其 Lobatto 实现，兼具变分精度与数值效率。出处：Wilhelmy 1994 #1。
3. **sGTO** (spherical GTO) — 球谐化的高斯型轨道，作为角向基组与 Lobatto 径向基配套。出处：Wilhelmy 1994 #1。
4. **Stieltjes-Tchebychev (ST) 成像** — 从 $L^2$ 离散赝谱的矩重构连续截面的算法，此处作为 LDKL 的对照方法。出处：Wilhelmy 1994 #1。
5. **CMS** (Continuum Multiple Scattering) — 以 Muffin-tin 势近似的连续态多重散射方法，此处作对照。出处：Wilhelmy 1994 #1。
6. **Feshbach 投影** (P/Q projection) — 用正交投影把 Hilbert 空间分为 $P$（束缚/共振）与 $Q$（连续）子空间，导出有效哈密顿量 $H_{\text{eff}}=PHP+PHQ(E-QHQ)^{-1}QHP$。出处：Domcke 1983 #2。
7. **共振能量与宽度** (resonance energy & width) — 共振态的复能量极点 $E_{\text{res}}-i\Gamma/2$，实部为能量、虚部给出宽度 $\Gamma$，从 $H_{\text{eff}}$ 的复极点提取。出处：Domcke 1983 #2。
8. **$i\varepsilon$ 极限** (outgoing-wave boundary prescription) — 在 Green 函数 $G(E)=(E-H_{\text{eff}}+i\varepsilon)^{-1}$ 中以 $+i\varepsilon$ 选取出射波边界条件的数学处理。出处：Domcke 1983 #2。
9. **截断球面波** (Truncated Spherical Wave, TSW) — 在有限半径 $R_c$ 处归零的球 Bessel 函数 $j_l(k_{ln}r/R_c)$，作 NAO 的原始函数。出处：Huang 2026 #3。
10. **系统可改进性** (systematic improvability) — 通过单调增大 $R_c$ 即可系统逼近完备基的性质，TSW 的核心优势。出处：Huang 2026 #3。
11. **迹极小化** (Trace Minimization) — 优化 TSW 参数使动能算符迹最小化的变分优化算法。出处：Huang 2026 #3。
12. **NAO** (Numerical Atomic Orbital) — 数值原子轨道；TSW 作为其原始函数，经系数 $c_{ln}$ 展开为原子轨道。出处：Huang 2026 #3。
13. **真空层镜像相互作用** (vacuum-image interaction) — 平面波周期边界下真空层引入的虚假相互作用，TSW 截断正是为消除它。出处：Huang 2026 #3。
14. **ABACUS** — 开源第一性原理软件包，TSW-NAO 方法的实现平台。出处：Huang 2026 #3。
15. **ASW** (Augmented Spherical Wave) — 缀加球面波方法：原子球内数值解 + 球 Hankel 包Envelope缀加。出处：Eyert #4。
16. **MTO** (Muffin-Tin Orbital) — 缀加原子轨道，原子球内数值解与球 Hankel 包络拼接而成，ASW 的构造单元。出处：Eyert #4。
17. **KKR** (Korringa-Kohn-Rostoker) — 基于多重散射 Green 函数的能带方法，ASW 的前身。出处：Eyert #4、Gonis 1999 #7。
18. **全势** (Full-Potential) — 不作 Muffin-tin 球近似、保留势全部空间结构的处理，ASW 的现代化方向。出处：Eyert #4。
19. **LMTO / LAPW** (Linear MTO / Linear APW) — 将能量依赖的缀加轨道线性化为能量无关基组的方法，构成 ASW→LMTO→LAPW→LCAO 演进链。出处：Eyert #4。
20. **矢量球面谐波** ($M_{lm},N_{lm},L_{lm}$) — 矢量 Helmholtz 方程的三类球面波解模式，矢量加法定理的对象。出处：Felderhof 1987 #5。
21. **加法定理** (addition theorem) — 球面波在坐标平移下的变换关系，多中心球面波展开的核心数学工具。出处：Felderhof 1987 #5。
22. **Gaunt 系数 / Clebsch-Gordan 系数** — 三个球谐积分 / 角动量耦合系数，加法定理位移系数的展开基。出处：Felderhof 1987 #5。
23. **T-matrix** (transition matrix) — 散射跃迁算符在球面波基下的矩阵表示，T-matrix 方法的基本对象。出处：Felderhof 1987 #5、Fruhnert 2024 #10。
24. **螺旋度本征态** (helicity eigenstate) — 自旋沿动量方向投影的本征态，自旋球面波展开的基。出处：Weinberg 1994 #6。
25. **自旋-轨道耦合** (spin-orbit coupling) — 自旋与轨道角动量的相对论性耦合，自旋球面波自然纳入。出处：Weinberg 1994 #6。
26. **Bloch 动量** (Bloch momentum) — 周期体系中标志平移对称性的量子数，准周期 Green 函数求值在任意 Bloch 动量下进行。出处：Moroz 2006 #8。
27. **Schlömilch 级数** — 球面波格子求和的指数收敛表示。出处：Moroz 2006 #8。
28. **格子求和** (lattice sums) — 周期 Green 函数所需的球面波级数求和，其极点处理与本项目 $1/(p^2-k^2-i\varepsilon)$ 同构。出处：Moroz 2006 #8。
29. **准周期 Green 函数** (quasi-periodic Green's function) — 部分维度具周期性的 Helmholtz Green 函数的 Schwinger 级数表示。出处：Moroz 2006 #8。
30. **MLFMA** (Multilevel Fast Multipole Algorithm) — 多级快速多极子算法，电磁/声学散射中加速球面波展开的核心方法。出处：Egel 2024 #9。
31. **平移算子对角化** (diagonal translation operator) — 把球面波平移算子在远场对角化以加速多极传递的技巧。出处：Egel 2024 #9。
32. **静态模式低秩表示** (low-rank static modes) — 低频/静态球面波模式的低秩压缩，MLFMA 加速策略之一。出处：Egel 2024 #9。
33. **Daphona** — 提议中的 T-matrix 标准化数据开放平台。出处：Fruhnert 2024 #10。
