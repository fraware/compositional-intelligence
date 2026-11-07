## Abstract

Classical Curry-Howard gives an exact relation among propositions, types, proofs, and programs. Contemporary AI reasoning systems operate in the candidate layer surrounding that exact relation. They rank tactics prior to kernel acceptance, optimize relaxed logical objectives prior to hard validation, attach probabilities to model-relative scientific claims, generate code prior to tests and static analysis, and emit reasoning traces whose evidential status requires separate faithfulness checks. Quantitative Curry-Howard names this candidate-layer interface between typed validity and learned scoring.

Quantitative Curry--Howard proposes a candidate-layer record Γ ⊢\_θ t : A ▷ Q. This is an operational annotation: system θ proposes candidate t for declared target label A under generator context Γ, with evidence record Q. The annotation is not a type-checking derivation. For a formal object language, a separate typing environment Δ and type τ determine independent acceptance through Δ ⊢ t : τ, with the correspondence between A and τ specified. Search rankings, soft satisfaction values, estimated probabilities, and reviewed confidence carry different semantics and validator targets.

Classical Curry–Howard relates a formal proof term to a judgment in a declared calculus. Quantitative search scores, relaxed logical satisfaction, probability estimates, and reviewer-facing warrants are separate evidence types. For a probability-valued warrant q in [0,1], the proposed record declares its binary target event Z, reference population D, observation process, and permitted decision role. Population calibration would mean E_D[Z | q] = q wherever the conditional expectation is defined; the claim must be assessed using held-out outcomes, subgroup diagnostics, and distribution-shift checks. The warrant remains advisory pending that evidence. A formal acceptance judgment Δ ⊢ t : τ remains independent of numerical warrant scores, including scores exhibiting pooled calibration.

## Contribution summary



<table>
<colgroup>
<col style="width: 7%"/>
<col style="width: 24%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Contribution</strong></th>
<th><strong>Publication claim</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C1</td>
<td>Quantitative judgment form</td>
<td>Gamma |-_theta t : A |&gt; Q records a candidate typed artifact with an attached quantitative evidence record.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Warrant-proof boundary</td>
<td>Scores, losses, probabilities, and confidence values guide search and review only under stated validator targets. Proof and exact validation remain properties of the relevant formal or empirical regime.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Four-layer model</td>
<td>The essay separates quantitative search, soft logical satisfaction, probabilistic warrant, and calibrated semantic participation.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Evidence record schema</td>
<td>The quantitative_judgment record stores score semantics, uncertainty, calibration, validation status, diagnostics, repair distance, epistemic type, and permitted use.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Calibration protocol</td>
<td>Quantitative evidence has practical force when it predicts validation, repair cost, reviewer action, reuse, or safe downstream use.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Bridge to action</td>
<td>Essay 7 treats warrant records as inputs to action authorization, memory updates, tool execution, rollback, and audit.</td>
</tr>
</tbody>
</table>



## Reader map



<table>
<colgroup>
<col style="width: 31%"/>
<col style="width: 68%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Reader</strong></th>
<th><strong>Recommended path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Formal-methods researcher</td>
<td>Sections 1, 3, 4, 5.1, 7, 8, and Appendix A</td>
</tr>
<tr class="even">
<td>AI-for-math researcher</td>
<td>Sections 4, 5.1, 8.1, 9, and Appendix B</td>
</tr>
<tr class="odd">
<td>Probabilistic-programming reader</td>
<td>Sections 5.3, 6, 8.3, and 9</td>
</tr>
<tr class="even">
<td>AI evaluation researcher</td>
<td>Sections 8, 9, 10, 11, and Appendix C</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read after Essay 5 and prior to Essay 7</td>
</tr>
</tbody>
</table>



## 1. Position in the Compositional Intelligence series {#1-position-in-the-compositional-intelligence-series}

Quantitative Curry-Howard supplies the evidence layer for candidate typed artifacts. The preceding essays define membership, target-type construction, transformation preservation, language composition, and architecture specification. Essay 6 addresses the evidential interval between candidate construction and accepted validation. In that interval, learned systems often attach numerical evidence to artifacts whose exact status remains unresolved.

Numerical evidence requires a record before it can support review or downstream use. A theorem prover score, a code-model probability, a differentiable satisfaction value, a scientific posterior, and an agent action score share only a superficial numerical format. Their validator targets differ. The record must state what the number predicts, how it was calibrated, which failures it detects, and which epistemic type it supports. Absent those fields, quantitative output can produce unwarranted authority even when the underlying model improves search.

The series architecture can be rendered as a dependency chain in which evidence attaches after architecture and before action.

> artifact membership -\> target-type inference -\> transformation preservation -\> architecture specification -\> quantitative warrant

The transition from architecture to warrant is substantive. Architecture determines the representational commitments available to a system. Quantitative Curry-Howard specifies how candidate artifacts produced under those commitments are scored, checked, repaired, and assigned permitted uses. Essay 7 then uses those evidence records as inputs to action authorization and audit.

## 2. Thesis and scope conditions {#2-thesis-and-scope-conditions}

Quantitative Curry-Howard treats learned scores and soft satisfaction values as evidence about candidate typed artifacts under explicit validator targets. The record does not upgrade a score into proof. It states how the score participates in search, calibration, repair, epistemic classification, and semantic participation.

Classical Curry-Howard specifies an exact judgment relative to a formal calculus. Candidate-ranking scores, relaxed satisfiability measures, probabilistic claims and confidence estimates occupy distinct evidence regimes. Each score must be interpreted relative to a stated target event or decision and its own validation procedure. Calibration claims depend on a declared sampling frame and held-out outcomes; learned evidence gains practical status only through measured improvements in search, review, repair or downstream use.

The contribution is an interface theory for evidence, not a replacement calculus for proof. Differentiable theorem proving, probabilistic programming, fuzzy logics, learned proof search, trace verification, and scientific uncertainty supply heterogeneous evidence mechanisms. The common audit question is whether a number attached to a generated artifact improves validation, repair, calibration, or membership in a structured environment.

## 3. Classical Curry-Howard and the candidate layer {#3-classical-curry-howard-and-the-candidate-layer}

Classical Curry-Howard fixes the exact validity target. In a dependent type-theoretic proof assistant, a proposition is represented as a type, and an accepted proof is an inhabitant of that type under a formal context.

> Δ ⊢ t : τ

This judgment records formal validity relative to a system. It does not measure search difficulty, probability before checking, empirical support, maintainability, or source-target alignment. Those quantities arise outside the exact judgment, despite their importance for learned theorem proving and AI-assisted formalization.

AI reasoning systems generally operate around the exact judgment through candidate production. A model proposes a tactic, retrieves premises, drafts a proof script, ranks a program, estimates confidence for a claim, or generates a reasoning trace. These artifacts require pre-validation evidence records and post-failure diagnostics. The candidate layer is the learned object; the validation layer supplies acceptance, rejection, or repair information.

> candidate layer: Gamma \|-\_theta t : A \|\> Q
>
> validation layer: Δ ⊢ t : τ (when the target label A denotes formal type τ)
>
> failure layer: diagnostics(t, A, Gamma)

The distinction localizes responsibility. A learned score can be good evidence for prioritizing search and weak evidence for validity. A rejected tactic can still contain useful repair signal. A proof that validates can still have poor maintainability or weak alignment to the source theorem. Quantitative Curry-Howard places those distinctions in the record so aggregate success rates do not hide them.

## 4. The quantitative judgment {#4-the-quantitative-judgment}

The central judgment records candidate construction with an explicit evidence object.

> Gamma \|-\_theta t : A \|\> Q

Under operational generator context Γ, system θ proposes a candidate representation t for target-class label A and attaches quantitative evidence record Q. The record states the target event or quantity, score meaning, calibration status, uncertainty, validator outcome, provenance, and permissible use. In formal tasks, accepted inhabitation is independently checked as Δ ⊢ t : τ under an explicit label-to-type mapping. Neither the annotation nor the numerical score constitutes a proof.

> Q = (score, probability, uncertainty, margin, loss, calibration, validation_status,
>
> diagnostics, repair_distance, epistemic_type, permitted_use)

A quantitative record is interpretable only relative to its declared score meaning. A probability claim identifies the random event, conditioning information, target population and validator used to observe outcomes. Calibration is an empirical property assessed on separate labeled data under a stated distribution and evaluation protocol, not a label conferred by recording a confidence value. Search logits, rank scores, soft logical satisfaction values and losses do not automatically represent probabilities of proof validity. Where hard validation is absent or reviewers disagree, record the uncertainty and the limitations of the resulting warrant explicitly.

The operational pipeline is sequential in implementation and typed in interpretation.

> infer target A
>
> construct candidate t
>
> score candidate under theta
>
> validate where available
>
> calibrate scores against outcomes
>
> repair failures using diagnostics
>
> assign epistemic type
>
> record permitted use

Each step can fail independently. Target inference can be wrong even when the score is high. A valid candidate can receive low confidence. A calibrated score can predict acceptance without predicting future reuse. The value of the record lies in preserving these distinctions for evaluation and review.

## 5. Four layers of Quantitative Curry-Howard {#5-four-layers-of-quantitative-curry-howard}

### 5.1 Quantitative search over formal objects {#5-1-quantitative-search-over-formal-objects}

Quantitative search assigns scores to candidate formal objects before exact validation. The object can be a tactic, proof term, proof state transition, lemma, program fragment, schema, or formal statement. The score has operational value only when it predicts a validator-relevant outcome such as proof progress, acceptance, search-depth reduction, repairability, or proof-state simplification.

> P_theta(tactic \| proof_state)

The search layer exposes a common failure in learned theorem proving. Locally plausible tactics can score highly and still lead to dead ends, circular search, excessive proof length, hidden assumptions, or library-inconsistent scripts. A useful quantitative record therefore stores validation status and repair distance in addition to probability or rank.

### 5.2 Soft logical satisfaction {#5-2-soft-logical-satisfaction}

Soft logical satisfaction replaces exact logical acceptance with real-valued or differentiable objectives. Differentiable theorem proving, real-valued neural logics, and proof-assistant treatments of fuzzy or differentiable logics show that such objectives can be studied formally. Their evidential status still depends on the semantics assigned to the value and its relation to hard validation.

A soft satisfaction value can mean relaxed constraint satisfaction, differentiable objective value, approximate truth under a t-norm, violation margin, or empirical fit. These meanings are not interchangeable. The quantitative_judgment record must state which interpretation is used and whether the value has been calibrated against a hard checker, exact constraint, reviewer decision, or downstream task outcome.

### 5.3 Probabilistic warrant {#5-3-probabilistic-warrant}

Probabilistic warrant concerns probabilities, posteriors, likelihoods, predictive distributions, and uncertainty estimates attached to candidate artifacts. Probabilistic programming and higher-order probability theory provide semantic tools for probabilistic computation. Scientific use requires additional record fields that state model assumptions, conditioning data, sensitivity, and permitted claim type.

A probability in this setting has no default epistemic type. It can be a calibrated predictive confidence, posterior support under a model, likelihood score, sampling frequency, judge-model score, or heuristic ranking value. The record assigns the number to one of these roles and limits downstream use accordingly.

### 5.4 Calibrated semantic participation {#5-4-calibrated-semantic-participation}

Calibrated semantic participation connects quantitative evidence to artifact membership. A generated proof script with high model confidence remains unvalidated until the target proof assistant accepts it. A scientific claim with posterior support remains model-relative until the evidentiary pathway supports stronger status. A reasoning trace with high plausibility remains a candidate trace until faithfulness and task relevance have been evaluated.

Classification confidence calibration tests whether predicted confidence agrees with empirical correctness frequencies <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P047" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P047-1" data-source-keys="Guo2017Calibration">[<a class="citation-link" href="#ref-Guo2017Calibration" aria-label="Provisional reference 1 — On Calibration of Modern Neural Networks">1</a>]</span>. This provides methodological background for evaluating predictive scores. In Quantitative Curry–Howard, proposed warrant scores would need an explicit target event or quantity, such as formal validation, repair cost, reviewer acceptance, downstream reuse, or authorized action. Binary acceptance events need held-out calibration analysis; continuous repair cost and other nonbinary outcomes need endpoint-appropriate predictive evaluation. Each decision policy must declare its outcome and test population. A high score alone confers no authority.

## 6. Quantitative evidence record v0.2 {#6-quantitative-evidence-record-v0-2}

The quantitative_judgment record is the companion object for this essay. It should be compact enough to attach to candidate artifacts and precise enough to prevent warrant confusion. The record is needed whenever a score, probability, loss, confidence value, or satisfaction value influences review, repair, reuse, or authorization.



<table>
<colgroup>
<col style="width: 21%"/>
<col style="width: 43%"/>
<col style="width: 34%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Question answered</strong></th>
<th><strong>Failure addressed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>target</td>
<td>Which type, claim, behavior, or object class is being attempted?</td>
<td>Score attached to an unclear object.</td>
</tr>
<tr class="even">
<td>score_semantics</td>
<td>What does the number mean?</td>
<td>Confidence treated as probability; loss treated as warrant.</td>
</tr>
<tr class="odd">
<td>validator_target</td>
<td>Which checker, test, reviewer, or validation condition should the score predict?</td>
<td>Optimization of the wrong property.</td>
</tr>
<tr class="even">
<td>calibration_status</td>
<td>Has the score been calibrated against outcomes?</td>
<td>Uncalibrated ranking used as evidence.</td>
</tr>
<tr class="odd">
<td>uncertainty</td>
<td>Which variability or epistemic uncertainty remains?</td>
<td>False precision.</td>
</tr>
<tr class="even">
<td>diagnostics</td>
<td>Which failure modes were detected?</td>
<td>Failed candidates treated as opaque.</td>
</tr>
<tr class="odd">
<td>repair_distance</td>
<td>How costly is the expected repair?</td>
<td>High-confidence artifacts with hidden maintenance cost.</td>
</tr>
<tr class="even">
<td>epistemic_type</td>
<td>Which kind of warrant supports the artifact?</td>
<td>Conjecture consumed as proof; simulation consumed as empirical claim.</td>
</tr>
<tr class="odd">
<td>permitted_use</td>
<td>Which downstream uses are allowed?</td>
<td>Evidence used outside its support regime.</td>
</tr>
</tbody>
</table>



The record should be interpreted as an audit artifact. Its fields are retained only when they alter validation, diagnosis, review, repair, reuse, or permitted use. If a field is filled after the fact and never consulted, the benchmark should remove it or reserve it for high-risk domains.

## 7. State-of-the-art landscape and source control {#7-state-of-the-art-landscape-and-source-control}

The state-of-the-art landscape supplies mechanisms for the candidate layer without validating the proposed record. Differentiable proving motivates soft search over proof-like objects <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P050" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P050-1" data-source-keys="DiffProving2017">[<a class="citation-link" href="#ref-DiffProving2017" aria-label="Provisional reference 2 — End-to-End Differentiable Proving">2</a>]</span>. Logical Neural Networks motivate score semantics for real-valued logical bounds <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P050" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P050-2" data-source-keys="LNN2020">[<a class="citation-link" href="#ref-LNN2020" aria-label="Provisional reference 3 — Logical Neural Networks">3</a>]</span>. Quasi-Borel spaces motivate rigorous treatment of higher-order probability <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P050" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P050-3" data-source-keys="QBS2017">[<a class="citation-link" href="#ref-QBS2017" aria-label="Provisional reference 4 — A Convenient Category for Higher-Order Probability Theory">4</a>]</span>. Formalized fuzzy and differentiable logics show that soft logics can receive algebraic and proof-theoretic analysis <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P050" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P050-4" data-source-keys="DifferentiableLogicsDTT2026">[<a class="citation-link" href="#ref-DifferentiableLogicsDTT2026" aria-label="Provisional reference 5 — A Foundation for Differentiable Logics using Dependent Type Theory">5</a>]</span>. Learned theorem proving and trace evaluation motivate checker-facing validation and faithfulness records.



<table>
<colgroup>
<col style="width: 25%"/>
<col style="width: 39%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Source area</strong></th>
<th><strong>What it contributes</strong></th>
<th><strong>Use in this essay</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>End-to-end differentiable proving</td>
<td>Differentiable proof search over dense representations inspired by backward chaining.</td>
<td>Motivates the soft-search layer and the boundary between proof success and soft objective value.</td>
</tr>
<tr class="even">
<td>Logical Neural Networks</td>
<td>Formula-associated neurons, real-valued logical bounds, and differentiable reasoning.</td>
<td>Motivates score semantics and soft logical satisfaction records.</td>
</tr>
<tr class="odd">
<td>Quasi-Borel spaces</td>
<td>A categorical setting for higher-order probability with continuous distributions and higher-order functions.</td>
<td>Motivates semantic care for probabilistic warrant.</td>
</tr>
<tr class="even">
<td>Differentiable and fuzzy logics in proof assistants</td>
<td>Formal comparison of analytic, algebraic, and proof-theoretic properties of soft logics.</td>
<td>Supports explicit specification for soft logics and validator targets.</td>
</tr>
<tr class="odd">
<td>Learned theorem proving</td>
<td>Candidate tactic generation, retrieval, proof-state interaction, and kernel validation.</td>
<td>Motivates the separation between candidate score and exact checker acceptance.</td>
</tr>
<tr class="even">
<td>Reasoning-trace evaluation</td>
<td>Tests and critiques for generated intermediate reasoning.</td>
<td>Motivates faithfulness records and permitted-use labels.</td>
</tr>
</tbody>
</table>



The source map is intentionally limited. Rocktaschel and Riedel, Riegel et al., Heunen et al., and Affeldt et al. <span class="citation-group" data-review="unapproved" data-target="QUANTITATIVE-CURRY-HOWARD-P051" data-scope-id="QUANTITATIVE-CURRY-HOWARD-P051-1" data-source-keys="DiffProving2017,LNN2020,QBS2017,DifferentiableLogicsDTT2026">[<a class="citation-link" href="#ref-DiffProving2017" aria-label="Provisional reference 2 — End-to-End Differentiable Proving">2</a>, <a class="citation-link" href="#ref-LNN2020" aria-label="Provisional reference 3 — Logical Neural Networks">3</a>, <a class="citation-link" href="#ref-QBS2017" aria-label="Provisional reference 4 — A Convenient Category for Higher-Order Probability Theory">4</a>, <a class="citation-link" href="#ref-DifferentiableLogicsDTT2026" aria-label="Provisional reference 5 — A Foundation for Differentiable Logics using Dependent Type Theory">5</a>]</span> motivate the warrant layer through established mechanisms and recent formal work. They do not establish the Quantitative Curry-Howard record, the benchmark, or the calibration protocol proposed here.

## 8. Worked examples {#8-worked-examples}

### 8.1 Lean proof search {#8-1-lean-proof-search}

Lean proof search exposes the candidate layer in a setting with exact validation. A model observes a proof state, retrieves premises, and proposes a tactic. The kernel or elaborator then accepts, rejects, or transforms the proof state. The quantitative record states what the score was intended to predict and records the actual validator result.

> Gamma = proof state, local context, retrieved lemmas
>
> A = next valid proof-state transition
>
> t = proposed tactic
>
> Q = tactic probability, premise confidence, calibration, diagnostics

The record has value when it predicts proof progress, reduces search, identifies repairable errors, or detects proof-state drift. It fails when high scores correlate with invalid tactics, circular searches, non-maintainable scripts, or misalignment between the formal target and the source theorem.

### 8.2 Differentiable constraints {#8-2-differentiable-constraints}

Differentiable constraint systems attach soft satisfaction values to candidate solutions or proof obligations. The target artifact can be a relaxed proof object, a candidate assignment, a safety certificate, or a learned representation. The record must state whether the value is an optimization objective, relaxed truth value, violation penalty, margin, or calibrated predictor of hard validation.

> A = constraint-satisfying object
>
> t = candidate assignment or learned representation
>
> Q = satisfaction value, gradient signal, violation profile, hard-validator status

This example identifies the central soft-hard risk. A relaxed objective can improve optimization and still diverge from exact constraint satisfaction. Quantitative Curry-Howard records that divergence instead of treating the soft score as a proxy for validity by default.

### 8.3 Probabilistic scientific claim {#8-3-probabilistic-scientific-claim}

A probabilistic scientific artifact is often a structured claim record with more evidential content than a standalone number. A model can produce posterior support, confidence intervals, uncertainty bands, or predictive distributions. The record must state data sources, model assumptions, sensitivity, uncertainty, epistemic type, and permitted claim level.

> A = model-relative claim type
>
> t = candidate scientific claim
>
> Q = posterior support, uncertainty, sensitivity, calibration, permitted claim level

The evidential status is limited by the validation pathway. A posterior can support a model-relative claim or motivate empirical testing. It does not support theorem-level or direct empirical status unless the relevant proof or measurement procedure supplies that stronger warrant.

### 8.4 Reasoning-trace verification {#8-4-reasoning-trace-verification}

Reasoning traces require separate scoring for plausibility and faithfulness. A generated trace can appear coherent and still fail to represent the actual computation that produced the answer. The record therefore separates trace confidence, answer confidence, verifier labels, step validity, and permitted use.

> A = faithful typed reasoning trace
>
> t = generated trace
>
> Q = step scores, verifier labels, faithfulness tests, answer linkage, permitted use

This record prevents trace plausibility from being consumed as evidence of reasoning faithfulness. The trace supports explanation, review, or debugging only to the extent that the validator target has been specified and tested.

### 8.5 Code synthesis with quantitative evidence {#8-5-code-synthesis-with-quantitative-evidence}

Code synthesis combines probability, validation, and maintainability evidence. A generated patch can receive high model score, pass visible tests, and still violate an interface invariant or dependency constraint. The quantitative record must therefore store validator targets beyond token probability or public test results.

> A = patch satisfying specification and interface constraints
>
> t = generated patch
>
> Q = token logprob, test status, static-analysis diagnostics, repair distance, reviewer status

The diagnostic value lies in relating scores to hidden tests, property checks, static analysis, review outcomes, and repair traces. A score that predicts visible test success and fails to predict invariant preservation has narrow permitted use.

## 9. Quantitative Curry-Howard Bench v0.2 {#9-quantitative-curry-howard-bench-v0-2}

Quantitative Curry-Howard Bench tests whether a structured evidence record changes decisions about candidate typed artifacts. Compare score-only and structured-record conditions using the same candidate pool, validators, model access, information budget and reviewer effort; report costs for extra evidence collection. Define the target event and primary decision metric before inspecting outcomes. Evaluate calibration and utility on held-out data without leaking validation results into predictive features. The practical claim succeeds only if the record improves a specified action, calibration, diagnosis or repair outcome beyond a cost-matched baseline.



<table>
<colgroup>
<col style="width: 20%"/>
<col style="width: 25%"/>
<col style="width: 29%"/>
<col style="width: 23%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Domain</strong></th>
<th><strong>Candidate artifact</strong></th>
<th><strong>Validator</strong></th>
<th><strong>Primary metric</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Lean or theorem proving</td>
<td>Tactic, proof script, formal statement.</td>
<td>Kernel check, proof replay, proof-state progress.</td>
<td>Validation prediction and repair distance.</td>
</tr>
<tr class="even">
<td>Code synthesis</td>
<td>Function, patch, query, typed API call.</td>
<td>Tests, type checker, static analysis, interface review.</td>
<td>Validity, invariant preservation, repair cost.</td>
</tr>
<tr class="odd">
<td>Differentiable constraints</td>
<td>Assignment, relaxed proof, constraint certificate.</td>
<td>Hard constraint check, violation analysis.</td>
<td>Soft-hard alignment.</td>
</tr>
<tr class="even">
<td>Scientific claims</td>
<td>Model-relative claim, uncertainty statement, protocol claim.</td>
<td>Sensitivity analysis, replication, expert review.</td>
<td>Epistemic-type accuracy.</td>
</tr>
<tr class="odd">
<td>Reasoning traces</td>
<td>Step trace, explanation, decomposition.</td>
<td>Faithfulness test, verifier, human review.</td>
<td>Trace usefulness and misleading-trace rate.</td>
</tr>
</tbody>
</table>



The benchmark has a single decisive question. Does the structured record improve prediction of validation, repair cost, reviewer action, calibration, epistemic typing, or semantic participation? A record that only increases annotation length fails this test.



<table>
<colgroup>
<col style="width: 23%"/>
<col style="width: 42%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Metric</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Why it matters</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>validation AUC</td>
<td>How well scores predict checker or validator success.</td>
<td>Tests operational meaning of scores.</td>
</tr>
<tr class="even">
<td>calibration error</td>
<td>Gap between confidence and empirical success.</td>
<td>Detects false authority.</td>
</tr>
<tr class="odd">
<td>repair-distance prediction</td>
<td>How well records predict edit, search, or reviewer effort.</td>
<td>Measures practical usefulness.</td>
</tr>
<tr class="even">
<td>epistemic-type accuracy</td>
<td>Whether the record assigns the correct warrant class.</td>
<td>Prevents warrant confusion.</td>
</tr>
<tr class="odd">
<td>semantic-participation gain</td>
<td>Improvement in reuse, review, repair, or permitted-use decisions.</td>
<td>Connects to the series thesis.</td>
</tr>
<tr class="even">
<td>misleading-score rate</td>
<td>Frequency of high-score invalid or unsafe artifacts.</td>
<td>Detects dangerous evidence failures.</td>
</tr>
</tbody>
</table>



## 10. Failure taxonomy {#10-failure-taxonomy}

The failure taxonomy identifies the evidential fault induced by the score or record. Its function is diagnostic, with description subordinated to repair and calibration. Each label should point to a repair, calibration, validator, or permitted-use change.



<table>
<colgroup>
<col style="width: 23%"/>
<col style="width: 36%"/>
<col style="width: 39%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure mode</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Diagnostic case</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>score-validity gap</td>
<td>High score fails to predict validation.</td>
<td>A proof tactic has high probability and receives kernel rejection.</td>
</tr>
<tr class="even">
<td>soft-hard mismatch</td>
<td>Soft satisfaction diverges from hard constraint satisfaction.</td>
<td>A relaxed logic objective passes and the exact validator fails.</td>
</tr>
<tr class="odd">
<td>calibration collapse</td>
<td>Confidence no longer matches success frequency.</td>
<td>High-confidence code patches fail hidden tests.</td>
</tr>
<tr class="even">
<td>warrant inflation</td>
<td>A weak evidence type is consumed as a stronger one.</td>
<td>A simulation-derived claim is used as empirical fact.</td>
</tr>
<tr class="odd">
<td>trace unfaithfulness</td>
<td>Reasoning trace fails to explain the actual answer path.</td>
<td>A coherent trace receives a negative step-linkage verdict.</td>
</tr>
<tr class="even">
<td>repair opacity</td>
<td>Failure gives no useful path to correction.</td>
<td>An invalid proof script has score but lacks diagnostics.</td>
</tr>
<tr class="odd">
<td>permitted-use violation</td>
<td>Evidence is used outside its support regime.</td>
<td>A benchmark score is used to justify deployment action.</td>
</tr>
<tr class="even">
<td>metric gaming</td>
<td>The score improves without better validation or reuse.</td>
<td>A model emits calibrated-looking records without better artifacts.</td>
</tr>
</tbody>
</table>



## 11. Strongest objections {#11-strongest-objections}



<table>
<colgroup>
<col style="width: 30%"/>
<col style="width: 39%"/>
<col style="width: 30%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Best answer</strong></th>
<th><strong>Operational test</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Curry-Howard is exact and AI scores are approximate.</td>
<td>Exact judgment and candidate judgment are kept separate.</td>
<td>Check whether readers can identify proof, validation, and warrant layers in examples.</td>
</tr>
<tr class="even">
<td>Probability has a different epistemic status from proof.</td>
<td>The record assigns epistemic type and permitted use, preserving the proof boundary.</td>
<td>Audit claim labels in scientific and theorem-proving cases.</td>
</tr>
<tr class="odd">
<td>Differentiable logic already covers soft reasoning.</td>
<td>The essay organizes soft reasoning around validation, calibration, repair, and semantic participation.</td>
<td>Compare record condition against score-only condition.</td>
</tr>
<tr class="even">
<td>Scores can be gamed.</td>
<td>The benchmark includes misleading-score rate, calibration error, and downstream-use constraints.</td>
<td>Use adversarial high-score invalid artifacts.</td>
</tr>
<tr class="odd">
<td>The record adds metadata overhead.</td>
<td>Fields are retained only when they improve diagnosis or decisions.</td>
<td>Ablate fields and measure repair or review gains.</td>
</tr>
<tr class="even">
<td>Reasoning traces are often unfaithful.</td>
<td>Trace faithfulness is a validator target, not an assumption.</td>
<td>Evaluate trace utility with verifier and reviewer protocols.</td>
</tr>
</tbody>
</table>



## 12. Kill criteria {#12-kill-criteria}

The proposal should be revised or narrowed under the following decision rules.



<table>
<colgroup>
<col style="width: 10%"/>
<col style="width: 89%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Criterion</strong></th>
<th><strong>Decision rule</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>K1</td>
<td>Quantitative records do not improve prediction of validation, repair cost, reviewer action, reuse, or permitted-use decisions.</td>
</tr>
<tr class="even">
<td>K2</td>
<td>Score semantics remain too ambiguous for reliable annotation across domains.</td>
</tr>
<tr class="odd">
<td>K3</td>
<td>Calibration measures do not reduce misleading-score use.</td>
</tr>
<tr class="even">
<td>K4</td>
<td>Soft logical satisfaction fails to predict hard validation in domains with hard validators.</td>
</tr>
<tr class="odd">
<td>K5</td>
<td>Epistemic typing does not reduce warrant inflation.</td>
</tr>
<tr class="even">
<td>K6</td>
<td>Record fields add review cost without diagnostic value.</td>
</tr>
<tr class="odd">
<td>K7</td>
<td>Models learn to produce plausible records without improving artifact quality.</td>
</tr>
</tbody>
</table>



## 13. Conclusion and transition to Essay 7 {#13-conclusion-and-transition-to-essay-7}

Quantitative Curry-Howard specifies the evidence layer around candidate typed artifacts. Generated artifacts often appear before validation, and learned systems attach numbers to them. Those numbers should guide search, review, repair, calibration, epistemic typing, and permitted use only when their semantics, validator targets, and calibration status are explicit.

The next essay moves from evidence to action. Once an agent calls tools, writes memory, edits files, schedules commitments, or operates instruments, quantitative warrant becomes an input to authorization and audit. Essay 7 therefore extends candidate typed artifacts with evidence records into typed effectful traces with preconditions, postconditions, authority, handlers, validators, rollback paths, and audit obligations.

## Appendix A. quantitative_judgment schema {#appendix-a-quantitative-judgment-schema}

> quantitative_judgment:
>
> artifact_id: string
>
> context: string
>
> target: string
>
> candidate: string
>
> model_or_system: string
>
> score: number \| string \| null
>
> score_semantics: string
>
> probability: number \| null
>
> uncertainty: string \| null
>
> loss_or_margin: string \| null
>
> validator_target: string
>
> calibration_status: string
>
> validation_status: string
>
> diagnostics: string
>
> repair_distance: string \| null
>
> epistemic_type: string
>
> permitted_use: list\[string\]
>
> forbidden_use: list\[string\]
>
> reviewer_notes: string \| null

## Appendix B. Benchmark item schema {#appendix-b-benchmark-item-schema}

> qch_benchmark_item:
>
> id: string
>
> domain: string
>
> source_context: string
>
> target_type: string
>
> candidate_artifact: string
>
> quantitative_record: quantitative_judgment
>
> validator: string
>
> validation_outcome: string
>
> repair_trace: string \| null
>
> ground_truth_epistemic_type: string
>
> permitted_use_label: list\[string\]
>
> failure_labels: list\[string\]


<section class="bibliography" aria-labelledby="references-heading" data-review="unapproved">
<h2 id="references-heading">References (provisional)</h2>
<p class="bibliography-note">Source-scoped working citations. Text and references await specialist and author review.</p>
<ol class="references-list">
<li id="ref-Guo2017Calibration" data-source-key="Guo2017Calibration" data-provisional="true"><span class="ref-key">[1]</span>. <a href="https://proceedings.mlr.press/v70/guo17a.html" rel="noopener noreferrer">On Calibration of Modern Neural Networks</a>. <span class="ref-details">Guo, Pleiss, Sun, and Weinberger · ICML 2017, PMLR 70:1321–1330.</span></li>
<li id="ref-DiffProving2017" data-source-key="DiffProving2017" data-provisional="true"><span class="ref-key">[2]</span>. <a href="https://papers.nips.cc/paper/6969-end-to-end-differentiable-proving" rel="noopener noreferrer">End-to-End Differentiable Proving</a>. <span class="ref-details">Rocktäschel and Riedel · NeurIPS 2017.</span></li>
<li id="ref-LNN2020" data-source-key="LNN2020" data-provisional="true"><span class="ref-key">[3]</span>. <a href="https://arxiv.org/abs/2006.13155" rel="noopener noreferrer">Logical Neural Networks</a>. <span class="ref-details">Riegel et al. · arXiv preprint 2020.</span></li>
<li id="ref-QBS2017" data-source-key="QBS2017" data-provisional="true"><span class="ref-key">[4]</span>. <a href="https://arxiv.org/abs/1701.02547" rel="noopener noreferrer">A Convenient Category for Higher-Order Probability Theory</a>. <span class="ref-details">Heunen, Kammar, Staton, and Yang · LICS 2017.</span></li>
<li id="ref-DifferentiableLogicsDTT2026" data-source-key="DifferentiableLogicsDTT2026" data-provisional="true"><span class="ref-key">[5]</span>. <a href="https://arxiv.org/abs/2602.23878" rel="noopener noreferrer">A Foundation for Differentiable Logics using Dependent Type Theory</a>. <span class="ref-details">Affeldt et al. · arXiv preprint 2026.</span></li>
</ol>
</section>
