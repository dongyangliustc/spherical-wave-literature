# Code-Context Injection Format

Code-context files summarize reviewed literature conclusions for the SW code project.

## File Location

Use:

```text
outputs/sw_context/literature_context_<phase>.md
```

Example:

```text
outputs/sw_context/literature_context_phase_g.md
```

## Length Constraint

Each file should stay under roughly 2-3 pages. It is a decision aid, not a literature review.

## Required Sections

```markdown
# Literature Context: Phase G

## Scope

One paragraph describing the code phase and included literature.

## Actionable Conclusions

| Claim | Source | Target Module | Confidence | Action |
|-------|--------|---------------|------------|--------|
| | | | | |

## Benchmark Candidates

| Benchmark | System | Observable | Readiness | Gate Use |
|-----------|--------|------------|-----------|----------|
| | | | | |

## Risk Evidence

| Risk | Source | Impact | Mitigation |
|------|--------|--------|------------|
| | | | |

## Exclusions

Short list of nearby topics intentionally not injected.
```

## Injection Rule

Only use records with:

- `review_status: reviewed`
- `actionability` equal to `implementation_guidance`, `direct_benchmark`, `risk_update`, or `code_context_candidate`
- explicit `project_modules`
