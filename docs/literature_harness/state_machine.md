# Candidate State Machine

The state machine controls how a source moves from discovery to project influence.

## Main Path

```text
discovered
  -> metadata_verified
  -> abstract_screened
  -> fulltext_available
  -> extracted
  -> reviewed
  -> indexed
  -> injected_to_code_context
```

## State Definitions

- `discovered`: A potentially relevant source was found.
- `metadata_verified`: Title, authors, year, and identifier were checked.
- `abstract_screened`: Abstract or table of contents was screened for relevance.
- `fulltext_available`: A legitimate local PDF, open-access copy, book chapter, or library-access reference is available.
- `extracted`: A structured note or extraction record exists.
- `reviewed`: A human or trusted review pass accepted the extraction.
- `indexed`: The item is allowed in core index or registry.
- `injected_to_code_context`: A concise, cited conclusion was added to a phase-specific SW context file.

## Failure and Holding States

- `duplicate`: Same DOI, arXiv ID, ISBN, or normalized title already exists.
- `out_of_scope`: Not relevant to spherical waves, continuum states, photoionization, scattering, or supporting math.
- `paywalled`: Metadata is useful, but full text cannot be accessed legitimately.
- `metadata_conflict`: Identifier, title, authors, or year disagree across sources.
- `low_quality`: Source appears unreliable or too weak for the knowledge base.
- `needs_human_review`: Automation cannot decide safely.

## Promotion Constraints

- `discovered` items can only enter candidate registries.
- `abstract_screened` items cannot update method conclusions.
- `fulltext_available` items still cannot update core indexes until extraction exists.
- `injected_to_code_context` requires `reviewed` plus explicit module mapping.
