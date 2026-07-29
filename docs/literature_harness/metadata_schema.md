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

## Promotion Rule

An item cannot move to `indexed` unless:

1. `id`, `title`, `authors`, `year`, `source_type`, `state`, and `review_status` are present.
2. At least one identifier or local path is present.
3. Deduplication has been checked.
4. `relevance`, `role`, `confidence`, and `actionability` are assigned.
