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
