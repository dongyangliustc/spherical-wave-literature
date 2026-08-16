# Literature Review Packet: 2026-08-07

## Summary

- Week: 2026-08-07
- Automation run IDs: manual/local generation
- New candidates: 19
- Recommended upgrades: 8
- Recommended rejects: 0
- Items needing human review: 8

## Recommended Upgrades

| ID | Source | Proposed State | Reason | Human Action |
|----|--------|----------------|--------|--------------|
| lit-lucchese-mckoy-1979-schwinger-electron-scattering | Application of the Schwinger variational principle to electron scattering | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-lucchese-takatsuka-mckoy-1986-schwinger-review | Applications of the Schwinger variational principle to electron-molecule collisions and molecular photoionization | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-lucchese-mckoy-1983-pade-co-photoionization | Pade-approximant corrections to general variational expressions of scattering theory: Application to photoionization of carbon monoxide | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-toffoli-coriani-stener-decleva-2024-tiresia-code | Tiresia: A code for molecular electronic continuum states and photoionization | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-masin-benda-gorfinkiel-2020-ukrmol-plus | UKRmol+: A suite for modelling electronic processes in molecules interacting with electrons, positrons and photons using the R-matrix method | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-tenorio-ponzi-coriani-decleva-2022-mr-dyson-b-spline | Photoionization Observables from Multi-Reference Dyson Orbitals Coupled to B-Spline DFT and TD-DFT Continuum | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-moitra-coriani-decleva-2021-correlation-photoionization | Capturing Correlation Effects on Photoionization Dynamics | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |
| lit-gozem-2015-plane-wave-coulomb-wave-photoionization | Photoelectron Wave Function in Photoionization: Plane Wave or Coulomb Wave? | reviewed/indexed | implementation_guidance | Approve promotion or keep as candidate |

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
