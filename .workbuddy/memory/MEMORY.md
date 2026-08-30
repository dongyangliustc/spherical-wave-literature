# 项目长期记忆（spherical_wave_literature）

> 本文件沉淀跨会话的项目级约定。日常日志见 `YYYY-MM-DD.md`。

## 知识库"同流不同信"体系（v0.1，2026-08-26 实施）

自产知识（对话/笔记）与文献知识**同流**进同一 ingest→索引→检索管道，但**不同信**：靠双轴打标 + 检索层 epistemic gate 区分可信度。

### 双轴打标（绝不合并为一个标签）
- **维度 A 来源属性 provenance**：`literature`(T0 外部发表) / `own_publication`(T0* 自有已发表) / `synth_summary`(T1 可追溯派生) / `ideation`(T2 自产猜想)。
- **维度 B 核实状态 epistemic_status**：`unverified < consistent < literature_supported < benchmark_verified`；负向 `conflicting / refuted / superseded / stale`。
- **claim_kind 分轨**：`fact`(强制文献锚定) / `derivation`(可复现即可) / `hypothesis`(永不注入) / `workflow`(仅人类使用)。

### 硬规则
- **注入代码上下文门槛：epistemic rank ≥ 2（literature_supported）**，仅 `literature/own_publication` provenance 可入选。
- **核实粒度：主张级为主 + chunk 继承 fail-closed**（chunk 继承所含主张最差值）。
- **门控在检索层**（`min_epistemic_status`），不在入库层；入库不设限、出库严把关。
- **机器只锚定不升级**：capture_claims 保守三级（T0/T0* 命中 score≥100→literature_supported；非 ideation 弱锚→consistent；无锚→unverified）；升级一律由 DY 在周报人工裁决。
- **黄金法则不改**：未审查主张不得影响代码决策。

### 关键落点
- 主张 registry：`index/registry/claims.yaml`（clm-XXXX，与 core/benchmark/risk 平行）。
- 抽取/锚定工具：`tools/capture_claims.py`（须在 `spherical_wave_mcp/.venv` 跑，依赖 editable install）。
- 打标规范：`docs/literature_harness/metadata_schema.md`（Source-of-Truth v0.1 节）+ `spherical_wave_mcp/config/sources.yaml`（provenance 字段，`source_type: own_note` 默认 ideation/unverified/hypothesis）。
- 周报：`docs/literature_harness/weekly_review_packet_template.md`「主张核实周报」节。
- 设计/试点记录：`docs/literature_harness/自产知识同流与核实迭代_草案v0.md`（现为 v0.1 + 决策已裁决）、`自产知识同流_试点报告_v0.1.md`。

### 案例与教训
- 试点 2026-08-26：2066 chunks，14 条捕获主张，clm-0013 人工升级为 literature_supported；见试点报告。
- **教训：自锚定失真**——capture_claims 必须排除 `ideation` provenance chunk 与自身来源，否则 own-note 字面命中会自我背书。
- **遗留债务**：12 条 consistent 待周报复核；clm-0001（GTO-FT+Lucchese 融合正确性）hypothesis 进验证队列。

## 常用任务节奏
- 周度：周一 11:00 索引重建自动化 + review packet 人工审查。
- 对话环境：MCP connector 改动后需重启才生效。

## 通用方法论 skill：claim-lifecycle（2026-08-27 沉淀）
- 把"同流不同信"体系从项目级泛化为**用户级通用技能**：`~/.workbuddy/skills/claim-lifecycle`（任意工作区可用）。
- 定位：主张生命周期知识管理（采集→打标→锚定→人工核实→多形态产出），面向任何知识库，不依赖本 MCP 组件。
- 核心工具：`scripts/extract_claims.py`（对话/笔记→主张卡）、`anchor_claims.py`（保守三级锚定，`--index` MCP 或 `--corpus` 免依赖双后端）、`report_generator.py`（**多形态产出**：inspect 库检定期报告 / weekly 核实周报 / tickets 验证工单 / audit 追溯审计 / inject 三类注入包 code_context|teaching_material|design_constraint）、`validate_registry.py`（CI 可用校验）。
- 方法论指引：`references/`（metadata_schema / lifecycle 状态机 / delivery_modes 产出矩阵 / pitfalls 工程陷阱）。
- 硬约束与项目版一致：机器只锚定不升级、hypothesis 永不注入、门控 rank≥2 且 provenance∈{literature,own_publication}、产出先过门再格式化。
- 打包：`claim-lifecycle.zip`（skill-creator 校验通过）。
