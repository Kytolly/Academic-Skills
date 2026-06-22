---
name: paper-reading-research-framing
description: Use when the user's current research is stable enough to turn into paper framing by comparing closest related works, checking claim-level citation support, clarifying positioning and differentiation, and extracting writing moves.
---

# Research Framing

Use this skill for the motivation: 形成论文表达 / 研究定位 / 引用支撑.

This skill merges the former citation-checking, differentiation, and writing-pattern motivations. They are not separate workflows here; they are three lenses on one question:

> How should this current research be stated as a paper, compared with similar work, and made to look both credible and distinctive?

## Output Root

Set `{workspace-root}` before creating, scanning, or updating artifacts:

- Default `{workspace-root}` to `workspace` (the repo-local `workspace/` directory).
- If the user specifies a workspace root, use that path exactly and do not add another `workspace/` layer.
- If the user provides an existing artifact or workflow path, infer `{workspace-root}` from that path and keep related artifacts under the same root.
- Do not create new generated workflow directories directly at the repository root.

## Core Workflow

1. Identify exactly one current research source: a Research Question Card, Committed Method Design, experiment plan, proposal draft, or user-provided research brief.
2. Pass the Research Framing Source Gate by recording what is stable, provisional, and out of scope.
3. Create or resume a Research Framing Workspace at `{workspace-root}/research-framing/{project-slug}/`.
4. Write or update `source_research.md`.
5. Build the Close Work Set: the 3-8 papers or systems the paper must be compared against.
6. Extract each close work's problem, method, setting, assumptions, evaluation, claims, and writing moves into `close_works.md`.
7. Draft `claim_support_bank.md`, mapping the user's key claims to papers that support, weaken, or fail to support them.
8. Draft `positioning_matrix.md`, comparing the user's work with close works across problem, method, setting, assumptions, evidence, and contribution type.
9. Draft `story_spine.md`, naming the paper-level story, gap framing, contribution highlights, novelty boundary, and claims to avoid.
10. Draft `writing_moves.md`, collecting reusable motivation framing, related-work transitions, contrast patterns, contribution wording, limitation wording, and figure/table patterns.
11. Ask the user to confirm, revise, or explicitly delegate the story spine and positioning.
12. Write `research_framing_package.md`.
13. Stop when the user can state the paper story, name the closest works, explain the difference from each, and support the main claims with credible citations.

## Framing Boundary

Research Framing is a writing-facing comparison workflow. It does not invent a new research problem, commit a method, or design experiments.

Use it to decide:

- what story the paper should tell,
- which close works define the comparison frame,
- which claims are citation-supported,
- how the paper differs from similar research,
- which contribution highlights are worth foregrounding,
- and which writing moves can be borrowed structurally.

Do not use it to:

- run a broad Field Map Workflow,
- validate whether the problem is real,
- choose the actual method,
- select baselines or metrics,
- or produce reviewer objections beyond writing-relevant positioning risks.

## Research Framing Source Gate

The workflow must begin from exactly one current research source:

- Research Question Card,
- Committed Method Design,
- experiment plan,
- proposal or paper draft,
- or user-provided research brief.

The gate is passed only when the following are recorded:

- source artifact or user-provided source text,
- current problem statement,
- current method or intervention, if any,
- target contribution type,
- key claims that need support,
- known close works or suspected close works,
- intended venue or audience, if known,
- provisional or unstable parts that should not be overclaimed,
- and the user's writing goal: introduction, related work, proposal, rebuttal prep, method positioning, or full paper framing.

If the source is not stable enough to frame as a paper, recommend the upstream workflow that should run first, such as `paper-reading-research-question`, `paper-reading-method-commitment`, or `paper-reading-experiment-design`.

## Research Framing Workspace

Create durable artifacts at:

```text
{workspace-root}/research-framing/{project-slug}/
```

Use this structure:

- `source_research.md`
- `close_works.md`
- `claim_support_bank.md`
- `positioning_matrix.md`
- `story_spine.md`
- `writing_moves.md`
- `research_framing_package.md`

## Reading Lenses

Read close papers with five lenses.

**Claim support**:
For each user claim, record whether a paper directly supports it, weakly supports it, contradicts it, narrows it, or only provides background. A citation is usable only when the paper supports the actual strength and scope of the claim.

**Positioning and differentiation**:
Compare the user's work with each close work across problem, method, setting, assumptions, evidence, and contribution. The goal is not to prove total uniqueness; it is to state a defensible novelty boundary.

**Story spine**:
Identify the narrative route that makes the current research feel necessary: known situation, unresolved tension, closest-work limitation, intervention, evidence plan, and contribution.

**Contribution highlights**:
Name what should be foregrounded because it is both true and differentiating: new problem framing, new mechanism, new setting, stronger evidence, clearer evaluation, useful system behavior, theoretical reframing, or practical constraint.

**Writing moves**:
Extract reusable rhetorical structures without copying prose: motivation openings, gap packaging, contrast transitions, contribution lists, related-work grouping, limitation handling, and figure or table patterns.

## Required Final Package

`research_framing_package.md` must include:

- source research summary,
- Close Work Set,
- paper story spine,
- positioning matrix summary,
- claim support bank summary,
- contribution highlights,
- safe claims and claims to avoid,
- reusable writing moves,
- recommended introduction or related-work outline,
- and remaining framing risks.

## Stop Conditions

Stop when all are true:

- the user can name the 3-8 closest works,
- the user can explain the difference from each close work,
- the main motivation and contribution claims have citation support or safer wording,
- the paper story is stated in a compact form,
- and the user has writing moves or an outline that can be transferred into the paper.
