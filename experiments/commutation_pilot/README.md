# Commutation pilot — validation controls

**Status** — synthetic software controls, not an empirical benchmark, study result, or model evaluation.

The Compositional Intelligence synthesis proposes using explicit source transformations, translations, corresponding target transformations, acceptance relations, and validators as diagnostic records. This directory implements a deliberately narrow control for the record taxonomy. Every item is an integer polynomial represented by a finite coefficient vector (constant coefficient first). Exact coefficient equality provides a complete oracle in this restricted domain.

The synthetic cases distinguish correct path agreement, matching invalid paths, an error uniquely attributable to the transform-then-translate path, an error uniquely attributable to the translate-then-transform path, and disagreement where neither path matches the independent reference. The classifier intentionally abstains from single-component attribution in the last case.

Run the deterministic validation:

    python3 -m unittest discover -s experiments/commutation_pilot -p 'test_*.py' -v
    python3 experiments/commutation_pilot/evaluate.py

The output explicitly identifies its synthetic status. No generated artifacts, agent trajectories, or human annotations have been evaluated. Passing these tests establishes only that the toy record parser and classifier behave as specified.

## What this control does and does not establish

A complete reference polynomial is available to both paths. Equality of coefficient vectors is exact, and any unequal degree-d polynomials admit a distinguishing integer input in the set from 0 through d. The evaluator uses this property to construct an exact disagreement witness without running untrusted source code. Local path validity is also checked by the independent reference, a stronger oracle than typical program tests, expert review, or informal-to-formal alignment.

The same reference evidence would enable a suitably equipped metamorphic-testing baseline to produce the same classifications. This control contains no mechanism favoring Functorial Consistency, and no incremental advantage follows from the fixture results.

## Protocol for a later empirical comparison

The prospective comparison tests whether a structured two-path diagnostic record improves correct, actionable fault identification, reviewer agreement, or repair efficiency relative to a **strong matched metamorphic-testing baseline**. Both conditions receive identical observations, source and target transformations, validation results, permitted reference access, query budgets, and execution resources. Only the presentation and use of the diagnostic record differ. An oracle mismatch counts as independently confirmed failure; uncertainty is recorded as uncertainty.

The unit of inference is an independent source-task or transformation family, with repeated random seeds and related instances nested within that unit. Hold out transformation templates and source repositories from any development examples. Randomize presentation order and blind annotators to the intervention label where feasible. Specify the reference-alignment process and adjudication rules before looking at intervention outcomes.

Pre-register the primary endpoint as the paired difference in independently adjudicated correct actionable diagnoses at matched cost, including explicit abstentions. Report the false-attribution rate, unknown-case coverage, validation and human-review expense, failure-detection recall, and per-domain uncertainty intervals. Use task-family clustered inference. Secondary analyses include recovery time and downstream repair correctness under identical validation budgets. Report inter-rater agreement for reviewed cases.

The suggested 80–120 items across heterogeneous domains form a **feasibility pilot**, not a powered confirmatory experiment. An independent holdout and power analysis are necessary before a positive claim. Include invalid-but-agreeing paths, ambiguous disagreement, stochastic outcomes, directional refinement, and reviewer disagreement. A failure of the structured record to improve actionable diagnoses at comparable resource cost is a substantive negative result.

Do not publish synthetic fixture counts as model performance, generalization evidence, or experimental validation of the research program.
