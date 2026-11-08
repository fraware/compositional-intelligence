# Series Preface

*Mateo Petel*

<!-- AUTHORITATIVE-DOCX SHA256 1ce80674057c8c2951652bbb0e1f39bb20be1b18c03080bbe2eb1ca33f02e8c5; source Essay0_Compositional_Intelligence_Preface_V3(1).docx -->

<h2 id="abstract">Abstract</h2>
<p>Compositional Intelligence is a proposed research program for evaluating generative AI through typed artifacts and the structured worlds those artifacts enter. The program retains prediction, scale, and benchmark performance as important evidence sources, then adds the object-level questions that those measures leave underspecified. It asks how models infer target types, construct candidate inhabitants, preserve structure across transformations, and integrate generated objects into environments where they can be checked, composed, reused, extended, warranted, or acted on under controlled effects.</p>
<p>This preface orients the suite. The main synthesis paper gives the compact framework. Essay 1 defines Semantic Participation as the membership criterion for generated artifacts. Essay 2 defines Typed Generativity as target-type inference and candidate-inhabitant construction. Essay 3 defines Functorial Consistency as the central evaluation principle. Essays 4 and 5 extend the program into language and architecture. Essays 6 and 7 complete the warrant and action layers.</p>
<p>The intended audience is expert. Mathematicians should see how the program separates proof, alignment, warrant, and semantic use. Scientists should see how protocols, models, measurements, claims, and permitted uses can be represented as artifacts with explicit status. AI researchers should see a benchmark agenda for structure-preserving generation. Formal-methods researchers should see a bridge from validation mechanisms to artifact membership, transformation stability, and effect control.</p>
<h2 id="purpose-of-the-series">1. Purpose of the Series</h2>
<p>Generative AI now produces objects that resemble reasoning, explanation, proof, code, protocol design, planning, and tool use. Cumulative knowledge requires a stronger account of status. A generated object must enter an environment with definitions, dependencies, validators, transformation rules, review practices, evidence standards, permitted uses, and effect constraints.</p>
<p>The series starts from the distinction between output and artifact. Fluent output supplies surface evidence. Artifact status requires checkability, source alignment, composability, repairability, reusability, warrant, and governed use. The distinction applies across mathematics, software, scientific work, language, architecture, and agentic systems.</p>
<p>The lifecycle used throughout the suite is diagnostic. Output -&gt; candidate artifact -&gt; typed candidate -&gt; transformed artifact -&gt; validated artifact -&gt; warranted artifact -&gt; reusable artifact -&gt; effectful action. The sequence exposes the status transitions that generated objects must pass through before they support cumulative reasoning or controlled intervention.</p>
<p>Each essay should therefore be read as part of one program whose object is the construction, transformation, validation, warranting, reuse, and execution of typed artifacts inside structured worlds.</p>
<h2 id="thesis-of-the-series">2. Thesis of the Series</h2>
<p>Compositional Intelligence proposes that generative AI should be evaluated through typed artifacts and the structured worlds those artifacts enter. A generated object matters when it can be expressed, validated, aligned, transformed, composed, warranted, reused, or acted on inside a semantic environment.</p>
<p>The thesis is broader than a single benchmark or formalism. It draws from type theory, Curry-Howard, Lambek grammar, categorical structure, formal verification, semantic parsing, geometric deep learning, probabilistic warrant, and effect systems. The unifying problem is composition under status. An AI-generated object has serious epistemic or operational value when it preserves relevant structure and receives a usable status inside an environment equipped to evaluate it.</p>
<p>The series therefore studies the object layer encoded by token sequences. The relevant objects include proofs, programs, theorem statements, semantic parses, protocols, plans, explanations, datasets, database queries, tool calls, memory writes, and skills. Evaluation must identify the object attempted, the environment targeted, the relation preserved, the warrant supplied, and the consequences authorized.</p>
<h2 id="deliverable-architecture">3. Deliverable Architecture</h2>
<p class="table-display-caption" id="table-1-caption">Table 1. Order, Document, Role</p>
<div aria-labelledby="table-1-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="1" id="table-1"><caption class="visually-hidden">Table 1. Order, Document, Role</caption>
<colgroup>
<col style="width: 7%"/>
<col style="width: 34%"/>
<col style="width: 58%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Order</strong></th>
<th scope="col"><strong>Document</strong></th>
<th scope="col"><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01</td>
<td>Main synthesis paper</td>
<td>Primary publishable statement of the research program.</td>
</tr>
<tr class="even">
<td>02</td>
<td>Essay 0 - Series Preface</td>
<td>Reader orientation, thesis, vocabulary, and reading plan.</td>
</tr>
<tr class="odd">
<td>03</td>
<td>Essay 1 - Semantic Participation</td>
<td>Membership criterion for AI-generated artifacts.</td>
</tr>
<tr class="even">
<td>04</td>
<td>Essay 2 - Typed Generativity</td>
<td>Generation as target-type inference and candidate-inhabitant construction.</td>
</tr>
<tr class="odd">
<td>05</td>
<td>Essay 3 - Functorial Consistency</td>
<td>Central evaluation principle through commutation-square tests.</td>
</tr>
<tr class="even">
<td>06</td>
<td>Essay 4 - Lambek Machines</td>
<td>Language-specific extension through typed compositional structure.</td>
</tr>
<tr class="odd">
<td>07</td>
<td>Essay 5 - Algebraic Architectures</td>
<td>Architecture-specific extension through structure, symmetry, and constraint.</td>
</tr>
<tr class="even">
<td>08</td>
<td>Essay 6 - Quantitative Curry-Howard</td>
<td>Warrant and evidence layer for candidate typed artifacts.</td>
</tr>
<tr class="odd">
<td>09</td>
<td>Essay 7 - Effectful and Conceptual Intelligence</td>
<td>Action, effect, memory, tools, plans, skills, and series closure.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Book document</td>
<td>Later reference volume assembled after individual drafts have stabilized.</td>
</tr>
</tbody>
</table></div>
<p>The main paper has priority as the public entry point for circulation, review, and citation. The essays should remain individually publishable and should also supply the technical development behind the compressed synthesis.</p>
<h2 id="foundational-sequence">4. Foundational Sequence</h2>
<p class="table-display-caption" id="table-2-caption">Table 2. Layer, Question, Canonical schema</p>
<div aria-labelledby="table-2-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="2" id="table-2"><caption class="visually-hidden">Table 2. Layer, Question, Canonical schema</caption>
<colgroup>
<col style="width: 25%"/>
<col style="width: 52%"/>
<col style="width: 22%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Layer</strong></th>
<th scope="col"><strong>Question</strong></th>
<th scope="col"><strong>Canonical schema</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Semantic Participation</td>
<td>When does a generated output qualify as a member of a structured world?</td>
<td>Member_E(a)</td>
</tr>
<tr class="even">
<td>Typed Generativity</td>
<td>How does a model infer the target object and construct a candidate inhabitant?</td>
<td>P_theta(t : A | Gamma)</td>
</tr>
<tr class="odd">
<td>Functorial Consistency</td>
<td>Does a generated artifact preserve structure across transformations and representations?</td>
<td>T(f(x)) ~= g(T(x))</td>
</tr>
</tbody>
</table></div>
<p>These three essays form the foundation. The membership layer defines the destination. The generation layer defines the construction problem. The transformation layer supplies the central evaluation object. Later essays extend the framework into language, architecture, warrant, and action.</p>
<h2 id="vocabulary-for-expert-readers">5. Vocabulary for Expert Readers</h2>
<p class="table-display-caption" id="table-3-caption">Table 3. Term, Definition in the series</p>
<div aria-labelledby="table-3-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="3" id="table-3"><caption class="visually-hidden">Table 3. Term, Definition in the series</caption>
<colgroup>
<col style="width: 22%"/>
<col style="width: 77%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Term</strong></th>
<th scope="col"><strong>Definition in the series</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Typed artifact</td>
<td>An attempted object under constraints, such as a proof, program, protocol, plan, semantic parse, explanation, theorem statement, database query, memory write, tool call, or skill.</td>
</tr>
<tr class="even">
<td>Structured world</td>
<td>An environment with objects, dependencies, validators, transformations, review practices, epistemic statuses, and permitted uses.</td>
</tr>
<tr class="odd">
<td>Semantic participation</td>
<td>The status of an artifact that can be expressed, validated or reviewed, aligned, composed, warranted, reused, or acted on inside a semantic environment.</td>
</tr>
<tr class="even">
<td>Target type</td>
<td>The inferred object class requested by a context, such as a proof, program, explanation, plan, protocol, or action schema.</td>
</tr>
<tr class="odd">
<td>Candidate inhabitant</td>
<td>The generated object that attempts to inhabit the inferred target type.</td>
</tr>
<tr class="even">
<td>Equivalence regime</td>
<td>The domain-specific criterion used to compare two paths in a Functorial Consistency square.</td>
</tr>
<tr class="odd">
<td>Epistemic type</td>
<td>The warrant label attached to an artifact, such as proved, formally validated, empirically supported, simulation derived, reviewed, conjectural, or unvalidated.</td>
</tr>
<tr class="even">
<td>Effect record</td>
<td>A record of preconditions, postconditions, authority, side effects, handlers, validators, and audit traces for action-taking systems.</td>
</tr>
</tbody>
</table></div>
<h2 id="claim-protocol">6. Claim Protocol</h2>
<p>The series separates established background, source-supported claims, interpretive synthesis, original proposals, and testable hypotheses. This protocol prevents overclaiming and gives expert readers a clear account of source use and evidentiary strength.</p>
<p class="table-display-caption" id="table-4-caption">Table 4. Level, Meaning, Treatment</p>
<div aria-labelledby="table-4-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="4" id="table-4"><caption class="visually-hidden">Table 4. Level, Meaning, Treatment</caption>
<colgroup>
<col style="width: 8%"/>
<col style="width: 38%"/>
<col style="width: 52%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Level</strong></th>
<th scope="col"><strong>Meaning</strong></th>
<th scope="col"><strong>Treatment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>L0</td>
<td>Formal or established background</td>
<td>Cite where the claim is nontrivial.</td>
</tr>
<tr class="even">
<td>L1</td>
<td>Source-supported empirical or system claim</td>
<td>Cite the specific source supporting the claim.</td>
</tr>
<tr class="odd">
<td>L2</td>
<td>Interpretive synthesis</td>
<td>Anchor in multiple literatures and state the interpretive step.</td>
</tr>
<tr class="even">
<td>L3</td>
<td>Original proposal</td>
<td>Mark as proposed by the Compositional Intelligence program.</td>
</tr>
<tr class="odd">
<td>L4</td>
<td>Testable hypothesis</td>
<td>State the test, metric, and failure condition.</td>
</tr>
</tbody>
</table></div>
<p>The artifacts introduced by the suite, including ArtifactRecord, TargetTypeRecord, FunctorialConsistencyItem, ArchitectureSpec, quantitative_judgment, TypedActionLedgerEntry, and ConceptTransferRecord, are proposed designs awaiting implementation or evaluation evidence unless later experiments supply direct support.</p>
<h2 id="reading-the-mathematical-notation">7. Reading the Mathematical Notation</h2>
<p>The notation is a design language for records, transformations, judgments, and evaluations. It should guide annotation, diagnosis, and implementation. It does not replace the validation regime of the target domain.</p>
<p class="table-display-caption" id="table-5-caption">Table 5. Notation, Reading — Notation, Reading</p>
<div aria-labelledby="table-5-caption" class="table-scroll" data-columns="2" role="group" tabindex="0"><table data-source-table="5" id="table-5"><caption class="visually-hidden">Table 5. Notation, Reading — Notation, Reading</caption>
<colgroup>
<col style="width: 32%"/>
<col style="width: 67%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Notation</strong></th>
<th scope="col"><strong>Reading</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Member_E(a)</td>
<td>Artifact a participates in environment E under explicit membership conditions.</td>
</tr>
<tr class="even">
<td>P_theta(t : A | Gamma)</td>
<td>Model theta constructs candidate inhabitant t of inferred target A under context Gamma.</td>
</tr>
<tr class="odd">
<td>T(f(x)) ~= g(T(x))</td>
<td>Transforming and then translating should agree with translating and then transforming under an explicit equivalence regime.</td>
</tr>
<tr class="even">
<td>A |= S</td>
<td>Architecture A satisfies, supports, or violates task specification S under a stated evidence regime.</td>
</tr>
<tr class="odd">
<td>Gamma |-theta t : A |&gt; Q</td>
<td>Candidate artifact t has target A under context Gamma with quantitative evidence record Q.</td>
</tr>
<tr class="even">
<td>Gamma; M; E; C |- a : Pre -&gt; Post ! epsilon @ rho</td>
<td>Agent action a transforms state under preconditions, postconditions, effects, authority, and risk records.</td>
</tr>
</tbody>
</table></div>
<h2 id="field-building-value">8. Field-Building Value</h2>
<p>The series supplies a research grammar for a recurring problem across AI, mathematics, formal methods, language, scientific computing, and agentic systems. Local success gives too little information about structure, warrant, reuse, and action. Compositional Intelligence proposes records and evaluation units that expose those missing dimensions.</p>
<p>The field-building value depends on concrete utility. The proposed schemas matter only if they improve diagnosis, validation, repair, reuse, architecture choice, calibration, effect control, or audit. Every essay should include failure modes and kill criteria. The program invites empirical refinement through tests that can remove or revise any component that lacks diagnostic value.</p>
<h2 id="publication-sequence">9. Publication Sequence</h2>
<p class="table-display-caption" id="table-6-caption">Table 6. Step, Action, Gate — Step, Action, Gate</p>
<div aria-labelledby="table-6-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="6" id="table-6"><caption class="visually-hidden">Table 6. Step, Action, Gate — Step, Action, Gate</caption>
<colgroup>
<col style="width: 7%"/>
<col style="width: 45%"/>
<col style="width: 47%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Step</strong></th>
<th scope="col"><strong>Action</strong></th>
<th scope="col"><strong>Gate</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Publish or circulate the main synthesis paper.</td>
<td>PDF compiled, citations resolved, source-use audit completed.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Publish Essay 0 as the orientation piece.</td>
<td>No repetition of the full paper; reading map and vocabulary clear.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Publish Essays 1-3 as the foundation trilogy.</td>
<td>Membership, generation, and transformation terminology aligned.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Publish Essays 4-7 as extensions.</td>
<td>Each extension inherits claim levels, schemas, validators, and kill criteria.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Assemble the book document.</td>
<td>All essays stabilized; consolidated glossary, schemas, and bibliography prepared.</td>
</tr>
</tbody>
</table></div>
<h2 id="closing-preface">10. Closing Preface</h2>
<p>Compositional Intelligence is offered as a research program for the next stage of generative AI evaluation. Its premise is simple and demanding. Generated objects should be judged by the worlds they can enter, the structures they preserve, the warrant that supports them, the uses they permit, and the consequences they can produce under controlled authority.</p>
<p>The essays should be read as a sequence of increasingly operational tests. The series starts with artifact membership, proceeds through generation and transformation, extends into language and architecture, adds warrant, and concludes with action. That sequence is the project mission. It should remain intact across publication, citation, revision, and later book assembly.</p>
<h2 id="appendix-a.-canonical-schemas">Appendix A. Canonical Schemas</h2>
<p class="table-display-caption" id="table-7-caption">Table 7. Layer, Schema, Artifact</p>
<div aria-labelledby="table-7-caption" class="table-scroll" data-columns="3" role="group" tabindex="0"><table data-source-table="7" id="table-7"><caption class="visually-hidden">Table 7. Layer, Schema, Artifact</caption>
<colgroup>
<col style="width: 20%"/>
<col style="width: 45%"/>
<col style="width: 33%"/>
</colgroup>
<thead>
<tr class="header">
<th scope="col"><strong>Layer</strong></th>
<th scope="col"><strong>Schema</strong></th>
<th scope="col"><strong>Artifact</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Membership</td>
<td>Member_E(a)</td>
<td>ArtifactRecord and semantic transport record</td>
</tr>
<tr class="even">
<td>Generation</td>
<td>P_theta(t : A | Gamma)</td>
<td>TargetTypeRecord and candidate_inhabitant_record</td>
</tr>
<tr class="odd">
<td>Transformation</td>
<td>T(f(x)) ~= g(T(x))</td>
<td>FunctorialConsistencyItem</td>
</tr>
<tr class="even">
<td>Language</td>
<td>w_i -&gt; tau_i -&gt; pi -&gt; [[pi]]</td>
<td>Lambek Auxiliary Supervision item</td>
</tr>
<tr class="odd">
<td>Architecture</td>
<td>TaskSpec -&gt; ArchitectureType -&gt; ArchitectureInstance; A |= S</td>
<td>ArchitectureSpec</td>
</tr>
<tr class="even">
<td>Warrant</td>
<td>Gamma |-theta t : A |&gt; Q</td>
<td>quantitative_judgment</td>
</tr>
<tr class="odd">
<td>Action</td>
<td>Gamma; M; E; C |- a : Pre -&gt; Post ! epsilon @ rho</td>
<td>TypedActionLedgerEntry</td>
</tr>
</tbody>
</table></div>
