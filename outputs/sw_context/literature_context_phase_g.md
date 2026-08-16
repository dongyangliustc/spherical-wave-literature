# Literature Context: Phase G

> Generated: 2026-08-13
> Source: 文献到代码桥接_PhaseG技术决策指南.md + registry (core.yaml + candidates.yaml + benchmarks.yaml + risks.yaml)
> Format: per docs/literature_harness/code_context_injection.md
> Injection target: SW Master Agent Phase G prompt (G.1-G.12)

## Scope

Phase G implements momentum-space Born/Schwinger corrections for the spherical-wave photoionization cross-section code. The literature context spans two methodological lineages: the Cacelli-Moccia-Rizzo GTO-L2 real-space tradition (methodological parent) and the Lucchese-McKoy iterative Schwinger variational tradition (direct implementation reference for Tier 2). The core mathematical question is whether fusing these two traditions in momentum space is self-consistent.

## Actionable Conclusions

| Claim | Source | Target Module | Confidence | Action |
|-------|--------|---------------|------------|--------|
| LB94 XC potential asymptotic behavior (-1/r) is critical for cross-section accuracy; LDA insufficient | Cacelli 2000 (Chem. Phys. 254, 113); Stener 2005 (JCP) | momentum_potential | fulltext | G.11 benchmark: enable LB94 as Tier 2 default |
| HF vs DFT potential causes ~20% systematic difference in continuum states | Cacelli 1993 (JCP 98, 8742) | separable_potential | fulltext | Confirm V_eff type in code; document as Spec Amendment |
| Fock exchange is nonlocal in momentum space: K(p,q) != K(|p-q|); current code uses local KS potential | risk-fock-exchange-nonlocal-momentum-space | separable_potential | fulltext | Distinguish Tier 2a (DFT-local) vs Tier 2b (HF-exchange); defer Fock to Phase H |
| lmax=3 sufficient for photoionization due to dipole selection rules | Wilhelmy 1994 (JCP); Cacelli 1993 | angular_reduction | fulltext | Maintain lmax=3 |
| N2 p-type initial state requires additional angular coupling beyond current implementation | Cacelli 1998 (PRA 57, 1895) | angular_reduction | fulltext | Must implement before Phase H molecular tests |
| Born kernel addition theorem converges slowly for large |r1-r2| | Felderhof 1987 (J. Math. Phys.) | angular_reduction | fulltext | G.11: add multi-center convergence test |
| L2 Stieltjes-Tchebycheff reconstruction does not provide beta parameters or resolved angular distributions | risk-stieltjes-beta-limitation | benchmark_strategy | fulltext | Do not rely on Stieltjes total cross sections alone for angular modules |
| G0+(p,p';E) is diagonal in momentum representation; non-diagonal in GTO basis | Domcke 1983 (PRA 28, 2777) Eq. (2.28) | green_function_matrix | fulltext | Maintain full non-diagonal implementation |
| eta parameter determines resonance width; physically eta -> 0+ | Lucchese 1986 (Phys. Rep. 131, 147) | green_function_matrix | fulltext | G.11: test eta sensitivity |
| Padé approximation accelerates principal value integral convergence | Lucchese 1983 (PRA 28, 1382) | green_function_matrix | fulltext | Post-G.9: optional Padé acceleration |
| tau(E) = [1 - V*G0]^{-1} * V is the Schwinger variational form; solve is more stable than inv | Domcke 1983 Eq. (2.34b); Gonis & Butler 1999 | tau_matrix | fulltext | Maintain numpy.linalg.solve; record as Spec Amendment |
| [1-V*G0] may be near-singular near resonance energy | Gonis & Butler 1999 (Springer) App. F | tau_matrix | fulltext | Lower condition number threshold to 1e8; emit WARNING above |
| Schwinger amplitude must reproduce Lucchese & McKoy 1979 He cross-section within 20% | Lucchese & McKoy 1979 (PRA 21, 112) | schwinger_amplitude | fulltext | G.11 Gate: compare He peak position ±0.5 eV, height ±20% |
| Length and velocity gauge should agree within 5% for correct Schwinger implementation | Cacelli 1993 §IV; Lucchese 1986 | schwinger_amplitude | fulltext | G.10: implement both gauges; G.12 target: L/V < 3 for all systems |
| Born correction is not an "improvement" but a qualitative change from unphysical free particle to physical scattering | Cacelli 1993 vs Phase F free GF analysis | sw_matrix_element | fulltext | Born precision must match Cacelli L2 results, not just "better than nothing" |
| Single-center H/He Born=0 is a physical selection rule, not a bug | Cacelli 1993 (L2 method has V_eff built-in) | sw_matrix_element | fulltext | Verify Born contribution in G.11 multi-center benchmarks |
| Rank-N separable potential: if Q is spanned by first N eigenstates, H_PQ(E-H_QQ)^{-1}H_QP is exactly rank-N | Domcke 1983 §11 | separable_potential | fulltext | Basis size R=50-200 per Lucchese 1986 ePolyScat |
| ePolyScat uses ~50-200 basis functions; Cacelli H2 uses ~30 GTO | Lucchese 1986; Cacelli 1993 | separable_potential | fulltext | Maintain R=50-200 range |
| Spherical Gaussian type orbitals (SGTO) have recurrence relations for free-particle Green's function matrix elements | Mahato & Skomorowski 2026 (arXiv:2605.18564) | sw_matrix_element, momentum_gto | fulltext | Direct formula reference for SW integral implementation |
| Obara-Saika recurrence enables efficient Cartesian Gaussian molecular integral computation | Obara & Saika 1986 (JCP); Obara & Saika 1988 (JCP) | GTO_integral, momentum_gto | fulltext | Use for GTO Fourier transform kernel recursion |
| McMurchie-Davidson auxiliary function approach for Cartesian Gaussian integrals | McMurchie & Davidson 1978 (JCP) | GTO_integral, momentum_gto | fulltext | Alternative to Obara-Saika; compare numerical stability |
| Complex Gaussian (cGTO) approach provides differential cross sections with length/velocity gauge consistency | Matsuzaki & Yabushita 2017 (JCC); Ammar et al. 2021 (JCC) | continuum_wave, PW_integral | fulltext | Method comparison; risk evidence for gauge issues |
| CH2O lacks published Cacelli benchmark; should not be used as hard Gate until external reference available | risk-ch2o-no-direct-cacelli-benchmark | benchmark_strategy | fulltext | Follow H2->N2->C2H2 path per Cacelli 1993->1998->2000 |

## Benchmark Candidates

| Benchmark | System | Observable | Readiness | Gate Use |
|-----------|--------|------------|-----------|----------|
| Cacelli 1993 H2 total cross-section | H2 | total_cross_section | figure_digitizable | Phase G Gate: error < 15% |
| Cacelli 1998 N2 beta parameter | N2 | beta_parameter | figure_digitizable | Phase H: after H2 Gate passes |
| Cacelli 2000 C2H2 differential cross-section | C2H2 | differential_cross_section | figure_digitizable | Phase H: low-symmetry molecule test |
| Lucchese 1979 He photoionization | He | total_cross_section | figure_digitizable | Phase G Gate: peak ±0.5 eV, height ±20% |

## Risk Evidence

| Risk | Source | Impact | Mitigation |
|------|--------|--------|------------|
| Momentum-space GTO-FT + spherical-wave Born correction may be mathematically inconsistent | Phase G decision guide §1 | Critical: entire Phase G validity | Verify against Cacelli 1993/1998 known results |
| Schwinger amplitude numerically unstable near resonance | Lucchese 1986 | High: G.10 may fail near shape resonances | Condition number diagnostics + Padé fallback |
| Fock exchange missing causes systematic cross-section bias | risk-fock-exchange; Cacelli 1993 | Medium: ~20% systematic error | Document as Spec Amendment; Phase H addition |
| CH2O lacks literature benchmark | risk-ch2o-no-direct-cacelli-benchmark | Medium: no objective Gate standard | Use H2->N2->C2H2 path; defer CH2O to Phase H |
| First-order Born truncation may be insufficient for molecules | Phase G decision guide §2.8 | High: Born vs Schwinger >30% indicates convergence failure | Quantify Born-Schwinger difference on H2 |
| L2 Stieltjes method cannot provide angular distributions | risk-stieltjes-beta-limitation | Medium: benchmark strategy gap | Do not use Stieltjes total σ alone for angular modules |
| Plane wave vs Coulomb wave normalization affects cross-section magnitude | Gozem 2015 (JPCL) | Medium: absolute cross-section calibration | Verify continuum wave normalization convention |

## Exclusions

- Phase H correlation methods (EOM-CC, MR-Dyson, RCS-ADC) — not needed for Phase G single-reference treatment
- R-matrix (UKRmol+) — alternative method track, not Phase G reference
- B-spline technical implementation details (Tiresia code architecture) — Phase G uses GTO-FT, not B-spline
- Attosecond dynamics and time-resolved PES — different physics regime
- Astrophysical photoionization databases — different application domain

## Key Literature Paths (for MCP read_source_segment)

| Source ID | PDF Path | Note Path |
|-----------|----------|-----------|
| lit-cacelli-1993-h2-gto-continuum | papers/GTO_continuum/Cacelli_1993_H2_photoionization_JCP.pdf | notes/GTO_continuum.md |
| lit-cacelli-1998-n2-differential | papers/GTO_continuum/Cacelli_1998_N2_differential_PRA.pdf | notes/GTO_continuum.md |
| lit-cacelli-2000-c2h2-differential | papers/GTO_continuum/Cacelli_2000_C2H2_differential_CP.pdf | notes/GTO_continuum.md |
| lit-domcke-1983-projection-scattering | papers/spherical_wave/Domcke_1983_projection_scattering_PRA.pdf | notes/spherical_wave.md |
| lit-lucchese-mckoy-1979-schwinger-electron-scattering | papers/Schwinger_L2/Lucchese_McKoy_1979_Schwinger_eHe_JPB.pdf | — |
| lit-lucchese-takatsuka-mckoy-1986-schwinger-review | papers/Schwinger_L2/Lucchese_Takatsuka_McKoy_1986_Schwinger_review_PhysRep.pdf | — |
| lit-lucchese-mckoy-1983-pade-co-photoionization | papers/Schwinger_L2/Lucchese_McKoy_1983_Pade_CO_photoionization_PRA.pdf | — |
| lit-mahato-skomorowski-2026-free-particle-green-sgto | papers/spherical_wave/Mahato_Skomorowski_2026_free_particle_Green_SGTO_arXiv.pdf | — |
| lit-obara-saika-1986-recursive-cartesian-gaussian-integrals | papers/GTO_continuum/Obara_Saika_1986_recursive_Cartesian_Gaussian_integrals_JCP.pdf | — |
| lit-obara-saika-1988-general-recurrence-cartesian-gaussian | papers/GTO_continuum/Obara_Saika_1988_general_recurrence_Cartesian_Gaussian_JCP.pdf | — |
| lit-wilhelmy-1994-lobatto-photoionization | papers/spherical_wave/Wilhelmy_1994_Lobatto_photoionization_JCP.pdf | notes/spherical_wave.md |
| lit-felderhof-1987-addition-theorems | papers/spherical_wave/Felderhof_1987_addition_theorems_JMP.pdf | — |

## Verification Checklist (for SW Master Agent)

### G.10 Implementation
- [ ] tau=0 limit: D_if(Schwinger) = D_if(Born), relative error < 1e-12
- [ ] Length/velocity gauge cross-section difference < 5%
- [ ] Matrix condition number > 1e8 triggers WARNING
- [ ] All existing regression tests pass
- [ ] He single-center test: Born=0 (physical), Schwinger != Born?

### G.11 Benchmark
- [ ] H2 Schwinger cross-section vs Cacelli 1993 Fig. 2: error < 15%
- [ ] Quantify Born correction contribution to H2
- [ ] Born vs Schwinger difference < 30% (else Born convergence insufficient)
- [ ] L/V ratio statistics for all energy points
- [ ] He cross-section vs Lucchese 1979 Fig. 1: peak ±0.5 eV, height ±20%

### G.12 Gate
- [ ] All systems L/V < 3
- [ ] All Phase F regression tests pass
- [ ] V_alpha_beta Hermitian, condition number < 1e6
- [ ] G0+ Hermitian, Im G[0,0] = -pi * on-shell density
