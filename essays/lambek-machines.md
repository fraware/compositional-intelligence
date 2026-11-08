# Lambek Machines

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 d7fa42921bd8ec0664fa1f23f3462bce1e26531dee2b6ad6db7210f92f128ad0; source Essay4_Lambek_Machines_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Lambek Machines applies the Compositional Intelligence framework to natural language. Semantic Participation defines artifact membership in structured environments. Typed Generativity models generation as candidate-inhabitant construction under an inferred target type. Functorial Consistency evaluates path agreement across transformations and target transports. This essay specializes that sequence to linguistic artifacts, where grammar-as-logic supplies an explicit account of typed composition.</p>
<p>The paper advances a bounded claim. Categorial type structure has scientific value for language models only insofar as it improves or explains downstream compositional behavior under specified evaluation regimes. The framework therefore avoids attributing Lambek reductions to transformer mechanisms, treating supertagging as semantic understanding, or replacing neural language modeling with symbolic grammar. It instead defines a testable interface between categorial structure and semantic behavior.</p>
<p>The core schema maps lexical items to categorial types, reduces those types through a derivation, and interprets the resulting derivation as semantic composition. A Lambek Machine is any language system that exposes enough of that pipeline for analysis, supervision, constrained generation, interpretability, repair, or architecture design. The proposed Lambek Auxiliary Supervision protocol tests whether categorial signals transfer beyond supertag accuracy to semantic parsing, scope control, attachment resolution, role assignment, and Functorial Language Consistency.</p>
<p>The proposal is falsifiable. A strong result shows that categorial structure improves downstream semantic behavior beyond strong pretrained, dependency-supervised, constituency-supervised, and semantic-tagging baselines. A weak result confines the claim to diagnostic analysis or supertag prediction. A negative result supports rejection of Lambek-specific supervision or architecture claims for the tested regime.</p>
<h2 id="contribution-summary">Contribution summary</h2>
<p class="table-display-caption" id="table-1-caption">Table 1. ID, Contribution, Publication claim</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table 1. ID, Contribution, Publication claim</caption>
<colgroup>
<col style="width: 7%"/>
<col style="width: 22%"/>
<col style="width: 69%"/>
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
<td>Language-domain specialization</td>
<td>Essay 4 instantiates Compositional Intelligence in natural-language artifacts through typed linguistic composition.</td>
</tr>
<tr class="even">
<td>C2</td>
<td>Operational definition</td>
<td>A Lambek Machine is defined by exposed typed-compositional structure, not by an unverifiable claim about hidden model mechanisms.</td>
</tr>
<tr class="odd">
<td>C3</td>
<td>Four-level hierarchy</td>
<td>The essay separates post-hoc categorial analysis, auxiliary supervision, grammar-guided decoding, and architecture-level typed-compositional bias.</td>
</tr>
<tr class="even">
<td>C4</td>
<td>Functorial Language Consistency</td>
<td>The essay instantiates commutation-square evaluation for paraphrase, scope, attachment, voice, coordination, negation, modality, and semantic parsing.</td>
</tr>
<tr class="odd">
<td>C5</td>
<td>Evaluation protocol</td>
<td>Lambek Auxiliary Supervision evaluates downstream semantic transfer against strong syntactic and semantic baselines.</td>
</tr>
<tr class="even">
<td>C6</td>
<td>Falsification policy</td>
<td>The strong claim fails when categorial supervision improves supertagging alone or is matched by simpler labels under downstream metrics.</td>
</tr>
</tbody>
</table></div>
<h2 id="reader-map">Reader map</h2>
<p class="table-display-caption" id="table-2-caption">Table 2. Reader, Recommended path</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table 2. Reader, Recommended path</caption>
<colgroup>
<col style="width: 30%"/>
<col style="width: 69%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Reader</strong></th>
<th scope="col"><strong>Recommended path</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NLP researcher</td>
<td>Sections 1, 3, 4, 6, 7, and 8.</td>
</tr>
<tr class="even">
<td>Semantic parsing researcher</td>
<td>Sections 4, 6, 7, 8.4, and Appendix B.</td>
</tr>
<tr class="odd">
<td>Formal-language or categorial-grammar researcher</td>
<td>Sections 2, 3, 4, 5, and Appendix A.</td>
</tr>
<tr class="even">
<td>AI evaluation researcher</td>
<td>Sections 6, 8, 9, 10, and 12.</td>
</tr>
<tr class="odd">
<td>Series reader</td>
<td>Read after Essay 3 and before Essay 5.</td>
</tr>
</tbody>
</table></div>
<h2 id="position-in-the-compositional-intelligence-series">1. Position in the Compositional Intelligence series</h2>
<p>Essay 4 tests whether the general framework retains technical content in a concrete linguistic domain. Essay 1 defines the membership conditions under which an output qualifies as an artifact in a structured environment. Essay 2 gives the generation-level account in which a model infers a target object and constructs a candidate inhabitant. Essay 3 supplies the transformation test through commutation-square evaluation. The language layer inherits these commitments and asks whether explicit compositional structure improves semantic behavior under controlled transformations.</p>
<p>artifact membership -&gt; target-type inference -&gt; transformation preservation -&gt; typed linguistic composition</p>
<p>A linguistic output should be evaluated as an artifact whose target environment includes grammar, interpretation, and downstream use. A sentence, parse, explanation, or dialogue response has surface acceptability only as a preliminary condition. The relevant membership questions concern lexical roles, argument structure, scope, attachment, semantic composition, discourse function, and permitted interpretation. Fluency gives insufficient evidence for those properties, so Essay 4 treats typed linguistic composition as a candidate evaluation and supervision layer.</p>
<p>Functorial Language Consistency provides the operative bridge from Essay 3 to language. A sentence can be transformed before semantic parsing, or parsed first and transformed inside the target representation. The two paths are compared under an explicit equivalence regime. This formulation turns linguistic compositionality into a path-agreement problem, permitting failures to be localized to lexical typing, reduction, semantic composition, target transformation, or validation.</p>
<h2 id="thesis-and-boundary-conditions">2. Thesis and boundary conditions</h2>
<p>The thesis of Lambek Machines is that grammar-as-logic supplies an explicit structure layer for evaluating, supervising, constraining, and interpreting language models. The claim is empirical and scoped. Categorial structure earns relevance only when it improves semantic behavior, diagnostic resolution, repair quality, or transformation-sensitive evaluation under declared metrics.</p>
<p>The framework treats transformer internals as an object of measurement, not as a premise. Attention heads, hidden states, and token distributions are not identified with Lambek reductions. Supertag prediction is also insufficient as a semantic result. The proposed interface isolates a tractable layer of linguistic structure, namely lexical categories, derivations, reductions, argument structure, and semantic composition. Open-domain discourse, pragmatics, grounding, sociolinguistic context, and task intent require additional machinery and fall outside the strongest claim of this essay.</p>
<p>The proposal is positioned among established literatures without absorbing their claims. Lambek calculus, Combinatory Categorial Grammar, Linear Categorial Grammar, DisCoCat, semantic parsing, supertagging, and grammar-constrained decoding provide the background vocabulary and operational substrates. Lambek Machines names the Compositional Intelligence interface that asks which explicit typed structures help neural language systems preserve meaning under composition and transformation.</p>
<h2 id="formal-core---the-lambek-machine-schema">3. Formal core - the Lambek Machine schema</h2>
<p>The formal core is a typed compositional pipeline from lexical items to semantic artifacts. Let w_i denote lexical items, tau_i their categorial types, pi a derivation from the tensor product of lexical types to a sentence or phrase type S, and [[pi]] the semantic composition map induced by that derivation. The schema is explicit in symbolic categorial parsing, partially explicit in supervised neural systems, and diagnostic in frontier language models whose internal mechanisms require separate evidence.</p>
<p>w_1, ..., w_n</p>
<p>-&gt; tau_1, ..., tau_n</p>
<p>-&gt; pi : tau_1 tensor ... tensor tau_n =&gt; S</p>
<p>-&gt; [[pi]](v_1, ..., v_n)</p>
<p>The schema separates failure modes that ordinary semantic scores tend to merge. A system can assign an incorrect lexical category, choose categories that fail to reduce globally, produce a valid derivation with the wrong semantic operation, or preserve syntax and lose the intended semantic relation. Each failure implies a different intervention. Lexical errors require category-level repair. Reduction failures require global well-typedness constraints. Semantic-composition errors require a target-side equivalence test. A single aggregate score obscures these distinctions.</p>
<p>A Lambek Machine is defined operationally as a language system that exposes typed compositional structure sufficiently for analysis, supervision, constrained generation, interpretability, repair, or architecture design. The definition makes no claim about literal internal execution of Lambek calculus. It specifies the observable interface required for benchmark construction and failure localization.</p>
<h2 id="literature-landscape-and-source-policy">4. Literature landscape and source policy</h2>
<p>The literature supporting Lambek Machines should be used source-functionally. Lambek calculus supplies the grammar-as-logic foundation in which lexical types compose through derivability. Supertagging supplies a practical lexical-category interface. DisCoCat connects grammatical reductions with compositional distributional semantics. Compositional semantic-parsing benchmarks supply controlled tests for syntax-to-meaning generalization. Grammar-constrained decoding supplies operational constraints at generation time. None of these sources validates the Lambek Auxiliary Supervision protocol proposed here.</p>
<p class="table-display-caption" id="table-3-caption">Table 3. Literature, Supported claim, Boundary for this essay</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table 3. Literature, Supported claim, Boundary for this essay</caption>
<colgroup>
<col style="width: 22%"/>
<col style="width: 39%"/>
<col style="width: 38%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Literature</strong></th>
<th scope="col"><strong>Supported claim</strong></th>
<th scope="col"><strong>Boundary for this essay</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Lambek calculus</td>
<td>Grammar-as-logic formalizes syntactic composition through typed derivability.</td>
<td>It supplies the formal anchor, not evidence about current model internals.</td>
</tr>
<tr class="even">
<td>CCG, LCG, and supertagging</td>
<td>Lexical categories provide practical signals for almost-parsing and category-level prediction.</td>
<td>Supertag accuracy is an intermediate metric, not semantic preservation.</td>
</tr>
<tr class="odd">
<td>DisCoCat</td>
<td>Categorical semantics links grammatical reductions with compositional distributional meaning.</td>
<td>It supplies a structural bridge rather than a replacement for frontier language models.</td>
</tr>
<tr class="even">
<td>Compositional semantic parsing</td>
<td>Benchmarks test systematic syntax-to-meaning generalization.</td>
<td>They do not isolate categorial structure as the causal factor.</td>
</tr>
<tr class="odd">
<td>Grammar-constrained decoding</td>
<td>Formal constraints can control generated output structure.</td>
<td>Schema validity alone does not establish semantic equivalence.</td>
</tr>
<tr class="even">
<td>LLM supertagging</td>
<td>Large language models can be evaluated on categorial supertagging.</td>
<td>The downstream transfer claim remains open.</td>
</tr>
<tr class="odd">
<td>Syntax and semantic baselines</td>
<td>Dependency, constituency, and semantic tagging provide strong alternatives.</td>
<td>They are required comparison classes for Lambek-specific claims.</td>
</tr>
</tbody>
</table></div>
<p>The source map fixes the evidential role of each tradition. Lambek 1958 supports grammar-as-logic. Bangalore and Joshi 1999 supports supertagging as almost parsing. Coecke, Sadrzadeh, and Clark 2010 supports the DisCoCat bridge. COGS and SLOG support compositional semantic-parsing context. Zhao and Penn 2024 supports LLM-based categorial supertagging. These sources motivate the research design; the implemented and measured value of Lambek Auxiliary Supervision remains an empirical obligation.</p>
<h2 id="four-levels-of-lambek-machines">5. Four levels of Lambek Machines</h2>
<p>The Lambek Machine hierarchy separates conservative diagnostic uses from stronger claims about supervision, decoding, and architecture. Level 1 and Level 2 are implementable with existing annotation and training pipelines. Level 3 applies grammar or semantic constraints during generation where target representations permit such control. Level 4 proposes architecture-level typed-compositional bias and therefore requires evidence beyond the scope of this essay.</p>
<p class="table-display-caption" id="table-4-caption">Table 4. Level, Name, Description, Evidence required</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="4" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table 4. Level, Name, Description, Evidence required</caption>
<colgroup>
<col style="width: 6%"/>
<col style="width: 21%"/>
<col style="width: 39%"/>
<col style="width: 31%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Name</strong></th>
<th scope="col"><strong>Description</strong></th>
<th scope="col"><strong>Evidence required</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>L1</td>
<td>Post-hoc categorial analysis</td>
<td>Analyze model outputs through categorial tags, reductions, or grammar diagnostics.</td>
<td>Diagnostics predict semantic failures or support repair.</td>
</tr>
<tr class="even">
<td>L2</td>
<td>Auxiliary categorial supervision</td>
<td>Train, prompt, or fine-tune models with supertags, structured categories, reduction validity, or derivation objectives.</td>
<td>Downstream semantic behavior improves beyond strong baselines.</td>
</tr>
<tr class="odd">
<td>L3</td>
<td>Grammar-guided decoding</td>
<td>Use grammar, category, or semantic constraints during generation.</td>
<td>Constraints improve validity, consistency, or interpretability with acceptable utility loss.</td>
</tr>
<tr class="even">
<td>L4</td>
<td>Architecture-level typed-compositional bias</td>
<td>Build model families whose computation is designed around typed composition or resource-sensitive reductions.</td>
<td>The architectural bias improves generalization or diagnostic resolution at scale.</td>
</tr>
</tbody>
</table></div>
<p>The hierarchy constrains publication claims. Evidence for L1 supports diagnostic analysis. Evidence for L2 supports auxiliary supervision. Evidence for L3 supports constrained generation in bounded settings. Evidence for L4 requires architecture comparisons that cannot be inferred from improved supertagging alone.</p>
<h2 id="functorial-language-consistency">6. Functorial Language Consistency</h2>
<p>Functorial Language Consistency instantiates the commutation-square benchmark for linguistic transformations. A sentence x is transformed on the source side by f, translated into a semantic artifact by T, and transformed on the target side by g. The evaluation compares T(f(x)) with g(T(x)) under an explicitly declared equivalence regime.</p>
<p>sentence x --f--&gt; transformed sentence f(x)</p>
<p>| |</p>
<p>T T</p>
<p>v v</p>
<p>semantic artifact T(x) --g--&gt; transformed artifact g(T(x))</p>
<p>Evaluation condition</p>
<p>T(f(x)) approx g(T(x))</p>
<p>The benchmark distinguishes meaning-preserving transformations from controlled semantic changes. Paraphrase and voice alternation often require stable denotation or thematic roles. Scope clarification, attachment clarification, modality changes, and authority-sensitive language require specific target-side updates. The evaluation therefore checks covariance under typed transformation, not invariance under arbitrary perturbation.</p>
<p class="table-display-caption" id="table-5-caption">Table 5. Transformation family, Source-side operation, Target-side expectation</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. Transformation family, Source-side operation, Target-side expectation</caption>
<colgroup>
<col style="width: 23%"/>
<col style="width: 38%"/>
<col style="width: 38%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Transformation family</strong></th>
<th scope="col"><strong>Source-side operation</strong></th>
<th scope="col"><strong>Target-side expectation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Paraphrase</td>
<td>Replace a sentence with a meaning-preserving formulation.</td>
<td>Denotation, semantic graph, or logical form remains equivalent.</td>
</tr>
<tr class="even">
<td>Scope clarification</td>
<td>Resolve quantifier, negation, modality, or adverbial scope.</td>
<td>The semantic artifact records the intended scope operation.</td>
</tr>
<tr class="odd">
<td>Attachment clarification</td>
<td>Fix whether a phrase modifies an event, entity, instrument, or location.</td>
<td>Semantic roles and attachment edges update accordingly.</td>
</tr>
<tr class="even">
<td>Voice alternation</td>
<td>Convert active and passive realizations.</td>
<td>Thematic roles remain stable under syntactic reordering.</td>
</tr>
<tr class="odd">
<td>Relative-clause restructuring</td>
<td>Modify embedded clauses or extraction structure.</td>
<td>Entity-role binding and long-distance dependencies remain correct.</td>
</tr>
<tr class="even">
<td>Coordination restructuring</td>
<td>Change coordination scope or distribute shared arguments.</td>
<td>Conjunct structure and argument sharing are preserved.</td>
</tr>
<tr class="odd">
<td>Negation or modality shift</td>
<td>Clarify the operator scope over events, intentions, permissions, or obligations.</td>
<td>Semantic operators attach to the correct predicate or proposition.</td>
</tr>
</tbody>
</table></div>
<p>The benchmark requires a declared target representation. T can be semantic parsing, logical-form construction, semantic-role labeling, dialogue-act interpretation, query construction, or typed explanation. The equivalence regime can use logical equivalence, denotational equality, graph isomorphism, query-result equality, role equivalence, or reviewed alignment. Reviewed alignment should appear only with rubrics and agreement measurement.</p>
<h2 id="diagnostic-cases">7. Diagnostic cases</h2>
<p>A small set of controlled cases clarifies what the benchmark measures. The cases below are not offered as coverage claims. They isolate recurring failure mechanisms that typed compositional structure should help diagnose or repair.</p>
<h3 id="quantifier-scope">7.1 Quantifier scope</h3>
<p>Quantifier scope exposes the difference between fluent interpretation and recorded semantic choice. In the sentence Every student read a book, the narrow-scope reading assigns a possibly different book to each student, and the wide-scope reading asserts one book read by all students. A commutation item can first clarify the source sentence as There is one book that every student read, then compare the resulting parse with a target-side scope transformation. The failure occurs when the model retains the surface-scope reading after the clarification or changes the logical form without representing the scope operation.</p>
<p>forall student, exists book, read(student, book)</p>
<p>exists book, forall student, read(student, book)</p>
<p>This case limits the Lambek-specific claim. Lexical categories alone are unlikely to resolve all scope phenomena. A successful Lambek Machine interface must connect category structure with the higher-order semantic operations that determine quantifier interpretation.</p>
<h3 id="prepositional-attachment">7.2 Prepositional attachment</h3>
<p>Prepositional attachment tests whether syntactic ambiguity is converted into the correct semantic relation. The sentence The scientist observed the cell with the microscope admits an instrumental reading and an entity-modifier reading. A source transformation that rewrites the sentence as The scientist used the microscope to observe the cell should force the microscope into the observing event. The target-side artifact fails if it leaves the microscope attached to the cell.</p>
<p>instrument(observe, microscope)</p>
<p>modifier(cell, microscope)</p>
<p>The case is useful only when the benchmark records both the syntactic attachment and the induced semantic operation. Category prediction has downstream value here only if it localizes the combinatory role of the prepositional phrase and supports repair of the semantic artifact.</p>
<h3 id="embedded-dependencies">7.3 Embedded dependencies</h3>
<p>Relative clauses test whether a system preserves role bindings across embedded structure. In The paper that the reviewer criticized was accepted, the system must distinguish the object of criticized from the subject of accepted. A useful item transforms the sentence through paraphrase or passive alternation and checks whether the semantic artifact preserves both event roles. The relevant error is not ungrammaticality; it is role collapse across clause boundaries.</p>
<h3 id="negation-and-adverbial-scope">7.4 Negation and adverbial scope</h3>
<p>Negation and adverbial scope test whether operators attach at the correct semantic level. The sentence The system did not intentionally delete the file denies intentional deletion and leaves accidental deletion open. A representation that treats the sentence as simple non-deletion, or as intentional non-deletion, loses the operative distinction. The benchmark should require the target artifact to place negation and intention over the intended predicate structure.</p>
<h3 id="coordination-and-voice">7.5 Coordination and voice</h3>
<p>Coordination and voice provide baseline transformation families whose difficulty increases under embedding. Active-passive alternation alone is often manageable, since thematic roles stay stable under surface-role reversal. Coordination is more diagnostic when shared arguments or distributed predicates are introduced. A system that preserves surface coordination and misassigns agents, patients, or themes fails the semantic artifact test even if its sentence-level output remains fluent.</p>
<h2 id="lambek-auxiliary-supervision-v0.2">8. Lambek Auxiliary Supervision v0.2</h2>
<p>Lambek Auxiliary Supervision is an experimental design for testing downstream transfer from categorial structure. A study that reports supertag accuracy alone supplies insufficient evidence for the strong claim. The target outcome is semantic preservation under controlled transformations, with supertagging treated as an intermediate mechanism.</p>
<p>The central hypothesis is that categorial type supervision improves downstream compositional behavior beyond strong pretrained baselines and simpler syntactic or semantic supervision. The hypothesis has a strict ablation requirement. Gains attributed to Lambek structure must exceed those obtained through dependency labels, constituency labels, semantic tags, flat supertags, or generic structured-output constraints.</p>
<p class="table-display-caption" id="table-6-caption">Table 6. Condition, Description, Purpose</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table 6. Condition, Description, Purpose</caption>
<colgroup>
<col style="width: 10%"/>
<col style="width: 51%"/>
<col style="width: 38%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Condition</strong></th>
<th scope="col"><strong>Description</strong></th>
<th scope="col"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>B0</td>
<td>Baseline model without explicit structure.</td>
<td>Estimate current capability.</td>
</tr>
<tr class="even">
<td>B1</td>
<td>Dependency-supervised baseline.</td>
<td>Test whether ordinary syntax explains the gains.</td>
</tr>
<tr class="odd">
<td>B2</td>
<td>Constituency-supervised baseline.</td>
<td>Test whether phrase-structure labels suffice.</td>
</tr>
<tr class="even">
<td>B3</td>
<td>Semantic-tagging baseline.</td>
<td>Compare against explicit semantic labels.</td>
</tr>
<tr class="odd">
<td>L1</td>
<td>Flat CCG or LCG supertag supervision.</td>
<td>Test lexical categorial signal.</td>
</tr>
<tr class="even">
<td>L2</td>
<td>Structured category supervision.</td>
<td>Test whether category internal structure adds value.</td>
</tr>
<tr class="odd">
<td>L3</td>
<td>Reduction or derivation supervision.</td>
<td>Test global well-typedness beyond local tags.</td>
</tr>
<tr class="even">
<td>L4</td>
<td>Grammar-guided decoding.</td>
<td>Test constrained generation in suitable target environments.</td>
</tr>
</tbody>
</table></div>
<p>The Lambek-specific claim is credible only when the L-conditions improve downstream semantic metrics beyond B1 through B3. A result in which flat supertagging improves and semantic behavior remains unchanged supports a narrower diagnostic claim, not the broader Lambek Machine proposal.</p>
<h2 id="benchmark-schemas">9. Benchmark schemas</h2>
<h3 id="lambek-benchmark-item">9.1 Lambek benchmark item</h3>
<p>lambek_benchmark_item:</p>
<p>id: string</p>
<p>sentence: string</p>
<p>transformation:</p>
<p>family: paraphrase | scope | attachment | voice | relative_clause | coordination | negation | modality</p>
<p>transformed_sentence: string</p>
<p>intended_semantic_effect: string</p>
<p>tokens: list[string]</p>
<p>gold_or_reference_supertags: list[string]</p>
<p>structured_category_representation: object</p>
<p>derivation_or_reduction: object | null</p>
<p>semantic_target:</p>
<p>representation_type: logical_form | graph | query | semantic_roles | other</p>
<p>value: object</p>
<p>target_transformation: object</p>
<p>equivalence_regime: string</p>
<p>validator_or_review_protocol: string</p>
<p>failure_labels: list[string]</p>
<h3 id="model-output-record">9.2 Model output record</h3>
<p>lambek_model_output:</p>
<p>item_id: string</p>
<p>model_id: string</p>
<p>condition: string</p>
<p>predicted_supertags: list[string]</p>
<p>predicted_structure: object | null</p>
<p>predicted_reduction: object | null</p>
<p>predicted_semantic_artifact: object</p>
<p>transformed_predicted_semantic_artifact: object</p>
<p>path_agreement_result: accept | reject | adjudicate</p>
<p>diagnostics: list[string]</p>
<p>repair_trace: string | null</p>
<h3 id="error-taxonomy">9.3 Error taxonomy</h3>
<p class="table-display-caption" id="table-7-caption">Table 7. Failure label, Meaning</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table 7. Failure label, Meaning</caption>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Failure label</strong></th>
<th scope="col"><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>lexical category error</td>
<td>The system assigns an incorrect categorial type to one or more tokens.</td>
</tr>
<tr class="even">
<td>reduction failure</td>
<td>Local categories are plausible but do not compose into the required phrase or sentence type.</td>
</tr>
<tr class="odd">
<td>semantic-composition error</td>
<td>The derivation exists, and the induced semantic operation is incorrect.</td>
</tr>
<tr class="even">
<td>scope drift</td>
<td>Quantifier, negation, modality, or adverbial scope changes incorrectly.</td>
</tr>
<tr class="odd">
<td>attachment drift</td>
<td>Modifier or prepositional attachment binds to the wrong event or entity.</td>
</tr>
<tr class="even">
<td>role inversion</td>
<td>Agent, patient, instrument, theme, or recipient roles are swapped.</td>
</tr>
<tr class="odd">
<td>long-distance dependency loss</td>
<td>An embedded relation or extraction dependency is lost under transformation.</td>
</tr>
<tr class="even">
<td>coordination error</td>
<td>Conjuncts, shared arguments, or distributive structure are misrepresented.</td>
</tr>
<tr class="odd">
<td>spurious invariance</td>
<td>The model keeps a semantic representation unchanged when the transformation should alter it.</td>
</tr>
<tr class="even">
<td>spurious change</td>
<td>The model alters the semantic representation under a meaning-preserving transformation.</td>
</tr>
<tr class="odd">
<td>validator mismatch</td>
<td>The output looks acceptable under one metric and fails the declared equivalence regime.</td>
</tr>
</tbody>
</table></div>
<h2 id="metrics-and-pilot-plan">10. Metrics and pilot plan</h2>
<p>A first pilot should be small enough for expert annotation and large enough to expose diagnostic signal. The recommended study uses 300 to 500 language items distributed across categorial supervision and Functorial Language Consistency tracks. The purpose is diagnostic novelty, not broad benchmark coverage.</p>
<p class="table-display-caption" id="table-8-caption">Table 8. Metric, Measures — Metric, Measures</p>
<div aria-labelledby="table-8-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="8" id="table-8"><caption class="visually-hidden">Table 8. Metric, Measures — Metric, Measures</caption>
<colgroup>
<col style="width: 30%"/>
<col style="width: 69%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Metric</strong></th>
<th scope="col"><strong>Measures</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>supertag accuracy</td>
<td>Local lexical category prediction.</td>
</tr>
<tr class="even">
<td>structured category accuracy</td>
<td>Correct internal category structure, including rare and long-tail categories.</td>
</tr>
<tr class="odd">
<td>reduction validity</td>
<td>Whether predicted categories compose into the intended phrase or sentence type.</td>
</tr>
<tr class="even">
<td>semantic parse accuracy</td>
<td>Correctness of the target semantic artifact.</td>
</tr>
<tr class="odd">
<td>scope accuracy</td>
<td>Correct placement of quantifier, negation, modality, and adverbial scope.</td>
</tr>
<tr class="even">
<td>attachment accuracy</td>
<td>Correct modifier, prepositional phrase, and semantic-role attachment.</td>
</tr>
<tr class="odd">
<td>paraphrase stability</td>
<td>Meaning preservation under controlled paraphrase.</td>
</tr>
<tr class="even">
<td>Functorial Language Consistency</td>
<td>Path agreement under transformation squares.</td>
</tr>
<tr class="odd">
<td>repair usefulness</td>
<td>Whether categorial diagnostics improve correction of failed outputs.</td>
</tr>
<tr class="even">
<td>annotation cost</td>
<td>Human or expert effort per item and agreement rate.</td>
</tr>
</tbody>
</table></div>
<p class="table-display-caption" id="table-9-caption">Table 8. Metric, Measures — Metric, Measures Metric Measures supertag accuracy Local lexical category prediction. structured category accuracy Correct internal category structure, including rare and long-tail categories. reduction validity Whether predicted categories compose into the intended phrase or sentence type. semantic parse accuracy Correctness of the target semantic artifact. scope accuracy Correct placement of quantifier, negation, modality, and adverbial scope. attachment accuracy Correct modifier, prepositional phrase, and semantic-role attachment. paraphrase stability Meaning preservation under controlled paraphrase. Functorial Language Consistency Path agreement under transformation squares. repair usefulness Whether categorial diagnostics improve correction of failed outputs. annotation cost Human or expert effort per item and agreement rate.</p>
<div aria-labelledby="table-9-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="9" id="table-9"><caption class="visually-hidden">Table 8. Metric, Measures — Metric, Measures Metric Measures supertag accuracy Local lexical category prediction. structured category accuracy Correct internal category structure, including rare and long-tail categories. reduction validity Whether predicted categories compose into the intended phrase or sentence type. semantic parse accuracy Correctness of the target semantic artifact. scope accuracy Correct placement of quantifier, negation, modality, and adverbial scope. attachment accuracy Correct modifier, prepositional phrase, and semantic-role attachment. paraphrase stability Meaning preservation under controlled paraphrase. Functorial Language Consistency Path agreement under transformation squares. repair usefulness Whether categorial diagnostics improve correction of failed outputs. annotation cost Human or expert effort per item and agreement rate.</caption>
<colgroup>
<col style="width: 27%"/>
<col style="width: 22%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Track</strong></th>
<th scope="col"><strong>Recommended size</strong></th>
<th scope="col"><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Supertag and structure track</td>
<td>150-200 sentences</td>
<td>Measure local and structured categorial prediction.</td>
</tr>
<tr class="even">
<td>Semantic parsing track</td>
<td>75-100 controlled examples</td>
<td>Measure transfer from categories to meaning.</td>
</tr>
<tr class="odd">
<td>Scope and attachment track</td>
<td>50-75 examples</td>
<td>Stress ambiguity resolution and semantic operations.</td>
</tr>
<tr class="even">
<td>Functorial Language Consistency track</td>
<td>75-125 transformation squares</td>
<td>Measure path agreement under controlled transformations.</td>
</tr>
<tr class="odd">
<td>Repair track</td>
<td>25-50 selected failures</td>
<td>Test whether categorial diagnostics improve correction.</td>
</tr>
</tbody>
</table></div>
<p>The split design should stress structural generalization. The dataset should include in-distribution items, long-tail categories, unseen category structures, paraphrase transformations, scope and attachment challenges, out-of-domain syntax, and commutation-square items. A benchmark restricted to common categories risks measuring memorized lexical patterns instead of typed compositional structure.</p>
<h2 id="success-and-failure-conditions">11. Success and failure conditions</h2>
<p>A strong result would show that explicit categorial structure improves downstream semantic behavior beyond strong baselines and simpler syntactic supervision. The result would remain scoped. It would establish that typed grammatical structure helps with a defined class of compositional failures, not that language models instantiate Lambek calculus internally.</p>
<p class="table-display-caption" id="table-10-caption">Table 10. Evidence pattern, Interpretation</p>
<div aria-labelledby="table-10-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="10" id="table-10"><caption class="visually-hidden">Table 10. Evidence pattern, Interpretation</caption>
<colgroup>
<col style="width: 53%"/>
<col style="width: 46%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Evidence pattern</strong></th>
<th scope="col"><strong>Interpretation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Categorial supervision improves semantic parsing, scope interpretation, attachment resolution, or semantic-role assignment.</td>
<td>Supports a downstream semantic-transfer claim.</td>
</tr>
<tr class="even">
<td>Structured category supervision outperforms flat supertag classification on rare, long-tail, or out-of-domain categories.</td>
<td>Supports the value of internal category structure.</td>
</tr>
<tr class="odd">
<td>Reduction supervision improves global well-typedness and semantic parse validity.</td>
<td>Supports derivation-level supervision beyond lexical labels.</td>
</tr>
<tr class="even">
<td>Categorial errors predict downstream semantic failures and support repair.</td>
<td>Supports diagnostic use of the structure layer.</td>
</tr>
<tr class="odd">
<td>Functorial Language Consistency improves under categorial supervision.</td>
<td>Supports transformation-sensitive value.</td>
</tr>
<tr class="even">
<td>Gains persist under paraphrase, syntactic reordering, and held-out transformation families.</td>
<td>Supports robustness of the downstream claim.</td>
</tr>
</tbody>
</table></div>
<p>A weak result would show improved supertag prediction without downstream semantic improvement. That result still has technical value, but it supports only the local analysis layer. A negative result would show that explicit categorial structure is separable from the semantic behaviors targeted here, or that simpler explicit syntax gives the same benefit at lower cost.</p>
<h2 id="strongest-objections">12. Strongest objections</h2>
<p class="table-display-caption" id="table-11-caption">Table 11. Objection, Response — Objection, Response</p>
<div aria-labelledby="table-11-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="11" id="table-11"><caption class="visually-hidden">Table 11. Objection, Response — Objection, Response</caption>
<colgroup>
<col style="width: 34%"/>
<col style="width: 65%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Objection</strong></th>
<th scope="col"><strong>Response</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Modern language models already encode syntax implicitly.</td>
<td>The proposal is compatible with implicit structure. The evaluation asks whether explicit categorial structure improves diagnosis, supervision, repair, or transformation consistency beyond strong baselines.</td>
</tr>
<tr class="even">
<td>Supertagging is not semantics.</td>
<td>The protocol treats supertagging as an entry point and downstream semantic preservation as the target.</td>
</tr>
<tr class="odd">
<td>Lambek grammars are too narrow.</td>
<td>The essay uses Lambek as the grammar-as-logic anchor and permits CCG, LCG, pregroups, DisCoCat, and related categorial systems as operational interfaces.</td>
</tr>
<tr class="even">
<td>DisCoCat has not scaled to frontier language models.</td>
<td>The essay uses DisCoCat as a structural bridge, not as a replacement model family.</td>
</tr>
<tr class="odd">
<td>Grammar constraints can reduce flexibility.</td>
<td>Level 3 should be tested only in target environments where constraints improve validity or interpretation. Open-domain generation can use diagnostics or auxiliary objectives.</td>
</tr>
<tr class="even">
<td>Dependency labels can perform equally well.</td>
<td>This is a decisive ablation. If ordinary syntax matches Lambek-specific structure, the claim should be narrowed.</td>
</tr>
<tr class="odd">
<td>The name Lambek Machine can overpromise.</td>
<td>The definition is operational and limited to exposed typed composition for analysis, supervision, constraint, interpretation, repair, or architecture design.</td>
</tr>
</tbody>
</table></div>
<h2 id="kill-criteria">13. Kill criteria</h2>
<p class="table-display-caption" id="table-12-caption">Table 12. Criterion, Decision rule</p>
<div aria-labelledby="table-12-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="12" id="table-12"><caption class="visually-hidden">Table 12. Criterion, Decision rule</caption>
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
<td>Categorial supervision improves supertag accuracy and downstream compositional metrics remain unchanged.</td>
</tr>
<tr class="even">
<td>K2</td>
<td>Dependency, constituency, or semantic-tagging baselines match categorial supervision across downstream tasks.</td>
</tr>
<tr class="odd">
<td>K3</td>
<td>Structured category prediction adds cost without outperforming flat labels on long-tail or out-of-domain categories.</td>
</tr>
<tr class="even">
<td>K4</td>
<td>Reduction supervision improves formal well-typedness and semantic artifacts remain unchanged.</td>
</tr>
<tr class="odd">
<td>K5</td>
<td>Functorial Language Consistency scores fail to distinguish systems beyond local semantic-parse accuracy.</td>
</tr>
<tr class="even">
<td>K6</td>
<td>Categorial diagnostics fail to help humans or systems repair errors.</td>
</tr>
<tr class="odd">
<td>K7</td>
<td>Annotation cost exceeds the diagnostic value produced.</td>
</tr>
</tbody>
</table></div>
<p>The decision rules should constrain the research program before expansion. If K1 or K2 holds repeatedly, Lambek Machines should retreat to a weaker claim about post-hoc categorial analysis. If K5 holds, the transformation families need redesign. If K7 holds, the protocol should be restricted to high-value transformations with reliable validators.</p>
<h2 id="relation-to-essay-5---algebraic-architectures">14. Relation to Essay 5 - Algebraic Architectures</h2>
<p>Essay 4 prepares the architecture-level question by isolating a case in which task structure is explicit. Lambek Machines asks whether one typed compositional structure improves linguistic behavior. Algebraic Architectures generalizes the design problem to model families whose commitments concern objects, transformations, symmetries, constraints, interfaces, and validators.</p>
<p>The bridge from language to architecture is specification satisfaction. If typed compositional structure improves semantic behavior, architecture design should account for the structures that the task requires a model to represent and preserve. The relevant questions are then architectural rather than merely linguistic. Which objects require representation, which transformations require preservation, which validators should be exposed, and which failure modes follow from insufficient or excessive inductive bias?</p>
<p>Essay 4 therefore functions as the controlled linguistic case before the architecture-general case. It provides a concrete setting in which formal structure can be tested as supervision, evaluation, constraint, diagnostic signal, or architecture bias.</p>
<h2 id="conclusion">15. Conclusion</h2>
<p>Lambek Machines supplies the language test for Compositional Intelligence. The gap under analysis is specific. Language models can generate fluent sentences, parses, explanations, and responses even when they fail to preserve typed composition across scope, attachment, role binding, embedded dependency, negation, coordination, or controlled semantic transformation.</p>
<p>Grammar-as-logic gives the gap a measurable structure. Lexical items receive types, type reductions yield derivations, and derivations induce semantic composition maps. These objects can be predicted, supervised, constrained, inspected, and used for repair. The scientific question is whether exposing them changes downstream semantic behavior under strong baselines and transformation-sensitive evaluation.</p>
<p>The proposal earns its place only through measurement. Supertagging alone is an intermediate result. The central test is downstream semantic behavior, especially Functorial Language Consistency. If explicit categorial structure improves semantic parsing, scope control, attachment resolution, dependency tracking, paraphrase stability, and repair, Lambek Machines defines a viable language-core research path. If it fails those tests, the concept should be narrowed to diagnostic analysis or rejected for the tested regime.</p>
<p>Algebraic Architectures extends this inquiry beyond language. The next essay treats model families as structural commitments about objects, transformations, symmetries, constraints, interfaces, and validators. The Lambek case supplies the first worked instance of that broader specification problem.</p>
<h2 id="appendix-a.-lambek-machine-record">Appendix A. Lambek Machine record</h2>
<p>lambek_machine_record:</p>
<p>system_id: string</p>
<p>level:</p>
<p>enum[</p>
<p>post_hoc_categorial_analysis,</p>
<p>auxiliary_categorial_supervision,</p>
<p>grammar_guided_decoding,</p>
<p>architecture_level_typed_compositional_bias</p>
<p>]</p>
<p>grammar_formalism: CCG | LCG | pregroup | ACG | other</p>
<p>exposed_structures:</p>
<p>- lexical_categories</p>
<p>- structured_categories</p>
<p>- reductions_or_derivations</p>
<p>- semantic_composition_maps</p>
<p>- diagnostics</p>
<p>validators:</p>
<p>- category_accuracy</p>
<p>- reduction_validity</p>
<p>- semantic_equivalence</p>
<p>- functorial_language_consistency</p>
<p>supported_transformations: list[string]</p>
<p>failure_labels: list[string]</p>
<p>evidence_level: L0 | L1 | L2 | L3 | L4</p>
<h2 id="appendix-b.-functorial-language-consistency-item">Appendix B. Functorial Language Consistency item</h2>
<p>functorial_language_consistency_item:</p>
<p>id: string</p>
<p>source_sentence: string</p>
<p>source_transformation:</p>
<p>family: string</p>
<p>transformed_sentence: string</p>
<p>intended_change: preserve_meaning | change_scope | change_attachment | change_role | change_modality | other</p>
<p>translation_task: semantic_parse | logical_form | semantic_roles | explanation | query | other</p>
<p>target_artifact: object</p>
<p>target_transformation: object</p>
<p>expected_target_artifact: object</p>
<p>equivalence_regime: logical | denotational | graph_isomorphism | query_result | role_equivalence | reviewed_alignment</p>
<p>validator: string</p>
<p>failure_taxonomy: list[string]</p>
<p>repair_guidance: string</p>
<h2 id="appendix-c.-source-map-and-verification-queue">Appendix C. Source map and verification queue</h2>
<p class="table-display-caption" id="table-13-caption">Table 13. Source anchor, Use in Essay 4</p>
<div aria-labelledby="table-13-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="13" id="table-13"><caption class="visually-hidden">Table 13. Source anchor, Use in Essay 4</caption>
<colgroup>
<col style="width: 36%"/>
<col style="width: 63%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Source anchor</strong></th>
<th scope="col"><strong>Use in Essay 4</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Lambek 1958</td>
<td>Background for grammar-as-logic and syntactic types.</td>
</tr>
<tr class="even">
<td>Bangalore and Joshi 1999</td>
<td>Background for supertagging as almost parsing.</td>
</tr>
<tr class="odd">
<td>Hockenmaier and Steedman or CCGbank</td>
<td>Dataset and parsing infrastructure context for CCG.</td>
</tr>
<tr class="even">
<td>Coecke, Sadrzadeh, and Clark 2010</td>
<td>Bridge between grammatical reductions and distributional semantics.</td>
</tr>
<tr class="odd">
<td>de Groote 2001</td>
<td>Abstract categorial grammar and syntax-semantics interface context.</td>
</tr>
<tr class="even">
<td>COGS 2020 and SLOG 2023</td>
<td>Compositional semantic parsing and structural-generalization context.</td>
</tr>
<tr class="odd">
<td>Zhao and Penn 2024</td>
<td>LLM-based CCG or LCG supertagging context.</td>
</tr>
<tr class="even">
<td>Grammar-constrained decoding sources</td>
<td>Decoding-constraint context, not evidence for Lambek-specific internal structure.</td>
</tr>
</tbody>
</table></div>
<p>Before public release, verify final metadata for all recent sources, especially 2023-2026 papers, ACL Anthology page numbers, arXiv versions, venue status, and benchmark claims. Source claims should remain source-functional. Background sources motivate the interface, and the Lambek Auxiliary Supervision protocol remains an original proposal until implemented and evaluated.</p>
<h2 id="appendix-d.-editorial-changes-from-v0.2-to-v0.3">Appendix D. Editorial changes from v0.2 to v0.3</h2>
<p class="table-display-caption" id="table-14-caption">Table 14. Area, Revision — Area, Revision</p>
<div aria-labelledby="table-14-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="14" id="table-14"><caption class="visually-hidden">Table 14. Area, Revision — Area, Revision</caption>
<colgroup>
<col style="width: 27%"/>
<col style="width: 72%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Area</strong></th>
<th scope="col"><strong>Revision</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mission alignment</td>
<td>The revision treats Functorial Language Consistency as the evaluation spine of the language layer.</td>
</tr>
<tr class="even">
<td>Definition</td>
<td>The Lambek Machine definition remains operational and bounded to avoid claims about hidden model mechanisms.</td>
</tr>
<tr class="odd">
<td>Evaluation</td>
<td>The auxiliary-supervision protocol is framed around downstream transfer and strong baseline comparison.</td>
</tr>
<tr class="even">
<td>Examples</td>
<td>Diagnostic cases now emphasize one failure mechanism per case and connect each case to an equivalence regime.</td>
</tr>
<tr class="odd">
<td>Schemas</td>
<td>Benchmark and output records remain implementation-ready for a first pilot.</td>
</tr>
<tr class="even">
<td>Failure policy</td>
<td>Kill criteria are stated as decision rules for narrowing or rejecting the claim.</td>
</tr>
<tr class="odd">
<td>Source policy</td>
<td>The source map separates background formalisms from original Compositional Intelligence proposals.</td>
</tr>
</tbody>
</table></div>
