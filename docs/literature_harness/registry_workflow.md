# Registry Workflow

This workflow is the normal operating procedure for manual or automated literature expansion.

## Manual Candidate Addition

1. Add a record to `index/registry/candidates.yaml`.
2. Set `state: discovered`.
3. Set `confidence: metadata_only` unless an abstract or full text has actually been reviewed.
4. Run `python tools\validate_registry.py`.
5. Generate or update a review packet with `python tools\generate_review_packet.py --date YYYY-MM-DD`.

## Candidate Promotion

Promotion from `candidates.yaml` to `core.yaml` requires:

1. Metadata verification.
2. Deduplication check.
3. A structured extraction note or a clear existing project note.
4. `review_status: reviewed`.
5. Human approval from a review packet.

## Benchmark Addition

Add a benchmark record when a source gives a system, observable, and source location. Use `status: candidate` until figure digitization or table extraction is complete.

## Risk Addition

Add a risk record whenever a source shows a limitation, contradiction, failure mode, or implementation hazard. Risks do not need to be negative toward the project; they need to prevent overclaiming.

## Weekly Review

The weekly packet is the only place automation should ask for human decisions. Keep questions narrow and actionable.
