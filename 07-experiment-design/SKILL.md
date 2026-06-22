---
name: paper-reading-experiment-design
description: Use when the user has a method idea or Committed Method Design and reads papers to design tasks, datasets, baselines, metrics, ablations, human evaluation, user studies, or a claim-to-evidence experiment plan.
---

# Experiment Design

Use this skill to turn a stable method's claims into an experiment plan. Treat the skill as a `Claim -> Evidence -> Protocol -> Reviewer Defense` converter: it does not complete the method, and it does not begin from benchmark, baseline, or metric lists. Baseline selection and metric selection are part of this workflow, not separate downstream skills.

If the Method Thesis, Mechanistic Claim, target failure, or intervention point is still unclear, route the user back to method commitment instead of inventing experiments for an unstable method.

## Output Root

Set `{workspace-root}` before creating, scanning, or updating artifacts:

- Default `{workspace-root}` to `workspace` (the repo-local `workspace/` directory).
- If the user specifies a workspace root, use that path exactly and do not add another `workspace/` layer.
- If the user provides an existing artifact or workflow path, infer `{workspace-root}` from that path and keep related artifacts under the same root.
- Do not create generated workflow directories directly at the repository root.

Create or resume one experiment folder at:

```text
{workspace-root}/experiment-designs/{field-slug}/{method-or-question-slug}/
```

Use `references/workspace-structure.md` for the artifact layout.

## Core Workflow

1. Locate the source method or source research question.
2. Pass the Experiment Design Source Gate.
3. Create or resume an experiment folder at `{workspace-root}/experiment-designs/{field-slug}/{method-or-question-slug}/`.
4. Write or update `source_experiment_context.md`.
5. Read the source artifact and relevant local context before decomposing claims.
6. If the source is not a Committed Method Design, write a Minimal Experiment Brief and mark every downstream artifact as provisional.
7. Decompose the Method Thesis, Mechanistic Claim, target outcomes, assumptions, and downstream pressure points into `claim_evidence_map.md`.
8. Pass the Claim-Evidence Review Gate before searching for benchmarks, baselines, or metrics.
9. Select evidence routes and an Experiment Stack for the key claims.
10. Search or inspect papers for tasks, datasets, evaluation settings, human-evaluation instruments, user-study patterns, and prior protocols that can test the claims.
11. Write `experiment_design.md` with the proposed tasks, data, protocol, comparisons, human evaluation or user study plan when needed, expected evidence, reviewer-objection coverage, and result interpretation contract.
12. Write `baseline_pressure_matrix.md`, choosing baselines that fairly pressure-test the method rather than merely filling a list.
13. Write `claim_metric_map.md`, mapping each key claim to observables, metrics, measurement protocol, validity risks, and failure interpretation.
14. Write `ablation_and_controls.md`, including component ablations, confound checks, stress tests, and negative or sanity checks.
15. Pass the Experiment Design Review Gate before treating the plan as final rather than provisional.
16. Stop when the user can draft the experiment section and justify why the design tests the paper's key claims.

If an experiment folder already exists, read the current artifacts first. Preserve user edits and update existing files instead of overwriting them blindly.

## Source Gate

Prefer a `committed_method_design.md` from `paper-reading-method-commitment`. It is the normal source for experiment design.

Allowed sources:

- Committed Method Design, preferred
- Research Question Card with a concrete possible study
- Source Problem Brief or rough method, only if the user explicitly wants a provisional experiment sketch

The gate is passed only when `source_experiment_context.md` records:

- source artifact path or user-provided source
- source status: committed / research-question / provisional
- Method Thesis or research question
- Mechanistic Claim, if available
- target outcome
- target failure and intervention point
- required ablations, implied baseline pressures, and implied metric signals, if available
- non-goals and scope boundaries
- evidence gaps or do-not-route warnings inherited from upstream artifacts

If the source method is not committed, mark the experiment design as `provisional` and do not present it as final validation evidence.

## Local Context Review Rules

Before writing `claim_evidence_map.md`, inspect the available local context. Default to local artifacts; do not start a broad web search until the source claims and evidence routes are explicit.

For a Committed Method Design source, read relevant available artifacts:

- `committed_method_design.md`
- `method_commitment_summary.md`
- `method_reconstruction.md`
- `method_attack_transcript.md`
- `method_decision_log.md`
- upstream source problem, Problem Reality Check, Method Inspiration, or Research Question artifacts referenced by the method commitment folder

For a Research Question Card, Source Problem Brief, rough method, or user-provided source, read relevant available artifacts:

- source Research Question Card or Source Problem Brief
- Problem Reality Check report and transcript, if available
- Method Inspiration `source_problem.md`
- `method_need_decomposition.md`
- `candidate_methods.md`
- `method_candidate_library.md`
- any local notes naming close work, expected baselines, benchmark candidates, metric concerns, feasibility constraints, unsafe motivation claims, or do-not-route warnings

Preserve inherited fragilities. If the source lacks a stable Method Thesis, Mechanistic Claim, target failure, intervention point, or target outcome, record the gap in `source_experiment_context.md` and route back to method commitment instead of fabricating an experiment plan.

## Minimal Experiment Brief

Use this section in `source_experiment_context.md` when the source is a Research Question Card, Source Problem Brief, rough method, or otherwise not a Committed Method Design.

Record:

- Method Thesis or research question
- Mechanistic Claim, if available
- target failure
- intervention point
- target outcome
- scope
- non-goals
- weakest link or main uncertainty
- main reviewer objection
- experiment design status: committed / research-question-level / provisional

If the Method Thesis, Mechanistic Claim, target failure, and intervention point cannot be stated without invention, stop and recommend method commitment before experiment design continues.

## Claim-Evidence Map

Do not start from a list of datasets or metrics. First map what must be proven or could be refuted.

For each key claim, record:

- claim type: problem, mechanism, performance, robustness, safety, usability, efficiency, or generalization
- observable evidence needed
- evidence route: standard benchmark, targeted workload, synthetic controlled task, real-world case study, ablation study, stress test, human evaluation, user study, or error analysis
- task or scenario that could expose the evidence
- baseline pressure needed
- metric signal needed
- ablation or control needed
- likely failure interpretation
- evidence strength: direct evidence / strong proxy / weak proxy / anecdotal evidence / speculative
- reviewer objection the evidence would answer

Every later task, baseline, metric, and ablation should trace back to at least one claim.

## Claim-Evidence Review Gate

Before searching for benchmarks, baselines, or metrics, ask the user to confirm, revise, or explicitly delegate the Claim-Evidence Map. The gate is passed only when the key claims and evidence routes are explicit enough that later choices can be traced back to them.

Use live challenge questions for high-risk claim decisions, especially when:

- a performance metric is being used as evidence for a mechanism claim
- a weak proxy is being used for a core claim
- the target failure is not exposed by the proposed task
- the claim requires a human evaluation or user study but the route is being avoided
- the evidence route would only show a narrow improvement while the claim is broad

Record the user's response or explicit delegation in `claim_evidence_map.md`.

## Evidence Routes And Experiment Stack

Choose evidence routes claim by claim. Not every claim needs a large experiment, but every core claim needs at least one explicit evidence route.

Common evidence routes:

- standard benchmark for performance, generalization, or comparison against existing work
- targeted workload for a specific failure or mechanism
- synthetic controlled task for mechanism validation and variable control
- real-world case study for scenario realism and system value
- ablation study for component or mechanism necessity
- stress test for robustness, safety, or boundary conditions
- human evaluation for subjective quality, understanding, trust, or usefulness
- user study for learning effects, behavior change, interaction benefits, or workflow impact
- error analysis for failure modes and applicability boundaries

Use an Experiment Stack to avoid proving only a narrow main effect while making broader claims. Include only layers that match the source method's actual claims:

1. Main Effect Experiment
2. Mechanism / Ablation Experiment
3. Robustness or Stress Test
4. Generalization Test
5. Human Evaluation or User Study, if needed
6. Cost / Efficiency Analysis
7. Failure Analysis

## Task And Dataset Design

Read papers to identify reviewer-recognizable evaluation settings and reusable protocols. Prioritize tasks and datasets that pressure-test the Mechanistic Claim, not just convenient benchmarks.

For each task or dataset, record:

- source paper or benchmark
- why it matches the target failure
- what claim it can test
- what it cannot test
- data availability and reproducibility
- expected comparison setup
- risks: leakage, saturation, distribution mismatch, annotation ambiguity, or construct mismatch

If no existing task fits the claim, propose a new task or data construction route and mark the missing benchmark evidence explicitly.

## Baseline Pressure Matrix

Baseline selection belongs here.

Choose baselines by pressure type:

- lower-bound or trivial baseline
- classic or reviewer-expected baseline
- strongest recent baseline
- closest prior work
- component-equivalent baseline that isolates the new mechanism
- ablated version of the proposed method
- oracle, upper-bound, or human reference when meaningful

For each baseline, record:

- what claim it pressures
- why it is fair
- what advantage or disadvantage it has
- reproducibility status
- whether it is required, optional, or rejected
- what reviewer objection it answers
- remaining weakness after including it

Do not include a baseline only because it is popular. Do not exclude close work because it is hard unless the limitation is recorded.

Map baseline pressure to reviewer objections:

- lower-bound or trivial baseline: answers whether the method only beats weak alternatives
- classic or reviewer-expected baseline: answers whether the method beats the field's default approach
- strongest recent baseline: answers whether the method is competitive with current work
- closest prior work: answers whether the method is just a repeat of an existing method
- component-equivalent baseline: answers whether gains come from the claimed mechanism rather than extra information, compute, tools, or privileges
- ablated proposed method: answers whether the core module or invariant is necessary
- oracle, upper-bound, or human reference: answers how far the method is from an idealized or expert ceiling

## Claim-Metric Map

Metric selection belongs here.

For each claim, map:

- observable construct
- primary metric
- secondary or diagnostic metric
- measurement protocol
- direction of improvement
- minimal meaningful effect or qualitative success criterion, if known
- failure interpretation
- metric validity risk

Avoid standalone metric banks. A metric is useful only when it measures a claim in a specific protocol.

Metric selection should make a claim observable. If the metric only measures a proxy, record whether the proxy is strong, weak, anecdotal, or speculative evidence and name the construct mismatch.

If the claim involves understanding, learning gain, personalization, Theory of Mind accuracy, dialogue quality, safety, or human trust, prefer validated metrics or established human-evaluation instruments from prior papers when available. Record construct mismatch rather than pretending a proxy is direct evidence.

## Ablations And Controls

Use ablations to test the Mechanistic Claim.

Include:

- component removal or replacement
- intervention-point ablation
- data-source or memory-source ablation
- objective, controller, or decision-rule ablation
- stress tests for the weakest link
- negative controls or sanity checks
- confound checks for data leakage, prompt sensitivity, annotation bias, or unfair baseline access

Each ablation must explain which mechanism or assumption it tests.

For each ablation or control, record:

- mechanism or assumption being tested
- expected result if the Mechanistic Claim holds
- interpretation if performance does not change
- interpretation if performance drops
- whether the result supports the mechanism or merely changes information access, compute, strictness, or utility

## Result Interpretation Contract

Before finalizing `experiment_design.md`, write a result interpretation contract that states how major result patterns should change the claim, method, or paper story.

At minimum, cover:

- main metric improves but ablation does not drop: performance claim may hold, mechanism claim is weak
- safety improves but task success drops sharply: method may be over-conservative
- strong benchmark result but weak targeted workload result: general performance may hold, target failure may not be solved
- human evaluation improves but automatic metric does not: explain the construct difference or downgrade the automatic metric
- close-work baseline matches the method: novelty or mechanism boundary needs revision
- proxy metric improves but direct evidence is missing: keep the claim narrow or record an evidence gap

## Experiment Design Review Gate

Before presenting the artifacts as a final experiment plan, ask the user to confirm, revise, or explicitly delegate the experiment design decisions. This is a workflow validation gate, not a human evaluation experiment.

The gate is passed only when the user accepts or delegates:

- the key claim decomposition
- the evidence route for each core claim
- the Experiment Stack layers included or intentionally omitted
- required baselines and the reviewer objections they answer
- primary metrics and their validity risks
- required ablations, controls, and stress tests
- result interpretation contract and failure implications

If the user rejects a key decision, update the affected artifact immediately before continuing. If the user delegates, record the delegation and keep the design status `provisional` unless the source method is committed and no unresolved gate issue remains.

## Output Artifacts

Create or update these files in the experiment folder:

- `source_experiment_context.md`
- `claim_evidence_map.md`
- `experiment_design.md`
- `baseline_pressure_matrix.md`
- `claim_metric_map.md`
- `ablation_and_controls.md`

Artifact responsibilities:

- `source_experiment_context.md`: source status, Minimal Experiment Brief when needed, Method Thesis, Mechanistic Claim, target failure, intervention point, scope, non-goals, weakest link, and inherited warnings
- `claim_evidence_map.md`: claim decomposition, evidence routes, evidence strength, reviewer-objection links, and Claim-Evidence Review Gate record
- `experiment_design.md`: Experiment Stack, tasks, data, protocols, human evaluation or user study plan when needed, expected evidence, failure analysis, and Result Interpretation Contract
- `baseline_pressure_matrix.md`: baselines organized by pressure type, claim attacked, fairness, reproducibility, reviewer objection, and remaining weakness
- `claim_metric_map.md`: observable constructs, primary and diagnostic metrics, measurement protocols, success criteria, validity risks, and failure interpretations
- `ablation_and_controls.md`: mechanism-linked ablations, controls, stress tests, sanity checks, confound checks, and what each result would mean

Use the reference templates in this directory when creating these artifacts.

## Required Templates

Use the reference templates in this directory:

- `references/workspace-structure.md`
- `references/source-experiment-context-template.md`
- `references/claim-evidence-map-template.md`
- `references/experiment-design-template.md`
- `references/baseline-pressure-matrix-template.md`
- `references/claim-metric-map-template.md`
- `references/ablation-and-controls-template.md`

## Stop Condition

Stop when every key claim has:

- at least one task, dataset, workload, human-evaluation, user-study, or error-analysis route
- at least one relevant baseline pressure or a recorded reason none applies
- at least one metric signal with a measurement protocol
- at least one ablation, control, or confound check
- a clear failure interpretation
- an evidence-strength label
- a reviewer-objection mapping where relevant
- a passed or explicitly delegated review-gate decision

The user should be able to draft the experiment section as `Claim -> Setting -> Baseline -> Metric -> Expected Evidence -> Failure Interpretation`.
