# 文献到代码桥接：Phase G 技术决策指南

> 从四份方法学深度调查报告与原始论文出发，回归到 SW 项目的核心源代码问题
> 生成日期：2026-07-29
> 目标读者：SW Master Agent（注入 Phase G 上下文）+ DY（人工审查）
> 方法论：每个技术决策点 = 文献证据 → 代码影响 → 验证标准

---

## 一、方法学定位：本项目在文献谱系中的位置

```
Cacelli-Moccia-Rizzo (1990s)              Lucchese-McKoy (1979-)
GTO-L² 实空间方法                         迭代 Schwinger 变分法
├─ Stieltjes-Tchebychev 矩重建               ├─ ePolyScat 代码
├─ 长度/速度规范一致性协议                   ├─ 单中心展开
├─ DFT/LB94 渐近势                           └─ Padé 加速
└─ 混合 GTO+STOCOS 基组                          ↓
    ↓                                        Phase G Tier 2
    ↓                                    (我们的 GTO-FT 动量空间版本)
    ↓
本项目 Phase F
(自由 Green 函数基线)

        ────── 本项目 Phase G ──────→
        动量空间 Born/Schwinger (新)
        ├─ Tier 1: 一阶 Born 修正 (无文献先例)
        └─ Tier 2: 可分展开 Schwinger (参照 Lucchese 1986, Domcke 1983)
```

**核心论断**：本项目的动量空间 GTO-FT + 球面波基组方法是 Cacelli 方法的"动量空间版本"，但 Phase G 的 Born/Schwinger 修正又借鉴了 Lucchese 的变分法。**这两个文献传统的融合在数学上是否正确，是本项目最需要验证的核心问题。**

---

## 二、逐模块技术决策指南

### 2.1 G.1-G.2：静态势 V_static 动量空间表示

**原始文献来源**：
- **Cacelli 2000** (Chem. Phys. 254, 113): 首次使用 DFT 势（LB94 交换相关势）替代 HF 势计算 GTO 连续态。关键发现：LB94 势的渐近行为 (-1/r) 对截面精度至关重要。
- **Stener 2005** (JCP, `Decleva_2022` 中引用): B-spline TDDFT 方法中使用 LB94 势改善渐近 Coulomb 尾部。

**当前实现** (`momentum_potential.py`):
- 使用 `V_static = V_nuc + V_Coulomb[ρ] + V_XC[ρ]`（局域 KS 势）
- GTO 积规则 `e^{-αr²}e^{-βr²} = e^{-(α+β)r²}` 用于 FT

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| V_XC 泛函选择 | Cacelli 2000: LB94 优于 LDA，渐近行为决定截面。Stener 2005: 确认 TDDFT+LB94 方案 | 当前仅 xc_mode='skip' 通过（Tier 1 不包含 XC） | **G.11 基准测试时启用 LB94 作为 Tier 2 默认** |
| 中性 1/s² 消除 | GTO 积规则在 s→0 时产生 1/s² 发散，需 Taylor 展开 | ✅ 已实现 `_small_s_taylor` | 维持现状 |
| Fock 交换的非局域性 | Cacelli 1993: HF vs DFT 势在连续态中有显著差异（~20%）。本项目当前 Tier 1 只用局域 KS 势 | G.7 已声明处理 J-K 但实际用 DFT V_eff | ⚠️ **G.7 需确认是否包含 K 算符**（见 §2.4） |

**验证标准**：
- [ ] He V_static(p-q) 的渐近极限是否满足 1/|p-q|² Coulomb 行为？
- [ ] 与 Cacelli 1993 表 II（H₂ 的偶极矩阵元实部/虚部）比较，误差 < 5%

---

### 2.2 G.3：Born 核角向积分

**原始文献来源**：
- **Felderhof 1987** (J. Math. Phys.): 球面波加法定理，标量波 `j_l(k|r₁-r₂|)Y_lm` 的展开。这是 Legendre 加法定理在 Born 核中的数学基础。
- **Wilhelmy 1994** (JCP): Lobatto 形状函数 + 部分波展开，连续态角向分解的直接实现参考。

**当前实现** (`angular_reduction.py`):
- `angular_integrate_born_kernel()` via 齐次 degree-l 多项式表示 + 按 m 分组合并
- 已验证：各向同性核 l>0 消失 < 1e-10，大 κ MC 测试 3% 容差

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| lmax 截断 | Wilhelmy 1994: 光电离中 l=3-4 足够（由于偶极选择定则）。Cacelli 1993: H₂ 需要 lmax=3 | lmax=3 ✅ | 维持 |
| non-s-type 密度 | Cacelli 1998: N₂ 的 p-type 初态需要额外的角向耦合 | NotImplementedError | **Phase H 分子测试前必须实现** |
| Born 核的收敛性 | Felderhof 1987: 加法定理在 |r₁-r₂| 大时收敛慢 | 未测试 | **G.11 加测多中心收敛性** |

**验证标准**：
- [ ] Born 核在各向同性极限下 l>0 完全消失（当前 ✅）
- [ ] 多中心场景 Born 核 vs 直接数值积分（dΩ_p, dΩ_q 离散化），误差 < 1%

---

### 2.3 G.4-G.6：Born 修正实现与 Gate

**原始文献来源**：
- **Domcke 1983** (PRA 28, 2777): Feshbach 投影算符形式主义。这是 Born 修正的原始理论框架——Lippmann-Schwinger 级数的一阶截断。
- **Cacelli 1993** (JCP 98, 8742): H₂ 截面规范一致性测试。这是 Born 修正 Gate 的基准数据源。

**当前实现** (`sw_matrix_element.py`):
- `_compute_born_correction()`: 双重径向积分 + Born 核角向积分
- G.6 Gate：单中心 H/He Born=0（已知物理限制），PROMOTE_WITH_CAVEATS

**关键发现 — 文献与实现的直接对比**：

```
文献 (Cacelli 1993 H₂):
├─ L²-GTO + Stieltjes 矩重建
├─ 直接求解偶极矩阵元 → 截面
├─ 长度规范 σ_L / 速度规范 σ_V 比值 ≈ 0.9-1.1
└─ 无需 Born 修正（L² 方法天然包含 V_eff）

本项目 (Phase F+G):
├─ 动量空间 GTO-FT + 球面波基组
├─ 自由 GF D_if(free) + Born 修正 D_if(Born)
├─ 待验证：Born 修正后的 L/V 比值
└─ Born 修正为必需（自由 GF 不含 V_eff）
```

**核心问题**：Cacelli 的 L² 方法天然包含了势能（因为 L² 基在实空间展开），而本项目的自由 GF 不含任何势能——因此 Born 修正不是"改进"，而是**从非物理自由粒子到物理散射的质变**。这意味着 Born 修正的精度必须与 Cacelli 1993 的 L² 结果相当，而不是"比无 Born 好就行"。

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| 单中心 Born=0 问题 | Cacelli 1993: L² 方法中初始 GTO 已有 V_eff，无此问题 | G.6 PROMOTE_WITH_CAVEATS | **在 G.11 多中心基准中验证 Born 实际贡献** |
| 双规范一致性 | Cacelli 1993 §IV: L/V 比值是验证规范不变性的核心指标。L²-ST 方法本身满足规范不变性 | G.6 He 2点 L/V>10 | **G.12 目标：所有基准系统 L/V < 3** |
| Born 修正的 (2π)^{-3/2} 归一化 | Cacelli 的动量空间公式使用标准 FT 约定 | ✅ 已修复 | 维持 |

**验证标准**：
- [ ] H₂ Born 修正后的截面与 Cacelli 1993 图 2 比较，误差 < 10%
- [ ] 所有系统 L/V 比值 < 3（放宽自 Cacelli 1993 的 < 1.1，因为我们的方法不同）
- [ ] Born 修正使 H 原子截面从 0 变为非零（验证 Born 确实提供了 angular coupling）

---

### 2.4 G.7：可分矩阵 V_αβ

**原始文献来源**：
- **Domcke 1983** (PRA 28, 2777) §11: "If Q is spanned by the first N eigenstates, then H_{PQ}(E-H_{QQ})^{-1}H_{QP} is exactly a rank-N separable potential." 这是可分展开的数学基础。
- **Lucchese 1986** (Phys. Rep. 131, 147): "Applications of the Schwinger variational principle..." §3-4: V_αβ 的 GTO 基矩阵元计算。**这是我们的直接实现参考。**
- **Cacelli 1993** (JCP 98, 8742): GTO 双电子积分的实空间计算方法（类比于 Obara-Saika 递推）。

**当前实现** (`separable_potential.py`):
- `V_αβ = <χ̃_α|J-K|χ̃_β>` 在 GTO-FT 基上
- K-sum 公式 bug 已修复（交叉项 (αν|βμ)）

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| 是否包含 Fock 交换 K？ | Domcke 1983: 可分展开理论上包含完整的 V_eff。Cacelli 2000: DFT 势可替代 HF 交换，减少计算量 | 代码声明 J-K，但实际可能只用 DFT | ⚠️ **G.7 需明确 V_eff 层次：DFT-only (Tier 2a) vs HF-with-exchange (Tier 2b)** |
| 基组大小 R | Lucchese 1986: ePolyScat 使用 ~50-200 基函数。Cacelli 1993: H₂ 用 ~30 GTO | R = 50-200 | 维持 |
| 矩阵正定性 | Domcke 1983: V_αβ 在物理势下应是正定或至少良态 | 已检测条件数 | **G.9 前加 Hermitian 检查** |

**核心问题**：G.7 在 SPEC 中声明为 `V_αβ = <χ̃_α|J-K|χ̃_β>`（包含 Fock 交换），但实际实现使用的是 DFT 局域势。**Fock 交换算符在动量空间是非局域的：K(p,q) ≠ K(|p-q|)**，这意味着当前的 `separable_potential.py` 如果使用 DFT 势，其数学结构与 SPEC 声明的不一致。

**建议**：
1. 确认当前 `separable_potential.py` 使用的 V_eff 类型
2. 如果仅 DFT：在 SPEC 中明确记录"当前实现使用局域 KS 势，非局域 Fock 交换推迟到 Phase H"
3. 如果需要 Fock 交换：Obara-Saika 递推需要在动量空间重新推导

**验证标准**：
- [ ] V_αβ 矩阵 Hermitian，条件数 < 1e6
- [ ] 对角线占优（物理上应有 V_αα 远大于 V_αβ(α≠β)，因为 GTO 是局域的）
- [ ] He 原子 V_αβ 的基态 vs 连续态基的对角项量级合理（~1-10 Hartree）

---

### 2.5 G.8：G₀⁺(E) Green 函数矩阵

**原始文献来源**：
- **Domcke 1983** (PRA 28, 2777): Eq. (2.28): G₀⁺(p,p';E) = δ(p-p') / (E - p²/2 + iε)。动量表示中对角的。
- **Lucchese 1986** (Phys. Rep. 131, 147): G₀⁺ 在 GTO 基中的矩阵元，包含主值积分 (principal value integral)。

**当前实现** (`green_function_matrix.py`):
- G₀⁺(E) = <χ̃_α|G₀⁺|χ̃_β> = ∫d³p χ̃_α*(p) χ̃_β(p) / (E - p²/2 + iη)
- 径向 `integrate_pole_subtracted()` + 角向 `angular_reduction`
- 已验证：Im G[0,0] = on-shell residue (ratio=1.0000)

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| η 参数选择 | Lucchese 1986: η 决定共振宽度。物理上 η → 0⁺ | 当前实现中有 η 参数 | **G.11 测试不同 η 值的灵敏度** |
| 对角近似 | Domcke 1983: G₀⁺ 在动量表示中对角。在 GTO 基中非对角 | 当前实现完整非对角 | 维持 |
| 主值积分方法 | Lucchese 1983: Padé 近似加速主值积分收敛 | 当前用 pole subtraction | **G.9 后可加 Padé 加速** (Lucchese 1983 方法) |

**验证标准**：
- [ ] G₀⁺ 矩阵 Hermitian（G_αβ = G_βα）
- [ ] 虚部 = -π × on-shell 态密度（当前 1.0000 ✅）
- [ ] E → ∞ 时 G₀⁺ → 0（自由粒子 Green 函数衰减）
- [ ] 实部的主值积分与留数定理结果一致

---

### 2.6 G.9：τ(E) 求解器

**原始文献来源**：
- **Domcke 1983** (PRA 28, 2777): Eq. (2.34b): τ(E) 的 Schwinger 变分形式。这是整个 Phase G 的理论核心。
- **Lucchese 1986** (Phys. Rep. 131, 147): Schwinger 变分原理的各种泛函形式，包括 Kohn 变分与 Schwinger 变分的等价性证明。
- **Gonis & Butler 1999** (Multiple Scattering, Springer): Appendix F: 角动量表象中 t-matrix 求逆。

**当前实现** (`tau_matrix.py`):
- `τ = [1 - V·G₀]^{-1}·V` via `numpy.linalg.solve`
- 11/11 tests pass, Lippmann-Schwinger residual 1e-10

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| solve vs inv | SPEC 字面要求 inv，实现用 solve | solve 更数值稳定 ✅ | 记录为 Spec Amendment |
| 矩阵条件数 | Gonis 1999: 当 E 接近共振能量时，[1-VG₀] 可能近奇异 | 条件数诊断 1e12 阈值 | **降低阈值到 1e8，超阈值时输出 WARNING** |
| Padé 加速 | Lucchese 1983: [N/N] Padé 近似系统修正变分误差 | 未实现 | **Phase H 增强项**：对 τ(E) 做 Padé 外推验证 |

**验证标准**：
- [ ] Lippmann-Schwinger 残差 ‖(1-VG₀)·τ - V‖ / ‖V‖ < 1e-8
- [ ] 标量 1×1 极限 τ = V/(1-VG₀) 匹配解析解（当前 ✅）
- [ ] τ(E) 在共振能量处的极点行为正确（虚部有峰，实部过零）

---

### 2.7 G.10：Schwinger 振幅（关键任务，当前卡在 503）

**原始文献来源**：
- **Lucchese & McKoy 1979** (PRA 21, 112): 首次将 Schwinger 变分原理应用于光电离，计算 He 截面。**这是最直接的实现参考。**
- **Domcke 1983** (PRA 28, 2777): Eq. (2.34a): Schwinger 振幅的完整表达式。
- **Lucchese 1986** (Phys. Rep. 131, 147): §6-7: 光电离中 Schwinger 变分法的实现细节。

**SPEC Eq. (11.9)**:
```
D_if ∝ ⟨p_f|p|φ̃_i⟩ + Σ_αβ ⟨p_f|p·G₀⁺|χ̃_α⟩ τ_αβ(E) ⟨χ̃_β|φ̃_i⟩
```

**文献指导的关键验证**：

Schwinger 振幅的正确实现需要验证以下物理性质：

1. **τ → 0 极限**：当 V → 0 时，Schwinger 振幅应退化为自由 GF 振幅 + Born 修正（已验证 ✅）
2. **τ → V 极限（R=1 标量）**：单基函数时，Schwinger 振幅应等于 Born 修正（已验证 ✅）
3. **幺正性**：Im D_if(Schwinger) 应满足光学定理（未验证 ⚠️）
4. **与 Lucchese 1979 He 截面比较**：这是最关键的物理验证（待做）

**文献指导的决策**：

| 决策点 | 文献证据 | 当前状态 | 建议 |
|--------|---------|---------|------|
| 双规范实现 | Cacelli 1993: 长度和速度规范应给出相近结果。Lucchese 1986: Schwinger 变分自动保证规范一致性（在完备基极限下） | 已计划 ✅ | **G.10 必须同时实现长度和速度规范** |
| 数值稳定性 | Lucchese 1986: τ(E) 在近共振时可能数值不稳定，需 Padé 处理 | 未考虑 | **G.10 应包含条件数检查 + near-singular 回退** |
| 与 ePolyScat 结果的对比 | Lucchese 1979 图 1-3 提供 He 和 H₂ 的 Schwinger 计算结果 | 未计划 | **G.11 Gate 必须与 Lucchese 1979 已发表结果对比** |

**核心问题**：G.10 是 Phase G 的"验收测试"——如果 Schwinger 振幅不能重现 Lucchese 1979 的 He/H₂ 光电离截面（在 20% 精度内），则说明动量空间的 GTO-FT 方法在数学上有根本缺陷。如果能够重现，则证明动量空间 + 球面波基组的路径是可行的。

**验证标准**：
- [ ] τ=0 极限下 D_if(Schwinger) = D_if(Born)（数值相等，相对误差 < 1e-12）
- [ ] 长度规范和速度规范的截面差异 < 5%
- [ ] He 截面与 Lucchese 1979 图 1 比较，峰值位置 ±0.5 eV，峰值高度 ±20%
- [ ] 所有已存在的 Phase F 回归测试通过（不破坏已有功能）

---

### 2.8 G.11-G.12：分子基准与 Gate

**原始文献来源**：
- **Cacelli 1993** (JCP 98, 8742): H₂ 截面的完整数据集（图 2-6）——这是 Tier 2 Gate 的黄金标准。
- **Cacelli 1998** (PRA 57, 1895): N₂ 微分截面和 β 参数——如果系统推进到 N₂。
- **Lucchese 1982** (PRL/博士论文): N₂ 和 CO₂ 的形状共振——如果验证共振结构。

**SPEC Gate 标准**：

| Gate 项 | 标准 | 文献参考 |
|---------|------|---------|
| G.11 H₂ benchmark | 截面vs Cacelli 1993 图2，误差 <15% | Cacelli 1993 JCP 98, 8742 |
| G.11 CH₂O benchmark | 无已发表参考；验证 Born vs Schwinger 差异 | N/A（需估算或与其他方法对比） |
| G.12 L/V → 1.0 | 所有系统 L/V < 3 | Cacelli 1993 §IV (放宽标准) |

**关键决策**：

**CH₂O 基准缺乏文献参考**是一个重要问题。SPHERICAL_WAVE_SPEC.md G.11 要求 "Compare against Cacelli 1993/1998 published results"，但 Cacelli 从未计算过 CH₂O。选项：

1. **方案 A**：H₂ → N₂ → CH₂O 渐进推进（参考 Cacelli 1993→1998→2000 的路径）
2. **方案 B**：直接用 CH₂O 与 ePolyScat 结果对比（需获取 ePolyScat 代码或许可）
3. **方案 C**：H₂ + CH₂O 并行，CH₂O 用内部一致性验证（Born vs Schwinger vs 自由 GF 差异）

**建议方案 A**：跟随 Cacelli 的论文推进路径（H₂ 1993 → N₂ 1998 → C₂H₂ 2000），每个分子有明确的已发表基准数据。CH₂O 推迟到 Phase H。

**验证标准**：
- [ ] H₂ Schwinger 截面 vs Cacelli 1993 图 2：误差 < 15%
- [ ] H₂ L/V 比值 < 3（所有能量点）
- [ ] 所有 Phase F 回归测试通过（破坏性变更检测）
- [ ] Born 修正 vs Schwinger 修正的差异对 H₂ 不应超过 30%（否则说明 Born 收敛不够）

---

## 三、整体技术风险矩阵

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| 动量空间 GTO-FT + 球面波的 Born 修正数学不自洽 | 低 | 极高 | 用 Cacelli 1993/1998 已知结果严格验证 |
| Schwinger 振幅在近共振时数值不稳定 | 中 | 高 | 条件数诊断 + Padé 回退 |
| Fock 交换缺失导致截面系统性偏差 | 高 | 中 | 明确记录为 Spec Amendment，Phase H 添加 |
| CH₂O 缺少文献基准，Gate 无客观标准 | 高 | 中 | 改用 H₂→N₂→C₂H₂ 路径，参考已知数据 |
| Born 修正一阶截断对分子体系不够 | 中 | 高 | 用 H₂ Born vs Schwinger 差异量化截断误差 |

---

## 四、Phase G 上下文注入到 SW Master Agent

以下内容应注入到 SW Master Agent 的 G.10 派遣指令中：

```
### 文献上下文（Phase G 技术决策指南摘要）

**G.10 的核心验证目标**：
实现 SPEC Eq. (11.9) 后，必须验证其与 Lucchese & McKoy 1979 (PRA 21, 112) 
已发表 He 光电离截面的定量一致性。这是动量空间 GTO-FT + Schwinger 方法的"存在性证明"。

**关键物理性质**：
1. τ→0 极限：应退化到 Born 修正（已验证）
2. 幺正性：Im D_if 应满足光学定理（需验证）
3. 双规范一致性：长度和速度规范截面差异 < 5%
4. 与 Lucchese 1979 比较：He 截面峰值位置 ±0.5 eV，高度 ±20%

**已知限制**：
- 当前 V_eff 使用局域 KS 势，不含非局域 Fock 交换
- 单中心 H/He Born=0 是物理选择定则，非 bug
- 多中心系统才能看到 Born 修正的实际贡献

**相关原始文献**（位于 papers/ 目录）：
- GTO_continuum/Cacelli_1993_H2_photoionization_JCP.pdf
- GTO_continuum/Cacelli_1998_N2_differential_PRA.pdf
- spherical_wave/Domcke_1983_projection_scattering_PRA.pdf
```

---

## 五、执行检查清单（用于 SW Master Agent 和人工审查）

### G.10 实现检查（实现完成后）

- [ ] 执行 `_compute_schwinger_amplitude()` 的 τ→0 极限测试
- [ ] 验证长度/速度规范输出差异 < 5%
- [ ] 检查矩阵条件数，> 1e8 时输出 WARNING
- [ ] 所有现有测试套件通过（回归测试）
- [ ] 为单中心 H 原子测试（期望 Born=0, Schwinger≠Born?）

### G.11 基准检查（Gate 执行前）

- [ ] H₂ Schwinger 截面 vs Cacelli 1993 图 2
- [ ] 确认 Born 修正对 H₂ 的实际贡献量
- [ ] Born vs Schwinger 差异量化（如 > 30%，Born 收敛不足）
- [ ] L/V 比值统计

### 人工审查建议（DY 手动检查）

1. **G.7 V_eff 实际形式**：打开 `separable_potential.py`，确认是 DFT 局域势还是 HF J-K
2. **G.3 Born 核数学**：由于 Critical Bug 历史，建议独立推导 `angular_integrate_born_kernel()` 的关键公式
3. **G.11/G.12 文献基准**：确认 Cacelli 1993 的 H₂ 截面数据可以从 PDF 或已发表表格提取
