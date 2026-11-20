# Semantic Participation

## Abstract

Formally checked proofs establish propositions in specified logical environments, tested software patches establish properties exercised by their test procedures, and simulation results establish conclusions conditional on models and numerical methods. Each result is meaningful, yet none independently warrants every later claim made in its name. The failure arises at the point of reliance, as evidence for one property is treated as authority for another.

This essay develops *semantic participation* as an account of how AI-generated artifacts become premises, components, and instruments of further intellectual work. It distinguishes the production of an artifact, its eligibility for a specified use, its actual incorporation into subsequent work, and its demonstrated contribution to that work. The governing question concerns the grounds of a particular dependence. What has been established, under which interpretation and assumptions, by which assessment procedure, and for what further purpose? *Semantic transport* names the additional assessment needed as artifacts cross representations or environments. Curry–Howard–Lambek provides an exact point of departure through typed construction and composition, while Lean illustrates the distance separating a checked formal statement from the intended mathematical claim.

The proposal synthesizes established practices in formal verification, source-alignment assessment, provenance, scientific documentation, and review. It neither replaces those practices nor supplies a universal semantic validator. Its empirical hypothesis is that decisions about downstream reliance improve if the relevant evidence and outstanding obligations are brought together at the point of use. Comparative testing against mature domain-specific alternatives, with full cost accounting, has yet to establish that benefit.

## 1. From a successful result to a justified premise

Consider an AI system asked to formalize a mathematical theorem in Lean. It returns a declaration accompanied by a proof accepted under the specified formal environment. The proof is mathematically significant. Yet the declaration might express a different statement from the theorem requested. Successful checking then establishes the formal target, while leaving the intended formalization uncompleted.

The distinction is fundamental. Proof checking assesses a precisely represented proposition under particular definitions and assumptions. Mathematical interpretation addresses the further question of correspondence with the source theorem. These assessments address different objects of concern. The first is an established relation inside a formal system; the second is a claim about interpretation across representations.

Comparable discrepancies arise outside mathematics. Code patches pass repository tests while changing interfaces relied upon by external applications. Simulated quantities are reproduced accurately in manuscripts and later cited as empirical observations. An executable plan produced by an agent might have effects outside its delegated authority. In each case, a local result becomes problematic at a later step that depends on it.

This essay calls that step a *point of reliance*. It occurs wherever a person or system treats an artifact as a premise, dependency, evidential basis, or instruction. The relevant question extends beyond whether the artifact has been checked. It concerns what the check established, how that finding relates to the proposed use, and whether further obligations intervene.

There is no shortage of existing practices directed at these questions. Proof certificates, test reports, code review, provenance records, research-object metadata, statistical protocols, and access controls already organize evidence and responsibility. Their effectiveness differs across domains, and their conclusions have distinct scopes. The proposed contribution is a way of relating those conclusions to particular acts of reliance, without turning them into one undifferentiated notion of validity.

*Semantic participation* names the broader phenomenon in which an artifact assumes a role within an evolving practice of reasoning and construction. Participation in the descriptive sense is observable through dependence. Participation in the justified sense additionally rests on adequate evidence for the specific inference or operation. An invalid conclusion might be widely cited, and an unauthorized component might be deeply integrated. Those are genuine instances of dependence, with defective grounds. The distinction keeps social uptake separate from epistemic standing.

## 2. The relevance and limits of Curry–Howard–Lambek

The Curry–Howard correspondence relates propositions to types and proofs to terms inhabiting those types. The judgment

\[
\Gamma \vdash t : A
\]

states that the term \(t\) has type \(A\) in context \(\Gamma\). The context matters. It specifies declarations and assumptions on which the construction depends. Term construction confers no unrestricted entitlement to inhabit any type selected by a later user.

Lambek's categorical account adds a precise account of composition. Under standard categorical interpretations of simply typed lambda calculus, types receive interpretations as objects, terms in context as suitable morphisms, and substitution as composition. This supplies an exact mathematical picture of how local constructions fit into larger derivations (Lambek and Scott, 1986). Valid composition depends on the types and relations actually involved.

The analogy for AI-generated work is disciplined, not literal. Proof terms, software patches, scientific estimates, and laboratory instructions do not share one type theory. Experimental warrant is not proof-term inhabitation, and institutional authorization is not categorical composition. The lesson is narrower and more valuable. Successful construction is judged relative to a target and context, while successful participation in further work depends on the relations governing composition.

This framing also establishes the division of labor within *Compositional Intelligence*. *Typed Generativity* studies the production of candidates for specified targets. *Functorial Consistency* studies the preservation of structure across transformation paths. *Semantic Participation* asks which grounds make the constructed artifact suitable for a particular subsequent inference or operation. The essays share a concern with structured composition, while their tests address distinct questions.

## 3. An environment-relative account of admission

The term *semantic environment* denotes a setting in which artifacts receive interpretations and participate in specified practices of checking, review, combination, and use. Lean developments, software repositories, scientific workflows, and institutional procedures instantiate such environments in different ways. Each has identifiable objects and dependencies, standards of acceptance, and consequences attached to particular actions.

For analytical purposes, write

\[
E_v=(\mathcal O_v,\mathcal C_v,\mathcal V_v,\mathcal R_v,\mathcal P_v).
\]

Here \(v\) denotes a recorded environment revision. The components describe interpreted objects, contextual and dependency relations, validation methods, review roles, and use policies, respectively. This is an organizational model. It makes no claim that a single semantics or common decision procedure governs all five components across domains.

Let \(a\) denote an artifact at an identified revision, \(s\) its declared source or purpose, \(e\) the available evidence, and \(u\) a contemplated use. The source might consist of an informal theorem, interface specification, experimental question, or instruction. Its interpretation might be ambiguous. Evidence might include a proof certificate, test output, measurement record, expert assessment, or documented limitation. Each entry identifies a property assessed and the conditions attached to the result.

Under an identified review regime at time \(t\), an assessor \(j\) might record

\[
J^{j,t}_{E_v}(a,s,e,u)=(\sigma,\Gamma,\rho),
\]

where \(\sigma\) is a disposition, \(\Gamma\) the conditions governing the decision, and \(\rho\) a rationale referencing the relevant evidence. Four dispositions are useful.

- **Accepted.** The identified criteria are satisfied for the particular use under assessment.
- **Conditional.** The specified use is eligible only if stated obligations are fulfilled and checked at the relevant decision point.
- **Rejected.** An established incompatibility defeats the proposed use under the identified criteria.
- **Unresolved.** Available information or interpretive agreement is insufficient for a justified disposition.

These are judgments attributed to an assessor and regime, not absolute properties of the artifact. The *conditional* disposition is especially vulnerable to misuse. A missing proof gains no epistemic standing from an annotation. If the intended operation relies on a verified property, the obligation to verify that property persists until discharged. Likewise, recording a restriction is distinct from enforcing it. Review records without effective controls must state the limits of their operational effect.

The decision also depends on the purpose. A boundedness lemma might support a later proof invoking boundedness while failing to complete a formalization task asserting attainment. Model estimates might guide experimental selection without supporting claims of experimentally demonstrated performance. Software changes might be incompatible with patch releases and acceptable as declared breaking changes. The artifact stays the same across these assessments; the proposed relation of reliance changes.

Useful records concentrate on six matters—artifact identity and revision, exact property checked, source interpretation, evidential support and assumptions, integration consequences, and the specific use under review. Their purpose is to make the grounds of a decision inspectable. Additional fields have value only if they affect diagnosis, repair, review, control, or subsequent work. Formal completeness is no substitute for substantive examination.

## 4. Admission, dependence, and contribution

Three further distinctions prevent the framework from becoming a theory of institutional permission alone.

First, **admission is prospective**. It records that a particular use has met, or has yet to meet, identified criteria. This need not involve a centralized gatekeeper. In mathematics, the relevant assessment might be performed by the researcher invoking a lemma. In software, a maintainer might decide on integration. In a laboratory, scientific and operational questions might belong to different authorized roles. The assessor and scope are indispensable to the meaning of a judgment.

Second, **dependence is descriptive**. Later operations \(d\) might import, quote, execute, interpret, or otherwise rely on \(a\). Write

\[
D_{E_v,t}(d,a;u)
\]

for an observed dependence in which \(a\) plays role \(u\). This notation does not certify the quality of that dependence. An artifact might be reused despite an unresolved admission judgment. Conversely, an approved artifact might never be used. Justified semantic participation joins actual dependence to adequate grounds for the particular use, subject to subsequent revision.

Third, **contribution is consequential**. Repeated imports do not rescue a badly designed, redundant, or misleading theorem. One carefully chosen dataset might nevertheless transform a scientific investigation. Frequency of reuse is evidence of circulation, not a measure of intellectual value. Value concerns the consequences of dependence under specified criteria.

These distinctions introduce time. Library updates might change an imported theorem's meaning. Retractions might weaken published estimates, and revised permissions might prohibit continued deployment. Prior admission is not permanent authorization. Competent systems identify decisions affected by changed grounds and subject them to appropriate reassessment. This involves tracing relevant dependencies and interpreting the effects of change. Neither capability follows automatically from attaching metadata to an artifact.

## 5. What the Extreme Value Theorem example establishes

Lean makes the separation of formal validity and source fidelity unusually clear. The kernel checks elaborated terms against declared formal types in a specified environment. That check is strong evidence for the formal proposition subject to its trusted components and axioms. It does not establish that the proposition is the one a mathematician intended to formalize. Lean's documentation also recommends inspecting axiomatic dependencies, including uses of admitted proofs, for consequential verification tasks (*Validating a Lean Proof*, Lean 4.36.0).

Consider the informal claim that a continuous real-valued function on a nonempty compact interval attains a maximum. For real numbers \(a\le b\) and \(f:[a,b]\to\mathbb R\), its intended conclusion has the form

\[
\exists x^*\in[a,b]\;\forall y\in[a,b],\quad f(y)\le f(x^*).
\]

The witness \(x^*\) is a point of the domain where the maximal value is attained. The generated declaration might instead assert boundedness above,

\[
\exists M\in\mathbb R\;\forall y\in[a,b],\quad f(y)\le M.
\]

The second proposition lacks a maximizing witness. It states that an upper bound exists, with no commitment that the bound is reached. In general, boundedness fails to imply attainment. For example, define \(f(x)=x\) for \(0\le x<1\), and \(f(1)=0\). This function is bounded on \([0,1]\) and has no maximizer, although its discontinuity excludes it from the hypotheses of the Extreme Value Theorem.

That qualification matters. Under the theorem's original hypotheses, both boundedness and attainment hold. Boundedness is a valid mathematical consequence of those hypotheses. The defect in the candidate formalization concerns **which conclusion the task called for**. It is neither a disproof of boundedness nor a claim that the two sentences acquire different truth values under the full theorem hypotheses. Formal implication tests alone might miss that defect, particularly if the surrounding hypotheses independently establish both conclusions.

Other errors concern quantifier order, changed definitions, unstated side conditions, or excessive specialization. The same source claim might also admit mathematically equivalent formal statements with different syntax. Faithful formalization thus calls for explicit attention to the chosen interpretation and semantic relation, beyond superficial similarity or successful checking.

Trust must also be specified precisely. Accepted elaborated terms might depend on axioms, and an axiom report is relevant to the consumer's chosen trust policy. In Lean, `#print axioms` exposes such dependencies, including `sorryAx` for incomplete proofs in the dependency chain. Records reporting only *Lean verified* conceal distinctions material to the intended reliance. This essay's mathematical formulas are illustrative; no Lean declaration has been executed or independently certified here.

FormalAlign (Lu et al., 2025), the benchmarks and metrics of Poiroux et al. (2025), and SHADOWBENCH (Han et al., 2026) directly address semantic alignment in autoformalization. They provide relevant methods, datasets, and tests for the source-fidelity question. The present proposal does not claim to originate that problem or solve it. It asks how an alignment judgment, once made with an identified method and limitations, informs a later decision to import, cite, or build upon the formal artifact.

## 6. Semantic transport and evidential continuity

Artifacts change representation and context. An informal theorem becomes a formal declaration. Simulation results appear as figures in scientific papers. Research prototypes become library dependencies. These transformations preserve some features, alter others, and occasionally introduce new evidence. The relevant continuity concerns both **what the transformed artifact says** and **what justifies reliance on it**.

Write a proposed transport as

\[
T:(a,E_s)\longmapsto(b,E_t,\rho_T),
\]

where \(\rho_T\) records the source and target revisions, the intended relation of preservation, evidence for that relation, altered assumptions, and unresolved obligations. The transport record makes an inspectable claim. It does not confer validity on its own transformation.

Preservation has no universal meaning. For mathematical statements it might concern equivalence, implication, or conservative extension. For software it might concern behavioral refinement under an interface contract. For numerical results it might concern an error bound and the domain of applicability of a model. For scientific inference it might concern the population, intervention, instrument, and background conditions underlying the estimate. The appropriate relation must be stated before a later consumer treats the transformation as harmless.

Consider a model-derived estimate that appears first in an experimental-planning document and later in a deployment recommendation. Perfectly reproducing its numerical value through both documents preserves the numeral. It does not establish suitability for the new deployment regime. That additional use needs evidence connecting the model's domain to the proposed conditions. Retaining a list of limitations is useful only insofar as those limitations influence the next decision.

One principle follows. **Repetition does not create missing warrant.** If a relation linking a model to a target population has never been established, faithfully citing successive summaries does not establish it. New measurements or a defensible transport argument might strengthen the evidential basis, yet that improvement must be separately identified. The claim is not that support necessarily weakens under every transformation. It is that each change in support needs its own grounds.

For successive transports \(T_1\) and \(T_2\), an assessment of the composite must account for the identity and meaning of the intermediate artifact, compatibility of the two asserted preservation relations, and assumptions introduced or discharged at each step. Two individually adequate records do not automatically establish an adequate composite, especially if their scopes differ. This is the bridge to *Functorial Consistency*, where alternative transformation paths are compared under explicit criteria. No general functorial structure is attributed here to empirical workflows or institutional decisions.

## 7. Scientific claims and software contracts

Suppose an AI-supported research workflow reports that “Molecule X is stable.” The assertion is incomplete without a specification of the relevant notion of stability. Thermodynamic preference, kinetic persistence, resistance to degradation, and behavior under specified laboratory conditions answer different scientific questions. Time horizon, temperature, solvent, material form, and measurement procedure might alter the interpretation of the claim itself.

Suppose a simulation estimates the persistence of a chemical species under one model and operating regime. The estimate might be useful in choosing an experiment. Reporting it as measured shelf life would assert another kind of evidential support. The simulation has produced no observation of that shelf life. Experimental results could later support a related claim, subject to their own controls, uncertainty, and measurement conditions.

This is best represented as a relation of support for a **specific claim**, not a permanent label applied to an entire document. In schematic notation,

\[
\operatorname{Support}^{j}(e,q\mid c),
\]

identifies an assessment by \(j\) of evidence \(e\) for claim \(q\) under conditions \(c\). The notation does not define a universal probability, proof rule, or threshold. The assessment method is domain-specific. One research report might contain observations, calibrated estimates, model predictions, and conjectures, each with a different basis of support. Their juxtaposition does not license upgrading one kind of claim to another.

Permission is again distinct. An empirical result might be adequately supported yet restricted by data-use agreements or operational safety rules. Conversely, authorization to run an experiment does not establish that its conclusions are scientifically sound. The account must preserve the difference separating evidential support from delegated authority.

In software, imagine a timestamp parser altered by an AI coding agent. The patch compiles and passes its existing unit tests, yet changes timezone-offset normalization. External callers expecting the earlier behavior might now receive a different result. Testing establishes properties of examined cases. Contract preservation concerns a broader set of behaviors, dependencies, and consumers.

The patch might be inappropriate for a backward-compatible release and legitimate within an explicitly versioned breaking change. Its use depends on a concrete integration decision with known tradeoffs. The same principle applies to a new theorem that introduces a library's dependency burden. Local correctness and integration quality involve distinct criteria, and both assessments are relevant to subsequent work.

## 8. From participation to cumulative improvement

A valid formal contribution might be mathematically interesting yet poorly suited to a maintained library. It might duplicate an existing theorem, obscure a more general abstraction, complicate search, or introduce costly dependencies. Another contribution might improve future proofs by exposing an especially useful intermediate lemma. Such differences concern the effects of integration, not the truth of the new statement.

For a pinned library \(L\), proposed contribution \(c\), and prospectively selected future workload \(\mathcal T\), consider a diagnostic vector

\[
\Delta_L(c;\mathcal T)
 = F(L\oplus c;\mathcal T)-F(L;\mathcal T).
\]

The operation \(L\oplus c\) describes a specified integration procedure, including any necessary refactoring. The components of \(F\) might measure successful proofs, retrieval effectiveness, automation performance, review time, dependency burden, and maintenance effort. Units and desirable directions differ, and no scalar measure of library value is implied.

The comparison is meaningful only under a defensible experimental design. Evaluator versions, tool budgets, task sampling, and prior exposure to the contribution all affect measured outcomes. Workloads assembled from tasks that directly restate the submitted theorem would exaggerate reuse. Maintainer judgment and future independent tasks supply complementary evidence, with their own biases and uncertainties.

The distinction is important for the series as a whole. *Typed Generativity* might establish that a system produces correct formal artifacts. Semantic participation asks whether those artifacts support justified further work. Library improvement asks whether that work has become more effective or reliable as a consequence. Each is a separate empirical claim.

## 9. Relation to established research

The proposed account builds on substantial existing infrastructures. Proof-carrying code exemplifies a producer supplying a checkable certificate for a consumer-defined policy (Necula, 1997). Lean provides formal validation and dependency inspection, while LeanDojo supports programmatic theorem-proving research and premise retrieval (Yang et al., 2023). Recent autoformalization studies examine whether generated formal statements preserve informal mathematical meaning (Lu et al., 2025; Poiroux et al., 2025; Han et al., 2026).

Beyond formal methods, W3C PROV represents entities, activities, agents, and derivation relations. FAIR principles address conditions supporting scientific data stewardship and reuse. RO-Crate supplies extensible descriptions of research objects, including domain-specific profiles. Datasheets for Datasets and Model Cards formalize documentation of purposes, evaluations, intended uses, and limitations (W3C, 2013; Wilkinson et al., 2016; RO-Crate Community, 2026; Gebru et al., 2021; Mitchell et al., 2019).

These precedents already cover much of the ground. An extensible provenance or research-object system might hold the proposed information without adopting a new format. Mature review procedures might already connect the evidence to consequential decisions. The framework's distinctive proposition concerns **the adequacy of a particular reliance relation**, not a claim to have invented evidence tracking or metadata for limitations.

The practical contribution, if established, would consist in connecting the relevant checks, interpretive assessments, dependency relations, and operational criteria at the exact place they affect a downstream decision. That connection might be implemented using existing formats and tools. Its value must be judged against comparable established practice, not an artificially impoverished baseline.

## 10. Evaluating the proposal

The empirical hypothesis is specific. In selected settings, a structured, use-focused assessment will reduce unsupported reliance or improve appropriate acceptance and deferral, compared with established domain-specific procedures at comparable evidential access and known total cost.

An exploratory study could assemble 100–150 cases from formalization, software integration, and scientific reporting. This range is a possible pilot size, not a calculation of statistical power. The pilot's function would be to assess construct validity, identify annotation ambiguities, estimate effect sizes and task difficulty, and determine whether a larger study is justified. Confirmatory experiments need separately justified sample sizes and analysis plans.

The comparison must be demanding. Baselines include existing validator output plus ordinary review, a competent domain-specific checklist or documentation process, and the proposed reliance-focused procedure. All conditions receive substantively equivalent evidence. Time spent assembling and interpreting records belongs in the cost accounting. An experimental arm furnished with expert answers in advance would confer an unfair advantage.

Reference decisions must also be constructed independently of the proposed interface. Domain experts would review the source specification, generated artifact, actual evidence, intended use, and applicable environment. Independent adjudication, recorded disagreement, and principled unresolved outcomes matter particularly in cases with ambiguous intentions. Agreement is a property to measure, not a substitute for accuracy.

Convincing benchmarks need contrastive cases. Two formal statements might both compile, with only one faithfully expressing the intended conclusion. Two patches might pass the same tests while differing in backward compatibility. Two scientific documents might report the same estimate while attaching different evidential claims. Natural cases complement deliberately constructed contrasts. Otherwise, detecting conspicuous synthetic errors risks becoming the entire task.

Primary outcomes would include unsupported uses incorrectly approved, justified uses wrongly refused, and consequential reliance errors during a subsequent task. Deferral must be assessed for both appropriateness and cost, since indiscriminate refusal produces apparent caution without useful discrimination. Secondary outcomes include decision time, reviewer calibration, repair quality, evidence-production effort, and downstream integration success. Results need uncertainty intervals, appropriate clustering by artifact and reviewer, and analysis of differences across domains and consequence levels.

A change experiment would revise a theorem dependency, interface contract, calibration, or authorization condition. The test would measure detection of affected consumers and the correctness of their revised decisions. Alert generation alone is an inadequate endpoint. Correct alerts ignored by consumers represent different failures from records that overlook the affected use.

The proposal is falsifiable in practice. Established procedures might equal or outperform the new approach. The additional structure might increase review costs without reducing errors. Reviewers might disagree despite complete records, or consumers might systematically disregard restrictions. Those findings would narrow the justified scope of the intervention. An unsuccessful implementation would neither refute every conceptual distinction nor establish its practical value.

## 11. The limits of the account

The first limit concerns interpretation. Informal specifications are incomplete, and competent readers disagree about intended mathematics, engineering contracts, or causal claims. An alignment judgment must record its interpreter, sources, and unresolved alternatives. It has no privileged access to intention solely because an AI system supplied a confident explanation.

The second concerns trust. Evidence records are themselves fallible artifacts. Purported checker results need inspectable links to their actual execution and trusted components. Reports generated and certified exclusively by the same untrusted agent have limited force under an adversarial threat model. Independent checking, access controls, signed records, or human review might be appropriate in particular settings; none is universal.

The third concerns governance. Technical validity, scientific support, and operational permission draw on different forms of authority. An admissible mathematical inference need not depend on an institutional approval process. Deployments affecting other people's systems might involve explicit delegation and effective control. Any implementation that conflates these settings risks replacing intellectual judgment with administrative formality.

The final limit concerns proportionality. Routine, low-consequence contributions seldom need elaborate records. Expensive assessment is justified only by its effect on decisions, and its effectiveness might be greatest at selected transitions instead of every internal step. Evidence favoring a leaner procedure is evidence against unnecessary complexity in the proposed framework. The aim is defensible reliance, not the proliferation of records.

## 12. Conclusion

AI systems increasingly produce artifacts intended to outlive the interaction that generated them. Theorems are imported into later proofs, patches become software dependencies, and scientific estimates inform new experiments. Their significance develops through these acts of dependence. The local result supplies part of the justification, while the contemplated use supplies the question that must be answered next.

Semantic participation provides a disciplined account of that transition. Its central distinctions separate artifact production, use-specific admission, actual dependence, and demonstrated contribution. Its account of transport examines whether meaning and evidential support continue to justify a claim as artifacts change representation and context. These distinctions neither solve interpretation nor bypass established checking and review. They identify the points where those practices must bear on further work.

For *Compositional Intelligence*, the ambition is cumulative. Typed construction concerns the formation of artifacts, compositional consistency concerns relations across transformations, and semantic participation concerns the justified incorporation of results into subsequent reasoning. The lasting test is whether a future user receives sufficient grounds for the precise claim or action undertaken in reliance on an AI-generated artifact.

## Appendix. A hypothetical reliance assessment

This example records the formalization mismatch described in Section 5. It is an illustrative assessment, not a deployed schema, verified Lean declaration, or implemented policy control.

```yaml
artifact:
  id: illustrative-boundedness-statement
  representation: hypothetical-formal-target
  environment:
    system: Lean
    system_version: unspecified
    library_revision: unspecified
source:
  requirement: maximum-attainment-on-closed-interval
  interpretation: maximizing-witness-required
evidence:
  checked_property: boundedness-above
  checker_execution:
    status: not_performed
    proof_reference: null
    axiom_report_reference: null
  source_alignment:
    status: assessed_for_this_illustration
    finding: requested-attainment-conclusion-absent
    basis: conclusion-and-witness-comparison
intended_use:
  purpose: present-as-formalization-of-maximum-attainment
  assessor: illustrative-analysis
  disposition: rejected
  rationale: target-does-not-express-requested-witness
  enforcement: not_implemented
reassessment:
  triggers:
    - revised-formal-target
    - revised-source-interpretation
    - new-validation-evidence
```

The boundedness theorem might be mathematically legitimate and appropriate for another use. This disposition concerns its inadequacy as the requested maximum-attainment formalization. No proof status is inferred from the hypothetical record.

## References

1. Lambek, J., and Scott, P. J. (1986). *Introduction to Higher-Order Categorical Logic*. Cambridge University Press. [Publisher record](https://books.google.com/books/about/Introduction_to_Higher_Order_Categorical.html?id=rx5hQgAACAAJ).
2. Lean Language Reference. (2026). *The Lean Language Reference*, version 4.36.0. [Official documentation](https://lean-lang.org/doc/reference/4.36.0/).
3. Lean Language Reference. (2026). *Validating a Lean Proof*, version 4.36.0. [Official documentation](https://lean-lang.org/doc/reference/4.36.0/ValidatingProofs/).
4. Necula, G. C. (1997). *Proof-Carrying Code*. Proceedings of the 24th ACM SIGPLAN–SIGACT Symposium on Principles of Programming Languages. [DOI](https://doi.org/10.1145/263699.263712).
5. Lu, J., Wan, Y., Huang, Y., Xiong, J., Liu, Z., and Guo, Z. (2025). *FormalAlign: Automated Alignment Evaluation for Autoformalization*. International Conference on Learning Representations. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fceedf8c9c0ff51f41b9fe0294ef0070-Abstract-Conference.html).
6. Poiroux, A., Weiss, G., Kunčak, V., and Bosselut, A. (2025). *Reliable Evaluation and Benchmarks for Statement Autoformalization*. Proceedings of EMNLP 2025, 17947–17969. [ACL Anthology](https://aclanthology.org/2025.emnlp-main.907/).
7. Han, H., et al. (2026). *SHADOWBENCH: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization*. Proceedings of EMNLP 2026, 53031–53067. [ACL Anthology](https://aclanthology.org/2026.emnlp-main.2335/).
8. Yang, K., et al. (2023). *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models*. Advances in Neural Information Processing Systems, Datasets and Benchmarks Track. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html).
9. W3C. (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation. [Specification](https://www.w3.org/TR/prov-dm/).
10. Wilkinson, M. D., et al. (2016). *The FAIR Guiding Principles for Scientific Data Management and Stewardship*. *Scientific Data*, 3, 160018. [Article](https://doi.org/10.1038/sdata.2016.18).
11. RO-Crate Community. (2026). *RO-Crate Metadata Specification*, version 1.3. [Specification](https://www.researchobject.org/ro-crate/specification/1.3/index.html).
12. Gebru, T., et al. (2021). *Datasheets for Datasets*. *Communications of the ACM*. [Manuscript](https://arxiv.org/abs/1803.09010).
13. Mitchell, M., et al. (2019). *Model Cards for Model Reporting*. Conference on Fairness, Accountability, and Transparency. [DOI](https://doi.org/10.1145/3287560.3287596).
