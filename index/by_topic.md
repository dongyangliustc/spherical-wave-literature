# 按主题分类索引

## 1. GTO 连续态方法（本项目方法学母体）

最核心主题。Cacelli-Moccia-Rizzo 团队在 1990s 发展了用 GTO 基组计算连续态与光电离截面的 L2 方法。

| 论文 | 方法贡献 | 对应本项目代码 |
|------|---------|--------------|
| Cacelli et al. (1993) [H2 截面] | GTO 基组+L2 技术算光电离截面 | CS_calculator.py、momentum_gto.py |
| Cacelli et al. (1998) [N2 微分截面] | 扩展到微分截面与不对称参数 | angular_reduction.py |
| Cacelli et al. (2000) [C2H2 截面] | 非对称分子处理 | frame_transform.py |
| Cacelli et al. (1990) [MOTECC] | L2 方法综述 | 理论框架总纲 |

## 2. 球面波基组与连续态展开

| 论文 | 方法贡献 | 对应本项目代码 |
|------|---------|--------------|
| Wilhelmy et al. (1994) [Lobatto 技术] | Lobatto 形状函数 + GTO 混合基组 | continuum_wave.py |
| Moroz (2006) [准周期格林函数] | 球面波格林函数展开 | SPHERICAL_WAVE_SPEC.md |
| Domcke (1983) [投影算符散射] | 投影算符 + 连续态 | 格林函数理论 |

## 3. B-spline 连续态（平行对照路线）

| 论文 | 方法对比 |
|------|---------|
| Tiresia 代码 (2023) | B-spline + 球谐展开，与 GTO 路线形成方法对比 |
| McCurdy & Martín (2004) | 复缩放 + B-spline 实现 |
| Stener et al. (2005) | TD-DFT + B-spline 光电离 |
| Brosolo & Decleva (1992) | B-spline 连续态开端 |
| **Moitra et al. (2021) [JCTC]** | **EOM-CC Dyson + B-spline TDDFT，捕获关联效应** |
| **Ruberti (2019) [JCTC]** | **RCS-ADC B-spline 方法，受限关联空间** |

## 4. 复积分与数值方法

| 论文 | 方法贡献 |
|------|---------|
| McCurdy & Martín (2004) | 外复缩放 (ECS) |
| Majety et al. (2015) | 混合耦合通道+tSURFF |

## 5. 光电离物理与综述

| 论文 | 方向 |
|------|------|
| **Gozem et al. (2015) [JPCL]** | **光电离中光电子波函数：平面波 vs Coulomb 波** |
| **Calegari et al. (2016) [JPB]** | **阿秒脉冲诱导的电荷迁移** |
| **Ruckenbauer et al. (2016) [SciRep]** | **时间分辨光电子光谱中的去活化通道** |
| Nisoli et al. (2017) [ChemRev] | 阿秒电子动力学综述 |
