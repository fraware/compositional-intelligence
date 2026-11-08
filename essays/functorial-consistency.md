# Functorial Consistency

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 e0c2a62b7b1c76aeda91f2fee25b3880f7f88d33c93622f71737f8e807ab3b0a; source Essay3_Functorial_Consistency_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Functorial Consistency evaluates AI-generated artifacts by path agreement under structured transformation. The object of evaluation is a commutation-square item containing a source object, a source-side transformation, a translation or semantic transport, a corresponding target-side transformation, an equivalence regime, and a validator. The benchmark asks whether transform-then-translate agrees with translate-then-transform according to the acceptance relation declared for the target environment.</p>
<p>The proposal addresses a failure mode that local correctness obscures. A generated proof, program, semantic representation, plan, or claim record can validate locally and still lose an assumption, alter generality, change target type, ignore an added constraint, or satisfy a validator that measures the wrong relation. Functorial Consistency makes such failures observable by comparing two typed paths through the same transformation problem.</p>
<p>The contribution is a benchmark specification, not an empirical result. The essay distinguishes Functorial Consistency from accuracy, robustness, self-consistency, metamorphic testing, and standard compositional generalization. It then gives domain instantiations, equivalence regimes, metrics, failure labels, annotation procedures, a minimal pilot plan, and kill criteria. The proposal earns scientific value only if commutation-square records reveal actionable failures beyond local validity and ordinary perturbation tests.</p>
<p>Table 1. Contribution summary.</p>
<p class="table-display-caption" id="table-1-caption">Table 1. Contribution summary.</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table 1. Contribution summary.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>ID</strong></th>
<th scope="col"><strong>Contribution</strong></th>
<th scope="col"><strong>Technical content</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C1</td>
<td>Benchmark unit</td>
<td>The commutation-square record specifies x, f, T, g, epsilon, and V as the minimal unit of structure-preservation evaluation.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Equivalence-regime control</td>
<td>Every agreement judgment names the acceptance relation, validator, reviewer protocol, and decision rule.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Domain instantiation</td>
<td>The benchmark is specified for mathematics-to-Lean, requirements-to-code, semantic parsing, planning, and science-facing artifact transport.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Failure localization</td>
<td>The taxonomy separates object failure, transformation failure, translation failure, target-transformation failure, non-commutation, type drift, assumption loss, and validator mismatch.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Falsification conditions</td>
<td>The proposal is narrowed or rejected if path agreement adds no diagnostic signal beyond local metrics or if equivalence judgments cannot be made reliable.</td>
</tr>
</tbody>
</table></div>
<h2 id="evaluation-object">1. Evaluation object</h2>
<p>Functorial Consistency evaluates relation preservation across two typed construction paths. The evaluator supplies a source artifact x, a source-side transformation f, a translation or semantic transport T, and a target-side transformation g intended to realize the same change after translation. The comparison concerns the two target artifacts produced by the square, not the surface similarity of intermediate text.</p>
<blockquote>
<p>source object x -- f --&gt; transformed source f(x)<br/>
| |<br/>
T T<br/>
v v<br/>
target object T(x) -- g --&gt; transformed target g(T(x))<br/>
<br/>
Evaluation condition<br/>
T(f(x)) ~ g(T(x))</p>
</blockquote>
<p>The formula is a specification pattern whose content comes from the declared environments and validators. A square has no evaluative force until the source environment, target environment, transformation family, equivalence regime, and acceptance procedure have been fixed. The approximation sign therefore functions as a pointer to an audit record, not as a mathematical license for informal agreement.</p>
<p>Path agreement is typed by the target environment. In a proof assistant, agreement can use implication, theorem equivalence, definitional equality, or reviewed alignment between an informal source and a formal statement. In executable settings, agreement can use a reference specification, property tests, trace comparison, or refinement checks. In semantic parsing and planning, the relevant relation is determined by denotation, graph structure, goal satisfaction, precondition satisfaction, effect constraints, and resource constraints.</p>
<h2 id="position-within-the-compositional-intelligence-series">2. Position within the Compositional Intelligence series</h2>
<p>Functorial Consistency supplies the transformation test for the first three layers of the series. Semantic Participation specifies membership conditions for artifacts in structured environments. Typed Generativity specifies how a model infers a target object and constructs a candidate inhabitant. Functorial Consistency then tests whether the candidate artifact maintains the relation that connects it to source transformations and target operations.</p>
<p>The test constrains the later layers by requiring each extension to state its preserved structure. A language extension must state which semantic relation should commute under paraphrase or scope transformation. An architecture extension must state which task transformations a model family supports. A warrant layer must state how scores relate to validation, repair, or epistemic status. An action layer must state how traces preserve preconditions, postconditions, authority, and permitted effects.</p>
<p>This role also limits the claim. The essay does not assert that all AI evaluation reduces to commutation. It identifies a class of failures that arise when an artifact moves between representations or environments under a structured change. The benchmark should be used where a corresponding target-side operation and an acceptance relation can be stated with enough precision for annotation and repair.</p>
<h2 id="formal-status-of-the-square">3. Formal status of the square</h2>
<p>The commutation square uses category-theoretic notation as an operational control on evaluation design. Objects, transformations, transports, and path agreement force the benchmark author to specify both routes through the task. The notation contributes only if it improves item construction, failure localization, annotation reliability, and repair guidance.</p>
<p>The source and target environments need not satisfy a full categorical formalization for the benchmark to operate. A proof assistant, codebase, semantic parser, planning domain, or scientific workflow can supply artifacts and admissible transformations without a complete category-theoretic account. The relevant requirement is weaker and more practical. The environment must support enough structure to define the two paths and decide target-side agreement.</p>
<p>Table 2. Minimal FunctorialConsistencyItem fields.</p>
<p class="table-display-caption" id="table-2-caption">Table 2. Minimal FunctorialConsistencyItem fields.</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table 2. Minimal FunctorialConsistencyItem fields.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Field</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Required annotation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>E_s</td>
<td>Source environment</td>
<td>Object language, task context, source validation assumptions.</td>
</tr>
<tr class="even">
<td>E_t</td>
<td>Target environment</td>
<td>Formal system, executable interface, parser target, planner, workflow, or review setting.</td>
</tr>
<tr class="odd">
<td>x</td>
<td>Source object</td>
<td>The artifact or statement before transformation.</td>
</tr>
<tr class="even">
<td>f</td>
<td>Source transformation</td>
<td>Named operation with a declared semantic effect.</td>
</tr>
<tr class="odd">
<td>T</td>
<td>Translation or semantic transport</td>
<td>Procedure that maps source artifacts to target artifacts.</td>
</tr>
<tr class="even">
<td>g</td>
<td>Target-side transformation</td>
<td>Operation in the target environment corresponding to f.</td>
</tr>
<tr class="odd">
<td>epsilon</td>
<td>Equivalence or acceptance regime</td>
<td>Relation used to compare the two target artifacts.</td>
</tr>
<tr class="even">
<td>V</td>
<td>Validator or review protocol</td>
<td>Formal checker, executable test, denotational comparison, constraint checker, or reviewer rubric.</td>
</tr>
</tbody>
</table></div>
<h2 id="equivalence-regimes">4. Equivalence regimes</h2>
<p>The equivalence regime is the benchmark field that prevents path agreement from collapsing into impressionistic similarity. It states which relation the two target artifacts must satisfy and which procedure decides that relation. A dataset mixing formal proof equivalence, executable behavior, denotation, constraint satisfaction, and expert review must label those regimes separately.</p>
<p>Table 3. Equivalence regimes for path-agreement evaluation.</p>
<p class="table-display-caption" id="table-3-caption">Table 3. Equivalence regimes for path-agreement evaluation.</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table 3. Equivalence regimes for path-agreement evaluation.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Regime</strong></th>
<th scope="col"><strong>Acceptance relation</strong></th>
<th scope="col"><strong>Validator</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Formal</td>
<td>Targets are identical, interderivable, or equivalent inside a formal environment.</td>
<td>Definitional equality, theorem equivalence, provable implication, alpha equivalence.</td>
</tr>
<tr class="even">
<td>Executable</td>
<td>Targets exhibit the same behavior under a stated specification.</td>
<td>Unit tests, property tests, refinement checks, model checking, trace comparison.</td>
</tr>
<tr class="odd">
<td>Denotational</td>
<td>Targets denote the same semantic object or produce the same query result.</td>
<td>Logical equivalence, graph isomorphism, normalized forms, controlled-model evaluation.</td>
</tr>
<tr class="even">
<td>Constraint</td>
<td>Targets satisfy the same operative requirements despite surface differences.</td>
<td>Precondition checks, postcondition checks, frame conditions, resource and authority constraints.</td>
</tr>
<tr class="odd">
<td>Reviewed</td>
<td>Expert or hybrid review decides whether intended meaning is preserved.</td>
<td>Rubric-based review, agreement statistics, adjudication, recorded failure label.</td>
</tr>
<tr class="even">
<td>Layered</td>
<td>Several relations are required for acceptance.</td>
<td>Combined formal, executable, denotational, and reviewed decisions with explicit precedence.</td>
</tr>
</tbody>
</table></div>
<p>Reviewed alignment is admissible only when stronger validators are unavailable or incomplete. The review protocol must specify the rubric, reviewer expertise, agreement metric, adjudication rule, and accepted failure labels. An item that hides expert judgment behind the symbol epsilon is underspecified and should be excluded from early benchmark releases.</p>
<p>Layered equivalence is often necessary in high-value domains. Mathematics-to-Lean can require formal equivalence between target statements and reviewed alignment between the informal claim and the formal statement. Scientific artifact transport can require workflow validity, statistical-assumption review, and epistemic-type control. Agent plans can require goal satisfaction, effect checking, and authority review in a single item.</p>
<h2 id="relation-to-adjacent-evaluation-families">5. Relation to adjacent evaluation families</h2>
<p>Functorial Consistency should be compared directly with established evaluation practices. Its novelty is not the claim that transformations matter. Its specific contribution is the reusable path-agreement record that combines source transformation, target transport, target-side operation, explicit equivalence regime, and failure localization.</p>
<p>Table 4. Distinction from adjacent evaluation families.</p>
<p class="table-display-caption" id="table-4-caption">Table 4. Distinction from adjacent evaluation families.</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table 4. Distinction from adjacent evaluation families.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Evaluation family</strong></th>
<th scope="col"><strong>Primary question</strong></th>
<th scope="col"><strong>Additional requirement introduced here</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accuracy</td>
<td>Does the local output satisfy the item.</td>
<td>Compare two paths through a transformation square.</td>
</tr>
<tr class="even">
<td>Robustness</td>
<td>Does output quality stay stable under perturbation.</td>
<td>Measure structured covariance under a typed transformation.</td>
</tr>
<tr class="odd">
<td>Self-consistency</td>
<td>Do repeated samples or reasoning paths agree.</td>
<td>Compare transform-then-translate against translate-then-transform.</td>
</tr>
<tr class="even">
<td>Compositional generalization</td>
<td>Can the model recombine familiar structures in new configurations.</td>
<td>Record source and target transformations plus an acceptance relation.</td>
</tr>
<tr class="odd">
<td>Metamorphic testing</td>
<td>Do outputs satisfy relations induced by input transformations.</td>
<td>Add source-target transport and target-side transformation as first-class fields.</td>
</tr>
</tbody>
</table></div>
<p>The benchmark should be narrowed if path agreement merely reproduces the ranking obtained from local validity or standard robustness tests. The intended diagnostic gain appears when two target artifacts validate locally, but the square exposes assumption loss, unintended weakening, overstrengthening, type drift, or constraint mention without operative integration.</p>
<h2 id="benchmark-domains">6. Benchmark domains</h2>
<p>The initial benchmark should prioritize domains where validators can be made explicit. Mathematics-to-Lean, requirements-to-code, semantic parsing, and planning supply target environments with formal, executable, denotational, or constraint-based checks. Science-facing claim transport is central to the series, but its early use should be limited to a reviewed-alignment track until annotation reliability has been measured.</p>
<h3 id="informal-mathematics-to-lean">6.1 Informal mathematics to Lean</h3>
<p>Mathematical formalization provides the cleanest starting point for path-agreement evaluation. The target environment can check formal artifacts, and the remaining difficulty is source-target alignment. A Lean theorem can pass the kernel and still represent a weakened, overstrengthened, or misdirected version of the informal source claim.</p>
<p>A diagnostic item can use maximum attainment as the source relation. One path specializes an informal compact-domain theorem to a closed interval and then formalizes it. The other path formalizes the general theorem and specializes the resulting target statement. Agreement requires a formal relation inside Lean, together with reviewed alignment confirming that the target still expresses attainment by a witness point and not merely existence of a supremum. The item therefore tests formal validity and alignment loss in a single square.</p>
<h3 id="natural-language-requirements-to-code">6.2 Natural-language requirements to code</h3>
<p>Requirements-to-code tasks expose path failures through executable specifications. A requirement transformation often adds a behavioral constraint that a model can mention in comments, handle for a narrow case, or omit from the operative implementation. Path comparison separates code that passes simple examples from code that satisfies the transformed specification.</p>
<p>An order-preserving deduplication item illustrates the mechanism. The source transformation adds idempotence and generic element handling to the original order-preservation requirement. The target-side operation adds property tests for first-occurrence order, repeated application, and element generality. Agreement is executable when both paths satisfy the same reference properties and counterexample suite. A failure in this item identifies constraint integration, interface drift, or behavioral overfitting more precisely than local tests alone.</p>
<h3 id="natural-language-to-semantic-parse">6.3 Natural language to semantic parse</h3>
<p>Semantic parsing is suited to controlled transformation families. The source side can vary paraphrase, quantifier scope, attachment, lexical choice, or representation format, and the target side can compare logical form, denotation, graph structure, or query result. Early items should avoid open-ended paraphrase and use transformations whose semantic effect is annotated before model evaluation.</p>
<p>A quantifier-scope item gives the benchmark a clear target relation. The source transformation fixes an existential wide-scope reading before parsing. The target-side operation normalizes the produced logical form to that selected scope. Path agreement is decided through logical or denotational equivalence over controlled models, so the benchmark tests whether surface transformations alter the represented meaning in the intended direction.</p>
<h3 id="goals-to-plans">6.4 Goals to plans</h3>
<p>Planning items test whether source-side constraint changes lead to target-side plan changes with operative effects. A locally successful final state can conceal missing preconditions, resource conflicts, approval dependencies, or unintended side effects. Path agreement therefore requires both goal satisfaction and trace-level constraint satisfaction.</p>
<p>A human-approval item supplies a compact diagnostic case. The source transformation requires approval before external transmission of a report. The target-side operation inserts the approval request and prevents the send step until approval is recorded. Agreement requires precondition satisfaction, effect-trace validation, and authority-boundary review. A plan that reaches the final state without the gate fails the square despite apparent task completion.</p>
<h3 id="scientific-protocols-to-claims">6.5 Scientific protocols to claims</h3>
<p>Science-facing items require layered review in domains where formal equivalence is unavailable. Protocol transformations can add controls, alter uncertainty assumptions, impose stopping rules, or restrict permitted claims. The target artifact is often a claim record whose epistemic type must match the available evidence.</p>
<p>A simulation-to-empirical item tests warrant preservation. The source artifact is a simulation-derived stability result. The source transformation adds empirical measurement requirements. The target-side transformation changes the claim record so that empirical support is granted only after measurement evidence is present. Agreement is judged through epistemic-type preservation and expert review of evidence status. This track should remain small until reviewed-alignment protocols reach acceptable reliability.</p>
<h2 id="transformation-families">7. Transformation families</h2>
<p>A transformation family is admissible only when it has a meaningful source-side operation and a corresponding target-side operation. Arbitrary perturbations weaken the benchmark, since path agreement depends on typed transformations whose semantic effect can be checked or reviewed. The first dataset should therefore use a small controlled set before expanding to richer transformations.</p>
<p>Table 5. Controlled transformation families.</p>
<p class="table-display-caption" id="table-5-caption">Table 5. Controlled transformation families.</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. Controlled transformation families.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Family</strong></th>
<th scope="col"><strong>Definition</strong></th>
<th scope="col"><strong>Initial domains</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Paraphrase</td>
<td>Change surface wording with intended meaning preservation.</td>
<td>Semantic parsing, mathematics, protocols.</td>
</tr>
<tr class="even">
<td>Specialization</td>
<td>Restrict a general artifact to a specified case.</td>
<td>Mathematics, code, planning.</td>
</tr>
<tr class="odd">
<td>Generalization</td>
<td>Lift a specific artifact to a broader class.</td>
<td>Mathematics, architecture, protocols.</td>
</tr>
<tr class="even">
<td>Constraint addition</td>
<td>Add a requirement, precondition, approval step, resource limit, or invariant.</td>
<td>Code, planning, agents, science.</td>
</tr>
<tr class="odd">
<td>Representation change</td>
<td>Move an artifact among natural language, formal statement, code, graph, plan, or evidence record.</td>
<td>All core domains.</td>
</tr>
<tr class="even">
<td>Decomposition</td>
<td>Split an artifact into subartifacts whose recomposition has a declared relation.</td>
<td>Code, proofs, plans, protocols.</td>
</tr>
<tr class="odd">
<td>Refinement</td>
<td>Replace an underspecified artifact with a more precise target object.</td>
<td>Requirements, theorem statements, claim records.</td>
</tr>
<tr class="even">
<td>Authority transformation</td>
<td>Change the action or claim that an artifact is permitted to support.</td>
<td>Agent plans, tool calls, laboratory actions.</td>
</tr>
</tbody>
</table></div>
<p>A transformation family should be removed from the initial release if annotators cannot define the corresponding target-side operation. This rule is stricter than ordinary perturbation design and is central to the benchmark. The transformation must induce a checkable target-side relation.</p>
<h2 id="metrics">8. Metrics</h2>
<p>Functorial Consistency requires diagnostic metrics in place of a single aggregate score. Local validity and path agreement measure different properties. A system with high local validity and low path agreement is structurally unreliable; a system with high path agreement on trivial transformations has passed an insufficiently demanding item.</p>
<p>Table 6. Recommended metrics.</p>
<p class="table-display-caption" id="table-6-caption">Table 6. Recommended metrics. — Metric, Question, Signal</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table 6. Recommended metrics. — Metric, Question, Signal</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Metric</strong></th>
<th scope="col"><strong>Question</strong></th>
<th scope="col"><strong>Signal</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local validity</td>
<td>Does each path output validate in the target environment.</td>
<td>Checker pass, tests pass, parse validity, plan validity.</td>
</tr>
<tr class="even">
<td>Path agreement</td>
<td>Do the two target artifacts agree under epsilon.</td>
<td>Formal relation, executable equivalence, denotational agreement, reviewed alignment.</td>
</tr>
<tr class="odd">
<td>Type preservation</td>
<td>Does the target artifact keep the intended object class.</td>
<td>No drift from theorem to example, function to script, plan to narrative.</td>
</tr>
<tr class="even">
<td>Assumption preservation</td>
<td>Are assumptions retained or intentionally changed.</td>
<td>No missing compactness, approval, control, resource, or domain assumptions.</td>
</tr>
<tr class="odd">
<td>Generality preservation</td>
<td>Does the transformation alter generality only in the declared direction.</td>
<td>No unintended weakening, specialization, or overstrengthening.</td>
</tr>
<tr class="even">
<td>Constraint integration</td>
<td>Does an added constraint affect the artifact operationally.</td>
<td>Constraint appears in proof obligation, code branch, plan step, or claim type.</td>
</tr>
<tr class="odd">
<td>Repair cost</td>
<td>How much work restores agreement.</td>
<td>Edit distance, reviewer repair time, number of counterexamples.</td>
</tr>
<tr class="even">
<td>Reviewer agreement</td>
<td>Are human judgments reliable when used.</td>
<td>Inter-annotator agreement and adjudication rate.</td>
</tr>
<tr class="odd">
<td>Diagnostic novelty</td>
<td>Does the square reveal failures missed by local metrics.</td>
<td>Failure labels unique to path comparison.</td>
</tr>
</tbody>
</table></div>
<p>Diagnostic novelty is the decisive pilot statistic. If commutation items produce no new failure labels beyond local validity, the benchmark should be narrowed. If the square reveals assumption loss, generality collapse, target-type drift, validator mismatch, or constraint failure, the added annotation cost has a concrete evaluation function.</p>
<h2 id="failure-taxonomy">9. Failure taxonomy</h2>
<p>The failure taxonomy identifies the broken component of the square. This localization is the principal advantage of the record format. The evaluator should be able to say whether the source item, source transformation, translation, target transformation, equivalence regime, or validator produced the failure.</p>
<p>Table 7. Failure labels and repair implications.</p>
<p class="table-display-caption" id="table-7-caption">Table 7. Failure labels and repair implications.</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table 7. Failure labels and repair implications.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure label</strong></th>
<th scope="col"><strong>Definition</strong></th>
<th scope="col"><strong>Repair implication</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Object failure</td>
<td>The source object is ill-posed, ambiguous, or invalid.</td>
<td>Revise the benchmark item before model evaluation.</td>
</tr>
<tr class="even">
<td>Transformation failure</td>
<td>The source-side transformation changes the task in an unintended way.</td>
<td>Rewrite f and define its semantic effect.</td>
</tr>
<tr class="odd">
<td>Translation failure</td>
<td>T(x) is invalid, misaligned, or targeted at the wrong object type.</td>
<td>Improve target-type inference or transport.</td>
</tr>
<tr class="even">
<td>Target-transformation failure</td>
<td>g(T(x)) fails to implement the corresponding target-side change.</td>
<td>Specify a stronger target operation or validator.</td>
</tr>
<tr class="odd">
<td>Non-commutation</td>
<td>Both paths validate locally and disagree under epsilon.</td>
<td>Analyze relation preservation and repair one path.</td>
</tr>
<tr class="even">
<td>Type drift</td>
<td>The generated target changes object class across a path.</td>
<td>Add type-stability checks.</td>
</tr>
<tr class="odd">
<td>Assumption loss</td>
<td>A required assumption disappears across one path.</td>
<td>Require assumption records and checks.</td>
</tr>
<tr class="even">
<td>Generality collapse</td>
<td>A general claim is reduced to an unnecessary special case.</td>
<td>Check generality direction against f.</td>
</tr>
<tr class="odd">
<td>Overstrengthening</td>
<td>The target path asserts more than the source supports.</td>
<td>Limit target claims to transported support.</td>
</tr>
<tr class="even">
<td>Spurious equivalence</td>
<td>The validator accepts agreement despite semantic divergence.</td>
<td>Replace or layer the equivalence regime.</td>
</tr>
<tr class="odd">
<td>Validator mismatch</td>
<td>The chosen validator measures the wrong relation.</td>
<td>Select a validator aligned to the intended relation.</td>
</tr>
<tr class="even">
<td>Constraint mention without integration</td>
<td>The output names a constraint without making it operative.</td>
<td>Require executable, formal, or trace-level evidence of integration.</td>
</tr>
</tbody>
</table></div>
<h2 id="functorial-consistency-bench-v0.3">10. Functorial Consistency Bench v0.3</h2>
<p>A first benchmark release should be small, explicit, and validator-driven. Its purpose is to test the diagnostic value of the square, not to claim broad coverage. Each item must expose both paths and must declare the acceptance relation before any model output is evaluated.</p>
<h3 id="benchmark-item-schema">10.1 Benchmark item schema</h3>
<p>Table 8. Benchmark item schema.</p>
<p class="table-display-caption" id="table-8-caption">Table 8. Benchmark item schema.</p>
<div aria-labelledby="table-8-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="8" id="table-8"><caption class="visually-hidden">Table 8. Benchmark item schema.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Field</strong></th>
<th scope="col"><strong>Type or value</strong></th>
<th scope="col"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>id</td>
<td>string</td>
<td>Stable item identifier.</td>
</tr>
<tr class="even">
<td>domain</td>
<td>math_to_lean, requirements_to_code, semantic_parse, planning, science_claims</td>
<td>Domain label for reporting.</td>
</tr>
<tr class="odd">
<td>source_environment</td>
<td>string</td>
<td>Context in which x is interpreted.</td>
</tr>
<tr class="even">
<td>target_environment</td>
<td>string</td>
<td>Context in which target artifacts are validated.</td>
</tr>
<tr class="odd">
<td>source_object</td>
<td>string or object</td>
<td>Artifact before transformation.</td>
</tr>
<tr class="even">
<td>source_transformation.name</td>
<td>string</td>
<td>Name of f.</td>
</tr>
<tr class="odd">
<td>source_transformation.definition</td>
<td>string</td>
<td>Operational definition of f.</td>
</tr>
<tr class="even">
<td>source_transformation.family</td>
<td>controlled family</td>
<td>Transformation family from Table 5.</td>
</tr>
<tr class="odd">
<td>translation_task</td>
<td>string</td>
<td>Instruction or procedure defining T.</td>
</tr>
<tr class="even">
<td>target_transformation.name</td>
<td>string</td>
<td>Name of g.</td>
</tr>
<tr class="odd">
<td>target_transformation.definition</td>
<td>string</td>
<td>Operational definition of g.</td>
</tr>
<tr class="even">
<td>equivalence_regime.type</td>
<td>formal, executable, denotational, constraint, reviewed, layered</td>
<td>Acceptance relation.</td>
</tr>
<tr class="odd">
<td>validator</td>
<td>string</td>
<td>Checker, test suite, comparison rule, or reviewer protocol.</td>
</tr>
<tr class="even">
<td>acceptance_rule</td>
<td>string</td>
<td>Decision rule for agreement.</td>
</tr>
<tr class="odd">
<td>expected_failure_sensitivities</td>
<td>list</td>
<td>Failure labels the item is designed to reveal.</td>
</tr>
<tr class="even">
<td>reviewer_notes</td>
<td>string</td>
<td>Guidance for adjudication and repair.</td>
</tr>
</tbody>
</table></div>
<h3 id="model-output-schema">10.2 Model-output schema</h3>
<p>Table 9. Model-output record.</p>
<p class="table-display-caption" id="table-9-caption">Table 9. Model-output record. — Field, Purpose</p>
<div aria-labelledby="table-9-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="9" id="table-9"><caption class="visually-hidden">Table 9. Model-output record. — Field, Purpose</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 49%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Field</strong></th>
<th scope="col"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>item_id</td>
<td>Links the output to the benchmark item.</td>
</tr>
<tr class="even">
<td>model_id</td>
<td>Identifies model, system, scaffold, and decoding condition.</td>
</tr>
<tr class="odd">
<td>path_A_transform_then_translate.transformed_source</td>
<td>Records f(x).</td>
</tr>
<tr class="even">
<td>path_A_transform_then_translate.target_artifact</td>
<td>Records T(f(x)).</td>
</tr>
<tr class="odd">
<td>path_A_transform_then_translate.validation_result</td>
<td>Records local validation for path A.</td>
</tr>
<tr class="even">
<td>path_B_translate_then_transform.initial_target_artifact</td>
<td>Records T(x).</td>
</tr>
<tr class="odd">
<td>path_B_translate_then_transform.transformed_target_artifact</td>
<td>Records g(T(x)).</td>
</tr>
<tr class="even">
<td>path_B_translate_then_transform.validation_result</td>
<td>Records local validation for path B.</td>
</tr>
<tr class="odd">
<td>path_agreement_result</td>
<td>Records the decision under epsilon.</td>
</tr>
<tr class="even">
<td>failure_labels</td>
<td>Records localized failures.</td>
</tr>
<tr class="odd">
<td>repair_trace</td>
<td>Records edits or diagnostics needed to restore agreement.</td>
</tr>
<tr class="even">
<td>confidence_or_score</td>
<td>Optional calibrated score or model confidence.</td>
</tr>
<tr class="odd">
<td>notes</td>
<td>Records evaluator caveats.</td>
</tr>
</tbody>
</table></div>
<h3 id="dataset-design">10.3 Dataset design</h3>
<p>The first release should contain 80 to 120 items and should concentrate on validator strength. A balanced seed set can include 25 mathematics-to-Lean items, 25 requirements-to-code items, 25 semantic-parse items, 15 planning items, and 10 science-claim items reserved for reviewed-alignment protocol testing. Ambiguity stress tests should be added after base equivalence regimes reach acceptable reliability.</p>
<p>Table 10. Seed dataset allocation.</p>
<p class="table-display-caption" id="table-10-caption">Table 10. Seed dataset allocation.</p>
<div aria-labelledby="table-10-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="10" id="table-10"><caption class="visually-hidden">Table 10. Seed dataset allocation.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Domain</strong></th>
<th scope="col"><strong>Seed items</strong></th>
<th scope="col"><strong>Primary equivalence regime</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mathematics to Lean</td>
<td>25</td>
<td>Formal theorem equivalence or implication plus reviewed source alignment.</td>
</tr>
<tr class="even">
<td>Requirements to code</td>
<td>25</td>
<td>Executable specification, property tests, counterexample generation.</td>
</tr>
<tr class="odd">
<td>Semantic parsing</td>
<td>25</td>
<td>Logical, denotational, graph, or query-result equivalence.</td>
</tr>
<tr class="even">
<td>Planning</td>
<td>15</td>
<td>Plan validity, precondition satisfaction, resource constraints, authority constraints.</td>
</tr>
<tr class="odd">
<td>Science claims</td>
<td>10</td>
<td>Layered review of protocol assumptions, evidence status, and permitted claim.</td>
</tr>
</tbody>
</table></div>
<h2 id="annotation-and-evaluation-protocol">11. Annotation and evaluation protocol</h2>
<p>The annotation protocol must force every benchmark item to expose the square. A prompt and an expected answer are insufficient. The record must include the source transformation, the corresponding target operation, the equivalence regime, the validator, and the expected failure sensitivities.</p>
<p>Table 11. Annotation protocol.</p>
<p class="table-display-caption" id="table-11-caption">Table 11. Annotation protocol.</p>
<div aria-labelledby="table-11-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="11" id="table-11"><caption class="visually-hidden">Table 11. Annotation protocol.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Step</strong></th>
<th scope="col"><strong>Action</strong></th>
<th scope="col"><strong>Acceptance criterion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Write source object x.</td>
<td>The object is expressible in E_s and has a target transport task.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Choose source transformation f.</td>
<td>The transformation has a clear semantic effect and a named family.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Define translation T.</td>
<td>The target environment and object class are explicit.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Define target transformation g.</td>
<td>The operation corresponds to f and can be applied to T(x).</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Set equivalence regime epsilon.</td>
<td>Validator, acceptance rule, reviewer protocol, and adjudication rule are explicit.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Run both paths.</td>
<td>Outputs are stored separately and locally validated.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Judge path agreement.</td>
<td>The comparison uses epsilon and records failure labels.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Record repair.</td>
<td>Automated or reviewer repair trace identifies the minimal useful fix.</td>
</tr>
</tbody>
</table></div>
<p>Evaluation reports must separate local validity from path agreement. A system with invalid target artifacts cannot be judged cleanly for structure preservation until invalid outputs are filtered or repaired. A system with high local validity and low path agreement supplies the strongest evidence for the benchmark, since the failure appears only after the square is evaluated.</p>
<h2 id="minimal-pilot-plan">12. Minimal pilot plan</h2>
<p>The pilot should answer whether the commutation-square record exposes important failures missed by local evaluation. The study should compare local accuracy, robustness-style perturbation tests, and path agreement on the same seed items. It should also include ablations for direct generation, two-path generation, and type-first generation with explicit target type, assumptions, transformation, and equivalence regime.</p>
<p>Table 12. Minimal pilot phases.</p>
<p class="table-display-caption" id="table-12-caption">Table 12. Minimal pilot phases.</p>
<div aria-labelledby="table-12-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="12" id="table-12"><caption class="visually-hidden">Table 12. Minimal pilot phases.</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Phase</strong></th>
<th scope="col"><strong>Work product</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P1</td>
<td>Build 80 to 120 seed items across four validator-centered domains and one science review track.</td>
</tr>
<tr class="even">
<td>P2</td>
<td>Define both paths and the equivalence regime before model evaluation.</td>
</tr>
<tr class="odd">
<td>P3</td>
<td>Evaluate at least three model families or prompting conditions.</td>
</tr>
<tr class="even">
<td>P4</td>
<td>Report local validity, path agreement, failure labels, repair cost, and diagnostic novelty.</td>
</tr>
<tr class="odd">
<td>P5</td>
<td>Measure annotator agreement on all reviewed-alignment items.</td>
</tr>
<tr class="even">
<td>P6</td>
<td>Release schemas, validators, example cards, and failure-label scripts before increasing scale.</td>
</tr>
</tbody>
</table></div>
<h2 id="objections-and-operational-responses">13. Objections and operational responses</h2>
<p>The main objections concern novelty, annotation cost, subjective equivalence, and domain specificity. These objections should be treated as design constraints. A benchmark that cannot distinguish itself from robustness, cannot specify reliable equivalence regimes, or cannot produce actionable failure labels has not earned expansion.</p>
<p>Table 13. Objections, responses, and tests.</p>
<p class="table-display-caption" id="table-13-caption">Table 13. Objections, responses, and tests.</p>
<div aria-labelledby="table-13-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="13" id="table-13"><caption class="visually-hidden">Table 13. Objections, responses, and tests.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Objection</strong></th>
<th scope="col"><strong>Operational response</strong></th>
<th scope="col"><strong>Required test</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ordinary robustness already covers this.</td>
<td>Robustness measures stability; this benchmark measures structured covariance under a typed transformation.</td>
<td>Show path failures absent from perturbation tests.</td>
</tr>
<tr class="even">
<td>Compositional generalization already covers this.</td>
<td>Existing benchmarks motivate the problem; the added object is the source-target path-agreement record.</td>
<td>Show that the record localizes failures.</td>
</tr>
<tr class="odd">
<td>The category-theoretic frame is optional.</td>
<td>Retain the frame only where it clarifies artifacts, transformations, transport, and commutation.</td>
<td>Compare annotation quality with and without the notation.</td>
</tr>
<tr class="even">
<td>Approximate equality is subjective.</td>
<td>Use reviewed alignment only with rubric, agreement metric, and adjudication.</td>
<td>Report reliability and disagreement categories.</td>
</tr>
<tr class="odd">
<td>The benchmark is expensive.</td>
<td>Start with a small validator-driven release and measure diagnostic novelty.</td>
<td>Compute failure labels unique to the square.</td>
</tr>
<tr class="even">
<td>Models can exploit format regularities.</td>
<td>Hold out transformation families and use counterexample-based validators where possible.</td>
<td>Measure transfer to unseen transformation families.</td>
</tr>
<tr class="odd">
<td>Domain specificity limits generality.</td>
<td>Initial specificity is required for valid equivalence regimes.</td>
<td>Earn cross-domain scope through repeated instantiation.</td>
</tr>
</tbody>
</table></div>
<h2 id="failure-modes-and-kill-criteria">14. Failure modes and kill criteria</h2>
<p>The proposal should be rejected, narrowed, or delayed when the benchmark fails to add diagnostic information at acceptable annotation cost. These decision rules should be applied before a larger research program is built around the square.</p>
<p>Table 14. Failure modes and decisions.</p>
<p class="table-display-caption" id="table-14-caption">Table 14. Failure modes and decisions.</p>
<div aria-labelledby="table-14-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="14" id="table-14"><caption class="visually-hidden">Table 14. Failure modes and decisions.</caption>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure mode</strong></th>
<th scope="col"><strong>Adverse evidence</strong></th>
<th scope="col"><strong>Decision</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F1</td>
<td>Path agreement adds no failure labels beyond local accuracy.</td>
<td>Retire or narrow the benchmark.</td>
</tr>
<tr class="even">
<td>F2</td>
<td>Annotators cannot define target-side transformations reliably.</td>
<td>Remove the domain or redesign transformation families.</td>
</tr>
<tr class="odd">
<td>F3</td>
<td>Equivalence regimes depend on vague review intuition.</td>
<td>Postpone reviewed-alignment tracks.</td>
</tr>
<tr class="even">
<td>F4</td>
<td>Commutation failures are mostly cosmetic.</td>
<td>Redesign item construction and validators.</td>
</tr>
<tr class="odd">
<td>F5</td>
<td>The notation improves presentation without improving evaluation.</td>
<td>Use plain commutation-test terminology.</td>
</tr>
<tr class="even">
<td>F6</td>
<td>Models improve through format matching and retain semantic failures.</td>
<td>Strengthen validators and hold out transformation families.</td>
</tr>
<tr class="odd">
<td>F7</td>
<td>The benchmark works only in formal domains.</td>
<td>Constrain claims to formal and executable settings.</td>
</tr>
<tr class="even">
<td>F8</td>
<td>Review cost exceeds diagnostic gain.</td>
<td>Reduce reviewed items or automate stronger validators.</td>
</tr>
</tbody>
</table></div>
<p>Table 15. Kill criteria.</p>
<p class="table-display-caption" id="table-15-caption">Table 15. Kill criteria. — Criterion, Decision rule</p>
<div aria-labelledby="table-15-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="15" id="table-15"><caption class="visually-hidden">Table 15. Kill criteria. — Criterion, Decision rule</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
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
<td>Path agreement correlates almost perfectly with local validity and adds no new failure labels.</td>
</tr>
<tr class="even">
<td>K2</td>
<td>Annotators cannot reliably define target-side transformations for a core domain.</td>
</tr>
<tr class="odd">
<td>K3</td>
<td>Equivalence regimes rely on reviewer intuition without acceptable agreement.</td>
</tr>
<tr class="even">
<td>K4</td>
<td>Repair traces show that most failures are formatting or presentation artifacts.</td>
</tr>
<tr class="odd">
<td>K5</td>
<td>The benchmark cannot distinguish models, prompts, or system designs beyond noise.</td>
</tr>
<tr class="even">
<td>K6</td>
<td>The framework recommends the same evaluation independent of domain structure.</td>
</tr>
<tr class="odd">
<td>K7</td>
<td>Reviewers cannot use the failure labels to guide repair.</td>
</tr>
</tbody>
</table></div>
<h2 id="conclusion">15. Conclusion</h2>
<p>Functorial Consistency defines a testable evaluation object for structure-preserving AI. The commutation square asks whether generated artifacts preserve declared relations across source transformations, target transports, and target-side operations. Its scientific value depends on explicit equivalence regimes, validator strength, failure localization, and diagnostic novelty beyond local correctness.</p>
<p>The strongest version of the proposal is deliberately bounded. It does not rely on category-theoretic authority, and it does not require every task to admit a fully formal structure. It requires explicit artifacts, transformations, transports, validators, and repair labels. That requirement makes the benchmark expensive, but it also makes the proposal falsifiable.</p>
<p>This essay supplies the evaluation core of the Compositional Intelligence series. Semantic Participation specifies when artifacts qualify for membership in structured environments, and Typed Generativity specifies how candidate artifacts are constructed. Functorial Consistency tests whether those candidates preserve the relations that justify reuse, review, and downstream action.</p>
<h2 id="appendix-a.-compact-benchmark-card-template">Appendix A. Compact benchmark card template</h2>
<p>Table A1. Benchmark card template.</p>
<p class="table-display-caption" id="table-16-caption">Table A1. Benchmark card template.</p>
<div aria-labelledby="table-16-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="16" id="table-16"><caption class="visually-hidden">Table A1. Benchmark card template.</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Field</strong></th>
<th scope="col"><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ID</td>
<td>Stable benchmark identifier.</td>
</tr>
<tr class="even">
<td>Domain</td>
<td>Benchmark domain.</td>
</tr>
<tr class="odd">
<td>Source environment</td>
<td>E_s.</td>
</tr>
<tr class="even">
<td>Target environment</td>
<td>E_t.</td>
</tr>
<tr class="odd">
<td>Source object x</td>
<td>Artifact before transformation.</td>
</tr>
<tr class="even">
<td>Source transformation f</td>
<td>Source-side operation.</td>
</tr>
<tr class="odd">
<td>Transformation family</td>
<td>Controlled family label.</td>
</tr>
<tr class="even">
<td>Translation task T</td>
<td>Source-to-target transport.</td>
</tr>
<tr class="odd">
<td>Target transformation g</td>
<td>Target-side corresponding operation.</td>
</tr>
<tr class="even">
<td>Equivalence regime epsilon</td>
<td>Acceptance relation.</td>
</tr>
<tr class="odd">
<td>Validator or review protocol</td>
<td>Decision procedure.</td>
</tr>
<tr class="even">
<td>Expected correct path relation</td>
<td>Expected agreement.</td>
</tr>
<tr class="odd">
<td>Known traps</td>
<td>Likely failure modes.</td>
</tr>
<tr class="even">
<td>Failure labels</td>
<td>Labels used for diagnosis.</td>
</tr>
<tr class="odd">
<td>Repair guidance</td>
<td>Useful repair procedure.</td>
</tr>
</tbody>
</table></div>
<h2 id="appendix-b.-worked-benchmark-cards">Appendix B. Worked benchmark cards</h2>
<p>Table B1. Worked benchmark cards.</p>
<p class="table-display-caption" id="table-17-caption">Table B1. Worked benchmark cards.</p>
<div aria-labelledby="table-17-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="17" id="table-17"><caption class="visually-hidden">Table B1. Worked benchmark cards.</caption>
<colgroup>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>ID</strong></th>
<th scope="col"><strong>Domain</strong></th>
<th scope="col"><strong>Square</strong></th>
<th scope="col"><strong>Equivalence regime</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A1</td>
<td>Math to Lean</td>
<td>Specialize a compact-domain maximum theorem before formalization, then compare with formalize-then-specialize.</td>
<td>Formal implication or theorem equivalence, plus reviewed informal alignment.</td>
</tr>
<tr class="even">
<td>B1</td>
<td>Requirements to code</td>
<td>Add order preservation and idempotence before implementation, then compare with implementation plus target-side property tests.</td>
<td>Executable behavior under reference properties and generated counterexamples.</td>
</tr>
<tr class="odd">
<td>C1</td>
<td>Semantic parse</td>
<td>Resolve quantifier scope in the source, then compare with logical-form normalization after parsing.</td>
<td>Logical or denotational equivalence over controlled models.</td>
</tr>
<tr class="even">
<td>D2</td>
<td>Planning</td>
<td>Add human approval before external transmission, then compare with plan-side insertion of an approval gate.</td>
<td>Precondition and authority-constraint satisfaction.</td>
</tr>
<tr class="odd">
<td>E2</td>
<td>Science claim</td>
<td>Move from simulation-derived result to empirical-claim requirement, then compare with claim-record epistemic-type change.</td>
<td>Epistemic-type preservation and expert review.</td>
</tr>
</tbody>
</table></div>
<h2 id="appendix-c.-reviewer-rubric-for-reviewed-alignment">Appendix C. Reviewer rubric for reviewed alignment</h2>
<p>Table C1. Reviewed-alignment rubric.</p>
<p class="table-display-caption" id="table-18-caption">Table C1. Reviewed-alignment rubric.</p>
<div aria-labelledby="table-18-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="18" id="table-18"><caption class="visually-hidden">Table C1. Reviewed-alignment rubric.</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Rubric dimension</strong></th>
<th scope="col"><strong>Review question</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Source meaning alignment</td>
<td>Does the target preserve the intended source claim, task, or protocol.</td>
</tr>
<tr class="even">
<td>Transformation fidelity</td>
<td>Does f introduce exactly the intended change.</td>
</tr>
<tr class="odd">
<td>Target-side correspondence</td>
<td>Does g implement the same change in E_t.</td>
</tr>
<tr class="even">
<td>Assumption preservation</td>
<td>Are required assumptions retained or intentionally modified.</td>
</tr>
<tr class="odd">
<td>Generality control</td>
<td>Does the target avoid unintended weakening or overstrengthening.</td>
</tr>
<tr class="even">
<td>Permitted-use control</td>
<td>Does the artifact state the claim or action it is allowed to support.</td>
</tr>
</tbody>
</table></div>
<p>Reviewed alignment should use three decisions, accept, reject, and adjudicate. Reject and adjudicate decisions must include a failure label and a repair note so that review remains connected to benchmark improvement.</p>
<h2 id="appendix-d.-source-notes-and-verification-queue">Appendix D. Source notes and verification queue</h2>
<p>Source-use boundaries should remain explicit. Lean documentation and Theorem Proving in Lean 4 support statements about Lean, dependent type theory, elaboration, and proof checking. LeanDojo supports programmatic interaction with Lean and retrieval-augmented theorem proving infrastructure. SCAN, CFQ, COGS, and SLOG support the compositional-generalization context. FormalBench and ConsistencyChecker support recent transformation-sensitive evaluation context. These sources motivate the evaluation problem; they do not establish Functorial Consistency as proposed here.</p>
<p>The bibliography should be rechecked before submission for 2025 and 2026 sources. The final pass should verify ACL Anthology page ranges, arXiv versions, venue status, official documentation versions, and rapidly moving agent or formal-reasoning sources at the submission date.</p>
<h2 id="appendix-e.-editorial-changes-from-v0.2-to-v0.3">Appendix E. Editorial changes from v0.2 to v0.3</h2>
<p>Table E1. Revision summary.</p>
<p class="table-display-caption" id="table-19-caption">Table E1. Revision summary. — Area, Revision</p>
<div aria-labelledby="table-19-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="19" id="table-19"><caption class="visually-hidden">Table E1. Revision summary. — Area, Revision</caption>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Area</strong></th>
<th scope="col"><strong>Revision</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Opening</td>
<td>The paper opens with the evaluation object and states claim status before the abstract.</td>
</tr>
<tr class="even">
<td>Paragraph architecture</td>
<td>List-like exposition has been replaced with developmental paragraphs and diagnostic cases.</td>
</tr>
<tr class="odd">
<td>Equivalence regimes</td>
<td>The acceptance relation is treated as the governing audit field for every square.</td>
</tr>
<tr class="even">
<td>Domain examples</td>
<td>Examples have been reduced to one diagnostic case per domain.</td>
</tr>
<tr class="odd">
<td>Benchmark schema</td>
<td>Item and output records have been converted into implementation-facing tables.</td>
</tr>
<tr class="even">
<td>Failure protocol</td>
<td>Failure modes and kill criteria now function as operational decision rules.</td>
</tr>
<tr class="odd">
<td>Claim policy</td>
<td>The benchmark remains a proposed design, with no reported result.</td>
</tr>
</tbody>
</table></div>
