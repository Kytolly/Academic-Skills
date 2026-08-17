# World Models

Resource: https://arxiv.org/abs/1803.10122

Year: 2018

Venue: arXiv / foundational work

Source Verified: Partial (local Zotero bibliographic record; cited by ReactiveGWM)

Discovery Source: Zotero search and citation chasing

## Research Problem

Can an agent learn a compact internal model of an environment and use imagined rollouts to learn behavior with limited direct interaction?

## Field Position

Foundational latent-dynamics route. It defines the conceptual lineage from compact predictive state representations to later action-conditioned game simulators.

## Assumption

A compressed visual latent and recurrent transition model retain enough task-relevant dynamics for control.

## Method

VAE compresses frames; an MDN-RNN predicts latent transitions; a lightweight controller acts using the learned internal model.

## Input/Output

Input: observations and actions.

Output: predicted latent transitions and a policy/controller.

## Evaluation

Game-control tasks and agent performance in learned/imaginative environments.

## Paper Visual Evidence

No capture added because the original PDF was not available as a verified local attachment during this run.

## Contribution Type

- model
- method
- theory

## Limitation

Low-dimensional latent prediction and small environments do not directly solve high-fidelity, real-time visual world generation.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Foundations and Taxonomies

## Similar Works

- [DreamerV3](2024-mastering-diverse-domains-through-world-models.md)

## Contrasting Works

- [GameNGen](2024-diffusion-models-are-real-time-game-engines.md)

## Gap Left

How to scale learned dynamics from compact task latents to visually rich, persistent, user-facing worlds.

## Notes

The main relevance is conceptual: prediction and imagination, not pixel-perfect game rendering.

