---
name: paper-reading-experiment-design
description: Use when the user has a method idea or Committed Method Design and reads papers to design tasks, datasets, baselines, metrics, ablations, human evaluation, user studies, or a claim-to-evidence experiment plan.
---

# Experiment Design

Use this skill to turn a method's claims into an experiment plan. Baseline selection and metric selection are part of this workflow, not separate downstream skills.

## Output Root

Set `{workspace-root}` before creating, scanning, or updating artifacts:

- Default `{workspace-root}` to `workspace` (the repo-local `workspace/` directory).
- If the user specifies a workspace root, use that path exactly and do not add another `workspace/` layer.
- If the user provides an existing artifact or workflow path, infer `{workspace-root}` from that path and keep related artifacts under the same root.
- Do not create generated workflow directories directly at the repository root.

## Core Workflow

1. Locate the source method or source research question.
2. Pass the Experiment Design Source Gate.
3. Create or resume an experiment folder at `{workspace-root}/experiment-designs/{field-slug}/{method-or-question-slug}/`.
4. Write or update `source_experiment_context.md`.
5. Decompose the Method Thesis, Mechanistic Claim, target outcomes, assumptions, and downstream pressure points into `claim_evidence_map.md`.
6. Search or inspect papers for tasks, datasets, evaluation settings, and prior protocols that can test the claims.
7. Write `experiment_design.md` with the proposed tasks, data, protocol, comparisons, human evaluation or user study plan when needed, and expected evidence.
8. Write `baseline_pressure_matrix.md`, choosing baselines that fairly pressure-test the method rather than merely filling a list.
9. Write `claim_metric_map.md`, mapping each key claim to observables, metrics, measurement protocol, and failure interpretation.
10. Write `ablation_and_controls.md`, including component ablations, confound checks, stress tests, and negative or sanity checks.
11. Stop when the user can draft the experiment section and justify why the design tests the paper's key claims.

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

## Claim-Evidence Map

Do not start from a list of datasets or metrics. First map what must be proven.

For each key claim, record:

- claim type: problem, mechanism, performance, robustness, safety, usability, efficiency, or generalization
- observable evidence needed
- task or scenario that could expose the evidence
- baseline pressure needed
- metric signal needed
- ablation or control needed
- likely failure interpretation
- evidence strength: direct / indirect / proxy / speculative

Every later task, baseline, metric, and ablation should trace back to at least one claim.

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

Do not include a baseline only because it is popular. Do not exclude close work because it is hard unless the limitation is recorded.

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

## Output Artifacts

Create or update these files in the experiment folder:

- `source_experiment_context.md`
- `claim_evidence_map.md`
- `experiment_design.md`
- `baseline_pressure_matrix.md`
- `claim_metric_map.md`
- `ablation_and_controls.md`

## Stop Condition

Stop when every key claim has:

- at least one task, dataset, or study route
- at least one relevant baseline pressure or a recorded reason none applies
- at least one metric signal with a measurement protocol
- at least one ablation, control, or confound check
- a clear failure interpretation

The user should be able to draft the experiment section outline from the artifacts.
