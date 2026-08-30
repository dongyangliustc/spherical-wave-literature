# Literature Metadata Schema

Each literature item should have one registry record.

## Required Fields

```yaml
id: "lit-cacelli-1993-h2-gto-continuum"
title: "Gaussian type orbital basis sets for the calculation of continuum properties in molecules: The photoionization cross section of H2"
authors: ["Cacelli", "Moccia", "Rizzo"]
year: 1993
source_type: "paper"
identifiers:
  doi: "10.1063/1.464482"
  arxiv: null
  isbn: null
paths:
  pdf: "papers/GTO_continuum/Cacelli_1993_H2_photoionization_JCP.pdf"
  note: null
topic_tags: ["GTO", "L2", "photoionization", "H2"]
project_modules: ["momentum_gto", "sw_matrix_element", "benchmark_h2"]
state: "indexed"
review_status: "reviewed"
relevance: "core"
role: ["method_origin", "benchmark"]
confidence: "fulltext_or_primary_index"
actionability: "direct_benchmark"
```

## Controlled Values

### `source_type`

- `paper`
- `review`
- `book`
- `chapter`
- `dataset`
- `software`
- `thesis`

### `state`

- `discovered`
- `metadata_verified`
- `abstract_screened`
- `fulltext_available`
- `extracted`
- `reviewed`
- `indexed`
- `injected_to_code_context`
- `duplicate`
- `out_of_scope`
- `paywalled`
- `metadata_conflict`
- `low_quality`
- `needs_human_review`

### `review_status`

- `unreviewed`
- `machine_screened`
- `human_review_needed`
- `reviewed`
- `rejected`

### `relevance`

- `core`: directly supports current project theory, implementation, or benchmark gates.
- `high`: likely useful for project decisions but not immediately required.
- `medium`: useful background or adjacent method.
- `low`: retained only for context.

### `role`

- `foundation`
- `method_origin`
- `method_comparison`
- `benchmark`
- `code_reference`
- `review`
- `frontier`
- `risk_evidence`
- `historical_context`

### `confidence`

- `metadata_only`
- `abstract_only`
- `fulltext_available`
- `fulltext_extracted`
- `fulltext_or_primary_index`
- `benchmark_verified`

### `actionability`

- `none`
- `reading_candidate`
- `formula_reference`
- `implementation_guidance`
- `direct_benchmark`
- `risk_update`
- `code_context_candidate`

---

## Source-of-Truth Metadata（v0.1, 2026-08-26）

> 「同流不同信」双轴打标。`provenance`（谁说的）与 `epistemic_status`（验证过没有）
> 是两个正交维度。文献条目级可携带 `default_epistemic_status`；自产知识下沉到**主张级**，
> chunk 检索时按最小核实状态过滤。

### `provenance`（来源属性）

| Value | Tier | 先验可信度 | 说明 |
|-------|------|-----------|------|
| `literature` | T0 | 高 | 外部同行评审，可溯源 |
| `own_publication` | T0* | 高（提示自偏差） | 已发表但为自产（含自有论文） |
| `synth_summary` | T1 | 中高 | 基于文献的派生/综述，锚点=文献链 |
| `ideation` | T2 | 低 | 自产共识/猜想，暂无外部锚点 |

### `epistemic_status`（核实状态，主张/chunk 级）

| Value | Rank | 可注入代码上下文 |
|-------|------|------------------|
| `benchmark_verified` | 3 | ✅ |
| `literature_supported` | 2 | ✅ |
| `consistent` | 1 | ❌（单源一致，待加固） |
| `unverified` / `unsupported` | 0 | ❌ |
| `conflicting` | -1 | ❌（人工裁决） |
| `refuted` / `superseded` / `stale` | -2 | ❌ |

> 门控规则：只有 `benchmark_verified` / `literature_supported` 可进入
> `injected_to_code_context`。chunk 取其中所含主张的最差值（fail-closed）。

### `claim_kind`（主张分轨，决定"支撑义务"）

| Value | 是否强制文献锚定 | 可否注入代码上下文 |
|-------|------------------|--------------------|
| `fact` | 强制 | 可（须 literature_supported） |
| `derivation` | 推演可复现即可 | 可（须 benchmark_verified） |
| `hypothesis` | 否 | 永不 |
| `workflow` / `notation` | 否 | 否 |

### 新增字段（registry 条目可选携带）

- `provenance_tier`：T0/T0*/T1/T2（冗余便于排序）
- `evidence_chain`：支撑该主张的文献/基准 ID 列表
- `verify_granularity`：`document` / `chunk` / `claim`（默认 claim）
- `last_verified`：最近核实日期（ISO）
- `default_epistemic_status` / `default_claim_kind`：来源级默认值（`sources.yaml` 自动推断）

## Promotion Rule

An item cannot move to `indexed` unless:

1. `id`, `title`, `authors`, `year`, `source_type`, `state`, and `review_status` are present.
2. At least one identifier or local path is present.
3. Deduplication has been checked.
4. `relevance`, `role`, `confidence`, and `actionability` are assigned.
