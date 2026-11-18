# Lambek Machines

## Abstract

A fluent linguistic output might carry an incorrect interpretation. The error might concern argument binding, attachment, quantifier scope, or the composition of structures unseen during training. *Lambek Machines* investigates whether explicit categorial composition helps language systems identify and correct such failures. The essay specializes Compositional Intelligence to the relation from lexical types and grammatical derivations to independently evaluated semantic artifacts.

A Lambek Machine is defined operationally as a language system with an inspectable typed-compositional interface. The interface might reside in a native architecture, an auxiliary predictor, a decoder constraint, or an external analyzer. Nothing in this definition establishes that a transformer implements Lambek calculus internally. Functorial Language Consistency (FLC), the associated evaluation scheme, compares interpretation across licensed linguistic transformations, with separate measurements of path agreement, semantic correctness, and coverage.

The contribution is a proposed comparative design, not an empirical result. Existing work already investigates supertagging, structured syntactic prediction, external categorial reconstruction, compositional semantic parsing, and scoped semantic invariance. The remaining question concerns *incremental and attributable* value. Under comparable data, computation, and evaluation, does structured category representation or derivation supervision improve independently checked semantic outcomes beyond competing structural signals? The essay also establishes a limitation of its own consistency criterion: under coherent equivalence and transformation assumptions, correct interpretation at both endpoints entails path agreement. FLC must consequently earn independent value through reference-sparse diagnosis, error localization, or repair. No experiment or performance gain is reported.

## 1. Language as a compositional artifact

The preceding essays introduce three commitments. Semantic Participation concerns the conditions under which an output belongs to a structured target environment. Typed Generativity treats generation as construction relative to an inferred target type. Functorial Consistency asks whether specified transformations agree across a source representation and its target interpretation. Natural language supplies a concrete setting in which these commitments meet: sentences have lexical and syntactic structure, interpretations depend on composition, and controlled transformations expose particular semantic obligations.

A fluent response might nonetheless invert thematic roles, attach a modifier to the wrong constituent, or change the scope of a quantifier. Those errors concern the interpretation of the linguistic artifact, not its surface acceptability. An explicit grammar-as-logic interface makes some of the underlying dependencies inspectable. Its scientific value depends on the additional failures it identifies, the corrections it supports, and the semantic performance it improves relative to credible alternatives.

This essay develops that hypothesis without assuming that human language is exhausted by categorial grammar. Discourse, pragmatic inference, reference, social context, and situated use introduce obligations outside the formal fragment studied here. The intended result is a bounded instrument for investigating compositional behavior in language systems.

## 2. Thesis, definition, and scope

The central hypothesis is that exposing typed grammatical composition improves at least one of three measurable outcomes: downstream semantic accuracy, transformation-sensitive semantic consistency, or the usefulness of error diagnosis and repair. Each outcome must be evaluated against the cost and performance of alternative structural representations.

A **Lambek Machine** is a language system equipped with an observable typed-compositional interface connecting lexical categories, grammatical composition, and a specified semantic target. The interface might be native to the model, produced by an auxiliary prediction head, imposed during decoding, or supplied by a separate analyzer. Its presence is an operational property of the complete system. It does not establish that the underlying neural model implements the Lambek calculus internally.

The name acknowledges Joachim Lambek's grammar-as-logic program. The experimental interface also admits related but mathematically distinct formalisms, including Combinatory Categorial Grammar (CCG), Lambek Categorial Grammar (LCG), pregroup grammars, and Abstract Categorial Grammars (ACG). Results obtained under one formalism must identify that formalism explicitly; they do not automatically extend to the others.

This boundary matters in particular for claims about semantics. Supertag prediction measures lexical-category classification. Grammatical derivability measures whether categories compose under a specified calculus. Semantic correctness measures whether the resulting target interpretation expresses the intended relations. These are separate outcomes, and success at an earlier stage does not entail success at a later one.

## 3. Formal core

Let an utterance consist of ordered tokens \(w_1,\ldots,w_n\), each assigned a lexical category \(w_i:A_i\). In the associative Lambek calculus a derivation of sentence type \(S\) has the form

\[
\pi:A_1,\ldots,A_n\vdash S.
\]

The antecedent is ordered. Structural exchange is unavailable, and the directional divisions \(A/B\) and \(B\backslash A\) specify the side from which a missing argument is supplied. This is a statement about one proof calculus. CCG, pregroups, and ACG have their own rules, interpretation procedures, and expressive boundaries; an implementation must identify its chosen formalism instead of treating these systems as interchangeable.

Given lexical denotations and a specified interpretation of grammatical proofs, a derivation induces a semantic composition. Under an appropriate monoidal interpretation, its type has the schematic form

\[
\llbracket\pi\rrbracket:
\llbracket A_1\rrbracket\otimes\cdots\otimes\llbracket A_n\rrbracket
\longrightarrow\llbracket S\rrbracket.
\]

The tensor notation belongs to the selected semantic model. Neither grammatical derivability nor the existence of such a map independently establishes a correct interpretation of a particular utterance.

Consider *Ada examined Bea*. In a simplified analysis, the two proper names receive noun-phrase type \(NP\), while *examined* receives transitive type \((NP\backslash S)/NP\). The derivation follows the directional applications

\[
\begin{aligned}
 &NP,\ (NP\backslash S)/NP,\ NP\vdash S,\\
 &(NP\backslash S)/NP,\ NP\vdash NP\backslash S,\\
 &NP,\ NP\backslash S\vdash S.
\end{aligned}
\]

In a stipulated simple extensional interpretation, the verb first receives its object and subsequently its subject, producing \(\mathrm{examine}(\mathrm{ada},\mathrm{bea})\). This toy derivation illustrates the passage from syntactic well-formedness to semantic interpretation; it does not settle reference, ambiguity, tense, or discourse commitments.

The distinction also limits failure attribution. A wrong supertag might prevent any derivation, yet a grammatical derivation might encode the wrong attachment. A correct derivation under one lexical assignment might yield a semantically incorrect artifact under an inaccurate lexical denotation. An observed correlation from a category error to a semantic error does not by itself identify a causal mechanism. Repair and intervention experiments must manipulate the suspected source of failure rather than infer causation from diagnostic labels alone.

## 4. Established work and the remaining question

The formal foundations are established. Lambek (1958) gives the grammar-as-logic starting point; Bangalore and Joshi (1999) develop supertagging as an approach to almost parsing; CCGbank (Hockenmaier and Steedman, 2007) provides annotated CCG derivations; de Groote (2001) introduces Abstract Categorial Grammars; and Coecke, Sadrzadeh, and Clark (2010) connect grammatical reduction with distributional semantic composition. These traditions motivate an interface, although their proof theories and semantic models are not identical.

The empirical record prevents an expansive novelty claim. COGS and SLOG probe lexical and structural generalization. Petit, Corro, and Yvon (2023) report improved performance on COGS through a graph-parsing design incorporating supertagging, valency constraints, matching, and training changes. The contribution of supertagging cannot be separated from all accompanying components solely by citing the aggregate result. ReCOGS (Wu, Manning, and Potts, 2023) further shows that incidental properties of logical-form encodings can alter the apparent difficulty of semantic generalization. A trustworthy evaluation must decide what constitutes semantic equivalence before scoring model predictions.

Related work has progressed beyond static supertag classification. Zhao and Penn (2024) study LLM-based CCG and LCG supertagging. Tran and colleagues (2026) compare step-by-step reasoning paths for LLM-based CCG parsing and find that parsing strategy affects performance. Zhao and colleagues (2026) investigate reinforcement learning for syntactic prediction, including CCG supertagging. Wang and colleagues (2026) compare structural language-model variants under extensive training and report that architectural gains vary with scaling and the baseline chosen. These results underscore the need to separate the value of a formal representation from the value of a training method, additional supervision, or computation.

Evaluation of semantic consistency also has relevant predecessors. Uceda-Sosa and colleagues (2026) formalize *scoped semantic invariance* and study reliability relative to bounded knowledge-graph domains. FLC is consequently presented as a particular semantic-parsing and transformation-evaluation design, not as the first use of controlled semantic invariance. Its proposed distinguishing obligations are an explicit source-to-target transformation map, independent reference semantics at both endpoints, and joint reporting of commutation and correctness. The relative diagnostic value of these obligations has yet to be demonstrated empirically.

Adjacent work further constrains originality. Deveci (2026) develops a diagnostic framework for natural-language-to-first-order-logic translation, separating formal defects from semantic generalization. Pareschi (2026) proposes external reconstruction of LLM outputs as CCG derivations, explicitly without identifying the transformer's internal computation with CCG. That manuscript is an unreviewed preprint in the source checked here. The external-lifting precedent already rules out a claim of novelty based solely on reconstructing categorial derivations from model outputs. Its remaining contribution must establish a measurable advantage in semantic prediction, diagnostic usefulness, or correction outcomes against existing syntactic and semantic alternatives.

The unresolved question is narrow. Holding the model, exposure, task, and validator as constant as practicable, what benefit is attributable to compositional category representation or derivational supervision over credible alternatives, and at what annotation and inference cost? A secondary question asks whether transformation-based testing retains diagnostic or repair value in settings where independent endpoint references are expensive or incomplete.

## 5. Four intervention levels

The four levels distinguish modes of integration and their evidential obligations. Evidence for one level does not establish the claims of the next.

| Level | Intervention | Principal test |
| --- | --- | --- |
| L1 | Post-hoc categorial analysis of existing model outputs | Do category and derivation diagnostics predict semantic errors or improve repair? |
| L2 | Auxiliary supervision using categories, structured categories, or derivations | Does supervision improve downstream meaning beyond matched alternatives? |
| L3 | Grammar- or semantics-guided decoding | Do constraints improve target validity and semantic correctness without unacceptable losses in task utility or coverage? |
| L4 | Architecture-level typed-compositional inductive bias | Does the architecture improve structural generalization or efficiency in controlled comparisons? |

L1 permits a frozen language model and an external analyzer. L2 changes the training objective or supervised representation. Prompting a model to output categories is a distinct inference-time intervention and must not be conflated with auxiliary training. L3 changes the decoding procedure and is especially pertinent to tasks with an explicitly specified output language. L4 changes the computational architecture itself and would need comparative evidence unavailable in the present essay.

Grammar-constrained decoding has an established literature. For example, Geng and colleagues (2023) study constraints for structured NLP outputs. Such constraints establish membership in a formal output language, subject to implementation correctness; they do not establish the semantic truth of what has been generated. Decoding quality and distributional distortion are additional considerations, as investigated by Park and colleagues (2024). L3 should report validity and semantic correctness as distinct metrics.

## 6. Functorial Language Consistency

Functorial Language Consistency (FLC) operationalizes the commutation-square idea for linguistic interpretation. Let \(X\) denote a task-specific collection of model inputs, including any context genuinely supplied to the model, and \(Y\) a declared semantic-target space. An interpreter \(T:X\to Y\) predicts a semantic artifact. A licensed partial transformation \(f:X\rightharpoonup X\) has a corresponding partial target operation \(g_f:Y\rightharpoonup Y\), defined by the benchmark independently of the model outputs. For inputs in the declared comparison domain, the intended relation is

\[
T(f(x))\ \approx\ g_f(T(x)).
\]

The relation \(\approx\) must be specified for the target and phenomenon. A transformation-level comparison is meaningful only if the chosen target operation is well-defined on the information represented in \(Y\). For example, a transformation dependent on word order cannot be evaluated solely on a target representation that discards all word-order distinctions unless the missing context is explicitly supplied as part of the target operation. Likewise, a target map that simply looks up the expected answer for each test item makes agreement vacuous. The benchmark must state the domain, inputs, and permissible auxiliary metadata for \(g_f\) before any predictions are inspected.

Because \(f\), \(g_f\), and semantic validators might be partial, *coverage is an outcome*. Invalid predicted artifacts, undefined target operations, ambiguous references, adjudication failures, and timeouts must be recorded separately. A failure to produce an evaluable artifact is never counted as semantic correctness or path agreement.

The source-first route applies \(f\) to \(x\), then interprets the transformed input as \(T(f(x))\). The interpretation-first route computes \(T(x)\), then applies \(g_f\) to obtain \(g_f(T(x))\). The benchmark compares the results under \(\approx\). Neither route is assumed to agree with the other.

Agreement is an evaluated obligation, not an equality supplied by the notation. *Functorial* here names the proposed comparison with the preceding essay; no mathematical functor is asserted. Such a claim would need formally specified source and target categories, identities, composition laws, and a mapping preserving them. The benchmark's partial transformations and empirically checked relations do not automatically provide those objects.

A benchmark item \(i\) also contains independently established reference semantics \(y_i\) and \(y_i'\) for its input \(x_i\) and transformed input \(f(x_i)\). Reference validation establishes the intended relationship \(y_i'\approx g_f(y_i)\). With a target-equivalence checker \(E\), define

\[
\begin{aligned}
P_i&=\mathbf{1}\!\left[E\!\left(T(f(x_i)),\,g_f(T(x_i))\right)\right],\\
C_i&=\mathbf{1}\!\left[E\!\left(T(x_i),\,y_i\right)\right]
     \mathbf{1}\!\left[E\!\left(T(f(x_i)),\,y_i'\right)\right].
\end{aligned}
\]

\(P_i\) measures path agreement and \(C_i\) demands correct interpretations at both endpoints. Both are defined only for predeclared, evaluable comparisons. An item with invalid syntax, an undefined target operation, failed reference validation, or an indeterminate equivalence test receives a recorded *indeterminate* status, not a zero silently mixed with confirmed semantic failure. Report (i) coverage over all attempted items, (ii) a conservative full-denominator pass rate that counts indeterminate attempts as nonpasses, (iii) an evaluable-subset conditional rate, and (iv) reasons for non-evaluation. Report the full joint \((P_i,C_i)\) table on the evaluable subset and check its logical constraints under the declared semantics. A conditional path-agreement rate alone invites selective-coverage artifacts.

### 6.1 A limit of the commutation test

The comparison has a useful logical constraint, which prevents overstating its novelty.

**Proposition (endpoint correctness entails path agreement).** Suppose \(\approx\) is an equivalence relation over the relevant target artifacts. Let the target operation \(g_f\) be defined on a domain closed under this equivalence and preserve it, meaning \(a\approx b\) implies \(g_f(a)\approx g_f(b)\) wherever the operation is defined. Suppose also that the independently established references satisfy \(y'_i\approx g_f(y_i)\). Then for any pair of defined predictions,

\[
T(x_i)\approx y_i\quad\text{and}\quad T(f(x_i))\approx y'_i
\quad\Longrightarrow\quad
T(f(x_i))\approx g_f(T(x_i)).
\]

Indeed, the second correct prediction is equivalent to \(y'_i\), the reference transformation identifies \(y'_i\) with \(g_f(y_i)\), and congruence identifies \(g_f(y_i)\) with \(g_f(T(x_i))\). Transitivity completes the argument. This is a short mathematical observation under declared assumptions, not a machine-checked theorem.

Two implications follow. First, in an exact and coherent evaluation, the outcome \((P_i,C_i)=(0,1)\) is impossible. Observing it signals a violated assumption, inconsistent reference or transformation annotations, an unsound or incomplete approximation to equivalence, or an implementation defect. Second, complete and reliable endpoint references already identify all semantic mistakes on the evaluated pair. Path agreement has no logically independent *error-detection* power over that ideal endpoint oracle. Its possible value is operational: detecting suspicious behavior without two full references, characterizing the structure of failures, predicting new failures, or improving repair. This limitation is central to the study's interpretation.

The claim has boundaries. Some practical validators implement graded similarity, heuristic alignment, or execution over finite test instances, where transitivity or congruence is unproven. Their outputs must not be treated as a mathematical equivalence relation. Under those validators, an apparently contradictory cell is a diagnostic flag, not a counterexample to the proposition.

### 6.2 The converse fails

**Why the two outcomes differ.** Consider a meaning-preserving paraphrase family with \(g_f\) equal to the identity on semantic artifacts. An interpreter returning one fixed incorrect artifact for every input has \(P_i=1\) on every valid item, yet \(C_i=0\) wherever its output disagrees with the references. This is a direct counterexample to the implication from commutation to semantic correctness. It establishes the necessity of the endpoint check, not the predictive benefit of FLC over existing evaluations.

The intended transformation must also be identifiable from the model's available input. An ambiguous sentence such as *Every student read a book* does not single out one scope reading without additional context or an annotation policy. For a disambiguation test, one defensible design supplies an explicit context or instruction identifying the reading to both the model and evaluator. Another retains a set of admissible reference readings and scores disambiguation separately. Hidden gold annotations must never be supplied to the model implicitly through an item-specific target map. A target operation selected in response to the model's predicted interpretation would invalidate the comparison.

The transformations differ in their obligations.

| Transformation family | Declared source operation | Target obligation |
| --- | --- | --- |
| Controlled paraphrase | Reformulate under an identified reading | Equivalent target meaning under a declared relation |
| Active–passive | Reorder grammatical roles in a licensed construction | Preserve the specified event participants; disclose any omitted information-structure effects |
| Scope clarification | Select one quantifier or negation reading using supplied context or an explicit instruction | Select the corresponding operator structure |
| Attachment clarification | Resolve a modifier or instrument attachment | Update the specified edge or event role |
| Relative-clause restructuring | Change embedding or extraction | Preserve the stipulated entity–event bindings |
| Coordination restructuring | Change grouping or shared-argument realization | Maintain or intentionally update conjunct structure |
| Modality intervention | Change possibility, permission, or obligation | Apply a declared nonidentity operator update |

A target validator might implement logical equivalence, alpha-equivalence of appropriately normalized forms, denotational equality, semantic-graph equivalence, query-result checks, or an expert review protocol. The implications differ. Agreement on a finite collection of database instances, for example, demonstrates agreement on those instances and no more. Each evaluator needs an explicit soundness boundary, version, error policy, and independent reference checks.

With complete, sound endpoint references, FLC cannot identify additional errors beyond incorrect endpoints under the proposition's assumptions. Its distinct empirical hypotheses concern reference-sparse screening, failure localization conditional on weaker inspection signals, and whether FLC-guided feedback improves repair relative to equally informative controls. Any improvement must be reported with reference-acquisition cost and validator coverage, not inferred from a raw increase in agreement.

## 7. Diagnostic cases

### 7.1 Quantifier scope

Consider *Every student read a book*. Two readings are:

\[
\forall x\,\bigl(\mathrm{student}(x)\Rightarrow
\exists y\,(\mathrm{book}(y)\land\mathrm{read}(x,y))\bigr),
\]

\[
\exists y\,\bigl(\mathrm{book}(y)\land
\forall x\,(\mathrm{student}(x)\Rightarrow\mathrm{read}(x,y))\bigr).
\]

The first permits different books for different students; the second asserts a common book. A context such as *The librarian had selected a particular book; every student read it* supplies a common-book reading. The original sentence is ambiguous. A meaningful test must either provide such disambiguating context to the model or represent the admissible readings explicitly. An evaluator-only choice of interpretation would turn a legitimate ambiguity into an artificial error. Lexical categories alone do not resolve the complete semantic problem; quantifier interpretation must be part of the specified interface.

### 7.2 Prepositional attachment

*The scientist observed the cell with the microscope* permits a natural instrumental reading and a less natural noun-modifier reading. The clarification *The scientist used the microscope to observe the cell* selects the instrument role. A diagnostic record distinguishes syntactic attachment from the resulting semantic edge. Accurate supertags without correct event–instrument binding do not count as semantic success.

### 7.3 Embedded dependencies

In *The paper that the reviewer criticized was accepted*, *the paper* is the object of *criticized* and the subject of *was accepted*. Paraphrase or voice transformations test the persistence of those bindings. A system might produce locally plausible syntax while assigning the reviewer the wrong event role. Categorial derivations are useful here only to the extent that they discriminate such cases or support an effective correction.

### 7.4 Negation and intention

*The system did not intentionally delete the file* has a salient reading in which intentional deletion is denied. The sentence does not, on that reading alone, establish that a deletion occurred or that none occurred. An evaluation item must explicitly encode the intended placement of negation and the intentionality operator. Collapsing the meaning into *the system did not delete the file* loses a distinction that matters to the target interpretation.

### 7.5 Coordination and voice

Voice alternations with overt agents provide useful controls for stable thematic roles. Coordination becomes more diagnostic under embedding or shared arguments, where alternative bracketings induce different semantic relationships. Each item needs a declared reading and an independently checked reference representation. Model fluency and local grammaticality are preliminary measurements, not the criterion for semantic preservation.

## 8. Lambek Auxiliary Supervision: a comparative protocol

Lambek Auxiliary Supervision (LAS) is a proposed comparative study of structural information, with semantic behavior as the main outcome. It separates the formal representation, the means of supplying that representation to the model, and the downstream task. An improved score under additional annotation or stronger optimization alone would not establish an advantage specific to categorial structure.

The study distinguishes four comparator families from three training interventions and one separate decoding experiment.

| Arm | Structural information or intervention | Principal question |
| --- | --- | --- |
| B0 | Base model trained on the downstream task | Reference outcome without an extra structural objective |
| B1 | Dependency supervision | Does ordinary dependency structure account for the gain? |
| B2 | Constituency supervision | Does phrase structure account for the gain? |
| B3 | Semantic tags or semantic-role supervision | Does direct semantic labeling account for the gain? |
| E1 | Flat CCG or LCG category IDs | Does lexical categorial annotation improve semantic behavior? |
| E2 | Categories predicted through their internal compositional syntax | Does structured *parameterization* improve generalization beyond the same categories treated as opaque IDs? |
| E3 | Derivation-aware or reduction-validity training | Do global proof constraints add value beyond local category structure? |
| E4 | Categorially guided decoding | Do inference-time constraints improve well-formedness, meaning, and utility against appropriate constrained-decoding controls? |

E1 and E2 need particular care. A flat supertag ID might already encode an entire category expression such as \((NP\backslash S)/NP\). E2 does not automatically contain more linguistic information. With identical source categories, its potential advantage comes from the *representation and training bias* induced by category constructors, especially on category structures or combinations absent from training. Any comparison claiming additional information must name and measure that information. E3 potentially exposes extra derivational labels, which must be controlled using derivation-level alternatives or explicit annotation-budget comparisons. E4 changes inference, so it is analyzed separately from auxiliary training.

The primary outcome is reference-validated downstream semantic accuracy on a held-out structural-generalization test. The initial confirmatory contrast, if justified by the pilot, compares derivation-aware E3 with the best eligible noncategorial structured baseline selected on a disjoint development set under a predeclared rule. Secondary tests compare E2 with E1 and E3 with E2, and test repair success under blinded feedback. Selection, hyperparameter tuning, and stopping rules must be completed without using the held-out test outcomes. The estimand is a performance difference for the *specified intervention and target population*, not an intrinsic or universal advantage of Lambek calculus.

For a first empirical implementation, the pilot must select one grammar formalism, one semantic representation, and a single endpoint task instead of pooling CCG, the Lambek calculus, ACG, and semantic-graph formalisms as though their annotations were equivalent. A CCG-derived training corpus with an explicitly mapped event–argument semantic target is one plausible initial route, conditional on annotation availability and licensing. The Lambek derivation in Section 3 is a formal illustration; it is not the exact proof calculus of such a CCG-based experiment.

The experiment must satisfy seven design conditions.

1. **Comparable exposure.** Fix the initial checkpoint, downstream examples, preprocessing, evaluation sets, and feasible optimization settings. Record supervision provenance, number of annotated tokens, supervision entropy or label complexity where informative, trainable parameters, total training compute, optimization search, and inference cost. Match annotation budgets when practicable; otherwise conduct cost-sensitive comparisons and state residual confounding.
2. **Information and objective controls.** Compare category IDs with a structured encoding of those same categories, not against a newly enriched annotation corpus. Include shuffled-category targets with a shuffle performed within training only, preserving meaningful marginal properties, and a generic auxiliary objective with comparable loss weight and output size. Compare derivation supervision with other tree-structured objectives to isolate proof-specific structure from an extra training signal.
3. **Support-aware generalization.** A flat-ID supertagger with a fixed output vocabulary is structurally unable to emit a category excluded from its vocabulary. Compare E1 and E2 first on held-out *combinations of already supported categories* to test learned compositional bias without an output-support confound. Treat generation of genuinely unseen category expressions as a separate open-set task; give competitors comparable generative output support or explicitly describe the support mismatch. Record category-tree depth, primitive constructors, training frequency, and actual lexical overlap.
4. **Separated evaluation families.** Split by construction family before generating paraphrases, counterfactuals, and lexical variants. Keep related inputs in one partition. Specify held-out constructions and independent domain-shift examples. Audit public benchmark overlap and distinguish observable leakage controls from unprovable absence of pretraining contamination.
5. **Independently fixed semantic targets.** Establish reference interpretations, transformation operations, ambiguity policies, and validator behavior before scoring model predictions. Validate reference pairs separately. Use expert adjudication for cases beyond deterministic checking; report unresolved cases and reviewer agreement.
6. **Statistical design.** Specify the minimum effect of scientific interest and sample size for a confirmatory follow-up. Report paired item-level differences, uncertainty intervals clustered by construction family, and variability across training seeds. Predeclare the primary arm contrast and how multiple comparisons are handled. The exploratory pilot cannot substitute for a powered claim of superiority.
7. **Coverage and cost.** Preserve all attempted cases in the denominator. Report invalid syntax, undecidable or timed-out validator comparisons, undefined transformations, abstentions, annotation disagreements, repair regressions, and latency. Conditional accuracy on the subset that passes the parser is a different statistic from task-level performance.

The FLC comparison deserves its own reference-sparse study. Within each prespecified transformation family, randomly select pairs for which only one endpoint reference is available to the diagnostic method, while reserving independent annotations of both endpoints for final evaluation. Evaluate whether path-disagreement flags predict a separately adjudicated held-out endpoint error, conditional on available syntax diagnostics and baseline prediction confidence. Measure precision–recall and calibration across families and report the annotation and validation work saved. Keep the final endpoint references hidden from this diagnostic stage; they serve only as an independent assessment. Since path agreement can hold for consistently wrong outputs, no claim of guaranteed error detection follows from the screen.

The study must distinguish **diagnosis** from **intervention**. A category-error tag that predicts a semantic failure is a diagnostic association. Evidence that altering a category-level component improves the semantic output needs a controlled manipulation, such as corrected category feedback versus comparably informative alternative feedback on the same initial error. Oracle categories and oracle derivations can estimate upper bounds, provided they are identified as privileged-information conditions and excluded from deployable model comparisons.

The strongest defensible positive finding would be a reproducible gain in held-out reference semantics under E2 or E3, surviving matched alternatives and sensitivity analyses, with a corresponding account of cost. Improvements confined to supertagging or proof validity remain useful local results and do not answer the central question.

## 9. Benchmark record and error attribution

An implementation needs enough metadata to reconstruct each transformation square and evaluate the two paths independently. The following JSON illustrates the shape of a record; its semantic representation is intentionally small and the annotation fields are illustrative rather than a proposed universal schema.

```json
{
  "id": "voice-001",
  "family_id": "agentive-voice-001",
  "split": "structural_test",
  "grammar_formalism": "CCG",
  "source": {
    "text": "The scientist examined the sample.",
    "reference_semantics": {
      "predicate": "examine",
      "agent": "scientist",
      "patient": "sample"
    }
  },
  "transformation": {
    "type": "voice_alternation",
    "text": "The sample was examined by the scientist.",
    "target_operation": "preserve_event_roles"
  },
  "transformed_reference_semantics": {
    "predicate": "examine",
    "agent": "scientist",
    "patient": "sample"
  },
  "equivalence": {
    "type": "semantic_role_equivalence",
    "validator_version": "to_be_specified"
  },
  "categorial_annotation": {
    "supertags": null,
    "derivation": null
  },
  "annotation_status": "illustrative_unvalidated"
}
```

For actual benchmark use, the record also needs a canonical tokenization, formal category syntax, allowed inference rules, explicit mapping from derivations to the target semantics, source provenance, and split provenance. Null annotations must be represented as missing data, not as successful parses. The example above has not been independently annotated or validated and cannot be counted as an experimental observation. Its null category fields are deliberate and do not support any claim that the associated CCG derivation has been supplied.

The error taxonomy must distinguish lexical-category errors, invalid derivations, syntactically admissible but semantically incorrect derivations, scope drift, attachment drift, thematic-role inversion, long-distance dependency loss, coordination errors, spurious invariance, spurious changes, undefined target maps, and validator disagreement. Each label needs an operational annotation rule. Several error types can apply to one item, so attribution should permit multiple labels and preserve disagreement instead of forcing an arbitrary single cause.

Repair experiments must compare the same initial failures under categorial diagnostics, dependency or constituency diagnostics, semantic feedback, and an unassisted control. Record the corrected target semantics, number of interventions, time and token cost, and whether the repair introduces new errors. Merely presenting a derivation or producing a syntactically valid revision is insufficient.

## 10. Pilot design and metrics

The pilot is exploratory. A concrete initial allocation consists of **400 disjoint evaluation units**, with grouping determined before any training–test split. An evaluation unit is one annotated utterance in the first three tracks and one source–transformation pair in the fourth. Construction-family identifiers group related items for splitting and analysis. The number of distinct surface sentences is a separate inventory. The purpose is to establish annotation reliability, the frequency of identifiable failures, validator coverage, and effect-size variability.

| Track | Evaluation units | Principal measurement |
| --- | ---: | --- |
| Local categories and structured supertags | 150 utterances | Local category accuracy and shared-support structural generalization; separately assess any open-set category task |
| Semantic parsing | 100 utterances | Reference-validated semantic accuracy |
| Scope and attachment | 50 context-specified utterances | Operator placement and semantic attachment |
| Transformation consistency | 100 source–transformation pairs | FLC path agreement, endpoint correctness, and coverage |
| Repair | 30 initially failed units sampled from the above | Randomized comparison of correction feedback; not added to the total |

The four main tracks sum to 400 evaluation units, including 100 two-input transformation pairs. If every transformation uses a distinct new sentence, the raw surface-sentence inventory reaches 500; reuse and variants must be logged explicitly. The 30-unit repair experiment is a selection from the 400 and is not an extra 30-unit benchmark track. Sampling from failures must be defined before reviewing the treatment arms to prevent favorable case selection.

For transformation items, report the full joint table of path agreement and both-endpoint correctness on evaluable pairs, and disclose undefined, invalid, and indeterminate outcomes on the full population. Under exact equivalence and a well-defined target operation, the correct-endpoints/disagreeing-path cell must be empty; any occurrence triggers an audit of annotations, domain restrictions, equivalence implementation, and reference consistency before substantive interpretation. The table also distinguishes consistently wrong commuting predictions from correct commuting predictions. For semantic endpoints, report the evaluator and the reference representation rather than relying on exact output-string equality. For diagnostics, predefine a way to test *incremental* error localization relative to ordinary endpoint accuracy and to dependency- or semantic-feedback controls.

Results must be disaggregated by held-out construction, category depth, transformation type, formalism coverage, and annotation certainty. With a small number of construction families, ordinary item bootstrap intervals are misleading; use uncertainty estimation that acknowledges the construction-family grouping and the stochastic variation from model training. The pilot determines whether a larger preregistered experiment is justified, rather than establishing decisive evidence by itself.

## 11. Interpretation and falsification

The hierarchy of evidential claims follows the outcome actually measured. Better supertagging establishes improved category prediction. Better reduction validity establishes more outputs accepted by a declared proof system. Improved reference-validated semantics under E1 supports local categorial supervision in the tested task. Reproducible additional gains from E2 over E1, or E3 over E2 and competing structured controls, support a narrower contribution from category composition or derivational information.

FLC has a separate burden. Under coherent exact equivalence, fully correct endpoints already force agreement, making FLC logically redundant as an error detector relative to two complete reference checks. The relevant evidence is whether path tests improve diagnosis under incomplete reference information, identify failure mechanisms at lower cost, or select effective repairs. Agreement gains without endpoint improvement cannot establish semantic improvement. Endpoint gains without a distinctive diagnostic benefit establish downstream improvement, not an independent value of the commutation test.

The following outcomes count against stronger claims.

- No improvement in downstream reference semantics despite higher supertag or derivation-validity scores.
- Equivalent semantic gains from dependency, constituency, semantic tags, or other structured supervision at comparable cost.
- No E2 advantage over the same category information encoded as flat IDs on held-out recombinations within the shared output support, or apparent gains arising exclusively from the flat classifier's inability to emit excluded categories.
- No E3 advantage over comparable tree- or constraint-based objectives once additional derivation labels are accounted for.
- No informative FLC signal under reference-sparse evaluation beyond comparable confidence, syntax, or semantic diagnostics, or no improvement in cost-adjusted repair outcomes.
- No benefit to repair quality, correction rate, or error-localization cost under blinded feedback comparisons.
- Validator disagreement, coverage failure, or annotation cost too large to support a trustworthy conclusion.

A null or negative outcome under the specified model and data regime constrains the corresponding intervention claim. It does not settle the merit of every categorial calculus, every natural language, or every future architecture. Positive findings likewise cannot establish any particular internal mechanism of a pretrained transformer without separate mechanistic interventions.

## 12. Objections and limitations

One objection is that pretrained language models already represent substantial syntactic information. The proposal is compatible with this observation. Its test is incremental value, not the existence of syntax in neural representations. Strong implicit performance raises the evidential threshold for explicit structure.

A second objection concerns expressivity. Categorial formalisms differ in their treatment of word order, extraction, coordination, discontinuity, and semantic composition. No single calculus in the proposed comparison is assumed to cover unrestricted language. Formalism-specific coverage must be measured, and unsupported constructions must not disappear from reported denominators.

A third objection is that semantic representations import assumptions of their own. Logical forms can encode incidental syntactic choices, and agreement on a finite set of executions can miss inequivalence. Multiple legitimate interpretations of an ambiguous sentence further complicate gold labels. This is why the benchmark must preserve ambiguity policies, use validators appropriate to the claim, and distinguish annotation uncertainty from model error.

A fourth objection concerns intervention confounding. If a model with derivation supervision receives more annotation, training compute, or decoding constraints than a baseline, the improvement might reflect those advantages rather than Lambek-specific structure. The experiment must document those differences and, where feasible, equalize them through matched controls.

Finally, grammar-constrained generation might improve syntactic validity at the expense of diversity, latency, coverage, or task utility. A formal guarantee about output membership does not establish the adequacy of the generated interpretation. The result is valuable only relative to the intended use and its stated constraints.

## 13. From language to architecture

Lambek Machines supplies a controlled linguistic test of a broader question. The relevant objects are categories, derivations, semantic interpretations, and transformation maps. The relevant commitments are derivability, interpretation, admissible transformation, and independently evaluated correctness. If exposing some of these commitments produces measurable gains, subsequent architectural work can investigate whether a native representation is more effective than an auxiliary analyzer or external constraint.

The next essay, *Algebraic Architectures*, extends that question to model families organized around specified objects, transformations, constraints, and validators. The language case also contributes a caution: formal-looking commutation diagrams do not supply independent correctness guarantees. Architectural claims need specified semantics, the proper proof obligations, and empirical tests of benefits beyond what a complete reference oracle already establishes.

## 14. Conclusion

Lambek Machines proposes a testable interface between typed grammatical composition and neural language behavior. Its purpose is to determine whether lexical categories and their derivations improve semantic interpretation, transformation consistency, diagnosis, and repair beyond simpler structural alternatives. The framework permits external analysis, auxiliary supervision, constrained decoding, and architectural design, while keeping their evidential claims separate.

The decisive outcome is not a higher supertag score or a valid grammatical proof. It is an attributable improvement in independently evaluated semantic interpretation under credible comparators, or a demonstrated diagnostic or repair advantage under incomplete reference information. The formal relationship between correct endpoints and path agreement makes the evaluation proposal more constrained, and more informative, than a claim of general consistency. The remaining contribution is to establish where categorial structure supplies value beyond existing methods, under what assumptions, and at what total cost.

## References

The following entries anchor the historical and empirical claims made above. The bibliography documents prior work; it does not constitute evaluation evidence for the proposed protocol. The Pareschi entry is identified as an unreviewed preprint.

1. Lambek, J. (1958). [The Mathematics of Sentence Structure](https://doi.org/10.1080/00029890.1958.11989160). *The American Mathematical Monthly*, 65(3), 154–170.
2. Bangalore, S., & Joshi, A. K. (1999). [Supertagging: An Approach to Almost Parsing](https://aclanthology.org/J99-2004/). *Computational Linguistics*, 25(2), 237–265.
3. de Groote, P. (2001). [Towards Abstract Categorial Grammars](https://aclanthology.org/P01-1033/). *Proceedings of the 39th Annual Meeting of the ACL*, 252–259.
4. Hockenmaier, J., & Steedman, M. (2007). [CCGbank: A Corpus of CCG Derivations and Dependency Structures Extracted from the Penn Treebank](https://aclanthology.org/J07-3004/). *Computational Linguistics*, 33(3), 355–396.
5. Coecke, B., Sadrzadeh, M., & Clark, S. (2010). [Mathematical Foundations for a Compositional Distributional Model of Meaning](https://arxiv.org/abs/1003.4394). arXiv:1003.4394.
6. Kim, N., & Linzen, T. (2020). [COGS: A Compositional Generalization Challenge Based on Semantic Interpretation](https://aclanthology.org/2020.emnlp-main.731/). *Proceedings of EMNLP 2020*.
7. Petit, A., Corro, C., & Yvon, F. (2023). [Structural Generalization in COGS: Supertagging Is (Almost) All You Need](https://aclanthology.org/2023.emnlp-main.69/). *Proceedings of EMNLP 2023*, 1089–1101.
8. Li, B., Donatelli, L., Koller, A., Linzen, T., Yao, Y., & Kim, N. (2023). [SLOG: A Structural Generalization Benchmark for Semantic Parsing](https://aclanthology.org/2023.emnlp-main.194/). *Proceedings of EMNLP 2023*, 3213–3232.
9. Wu, Z., Manning, C. D., & Potts, C. (2023). [ReCOGS: How Incidental Details of a Logical Form Overshadow an Evaluation of Semantic Interpretation](https://aclanthology.org/2023.tacl-1.96/). *Transactions of the Association for Computational Linguistics*, 11, 1719–1733.
10. Geng, S., Josifoski, M., Peyrard, M., & West, R. (2023). [Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning](https://aclanthology.org/2023.emnlp-main.674/). *Proceedings of EMNLP 2023*.
11. Zhao, J., & Penn, G. (2024). [LLM-Supertagger: Categorial Grammar Supertagging via Large Language Models](https://aclanthology.org/2024.findings-emnlp.39/). *Findings of EMNLP 2024*, 697–705.
12. Park, K., Wang, J., Berg-Kirkpatrick, T., Polikarpova, N., & D'Antoni, L. (2024). [Grammar-Aligned Decoding](https://proceedings.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html). *Advances in Neural Information Processing Systems 37*.
13. Tran, T.-A., Han, N., Ishii, T., & Miyao, Y. (2026). [Step-by-Step CCG Parsing with Large Language Models](https://aclanthology.org/2026.findings-emnlp.1412/). *Findings of EMNLP 2026*, 30093–30115.
14. Zhao, J., Wang, Y., Liu, J., Zhang, X., Cao, L., Huang, J., Zhao, Y., Cai, R., Ding, Y., & Penn, G. (2026). [Syntactic Prediction through Reinforcement Learning](https://aclanthology.org/2026.emnlp-main.283/). *Proceedings of EMNLP 2026*, 6477–6492.
15. Wang, P., Zhang, Z., Lou, C., & Tu, K. (2026). [A Scaled-Up Empirical Study of Syntactic Language Models](https://aclanthology.org/2026.emnlp-main.1225/). *Proceedings of EMNLP 2026*, 27961–27976.
16. Uceda-Sosa, R., Chang, M., Natesan Ramamurthy, K., & Singh, M. (2026). [Scoped Semantic Invariance as a Foundation for LLM Reliability](https://aclanthology.org/2026.emnlp-main.2545/). *Proceedings of EMNLP 2026*, 57863–57884.
17. Deveci, İ. E. (2026). [A Diagnostic Framework for Compositional Generalization via NL-to-FOL Translation](https://doi.org/10.1007/s10849-026-09480-0). *Journal of Logic, Language and Information*. Published 13 June 2026.
18. Pareschi, R. (2026). [From Dependency to Compositionality: A Neurosymbolic Lifting of LLM Outputs via Combinatory Categorial Grammar](https://arxiv.org/abs/2607.18961). *arXiv preprint*, arXiv:2607.18961. Unreviewed in the checked source.


## Appendix. Minimal FLC validator contract

The following is an *illustrative* validation contract for a restricted event–role target; it is not implemented or certified as part of this essay. Its purpose is to specify the interface a reproducible study would need before assigning correctness labels.

A semantic artifact contains a declared predicate, ordered event arguments identified by semantic roles, a quantifier/scope component if the phenomenon needs it, and an annotation of any excluded phenomena. A canonicalization policy maps permissible superficial differences in variable identifiers and serialization into the same semantic class. Canonicalization must never erase event-role inversions or scope distinctions that the benchmark purports to test. The task specification states whether reference identity and discourse information are abstracted away.

For a voice-alternation item with two explicitly named participants, take the source *Ada examined Bea* and the transformed sentence *Bea was examined by Ada*. Fix both references independently as the role representation `{"predicate":"examine","agent":"ada","patient":"bea"}`. The target operation preserves that representation. An interpreter that swaps `agent` and `patient` at both endpoints passes the path-agreement check and fails the reference-correctness check. An interpreter that swaps the roles at exactly one endpoint fails both. An interpreter with correctly represented roles at both endpoints passes both. These logical outcomes follow from the stipulated equivalence policy; they are not observations about any language model.

A validator must return one of `equivalent`, `inequivalent`, or `indeterminate`, with a machine-readable reason for indeterminacy. Before evaluating model outputs, the research team must run at least the following reference-level checks: identical artifacts compare equivalent; different variable names normalize appropriately; swapped thematic roles compare inequivalent; forbidden scope changes compare inequivalent; invalid artifacts are rejected with an error; transformation references satisfy their declared target operations; and declared congruence holds on the supported domain. Where congruence has only been tested on a finite sample, record it as tested behavior instead of a general guarantee.

Retain a version identifier for the semantic schema, canonicalizer, equivalence checker, transformation operator, reference annotations, and adjudication policy. Inference outputs and evaluation results must include original model outputs, canonical artifacts, checked domain membership, checker outcome, and any exception or timeout. An implementation meeting this contract would support reproducible bounded comparisons; it would not, by itself, validate semantic interpretations outside the declared domain.
