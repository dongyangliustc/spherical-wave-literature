# 按相关度分级的阅读清单（2026-09-11 重写）

> **口径**：⭐ 表示**本项目当前阶段的阅读优先级**，不等价于 registry 的 `relevance` 字段（后者表"与项目主题的相关性"）。二者允许不一致（例：Nisoli 2017 registry=medium 而 ⭐=⭐⭐），这不是矛盾，是不同轴。
> **判据锚点（2026-09-11 版）**：Born 残差谱范数 ‖V_res G_ref W‖₂ ≈ 776.2 不收敛（交换 K = 4.83 主导、非球性四极 41.5）。"高相关" = 能影响 ①连续态表示层 ②积分核 ③交换与共振处理 ④基准比对 四类决策之一。**该锚点须随瓶颈迁移而更新。**
> **范围**：67 篇（全文可用，参与分级）。另 2 条 `state: discovered`（无 PDF）不参与分级，见 `by_topic.md` 附录。

| 档位 | 定义 | 篇数 |
|---|---|---|
| ⭐⭐⭐⭐⭐ | 紧耦合：本路线方法学母体 / 与项目同题的公式来源 / 直接可比对的基准 | 6 |
| ⭐⭐⭐⭐ | 中耦合：能改变实现细节或架构选择，或需交叉验证的平行路线领头工作 | 18 |
| ⭐⭐⭐ | 弱耦合：特定专题或平行路线的实现细节，定向查阅 | 32 |
| ⭐⭐ | 无耦合：主题偏离，仅作概念/引用背景 | 11 |

---

## ⭐⭐⭐⭐⭐ 核心必读（6 篇）

**1. Cacelli, Moccia, Rizzo (1993)** — *J. Chem. Phys.*
→ GTO + L² 技术算 H₂ 光电离截面，**本项目方法学母体**
→ 对应模块：`momentum_gto`、`sw_matrix_element`、`benchmark_h2`

**2. Cacelli, Moccia, Rizzo (1998)** — *Phys. Rev. A*
→ 推广至微分截面与不对称参数 β，`angular_reduction` 的原始依据
→ 对应模块：`angular_reduction`、`frame_transform`、`benchmark_n2`

**3. Cacelli, Moccia, Rizzo (2000)** — *Chem. Phys.*
→ 非对称/多原子分子（C₂H₂）处理
→ 对应模块：`frame_transform`、`benchmark_c2h2`

**4. Carmona-Novillo, Moccia, Spizzo (1996)** — *Chem. Phys.*
→ 混合 GTO/STOCOS L² 基组，LiH 截面 + β；表示层混合策略的先例
→ 对应模块：`momentum_gto`、`angular_reduction`、`benchmark_lih`

**5. Huang, Li, Luo, Wu, Duan, Zhang (2026)** — *J. Chem. Phys.*
→ **与项目同题**：递归 Gaussian 积分高效计算阴离子光脱附截面，可直接复现比对
→ 对应模块：`PW_integral`、`GTO_integral`、`momentum_gto`、`CS_calculator`

**6. Mahato, Skomorowski (2026)** — *arXiv:2605.18564*
→ 球高斯与平面波调制高斯基上的**自由粒子格林函数矩阵元解析递推** —— `SW_integral` / `continuum_wave` 的公式直接来源
→ 对应模块：`continuum_wave`、`SW_integral`、`momentum_gto`、`sw_matrix_element`

---

## ⭐⭐⭐⭐ 重要参考（18 篇）

### 积分核（3 篇）

**7. Obara, Saika (1986)** — *J. Chem. Phys.*
→ Cartesian Gaussian 积分递推（OS 递推）原始文献，`GTO_integral` 的算法底座

**8. Obara, Saika (1988)** — *J. Chem. Phys.*
→ 广义递推公式，**含 Fourier 变换核**，动量空间积分的直接依据

**9. McMurchie, Davidson (1978)** — *J. Chem. Phys.*
→ Hermite 辅助函数展开方案，与 OS 递推互补的积分实现路线

### 可分势与 Schwinger（4 篇）

**10. Domcke (1983)** — *Phys. Rev. A*
→ 投影算符 + 可分势散射；`separable_potential` / `tau_matrix` 的理论母体

**11. Lucchese, McKoy (1979)** — *J. Phys. B*
→ Schwinger 变分原理用于电子散射（原始文献）

**12. Lucchese, Takatsuka, McKoy (1986)** — *Phys. Rep.*
→ Schwinger 变分在电子-分子碰撞与分子光电离中的系统综述，实现的主要参照

**13. Lucchese, McKoy (1983)** — *Phys. Rev. A*
→ 变分表达的 Padé 逼近修正；**变分收敛风险的直接证据**

### 表示层增强（5 篇）

**14. Wilhelmy, Ackermann, Görling, Rösch (1994)** — *J. Chem. Phys.*
→ Lobatto 形状函数 + GTO 混合基组；表示层构造的先例

**15. Moccia, Montuoro (2003)** — *Chem. Phys. Lett.*
→ STO + B-spline 混合 L² 基组算 Li₂ 微分截面；"表示层拼装"的成熟范例

**16. Cacelli (1997)** — *J. Phys. B*
→ **直接评估 GTO 类表示对连续态的描述能力**，正对 J.4 表示层归因问题

**17. Gozem, Gunina, Ichino, Osborn, Stanton, Krylov (2015)** — *J. Phys. Chem. Lett.*
→ 光电子波函数取平面波还是 Coulomb 波的定量评估；归一化与规范（L/V）风险的直接证据

**18. Marante, Argenti, Martín (2014)** — *Phys. Rev. A*
→ 混合 Gaussian-B-spline 连续态的显式构造，跨基组拼装实操参考

### 球面波与多中心（3 篇）

**19. Felderhof, Jones (1987)** — *J. Math. Phys.*
→ 矢量 Helmholtz 方程球面波解的加法定理，`spherical_multipole` 展开合并的数学底座

**20. Gharibnejad, Douguet, Schneider (2021)** — *Comput. Phys. Commun.*
→ 多中心求积直接构造分子连续态；**Phase K 多中心扩展的首选备选方案**

**21. Gil, Winstead, Sheehy, McKoy (1990)** — *Phys. Scr.*
→ Feshbach-Fano + Mulliken 轨道分析形状共振；**直接对应 J.3.5 交换 K=4.83 主导的诊断**

### 平行路线领头工作（1 篇）

**22. Toffoli, Coriani, Stener, Decleva (2024)** — *Comput. Phys. Commun.*
→ Tiresia 代码：平行路线（B-spline）领头代码，交叉验证与叙事定位的主要对照
→ 注：DOI 后缀为 2023（注册年），出版年为 2024（CPC 297, 109038）

### Dyson 轨道与多体关联（2 篇）

**23. Schio, Alagia, Moitra, Toffoli, Ponzi, Stener, Coriani, Decleva et al. (2026)** — *J. Chem. Phys.* **164**, 204301
→ 手性分子（环氧氯丙烷）Cooper 极小处光电子动力学：HF/DFT 无法解释的 β 振荡，**仅 EOM-CCSD Dyson 轨道（同对称性单空穴组态混合）可重现**
→ **附左右 Dyson 轨道与谱强度 γ^L·γ^R 完整公式** —— Dyson 轨道侧与本项目同题的公式来源 + 直接可比对的 β 基准
→ 对应模块：`frame_transform`、`momentum_gto`、`method_comparison`
→ 注：registry 原 `doi: null`，2026-09-11 经 Crossref 题名检索补为 `10.1063/5.0333577`

**24. Keizer, Paggi, Berger, Romaniello, Förster (2026)** — *arXiv:2608.25669*
→ MCDE 与 ADC(3) / nD-ADC(3) 的系统基准：**引用 ADC(3) 精度时必须注明分支**（`nD-ADC(3)` ≠ `Dyson-ADC(3)`，差 ~0.1 eV，强关联 >0.25 eV）
→ **边界提示**：MCDE 家族的增益在束缚态谱函数侧，**不能**用于本项目的连续态瓶颈（Born 谱范数 776.2）
→ 对应模块：`correlation_strategy`、`method_comparison`、`benchmark_strategy`

---

## ⭐⭐⭐ 专题与扩展（32 篇）

定向查阅用：读摘要 + 关键公式节即可，不必通读。

| 文献（年） | 出处 | 判据 / 用途 |
|---|---|---|
| Brosolo, Decleva (1992) | Chem. Phys. | B-spline 变分连续态开端；H₂⁺ 基准与基组无关性论据 |
| Decleva, Stener, Toffoli (2022) | Molecules | Tiresia 路线总览，快速定位 |
| Stener, Fronzoni, Decleva (2005) | JCP | 非迭代 TD-DFT + 多中心 B-spline 实现细节 |
| Tenorio, Ponzi, Coriani, Decleva (2022) | Molecules | 多参考 Dyson 与连续态耦合，关联处理对照 |
| Moitra, Coriani, Decleva (2021) | JCTC | EOM-CC Dyson + B-spline，关联效应捕获对照 |
| Ruberti (2019) | JCTC | 受限关联空间 ADC + B-spline 全截面计算 |
| Bachau, Cormier, Decleva, Hansen, Martín (2001) | Rep. Prog. Phys. | B-spline 应用权威综述，方法史定位 |
| Zatsarinny, Bartschat (2013) | J. Phys. B | B-spline R-matrix 综述，分区理论对照 |
| Mašín, Benda, Gorfinkiel, Harvey, Tennyson (2020) | CPC | UKRmol+ 代码包，工作流与验证链设计参照 |
| Fang, Su, Tennyson et al. (2026) | JCP | 表示层标定（参考态权重）；**应用前须先做瓶颈归因 A/B** |
| Natalense, Lucchese (1999) | JCP | ePolyScat 截面 + β 算例，基准数据来源 |
| Gianturco, Lucchese, Sanna (1994) | JCP | 静态交换近似的 ePolyScat 算例，可分势应用实例 |
| McCurdy, Martín (2004) | J. Phys. B | ECS + B-spline 关键实现（复缩放备选路线） |
| Matsuzaki, Yabushita (2017) | J. Comput. Chem. | 复 GTO（cGTO）连续态 + 双势公式 |
| Ammar, Ancarani, Leclerc (2021) | J. Comput. Chem. | 复高斯 + Coulomb 连续态，长度/速度规范讨论 |
| Jagau, Bravaya, Krylov (2017) | Annu. Rev. Phys. Chem. | 电子共振（CAP/复能量）系统综述，共振处理选型 |
| Hazi (1978) | J. Phys. B | 纯 L² 方法算共振宽度源头文献 |
| Ota, Yamazaki, Sebilleau (2021) | J. Phys. B | 全势多中心 MFPAD，角分布完整处理参照 |
| Borràs, González-Vázquez, Argenti (2021) | JCTC | Feshbach 共振附近 MFPAD 的 XCHEM 实现 |
| Borràs, Fernández-Milán, Argenti (2023) | CPC | XCHEM-2.0 代码化版本，工作流参照 |
| Duan, Gong, Cheng, Zhang (2024) | PRA | 多中心连续态 → MFPAD（含扭曲光子），前沿 |
| Huang, Jin, Zhang, Chen, Li (2026) | arXiv:2603.13995 | 截断球面波 NAO 基，基组设计思路借鉴 |
| Moroz (2006) | J. Phys. A | 准周期格林函数格点求和，周期性延拓备用 |
| Hughes (1994) | J. Math. Phys. | 任意自旋球面波展开，自旋分辨扩展时查阅 |
| Gonis, Butler (2000) | Springer | 多重散射/MST 与 t 矩阵系统论述，概念参照 |
| Eyert (2000) | Int. J. Quantum Chem. | ASW 方法导论，球面波基在固体中的经典用法 |
| Vanroose, Horner, Martín, Rescigno, McCurdy (2006) | PRA | H₂ 双电离 ECS 精确基准，H₂ 体系扩展参考 |
| Paggi, Berger, Romaniello (2026) | arXiv:2607.20070 | MCDE 芯/价光发射谱（束缚态侧），方法边界参照 |
| Romaniello, Berger (2026) | arXiv:2603.27329 | 屏蔽 MCDE（体相 Si plasmon 卫星），MCDE 屏蔽起点 |
| Zhang, Li, Pathak, Sato, Ishikawa, He (2026) | PRL 136(1) | 时域扩展 Koopmans 定理；**自然轨道不能替代 Dyson 轨道**的边界证据 |
| Yuwono, Li, Zhang, Li, DePrince (2025) | JCP 162(8) | 双分量相对论 EOM-CC 电子电离，相对论化实现对照 |
| Thapa, Dutta (2026) | arXiv:2602.21834 | 相对论 EOM-CC 三体修正，精度基准（MAE 0.01–0.08 eV） |

---

## ⭐⭐ 边缘与存档（11 篇）

主题偏离，仅作概念或引用背景；不进精读队列。

- **Nisoli, Decleva, Calegari, Palacios, Martín (2017)** — *Chem. Rev.*，阿秒电子动力学综述
- **Calegari, Trabattoni, Palacios, Ayuso, Castrovilli, Decleva, Martín, Nisoli (2016)** — *J. Phys. B*，阿秒电荷迁移（生物分子）
- **Ruckenbauer, Mai, Marquetand, González (2016)** — *Sci. Rep.*，trPES 去活化通道（旁支）
- **Hróðmarsson, van Dishoeck (2023)** — *A&A*，Leiden VUV 截面数据库（与当前路线无耦合）
- **Djajaputra, Cooper (2003)** — *Phys. Status Solidi B*，LMTO 紧束缚参数（NiAl）
- **Dziedzic, Hill, Skylaris (2013)** — *JCP*，线性标度 HF 交换能（Wannier）
- **Corsaro, Miano, Tamburrino, Ventre, Forestiere (2026)** — *IEEE TAP*，MLFMA 电磁散射超表面
- **Asadova, Achouri, Arjas, Auguié, Aydin, Rockstuhl (2025)** — *JQSRT*，T 矩阵数据格式建议
- **Sellié, Berger, Romaniello (2026)** — *Phys. Rev. B* 114(12)，MCDE 双电离谱（Auger 方向，与当前路线无耦合）
- **Misael, Gomes (2024)** — *arXiv:2412.08403*，相对论嵌入式 CVS-EOM-CC 处理锕系芯电离（体系偏离）
- **Mukhopadhyay, Mukherjee, Gururangan, Piecuch, Dutta (2026)** — *JCTC* 22, 3233，相对论 DIP-EOM-CC（双电离势，体系偏离）

---

## 与 2026-07-22 旧版的差异

旧版为两份互不一致的清单（`by_relevance.md` 19 篇 vs `README.md` 明细表 20 篇：对 Moccia 2003 差 2 档、对 Brosolo/Stener 差 1 档，另有 3 篇为 README 独有）。本次按单一口径统一重定级：

| 类别 | 篇数 | 说明 |
|---|---|---|
| 新增定级 | 38 | 旧版未收录（⭐⭐⭐⭐⭐ 2 / ⭐⭐⭐⭐ 9 / ⭐⭐⭐ 19 / ⭐⭐ 8） |
| 上调 | 2 | Moccia & Montuoro 2003（3→4，表示层拼装范例）；Gozem 2015（3→4，规范/归一化风险证据） |
| 下调 | 10 | B-spline 块 6 篇（4→3，平行路线降为交叉验证）；四篇综述/旁支（3→2，无实现耦合） |
| 不变 | 9 | Cacelli 1993/1998/2000、Carmona-Novillo 1996（均 5★）；Wilhelmy 1994、Brosolo 1992、Stener 2005 等 |

> **下调不等于降级处理**：所有文献仍在 registry 中、仍进向量索引、仍可被检索与引用，仅"是否属于当前精读队列"的判定发生变化。

---

## 附：未参与分级的待下载条目（2 条，`state: discovered`）

### 旧版遗留的两个"幽灵条目"（2026-09-11 反向核实后登记）

`README.md` 明细表曾列入但从未落地（无 registry、无 PDF）：

| 文献 | 出处 | 处置 |
|---|---|---|
| Cacelli, Carravetta, Rizzo, Moccia (1990) | MOTECC-90，Springer 书章 pp. 639-691 | 已登记；书章全文可获取性待评估 |
| Majety, Zielinski, Scrinzi (2015) | New J. Phys. 17(6), 063002 | 已登记；OA 可下载 |

### B. 并行调研新增的 10 条 —— 已结清

来源 `outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`：MCDE / 时域 EKT / 相对论 EOM-CC 三类。2026-09-11 已补齐全文（`papers/Dyson_orbital/`）并完成定级：**⭐⭐⭐⭐ 2 篇（Schio、Keizer）· ⭐⭐⭐ 5 篇 · ⭐⭐ 3 篇**，归入 `by_topic.md` **T12**。

> 边界说明：本清单的 ⭐ 分级**只覆盖有全文的 67 篇**。无全文条目先补文献、再定级，避免"凭摘要定优先级"。
