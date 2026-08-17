# {Paper Title}

## One-Sentence Takeaway

{One sentence describing the paper's central move and why it matters.}

## Paper Information Card

> Title: {title in English, Italic}
> Authors: {authors} 
> Status: {year and venue or preprint status}
> Resource: | {stable URL, DOI, or identifier} |

## Research Problem

- Problem:
- Why it matters:
- Gap in prior work:

## Field Position

- Research branch:
- Method route:
- Closest prior approaches:
- Claimed differentiation:

## Core Idea

Explain the method at the level needed to reconstruct its logic. Separate paper claims from interpretation.

### Paper claim

{Claim with page or section citation.}

### Interpretation

{Agent synthesis, explicitly marked as interpretation.}

## Method

### Inputs and outputs

- Input:
- Output:

### Architecture or pipeline

{Mechanism, modules, information flow, and training/inference distinction.}

![{Figure number and content-focused caption}](assets/{figure-filename}.png)

### Objective and training

{Important losses, supervision, data construction, or optimization choices.}

## Mathematical Formulation

Use `$...$` for inline mathematics, such as $x_{t+1}=f(x_t,a_t)$.

Use `$$...$$` for display mathematics:

$$
\mathcal{L}(\theta)=\sum_t \ell_\theta(x_t,a_t)
$$

Define symbols and cite the paper section or equation number.

## Data and Evaluation

- Datasets or environments:
- Baselines:
- Metrics:
- Protocol:
- Ablations or controls:

![{Table number and content-focused caption}](assets/{table-filename}.png)

## Main Findings

| Finding | Evidence | Scope | Confidence / caveat |
|---|---|---|---|
| {Finding} | {Page, figure, table, or experiment} | {What was actually tested} | {Caveat} |

## Assumptions and Limitations

- Assumptions:
- Reported limitations:
- Additional interpretation:
- Threats to validity:

## Reusable Ideas

- Transferable mechanism:
- Useful experimental pattern:
- Data construction idea:
- What should not be transferred blindly:

## Open Questions

1. {Question raised by evidence or limitations}

## Reproduction Notes

- Code / project page:
- Required data or environment:
- Missing implementation details:
- Expected reproduction risks:

## User Notes

{Preserve user-authored observations here and attribute them clearly.}
