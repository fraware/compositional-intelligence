# Functorial Consistency

*Mateo Petel*

## Abstract

Functorial Consistency evaluates AI-generated artifacts by path agreement under structured transformation. The object of evaluation is a commutation-square item containing a source object, a source-side transformation, a translation or semantic transport, a corresponding target-side transformation, an equivalence regime, and a validator. The benchmark asks whether transform-then-translate agrees with translate-then-transform according to the acceptance relation declared for the target environment.

The proposal addresses a failure mode that local correctness obscures. A generated proof, program, semantic representation, plan, or claim record can validate locally and still lose an assumption, alter generality, change target type, ignore an added constraint, or satisfy a validator that measures the wrong relation. Functorial Consistency makes such failures observable by comparing two typed paths through the same transformation problem.

The contribution is a benchmark specification, not an empirical result. The essay distinguishes Functorial Consistency from accuracy, robustness, self-consistency, metamorphic testing, and standard compositional generalization <span class="citation-group">[<a class="citation-link" href="#ref-FormalBench2025" aria-label="Reference 1 — Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference">1</a>, <a class="citation-link" href="#ref-ConsistencyChecker2025" aria-label="Reference 2 — ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities">2</a>, <a class="citation-link" href="#ref-ChenEtAl2018Metamorphic" aria-label="Reference 3 — Metamorphic Testing: A Review of Challenges and Opportunities">3</a>]</span>. It then gives domain instantiations, equivalence regimes, metrics, failure labels, annotation procedures, a minimal pilot plan, and kill criteria. The proposal earns scientific value only if commutation-square records reveal actionable failures beyond local validity and ordinary perturbation tests.

Table 1. Contribution summary.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Contribution</strong></th>
<th><strong>Technical content</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C1</td>
<td>Benchmark unit</td>
<td>The typed item records E_s, E_t, x, f, T=(T_0,T_1), g, acceptance relation R and validator V.</td>
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
</table>



## 1. Evaluation object {#1-evaluation-object}

Functorial Consistency proposes a typed two-path test. For x in X, a source transformation f : X -> X′, transports T_0 : X -> Y and T_1 : X′ -> Y′, and target transformation g : Y -> Y′, both T_1(f(x)) and g(T_0(x)) inhabit Y′. The declared relation R is a subset of Y′ × Y′ with an explicit operand order, including directional refinement where appropriate. The evaluation record distinguishes invalid item, unavailable path, unknown relation, false relation, and true relation, with oracle provenance and applicable coverage denominators. A false relation is a determined counterexample to that item’s proposed comparison; unknown indicates insufficient evidence under the declared oracle. Finite square results are separate from quantified identity and composition preservation laws for any claimed functor.

> Source path: x ∈ X ---f→ f(x) ∈ X′. Transports: T_0 : X → Y and T_1 : X′ → Y′. Target path: T_0(x) ∈ Y ---g→ g(T_0(x)) ∈ Y′. Evaluation compares T_1(f(x)) R g(T_0(x)) in Y′ under the declared relation R and its evaluator. A relation result presupposes that the two paths are defined and locally valid.

The square is an operational item-level comparison of two well-typed paths, not by itself a theorem of mathematical functoriality. An item declares its source and target environments, source object, source operation, two transports, target-side operation, comparison relation and its orientation, and independently auditable validators. Item formation and local path validation precede comparison of T_1(f(x)) with g(T_0(x)). Invalid or undefined paths, demonstrated disagreement, and unresolved comparison evidence receive different labels. A directional refinement relation need not be symmetric. Formal functoriality would additionally specify categories and mappings preserving identities and composition; the present benchmark tests selected path agreements.

For stochastic transports, each evaluation item declares its statistical estimand. Under a pathwise estimand, specify a justified joint coupling of both path outputs and estimate the probability of R under that coupling. Shared nominal random seeds alone do not establish a valid coupling. Under a distributional estimand with a measurable deterministic target map g, compare the law of T_1(f(x)) with g_#Law(T_0(x)) using a prespecified metric or test. For a randomized target operation g, use the law induced by its declared transition kernel in place of a deterministic pushforward. Equal marginal laws do not entail pathwise agreement for arbitrary couplings. Report sampling budgets, seeds, dependence assumptions, invalid outputs, missing paths, validator uncertainty, and sampling uncertainty separately. The deterministic square is the point-mass case. Neither evaluation outcome alone establishes the identity or composition laws of a functor.

Commutation establishes agreement only relative to the supplied relation and validator. Constant transports into a single target object, for example, yield commuting squares despite losing source distinctions. An evaluation item must separately record source-to-target adequacy, freeze source and target operations and acceptance criteria before observing model outputs, and test for degeneracy using independently specified controls. A defective benchmark specification is an invalid_item, and a fixture awaiting a decisive eligibility check is an unresolved_item. A generated object decisively failing a local validator is an invalid_candidate, while an inconclusive local check is unresolved_local_validity. Report locally valid-pair coverage, relation-adjudication coverage, conditional relation agreement, relation-pass yield over eligible attempts, and the stricter joint relation-and-independent-adequacy yield. A commuting pair that fails source adequacy contributes to relation-pass yield and fails the joint adequacy criterion. Invalid benchmark items are separately counted and excluded from model-performance denominators.


Every comparison declares the target relation, its direction and the validator. Formal settings distinguish definitional equality, logical equivalence, implication and refinement. Executable settings distinguish tested behavioral agreement from proved properties. In semantic parsing and planning, the relation is specified through denotation, goal satisfaction, preconditions, effects and resource obligations. A reviewer-based comparison records a rubric, adjudication and uncertainty. Negative and positive controls test whether the validator discriminates the intended relation.

## 2. Position within the Compositional Intelligence series {#2-position-within-the-compositional-intelligence-series}

Functorial Consistency supplies the transformation test for the first three layers of the series. Semantic Participation specifies membership conditions for artifacts in structured environments. Typed Generativity specifies how a model infers a target object and constructs a candidate inhabitant. Functorial Consistency then tests whether the candidate artifact maintains the relation that connects it to source transformations and target operations.

The test constrains the later layers by requiring each extension to state its preserved structure. A language extension must state which semantic relation should commute under paraphrase or scope transformation. An architecture extension must state which task transformations a model family supports. A warrant layer must state how scores relate to validation, repair, or epistemic status. An action layer must state how traces preserve preconditions, postconditions, authority, and permitted effects.

This role also limits the claim. The essay does not assert that all AI evaluation reduces to commutation. It identifies a class of failures that arise when an artifact moves between representations or environments under a structured change. The benchmark should be used where a corresponding target-side operation and an acceptance relation can be stated with enough precision for annotation and repair.

## 3. Formal status of the square {#3-formal-status-of-the-square}

The commutation square uses category-theoretic notation as an operational control on evaluation design. Objects, transformations, transports, and path agreement force the benchmark author to specify both routes through the task. The notation contributes only if it improves item construction, failure localization, annotation reliability, and repair guidance.

The benchmark needs well-formed source and target artifacts, composable paths and a declared acceptance procedure. Its proposed evaluation unit applies to proof assistants, software systems, parsers, planning environments and scientific workflows equipped with task-specific validators. A stronger category-theoretic model would separately introduce source and target categories, identity maps, composition and a functor preserving those operations. The proposed benchmark evaluates selected path agreements; its practical adequacy is established through annotation and comparative testing.

Table 2. Minimal FunctorialConsistencyItem fields.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Required annotation</strong></th>
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
<td>R</td>
<td>Equivalence or acceptance regime</td>
<td>Relation used to compare the two target artifacts.</td>
</tr>
<tr class="even">
<td>V</td>
<td>Validator or review protocol</td>
<td>Formal checker, executable test, denotational comparison, constraint checker, or reviewer rubric.</td>
</tr>
</tbody>
</table>



## 4. Equivalence regimes {#4-equivalence-regimes}

The equivalence regime is the benchmark field that prevents path agreement from collapsing into impressionistic similarity. It states which relation the two target artifacts must satisfy and which procedure decides that relation. A dataset mixing formal proof equivalence, executable behavior, denotation, constraint satisfaction, and expert review must label those regimes separately.

Table 3. Equivalence regimes for path-agreement evaluation.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Regime</strong></th>
<th><strong>Acceptance relation</strong></th>
<th><strong>Validator</strong></th>
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
</table>



Reviewed alignment is admissible only when stronger validators are unavailable or incomplete. The review protocol must specify the rubric, reviewer expertise, agreement metric, adjudication rule, and accepted failure labels. An item that hides expert judgment behind the symbol epsilon is underspecified and should be excluded from early benchmark releases.

Layered equivalence is often necessary in high-value domains. Mathematics-to-Lean can require formal equivalence between target statements and reviewed alignment between the informal claim and the formal statement. Scientific artifact transport can require workflow validity, statistical-assumption review, and epistemic-type control. Agent plans can require goal satisfaction, effect checking, and authority review in a single item.

## 5. Relation to adjacent evaluation families {#5-relation-to-adjacent-evaluation-families}

The relevant antecedents include compositional-generalization tests, metamorphic relations <span class="citation-group">[<a class="citation-link" href="#ref-ChenEtAl2018Metamorphic" aria-label="Reference 3 — Metamorphic Testing: A Review of Challenges and Opportunities">3</a>]</span> and reversible-transformation consistency. FormalBench evaluates formal-specification consistency, completeness proxies, transformation robustness, and repair, with success/failure/unknown verification outcomes; ConsistencyChecker evaluates reversible-transformation paths using similarity-based consistency scores <span class="citation-group">[<a class="citation-link" href="#ref-FormalBench2025" aria-label="Reference 1 — Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference">1</a>, <a class="citation-link" href="#ref-ConsistencyChecker2025" aria-label="Reference 2 — ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities">2</a>]</span>. The proposed contribution is a typed source-to-target record with the two transport paths, an explicit directional acceptance relation, independently specified adequacy checks, validator evidence, and observed failure-location labels. A single failed square does not identify a unique causal fault; causal attribution needs controlled interventions or independently established fault provenance. Incremental diagnostic and repair value must be assessed against task-matched comparator methods and an information-matched structured-record baseline.

Table 4. Distinction from adjacent evaluation families.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Evaluation family</strong></th>
<th><strong>Primary question</strong></th>
<th><strong>Additional requirement introduced here</strong></th>
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
</table>



The benchmark should be narrowed if path agreement merely reproduces the ranking obtained from local validity or standard robustness tests. The intended diagnostic gain appears when two target artifacts validate locally, but the square exposes assumption loss, unintended weakening, overstrengthening, type drift, or constraint mention without operative integration.

## 6. Benchmark domains {#6-benchmark-domains}

The initial benchmark should prioritize domains where validators can be made explicit. Mathematics-to-Lean, requirements-to-code, semantic parsing, and planning supply target environments with formal, executable, denotational, or constraint-based checks. Science-facing claim transport is central to the series, but its early use should be limited to a reviewed-alignment track until annotation reliability has been measured.

### 6.1 Informal mathematics to Lean {#6-1-informal-mathematics-to-lean}

Mathematical formalization provides the cleanest starting point for path-agreement evaluation. The target environment can check formal artifacts, and the remaining difficulty is source-target alignment. A Lean theorem can pass the kernel and still represent a weakened, overstrengthened, or misdirected version of the informal source claim.

A diagnostic item can use maximum attainment as the source relation. One path specializes an informal compact-domain theorem to a closed interval and then formalizes it. The other path formalizes the general theorem and specializes the resulting target statement. Agreement requires a formal relation inside Lean, together with reviewed alignment confirming that the target still expresses attainment by a witness point and not merely existence of a supremum. The item therefore tests formal validity and alignment loss in a single square.

### 6.2 Natural-language requirements to code {#6-2-natural-language-requirements-to-code}

Requirements-to-code tasks expose path failures through executable specifications. A requirement transformation often adds a behavioral constraint that a model can mention in comments, handle for a narrow case, or omit from the operative implementation. Path comparison separates code that passes simple examples from code that satisfies the transformed specification.

An order-preserving deduplication item illustrates the mechanism. The source transformation adds idempotence and generic element handling to the original order-preservation requirement. The target-side operation adds property tests for first-occurrence order, repeated application, and element generality. Agreement is executable when both paths satisfy the same reference properties and counterexample suite. A failure in this item identifies constraint integration, interface drift, or behavioral overfitting more precisely than local tests alone.

### 6.3 Natural language to semantic parse {#6-3-natural-language-to-semantic-parse}

Semantic parsing is suited to controlled transformation families. The source side can vary paraphrase, quantifier scope, attachment, lexical choice, or representation format, and the target side can compare logical form, denotation, graph structure, or query result. Early items should avoid open-ended paraphrase and use transformations whose semantic effect is annotated before model evaluation.

A quantifier-scope item gives the benchmark a clear target relation. The source transformation fixes an existential wide-scope reading before parsing. The target-side operation normalizes the produced logical form to that selected scope. Path agreement is decided through logical or denotational equivalence over controlled models, so the benchmark tests whether surface transformations alter the represented meaning in the intended direction.

### 6.4 Goals to plans {#6-4-goals-to-plans}

Planning items test whether source-side constraint changes lead to target-side plan changes with operative effects. A locally successful final state can conceal missing preconditions, resource conflicts, approval dependencies, or unintended side effects. Path agreement therefore requires both goal satisfaction and trace-level constraint satisfaction.

A human-approval item supplies a compact diagnostic case. The source transformation requires approval before external transmission of a report. The target-side operation inserts the approval request and prevents the send step until approval is recorded. Agreement requires precondition satisfaction, effect-trace validation, and authority-boundary review. A plan that reaches the final state without the gate fails the square despite apparent task completion.

### 6.5 Scientific protocols to claims {#6-5-scientific-protocols-to-claims}

Science-facing items require layered review in domains where formal equivalence is unavailable. Protocol transformations can add controls, alter uncertainty assumptions, impose stopping rules, or restrict permitted claims. The target artifact is often a claim record whose epistemic type must match the available evidence.

A simulation-to-empirical item tests warrant preservation. The source artifact is a simulation-derived stability result. The source transformation adds empirical measurement requirements. The target-side transformation changes the claim record so that empirical support is granted only after measurement evidence is present. Agreement is judged through epistemic-type preservation and expert review of evidence status. This track should remain small until reviewed-alignment protocols reach acceptable reliability.

## 7. Transformation families {#7-transformation-families}

A transformation family is admissible only when it has a meaningful source-side operation and a corresponding target-side operation. Arbitrary perturbations weaken the benchmark, since path agreement depends on typed transformations whose semantic effect can be checked or reviewed. The first dataset should therefore use a small controlled set before expanding to richer transformations.

Table 5. Controlled transformation families.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Family</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Initial domains</strong></th>
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
</table>



A transformation family should be removed from the initial release if annotators cannot define the corresponding target-side operation. This rule is stricter than ordinary perturbation design and is central to the benchmark. The transformation must induce a checkable target-side relation.

## 8. Metrics {#8-metrics}

Functorial Consistency requires diagnostic metrics in place of a single aggregate score. Local validity and path agreement measure different properties. High local validity with low path agreement indicates instability under the tested transformation family and acceptance relation. Broader reliability needs independent evidence. High path agreement on trivial transformations provides insufficient evidence of performance on more demanding items.

Table 6. Recommended metrics.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Metric</strong></th>
<th><strong>Question</strong></th>
<th><strong>Signal</strong></th>
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
<td>Do the two target artifacts satisfy the relation R under validator V.</td>
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
</table>



Diagnostic novelty is the decisive pilot statistic. If commutation items produce no new failure labels beyond local validity, the benchmark should be narrowed. If the square reveals assumption loss, generality collapse, target-type drift, validator mismatch, or constraint failure, the added annotation cost has a concrete evaluation function.

## 9. Failure taxonomy {#9-failure-taxonomy}

The failure taxonomy identifies possible fault locations in a failed square. Path disagreement alone does not determine which component is responsible. Attribution to the source item, source transformation, translation, target transformation, equivalence regime, or validator needs local validation, controlled interventions, or independent fault provenance.

Table 7. Failure labels and repair implications.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure label</strong></th>
<th><strong>Definition</strong></th>
<th><strong>Repair implication</strong></th>
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
<td>Both paths validate locally and fail the declared relation R.</td>
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
</table>



## 10. Functorial Consistency Bench v0.3 {#10-functorial-consistency-bench-v0-3}

A first benchmark release should be small, explicit, and validator-driven. Its purpose is to test the diagnostic value of the square, not to claim broad coverage. Each item must expose both paths and must declare the acceptance relation before any model output is evaluated.

### 10.1 Benchmark item schema {#10-1-benchmark-item-schema}

Table 8. Benchmark item schema.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Type or value</strong></th>
<th><strong>Purpose</strong></th>
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
</table>



### 10.2 Model-output schema {#10-2-model-output-schema}

Table 9. Model-output record.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 49%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Purpose</strong></th>
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
<td>Records T_1(f(x)).</td>
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
<td>Records the decision under R and V.</td>
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
</table>



### 10.3 Dataset design {#10-3-dataset-design}

The first release should contain 80 to 120 items and should concentrate on validator strength. A balanced seed set can include 25 mathematics-to-Lean items, 25 requirements-to-code items, 25 semantic-parse items, 15 planning items, and 10 science-claim items reserved for reviewed-alignment protocol testing. Ambiguity stress tests should be added after base equivalence regimes reach acceptable reliability.

Table 10. Seed dataset allocation.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Domain</strong></th>
<th><strong>Seed items</strong></th>
<th><strong>Primary equivalence regime</strong></th>
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
</table>



## 11. Annotation and evaluation protocol {#11-annotation-and-evaluation-protocol}

The annotation protocol must force every benchmark item to expose the square. A prompt and an expected answer are insufficient. The record must include the source transformation, the corresponding target operation, the equivalence regime, the validator, and the expected failure sensitivities.

Table 11. Annotation protocol.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
<th><strong>Acceptance criterion</strong></th>
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
<td>Set the comparison relation R and validator V.</td>
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
<td>The comparison uses R and V and records failure labels.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Record repair.</td>
<td>Automated or reviewer repair trace identifies the minimal useful fix.</td>
</tr>
</tbody>
</table>



Evaluation reports must separate local validity from path agreement. Invalid candidate artifacts and inconclusive local validations receive distinct outcomes and remain in the eligible-attempt denominator. Structure-preservation agreement is reported on locally valid, relation-adjudicable pairs alongside valid-pair rate, relation-pass yield, independent adequacy verdicts, and joint relation-and-adequacy yield; ineligible fixtures and their rates are reported separately. A system with high local validity and low path agreement supplies the strongest evidence for the benchmark, since the failure appears only after the square is evaluated.

## 12. Minimal pilot plan {#12-minimal-pilot-plan}

The pilot should answer whether the commutation-square record exposes important failures missed by local evaluation. The study should compare local accuracy, robustness-style perturbation tests, and path agreement on the same seed items. It should also include ablations for direct generation, two-path generation, and type-first generation with explicit target type, assumptions, transformation, and equivalence regime.

Table 12. Minimal pilot phases.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Phase</strong></th>
<th><strong>Work product</strong></th>
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
</table>



## 13. Objections and operational responses {#13-objections-and-operational-responses}

The main objections concern novelty, annotation cost, subjective equivalence, and domain specificity. These objections should be treated as design constraints. A benchmark that cannot distinguish itself from robustness, cannot specify reliable equivalence regimes, or cannot produce actionable failure labels has not earned expansion.

Table 13. Objections, responses, and tests.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Objection</strong></th>
<th><strong>Operational response</strong></th>
<th><strong>Required test</strong></th>
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
</table>



## 14. Failure modes and kill criteria {#14-failure-modes-and-kill-criteria}

The proposal should be rejected, narrowed, or delayed when the benchmark fails to add diagnostic information at acceptable annotation cost. These decision rules should be applied before a larger research program is built around the square.

Table 14. Failure modes and decisions.



<table>
<colgroup>
<col style="width: 33%"/>
<col style="width: 33%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Failure mode</strong></th>
<th><strong>Adverse evidence</strong></th>
<th><strong>Decision</strong></th>
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
</table>



Table 15. Kill criteria.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
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
</table>



## 15. Conclusion {#15-conclusion}

Functorial Consistency defines a testable evaluation object for structure-preserving AI. The commutation square asks whether generated artifacts preserve declared relations across source transformations, target transports, and target-side operations. Its scientific value depends on explicit equivalence regimes, validator strength, failure localization, and diagnostic novelty beyond local correctness.

The strongest version of the proposal is deliberately bounded. It does not rely on category-theoretic authority, and it does not require every task to admit a fully formal structure. It requires explicit artifacts, transformations, transports, validators, and repair labels. That requirement makes the benchmark expensive, but it also makes the proposal falsifiable.

This essay supplies the evaluation core of the Compositional Intelligence series. Semantic Participation specifies when artifacts qualify for membership in structured environments, and Typed Generativity specifies how candidate artifacts are constructed. Functorial Consistency tests whether those candidates preserve the relations that justify reuse, review, and downstream action.

## Appendix A. Compact benchmark card template {#appendix-a-compact-benchmark-card-template}

Table A1. Benchmark card template.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
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
<td>Relation R and validator V</td>
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
</table>



## Appendix B. Worked benchmark cards {#appendix-b-worked-benchmark-cards}

Table B1. Worked benchmark cards.



<table>
<colgroup>
<col style="width: 24%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
<col style="width: 25%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Domain</strong></th>
<th><strong>Square</strong></th>
<th><strong>Equivalence regime</strong></th>
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
</table>



## Appendix C. Reviewer rubric for reviewed alignment {#appendix-c-reviewer-rubric-for-reviewed-alignment}

Table C1. Reviewed-alignment rubric.



<table>
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th><strong>Rubric dimension</strong></th>
<th><strong>Review question</strong></th>
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
</table>



Reviewed alignment should use three decisions, accept, reject, and adjudicate. Reject and adjudicate decisions must include a failure label and a repair note so that review remains connected to benchmark improvement.


<section class="bibliography" aria-labelledby="references-heading">
<h2 id="references-heading">References</h2>

<ol class="references-list">
<li id="ref-FormalBench2025"><span class="ref-key">[1]</span> <a href="https://aclanthology.org/2025.acl-long.1068/" rel="noopener noreferrer">Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference</a>. <span class="ref-details">Le-Cong, Le, and Murray · ACL 2025.</span></li>
<li id="ref-ConsistencyChecker2025"><span class="ref-key">[2]</span> <a href="https://aclanthology.org/2025.acl-long.1585/" rel="noopener noreferrer">ConsistencyChecker: Tree-based Evaluation of LLM Generalization Capabilities</a>. <span class="ref-details">Hong, Yu, and You · ACL 2025.</span></li>
<li id="ref-ChenEtAl2018Metamorphic"><span class="ref-key">[3]</span> <a href="https://doi.org/10.1145/3143561" rel="noopener noreferrer">Metamorphic Testing: A Review of Challenges and Opportunities</a>. <span class="ref-details">Chen, Kuo, Liu, Poon, Towey, Tse, and Zhou · ACM Computing Surveys 51(1), 2018, article 4 · DOI:10.1145/3143561.</span></li>
</ol>
</section>
