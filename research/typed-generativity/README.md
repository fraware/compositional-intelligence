# Typed Generativity — publication and methods

The current publication manuscript is [Typed Generativity V5](../../essays/typed-generativity.md). This edited version supersedes the earlier website edition. The original V3 DOCX fingerprint in the manuscript identifies the historical source, not the edited V5 content. The original 15 tables are preserved verbatim.

## Methodological companions

- [Full evaluation protocol](full-evaluation-protocol.md) — experimental design, identification, comparison conditions, missing evidence, and inference.
- [Domain acceptance handbook](domain-acceptance-handbook.md) — proposed criteria for code, Lean mathematics, explanations, scientific protocols, planning, and tool use.
- [V5 editorial audit](v5-editorial-audit.md) — source-preservation checks, editorial rationale, and explicitly unverified claims. This records the state of the manuscript before repository integration.

## Reproducible benchmark contract

The following source files are committed alongside the methods text.

- [Record schema](typed_generativity_benchmark_contract_v0.2.schema.json)
- [Structural validator](validate_typed_generativity_contract_v02.py)
- [Regression tests](test_typed_generativity_contract_v02.py)
- [Synthetic fixture](typed_generativity_synthetic_fixture_v0.2.json)
- [Runner-safe example](typed_generativity_runner_safe_v0.2.json)
- [Expected synthetic summary](typed_generativity_synthetic_summary_v0.2.json)

With Python 3.11 or later and `jsonschema>=4.18,<5` installed, run these commands from this directory.

```sh
python3 -m unittest -q test_typed_generativity_contract_v02.py
python3 validate_typed_generativity_contract_v02.py \
  typed_generativity_synthetic_fixture_v0.2.json \
  --schema typed_generativity_benchmark_contract_v0.2.schema.json \
  --summary summary.json --runner-view runner.json
```

The fixtures are synthetic, and structural validation does not certify scientific claims, model performance, assessor independence, or execution traces.

These materials specify a prospective study. No empirical improvement, internal type-like representation, or domain-specific scoring validity has been established by the current artifacts. The scoring contracts need independent calibration before confirmatory evaluation.

The website source and test infrastructure live elsewhere in this repository. The edit to the essay and the update to its publication checks are reviewed together to avoid accidental divergence.
