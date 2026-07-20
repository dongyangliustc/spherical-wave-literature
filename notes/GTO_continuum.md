# GTO 连续态方法 — 读书笔记

> 目录: `papers/GTO_continuum/` | 共 7 篇
> 主题: 用 Gaussian Type Orbital (GTO) 基组计算分子连续态与光电离截面
> 核心团队: Cacelli, Moccia, Rizzo (1990s) — 本项目方法学母体

---

## 1. Cacelli, Moccia, Rizzo — 1993 — H₂ 截面

**文件**: `Cacelli_1993_H2_photoionization_JCP.pdf`
**DOI**: `10.1063/1.464482`
**期刊**: J. Chem. Phys. 98, 8742
**优先级**: ⭐⭐⭐⭐⭐

### 原理推导
- 将分子光致电离问题转化为 L² 基组中的连续态求解
- 束缚态用标准 GTO 基组描述（如 Dunning 基组）
- 连续态用 **L² 基组加 Stieltjes-Tchebychev (ST) 成像技术** 提取光电离截面
- 总截面公式: $\sigma = \frac{4\pi^2\alpha\omega k}{3} \sum_l |\langle \psi_f | \mathbf{r} | \psi_i \rangle|^2$
- 长度规范与速度规范均实现，验证了规范不变性

### 方法创新
- 使用 **GTO 作为连续态展开基**，而非传统的 B-spline 或数值打靶法
- L²-ST 方法克服了连续态计算中的边界条件难题——不直接求解连续态波函数，而是通过离散谱的矩重构连续截面
- 与 Kohn 变分法结合，避免了长程边界条件的人为截断

### 程序拓展值得借鉴
- 基组选择策略：收缩 GTO 用于束缚态，未收缩 GTO 用于连续态
- 矩阵元的计算：所有积分都在实空间 GTO 基上解析计算
- Stieltjes 矩的重构算法
- 长度/速度规范的双重实现可作为本项目规范验证的参考

### 与项目关联
本项目（动量空间 GTO + 球面波基组）可视为该工作的"动量空间版本"：
- 相同目标：GTO 基组计算光电离截面
- 不同路径：本项目将积分转到动量空间，用球面波解析处理连续态
- 规范一致性验证策略可沿用

---

## 2. Cacelli, Moccia, Rizzo — 1998 — N₂ 微分截面

**文件**: `Cacelli_1998_N2_differential_PRA.pdf`
**DOI**: `10.1103/physreva.57.1895`
**期刊**: Phys. Rev. A 57, 1895
**优先级**: ⭐⭐⭐⭐⭐

### 原理推导
- 从总截面推广到 **微分截面（Differential Cross Section, DCS）** 和 **不对称参数 β**
- 角分布 $I(\theta) = \frac{\sigma}{4\pi}[1 + \beta P_2(\cos\theta)]$
- 偶极矩阵元的分波分解：$\langle \psi_f | \mathbf{r} | \psi_i \rangle \rightarrow (l,m)$ 分波
- 长度/速度规范下 β 参数的一致性验证

### 方法创新
- 将 L²-GTO 方法从总截面推广到角分辨截面
- 各向异性分子（N₂）的多通道处理
- 提出用 GTO 基组同时描述形状共振和连续态

### 程序拓展值得借鉴
- β 参数的数值提取方法
- 分波截面 $\sigma_l$ 的分解方法
- 多参考初态的处理方式（等价于本项目的多个束缚 GTO）
- 本项目应在 CS_calculator.py 的 β 参数计算中参考

---

## 3. Cacelli, Moccia, Rizzo — 2000 — C₂H₂ 截面

**文件**: `Cacelli_2000_C2H2_differential_CP.pdf`
**DOI**: `10.1016/s0301-0104(99)00325-0`
**期刊**: Chem. Phys. 254, 113
**优先级**: ⭐⭐⭐⭐⭐

### 原理推导
- 将 GTO-L² 方法推广到更复杂的线性多原子分子（乙炔）
- 引入基于密度泛函理论（DFT）的有效局域势
- 与前两篇的 Hartree-Fock 势对比，验证 DFT 势在连续态计算中的有效性

### 方法创新
- DFT 势与 GTO 连续态基组的首次结合
- 用 LB94 交换相关势改善渐近行为
- 多个价壳层电离通道的同时处理

### 程序拓展值得借鉴
- DFT 势的数值积分方法（在 GTO 基上的矩阵元计算）
- 多通道耦合的处理流程
- 对称性约化：利用分子点群简化积分计算

---

## 4. Carmona-Novillo, Moccia, Spizzo — 1996 — LiH 截面

**文件**: `CarmonaNovillo_1996_LiH_photoionization_CP.pdf`
**DOI**: `10.1016/0301-0104(96)00128-0`
**期刊**: Chem. Phys. 210, 457
**优先级**: ⭐⭐⭐⭐⭐

### 原理推导
- 异核双原子分子（LiH）的光电离
- **混合 GTO/STOCOS 基组**：内层用 GTO，外层用 STOCOS（Spherical Gaussian-Type Orbitals Centered on the Center of Mass）
- 首次处理无中心对称分子的光电离

### 方法创新
- STOCOS 基组：以质心为中心的球面 GTO，改善角动量收敛
- 混合基组策略：将 GTO 的灵活性与 STOCOS 的角收敛性结合
- 异核分子的偶极矩阵元计算

### 程序拓展值得借鉴
- 混合基组策略是本项目的直接参考——本项目在用 GTO + 球面波混合
- 质心坐标系的处理（对应 frame_transform.py）
- 异核分子的对称性降级处理方法

---

## 5. Moccia, Montuoro — 2003 — Li₂ 微分截面

**文件**: `Moccia_Montuoro_2003_Li2_differential_CPL.pdf`
**DOI**: `10.1016/s0009-2614(02)01765-7`
**期刊**: Chem. Phys. Lett. 364, 429
**优先级**: ⭐⭐⭐⭐

### 原理推导
- Li₂ 分子的微分光电离截面
- **混合 L² 基组：STO（Slater Type Orbital）+ B-spline**
- STO 描述束缚态，B-spline 描述连续态

### 方法创新
- STO+B-spline 混合基，对比纯 GTO 方法的优劣
- B-spline 在描述连续态径向波函数方面的优势
- 含电子关联效应的处理（配置相互作用波函数）

### 程序拓展值得借鉴
- 混合基组策略的对比分析——本项目选择 GTO+球面波，与此处 STO+B-spline 形成对照
- B-spline 径向基组的布点策略
- 电子关联的处理方法

---

## 6. Toffoli, Coriani, Stener, Decleva — 2023 — Tiresia 代码

**文件**: `Toffoli_2023_Tiresia_CPC.pdf`
**DOI**: `10.1016/j.cpc.2023.109038`
**期刊**: Comput. Phys. Commun. 296, 109038
**优先级**: ⭐⭐⭐⭐

### 原理推导
- Tiresia：基于 B-spline + 球谐函数的分子连续态计算软件包
- DFT/TD-DFT 哈密顿量 + B-spline 基组
- Galerkin 方法直接求解非齐次 Schrödinger 方程

### 方法创新
- 多中心 B-spline 基组：每个原子中心放一组 B-spline×球谐
- Dyson 轨道 + B-spline 连续态（实现多参考波函数的连续态计算）
- TD-DFT 框架中处理光吸收和光电离
- 大规模并行 MPI 实现

### 程序拓展值得借鉴
- 多中心基组的实现架构（本项目也是多中心，但用 GTO）
- Galerkin 方法求解连续态（区别于本项目的解析 Green 函数）
- MPI 并行策略
- 输出交界面：截面、β 参数、延迟时间的计算流程
- **本项目的重要对照代码**：对比 B-spline 路线 vs GTO 路线的优劣

---

## 7. Brosolo, Decleva — 1992 — H₂⁺ 光电离

**文件**: `Brosolo_Decleva_1992_H2plus_BSpline_CP.pdf`
**DOI**: `10.1016/0301-0104(92)80069-8`
**期刊**: Chem. Phys. 159, 185
**优先级**: ⭐⭐⭐⭐

### 原理推导
- H₂⁺ 在 B-spline 基上的连续态变分计算
- 基于 **Kohn 变分原理** 的连续态求解
- B-spline 基组直接展开连续态径向波函数

### 方法创新
- B-spline 的灵活布点：在核附近密集、在外部稀疏
- 变分法保证了连续态能量的正确 Kato 归一化
- 同时处理束缚-自由和自由-自由跃迁矩阵元

### 程序拓展值得借鉴
- Kohn 变分方法在求解连续态中的应用（可作为本项目解析 Green 函数方法的对照）
- B-spline 基组的渐近边界条件处理
- 精确验证的基准结果（H₂⁺ 是可解析求解的）

---

## 本目录核心贡献总结

| 编号 | 核心贡献 | 对应本项目 |
|------|---------|----------|
| 1 | GTO 连续态 + H₂ 截面基准 | 方法学总纲 |
| 2 | 微分截面与 β 参数 | CS_calculator.py β 参数 |
| 3 | DFT 势 + 多原子拓展 | 势能模型选择 |
| 4 | 混合 GTO/STOCOS 基组 | 本项目 GTO+球面波混合 |
| 5 | STO+B-spline 对比路线 | angular_reduction.py 参考 |
| 6 | Tiresia (B-spline) 代码架构 | 程序架构对照 |
| 7 | Kohn 变分 + B-spline 连续态 | continuum_wave.py 参考 |

---

## 术语表

> 按本笔记中出现的顺序整理。出处为本目录所列对应论文（"#编号"指上文小节序号）。

1. **$L^2$ 基组** (square-integrable basis) — 由平方可积函数（GTO/STO）构成的离散基组，对角化后给出离散赝谱而非真实连续态。出处：Cacelli 1993 #1。
2. **Stieltjes-Tchebychev (ST) 成像** — 从 $L^2$ 赝谱的振子强度矩重构连续截面的算法，GTO 连续态方法的核心，避免直接处理边界条件。出处：Cacelli 1993 #1。
3. **Dunning 基组** (cc-pVnZ) — 相关一致高斯基组，束缚态标准选择；连续态则用未收缩 GTO。出处：Cacelli 1993 #1。
4. **收缩 / 未收缩 GTO** (contracted / uncontracted GTO) — 多个原函数合成一个收缩函数（束缚态用）vs 保留独立原函数（连续态需灵活性）。出处：Cacelli 1993 #1。
5. **长度规范 / 速度规范** (length / velocity gauge) — 偶极算符取 $\mathbf{r}$ 或 $\mathbf{p}/\omega$；两者截面一致即规范不变性，正确性检验手段。出处：Cacelli 1993 #1。
6. **微分截面** (Differential Cross Section, DCS) — 截面对出射立体角的导数，描述角分布。出处：Cacelli 1998 #2。
7. **不对称参数 $\beta$** (asymmetry parameter) — 角分布 $I(\theta)=\frac{\sigma}{4\pi}[1+\beta P_2(\cos\theta)]$ 中的各向异性参数。出处：Cacelli 1998 #2。
8. **分波分解** (partial-wave decomposition) — 把偶极矩阵元按 $(l,m)$ 角动量分波展开，提取各分波截面 $\sigma_l$。出处：Cacelli 1998 #2。
9. **形状共振** (shape resonance) — 连续态势垒临时俘获电子造成的截面峰。出处：Cacelli 1998 #2。
10. **DFT 有效局域势** — 以密度泛函理论提供的等效局域势替代 HF 势描述连续态。出处：Cacelli 2000 #3。
11. **LB94** — 渐近行为修正为 $-1/r$ 的交换相关泛函，对连续态长程行为至关重要。出处：Cacelli 2000 #3。
12. **多通道** (multi-channel) — 同时处理多个价壳层电离通道的耦合。出处：Cacelli 2000 #3。
13. **对称性约化** (symmetry reduction) — 利用分子点群简化积分计算。出处：Cacelli 2000 #3。
14. **STOCOS** (Spherical GTO Centered on Center of Mass) — 以质心为中心、径向 $r^l e^{-\zeta r}\cos(k_n r)$ 的 $L^2$ 连续态基，改善角动量收敛。出处：Carmona-Novillo 1996 #4。
15. **质心坐标系** (center-of-mass frame) — 异核分子连续态展开所选参考系，对应 `frame_transform.py`。出处：Carmona-Novillo 1996 #4。
16. **STO** (Slater Type Orbital) — 径向 $r^n e^{-\zeta r}$ 的 Slater 型轨道，渐近行为优于 GTO。出处：Moccia & Montuoro 2003 #5。
17. **配置相互作用** (Configuration Interaction, CI) — 多行列式线性组合描述电子关联。出处：Moccia & Montuoro 2003 #5。
18. **Tiresia** — Trieste 学派的 B-spline+球谐分子连续态计算软件包。出处：Toffoli 2023 #6。
19. **Galerkin 方法** — 加权残差取试探函数作权函数的投影法，此处用于直接求解非齐次 Schrödinger 方程。出处：Toffoli 2023 #6。
20. **Dyson 轨道** (Dyson orbital) — $|\Phi^{Dyson}\rangle=\sqrt{N}\langle\Psi_f^{N-1}|\Psi_i^N\rangle$，连接 N 与 N−1 电子态的单电子轨道，作光电离初态。出处：Toffoli 2023 #6。
21. **TD-DFT** (Time-Dependent DFT) — 时间相关密度泛函线性响应理论，处理光吸收/光电离。出处：Toffoli 2023 #6。
22. **MPI** (Message Passing Interface) — 分布式内存并行标准，Tiresia 大规模实现的并行方案。出处：Toffoli 2023 #6。
23. **Kohn 变分** — 对散射 K 矩阵的变分方法，B-spline 连续态变分求解的基础。出处：Brosolo & Decleva 1992 #7。
24. **Kato 归一化** — 连续态在原点附近的归一化条件（Kato cusp），变分法保证其正确性。出处：Brosolo & Decleva 1992 #7。
25. **束缚-自由 / 自由-自由跃迁** (bound-free / free-free transition) — 束缚↔连续 与 连续↔连续 的矩阵元，B-spline 方法同时处理。出处：Brosolo & Decleva 1992 #7。
