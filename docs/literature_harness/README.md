# Literature Harness Overview

This directory defines the operating rules for expanding the spherical-wave literature knowledge base.

The harness exists to prevent three common failures:

1. Collecting papers without knowing why they matter.
2. Summarizing sources before metadata and duplicates are controlled.
3. Feeding unreviewed claims into SW code decisions.

## Operating Order

Use the harnesses in this order:

1. Source Discovery
2. Metadata and Dedup
3. Candidate State Machine
4. Quality Scoring
5. Extraction
6. Benchmark Tracking
7. Risk and Counterevidence
8. Human Review
9. Code-Context Injection

## Rule of Thumb

A source can be discovered automatically, but it should not influence core indexes, benchmark gates, or SW code context until it has passed metadata verification, deduplication, and review.

## First Implementation Boundary

The first implementation phase creates rules and schemas only. It does not run internet discovery, download files, or modify the existing core literature index.
