# Quantitative Curry–Howard

## Abstract

Learned theorem provers rank candidate tactics before checking them. Code generators assign scores to patches before their behavior has been established. Scientific models attach probabilities to claims that depend on assumptions, measurements, and inferential choices. These numbers influence the path from proposal to acceptance, yet none carries its own rule of validity.

*Quantitative Curry–Howard* studies this interval around the Curry–Howard correspondence, under which a proof is a term inhabiting a proposition represented as a type. The essay distinguishes a model's propensity to generate an artifact from the probability of its acceptance, a differentiable objective from exact constraint satisfaction, and a scientific posterior from independent empirical support. Its central claim is that **quantitative warrant belongs to a specified candidate, target, assessment procedure, and context**. Composition and revision preserve that warrant only through a further justification.

The prospective record describes a prediction, while the completed assessment documents a scoped finding. Neither record independently authorizes consequential action. The proposal is an interpretive discipline, distinct from quantitative type theory or a new proof calculus. Its practical value is open to empirical testing against existing scores, validators, and provenance practices.

## 1. The interval before a proof

Consider a theorem prover attempting to construct a proof of a proposition $P$ from a hypothesis $h : P \land Q$. Two candidate Lean scripts differ by a single projection.

```lean
-- Rejected: h has type P ∧ Q, while the goal has type P.
example (P Q : Prop) (h : P ∧ Q) : P := by
  exact h

-- Accepted: h.left supplies a term of the required type.
example (P Q : Prop) (h : P ∧ Q) : P := by
  exact h.left
```

Suppose an illustrative generator assigns the first script probability $0.70$ and the second probability $0.30$ within a restricted two-candidate distribution. These hypothetical values describe generation propensity, not checker-success probabilities. The first script fails because `h` has type `P ∧ Q`, while the target is `P`. The second projects an inhabitant of `P`. In a successful complete tactic proof, elaboration constructs a term for kernel checking. Acceptance depends on the formal rules and declared assumptions, not the model's ranking [1, 2].

The ranking influences which candidate a constrained search policy tests first. A diagnostic might direct repair toward `.left`, while the search budget determines whether the accepted script is tested at all. Quantitative evidence influences the route to proof, while the kernel governs formal acceptance.

Three questions emerge from this small example. Does the number describe what the model is inclined to generate, what a checker is likely to accept, or what a reviewer ought to inspect? Does the recorded result concern the candidate as originally proposed, or a repaired candidate? If the assumptions or environment change, what justifies reusing the old verdict? The questions differ even though each involves the same short proof script.

The same difficulty arises in software synthesis and scientific inference. Code likelihood does not establish compliance with an interface contract. A small penalty for constraint violation does not satisfy the constraint. A high posterior probability does not establish the adequacy of the model producing it. The common question is **what a particular number warrants under a particular standard**, and how that warrant changes as an artifact moves through a larger system.

## 2. The exact judgment and the proposed artifact

The Curry–Howard correspondence relates propositions to types and proofs to terms inhabiting those types. In a type-theoretic setting, the judgment

$$
\Gamma\vdash_K t:A
$$

asserts that the term $t$ has type $A$ under context $\Gamma$, according to the rules of a specified formal system $K$. The subscript makes the system dependence explicit. Formal acceptance is relative to the precise proposition, its axioms, imported declarations, and trusted mechanisms. Kernel checking establishes the formal target under those dependencies, without certifying that the target expresses the intended informal statement. In Lean, `sorry` creates an axiom dependency, detectable as `sorryAx`, while native evaluation introduces additional compiler-related trust assumptions. Inspecting `#print axioms` and the validation pathway is consequently part of determining what a checked declaration establishes [1, 2].

Generated tactics and unfinished proof scripts have a different status. The script instructs an elaboration process that might produce a term. Calling that script an inhabitant of $A$ would prejudge validation. The shorthand $\Gamma\vdash_\theta t:A\triangleright Q$ risks presenting a model proposal as a typing derivation. A proposal operation makes that distinction explicit.

$$
\operatorname{Propose}_\theta(s,\Gamma,A)=(c,Q^-).
$$

Here $\Gamma$ is the formal typing context and $s$ the model-facing information, potentially including a serialized proof state or search history. The candidate $c$ is syntax, a tactic, or a draft term. The record $Q^-$ contains information fixed **before assessment**. The operation asserts no type inhabitation. In particular, a tactic that reduces a goal is not automatically a complete proof of that goal.

A checker-facing procedure $V$ subsequently assesses the candidate under the declared target and current proof state $u$.

$$
V_{K,\Gamma,A,u}(c)\in
\left\{
\operatorname{complete}(t),\ \operatorname{continue}(u'),\
\operatorname{reject}(d),\ \operatorname{indeterminate}(r)
\right\}.
$$

This schematic interface distinguishes a finished proof from a successful intermediate tactic. The outcome $\operatorname{complete}(t)$ certifies that elaboration has produced a term $t$ accepted by the kernel with $\Gamma\vdash_K t:A$ under the declared dependencies. The outcome $\operatorname{continue}(u')$ records a tactic that succeeded while leaving goals in the updated state $u'$. It establishes neither completion nor a proof of $A$. Rejection carries diagnostics $d$, and indeterminacy $r$ covers interrupted or inconclusive assessment. Rejection of one candidate does not establish that its target is uninhabited; a timeout does not establish invalidity. A concrete implementation must specify its elaboration, kernel-checking, trust, and failure semantics.

Other domains have different validators and conclusions. Passing finite tests, satisfying a type checker, receiving an expert judgment, and obtaining a laboratory measurement yield evidence with different scopes. The proposed record preserves those differences.

The assessment appends a verdict and its provenance to the earlier record,

$$
Q^+=(Q^-,\operatorname{result}(V),\pi),
$$

where $\pi$ identifies the procedure, version, and relevant execution conditions. This is a record-construction convention, not a logical rule. The original score is preserved with its original meaning. The superscripts identify the point in the workflow at which information becomes available, not a hierarchy of evidential strength.

The separation of $Q^-$ and $Q^+$ has methodological consequences. An experiment asking whether numerical evidence predicts checker acceptance must evaluate the prediction using information fixed before checker execution. Feeding the recorded validation outcome back into the predictive representation would make the evaluation circular. By contrast, a retrospective audit properly includes the outcome and its diagnostics, provided the record states how the information was obtained.

The title *Quantitative Curry–Howard* names an interpretive question at the boundary of exact typing, not a new typing calculus. Quantitative type theory already has a technical literature on graded resource usage, including Atkey's formulation [3]. The quantities studied here concern search, prediction, and evidence attached to *unvalidated proposals*. No numerical typing rule or theorem converting model confidence into formal validity is proposed.

## 3. Three numerical meanings and the question of use

Numerical reports attached to AI-generated artifacts fall into several semantic classes. Three are prominent: search scores, softened objectives, and probabilistic claims. Their categories are not exhaustive and are not necessarily mutually exclusive. Whether any such number justifies a downstream operation is a further question, governed by the target and the applicable validation regime.

### 3.1 Search scores

A tactic generator might assign the score

$$
q_\theta(c\mid s)=P_\theta(c\mid s),
$$

where $s$ represents the model's proof-state input and $c$ is the candidate tactic. Here the probability concerns *generation by the model*. It is a distribution over candidates under a specified decoding setup, not automatically a probability of checker acceptance. Training procedures and ranking functions might produce unnormalized logits or arbitrary scores instead of probabilities. Interpretation depends on the score's origin, normalization, candidate set, and decoding procedure. Renormalizing over a restricted list changes generation probability without changing formal validity.

Learning to rank useful tactics is an established route to more effective proof search. Systems such as LeanDojo expose proof states, retrieved premises, candidate tactics, and environment feedback for that purpose [4]. The legitimate role of the score is selection under constraints of time and computation. Its evaluation concerns the cost of reaching a checked proof, the diversity of promising paths, and the ability to recover from failed steps. High rank alone establishes none of these outcomes.

If an application instead predicts the chance that a proposed complete proof will pass the declared checker, it is asserting a distinct quantity,

$$
\widehat p_\theta(V(c)=\operatorname{complete}\mid s,c).
$$

The validator parameters are suppressed in this shorthand, and the forecast calls for evaluation on a specified population of candidates and environments. For a fixed complete candidate and deterministic checker, the verdict itself is deterministic. Uncertainty concerns the population of tasks, candidates, or partially observed conditions. Training on successful proofs does not independently establish calibration for complete-proof acceptance.

### 3.2 Differentiable satisfaction

Neural-symbolic systems sometimes replace a discrete constraint with a real-valued satisfaction function or loss. Differentiable proof search, Logical Neural Networks, and formal studies of differentiable logics provide established approaches to such representations [5, 6, 7]. Their semantics differ. Some scores arise from embedding similarity during proof search. Others measure degrees of satisfaction within a specified logic or penalties under a relaxation.

Suppose a system seeks $x\leq 0$ and optimizes the penalty

$$
L(x)=\bigl(\max\{0,x\}\bigr)^2.
$$

At $x=0.01$, the loss is $10^{-4}$. The loss is small and the constraint is still violated. Any implication from approximate loss to exact validity needs an explicit mathematical bound relating the surrogate, numerical representation, and hard acceptance condition. The scale of the loss alone supplies no such implication.

In certain formalisms, real-valued semantics are themselves the intended meaning of the logic. Such values are not defective approximations of classical truth. The system must first identify whether it is reasoning in a many-valued logic, optimizing a surrogate for a classical condition, or predicting the result of a separate checker. The relevant standard follows from that choice.

### 3.3 Probabilistic warrant

Scientific models attach posterior probabilities, likelihoods, predictive distributions, and uncertainty intervals to claims. Their interpretation depends on the statistical model, conditioning information, measurement procedure, and inferential target. Higher-order probabilistic semantics, including quasi-Borel spaces, provide mathematically developed accounts of probabilistic computation [8]. Those semantic results do not establish that a particular scientific claim is adequately supported by its data.

For illustration, suppose a scientific model reports the posterior probability

$$
P(H\mid D,M)=0.93,
$$

for hypothesis $H$, data $D$, and model $M$. The value expresses model-conditional support under a specified prior and likelihood. It does not, by itself, establish the adequacy of $M$, the integrity of $D$, causal identification, or the reproducibility of the result. Those are separate questions with potentially different evidence.

Likewise, a model's token probability, a predictive probability of experimental success, and a posterior probability assigned to a hypothesis have distinct conditioning structures. Putting each in the same field labelled `confidence` would erase the distinction that permits responsible interpretation.

### 3.4 From numerical evidence to semantic participation

The preceding essays in *Compositional Intelligence* investigate the conditions under which artifacts participate in structured mathematical, computational, and scientific environments. Quantitative evidence has an analogous role only within those conditions. It might help select a candidate for inspection, estimate the cost of repair, or support a risk-sensitive decision to request independent verification. It does not confer membership through numerical magnitude alone.

A proof script becomes a checked proof through an accepted formal derivation. A code patch gains a limited functional warrant from specified tests and a stronger, differently scoped warrant from additional checks or proof obligations. A scientific claim gains support through appropriate measurement, analysis, and critical scrutiny. A reasoning trace has evidential value only for the properties established by its evaluation. Research on unfaithful chain-of-thought explanations demonstrates why a plausible account of intermediate reasoning must not be mistaken for a faithful account of the computation that produced an answer [9, 10].

These distinctions place a burden on the evidence record: its contents must preserve the *meaning* of each score, not just its value.

## 4. What an evidence record must preserve

The record needs enough information to reconstruct its claim and scope. Before validation, it identifies the candidate, target, environment, numerical semantics, predicted event where applicable, and intended checker. Following validation, it appends the procedure's verdict, assumptions, and diagnostics. Identity must extend beyond the artifact's bytes. Identical source text checked against two specifications constitutes two distinct assessments.

| Question | Prospective record $Q^-$ | Retrospective record $Q^+$ |
| --- | --- | --- |
| Which artifact and claim? | Immutable artifact identity, target, context, relevant versions | Same identities, plus assessed property and scope |
| What does the number mean? | Score kind, scale, conditioning information, predicted event or objective | Original score retained without retrospective reinterpretation |
| Which procedure supplies a verdict? | Validator identity, intended property, acceptance policy | Procedure version, outcome, assumptions, diagnostics |
| Is the prediction supported? | Calibration population, method, limitations, or explicit uncalibrated status | Independent scoring and shift analysis, if available |
| What follows from the evidence? | Proposed review decision, not a grant of authority | Observed repair, review outcome, applicable authorization decision |

The temporal separation protects the meaning of evidence. Estimated repair cost before testing differs from the observed effort expended during repair. Predicted test success differs from an observed result. Reviewer-facing summaries that incorporate hidden validation outcomes are retrospective reports, not independent pre-validation estimates. Records need timestamps or stage identifiers sufficient to preserve these differences.

The need for provenance is more than administrative. Proof-search scores calibrated on one library might fail on another. The test verdict belongs to a specific patch and test environment. The posterior refers to the data, assumptions, and analysis used to construct it. Reuse of the artifact does not establish reuse of its evidence.

Established work already addresses related needs. Model Cards document intended uses, evaluation conditions, and limitations for trained systems [11]. W3C PROV-DM specifies entities, activities, agents, derivations, and revisions in provenance descriptions [15]. The in-toto framework records and checks evidence about steps in a software supply chain [16]. These precedents cover substantial parts of the recording problem. The narrower subject here is the interpretation and justified reuse of *candidate-specific quantitative evidence* across proposal, assessment, revision, and subsequent use. Its proposed practical value depends on improvements beyond those existing mechanisms.

Epistemic classifications must be specific to the domain. For proof artifacts, `proposed`, `rejected by this checker`, and `accepted under these axioms` describe assessable states. For scientific claims, model-conditional inference, observational corroboration, and experimental replication identify distinct evidentiary routes. These classifications form no universal ranking of truth or certainty.

Permitted-use fields need equally careful interpretation. Evidence might support a recommendation to inspect a patch or reproduce an experiment. Authorization to deploy a patch or operate an instrument depends additionally on an applicable policy and on independently established authority. The record informs that decision without supplying its own authority.

## 5. The problem of composition

The connection to compositional intelligence becomes more precise once artifacts are assembled into larger processes. Evidence about individual steps need not establish evidence about their composition.

Consider $n$ sequentially proposed transformations. Let $E_i$ denote successful validation of the declared property at step $i$ under a common probability model. For event sequences with positive-probability conditioning prefixes, the chain rule gives

$$
P\!\left(\bigcap_{i=1}^{n}E_i\right)
= P(E_1)\prod_{i=2}^{n}P\!\left(E_i\mid E_1,\ldots,E_{i-1}\right).
$$

The chain rule does not license multiplication of unrelated local confidence labels. Such a calculation needs the actual conditional probabilities, or a justified independence model that applies to the joint process. Shared premises, adaptive selection, and state changes create dependence. Scores calibrated on different populations might not even refer to events in a common joint distribution.

Formal composition has a different structure. Terms $f:A\to B$ and $g:B\to C$ yield $g\circ f:A\to C$ in an appropriate typing context. This establishes a typed composite, not every informal property one might attribute to it. More specific contracts demand compatible preconditions, postconditions, and assumptions. Two locally checked components with incompatible contracts do not acquire an end-to-end guarantee through aggregation of their scores.

For empirical systems, composition introduces distribution shift and correlated failures. A workflow assembled from a planner, retriever, model, and tool validator might expose states absent from the components' isolated tests. An evidence record is useful here through its scope restrictions, provenance, and identification of untested interfaces. One aggregate confidence value for the workflow would obscure those dependencies.

This distinction also clarifies the relation to the earlier essays. *Functorial Consistency* asks whether intended structure is preserved across transformations. *Algebraic Architectures* asks which structural obligations a system enforces and which depend on evidence about an implementation. Quantitative Curry–Howard examines the additional question of **what survives as warranted knowledge about a candidate as it crosses those interfaces**. The composition of artifacts, the composition of formal derivations, and the composition of empirical confidence are separate operations.

## 6. Evidence under revision and change of context

Revision provides a stronger test of evidential discipline. The proof script `exact h.left` in Section 1 succeeds under `h : P ∧ Q` for target `P`. Change the hypothesis to `h : Q ∧ P`, leaving the goal unchanged. For arbitrary propositions `P` and `Q`, the former script now selects a proof of `Q`, while `exact h.right` is appropriate. The script's spelling and its old score have not changed. The formal obligation has.

This illustrates a general problem. A previously tested patch receives a dependency update. A theorem is reused under changed imports. A statistical claim is extended to observations collected under a different sampling procedure. Surface continuity of an artifact establishes no corresponding continuity in its warrant.

Let the *validation context* be represented schematically by

$$
\mathcal C=(c,A,\Gamma,K,V,\omega).
$$

Here $c$ is the assessed artifact, $A$ the asserted target, $\Gamma$ its assumptions, $K$ the governing formal or empirical semantics, $V$ the assessment procedure, and $\omega$ the operational environment. In nonformal domains, the components need corresponding domain-specific definitions. The verdict establishes a scoped statement about this context, tied to its assessment conditions.

For a formal proof, rechecking in $\mathcal C'$ or establishing a property-preserving mapping supplies a path to renewed acceptance. For a patch, the evidence might consist of regression tests under the updated dependencies or a verified compatibility argument. For a statistical model, the evaluation population and explicit shift assumptions are central. Program equivalence provides no evidence of predictive generalization across populations. **Transport of formal validity and transport of statistical performance have distinct proof obligations.**

Context changes need not destroy validity. The claim is narrower: the old observation alone does not decide the new case. The evidential history identifies what changed, what was preserved, and what further assessment supports the intended use.

Evidence transfer is consequently a *separate operation* from the production of a new score. Denote the attempted transfer abstractly by

$$
\operatorname{Transport}(Q,\mathcal C\rightsquigarrow\mathcal C').
$$

The expression records an attempted transfer, not an inference rule. Its justification must identify the property carried from $\mathcal C$ to $\mathcal C'$ and the argument supporting that transfer. Without it, the scope of the original verdict in the new context is unresolved. Hashes and version identifiers identify the objects without establishing semantic equivalence.

The link from structural preservation to evidential preservation has a precise limit. Even a warranted transformation is relevant only for the property it preserves, under the assumptions establishing that preservation. Records have practical value if they expose those assumptions and prevent unwarranted extension of earlier verdicts.

## 7. From evidence to a decision

Calibration relates prospective numerical predictions to a defined outcome. Let $Y=1$ denote completion accepted by a specified proof checker and $\widehat p$ the predicted probability of that event. Relative to a fixed joint distribution over candidates, contexts, predictions, and outcomes, ideal calibration is

$$
\mathbb E[Y\mid\widehat p]=\widehat p\quad\text{almost surely}
$$

This is a distributional condition, not a guarantee for an individual proof attempt. Finite samples permit only estimates subject to uncertainty. Proper scoring rules, including the Brier and logarithmic scores, assess probabilistic predictions beyond their ranking performance [12].

The event and population are decisive. Calibration for parser acceptance says little about hidden behavioral tests. Calibration for routine repairs need not transfer to security-sensitive changes. Calibration, discrimination, performance on rare events, and decision quality assess different properties. Repair effort depends on the repair policy, tool budget, and cost definition; it is no intrinsic scalar property of a defective artifact.

Calibration leaves the decision problem unresolved. The cost of checking influences which candidates warrant attention, while a high predicted success rate supplies no authority for unsafe operations. One idealized rule minimizes expected loss over independently authorized actions,

$$
a^*\in\arg\min_{a\in\mathcal A_{\mathrm{authorized}}(I)}
 \mathbb E[\ell(a,Z)\mid I],
$$

where $I$ is the evidence available at decision time, $Z$ the relevant outcomes, and $\mathcal A_{\mathrm{authorized}}(I)$ a nonempty policy-permitted action set, including deferral where appropriate. This equation defines neither the loss function nor the authority. It describes the role of predictive information in an idealized choice under those independently supplied commitments. For inexpensive proof search, low probability might justify a speculative check. For physical intervention, high probability alone supplies no permission to act.

Selective classification and conformal risk control address related statistical decisions under specified assumptions and losses [13, 14]. Their results warrant attention, especially where a system abstains or defers to a stronger validator. They do not turn an arbitrary model score into a finite-sample guarantee, and their guarantees have defined sampling, exchangeability, or other methodological conditions. This essay proposes an interpretation discipline for heterogeneous artifacts, distinct from those established prediction and risk-control methods.

The interface admits a compact summary without conflating these roles.

$$
\operatorname{Decision}=\delta(\text{artifact},Q^+,\text{policy},\text{authority},\text{context}).
$$

Here $Q^+$ is the scoped information already available to the decision-maker. Decisions made before assessment necessarily use $Q^-$. The function $\delta$ is a policy or institutional rule, not an additional typing judgment. Its distinct inputs prevent a probability estimate from being silently converted into permission.

Repair illustrates the temporal order once more. Rejection of `exact h` in the opening example supplies information for constructing `exact h.left`. The repaired script is a distinct candidate. The new prospective score refers to a new information history, potentially including the earlier diagnostic. Evaluating that score fairly means recording that history and excluding only information unavailable at its actual prediction time. Reusing a previous candidate's validation result as if it described the revised candidate would misstate the evidence.

## 8. Testing whether the distinction is useful

The proposal warrants study only to the extent that these distinctions improve outcomes beyond existing scores, validator logs, and ordinary provenance. The evaluation must separate effects of information content from effects of how that information is presented.

For a reviewer study, fix candidate artifacts, validation outcomes, checker access, and decision budgets. Randomize reviewers or trials across a standard-information condition, a score-only condition, and a condition that includes score semantics, provenance, applicability limits, and calibration information. Provide a plain-language explanation control with comparable information and length. The causal comparison must identify whether the intervention adds predictive information, changes presentation, or changes the review policy.

On a fixed candidate set, unchanged score values have unchanged ROC-AUC, regardless of attached labels. A structured representation might nevertheless support a separately trained target-specific predictor, reduce mistaken reuse of old evidence, or lead reviewers to request appropriate revalidation. Such gains need distinct endpoints and controls. Field ablations identify the incremental contribution of provenance, uncertainty, and scope declarations.

Predictive tests use information available at the specified decision time. They exclude the current checker result, subsequent diagnostics, and future repair, while retaining earlier feedback legitimately available to an iterative agent. Calibration fitting and policy selection must be completed without access to the held-out test outcomes. Splits account for repeated variants of the same proof, shared repository history, and near-duplicate tasks. Search creates selection effects because rank-based policies validate a nonrandom subset of proposed candidates. Metrics must name the sampled population and the validation-selection mechanism, including any unobserved labels.

Retrospective studies use $Q^+$ under matched access to past validation outcomes. Candidate quality must remain fixed if the study attributes an improvement to the record. Transport experiments change one stated element of the context and ask whether a reviewer or automated policy identifies the resulting revalidation obligation. Ground truth concerns whether transfer is supported, not a presumption that every change invalidates the artifact.

Endpoints follow the intended use. Predictive performance uses discrimination, proper scoring rules, and calibration diagnostics for a prespecified event. Repair studies report reviewer time, edits, and validator calls separately under a defined repair policy. Decision studies measure erroneous approval, unjustified evidence transfer, appropriate deferral, and missed valid opportunities, with cost and authority held fixed. Repeated runs and uncertainty intervals support interpretation. Substantial distribution shifts and high-consequence errors warrant separate analysis.

Evidence in favor of the proposal would identify a measurable improvement attributable to a defined field or decision procedure, not to longer annotations or stronger validators. The opposite result is equally informative. An existing validator interface might already communicate all information necessary for the task, making further recording redundant. No empirical benefit is asserted in this essay.

## 9. Limits of the analogy

The Curry–Howard correspondence concerns exact formal judgments. Predictive scores on candidate proofs do not extend it, and scientific hypotheses have no general proof-as-program interpretation. The correspondence functions here as a reference point for distinguishing proposals from accepted judgments. Extensions to software assessment and scientific inference retain their own, explicitly different standards.

A second limitation is heterogeneity. Kernel checking, finite software tests, expert review, and scientific replication establish different properties. No universal acceptance probability spans these procedures. Likewise, a model-relative posterior is not properly evaluated by the same calibration experiment as a prospective checker-success predictor. In some settings, representative data for calibration are unavailable, and a record must report that limitation instead of presenting an unsupported numerical degree of certainty.

Institutional use introduces a further risk. Structured annotations might create an appearance of rigor while leaving defective specifications, weak validators, and unauthorized operations untouched. Their practical significance rests on an explicit account of what an assessment establishes, which contexts preserve its conclusions, and which decisions the information changes.

## 10. From warranted artifacts to effectful systems

Candidate proofs, model scores, and checker verdicts belong to different judgments. This separation extends to software and empirical inquiry, with their own assessment procedures and limits. Quantitative evidence gains meaning through a specified target, context, and decision, while composition or revision creates a further question about which conclusions survive.

The opening Lean example shows this progression in miniature. The model initially favors a rejected candidate, and the diagnostic motivates a repair assessed independently. A subsequent change of formal context alters which projection is valid. No single confidence label captures these transitions. The evidential history does, provided it preserves the changes in the objects and standards being assessed.

*Effectful and Conceptual Intelligence* takes the next step, from assessed artifacts to operations that modify memory, files, institutions, or physical environments. At that stage, interpretation of evidence becomes inseparable from preconditions, authority, effects, and recovery. **A score concerns a specified question and assessment, while permission to act depends on independent authority and applicable conditions.**

## Appendix. Minimal evidence contract

The following schematic YAML separates information available at proposal time from later observations. It is an illustration, not a validated data schema or interoperability standard. Identifiers need domain-specific canonicalization. The artifact digest attests to bytes, not correctness.

```yaml
candidate:
  artifact_id: sha256-of-exact-input-bytes
  target_id: specification-and-version
  context_id: formal-assumptions-dependencies-and-environment
prospective:
  producer_id: model-and-decoding-configuration
  observed_at: proposal-time
  score:
    kind: generation_probability
    value: null                 # fill from an actual observation
    conditioning_id: model-input-and-candidate-set
    predicted_event: null       # set only for a predictive score
    calibration_id: null        # no implicit calibration claim
assessment:
  validator_id: declared-validator-and-version
  assessed_property_id: exact-property
  execution_id: null
  outcome: pending              # complete, continue, reject, indeterminate
  assumptions: []
  diagnostics: null
transfer:
  successor_context_id: null
  preservation_evidence_id: null
use:
  evidential_scope: proposed-candidate
  authority_reference: null
```

The `prospective` section is completed before the current assessment. The `assessment` section records a later event without overwriting the original score. Every repaired artifact receives a new identity and prediction record. Earlier feedback in its generation history is identified explicitly. The transfer section records a separate justification, with a missing identifier indicating that no preservation evidence has been supplied. Concrete deployments would need a typed field specification, integrity model, event ordering, failure semantics, and independent policy rules.

## References

1. Lean Project. *The Lean Language Reference*, “Tactic Proofs.” [Reference manual](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/).
2. Lean Project. *The Lean Language Reference*, “Validating a Lean Proof.” [Reference manual](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).
3. Robert Atkey. “The Syntax and Semantics of Quantitative Type Theory.” *LICS*, 2018. [Author manuscript](https://strathprints.strath.ac.uk/64031/).
4. Kaiyu Yang et al. “LeanDojo: Theorem Proving with Retrieval-Augmented Language Models.” *NeurIPS*, 2023. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4441469427094f8873d0fecb0c4e1cee-Abstract-Datasets_and_Benchmarks.html).
5. Tim Rocktäschel and Sebastian Riedel. “End-to-End Differentiable Proving.” *NeurIPS*, 2017. [Proceedings](https://papers.nips.cc/paper/6969-end-to-end-differentiable-proving).
6. Ryan Riegel et al. “Logical Neural Networks.” 2020. [arXiv](https://arxiv.org/abs/2006.13155).
7. Reynald Affeldt et al. “Taming Differentiable Logics with Coq Formalisation.” *ITP*, 2024. [Proceedings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2024.4).
8. Chris Heunen, Ohad Kammar, Sam Staton, and Hongseok Yang. “A Convenient Category for Higher-Order Probability Theory.” *LICS*, 2017. [arXiv](https://arxiv.org/abs/1701.02547).
9. Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. “Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting.” *NeurIPS*, 2023. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html).
10. Tamera Lanham et al. “Measuring Faithfulness in Chain-of-Thought Reasoning.” 2023. [arXiv](https://arxiv.org/abs/2307.13702).
11. Margaret Mitchell et al. “Model Cards for Model Reporting.” FAT*, 2019. [Proceedings](https://doi.org/10.1145/3287560.3287596).
12. Tilmann Gneiting and Adrian E. Raftery. “Strictly Proper Scoring Rules, Prediction, and Estimation.” *Journal of the American Statistical Association* 102, 2007, pp. 359–378. [Publisher](https://doi.org/10.1198/016214506000001437).
13. Yonatan Geifman and Ran El-Yaniv. “Selective Classification for Deep Neural Networks.” *NeurIPS*, 2017. [Proceedings](https://proceedings.neurips.cc/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html).
14. Anastasios Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. “Conformal Risk Control.” *ICLR*, 2024. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html).
15. World Wide Web Consortium. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Specification](https://www.w3.org/TR/prov-dm/).
16. Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curtmola, and Justin Cappos. “in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes.” *USENIX Security*, 2019. [Proceedings](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias).
