# Mastering Diverse Domains through World Models

Resource: local Zotero PDF; arXiv:2301.04104

Year: 2024

Venue: Nature / DreamerV3

Source Verified: Yes

Discovery Source: Zotero search

## Research Problem

Can one world-model-based reinforcement learning algorithm solve many domains without per-domain tuning?

## Field Position

The strongest control-oriented latent world-model seed. It represents “learn dynamics to improve an agent” rather than “generate a world for a human player.”

## Assumption

Task-relevant future outcomes can be modeled in latent space, and actor-critic learning in imagination transfers to the real environment.

## Method

DreamerV3 learns a recurrent state-space world model, predicts outcomes of candidate actions, and trains actor and critic networks on imagined trajectories. Robust normalization, balancing, and transformations support a single configuration across domains.

## Input/Output

Input: observations, actions, rewards, and continuation signals.

Output: latent dynamics plus actor/critic behavior.

## Evaluation

Over 150 tasks across Atari, ProcGen, DMLab, Minecraft, control suites, and non-visual domains; includes Minecraft diamond collection from pixels and sparse rewards.

## Paper Visual Evidence

No capture added because its benchmark overview is useful for RL breadth but not necessary to explain the game-world-generation clusters.

## Contribution Type

- model
- method
- analysis

## Limitation

Success is measured mainly by agent return, not by human-facing visual realism, controllability, memory, or game-rule fidelity.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Evaluation and Benchmarking

## Similar Works

- [World Models](2018-world-models.md)

## Contrasting Works

- [WorldMark](2026-worldmark.md)

## Gap Left

A unified account of when task-oriented latent prediction is sufficient and when explicit visual/state simulation is necessary.

## Notes

Important boundary paper: it prevents conflating agent-learning world models with interactive video world models.

