# B-spline 连续态方法 — 读书笔记

> 目录: `papers/B_spline_continuum/` | 共 3 篇
> 主题: 用 B-spline 基组展开电子连续态，计算光电离可观测量
> 核心学派: Decleva (Trieste) — Tiresia 代码路线

---

## 1. Stener, Fronzoni, Decleva — 2005 — TD-DFT B-spline 光电离

**文件**: `Stener_2005_TDDFT_photoionization_JCP.pdf`
**DOI**: `10.1063/1.1937367`
**期刊**: J. Chem. Phys. 122, 234301
**优先级**: ⭐⭐⭐⭐

### 原理推导
- 使用 **时间相关密度泛函理论（TD-DFT）** 描述分子光电离
- 连续态通过 **多中心 B-spline 基组** 展开
- 光吸收截面通过偶极响应函数的虚部获得，等价于 Kramers-Kronig 关系
- 与 Tiresia 代码的算法一致，但侧重于 TD-DFT 而非静态 DFT

### 方法创新
- **非迭代算法**：避免传统的迭代求解响应方程
- 平面波扰动算符的数值展开
- CS₂ 和 C₆H₆ 的验证计算，展示对中等大小分子的适用性

### 程序拓展值得借鉴
- TD-DFT 线性响应方程的矩阵求解方法
- Stieltjes 成像技术的数值实现
- 多中心 B-spline 的积分策略
- 本项目中 DFT 势的连续态计算可参考此方案

---

## 2. Decleva, Stener, Toffoli — 2022 — Tiresia 综述

**文件**: `Decleva_2022_Tiresia_continuum_Molecules.pdf`
**DOI**: `10.3390/molecules27062026`
**期刊**: Molecules 27, 2026
**优先级**: ⭐⭐⭐⭐

### 原理推导
- 全面综述 **多中心 B-spline + 球谐** 基组的理论框架
- LCAO（线性组合原子轨道）形式的多中心展开
- R-matrix 方法与 B-spline 的结合

### 方法创新
- 多中心 B-spline 基组的系统完备性证明
- 全电子势与赝势的统一处理
- 静态 DFT, TD-DFT, Dyson-DFT, Dyson-TDDFT 四种哈密顿量层次的连续态计算
- 波包传播在连续态基上的实现

### 程序拓展值得借鉴
- **四层方法学层次** 可作为本项目的方法论参考
- 静态 DFT → TD-DFT → Dyson-DFT → Dyson-TDDFT 递进
- 多中心基组的矩阵元计算策略
- 波包传播方法（可用于本项目的时域拓展）

---

## 3. Tenorio, Ponzi, Coriani, Decleva — 2022 — Dyson 轨道+B-spline

**文件**: `Tenorio_2022_Dyson_photoionization_Molecules.pdf`
**DOI**: `10.3390/molecules27041203`
**期刊**: Molecules 27, 1203
**优先级**: ⭐⭐⭐⭐

### 原理推导
- 使用 **MS-CASPT2 Dyson 轨道** 作为初态，耦合 B-spline 连续态
- Dyson 轨道 $|\Phi^{Dyson}\rangle = \sqrt{N} \langle \Psi_f^{N-1} | \Psi_i^N \rangle$
- 连续态通过 DFT/TD-DFT 有效势描述
- 适用于处理**卫星峰（satellite bands）**和强关联体系

### 方法创新
- Dyson 轨道与 B-spline 连续态的耦合方案
- 在 OpenMolcas 中的实现与对称性处理
- 首次对 CS 和 SiS 分子进行高精度卫星峰计算

### 程序拓展值得借鉴
- Dyson 轨道计算流程（可融入本项目的初态处理）
- 多参考方法与连续态的接口（本项目的 Potrf 类似）
- 卫星峰的处理策略

---

## 本目录核心贡献总结

B-spline 路线是本项目（GTO 路线）的**平行对照方法学**。两条路线的对比：

| 维度 | B-spline 路线（本目录） | GTO 路线（本项目） |
|------|----------------------|------------------|
| 连续态基组 | B-spline + 球谐 | 球面波格林函数 + GTO |
| 积分方法 | 数值积分 | 解析傅里叶变换 |
| 束缚态 | 独立 GTO 基 | 相同 GTO 基 |
| 收敛性 | 系统可控（B-spline 阶数） | 系统可控（GTO 指数 + 球面波截断） |
| 软件实现 | Tiresia（Fortran/MPI） | Python 原型 |
| 物理范围 | 静态 DFT → TD-DFT → Dyson | 长度/速度规范 + IBP 加速 |

Tiresia 代码（Toffoli 2023）的架构设计和输出接口是本项目程序拓展的直接参考。
