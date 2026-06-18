# Paper Reading Skills

This context defines the vocabulary for paper-reading skills that turn a reading motivation into a concrete research workflow and durable artifacts.

## Language

**Field Map Workflow**:
A complete domain-mapping workflow for entering a research direction, starting from scope boundaries and ending with paper clusters, gap analysis, and a human-readable report.
_Avoid_: Field map as a single markdown file, quick paper list

**Field Boundary**:
The explicit inclusion and exclusion criteria that define which research questions, papers, methods, systems, and benchmarks belong inside the user's current research scope.
_Avoid_: Topic, area, background

**Field Boundary Gate**:
The required clarification step before collecting papers; it is passed only when the research target, in-scope areas, out-of-scope areas, time or venue limits, user goal, and stop condition are explicit.
_Avoid_: Optional preface, rough topic note

**Proposed Field Boundary**:
An AI-drafted Field Boundary offered to the user for critique and revision before the Field Boundary Gate is passed.
_Avoid_: User questionnaire, final scope

**Field Map Workspace**:
A durable artifact set for exactly one research direction explored through a Field Map Workflow.
_Avoid_: Output folder, notes dump

**Seed Paper**:
A representative starting paper selected to anchor the field map, usually from surveys, classic works, high-citation recent papers, benchmark papers, or related systems.
_Avoid_: Random paper, first batch paper

**Seed Set**:
An initial set of roughly 8-12 Seed Papers chosen for coverage across overview, foundational, recent high-impact, benchmark, dataset, evaluation, system, or application perspectives.
_Avoid_: Top ten papers, arbitrary reading list

**Paper Position Record**:
A structured note for one paper that captures the paper's position in the field, including its problem, assumptions, method route, evaluation, contribution type, related works, contrasting works, and gaps left.
_Avoid_: Paper summary, reading notes

**Position-Oriented Reading**:
A paper-reading mode that reads only deeply enough to place a paper in the Field Map Workflow and complete its Paper Position Record.
_Avoid_: Full close reading, exhaustive summary

**Candidate Pool**:
A broad, auditable collection of papers discovered from citations, references, keyword expansion, benchmarks, leaderboards, and related-work trails before selecting which papers to read closely.
_Avoid_: Final paper set, reading list

**Selected Expansion Set**:
The roughly 25-35 non-seed papers chosen from the Candidate Pool for Paper Position Records.
_Avoid_: All discovered papers, search results

**User-Provided Paper**:
A paper directly uploaded or linked by the user, which takes priority over network-discovered papers during Field Map Workflow discovery.
_Avoid_: Local corpus, existing library

**Network Discovery**:
The default paper discovery mode when the user has not provided papers, using web search, citation trails, survey bibliographies, benchmark pages, and other online sources.
_Avoid_: Repository search, offline literature lookup

**Research Cluster**:
A group of papers that share a core problem, method route, assumptions, or evaluation setting within the field map.
_Avoid_: Category, bucket, theme

**Primary Research Cluster**:
The one Research Cluster that best explains a paper's main field position.
_Avoid_: Main category

**Secondary Research Cluster**:
An additional Research Cluster that a paper meaningfully informs without being its main field position.
_Avoid_: Tag, loose theme

**Research Opportunity**:
A possible future research direction derived from gaps across the mapped papers, such as conceptual, method, evaluation, system, or theoretical gaps.
_Avoid_: Idea, future work note

**Research Opportunity Candidate**:
A Research Opportunity backed by paper evidence and phrased so it can become a possible research question, with risks and objections recorded.
_Avoid_: Speculation, loose future work

**Research Question Workflow**:
A downstream paper-reading workflow that turns Research Opportunity Candidates from exactly one Field Map Workspace into evidence-backed Candidate Angles and Research Question Cards.
_Avoid_: Brainstorming, topic generation, generic idea search

**Research Question Card**:
A decision-ready research question artifact derived from one or more Research Opportunity Candidates, recording the question, supporting evidence, fit to the user's writing intent, feasibility, novelty, risks, and whether further paper discovery is needed.
_Avoid_: Idea card, question list item, topic note

**Problem Reality Check**:
A paper-reading workflow routed to exactly one Research Question Card before interrogation begins, stress-testing whether that card's problem is real, externally grounded, and strong enough to motivate research.
_Avoid_: General risk review, method critique, reviewer objection list

**Problem Reality Check Report**:
A durable review artifact attached to one Research Question Card, recording the problem-reality verdict, strongest supporting evidence, weak assumptions, caution points, unsafe motivation claims, and follow-up evidence needs.
_Avoid_: Risk list, paper summary, informal comments

**Problem Reality Verdict**:
The controlled final status of a Problem Reality Check Report: `problem-solid`, `needs-evidence`, `motivation-fragile`, or `reject`.
_Avoid_: Free-form confidence note, numeric score, keep/defer decision

**Unsafe Motivation Claim**:
A motivation statement that a Problem Reality Check Report warns against because it is overstated, undersupported, contradicted by evidence, too broad, or likely to be attacked during paper review.
_Avoid_: Limitation, reviewer objection, writing polish note

**Targeted Evidence Need**:
A focused evidence gap identified by a Problem Reality Check Report, phrased as a recommended next investigation without automatically launching a new paper-search workflow.
_Avoid_: Full literature review, automatic evidence collection, vague next step

**Theoretical Grounding Workflow**:
A downstream paper-reading workflow routed to exactly one Research Question Card and its completed Problem Reality Check Report, extracting Theory-Support Claims and Theory Hooks from the checked problem and turning them into a small set of theoretical traditions and a theory-backed problem framing.
_Avoid_: Theory search, literature background, theoretical justification

**Theoretical Grounding Source Gate**:
The required routing step before a Theoretical Grounding Workflow begins; it is passed only when exactly one source Research Question Card and its completed Problem Reality Check Report are identified, including the Problem Reality Verdict and any motivation fragilities or evidence needs.
_Avoid_: Optional context loading, broad theory scan

**Theory-Support Claim**:
A key judgment in the paper or project that needs theoretical support, recorded as the exact sentence to support and the reason it needs theory rather than decorative citation.
_Avoid_: Core claim, citation topic, related theory

**Problem-Theory Decomposition**:
A durable artifact in a Theoretical Grounding Workflow that decomposes the checked problem into phenomenon, mechanism, failure, Theory-Support Claims, and boundary before candidate theoretical traditions are selected.
_Avoid_: Internal reasoning, outline, theory notes

**Theory Hook**:
A concept relationship extracted from a Problem-Theory Decomposition that could be explained or supported by a theoretical tradition, such as how a source affects trustworthiness or how long-term state influences later action.
_Avoid_: Keyword, theory name, citation label

**Candidate Theoretical Tradition**:
A possible theory, conceptual lineage, or research tradition considered because it can explain one or more Theory Hooks or support one or more Theory-Support Claims.
_Avoid_: Famous theory, citation candidate, background area

**Selected Theoretical Tradition**:
A Candidate Theoretical Tradition kept for the final grounding because it directly supports a Theory-Support Claim, explains a Theory Hook, has clear boundaries, and can shape the problem framing.
_Avoid_: Best-known theory, related work cluster, decorative citation

**Targeted Theory Search**:
A narrow paper-search step inside a Theoretical Grounding Workflow that the agent should run by default to verify Candidate Theoretical Traditions and representative sources for specific Theory Hooks or Theory-Support Claims without mapping the whole field.
_Avoid_: Field map, broad literature review, theory brainstorming

**Provisional Theoretical Grounding**:
A theory-backed framing draft whose Candidate Theoretical Traditions have not yet been fully verified with representative sources after Targeted Theory Search is unavailable, explicitly deferred, or insufficient.
_Avoid_: Final theoretical grounding, unsupported theory list

**Theory Evidence Need**:
A remaining source gap recorded only after Targeted Theory Search is unavailable or insufficient, naming the affected Theory-Support Claim, the missing source type, and the search question needed to stabilize the theoretical framing.
_Avoid_: User homework, vague citation gap, general bibliography need

**Theoretical Grounding Workspace**:
A durable artifact set for grounding checked Research Question Cards from exactly one Research Question Workspace, organized around source-problem routing, per-card grounding folders, Theory Hooks, selected theoretical traditions, and final theory-backed framing.
_Avoid_: Problem Reality Check folder, theory notes folder, background reading dump

**Theoretical Pillar**:
A claim-centered theoretical support structure in a Theoretical Grounding Report, linking one Theory-Support Claim to the Selected Theoretical Traditions that support it, the boundaries of that support, and the framing change it enables.
_Avoid_: Theory list, background section, named citation cluster

**Theoretical Grounding Report**:
The final artifact of a Theoretical Grounding Workflow, containing a theory-backed problem framing, Theoretical Pillars organized by Theory-Support Claim, framing changes from the original Research Question Card, and remaining fragilities or evidence needs.
_Avoid_: Theory summary, related work section, citation list

**Theoretical Tradition Selection Gate**:
The required confirmation step before writing a Theoretical Grounding Report; it is passed only when the user confirms, revises, or explicitly delegates the 2-4 Selected Theoretical Traditions and their rationale.
_Avoid_: Automatic theory choice, hidden selection, final theory list

**Method Inspiration Source Gate**:
The required routing step before a Method Inspiration Workflow begins; it is passed only when exactly one Research Question Card or one Source Problem Brief is identified, with the evidence status and reason for method search recorded.
_Avoid_: Source Problem Gate, loose problem note, implicit method-starting context

**Source Problem Brief**:
A user-provided problem record that can provisionally start Method Inspiration when no Research Question Card is available, naming the target problem, failure scenario, intended intervention point, constraints, non-goals, and evidence status.
_Avoid_: Rough idea, topic note, method prompt

**Method Inspiration Workflow**:
A downstream paper-reading workflow that turns one Research Question Card or Source Problem Brief into a Method Candidate Library through method-need decomposition, targeted method search, pattern extraction, transfer mapping, and candidate-method assembly.
_Avoid_: Method brainstorm, architecture design, related-work scan

**Method Inspiration Boundary**:
The boundary that Method Inspiration stops at auditable Candidate Methods and must not ask the user to immediately commit to a paper's actual core method; the human researcher owns the later jump from inspiration to a Committed Method Design.
_Avoid_: Agent-generated final method, automatic novelty creation, complete method design, quick commitment prompt

**Method Commitment Workflow**:
A reserved downstream workflow for turning method inspiration and the researcher's own judgment into a human-owned Committed Method Design; it is intentionally separate from Method Inspiration and is not yet specified.
_Avoid_: Method Inspiration final step, quick synthesis prompt, agent-owned method invention

**Method Inspiration Workspace**:
A durable artifact set for method inspiration from exactly one field context, organized around source-problem routing, per-problem inspiration folders, Method Needs, Method Patterns, Transfer Mappings, Candidate Methods, and Method Candidate Libraries.
_Avoid_: Method notes folder, architecture folder, paper dump

**Method Need**:
A problem-derived functional requirement for a method, naming the target failure, intervention point, required capability, expected inputs and outputs, constraints, success signal, and evidence status.
_Avoid_: Model module, feature idea, implementation component

**Method Need Decomposition**:
A durable artifact in a Method Inspiration Workflow that turns the source Research Question Card or Source Problem Brief into Method Needs before method papers are searched.
_Avoid_: Architecture plan, module list, generic requirements document

**Method Needs Confirmation Gate**:
The required confirmation step after Method Need Decomposition; it is passed only when the user confirms, revises, or explicitly delegates the Method Needs before Targeted Method Search proceeds.
_Avoid_: Hidden requirement inference, automatic method search, informal needs check

**Targeted Method Search**:
A narrow paper-search step inside a Method Inspiration Workflow that looks for method ideas for specific Method Needs across Same-Problem Papers, Adjacent-Problem Papers, and Far-Analogy Papers.
_Avoid_: Method Paper Search, broad related work search, baseline search

**Method Search Sufficiency Check**:
A coverage-based check in a Method Inspiration Workflow that decides whether each core Method Need has enough Same-Problem, Adjacent-Problem, and Far-Analogy evidence to extract Method Patterns and move toward assembly, or should remain marked as `needs-search`.
_Avoid_: Fixed paper-count target, exhaustive search, arbitrary stopping point

**Same-Problem Paper**:
A method-search candidate that directly addresses the same or highly similar problem as the source Research Question Card or Source Problem Brief.
_Avoid_: Baseline by default, any paper from the same field

**Adjacent-Problem Paper**:
A method-search candidate whose problem differs from the source problem but whose mechanism, failure mode, or required capability matches one or more Method Needs.
_Avoid_: Same-topic paper, loosely related paper

**Far-Analogy Paper**:
A method-search candidate from a more distant field whose method structure can transfer to one or more Method Needs despite substantial domain or task differences.
_Avoid_: Inspirational citation, random analogy, metaphor

**Method Pattern**:
A reusable method design pattern extracted from a paper, tied to a source URL, source paper type, matched Method Need, original setting, core mechanism, Transferable Unit, assumptions, inputs and outputs, integration cost, transfer risk, and evidence strength.
_Avoid_: Paper summary, full method copy, implementation recipe

**Transferable Unit**:
The smallest reusable design element inside a Method Pattern, such as a module, objective, training flow, inference flow, data construction step, filter, router, memory update, critic, or controller.
_Avoid_: Whole architecture, inspiration, vague lesson

**Transfer Mapping**:
A durable artifact in a Method Inspiration Workflow that decides how Method Patterns transfer into the source problem by recording Need-Pattern Fit before assigning any Assembly Role.
_Avoid_: Direct architecture design, analogy note, method mashup

**Need-Pattern Fit**:
The fit judgment between one Method Pattern and one Method Need, naming the matched capability, mismatch, required adaptation, transfer boundary, and whether the pattern is eligible for candidate-method assembly.
_Avoid_: Similarity score, relevance note, citation match

**Assembly Role**:
The role a Method Pattern may play inside a candidate method after Need-Pattern Fit is established, such as input processor, retriever, planner, memory manager, critic, training objective, data generator, evaluation proxy, or controller.
_Avoid_: Model component by default, paper label, arbitrary module name

**Candidate Method Assembly**:
A workflow step that combines eligible Method Patterns into 3-5 comparable Candidate Methods, making coverage, roles, flows, novelty hypotheses, weak links, feasibility, and experiment implications explicit.
_Avoid_: Single best method, architecture drafting, method brainstorming

**Candidate Method**:
A possible method design assembled from Method Patterns, recording its method thesis, covered and uncovered Method Needs, Assembly Roles, inputs, modules, outputs, training or inference flow, source papers, novelty hypothesis, weakest link, feasibility, experiment implications, and status.
_Avoid_: Final method, implementation plan, idea sketch

**Committed Method Design**:
A human-owned method design that the researcher has chosen or authored after method inspiration, stable enough to serve as the source method for experiment design, baseline search, metric search, positioning, or risk-objection workflows.
_Avoid_: Candidate Method, agent-generated method, real method

**Method Candidate Library**:
The final artifact of a Method Inspiration Workflow, containing several Candidate Methods plus the selected, deferred, and rejected Method Patterns, transfer judgments, source URLs, risks, disposition reasons, and evidence statuses needed to compare and later revise them.
_Avoid_: Method summary, chosen architecture, paper list

**Method Pattern Disposition**:
The recorded outcome for a Method Pattern after Transfer Mapping, such as selected for assembly, deferred, or rejected, with reasons such as mismatch, too-strong assumptions, high integration cost, weak evidence, or excessive similarity to a baseline.
_Avoid_: Hidden discard, gut-feel filtering, unexplained exclusion

**Candidate Method Selection Gate**:
The required confirmation step before finalizing the Method Candidate Library; it is passed only when the user confirms, revises, replaces, or explicitly delegates the 3-5 Candidate Methods and their assembly rationales.
_Avoid_: Automatic final method choice, unconfirmed architecture, single winner, choosing a Committed Method Design

**Problem Reality Check Workspace**:
A durable artifact set for single-card Problem Reality Checks from exactly one Research Question Workspace, organized around source-card routing, per-card check reports, cross-report comparison, and evidence needs.
_Avoid_: Research Question Workspace subfolder, comments folder, review notes dump

**Source Card Gate**:
The required routing step before a Problem Reality Check begins; it is passed only when exactly one source Research Question Card is identified and its key metadata is recorded.
_Avoid_: Optional card selection, broad question-area review

**Reality Check Dimension**:
A required interrogation lens inside a Problem Reality Check, covering one aspect of whether the Research Question Card's problem is real, grounded, supported, unsolved, safely motivated, and well-scoped.
_Avoid_: Loose checklist item, score category, reviewer comment type

**Challenge Question**:
An attack-style but answerable question inside a Problem Reality Check, pairing a skeptical claim with the hidden assumption being tested, the evidence that would satisfy the challenge, and the recommended answer or likely verdict.
_Avoid_: Generic checklist prompt, yes/no question, vague concern

**Interrogation Transcript**:
A durable turn-by-turn record of a Problem Reality Check, capturing each Challenge Question, the agent's provisional recommendation, the user's response or correction, and the resulting dimension verdict before the final report is written.
_Avoid_: One-shot report, hidden reasoning, informal chat log

**Research Question Workspace**:
A durable artifact set for research-question selection derived from exactly one Field Map Workspace and organized around candidate angles, writing intent, and Research Question Cards.
_Avoid_: Field map subfolder, brainstorming folder, topic shortlist

**Writing Intent**:
The user's explicit priority order for choosing research questions, including the main paper-writing goal, secondary goals, and practical constraints that shape how Research Opportunity Candidates are turned into Research Question Cards.
_Avoid_: Preference, taste, vague goal

**Guided Choice**:
A narrowing interaction in which the agent offers multiple viable options or a binary tradeoff before asking the user to choose, so research-question selection converges through comparison instead of single-option confirmation.
_Avoid_: Single recommendation, yes/no confirmation, open-ended preference question

**Candidate Angle**:
A narrower research cut derived from a Research Opportunity Candidate and shaped by a possible contribution type, such as benchmark, method, system, study, theory, or evaluation protocol.
_Avoid_: Subtopic, idea variant, direction

**Contribution Type**:
The primary kind of research contribution a Candidate Angle is expected to make, such as benchmark, evaluation protocol, defense method, system, human study, conceptual model, or empirical measurement.
_Avoid_: Paper type, format, flavor

**Evidence Sufficiency Check**:
A gate in the Research Question workflow that decides whether a Candidate Angle has enough paper-backed support to become a Research Question Card, needs targeted evidence collection, or should be deferred.
_Avoid_: Gut check, confidence score, quick validation

**Supporting Evidence**:
Additional paper-backed evidence collected during the Research Question workflow to support a Candidate Angle or Research Question Card when the source Field Map Workspace is not sufficient.
_Avoid_: Proof, justification text, invented support

**Field Map Report**:
A zero-build static HTML report inside a Field Map Workspace that organizes the boundary, seed set, search strategy, clusters, paper table, opportunities, and next actions for human reading.
_Avoid_: Web app, dashboard

## Example Dialogue

Dev: "Should `field map` just output `research_clusters.md`?"

Domain expert: "No. Use **Field Map Workflow** for the full process. It creates one **Field Map Workspace**, starts with the **Field Boundary**, uses **Seed Papers** to expand the literature set, groups papers into **Research Clusters**, and ends by naming **Research Opportunities**."

Dev: "Should we run a `risk objection` pass on all three question cards?"

Domain expert: "Not for problem motivation. Use a **Problem Reality Check** after the **Source Card Gate** selects exactly one **Research Question Card**. The check asks one **Challenge Question** at a time, records an **Interrogation Transcript**, then writes one **Problem Reality Check Report**, assigns a **Problem Reality Verdict**, flags **Unsafe Motivation Claims**, and records **Targeted Evidence Needs** without launching a new paper search."

Dev: "Can the theoretical grounding skill just list provenance theory, trust theory, and governance theory?"

Domain expert: "No. Use a **Theoretical Grounding Workflow** only after the **Theoretical Grounding Source Gate** finds one checked card and its completed **Problem Reality Check Report**. First write a **Problem-Theory Decomposition**, confirm the **Theory-Support Claims**, extract **Theory Hooks**, run **Targeted Theory Search**, then keep only **Selected Theoretical Traditions** that support claim-centered **Theoretical Pillars** in the final **Theoretical Grounding Report**. If sources are still thin after search, record a **Theory Evidence Need** instead of pretending the theory support is final."

Dev: "Can method inspiration start from a rough problem?"

Domain expert: "Yes, but call the routing step the **Method Inspiration Source Gate**. Prefer one **Research Question Card** as the source; if the user only has a rough problem, write a **Source Problem Brief** and mark downstream method candidates as provisional until the problem has been checked."

Dev: "Should method inspiration end by asking the user to choose the final method?"

Domain expert: "No. Respect the **Method Inspiration Boundary**: 05 ends with a **Method Candidate Library**, not a **Committed Method Design**. The later **Method Commitment Workflow** is reserved for the human researcher to turn inspiration into an owned method design."
