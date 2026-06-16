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
