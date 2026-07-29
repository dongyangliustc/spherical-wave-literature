# Scoring Rubric

The scoring rubric keeps expansion disciplined.

## Relevance

- `core`: Directly supports current project formulas, implementation choices, or benchmark gates.
- `high`: Important to method selection or likely future implementation.
- `medium`: Useful for background, comparison, or teaching.
- `low`: Contextual only.

## Role

Use one or more:

- `foundation`: Basic theory, textbook, or mathematical reference.
- `method_origin`: Original method paper.
- `method_comparison`: Compares multiple routes.
- `benchmark`: Contains numerical or figure data for validation.
- `code_reference`: Describes software architecture or reproducible implementation.
- `review`: Representative review article.
- `frontier`: Recent paper likely to shift direction.
- `risk_evidence`: Shows limitations, failure modes, or counterarguments.
- `historical_context`: Explains lineage but does not drive implementation.

## Confidence

- `metadata_only`: Only bibliographic record is known.
- `abstract_only`: Abstract or summary has been read.
- `fulltext_available`: Full text exists but has not been extracted.
- `fulltext_extracted`: Structured extraction exists.
- `fulltext_or_primary_index`: Full text or project-maintained primary index supports the claim.
- `benchmark_verified`: Data was checked against a figure, table, or extracted benchmark.

## Actionability

- `none`: Keep only as context.
- `reading_candidate`: Worth reading later.
- `formula_reference`: Provides equations or notation.
- `implementation_guidance`: Affects code architecture or algorithms.
- `direct_benchmark`: Can validate code outputs.
- `risk_update`: Updates risk matrix.
- `code_context_candidate`: Candidate for SW phase context.

## Hard Rule

Do not assign `confidence: benchmark_verified` unless the benchmark data source and observable are recorded in the benchmark registry.
