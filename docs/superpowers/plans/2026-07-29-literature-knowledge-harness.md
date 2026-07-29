# Literature Knowledge Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a governed, extensible harness for continuously expanding the spherical-wave literature knowledge base without polluting core indexes.

**Architecture:** Start with documentation, schemas, and review gates before any networked automation. Later phases add registries, validators, discovery jobs, extraction jobs, and code-context injection.

**Tech Stack:** Markdown governance files, YAML-style registry records, Python validation scripts in later phases, Codex heartbeat automation after validation exists.

## Global Constraints

- Do not download copyrighted full text automatically from non-authorized sources.
- Do not promote candidates into core indexes without metadata verification and deduplication.
- Do not mark confidence as high unless full text or benchmark data has been reviewed.
- Preserve existing `papers/`, `notes/`, and `index/` semantics.
- Keep SW code-context injection concise and phase-specific.

---

## File Structure

- `docs/superpowers/specs/2026-07-29-literature-knowledge-harness-design.md`: design spec.
- `docs/literature_harness/README.md`: overview of the nine harnesses and operating order.
- `docs/literature_harness/metadata_schema.md`: registry fields and allowed values.
- `docs/literature_harness/state_machine.md`: candidate states and transitions.
- `docs/literature_harness/scoring_rubric.md`: quality scoring rules.
- `docs/literature_harness/benchmark_schema.md`: benchmark evidence schema.
- `docs/literature_harness/weekly_review_packet_template.md`: human review packet template.
- `docs/literature_harness/code_context_injection.md`: format for SW code-context injection.

### Task 1: Governance Documentation Foundation

**Files:**
- Create: `docs/literature_harness/README.md`
- Create: `docs/literature_harness/metadata_schema.md`
- Create: `docs/literature_harness/state_machine.md`
- Create: `docs/literature_harness/scoring_rubric.md`
- Create: `docs/literature_harness/benchmark_schema.md`
- Create: `docs/literature_harness/weekly_review_packet_template.md`
- Create: `docs/literature_harness/code_context_injection.md`

**Interfaces:**
- Consumes: current project layout and existing `index/README.md`.
- Produces: stable written rules for future registry and automation tasks.

- [ ] Step 1: Add the overview document.
- [ ] Step 2: Add metadata schema with controlled field values.
- [ ] Step 3: Add state machine document with promotion and failure states.
- [ ] Step 4: Add scoring rubric for relevance, role, confidence, and actionability.
- [ ] Step 5: Add benchmark schema.
- [ ] Step 6: Add weekly review template.
- [ ] Step 7: Add code-context injection format.
- [ ] Step 8: Verify files are present with `rg --files docs/literature_harness`.

### Task 2: Registry Skeleton

**Files:**
- Create: `index/registry/README.md`
- Create: `index/registry/candidates.yaml`
- Create: `index/registry/core.yaml`
- Create: `index/registry/benchmarks.yaml`
- Create: `index/registry/risks.yaml`

**Interfaces:**
- Consumes: schemas from Task 1.
- Produces: empty, reviewable registries for later automation.

- [ ] Step 1: Create registry README describing ownership and edit rules.
- [ ] Step 2: Create empty candidate registry with one commented example.
- [ ] Step 3: Create empty core registry with one commented example.
- [ ] Step 4: Create empty benchmark registry with one commented example.
- [ ] Step 5: Create empty risk registry with one commented example.
- [ ] Step 6: Verify no existing core index is modified.

### Task 3: Registry Validator

**Files:**
- Create: `tools/validate_registry.py`
- Create: `tests/test_validate_registry.py`

**Interfaces:**
- Consumes: registry YAML files from Task 2.
- Produces: command `python tools/validate_registry.py` that validates required fields, enum values, duplicate IDs, and DOI/arXiv/ISBN uniqueness.

- [ ] Step 1: Write tests for missing required fields, invalid enum values, duplicate IDs, and accepted empty registries.
- [ ] Step 2: Run tests and confirm they fail because validator does not exist.
- [ ] Step 3: Implement minimal YAML loading and validation.
- [ ] Step 4: Run tests and confirm they pass.
- [ ] Step 5: Run validator on the repository registries.

### Task 4: First Seed Registry Import

**Files:**
- Modify: `index/registry/core.yaml`
- Modify: `index/registry/benchmarks.yaml`
- Modify: `index/registry/risks.yaml`

**Interfaces:**
- Consumes: existing `index/README.md`, `index/by_topic.md`, and Phase G decision guide.
- Produces: initial reviewed registry entries for the current core literature.

- [ ] Step 1: Import Cacelli 1993, Cacelli 1998, Cacelli 2000, Domcke 1983, Wilhelmy 1994, Decleva 2022, Toffoli 2023, Lucchese-related benchmark placeholders.
- [ ] Step 2: Add benchmark records for H2, N2, and C2H2 where the existing index indicates a published reference.
- [ ] Step 3: Add risk records for Fock exchange nonlocality, GTO continuum limitations, and Stieltjes beta-parameter limitations.
- [ ] Step 4: Run the validator.

### Task 5: Weekly Automation Prompt

**Files:**
- Create: `docs/literature_harness/automation_prompt.md`

**Interfaces:**
- Consumes: all governance docs and registries.
- Produces: a safe prompt for a future Codex heartbeat automation.

- [ ] Step 1: Write a prompt that searches for candidate literature but only updates candidate registry and review packet.
- [ ] Step 2: Explicitly forbid direct promotion to core indexes.
- [ ] Step 3: Include failure logging rules.
- [ ] Step 4: Review the prompt against safety constraints.

### Task 6: Heartbeat Automation Creation

**Files:**
- No repository file edits required unless Codex records automation metadata.

**Interfaces:**
- Consumes: `docs/literature_harness/automation_prompt.md`.
- Produces: a paused or active Codex heartbeat automation, depending on user approval.

- [ ] Step 1: Ask the user whether the automation should start paused or active.
- [ ] Step 2: Create the heartbeat automation using Codex automation tools.
- [ ] Step 3: Confirm schedule, prompt scope, and notification policy.

## Self-Review

- Spec coverage: all nine harnesses are represented by Task 1 documents, with later tasks for registries, validation, import, automation prompt, and heartbeat creation.
- Placeholder scan: this plan intentionally names later tasks but does not include code blocks for Task 3 because Task 3 is not being executed in this first pass.
- Scope check: discovery automation is deferred until governance, registries, and validation exist.
