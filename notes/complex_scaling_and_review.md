# 复缩放与综述类 — 读书笔记

> 目录: `papers/complex_scaling/` (1 篇) + `papers/general_review/` (5 篇)
> 主题: 复平面积分方法（ECS）与光电离综述

---

## complex_scaling — 复缩放方法

## 1. McCurdy, Martín — 2004 — ECS + B-spline

**文件**: `McCurdy_Martin_2004_ECS_BSpline_JPB.pdf`
**DOI**: `10.1088/0953-4075/37/4/017`
**期刊**: J. Phys. B: At. Mol. Opt. Phys. 37, 917
**优先级**: ⭐⭐⭐⭐

### 原理推导
- **外复缩放（Exterior Complex Scaling, ECS）**：在有限区域外将坐标旋转到复平面
- $r \to \begin{cases} r & r < R_0 \\ R_0 + (r - R_0)e^{i\theta} & r \geq R_0 \end{cases}$
- 缩放后连续态波函数 $e^{ikr}$ → $e^{ikr\cos\theta}e^{-kr\sin\theta}$ 呈指数衰减
- 避免了直接处理振荡边界条件

### 方法创新
- ECS 与 B-spline 的首次结合
- 通过 Poisson 方程计算 ECS 下的双电子积分
- 适用于多个离化问题（双电离、解离等）
- 无需解析连续态波函数的知识

### 程序拓展值得借鉴
- **本项目 complex_contour.py 的复平面积分应与 ECS 对比**
- 本项目使用复平面围道避开极点，ECS 通过坐标旋转衰减尾波
- B-spline + ECS 的积分策略
- 双电子问题的处理方法（本项目暂未涉及）

### 与项目关联
ECS 与本项目的复平面围道积分是两种不同的"复域"策略：
- 本项目：动量空间围道 $\int_C f(p) dp$ 避开 $p=k$ 极点
- ECS：实空间坐标旋转 $r \to re^{i\theta}$ 使连续态衰减
- 两者在数学上是等价的（Cauchy 定理），但数值实现差异大
- ECS 的优势：无需知道连续态解析形式；劣势：需要复矩阵对角化

---

## general_review — 综述与扩展阅读

## 2. Nisoli, Decleva, Calegari et al. — 2017 — 阿秒分子动力学

**文件**: `Nisoli_2017_attosecond_electron_dynamics_ChemRev.pdf`
**DOI**: `10.1021/acs.chemrev.6b00453`
**期刊**: Chem. Rev. 117, 10760
**优先级**: ⭐⭐⭐

### 核心内容
- 阿秒科学在分子系统中的应用综述
- 飞秒激光 → 阿秒脉冲产生的物理机制（HHG）
- 泵浦-探测实验中的电子波包动力学
- 分子光致电离的时域描述

### 与本项目关联
- 光致电离截面（本项目）是阿秒泵浦-探测实验的输入参数
- 分子框架光电离中的干涉效应
- 电子波包的动力学描述可作为项目时域拓展的参考

---

## 3. Hróðmarsson & van Dishoeck — 2023 — VUV 数据库综述

**文件**: `Hróðmarsson_2023_VUV_database_AA.pdf`
**DOI**: `10.1051/0004-6361/202346645`
**期刊**: Astron. Astrophys. 675, A153
**优先级**: ⭐⭐⭐

### 核心内容
- Leiden VUV 光致离解/电离截面数据库更新
- 14 种新分子的截面数据
- 星际辐射场下的光化学反应率
- 屏蔽效率的计算框架（尘埃、H₂、CO 等）

### 与本项目关联
- 提供了光电离截面的基准数据（验证数据集）
- 天体化学模型中的截面使用场景（本项目出口）
- 屏蔽效率的计算方法

---

## 4. Vanroose et al. — 2006 — H₂ 双电离

**文件**: `Vanroose_2006_H2_double_photoionization_PRA.pdf`
**DOI**: `10.1103/physreva.74.052702`
**期刊**: Phys. Rev. A 74, 052702
**优先级**: ⭐⭐⭐

### 核心内容
- H₂ 分子的双光子双电离全微分截面（TDCS）
- ECS + B-spline 方法求解相关连续态
- 取向平均的 H₂ 分子的双电离

### 与本项目关联
- 双电离超出了本项目当前范围，但展示了 ECS 方法对关联连续态的处理能力
- **可参考**：取向平均截面的计算（frame_transform.py）

---

## 5. Ruiz-Serrano et al. — 2012 — 线性标度 HF (ONETEP)

**文件**: `RuizSerrano_2012_linear_scaling_HF_ONETEP.pdf`
**期刊**: J. Chem. Phys. 136, 234107 / Southampton 技术报告
**优先级**: ⭐⭐⭐

### 核心内容
- ONETEP 中线性标度 HF 交换计算
- 非正交广义 Wannier 函数（NGWF）表述
- 平面波精度下的线性标度杂化泛函

### 与本项目关联
- 展示了大规模量子化学计算中的技术取舍
- 辅助基组 + 距离截断的线性标度策略

---

## 6. Qian et al. — 2002 — NAO Hubbard 模型

**文件**: `Qian_2002_NAO_Hubbard_arXiv.pdf`
**DOI**: arXiv:cond-mat/0205368
**优先级**: ⭐⭐

### 核心内容
- 数值原子轨道（NAO）在强关联体系中的应用
- Hubbard 模型的紧束缚参数化
- 第一性原理→模型哈密顿量的降维策略

### 与本项目关联
- NAO 的构造方法（联系 Huang 2026 TSW）
- 项目关联度较低，作为补充参考

---

## 本目录核心贡献总结

| 论文 | 核心方法 | 对本项目的贡献 |
|------|---------|-------------|
| McCurdy 2004 | ECS + B-spline | 复平面积分的对照路线 |
| Nisoli 2017 | 阿秒分子综述 | 项目应用场景 |
| Hróðmarsson 2023 | VUV 截面数据库 | 验证数据集 |
| Vanroose 2006 | ECS 双电离 | 方法展示与取向平均 |
| Ruiz-Serrano 2012 | 线性标度 ONETEP | 程序架构参考 |
