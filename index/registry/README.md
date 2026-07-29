# Literature Registry

This directory is the controlled registry layer for the literature knowledge base.

The registry is deliberately separate from the human-readable indexes in `index/README.md`, `index/by_topic.md`, and `index/by_relevance.md`.

## Files

- `candidates.yaml`: discovered or screened sources that are not yet core knowledge.
- `core.yaml`: reviewed sources allowed to influence main indexes and project decisions.
- `benchmarks.yaml`: benchmark evidence mapped to systems, observables, and code phases.
- `risks.yaml`: method limitations, counterevidence, and implementation risks.

## Editing Rules

1. New automated discoveries go to `candidates.yaml`.
2. Core indexes should not be updated from candidate records alone.
3. Benchmark records must reference a literature item.
4. Risk records should include evidence and project impact.
5. Duplicate records should be resolved by DOI, arXiv ID, ISBN, or normalized title.

See `docs/literature_harness/` for schemas and promotion rules.
