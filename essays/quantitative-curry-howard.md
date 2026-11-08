# Quantitative Curry-Howard

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 be5dbebb3bfd7c0c7a8afbab0f48a614d113420d27cf2354b49b55e3dc2170cc; source Essay6_Quantitative_Curry_Howard_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Classical Curry-Howard gives an exact relation among propositions, types, proofs, and programs. Contemporary AI reasoning systems operate in the candidate layer surrounding that exact relation. They rank tactics prior to kernel acceptance, optimize relaxed logical objectives prior to hard validation, attach probabilities to model-relative scientific claims, generate code prior to tests and static analysis, and emit reasoning traces whose evidential status requires separate faithfulness checks. Quantitative Curry-Howard names this candidate-layer interface between typed validity and learned scoring.</p>
<p>The core judgment is displayed as Gamma |-_theta t : A |&gt; Q. Under context Gamma, system theta proposes candidate inhabitant t for target A and attaches quantitative evidence record Q. The record can include score semantics, probability, uncertainty, loss or margin, validator target, calibration status, validation outcome, diagnostics, repair distance, epistemic type, and permitted use. The judgment is operational. It records evidence around candidate typed artifacts and remains subordinate to the relevant checker, test, proof regime, review procedure, or empirical validation pathway.</p>
<p>The essay separates quantitative search over formal objects, soft logical satisfaction, probabilistic warrant, and calibrated semantic participation. This separation is audit-relevant. A score used for search, a relaxed truth value, a posterior probability, and a reviewer-facing confidence label have different semantics, validator targets, and permitted uses. The proposed benchmark tests whether quantitative records predict validation, repair cost, reviewer action, calibration quality, epistemic type, and downstream semantic participation. The proposal is retained only if numeric evidence changes validation, repair, review, reuse, or authorization decisions under explicit validators.</p>
<h2 id="contribution-summary">Contribution summary</h2>
<p class="table-display-caption" id="table-1-caption">Table 1. ID, Contribution, Publication claim</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table 1. ID, Contribution, Publication claim</caption>
<colgroup>
<col style="width: 7%"/>
<col style="width: 24%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>ID</strong></th>
<th scope="col"><strong>Contribution</strong></th>
<th scope="col"><strong>Publication claim</strong></th>
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
</table></div>
<h2 id="reader-map">Reader map</h2>
<p class="table-display-caption" id="table-2-caption">Table 2. Reader, Recommended path</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table 2. Reader, Recommended path</caption>
<colgroup>
<col style="width: 31%"/>
<col style="width: 68%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Reader</strong></th>
<th scope="col"><strong>Recommended path</strong></th>
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
</table></div>
<h2 id="position-in-the-compositional-intelligence-series">1. Position in the Compositional Intelligence series</h2>
<p>Quantitative Curry-Howard supplies the evidence layer for candidate typed artifacts. The preceding essays define membership, target-type construction, transformation preservation, language composition, and architecture specification. Essay 6 addresses the evidential interval between candidate construction and accepted validation. In that interval, learned systems often attach numerical evidence to artifacts whose exact status remains unresolved.</p>
<p>Numerical evidence requires a record before it can support review or downstream use. A theorem prover score, a code-model probability, a differentiable satisfaction value, a scientific posterior, and an agent action score share only a superficial numerical format. Their validator targets differ. The record must state what the number predicts, how it was calibrated, which failures it detects, and which epistemic type it supports. Absent those fields, quantitative output can produce unwarranted authority even when the underlying model improves search.</p>
<p>The series architecture can be rendered as a dependency chain in which evidence attaches after architecture and before action.</p>
<blockquote>
<p>artifact membership -&gt; target-type inference -&gt; transformation preservation -&gt; architecture specification -&gt; quantitative warrant</p>
</blockquote>
<p>The transition from architecture to warrant is substantive. Architecture determines the representational commitments available to a system. Quantitative Curry-Howard specifies how candidate artifacts produced under those commitments are scored, checked, repaired, and assigned permitted uses. Essay 7 then uses those evidence records as inputs to action authorization and audit.</p>
<h2 id="thesis-and-scope-conditions">2. Thesis and scope conditions</h2>
<p>Quantitative Curry-Howard treats learned scores and soft satisfaction values as evidence about candidate typed artifacts under explicit validator targets. The record does not upgrade a score into proof. It states how the score participates in search, calibration, repair, epistemic classification, and semantic participation.</p>
<p>The scope conditions preserve the exact layer. Classical Curry-Howard remains an exact judgment inside a specified formal system. Quantitative evidence occupies the candidate layer surrounding that judgment. Probabilities, losses, confidence values, and satisfaction values require stated semantics before they can enter review. The practical claim of the essay is validated only through calibration against checker outcomes, hard validators, expert review, repair traces, and permitted-use decisions.</p>
<p>The contribution is an interface theory for evidence, not a replacement calculus for proof. Differentiable theorem proving, probabilistic programming, fuzzy logics, learned proof search, trace verification, and scientific uncertainty supply heterogeneous evidence mechanisms. The common audit question is whether a number attached to a generated artifact improves validation, repair, calibration, or membership in a structured environment.</p>
<h2 id="classical-curry-howard-and-the-candidate-layer">3. Classical Curry-Howard and the candidate layer</h2>
<p>Classical Curry-Howard fixes the exact validity target. In a dependent type-theoretic proof assistant, a proposition is represented as a type, and an accepted proof is an inhabitant of that type under a formal context.</p>
<blockquote>
<p>Gamma |- t : A</p>
</blockquote>
<p>This judgment records formal validity relative to a system. It does not measure search difficulty, probability before checking, empirical support, maintainability, or source-target alignment. Those quantities arise outside the exact judgment, despite their importance for learned theorem proving and AI-assisted formalization.</p>
<p>AI reasoning systems generally operate around the exact judgment through candidate production. A model proposes a tactic, retrieves premises, drafts a proof script, ranks a program, estimates confidence for a claim, or generates a reasoning trace. These artifacts require pre-validation evidence records and post-failure diagnostics. The candidate layer is the learned object; the validation layer supplies acceptance, rejection, or repair information.</p>
<blockquote>
<p>candidate layer: Gamma |-_theta t : A |&gt; Q</p>
<p>validation layer: Gamma |- t : A</p>
<p>failure layer: diagnostics(t, A, Gamma)</p>
</blockquote>
<p>The distinction localizes responsibility. A learned score can be good evidence for prioritizing search and weak evidence for validity. A rejected tactic can still contain useful repair signal. A proof that validates can still have poor maintainability or weak alignment to the source theorem. Quantitative Curry-Howard places those distinctions in the record so aggregate success rates do not hide them.</p>
<h2 id="the-quantitative-judgment">4. The quantitative judgment</h2>
<p>The central judgment records candidate construction with an explicit evidence object.</p>
<blockquote>
<p>Gamma |-_theta t : A |&gt; Q</p>
</blockquote>
<p>Under context Gamma, system theta proposes candidate inhabitant t of target A with quantitative evidence record Q. The context can include proof state, prompt, source artifact, retrieved material, tool state, memory, dataset, policy context, or target environment. The target A states the attempted object class. The candidate t is the proposed artifact. The record Q specifies the semantics and validator target of the attached number.</p>
<blockquote>
<p>Q = (score, probability, uncertainty, margin, loss, calibration, validation_status,</p>
<p>diagnostics, repair_distance, epistemic_type, permitted_use)</p>
</blockquote>
<p>A quantitative record is usable only when its fields constrain interpretation. A confidence value needs calibration. A probability needs conditioning assumptions. A relaxed loss needs a hard-validator target or a stated proxy role. A reasoning-trace score needs a faithfulness validator. The absence of these fields turns numeric output into an annotation with unclear evidential force.</p>
<p>The operational pipeline is sequential in implementation and typed in interpretation.</p>
<blockquote>
<p>infer target A</p>
<p>construct candidate t</p>
<p>score candidate under theta</p>
<p>validate where available</p>
<p>calibrate scores against outcomes</p>
<p>repair failures using diagnostics</p>
<p>assign epistemic type</p>
<p>record permitted use</p>
</blockquote>
<p>Each step can fail independently. Target inference can be wrong even when the score is high. A valid candidate can receive low confidence. A calibrated score can predict acceptance without predicting future reuse. The value of the record lies in preserving these distinctions for evaluation and review.</p>
<h2 id="four-layers-of-quantitative-curry-howard">5. Four layers of Quantitative Curry-Howard</h2>
<h3 id="quantitative-search-over-formal-objects">5.1 Quantitative search over formal objects</h3>
<p>Quantitative search assigns scores to candidate formal objects before exact validation. The object can be a tactic, proof term, proof state transition, lemma, program fragment, schema, or formal statement. The score has operational value only when it predicts a validator-relevant outcome such as proof progress, acceptance, search-depth reduction, repairability, or proof-state simplification.</p>
<blockquote>
<p>P_theta(tactic | proof_state)</p>
</blockquote>
<p>The search layer exposes a common failure in learned theorem proving. Locally plausible tactics can score highly and still lead to dead ends, circular search, excessive proof length, hidden assumptions, or library-inconsistent scripts. A useful quantitative record therefore stores validation status and repair distance in addition to probability or rank.</p>
<h3 id="soft-logical-satisfaction">5.2 Soft logical satisfaction</h3>
<p>Soft logical satisfaction replaces exact logical acceptance with real-valued or differentiable objectives. Differentiable theorem proving, real-valued neural logics, and proof-assistant treatments of fuzzy or differentiable logics show that such objectives can be studied formally. Their evidential status still depends on the semantics assigned to the value and its relation to hard validation.</p>
<p>A soft satisfaction value can mean relaxed constraint satisfaction, differentiable objective value, approximate truth under a t-norm, violation margin, or empirical fit. These meanings are not interchangeable. The quantitative_judgment record must state which interpretation is used and whether the value has been calibrated against a hard checker, exact constraint, reviewer decision, or downstream task outcome.</p>
<h3 id="probabilistic-warrant">5.3 Probabilistic warrant</h3>
<p>Probabilistic warrant concerns probabilities, posteriors, likelihoods, predictive distributions, and uncertainty estimates attached to candidate artifacts. Probabilistic programming and higher-order probability theory provide semantic tools for probabilistic computation. Scientific use requires additional record fields that state model assumptions, conditioning data, sensitivity, and permitted claim type.</p>
<p>A probability in this setting has no default epistemic type. It can be a calibrated predictive confidence, posterior support under a model, likelihood score, sampling frequency, judge-model score, or heuristic ranking value. The record assigns the number to one of these roles and limits downstream use accordingly.</p>
<h3 id="calibrated-semantic-participation">5.4 Calibrated semantic participation</h3>
<p>Calibrated semantic participation connects quantitative evidence to artifact membership. A generated proof script with high model confidence remains unvalidated until the target proof assistant accepts it. A scientific claim with posterior support remains model-relative until the evidentiary pathway supports stronger status. A reasoning trace with high plausibility remains a candidate trace until faithfulness and task relevance have been evaluated.</p>
<p>Calibration supplies the bridge from score to action. A score is useful when it predicts validation, repair cost, reviewer acceptance, downstream reuse, or safe action. It is hazardous when it assigns authority without predictive value. Quantitative Curry-Howard therefore treats calibration as an evidential condition, not as a cosmetic reporting field.</p>
<h2 id="quantitative-evidence-record-v0.2">6. Quantitative evidence record v0.2</h2>
<p>The quantitative_judgment record is the companion object for this essay. It should be compact enough to attach to candidate artifacts and precise enough to prevent warrant confusion. The record is needed whenever a score, probability, loss, confidence value, or satisfaction value influences review, repair, reuse, or authorization.</p>
<p class="table-display-caption" id="table-3-caption">Table 3. Field, Question answered, Failure addressed</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table 3. Field, Question answered, Failure addressed</caption>
<colgroup>
<col style="width: 21%"/>
<col style="width: 43%"/>
<col style="width: 34%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Field</strong></th>
<th scope="col"><strong>Question answered</strong></th>
<th scope="col"><strong>Failure addressed</strong></th>
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
</table></div>
<p>The record should be interpreted as an audit artifact. Its fields are retained only when they alter validation, diagnosis, review, repair, reuse, or permitted use. If a field is filled after the fact and never consulted, the benchmark should remove it or reserve it for high-risk domains.</p>
<h2 id="state-of-the-art-landscape-and-source-control">7. State-of-the-art landscape and source control</h2>
<p>The state-of-the-art landscape supplies mechanisms for the candidate layer without validating the proposed record. Differentiable proving motivates soft search over proof-like objects. Logical Neural Networks motivate score semantics for real-valued logical bounds. Quasi-Borel spaces motivate rigorous treatment of higher-order probability. Formalized fuzzy and differentiable logics show that soft logics can receive algebraic and proof-theoretic analysis. Learned theorem proving and trace evaluation motivate checker-facing validation and faithfulness records.</p>
<p class="table-display-caption" id="table-4-caption">Table 4. Source area, What it contributes, Use in this essay</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table 4. Source area, What it contributes, Use in this essay</caption>
<colgroup>
<col style="width: 25%"/>
<col style="width: 39%"/>
<col style="width: 35%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Source area</strong></th>
<th scope="col"><strong>What it contributes</strong></th>
<th scope="col"><strong>Use in this essay</strong></th>
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
</table></div>
<p>The source map is intentionally limited. Rocktaschel and Riedel, Riegel et al., Heunen et al., and Affeldt et al. motivate the warrant layer through established mechanisms and recent formal work. They do not establish the Quantitative Curry-Howard record, the benchmark, or the calibration protocol proposed here.</p>
<h2 id="worked-examples">8. Worked examples</h2>
<h3 id="lean-proof-search">8.1 Lean proof search</h3>
<p>Lean proof search exposes the candidate layer in a setting with exact validation. A model observes a proof state, retrieves premises, and proposes a tactic. The kernel or elaborator then accepts, rejects, or transforms the proof state. The quantitative record states what the score was intended to predict and records the actual validator result.</p>
<blockquote>
<p>Gamma = proof state, local context, retrieved lemmas</p>
<p>A = next valid proof-state transition</p>
<p>t = proposed tactic</p>
<p>Q = tactic probability, premise confidence, calibration, diagnostics</p>
</blockquote>
<p>The record has value when it predicts proof progress, reduces search, identifies repairable errors, or detects proof-state drift. It fails when high scores correlate with invalid tactics, circular searches, non-maintainable scripts, or misalignment between the formal target and the source theorem.</p>
<h3 id="differentiable-constraints">8.2 Differentiable constraints</h3>
<p>Differentiable constraint systems attach soft satisfaction values to candidate solutions or proof obligations. The target artifact can be a relaxed proof object, a candidate assignment, a safety certificate, or a learned representation. The record must state whether the value is an optimization objective, relaxed truth value, violation penalty, margin, or calibrated predictor of hard validation.</p>
<blockquote>
<p>A = constraint-satisfying object</p>
<p>t = candidate assignment or learned representation</p>
<p>Q = satisfaction value, gradient signal, violation profile, hard-validator status</p>
</blockquote>
<p>This example identifies the central soft-hard risk. A relaxed objective can improve optimization and still diverge from exact constraint satisfaction. Quantitative Curry-Howard records that divergence instead of treating the soft score as a proxy for validity by default.</p>
<h3 id="probabilistic-scientific-claim">8.3 Probabilistic scientific claim</h3>
<p>A probabilistic scientific artifact is often a structured claim record with more evidential content than a standalone number. A model can produce posterior support, confidence intervals, uncertainty bands, or predictive distributions. The record must state data sources, model assumptions, sensitivity, uncertainty, epistemic type, and permitted claim level.</p>
<blockquote>
<p>A = model-relative claim type</p>
<p>t = candidate scientific claim</p>
<p>Q = posterior support, uncertainty, sensitivity, calibration, permitted claim level</p>
</blockquote>
<p>The evidential status is limited by the validation pathway. A posterior can support a model-relative claim or motivate empirical testing. It does not support theorem-level or direct empirical status unless the relevant proof or measurement procedure supplies that stronger warrant.</p>
<h3 id="reasoning-trace-verification">8.4 Reasoning-trace verification</h3>
<p>Reasoning traces require separate scoring for plausibility and faithfulness. A generated trace can appear coherent and still fail to represent the actual computation that produced the answer. The record therefore separates trace confidence, answer confidence, verifier labels, step validity, and permitted use.</p>
<blockquote>
<p>A = faithful typed reasoning trace</p>
<p>t = generated trace</p>
<p>Q = step scores, verifier labels, faithfulness tests, answer linkage, permitted use</p>
</blockquote>
<p>This record prevents trace plausibility from being consumed as evidence of reasoning faithfulness. The trace supports explanation, review, or debugging only to the extent that the validator target has been specified and tested.</p>
<h3 id="code-synthesis-with-quantitative-evidence">8.5 Code synthesis with quantitative evidence</h3>
<p>Code synthesis combines probability, validation, and maintainability evidence. A generated patch can receive high model score, pass visible tests, and still violate an interface invariant or dependency constraint. The quantitative record must therefore store validator targets beyond token probability or public test results.</p>
<blockquote>
<p>A = patch satisfying specification and interface constraints</p>
<p>t = generated patch</p>
<p>Q = token logprob, test status, static-analysis diagnostics, repair distance, reviewer status</p>
</blockquote>
<p>The diagnostic value lies in relating scores to hidden tests, property checks, static analysis, review outcomes, and repair traces. A score that predicts visible test success and fails to predict invariant preservation has narrow permitted use.</p>
<h2 id="quantitative-curry-howard-bench-v0.2">9. Quantitative Curry-Howard Bench v0.2</h2>
<p>Quantitative Curry-Howard Bench tests whether evidence records improve decisions about candidate typed artifacts. The benchmark compares artifacts generated without records, artifacts with score-only reports, and artifacts with structured quantitative_judgment records. The record condition must show value beyond cosmetic confidence reporting.</p>
<p class="table-display-caption" id="table-5-caption">Table 5. Domain, Candidate artifact, Validator, Primary metric</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. Domain, Candidate artifact, Validator, Primary metric</caption>
<colgroup>
<col style="width: 20%"/>
<col style="width: 25%"/>
<col style="width: 29%"/>
<col style="width: 23%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Domain</strong></th>
<th scope="col"><strong>Candidate artifact</strong></th>
<th scope="col"><strong>Validator</strong></th>
<th scope="col"><strong>Primary metric</strong></th>
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
</table></div>
<p>The benchmark has a single decisive question. Does the structured record improve prediction of validation, repair cost, reviewer action, calibration, epistemic typing, or semantic participation? A record that only increases annotation length fails this test.</p>
<p class="table-display-caption" id="table-6-caption">Table 6. Metric, Definition, Why it matters</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table 6. Metric, Definition, Why it matters</caption>
<colgroup>
<col style="width: 23%"/>
<col style="width: 42%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Metric</strong></th>
<th scope="col"><strong>Definition</strong></th>
<th scope="col"><strong>Why it matters</strong></th>
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
</table></div>
<h2 id="failure-taxonomy">10. Failure taxonomy</h2>
<p>The failure taxonomy identifies the evidential fault induced by the score or record. Its function is diagnostic, with description subordinated to repair and calibration. Each label should point to a repair, calibration, validator, or permitted-use change.</p>
<p class="table-display-caption" id="table-7-caption">Table 7. Failure mode, Meaning, Diagnostic case</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table 7. Failure mode, Meaning, Diagnostic case</caption>
<colgroup>
<col style="width: 23%"/>
<col style="width: 36%"/>
<col style="width: 39%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure mode</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Diagnostic case</strong></th>
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
</table></div>
<h2 id="strongest-objections">11. Strongest objections</h2>
<p class="table-display-caption" id="table-8-caption">Table 8. Objection, Best answer, Operational test</p>
<div aria-labelledby="table-8-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="8" id="table-8"><caption class="visually-hidden">Table 8. Objection, Best answer, Operational test</caption>
<colgroup>
<col style="width: 30%"/>
<col style="width: 39%"/>
<col style="width: 30%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Objection</strong></th>
<th scope="col"><strong>Best answer</strong></th>
<th scope="col"><strong>Operational test</strong></th>
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
</table></div>
<h2 id="kill-criteria">12. Kill criteria</h2>
<p>The proposal should be revised or narrowed under the following decision rules.</p>
<p class="table-display-caption" id="table-9-caption">Table 9. Criterion, Decision rule</p>
<div aria-labelledby="table-9-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="9" id="table-9"><caption class="visually-hidden">Table 9. Criterion, Decision rule</caption>
<colgroup>
<col style="width: 10%"/>
<col style="width: 89%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Criterion</strong></th>
<th scope="col"><strong>Decision rule</strong></th>
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
</table></div>
<h2 id="conclusion-and-transition-to-essay-7">13. Conclusion and transition to Essay 7</h2>
<p>Quantitative Curry-Howard specifies the evidence layer around candidate typed artifacts. Generated artifacts often appear before validation, and learned systems attach numbers to them. Those numbers should guide search, review, repair, calibration, epistemic typing, and permitted use only when their semantics, validator targets, and calibration status are explicit.</p>
<p>The next essay moves from evidence to action. Once an agent calls tools, writes memory, edits files, schedules commitments, or operates instruments, quantitative warrant becomes an input to authorization and audit. Essay 7 therefore extends candidate typed artifacts with evidence records into typed effectful traces with preconditions, postconditions, authority, handlers, validators, rollback paths, and audit obligations.</p>
<h2 id="appendix-a.-quantitative_judgment-schema">Appendix A. quantitative_judgment schema</h2>
<blockquote>
<p>quantitative_judgment:</p>
<p>artifact_id: string</p>
<p>context: string</p>
<p>target: string</p>
<p>candidate: string</p>
<p>model_or_system: string</p>
<p>score: number | string | null</p>
<p>score_semantics: string</p>
<p>probability: number | null</p>
<p>uncertainty: string | null</p>
<p>loss_or_margin: string | null</p>
<p>validator_target: string</p>
<p>calibration_status: string</p>
<p>validation_status: string</p>
<p>diagnostics: string</p>
<p>repair_distance: string | null</p>
<p>epistemic_type: string</p>
<p>permitted_use: list[string]</p>
<p>forbidden_use: list[string]</p>
<p>reviewer_notes: string | null</p>
</blockquote>
<h2 id="appendix-b.-benchmark-item-schema">Appendix B. Benchmark item schema</h2>
<blockquote>
<p>qch_benchmark_item:</p>
<p>id: string</p>
<p>domain: string</p>
<p>source_context: string</p>
<p>target_type: string</p>
<p>candidate_artifact: string</p>
<p>quantitative_record: quantitative_judgment</p>
<p>validator: string</p>
<p>validation_outcome: string</p>
<p>repair_trace: string | null</p>
<p>ground_truth_epistemic_type: string</p>
<p>permitted_use_label: list[string]</p>
<p>failure_labels: list[string]</p>
</blockquote>
<h2 id="appendix-c.-source-use-warnings">Appendix C. Source-use warnings</h2>
<p class="table-display-caption" id="table-10-caption">Table 10. Source class, Use boundary</p>
<div aria-labelledby="table-10-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="10" id="table-10"><caption class="visually-hidden">Table 10. Source class, Use boundary</caption>
<colgroup>
<col style="width: 30%"/>
<col style="width: 69%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Source class</strong></th>
<th scope="col"><strong>Use boundary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>End-to-end differentiable proving</td>
<td>Supports feasibility of differentiable proof-search mechanisms; it does not validate the Quantitative Curry-Howard record.</td>
</tr>
<tr class="even">
<td>Logical Neural Networks</td>
<td>Supports neural-symbolic systems with real-valued logical semantics; it does not make neural scores equivalent to proof.</td>
</tr>
<tr class="odd">
<td>Quasi-Borel spaces</td>
<td>Supports higher-order probability semantics; it does not settle the epistemic status of generated scientific claims.</td>
</tr>
<tr class="even">
<td>Differentiable and fuzzy logics</td>
<td>Supports soft logics with algebraic and proof-theoretic properties; it does not remove validator-target and calibration requirements.</td>
</tr>
<tr class="odd">
<td>Proof assistants and theorem proving</td>
<td>Supply exact validation contexts; they do not establish alignment, calibration, repair value, or semantic participation alone.</td>
</tr>
<tr class="even">
<td>Reasoning-trace literature</td>
<td>Motivates trace verification; trace plausibility remains separate from trace faithfulness.</td>
</tr>
</tbody>
</table></div>
