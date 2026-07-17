# 球面波基组与光电离截面计算 —— 文献索引

> 建立日期：2026-07-15
> 对应项目：动量空间球面波基组光致电离截面计算（GTO 傅里叶变换 + IBP 处理偶极规范）

---

## 目录结构

```
spherical_wave_literature/
├── index/
│   └── README.md           ← 本文件：完整索引
│   └── by_topic.md         ← 按主题分类的索引
│   └── by_relevance.md     ← 按相关度分级的阅读清单
├── papers/                 ← PDF 文件按主题子目录存放
│   ├── GTO_continuum/      ← GTO 连续态方法（Cacelli-Moccia-Rizzo 系列）
│   ├── B_spline_continuum/ ← B-spline 连续态（Decleva 学派 / Tiresia）
│   ├── spherical_wave/     ← 球面波展开与格林函数
│   ├── complex_scaling/    ← 复缩放与围道积分方法
│   └── general_review/     ← 综述文章
└── notes/                  ← 阅读笔记
```

---

## 核心论文学术索引

### 第 I 类：最直接相关（GTO 连续态方法）★★★★★

| # | 标题 | 作者 | 年份 | 期刊 | DOI |
|---|------|------|------|------|-----|
| 1 | Gaussian type orbital basis sets for the calculation of continuum properties in molecules: The photoionization cross section of H2 | Cacelli, Moccia, Rizzo | 1993 | J. Chem. Phys. | [10.1063/1.464482](https://doi.org/10.1063/1.464482) |
| 2 | Gaussian-type-orbital basis sets for the calculation of continuum properties in molecules: The differential photoionization cross section of molecular nitrogen | Cacelli, Moccia, Rizzo | 1998 | Phys. Rev. A | [10.1103/physreva.57.1895](https://doi.org/10.1103/physreva.57.1895) |
| 3 | Gaussian Type Orbitals basis sets for the calculation of continuum properties in molecules: the differential photoionization cross section of acetylene | Cacelli, Moccia, Rizzo | 2000 | Chem. Phys. | [10.1016/s0301-0104(99)00325-0](https://doi.org/10.1016/s0301-0104(99)00325-0) |
| 4 | Continuum by L2 Methods: Molecular Photoionization Cross Section | Cacelli, Carravetta, Rizzo, Moccia | 1990 | MOTECC-90 | [10.1007/978-94-009-2219-8_12](https://doi.org/10.1007/978-94-009-2219-8_12) |
| 5 | Photoionization cross section and asymmetry parameter of LiH: a mixed GTO/STOCOS L2 basis set calculation | Carmona-Novillo, Moccia, Spizzo | 1996 | Chem. Phys. | [10.1016/0301-0104(96)00128-0](https://doi.org/10.1016/0301-0104(96)00128-0) |
| 6 | Mixed L2 basis set: STOs plus B-Splines. Calculation of the differential photoionization cross-section of Li2 | Moccia, Montuoro | 2003 | Chem. Phys. Lett. | [10.1016/s0009-2614(02)01765-7](https://doi.org/10.1016/s0009-2614(02)01765-7) |

### 第 II 类：B-spline 连续态方法（方法平行线）★★★★

| # | 标题 | 作者 | 年份 | 期刊 | DOI |
|---|------|------|------|------|-----|
| 7 | Tiresia: A code for molecular electronic continuum states and photoionization | Toffoli, Coriani, Stener, Decleva | 2023 | Comput. Phys. Commun. | [10.1016/j.cpc.2023.109038](https://doi.org/10.1016/j.cpc.2023.109038) |
| 8 | Continuum Electronic States: The Tiresia Code | Decleva, Stener, Toffoli | 2022 | Molecules | [10.3390/molecules27062026](https://doi.org/10.3390/molecules27062026) |
| 9 | Photoionization Observables from Multi-Reference Dyson Orbitals Coupled to B-Spline DFT and TD-DFT Continuum | Tenorio et al. | 2022 | Molecules | [10.3390/molecules27041203](https://doi.org/10.3390/molecules27041203) |
| 10 | Implementation of exterior complex scaling in B-splines to solve atomic and molecular collision problems | McCurdy, Martín | 2004 | J. Phys. B | [10.1088/0953-4075/37/4/017](https://doi.org/10.1088/0953-4075/37/4/017) |
| 11 | Time-dependent density-functional theory for molecular photoionization with noniterative algorithm and multicenter B-spline basis set | Stener, Fronzoni, Decleva | 2005 | J. Chem. Phys. | [10.1063/1.1937367](https://doi.org/10.1063/1.1937367) |
| 12 | Variational approach to continuum orbitals in a spline basis: An application to H2+ photoionization | Brosolo, Decleva | 1992 | Chem. Phys. | [10.1016/0301-0104(92)80069-8](https://doi.org/10.1016/0301-0104(92)80069-8) |

### 第 III 类：球面波展开与散射理论 ★★★★

| # | 标题 | 作者 | 年份 | 期刊 | DOI |
|---|------|------|------|------|-----|
| 13 | Molecular photoionization cross sections by the Lobatto technique. I. Valence photoionization | Wilhelmy, Ackermann, Görling, Rösch | 1994 | J. Chem. Phys. | [10.1063/1.466475](https://doi.org/10.1063/1.466475) |
| 14 | Quasi-periodic Green's functions of the Helmholtz and Laplace equations | Moroz | 2006 | J. Phys. A | [10.1088/0305-4470/39/36/009](https://doi.org/10.1088/0305-4470/39/36/009) |
| 15 | Multiple scattering in solids | Gonis, Butler | 1999 | Springer | [10.1007/978-1-4612-1290-4](https://doi.org/10.1007/978-1-4612-1290-4) |
| 16 | Projection-operator approach to potential scattering | Domcke | 1983 | Phys. Rev. A | [10.1103/PHYSREVA.28.2777](https://doi.org/10.1103/PHYSREVA.28.2777) |

### 第 IV 类：综述与扩展阅读 ★★★

| # | 标题 | 作者 | 年份 | 期刊 | DOI |
|---|------|------|------|------|-----|
| 17 | Attosecond Electron Dynamics in Molecules | Nisoli, Decleva, Calegari et al. | 2017 | Chem. Rev. | [10.1021/acs.chemrev.6b00453](https://doi.org/10.1021/acs.chemrev.6b00453) |
| 18 | Photoionization of few electron systems: a hybrid coupled channels approach | Majety, Zielinski, Scrinzi | 2015 | New J. Phys. | [10.1088/1367-2630/17/6/063002](https://doi.org/10.1088/1367-2630/17/6/063002) |
| 19 | Photodissociation and photoionization of molecules of astronomical interest | Hróðmarsson, van Dishoeck | 2023 | A&A | [10.1051/0004-6361/202346645](https://doi.org/10.1051/0004-6361/202346645) |
| 20 | Double photoionization of aligned molecular hydrogen | Vanroose et al. | 2006 | Phys. Rev. A | [10.1103/physreva.74.052702](https://doi.org/10.1103/physreva.74.052702) |

---

## 按阅读优先级排序

### 第一梯队（必须精读）
1. Cacelli, Moccia, Rizzo (1993) — GTO 连续态计算 H2 截面 ← **方法学母体**
2. Cacelli, Moccia, Rizzo (1998) — GTO 连续态计算 N2 微分截面 ← **推广到多原子**
3. Cacelli, Moccia, Rizzo (2000) — GTO 连续态计算 C2H2 截面 ← **非对称分子处理**
4. Carmona-Novillo, Moccia, Spizzo (1996) — LiH 截面与不对称参数

### 第二梯队（方法对比参考）
5. Toffoli et al. (2023) — Tiresia 代码（B-spline 路线对比）
6. Decleva, Stener, Toffoli (2022) — B-spline 连续态综述
7. Tenorio et al. (2022) — Dyson 轨道 + B-spline 方法
8. Stener et al. (2005) — TD-DFT B-spline 方法

### 第三梯队（背景与扩展）
9. Nisoli et al. (2017) — 阿秒分子电子动力学综述
10. McCurdy & Martín (2004) — 复缩放 + B-spline 实现
11. Wilhelmy et al. (1994) — Lobatto 技术
12. Hróðmarsson & van Dishoeck (2023) — 天体物理光电离数据库

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
