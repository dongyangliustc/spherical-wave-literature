# Spec I.1/I.2 Literature Download and Classification Plan

Scope: `D:\WORK\Coulomb\Spherical Wave\SPHERICAL_WAVE_SPEC.md` sections 1.1 and 1.2.

## Local Downloads Completed

| Journal / Source | Article | Identifier | Local directory | Local file | Notes |
|---|---|---|---|---|---|
| arXiv | Free-particle Green's function matrix elements over spherical Gaussian and plane-wave-modulated Gaussian basis functions | arXiv:2605.18564 | `papers/spherical_wave` | `Mahato_Skomorowski_2026_free_particle_Green_SGTO_arXiv.pdf` | Directly supports the SW free-particle Green-function core, momentum-space normalization, and recurrence design. |
| The Journal of Physical Chemistry Letters | Photoelectron Wave Function in Photoionization: Plane Wave or Coulomb Wave? | DOI:10.1021/acs.jpclett.5b01891 | `papers/general_review` | `Gozem_2015_photoelectron_wavefunction_JPCL.pdf` | Already present locally; useful for the `PlaneWave` baseline, continuum normalization, and PW vs Coulomb-wave risk framing. |

## Human Download Table

These items were metadata-verified from legitimate scholarly pages, but I did not auto-download publisher PDFs because the current run could not prove institution-authorized access for unattended download. Please download through USTC WebVPN/library or publisher pages, then place them in the target directories below.

| Journal | Article / DOI | Should go under | Suggested filename | Why it matters for Spec 1.1/1.2 |
|---|---|---|---|---|
| Physical Review A | Multicenter continuum-state approach to molecular-frame photoelectron angular distributions: From plane-wave to twisted photons. DOI:10.1103/PhysRevA.109.063114 | `papers/spherical_wave` | `Duan_2024_multicenter_continuum_MFPAD_PRA.pdf` | Modern multicenter continuum-state comparison for `continuum_wave.py`, `frame_transform.py`, and angular integration. |
| The Journal of Chemical Physics | Efficient recursive computation of molecular integrals over Cartesian Gaussian functions. DOI:10.1063/1.450106 | `papers/GTO_continuum` | `Obara_Saika_1986_recursive_Cartesian_Gaussian_integrals_JCP.pdf` | Foundation for `GTO_integral.py` and recurrence patterns that should inform `momentum_gto.py`. |
| The Journal of Chemical Physics | General recurrence formulas for molecular integrals over Cartesian Gaussian functions. DOI:10.1063/1.455717 | `papers/GTO_continuum` | `Obara_Saika_1988_general_recurrence_Cartesian_Gaussian_JCP.pdf` | Extends recurrence formulas, including Fourier-transform kernels relevant to momentum-space GTO handling. |
| Journal of Computational Physics | One- and two-electron integrals over cartesian gaussian functions. DOI:10.1016/0021-9991(78)90092-X | `papers/GTO_continuum` | `McMurchie_Davidson_1978_cartesian_gaussian_integrals_JCP.pdf` | Alternate foundational Gaussian integral formalism for validating implementation choices in the existing GTO layer. |
| Journal of Computational Chemistry | Calculation of photoionization differential cross sections using complex Gauss-type orbitals. DOI:10.1002/jcc.24848 | `papers/GTO_continuum` | `Matsuzaki_Yabushita_2017_cGTO_photoionization_JCC.pdf` | Directly compares cGTO continuum representations against photoionization differential observables. |
| Journal of Computational Chemistry | A complex Gaussian approach to molecular photoionization. DOI:10.1002/jcc.26760 | `papers/GTO_continuum` | `Ammar_2021_complex_Gaussian_photoionization_JCC.pdf` | Useful comparator for the existing `pw_cgto_hybrid` production model and length/velocity gauge behavior. |
| Journal of Physics B | Performance of polynomial Gaussian functions in describing the molecular electronic continuum. DOI:10.1088/0953-4075/30/24/006 | `papers/GTO_continuum` | `Cacelli_1997_polynomial_Gaussian_continuum_JPB.pdf` | Important risk/comparison source for how far GTO/L2 continuum descriptions can be trusted. |
| Physical Review A | Pade-approximant corrections to general variational expressions of scattering theory: Application to photoionization of carbon monoxide. DOI:10.1103/PhysRevA.28.1382 | `papers/Schwinger_L2` | `Lucchese_McKoy_1983_Pade_CO_photoionization_PRA.pdf` | Existing candidate had an incorrect PDF pointer; still needs legitimate full text for Schwinger/Pade comparison. |
| The Journal of Chemical Physics | Calculation of low-energy elastic cross sections for electron-CF4 scattering. DOI:10.1063/1.467237 | `papers/Schwinger_L2` | `Gianturco_Lucchese_Sanna_1994_CF4_scattering_JCP.pdf` | Existing candidate remains blocked by publisher verification; useful for ePolyScat/static-exchange comparison. |

## Registry Updates

- Added 9 Spec I.1/I.2-focused candidates to `index/registry/candidates.yaml`.
- Corrected `lit-lucchese-mckoy-1983-pade-co-photoionization`, which incorrectly pointed to the 1999 SF6 PDF.
- No entries were promoted to `index/registry/core.yaml`.
- No benchmark or risk registry entries were changed in this pass.

