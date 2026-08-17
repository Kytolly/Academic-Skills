# WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models

Resource: local Zotero PDF; arXiv:2606.31672

Year: 2026

Venue: arXiv preprint / benchmark

Source Verified: Yes

Discovery Source: Zotero search

## Research Problem

Short-rollout metrics hide per-frame control failures, mid-sequence visual collapse, physical violations, and failed scene revisits. How should long-horizon interactive stability be evaluated?

## Field Position

Long-horizon open-world evaluation branch. It complements WorldMark's standardized cross-model tests with deeper temporal, memory, and physics diagnostics.

## Assumption

Interactive world quality is multi-dimensional, and physics/memory scores should be interpreted only when action controllability is adequate.

## Method

Four dimensions: per-frame action following; segment-based visual drift; controllability-gated physics across mechanics/optics/3D consistency; action-decoupled scene and subject memory tests.

## Input/Output

Input: 600+ first/third-person open-world cases with continuous 10-60 second WASD interactions.

Output: action, vision, physics, memory, and overall rankings.

## Evaluation

More than ten open- and closed-source interactive world models across Nature, Urban, and Indoor settings. The paper reports that no model reliably satisfies all dimensions.

## Paper Visual Evidence

No final capture added; Figure 2 is a high-value candidate because it visually separates control, vision, physics, and memory failure modes.

## Contribution Type

- benchmark
- dataset
- analysis

## Limitation

Open-world camera navigation does not fully cover discrete game state, combat, multi-agent intention, rule validity, or reward/task dynamics.

## Primary Research Cluster

Evaluation and Benchmarking

## Secondary Research Clusters

- Real-Time Systems and Long-Horizon Memory
- Structured State and Mechanics Consistency

## Similar Works

- [WorldMark](2026-worldmark.md)

## Contrasting Works

- [DreamerV3](2024-mastering-diverse-domains-through-world-models.md)

## Gap Left

Evaluation that unifies open-world stability with game-specific mechanics and autonomous actors.

## Notes

Its controllability-gated physics design is a useful template: downstream quality claims should not be scored as if intended actions had occurred when they did not.

