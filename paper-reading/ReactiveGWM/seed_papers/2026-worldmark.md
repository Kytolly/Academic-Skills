# WorldMark: A Unified Benchmark Suite for Interactive Video World Models

Resource: local Zotero PDF; https://alaya-studio.github.io/WorldMark/; arXiv:2604.21686

Year: 2026

Venue: arXiv preprint / benchmark

Source Verified: Yes

Discovery Source: Zotero search

## Research Problem

Models use private scenes, trajectories, and control interfaces, so their reported metrics are not comparable. How can interactive image-to-video world models be tested on a common playing field?

## Field Position

Standardized cross-model evaluation branch. It focuses on comparability rather than proposing a generator.

## Assumption

Semantically equivalent action commands can be mapped into heterogeneous native control formats well enough for fair comparison.

## Method

A shared WASD-style action vocabulary, model-specific action mapping, 500 cases across perspectives/styles/difficulty, and modular metrics for visual quality, control alignment, and world consistency.

## Input/Output

Input: standardized reference images and action sequences translated to each model's interface.

Output: comparable model rollouts and evaluation scores.

## Evaluation

Six major interactive video world models; 20-60 second tests across first/third person and photorealistic/stylized scenes; online pairwise World Model Arena.

## Paper Visual Evidence

No final capture added; Figure 1 is a candidate for explaining standardized action mapping.

## Contribution Type

- benchmark
- dataset
- analysis

## Limitation

Shared action semantics do not guarantee identical low-level physical meaning; NPC strategy, game rules, and task-specific mechanics remain outside the core protocol.

## Primary Research Cluster

Evaluation and Benchmarking

## Secondary Research Clusters

- Real-Time Systems and Long-Horizon Memory

## Similar Works

- [WorldRoamBench](2026-worldroambench.md)

## Contrasting Works

- [ReactiveGWM](2026-reactivegwm.md)

## Gap Left

A benchmark spanning player action, NPC intent, explicit game mechanics, entity identity, and long-horizon causal outcomes in the same protocol.

## Notes

WorldMark identifies standardized test conditions, not only better metrics, as the central evaluation bottleneck.

