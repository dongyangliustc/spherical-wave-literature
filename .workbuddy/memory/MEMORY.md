# 项目长期记忆（spherical_wave_literature）

> 跨会话项目约定。过程细节见 `YYYY-MM-DD.md` 日常日志。

## 一、索引维护 SOP 与硬规则（2026-09-11）

**三层结构**：`index/registry/*.yaml`（受控事实来源）→ `index/*.md`（派生视图）→ 向量索引 chunk（由 `sources.yaml` 摄入，**md 改动后须重建才反映**）。

**SOP**：跨文件一致性比对 → 只改 `registry/*.yaml`（必过 `tools/validate_registry.py`）→ 派生 `index/*.md` → 三方 basename 核对 → **一次性** `ingest` 重建。
注：`registry/*.yaml`、`index/*.md`、`notes/*.md`、`outputs/*.md` 全进索引，一改即陈旧。

**常驻校验工具（勿再手工 grep 数数）**
- `tools/check_three_way.py`：三方一致性核对（磁盘 PDF / registry `paths.pdf` / `sources.yaml` `format=pdf`），六向差集，`--strict` 可作 CI 门禁。
- `tools/audit_index_counts.py`：索引层自洽审计（明细表行数、分档计数、每组行数、PDF 引用有效性/重复）。
- `tools/validate_registry.py`：受控词表校验（`role` 值误填进 `actionability` 这类错误肉眼必漏）。

**硬规则**
1. **DOI 后缀年 ≠ 出版年**。判定序：Crossref `published-print` > 卷号 > DOI 后缀。（实例：Tiresia `cpc.2023.109038` 实为 2024-04 / CPC 297。）
2. **registry 会被并行工作流写入** → 条目计数必须带时点标注，写完即复核。
3. **索引重建只做一次**，且在所有 md/yaml 改动之后。
4. **`index/*.md` 的 markdown 表格会被（编辑器侧）自动重新填充空格** → 任何解析这些表格的脚本**必须用空白容错正则**（`^\|\s*(T\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|`），不可锚定精确空白；改脚本后要在文件被外部改写之后再验一次。

## 二、文献入库标准流程（单篇 PDF 4 步）

1. **归位**：`papers/<主题子目录>/`，命名 `Author_Year_keywords_Journal.pdf`（单数第一作者姓氏优先，禁空格）。子目录：GTO_continuum / B_spline_continuum / Schwinger_L2 / R_matrix / spherical_wave / complex_scaling / general_review / Dyson_orbital。
2. **数据源登记**：`spherical_wave_mcp/config/sources.yaml` 追加 `source_id: paper-<作者>-<年份>`，`source_type: textbook`，`priority: 2`。
3. **registry 登记**：`index/registry/candidates.yaml` 追加（`id: lit-<作者>-<年份>-<主题>`），必含 doi / pdf 相对路径 / topic_tags / project_modules / state / relevance / role / actionability。
4. **索引重建**：`cd spherical_wave_mcp && .venv/Scripts/course-material-mcp.exe ingest --config config/sources.yaml --index data/index/materials.sqlite`（先备份 sqlite）。

**验证**：`search` 命中新 source_id，且打标 `provenance=literature` / `epistemic_status=literature_supported` / `claim_kind=fact`。

**三方对齐（批量入库后必做）**：`papers/**/*.pdf` basename 集合 ≡ registry `paths.pdf` basename ≡ `sources.yaml` 中 `format=pdf` 条目，三方全等。
**元数据必须经 PDF 正文 + Crossref/arXiv 核实，不可信文件名**（2026-09-11 查出 5 篇名实不符）。
核实通道：`curl` 可用（python urllib 直连 HTTPS 被沙箱阻断）；curl 须给 `D:/...` 路径，不能用 `/tmp`。
**AIP 文件名→DOI**：`044309_1_5.0307607.pdf` 中 `5.0307607` 即 DOI 后缀（前缀 10.1063）。

**主题归类边界**：纯 B-spline 一律入 `B_spline_continuum/`；混合基组（GTO+B-spline、STO+B-spline）留在 `GTO_continuum/`，以"核心表示是否为高斯类"裁定。

## 三、相关度定级口径

**两轴分离（勿混）**：registry `relevance`（主题相关性 core/high/medium/low）≠ `by_relevance.md` 的 ⭐ 星级（当前阶段阅读优先级）。二者允许不一致。

**星级 rubric**：⭐⭐⭐⭐⭐ 紧耦合（母体/同题公式来源/直接基准）· ⭐⭐⭐⭐ 中耦合（改实现或架构选择，或平行路线领头）· ⭐⭐⭐ 弱耦合（专题定向查阅）· ⭐⭐ 无耦合（仅概念背景）。
**当前锚点（2026-09-11）**：Born 残差谱范数 ‖V_res G_ref W‖₂≈776.2 不收敛（交换 K=4.83 主导、非球性四极 41.5）→ "高相关" = 影响 ①连续态表示层 ②积分核 ③交换与共振 ④基准比对 之一。**锚点须随瓶颈迁移更新**。
**重定级前必做跨文件一致性比对**（旧两份索引曾对 Moccia 2003 差 2 档）。
**"幽灵条目"双向缺口**：registry 有/PDF 无（→补下载）⇄ README 有/registry 与 PDF 皆无（→按 `state: discovered` 登记）。

**主题分组 T1–T12**：T1 GTO/L2 母体与基准 · T2 动量空间积分核 · T3 可分势与 Schwinger · T4 连续态表示层 · T5 球面波/加法定理/格林函数 · T6 多中心连续态与 MFPAD · T7 共振与交换 · T8 B-spline 平行路线 · T9 R-matrix/UKRmol+/ePolyScat · T10 复缩放 ECS · T11 光电离物理与背景 · T12 边缘存档。

## 四、知识库"同流不同信"体系

自产知识与文献同流进同一管道，但**不同信**：双轴打标 + 检索层 epistemic gate。
- **轴 A provenance**：`literature` / `own_publication` / `synth_summary` / `ideation`。
- **轴 B epistemic_status**：`unverified < consistent < literature_supported < benchmark_verified`；负向 `conflicting/refuted/superseded/stale`。
- **claim_kind**：`fact`(须文献锚定) / `derivation` / `hypothesis`(永不注入) / `workflow`。
- **硬规则**：注入门槛 rank ≥ 2 且 provenance∈{literature, own_publication}；核实粒度主张级 + chunk 继承 fail-closed；门控在检索层不在入库层；**机器只锚定不升级**（升级由 DY 周报裁决）；未审查主张不得影响代码决策。
- **落点**：`index/registry/claims.yaml`（clm-XXXX）· `tools/capture_claims.py`（须在 `spherical_wave_mcp/.venv` 跑）· `docs/literature_harness/metadata_schema.md` · 周报模板 `weekly_review_packet_template.md`。
- **教训：自锚定失真**——capture_claims 必须排除 `ideation` provenance chunk 与自身来源，否则 own-note 字面命中会自我背书。
- 通用化技能：`~/.workbuddy/skills/claim-lifecycle`（跨工作区可用）。

## 五、方法学要点

**Dyson 轨道获取方法**（权威文件 `outputs/Dyson轨道获取方法_分类与排序_2026-09-11.md`；10 篇代表文献已入库 `papers/Dyson_orbital/`，归 `by_topic.md` **T12**，分档见 `by_relevance.md`）
- 四大家族：A 传播子/Green 函数 · B 耦合簇 · C 多参考 · D 时域/多体新族。
- **双维排序不可混用**：IP/谱函数（束缚态侧）头部 = MCDE > Dyson-ADC(3) > EOM-CC；光电离截面（连续态侧）头部 = Tiresia(B-spline) > ePolyScat > UKRmol+。**两轴几乎正交**。
- **【引用陷阱】MCDE 的多通道收益在束缚态侧，不在连续态侧** → 不能解决本项目 J.3.5 连续态瓶颈。MCDE 全出 Toulouse 单学派，无公开代码。
- `nD-ADC(3)` ≠ `Dyson-ADC(3)`（差 ~0.1 eV）；引用 ADC(3) 精度须注明分支（基准见 Keizer 2026）。
- 硬反证：瞬时自然轨道**不能**替代 Dyson 轨道（PRL 136, 013204 (2026)，H⁻ 通道分辨 PMD 出假峰）。
- 相对论 EOM-CC 已成型（三体修正 MAE 0.01–0.08 eV），旧综述"相对论不充分"已部分过时。
- ML/神经网络 Dyson 轨道仍空白。
- 与本项目直接相关：**Schio 2026, JCP 164, 204301（DOI 10.1063/5.0333577）** + arXiv:2602.23223 —— 手性分子 Cooper 极小 β 振荡，HF/DFT 无法解释，仅 EOM-CCSD Dyson 轨道（同对称性单空穴组态混合）可重现；附左右 Dyson 轨道与谱强度 γ^L·γ^R 完整公式。
- **复核方法论**：先看旧综述自述检索截止日期；**原文自己的"盲区清单"是最高效复核索引**；追加 YAML 后必跑校验器。

**表示层标定**（Fang 2026, JCP 164, 044309；笔记 `notes/R_matrix_Fang2026_CO_OTMO_阅读笔记.md`）
- 范式：把参考态/基组表示中的人为权重升为以外部可观测量为目标函数的待优化参数；两阶段 = 离散枚举 → 坐标下降。
- 前提硬约束：**靶侧是精度瓶颈**。本项目 J.3.5 诊断指向连续态侧，照搬前须做瓶颈归因实验 A/B。
- 须规避：①代理优化当成真优化；②用自身计算结果反调参考态（即"自锚定失真"）。
- 引用禁忌：该文 "ANN/backprop" 是修辞、AIP Scilight "machine learning" 属媒体包装，不可作方法学依据。

## 六、工具与环境

- **PDF 精读**：专用 venv `~/.workbuddy/binaries/python/envs/pdf`（pypdf）。`.../envs/pdf/Scripts/python.exe`。`Read` 直读 `.pdf` 会报 binary，须先转 txt；提取产物放 `outputs/<Author><Year>_<slug>_fulltext.txt`。
- **文献下载通道**：`arxiv.org` / `export.arxiv.org` 直连被沙箱阻断（curl `http=000`）。可用路径 = **scansci_pdf MCP**（`smart_download` / `batch_download`，identifier 传 arXiv ID 或 DOI）；MCP 掉线时降级 CLI：`C:\Users\Administrator.DESKTOP7RU274I\.workbuddy\binaries\python\envs\scansci2\Scripts\scansci-pdf.exe get <id> --output <dir>`。
- **APS 已改用随机式 DOI 后缀**（`10.1103/jcfy-vdm8`、`10.1103/dcdw-ly16`），不含期刊/卷信息 → 不可凭 DOI 形态判断真伪，必须 Crossref 复核。
- **常用节奏**：周度周一 11:00 索引重建自动化 + review packet 人工审查；MCP connector 改动需重启生效。
