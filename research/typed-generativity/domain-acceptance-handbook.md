# Typed Generativity — Domain Acceptance Handbook v0.2

## Status and purpose

This handbook proposes **prospective evaluation rules** for the six domains used by *Typed Generativity — Scientific Revision V4*. No benchmark items have been independently adjudicated under these rules. No scientific, software, or agent execution results are reported. The rules require domain-expert approval before a confirmatory study.

Across domains, `accepted` has one procedural meaning: every frozen mandatory criterion has a supported positive final judgment for the submitted artifact under the relevant environment and evidence regime. Its epistemic meaning depends on the domain. A successful unit test and a kernel-checked proof have different guarantees; an expert-reviewed laboratory protocol and an actually executed experiment represent different evidence.

Each frozen item needs a task-family identifier, a versioned prompt, admissible target interpretations, independently authored target-alignment rubric, mandatory criteria, validator identities and versions, evidence grades, evaluator assignments, tool permissions, and an ambiguity policy. Item authors are separate from the operators generating model artifacts. Rubrics and hidden expected results remain outside the generator-facing task projection. All human scoring uses preserved independent decisions and explicit adjudication.

## 1. Code generation

**Target object.** A patch, module, function, or test artifact under a specified language, dependency, API, and behavioral contract. The evaluator must distinguish ordinary type checking from behavioral acceptance.

**Mandatory criterion families.** Target-to-request alignment, parse/build success under pinned dependencies, declared API and input-output compatibility, behavior on a frozen representative and adversarial test suite, and relevant side-effect or resource constraints. A formal refinement proof, if available, is recorded separately from test results. Test-suite acceptance is an observation on the tested inputs, not universal correctness.

**Independent reference.** Human-specified behavior contract and fixtures held outside the generator prompt. Property tests, reference implementations, mutation tests, and edge cases are appropriate calibration instruments. Benchmarks with a mutable repository need a fully specified base commit and execution environment.

**Disqualifying observations.** Mismatched return order, changed API signatures, incorrect exceptional behavior, unapproved dependency installation, unauthorized file modification, or fabricated test-output evidence. A dependency or environment failure is a separate evaluation status unless it follows from an unauthorized change by the candidate.

**Evidence grade.** Compiler/type-checker result plus test-suite results; formal verification only with a corresponding machine-checked statement and disclosed assumptions.

## 2. Lean and mathematical formalization

**Target object.** One of a formal statement, formal proof of a frozen theorem, informal mathematical derivation, or translation record. A benchmark item must select the intended object and must not combine proof checking and natural-language argument quality into one unspecified criterion.

**Mandatory criterion families.** Agreement of the formal statement with an independently frozen mathematical reference; well-formed definitions and imports; proof-term checking by the pinned Lean kernel where a proof is requested; recorded axiom dependency closure; and rejection of `sorry`, unauthorized axioms, or unapproved trusted computation. Successful elaboration of a declaration is insufficient to establish the theorem's mathematical truth under an intended interpretation.

**Independent reference.** Expert-written mathematical statement with quantified domains, hypotheses, and witnesses; a reviewed Lean target statement or an admissible set of equivalent statements; a versioned Lean environment and pinned library. Extract axiom dependencies from the exact result and document allowed foundational and additional axioms. Where feasible, recheck under an independent kernel or exported-proof checker.

**Disqualifying observations.** Altering the theorem into an easier claim, omitting a nonemptiness premise, proving supremum existence instead of attainment, importing an unrestricted axiom, using `sorry`, or reporting an unexecuted check as success. The allowed axiom set and the meaning of definitional equality must be specified for the particular formal environment.

**Evidence grade.** Formal kernel checking for the stated proposition, plus independent expert source-to-target alignment review. Their outcomes are recorded independently.

## 3. Explanation

**Target object.** An explanation for a declared audience, epistemic level, purpose, and permissible background. The output is evaluated as an explanatory artifact, not an unqualified truth oracle.

**Mandatory criterion families.** Correct identification of the intended question and audience; coverage of indispensable concepts; factual and mathematical accuracy relative to specified authoritative references; honest treatment of assumptions and uncertainty; and clarity under a pretested rubric. Distinguish clarity from factual correctness.

**Independent reference.** Domain-expert reference notes and a rubric drafted before seeing candidate outputs. Human reviewers judge interpretable criteria independently. For prompts compatible with several legitimate explanatory targets, item authors record an admissible set or move the task to a clarification cohort.

**Disqualifying observations.** Unsupported central assertion, materially false derivation, invented citation, audience mismatch leading to a materially misleading explanation, or replacement of requested proof with intuition alone.

**Evidence grade.** Source-backed expert review, supported where feasible by deterministic checks of factual assertions. Reviewer agreement must be reported rather than inferred from the final adjudicated label.

## 4. Scientific protocol design

**Target object.** A prospective experimental protocol for a stated hypothesis, measurement environment, and intended evidential claim. A proposed protocol is not a record of an executed experiment.

**Mandatory criterion families.** Operationalized hypothesis and primary estimand; specified measurement and controls relevant to the setting; replicate and sampling design; planned uncertainty analysis; relevant calibration or quality checks; declared exclusion and stopping rules; feasible resources and safety/authority constraints; and a conclusion no stronger than the planned evidence. An item lacking essential scientific context needs an explicit uncertainty or clarification standard.

**Independent reference.** Domain experts review the task-specific adequacy rubric, independently of candidate protocols. Feasibility, statistical adequacy, and safety review may have distinct assessor roles. The benchmark must report unavailable equipment or missing contextual information separately from model omissions.

**Disqualifying observations.** Conflating simulation with physical measurement, unsupported causal claims, absence of indispensable controls, hidden post hoc outcome selection, or declaring an unperformed experiment successful. An apparent protocol completeness score does not establish validity of eventual data.

**Evidence grade.** Prospective expert-reviewed protocol quality. Actual experimental evidence, if ever collected, constitutes a separate study under its own provenance, safety review, and measurement record.

## 5. Planning

**Target object.** A constrained plan or conditional policy from an explicitly specified initial state to a goal under permitted actions, resources, timing, and contingencies.

**Mandatory criterion families.** Correct target state; feasible sequencing and precedence; resource and time consistency; environmental and authorization constraints; recoverability under declared disturbances; and explicit conditions under which success is claimed. Evaluate the plan against a pinned state model or simulator if one is available.

**Independent reference.** Expert-specified state constraints, initial conditions, state-transition model, and acceptance tests. Scenario perturbations must be drawn independently from the generator's output. A plan's simulated feasibility is not proof of success in the physical world.

**Disqualifying observations.** Unavailable resources, conflicting dependencies, unapproved actions, a plan that cannot reach its stated goal under the declared model, or an unacknowledged irreversible step.

**Evidence grade.** Formal or programmatic constraint checking and controlled simulation, with human judgment for requirements outside the model. Real-world execution has a distinct evidence category.

## 6. Tool use

**Target object.** A typed, authorized action proposal or a bounded execution trace in a specified tool environment. Schema conformance, permission, attempted execution, and state reconciliation are distinct checks.

**Mandatory criterion families.** Selection of the correct tool and arguments; conformity with the current interface schema; enforcement of identity, role, consent, and permitted-use constraints; valid preconditions; observed action outcome; and reconciliation of resulting state where execution is authorized. If the benchmark is dry-run only, the outcome must be labeled as simulated and never as verified external execution.

**Independent reference.** Frozen tool specification, authorization policy, permitted action scope, isolated environment snapshot, expected state transitions, and trustworthy logs of tool invocations and resulting state. Generated explanations of success are not a substitute for observed tool evidence.

**Disqualifying observations.** Invocation beyond granted authority, schema-valid but unauthorized calls, falsely reported effects, skipped required validation, or unexplained divergence from the recorded post-state. If tool access fails for infrastructure reasons, the trial disposition records missing execution evidence separately from the model's attempted action.

**Evidence grade.** Structured tool-schema validation plus sandbox execution and state reconciliation, or explicitly labeled dry-run simulation. The mechanism enforcing permissions lies outside generator text and must itself be independently tested.

## Cross-domain reporting and negative controls

Acceptance rates must be reported per domain and per evidence grade. An equal-weight domain macro-average is a chosen summary across six heterogeneous contracts, not a natural frequency-weighted estimate of real-world tasks. The primary contrast compares assignment to type-first articulation with assignment to neutral preparation. Reviewers must not infer treatment from the displayed prompt or prep trace if it is avoidable, and any residual unblinding risk must be acknowledged.

Calibration items ought to include deliberately wrong target kinds, plausible invalid artifacts, missing required controls, absent or nonexecuted validators, and downstream-use violations. These are **test constructions**, not observations of model behavior. Negative controls must be selected independently of the system under assessment and must exercise each specific criterion's ability to reject violations. A good validator catches seeded failures without admitting inappropriate artifacts; passing a calibration set alone does not establish complete validator soundness.

For each tested item, retain criterion-level execution status and observed evidence; machine acceptance and reviewer judgments can disagree. Disagreement is reported and adjudicated under a frozen rule. The benchmark's validity rests on those substantive checks, not on the structural record validator shipped with the manuscript.
