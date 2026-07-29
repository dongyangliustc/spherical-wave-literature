# Literature Review Packet: 2026-07-29

## Summary

- Week: 2026-07-29
- Automation run IDs: manual/local generation
- New candidates: 0
- Recommended upgrades: 0
- Recommended rejects: 0
- Items needing human review: 0

## Recommended Upgrades

| ID | Source | Proposed State | Reason | Human Action |
|----|--------|----------------|--------|--------------|
|  |  |  |  |  |

## Recommended Rejects

| ID | Source | Reject Reason | Evidence |
|----|--------|---------------|----------|
|  |  |  |  |

## Needs Human Review

| ID | Question | Options | Suggested Decision |
|----|----------|---------|--------------------|
|  |  |  |  |

## Benchmark Updates

| Benchmark ID | System | Observable | Status Change | Code Impact |
|--------------|--------|------------|---------------|-------------|
| bench-cacelli-1993-h2-total-cross-section | H2 | total_cross_section | candidate | Phase G |
| bench-cacelli-1998-n2-beta | N2 | beta_parameter | candidate | Phase H |
| bench-cacelli-2000-c2h2-differential | C2H2 | differential_cross_section | candidate | Phase H |

## Risk Updates

| Risk ID | Claim | Evidence | Project Impact |
|---------|-------|----------|----------------|
| risk-fock-exchange-nonlocal-momentum-space | Nonlocal Fock exchange cannot be represented as a simple local V(|p-q|) kernel. | Phase G decision guide notes mismatch between J-K specification and local KS-potential implementation. | Separable potential and Schwinger layers must distinguish DFT-local and HF-exchange tiers. |
| risk-stieltjes-beta-limitation | L2 Stieltjes-Tchebycheff reconstruction does not directly provide beta parameters or resolved angular distributions. | Existing beginner and comparison notes identify lack of asymptotic angular information as a key limitation. | Benchmark strategy must not rely on Stieltjes-style total cross sections alone for angular modules. |
| risk-ch2o-no-direct-cacelli-benchmark | CH2O lacks a directly matched Cacelli benchmark in the current library. | Phase G decision guide recommends H2 -> N2 -> C2H2 before CH2O. | CH2O should not be used as a hard Gate until an external reference or ePolyScat comparison is available. |

## SW Code Context Candidates

| Claim | Source ID | Target Phase | Target Module |
|-------|-----------|--------------|---------------|
|  |  |  |  |
