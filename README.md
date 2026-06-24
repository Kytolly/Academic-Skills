# Paper Reading Skills

Languages: English | [Chinese](README.zh-CN.md)

> A research-oriented Codex skill suite that turns paper reading into structured research decisions.

Paper Reading Skills is a suite of Codex skills for early-stage research. Its goal is not to summarize papers in isolation, but to help researchers organize reading around a clear research motivation at each stage and turn reading results into durable artifacts that can support the next research move.

A lot of inefficient reading happens not because papers are too hard, but because the reader has not clarified these questions before reading:

* Why am I reading these papers?
* Which research decision am I trying to make right now?
* Which parts of the papers should I focus on?
* What should this reading session produce?
* When is it enough to stop?

This project breaks paper reading into a set of common research actions, with a workflow, input boundary, reading strategy, output format, and stopping condition for each action.

---

## Core Idea

Ordinary paper reading often aims at "finishing papers." This project aims at "making research judgments."

For example:

* When entering a new direction, start by building a field map instead of rushing into paper summaries.
* When you have an early idea, run a problem reality check before designing a method.
* When a method starts taking shape, pass through method commitment before treating it as a final plan.
* When preparing to write a paper, organize around close work, claim support, and positioning instead of broad related-work collection.

Each skill corresponds to a concrete research stage and produces artifacts that downstream workflows can consume.

---

## Skill Map

| Stage | Skill | Research Question It Helps Answer | Main Output |
| ----- | ----- | --------------------------------- | ----------- |
| 01 | Field Map | What are the main branches, method routes, and research opportunities in this field? | Field map / research clusters / opportunity candidates |
| 02 | Research Question | Which gaps can become actionable research questions? | Research question cards |
| 03 | Problem Reality Check | Is this problem real, or only superficially plausible? | Problem justification / risk notes |
| 04 | Theoretical Grounding | Is there theoretical support that can strengthen the problem framing? | Theoretical grounding package |
| 05 | Method Inspiration | Which mechanisms from papers can be transferred into candidate methods? | Method candidate library |
| 06 | Method Commitment | Is the current method stable enough for the researcher to own? | Committed / provisional / redesign / rejected method outcome |
| 07 | Experiment Design | How can claims be translated into verifiable experiment designs? | Experiment plan / baseline pressure matrix / claim-metric map |
| 08 | Research Framing | How should this research be positioned in the paper narrative and related-work comparison? | Research framing package |
| Extra | Workspace Presentation | How can an existing research workspace become a browsable, handoff-ready interface? | Interactive presentation workspace |

---

## Workflow

The skills are designed as a research pipeline:

```text
Field Map
  |
  v
Research Question
  |
  v
Problem Reality Check
  |
  v
Theoretical Grounding
  |
  v
Method Inspiration
  |
  v
Method Commitment
  |
  v
Experiment Design
  |
  v
Research Framing
  |
  v
Workspace Presentation
```

This pipeline is not strictly linear. Users can start from any stage depending on their current research state.

For example:

* If the user is new to a field, start with `01-field-map`.
* If the user already has an idea but is unsure whether it is valid, start with `03-problem-reality-check`.
* If the user has several candidate methods, start with `06-method-commitment`.
* If the user already has a stable method and wants to design experiments, start with `07-experiment-design`.

---

## Example Use Cases

### 1. Entering a New Research Direction

User goal:

> I want to understand LLM agent evaluation, but I do not know the main branches yet.

Recommended skill:

```text
01-field-map
```

Expected output:

* field boundary
* seed paper set
* paper position records
* research clusters
* opportunity candidates
* static HTML field report

---

### 2. Turning a Vague Gap into a Research Question

User goal:

> I found several gaps in related work, but I do not know which one is worth pursuing.

Recommended skill:

```text
02-research-question
```

Expected output:

* candidate research questions
* motivation notes
* feasibility risks
* evidence requirements
* recommended next step

---

### 3. Stress-testing a Research Idea

User goal:

> I have an idea, but I am worried the problem may already be solved or not important enough.

Recommended skill:

```text
03-problem-reality-check
```

Expected output:

* problem existence check
* evidence support
* prior-solution risk
* motivation safety notes
* recommended reframing or stop condition

---

### 4. Converging on a Method

User goal:

> I have several candidate methods and want to decide what my final method should be.

Recommended skill:

```text
06-method-commitment
```

Expected output:

* source method
* method reconstruction
* challenge questions
* decision log
* method commitment status
* downstream routing suggestion

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/snake-fan/Paper-Reading-Skills.git
cd Paper-Reading-Skills
```

Each numbered directory contains one Codex skill:

```text
01-field-map/
02-research-question/
03-problem-reality-check/
04-theoretical-grounding/
05-method-inspiration/
06-method-commitment/
07-experiment-design/
08-research-framing/
workspace-presentation/
```

Before using a skill, identify the current research state:

```text
I am currently trying to:
- understand a field
- find a research question
- verify whether a problem is real
- find theoretical support
- get method inspiration
- commit to a method
- design experiments
- frame the paper
```

Then invoke the corresponding skill in Codex.

Example prompt:

```text
Use the field-map skill to help me map the research field of memory safety in LLM agents.
I want to identify major branches, representative papers, evaluation settings, saturated areas, and possible research opportunities.
```

---

## Output Philosophy

Each skill is designed to produce durable research artifacts, not temporary chat summaries.

The outputs should be:

* traceable: important claims should connect back to papers or prior artifacts;
* decision-oriented: each artifact should help the user make a research decision;
* reusable: downstream skills should be able to consume upstream outputs;
* bounded: each workflow should have clear stopping conditions;
* honest about uncertainty: weak evidence, unresolved risks, and unsafe claims should be explicitly recorded.

---

## Design Principles

### 1. Motivation-first reading

The project assumes that paper reading should start from the user's current research motivation, not from a generic summary template.

### 2. Artifact-driven workflow

Every skill writes structured artifacts so that research progress does not disappear inside chat history.

### 3. Human-owned decisions

The agent can propose, organize, attack, and summarize, but important research commitments should remain visible to the user.

### 4. Downstream routing discipline

Not every output should be passed downstream. For example, a weak problem should not automatically enter method design, and a provisional method should not be treated as experiment-ready.

### 5. Evidence-aware framing

The project avoids turning weak evidence into strong claims. It records what can be safely claimed, what needs more support, and what should be avoided.

---

## Repository Structure

```text
.
├── README.md
├── README.zh-CN.md
├── 01-field-map/
│   └── SKILL.md
├── 02-research-question/
│   └── SKILL.md
├── 03-problem-reality-check/
│   └── SKILL.md
├── 04-theoretical-grounding/
│   └── SKILL.md
├── 05-method-inspiration/
│   └── SKILL.md
├── 06-method-commitment/
│   └── SKILL.md
├── 07-experiment-design/
│   └── SKILL.md
├── 08-research-framing/
│   └── SKILL.md
└── workspace-presentation/
    ├── SKILL.md
    ├── references/
    └── templates/
```

---

## Current Status

Completed:

* core skill structure
* field map workflow
* research question workflow
* problem reality check workflow
* theoretical grounding workflow
* method inspiration workflow
* method commitment workflow
* experiment design workflow
* research framing workflow
* workspace presentation workflow

In progress:

* improving cross-skill artifact compatibility
* refining workflow gates and status routing
* adding more example workspaces
* improving presentation templates

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
