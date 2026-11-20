# Functorial Consistency

## Abstract

Local validation establishes a property of an AI-generated artifact under a specified checker. It does not establish that a translation respects changes to the task from which the artifact originated. A formally accepted theorem might express a weaker proposition, a functioning program might omit an added requirement, and a plan might reach its goal through a prohibited action. These defects concern correspondence across transformations, even in cases where individual outputs pass their local checks.

*Functorial Consistency* develops a typed protocol for evaluating that correspondence. Given a source transformation, a source-to-target translation, and a corresponding target operation, it compares transform-then-translate with translate-then-transform under an independently specified relation. The record keeps local validity, source alignment, path agreement, and validator adequacy distinct. It also distinguishes a commuting square from the stronger identity and composition laws associated with a functor.

The protocol belongs to metamorphic testing and introduces no new class of logical oracle. Its proposed contribution is methodological: specifying valid relational tests, identifying counterexamples, and attributing failures across representation boundaries. The essay develops the comparison, exhibits a case of misleading agreement, and sets out a controlled evaluation against existing testing workflows. The benchmark and its anticipated benefits have yet to be established empirically.

## 1. The evaluation problem

An informal theorem translated into Lean provides a direct illustration. A proof accepted by the kernel certifies a judgment relative to its formal statement, dependencies, and axioms. The kernel does not decide whether that statement conveys the informal mathematician's intended claim. A proof of the existence of a supremum, for example, does not itself establish attainment by an element of the domain. The validation boundary matters precisely because a generated artifact might be impeccable inside a formal environment while expressing the wrong proposition [1].

Comparable distinctions arise in software and action. A program that passes the original examples might fail a revised requirement. A plan that reaches the prescribed final state might violate an approval obligation added to the task. A scientific claim record might inherit the appearance of empirical support from a simulation. In each case the evaluator needs to examine the relationship linking the initial requirement, its revision, and the artifact produced under that revision.

These evaluations concern distinct obligations. Local acceptance asks whether an artifact satisfies a designated checker. Source adequacy asks whether it expresses the intended task. Transformation compatibility asks whether the source-side change is reflected in the target-side operation. Each judgment needs its own evidence. A locally accepted artifact that violates an independently specified correspondence is an especially informative case.

Within the Compositional Intelligence series, *Semantic Participation* examines admissibility in structured environments, while *Typed Generativity* examines construction under a declared target type. The present essay investigates the stability of that construction under controlled changes. The ambition is restricted to transformations carrying enough semantic structure to support an independent comparison.

## 2. The typed commutation square

Let \(S_0\) and \(S_1\) be spaces of source tasks, and \(Y_0\) and \(Y_1\) the corresponding spaces of target artifacts. Fix a system configuration \(\theta\), including prompts, tools, software versions, and the sampling policy. In the well-typed deterministic case, a benchmark item specifies four maps.

\[
\begin{aligned}
f &: S_0 \longrightarrow S_1,\\
T_\theta^{(0)} &: S_0 \longrightarrow Y_0,\\
T_\theta^{(1)} &: S_1 \longrightarrow Y_1,\\
g_f &: Y_0 \longrightarrow Y_1.
\end{aligned}
\]

Both well-typed routes terminate in \(Y_1\). Their comparison is governed by a declared relation \(R_f\subseteq Y_1\times Y_1\). The arrows describe successful applications on their admissible domains, not a guarantee that an evaluated generator always produces a valid artifact. Failed, timed-out, ill-typed, or inapplicable executions receive separate outcome records. They are retained in the denominator of attempted evaluations and never assigned invented artifacts in \(Y_0\) or \(Y_1\).

\[
\boxed{\quad T_\theta^{(1)}(f(x))\;R_f\;g_f(T_\theta^{(0)}(x))\quad}
\]

The target operation \(g_f\) is specified independently of the evaluated outputs and justified as a counterpart of \(f\). It transforms artifacts, while a separate validator judges the result. Equality yields a strictly commuting square. Semantic equivalence or directed refinement yields a relation-valued compatibility test, with the comparison order fixed in the item specification. Reversing a directed relation changes the claim.

The square separates four questions that are liable to be conflated. First, is \(f\) a coherent source transformation? Second, do the generated objects have the required types and satisfy their local conditions? Third, does \(g_f\) implement the semantic change prescribed by \(f\)? Fourth, do the two resulting artifacts satisfy \(R_f\)? A failing square supplies an observed discrepancy. Attribution to a particular model or test component needs further evidence.

For a stochastic generator, the displayed maps represent sampled realizations conditional on their being well-typed. The agreement rate is defined relative to a declared joint sampling scheme: independently sampled paths and paths with coupled random choices need not have the same agreement probability. Retry rules, inference budgets, and failure handling are fixed in advance. Independent repetitions under an identity or no-change source transformation provide a control for ordinary sampling disagreement. Sample-level agreement differs from equality of output distributions, and one disagreeing pair does not establish a systematic failure across runs.

### 2.1 Compatibility, equivariance, and functoriality

The square expresses a compatibility condition resembling an intertwining or equivariance equation. Translation responds to an operation on its inputs in a way that agrees, under \(R_f\), with the corresponding operation on its outputs. This is the immediate object of measurement. Agreement on one square establishes neither a functor nor coherent target operations for all source transformations.

A functor in the categorical sense assigns target objects and morphisms to source objects and morphisms and preserves identity morphisms and composition [2]. If a family of source transformations forms a category and the target operations are proposed images under a map \(F\), the additional laws have the form

\[
\begin{aligned}
g_{\operatorname{id}_{S_i}} &= \operatorname{id}_{Y_i},\\
g_{f_2\circ f_1} &= g_{f_2}\circ g_{f_1}
\end{aligned}
\]

for every applicable object and composable pair. These are laws of the assignment \(f\mapsto g_f\), distinct from the compatibility of that assignment with the translation maps \(T_\theta^{(i)}\). A categorical claim additionally needs an object mapping, well-defined morphism assignments, and proofs of the relevant laws. The benchmark specifies finite checks of selected instances, not those proofs.

Composition supplies an additional test. For composable source operations \(f_1\) and \(f_2\), compare the target operation assigned to \(f_2\circ f_1\) with the sequential application of \(g_{f_1}\) and \(g_{f_2}\), preserving intermediate types. Agreement of the constituent squares does not, on its own, establish compatibility with the separately assigned operation \(g_{f_2\circ f_1}\). That conclusion also depends on the target-side composition law and, for relation-valued tests, appropriate transitivity and congruence properties. The evaluation must establish those conditions or test the composite directly.

The categorical framing earns its place through this separation of *typing*, *path compatibility*, and *composition*. It provides an audit discipline for specifying which constructions are comparable. It does not derive source fidelity from commutation or confer mathematical authority on a finite collection of successful tests. A study limited to individual squares is accurately described as **transformation-compatibility testing**; the fuller functorial interpretation is a conditional, stronger program.

## 3. A worked square with an observable failure

Consider a system that translates task descriptions into executable plans for preparing and transmitting a report. The original source task \(x\) directs preparation followed by external transmission. The source transformation \(f\) adds the condition that recorded human approval must precede transmission. The target language distinguishes the action of *requesting* approval from the event of *receiving* it.

The independently specified target operation \(g_f\) introduces an approval request and guards each external send action with a report-specific `approval_recorded` predicate. Under the declared action semantics, recorded approval is initially absent, becomes true only through a separate authorized event, and persists until the report is sent. The guard is evaluated at transmission. The two routes produce the following illustrative artifacts.

| Route | Executable control flow |
| --- | --- |
| Transform, then translate | `prepare; request_approval; send` with no approval guard |
| Translate, then transform | `prepare; request_approval; await approval_recorded; send` with `approval_recorded` as a send precondition |

The first route confuses requesting authorization with receiving it. The resulting plan permits `request_approval → send` with no intervening approval event. The second plan excludes that execution, while allowing transmission if the environment records approval. Both plans pass basic syntax and action-type checks, and both have a reachable transmitted-report state under suitable environmental actions. The independent authority specification rejects the first plan, with the unauthorized send as a concrete counterexample.

The safety property is \(\mathbf{G}(\mathrm{send}(r)\Rightarrow\mathrm{approval\_recorded}(r))\), for each report \(r\). Here the state predicate denotes approval already recorded at the point of transmission, not the occurrence of an approval request. The comparison uses the sets of permitted traces projected onto common approval and transmission events, abstracting away internal control steps such as `await`. Those sets differ because the first plan permits unauthorized transmission. The comparison does not infer compliance from an approval-related action name.

An authority-aware local validator applied to the revised task also rejects the first plan. The square adds no logical strength to that oracle. Its hypothesized advantage is explanatory: it ties the missing guard to the transport of a specific source requirement, yielding a targeted repair record. The benefit must justify the additional cost of specifying \(g_f\), the trace projection, and the relation.

A different defect illustrates the opposite danger. Suppose a translation maps every source task to the same inert target artifact, and every assigned target operation leaves that artifact unchanged. The two paths then agree on every tested square, despite the disappearance of all source meaning. Even exact identity and composition behavior on this degenerate output would not establish faithful translation. **Path agreement establishes compatibility of routes under the declared relation. Source adequacy independently establishes correspondence with the intended task.** The benchmark needs both judgments.

## 4. What the acceptance relation must mean

The declared relation is the semantic content of a benchmark item. The validator is a fallible procedure for determining that relation, and its decision must be distinguished from the relation's truth. Every item records the comparison direction, the admissible artifact types, the relevant inputs or traces, and the assumptions under which the judgment is intended. Verdicts include *pass*, *fail*, and *indeterminate*, with separate records for timeouts, inadequate coverage, and unresolved reviews.

| Regime | Declared relation | Evidence and limits |
| --- | --- | --- |
| Formal | Definitional equality, proven equivalence, or directed implication | Kernel checking establishes a formal judgment relative to named assumptions and dependencies; informal-source alignment is separate. |
| Executable | Observational equivalence or trace refinement over a declared domain | Property tests provide sampled evidence; exhaustive checking or proof has a different status. |
| Denotational | Equality of interpretation under a specified semantics | Normalization, decision procedures, or finite-model comparison operate within a defined fragment. |
| Constraint-based | Pairwise refinement or agreement of permitted behaviors under preconditions, effects, resources, and authority conditions | State or trace checks cover the obligation represented by the source change; individual compliance is reported separately. |
| Reviewed | Agreement under an explicit expert rubric | Independent judgments, disagreement statistics, and adjudication bound the reliability of the conclusion. |
| Combined | Conjunction or specified precedence of named obligations | Every subcheck retains its provenance and indeterminate status. |

An asymmetric relation cannot be presented as undirected equality. If \(R_f\) is trace inclusion, a statement that the first plan has fewer behaviors than the second is not interchangeable with its converse. Likewise, mutual satisfaction of a broad constraint might be too weak to establish equivalence. A benchmark must specify whether it tests behavioral equality, refinement, compliance with a shared specification, or some explicitly justified combination.

Three judgments remain distinct. **Local admissibility** concerns well-formedness and basic environmental checks. **Source adequacy** examines correspondence with the task, including revised assumptions and permissions. **Relational compatibility** examines the two routes under \(R_f\). Disagreement across these judgments is informative only if each verdict, oracle, and applicable trust boundary is recorded. Source adequacy is never inferred from successful path agreement.

The comparison also depends on an independently justified \(g_f\). In requirements-to-code evaluation, adding tests changes the validator, not the implementation. A genuine target-side transformation must transform implementations into implementations. If no justified operation exists, the appropriate alternative is a directly specified metamorphic relation on the outputs. Such items belong to a relational-only baseline, not the commutation-square track.

Semantic parsing contains an analogous trap. A target operation that overwrites an incorrect parse with the intended parse would conceal the error. Normalization must be justified as meaning-preserving on its declared domain, or the intervention must be labeled as a repair. Any human adjudication needs an explicit rubric, independent initial judgments, and a record of cases outside the rubric's competence.

## 5. Position relative to prior evaluation

Metamorphic testing specifies relations that a system's outputs are expected to satisfy under related inputs [3]. It already addresses the problem of testing systems without a complete individual-output oracle. The present proposal inhabits this tradition, including its recent application to language models and language tasks [4]. Automated approaches such as LLMorph further illustrate that transformation-based test generation and defect detection are established technical practices [10].

The formal relation is direct. For a baseline output \(a=T_\theta^{(0)}(x)\) and a transformed output \(b=T_\theta^{(1)}(f(x))\), a conventional metamorphic relation \(M_f\) could be specified by

\[
M_f(a,b)\quad\Longleftrightarrow\quad b\;R_f\;g_f(a).
\]

Given the same \(f\), \(g_f\), \(R_f\), outputs, and soundly implemented oracle, the metamorphic relation and the square express an identical acceptance condition. **Their verdicts coincide by definition.** The proposed specification consequently makes no claim of additional logical expressive power or superior fault detection relative to an equally specified metamorphic test.

The research question concerns the *construction and use* of those relations. An explicit typed record might reduce invalid test definitions, expose mistakes in target-side correspondence, encourage tests of composition, or improve the evidence connecting a failure to its source transformation. It might instead add terminology and annotation cost without improving any of these outcomes. Both possibilities belong in the empirical evaluation.

| Evaluation approach | Existing question | Relevant comparison |
| --- | --- | --- |
| Local validity | Does an artifact pass its designated checker? | Is an independently confirmed correspondence failure missed by that checker? |
| Robustness | Does performance persist under changed inputs or environments? | Is the change annotated with an exact intended semantic effect? |
| Self-consistency | Do repeated outputs or reasoning trajectories agree? | Does agreement persist across deliberate, differently ordered transformations? |
| Compositional generalization | Does a system handle unfamiliar combinations of familiar parts? | Are the failed relations attributed to controlled transformations and tested for composition? |
| Metamorphic testing | Does an expected input–output relation hold across executions? | Does a typed-square authoring protocol improve specification quality, triage, or cost against an equally informed metamorphic-testing workflow? |

SCAN, CFQ, COGS, and SLOG motivate systematic and structural generalization studies [5–8]. They do not establish the proposed protocol's utility. LeanDojo provides relevant infrastructure for interacting with formal proof environments without validating these particular benchmark claims [9]. The practical contribution, if demonstrated, would be an authoring and diagnostic discipline for relation-sensitive evaluation across domains, not a replacement for those literatures.

## 6. Domain instantiations

### 6.1 Informal mathematics to Lean

The source artifact is an informal theorem and the target artifact is a formal statement, optionally accompanied by its proof. The initial transformation family consists of well-defined specializations, changes of representation, and controlled alterations to assumptions. For example, specialize an informal theorem asserting maximum attainment by a continuous real-valued function on a nonempty compact set to a nonempty closed interval. The target-side operation performs the corresponding specialization on the formal statement.

The formal propositions are compared through mutual implication under identical assumptions. Independently, a source-alignment review checks that each states maximum attainment by a witness point. Existence of a supremum alone is insufficient. Kernel acceptance establishes validity of the formal proofs, not faithful translation of the informal claim [1]. A useful record distinguishes a valid formal proof of the wrong statement from a failed proof of the intended statement, and tracks assumptions imported through the formal environment.

### 6.2 Natural-language requirements to code

The source artifact is a behavioral requirement; its target is an implementation satisfying a declared interface. Consider a function that removes duplicate strings while retaining their first occurrence. The source transformation extends the output interface to return both the retained sequence and the number of distinct strings. Unlike an added property already entailed by correct deduplication, this changes the target type and creates a concrete transport obligation.

An independently specified target operation wraps the original implementation, retaining its output and attaching the length of that output. Thus \(g_f\) maps a sequence-returning program to a pair-returning program, with an explicit type change. The direct translation of the revised source is tested against the wrapped implementation under a declared domain of input lists. An implementation that returns the original input length instead of the deduplicated length passes on inputs without duplicates and fails on a counterexample containing repeated strings. Tests and reference properties remain validators; they are not substitutes for the required program-to-program transformation. Both implementations might still share a flawed deduplication routine, which is why source adequacy receives its own check.

### 6.3 Natural language to semantic representation

A controlled source transformation resolves quantifier scope or changes a surface expression without altering its meaning. The translation procedure produces a typed logical form or query representation. The corresponding target-side operation performs a meaning-preserving rewrite or a precisely defined scope transformation, with its semantic effect specified before evaluation.

Logical equivalence is checked within a named fragment or over a declared finite model family. Agreement over finitely many models must be reported as bounded evidence unless the decision procedure is complete for the fragment. In scope-sensitive cases, the benchmark distinguishes genuinely equivalent expressions from expressions that agree only under a restricted model class.

### 6.4 Goals to plans

Planning tests examine preconditions, state changes, resource obligations, and authority constraints. Source transformations include approval requirements, resource restrictions, and changes to permitted external effects. The target-side operation must transform executable plans within the declared action schema; validation must inspect traces, not final states alone.

The approval-gate example in Section 3 supplies a diagnostic item. Additional cases might test whether a constraint is named in plan text without governing executable guards. Each item must specify whether the comparison concerns a single trace, all traces permitted by a nondeterministic plan, or a refinement relation over trace sets.

### 6.5 Scientific protocols to claims

Scientific translation presents a distinct problem of evidential support. The source might describe a simulated stability result, an experimental protocol, or a measured outcome. Its target is a structured claim record bearing a stated evidential status. Changing the protocol to introduce empirical measurement obligations must not automatically turn simulated evidence into an observed result.

The target-side operation modifies the permitted claim status or introduces an unmet-evidence obligation. Empirical status is recorded only in the presence of qualifying measurement evidence. This track involves scientific judgment about assumptions and evidence quality, and it stays exploratory pending acceptable review reliability. No experimental results are presented in this essay.

## 7. Admissible transformations

The first dataset uses a small, controlled set of source transformations. Every included transformation has a declared semantic effect and a corresponding, independently reviewable target operation or relational oracle. Arbitrary textual changes without an annotated meaning relation do not qualify.

| Family | Source-side change | Primary control |
| --- | --- | --- |
| Paraphrase | Alter surface expression while preserving intended meaning | Establish semantic equivalence before testing. |
| Specialization | Restrict a general statement or task to a declared case | Check the direction and retained assumptions. |
| Generalization | Extend an artifact's intended domain | Establish the wider obligation independently. |
| Constraint addition | Introduce a requirement, invariant, or authority condition | Verify its operative effect, not textual mention alone. |
| Representation change | Re-encode an artifact inside the source environment | Distinguish source-side re-encoding from source-to-target transport. |
| Decomposition | Divide a task into components with a recomposition rule | Check recomposed semantics and interface compatibility. |
| Refinement | Replace an underspecified object with a more constrained one | State a directed refinement relation. |
| Authority change | Alter which actions or claims the artifact is permitted to support | Inspect action traces or evidence-linked claim status. |

These families do not all admit the same comparator. Paraphrase is naturally associated with semantic invariance, specialization with a directed relation, and authority change with a constraint on permitted effects. Benchmark-wide scoring must retain those distinctions.

## 8. Failure attribution

Failure localization is a proposed benefit of the square, contingent on reliable validators and an annotation protocol. Its records distinguish defects in item design, discrepancies in evaluated outputs, and weaknesses in validation.

| Failure class | Diagnostic condition | Interpretation |
| --- | --- | --- |
| Invalid source or transformation | \(x\) or \(f\) lacks a sufficiently defined semantics | Item-design defect; exclude or repair before model scoring. |
| Incorrect target correspondence | \(g_f\) implements a different change from \(f\) | Benchmark-design defect unless the operation is part of the system under evaluation. |
| Type or execution failure | An attempted translation fails, violates the target type, or cannot support a required target operation | Record the attempted path and its ineligibility for relational scoring. |
| Source-alignment failure | A well-typed artifact misstates the source task, its assumptions, or its permitted effects | Assess against the independent source-adequacy judgment, even if paths agree. |
| Non-commutation | Both paths satisfy the eligibility conditions and fail \(R_f\) | Genuine path disagreement under the declared relation. |
| Assumption or generality drift | An artifact loses premises, weakens the conclusion, or asserts excess generality | Substantive semantic failure supported by independent analysis. |
| Constraint omission | A new obligation is absent from the executable artifact or operative statement | Failure to integrate the source transformation. |
| False acceptance | The validator accepts artifacts that violate the declared relation | Validator error; revise the oracle and reassess affected records. |
| Indeterminate judgment | Timeout, unsupported construct, insufficient evidence, or unresolved review | Withhold an agreement judgment and report coverage. |

These labels are not mutually exclusive. For instance, a type-correct theorem that states a weaker claim might receive a translation-alignment label and a generality label. Primary failure attribution must distinguish *observed disagreement* from a conjectured cause. Attribution to the model, transformation operator, or validator needs evidence beyond the disagreement itself.

## 9. Benchmark specification

The proposed initial release is a protocol and dataset design, not an existing validated benchmark. Every item records its semantic context, both transformations, and its oracle before any evaluated model produces an output. The minimal artifact comprises a specification record, an execution record, and an adjudication record.

| Specification field | Required content |
| --- | --- |
| `id`, `domain`, `version` | Stable identity, target domain, and item revision. |
| `source_environment`, `target_environment` | Object languages, execution semantics, interface versions, and relevant dependencies. |
| `source_object`, `source_transformation` | Original task, transformation definition, and independently checked semantic effect. |
| `translation_task`, `system_configuration` | Translation instructions, model or agent configuration, sampling conditions, and tool access. |
| `target_transformation` | Typed operation \(g_f\), its applicability domain, provenance, and independent review; required for the square track. |
| `acceptance_relation` | Named relation, argument direction, target types, applicability domain, and decision rule. |
| `local_validators`, `source_adequacy_validator`, `relational_validator` | Separate syntax/type checks, source-fidelity tests, and relation checks, with versions, assumptions, and timeout policy. |
| `expected_failure_sensitivities`, `item_family` | Preregistered diagnostic categories, counterexample families, and a grouping identifier for related tasks. |
| `review_protocol`, `authoring_method` | Rubric, reviewer qualifications, independent judgments, authoring intervention, and adjudication procedure. |

The execution record contains \(T_\theta^{(0)}(x)\), \(T_\theta^{(1)}(f(x))\), the result of applying \(g_f\) where defined, the independent local, source-adequacy, and relational checks, and all error or indeterminate outcomes. It also records execution seeds, elapsed time, tool and test budgets, and relevant environment identifiers. The adjudication record identifies the observed failure, any separately supported causal diagnosis, reviewer disagreement, and the cost of producing an actionable repair.

### 9.1 Initial allocation

The proposed pilot comprises 100 items, with a range of 80–120 if validation costs warrant adjustment. Its purpose is to establish feasibility and refine the instruments. It is not a powered demonstration of universal model rankings.

| Domain | Proposed items | Primary assessment |
| --- | ---: | --- |
| Informal mathematics to Lean | 25 | Proof and proposition checks with independent informal alignment. |
| Requirements to code | 25 | Executable property and counterexample checks. |
| Semantic parsing | 25 | Typed logical forms and constrained denotational checks. |
| Planning | 15 | Preconditions, effects, authority, and trace validation. |
| Scientific claim records | 10 | Reviewed evidential status and assumption alignment. |
| **Total** | **100** | **Exploratory, domain-stratified pilot.** |

The scientific track functions primarily as a feasibility study for reviewed alignment. The smaller domain groups are insufficient for strong cross-domain comparisons without further sampling and uncertainty analysis.

## 10. Evaluation design and analysis

The central empirical comparison has two different questions. First, does a properly specified relational test expose substantive defects that a designated local checker misses? Second, does the typed-square *authoring method* produce more reliable or useful relations than a conventional metamorphic-testing workflow equipped with comparable information? The first question evaluates the diagnostic role of relational testing; the second evaluates the contribution particular to this proposal.

The second comparison is decisive for assessing any incremental methodological contribution. Both workflows receive the same task families, target semantics, intended source transformations, available reference information, and oracle budget. One authoring condition uses a conventional metamorphic-relation template; the other uses the typed-square record with explicit target-operation and source-adequacy fields. Within task-family strata, items and authoring conditions are randomized and balanced across authors; each condition covers the same families, and author experience is recorded. No author receives the same underlying task under both conditions. Independent adjudicators apply a common rubric to standardized test descriptions that conceal the authoring condition as far as possible. The analysis accounts for author and task-family clustering, and records exclusions or revisions using the same rules in both conditions.

The principal quality outcomes are independent acceptance of the resulting test specification, error or indeterminacy rate, correctness of counterexamples on defect-injected references, and accuracy of failure attribution. Costs include drafting, validating the target correspondence, executing the tests, and adjudicating failures. Diagnostic yield is reported as the number of independently confirmed, distinct, actionable defects per unit of total evaluation effort, along with raw counts and false-positive rates. Each count has a declared unit of analysis, preventing multiple equivalent test cases from inflating the apparent evidence.

For an authoring workflow \(w\), one descriptive cost-normalized measure is

\[
\widehat{Y}_w=
\frac{N_{\mathrm{confirmed,actionable},w}}{H_{\mathrm{authoring},w}+H_{\mathrm{checking},w}+H_{\mathrm{adjudication},w}},
\]

with nonzero measured hours in the denominator. The study reports workflow-specific quantities and paired or cluster-aware contrasts. The ratio describes the evaluation workflow, not an intrinsic property of a model. Time and reviewer effort are measured prospectively under a common accounting rule. Automated compute and tool costs are reported separately or translated into a prespecified common cost unit.

Local validity records well-typedness and basic environmental checks. Source adequacy is evaluated separately against the independently specified task, including its revised obligations. Relational outcomes are reported for the full attempted set, alongside eligibility coverage, and separately for the subset of artifacts passing relevant local checks. Restricting all analysis to locally accepted artifacts would conceal the influence of validator strength. If both evaluation methods receive an identical instantiated metamorphic relation, identical model outputs, and the same relational oracle, their pass/fail judgments are mathematically identical; the intervention then concerns documentation, independent review, and repair utility alone.

Repeated model runs require explicit treatment of stochasticity. Per-domain and per-transformation-family estimates retain the appropriate sampling units, with cluster-aware uncertainty where item families or seeds induce dependence. Identity-transformation controls and multiple seeds help distinguish a transformation-associated discrepancy from baseline variation across sampled outputs. Model reliability, test sensitivity, and failure localization are analyzed as separate quantities. Evaluating a generator under direct, two-path, or type-first prompts constitutes a separate experiment from evaluating the authors and validators of the tests. Any such comparison needs matched inference budgets and must report abstentions, failures, and missing executions.

Item creation and scoring remain independent. Source transformations, reference target operations, and acceptance relations are fixed before the evaluated outputs are inspected. Validators are challenged with correct references, injected substantive defects, and adversarial near-misses. Held-out transformations and explicit item provenance address test leakage and template memorization without establishing that contamination is absent. The initial allocation is an exploratory instrument-development study, not an adequately powered ranking of model families.

## 11. Pilot workflow and stopping conditions

Construction proceeds from a small number of validated square templates. Item authors first establish the source meaning and transformation. A separate review checks the target operation and the acceptance relation. Domain validators are tested on correct references and deliberately injected defects. Only validated items enter model evaluation. Outputs are logged independently for the two paths, and disagreements receive blinded adjudication under a fixed rubric.

Expansion depends on trustworthy transformations, independently established reference judgments, and measured improvements in test specification, actionable diagnosis, or evaluation efficiency at an acceptable cost.

The stopping conditions are concrete. The initial claim must be narrowed or the track discontinued under any of the following circumstances.

- Target operations fail independent semantic review or are ill-typed for a substantial class of candidate items.
- Reviewed judgments do not achieve a prespecified reliability threshold, or adjudication exposes persistent ambiguity in the acceptance relation.
- Apparent disagreements arise predominantly from formatting, stochastic variance, or validator defects, with few confirmed substantive transformation failures.
- Specification quality, actionable failure attribution, and cost-normalized yield show no advantage over equally informed metamorphic-testing workflows.
- Failure labels do not improve fault localization or repair relative to a simpler test record.
- Evidence of success is confined to a narrow formal setting while broader claims continue to be made without support.

The exact thresholds for reviewer reliability, authoring quality, diagnostic yield, and practical cost belong in a preregistered protocol once item difficulty and annotation variance are estimated. Assigning numerical thresholds without pilot evidence would create false precision.

## 12. Limits of the proposal

The framework is deliberately selective. Some tasks lack a well-defined source transformation, a tractable target-side operation, or a reliable acceptance relation. Several domains support directed refinement more naturally than symmetric equivalence. Others contain underspecified semantics that no finite test suite fully resolves. The absence of an adequate oracle is a limitation on evaluation, not evidence of a failed model.

Even a valid square diagnoses a relation on particular artifacts under a particular environment and validator. It does not establish general semantic competence, the correctness of all downstream uses, or universal preservation of structure. The stronger mathematical interpretation associated with functors calls for explicit categories, identity and composition laws, and appropriately scoped evidence beyond individual squares. Approximate relations need their own congruence and composition assumptions before transitive reasoning is justified.

Task-specific checking retains independent authority. Lean proof verification, executable specifications, trace validation, and expert review establish different judgments under different trust assumptions. The square contributes only if its relational obligation or diagnostic record improves on those existing checks.

## 13. Conclusion

Functorial Consistency develops a disciplined question about AI-generated artifacts. If the source task changes in a specified way, does translation respect that change under a declared relation in the target environment? The commutation square makes the question explicit and exposes the assumptions needed to assess it. Its value depends on the independent specification of both routes, the typing of their outputs, and a validator commensurate with the relation being tested.

The proposal rests on finite, independently checked cases. Successful path agreement neither proves general functoriality nor establishes semantic fidelity. Scientific value depends on a demonstrated improvement in test construction, error attribution, or evaluation efficiency against matched metamorphic-testing practice.

Within the Compositional Intelligence series, the essay thus connects the construction of typed artifacts to the preservation of meaning, obligations, and permissible effects through transformation. That connection is most useful where the intended relation is explicit enough to be challenged by a counterexample and repaired through a recorded change.

## Appendix A. Compact benchmark card

| Field | Example annotation for the approval task |
| --- | --- |
| Source object | Prepare and transmit the specified report. |
| Source transformation | Add mandatory recorded approval before external transmission. |
| Translation | Produce a plan in the declared action language. |
| Target operation | Insert approval request and a state-dependent guard on every transmit action. |
| Target type | Executable plan with declared preconditions, effects, and action guards. |
| Acceptance relation | Equivalence of permitted transmission traces under the declared action semantics. |
| Local checks | Plan syntax, type and action-schema validity, and goal reachability. |
| Source adequacy | Recorded approval is a genuine precondition for transmission under the revised task. |
| Relational check | Trace comparison under the declared state semantics, with an explicit witness for disagreement. |
| Defect injection | Delete the approval guard while retaining the approval-request step. |
| Expected finding | A trace permits transmission with no recorded approval. |
| Reviewer task | Verify the counterexample and attribute the missing guard. |
| Limit | Strong authority-aware local validation detects the same substantive violation. |

## Appendix B. Review rubric

Reviewed-alignment items use three decisions: *accept*, *reject*, and *indeterminate*. Reviewers record the intended source meaning, the transformation's semantic effect, the target operation's correspondence, retained and changed assumptions, the direction of any generality change, and the permitted use of the resulting artifact. Every rejected or indeterminate item carries a reason and an adjudication trail. Reliability is measured on independent initial judgments, prior to adjudication.

## References

1. Lean Language Reference. [*Validating a Lean Proof*](https://lean-lang.org/doc/reference/latest/ValidatingProofs/). Official Lean documentation, accessed November 2026.
2. Charlotte Aten, Venanzio Capretta, and William DeMeo. [*Functor and Natural Transformation*](https://categorytheory.gitlab.io/functor_and_natural_transformation.html), *Category Theory: A Concise Course*, Section 6, 2019.
3. Tsong Yueh Chen et al. [*Metamorphic Testing: A Review of Challenges and Opportunities*](https://i.cs.hku.hk/~tse/Papers/2010s/hlmtCSUR.html). *ACM Computing Surveys* 51(1), 2018.
4. Steven Cho, Stefano Ruberto, and Valerio Terragni. [*Metamorphic Testing of Large Language Models for Natural Language Processing*](https://doi.org/10.1109/ICSME64153.2025.00025). *Proceedings of the 41st IEEE International Conference on Software Maintenance and Evolution*, pp. 174–186, 2025.
5. Brenden M. Lake and Marco Baroni. [*Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks*](https://proceedings.mlr.press/v80/lake18a.html). ICML, 2018.
6. Daniel Keysers et al. [*Measuring Compositional Generalization: A Comprehensive Method on Realistic Data*](https://research.google/pubs/measuring-compositional-generalization-a-comprehensive-method-on-realistic-data/). ICLR, 2020.
7. Najoung Kim and Tal Linzen. [*COGS: A Compositional Generalization Challenge Based on Semantic Interpretation*](https://aclanthology.org/2020.emnlp-main.731/). EMNLP, 2020.
8. Bingzhi Li, Lucia Donatelli, Alexander Koller, Tal Linzen, Yuekun Yao, and Najoung Kim. [*SLOG: A Structural Generalization Benchmark for Semantic Parsing*](https://aclanthology.org/2023.emnlp-main.194/). EMNLP, 2023, pp. 3213–3232.
9. Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J. Prenger, and Animashree Anandkumar. [*LeanDojo: Theorem Proving with Retrieval-Augmented Language Models*](https://papers.nips.cc/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html). NeurIPS, 2023.
10. Steven Cho, Stefano Ruberto, and Valerio Terragni. [*LLMorph: Automated Metamorphic Testing of Large Language Models*](https://doi.org/10.1109/ASE63991.2025.00385). *Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering* (tool demonstration), pp. 4102–4105, 2025.
