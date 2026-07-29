# Benchmark Schema

Benchmark records track sources that can validate code.

## Required Fields

```yaml
id: "bench-cacelli-1993-h2-total-cross-section"
literature_id: "lit-cacelli-1993-h2-gto-continuum"
system: "H2"
observable: "total_cross_section"
energy_range: "photoelectron or photon energy range as reported"
data_availability: "figure_digitizable"
source_location: "figure 2"
target_phase: "Phase G"
target_modules: ["sw_matrix_element", "tau_matrix", "schwinger_amplitude"]
acceptance_threshold: "relative error < 15% after comparable setup"
status: "candidate"
notes: "Use only after digitization and unit reconciliation."
```

## Controlled Values

### `observable`

- `total_cross_section`
- `differential_cross_section`
- `beta_parameter`
- `phase_shift`
- `partial_wave_cross_section`
- `MFPAD`
- `time_delay`
- `matrix_element`

### `data_availability`

- `table`
- `figure_digitizable`
- `raw_data`
- `text_only`
- `not_available`

### `status`

- `candidate`
- `digitized`
- `unit_checked`
- `ready_for_gate`
- `used_in_gate`
- `rejected`

## Benchmark Priority

For the current project, prioritize:

1. H and He sanity checks.
2. H2 published total cross sections.
3. N2 differential cross sections and beta parameters.
4. C2H2 total and differential cross sections.
5. CH2O only after an external reference is identified.
