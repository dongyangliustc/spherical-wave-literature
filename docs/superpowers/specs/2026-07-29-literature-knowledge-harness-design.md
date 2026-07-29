# Literature Knowledge Harness Design

> Date: 2026-07-29
> Scope: `spherical_wave_literature` as a governed literature and knowledge base for spherical-wave photoionization work.

## Purpose

This harness turns the repository from a collection of PDFs and notes into a controlled literature knowledge system. Its main job is to continuously expand the library while preserving trust, traceability, and usefulness for the associated SW code project.

## Design Principles

1. Discovery is not ingestion. A found item enters a candidate workflow before it can affect core indexes.
2. Every accepted item must explain its role in the project.
3. Metadata and deduplication come before summarization.
4. Benchmark evidence receives special handling because it can validate code.
5. Negative evidence and method limitations are first-class knowledge.
6. Weekly review packets must keep human review short and focused.
7. Code-context injection must be concise, cited, and phase-specific.

## Harnesses

### 1. Source Discovery Harness

Find candidate books, review articles, and recent papers through controlled source channels:

- Seed papers already stored in `papers/`
- DOI and arXiv metadata
- Author networks
- Citation trails from core papers
- Journal and proceedings monitoring
- Book and chapter references for foundational theory

Discovery output is a candidate record, not a core note.

### 2. Metadata and Dedup Harness

Each item gets a stable ID and normalized metadata before extraction. Deduplication priority:

1. DOI
2. arXiv ID
3. ISBN
4. Normalized title hash
5. Author-year-title fuzzy match

Conflicts are recorded instead of silently resolved.

### 3. Candidate State Machine Harness

Items move through explicit states:

`discovered -> metadata_verified -> abstract_screened -> fulltext_available -> extracted -> reviewed -> indexed -> injected_to_code_context`

Failure states include:

`duplicate`, `out_of_scope`, `paywalled`, `metadata_conflict`, `low_quality`, `needs_human_review`

### 4. Quality Scoring Harness

Every item carries the following controlled fields:

- `relevance`
- `role`
- `confidence`
- `actionability`
- `review_status`

High-confidence claims require either full-text extraction or explicit benchmark evidence.

### 5. Extraction Harness

Every extracted item should produce a structured note covering:

- Problem solved
- Core equations and symbols
- Assumptions and boundary conditions
- Numerical parameters
- Benchmark data
- Project module mapping
- Risks, limitations, and unresolved questions

### 6. Benchmark Harness

Benchmark-bearing sources are tracked separately by system, observable, data availability, and target code module. This harness supports Phase G/H validation, especially for H, He, H2, N2, C2H2, and later CH2O.

### 7. Risk and Counterevidence Harness

Limitations, failed assumptions, and competing-method critiques are captured as `risk_evidence`. These records update technical risk matrices instead of disappearing into prose summaries.

### 8. Human Review Harness

The automation should produce a weekly review packet with:

- New candidates
- Recommended upgrades
- Recommended rejects
- Items needing human judgment
- Highest-impact conclusions for SW code work

### 9. Code-Context Injection Harness

Only reviewed, phase-relevant conclusions are injected into SW code context files. Injection files must be short, cited, and mapped to code modules or tests.

## Repository Layout

The harness adds governance documents under `docs/literature_harness/` and implementation plans under `docs/superpowers/`.

Candidate and registry data should later live under `index/registry/`, but the first phase only defines schemas and review rules.

## Acceptance Criteria

- The harness defines explicit metadata fields and allowed values.
- The candidate state machine is documented.
- Benchmark evidence has its own schema.
- Weekly review packets have a stable template.
- Code-context injection has a stable, concise format.
- No automated discovery is enabled before the registry and validation rules exist.
