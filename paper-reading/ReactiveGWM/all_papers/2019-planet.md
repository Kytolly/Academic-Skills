# Learning Latent Dynamics for Planning from Pixels (PlaNet)

Resource: ReactiveGWM Reference [14] / PMLR 2019

Year: 2019

Venue: ICML

Source Verified: Partial

Discovery Source: Citation chasing

## Research Problem

Learn compact visual dynamics that support planning without reconstructing every irrelevant pixel detail.

## Field Position

Latent planning foundation between early World Models and Dreamer.

## Assumption

Planning-relevant dynamics can be represented by a recurrent latent state-space model.

## Method

Latent dynamics learning from pixels with online planning over imagined trajectories.

## Input/Output

Input: images and actions. Output: latent rollouts and planned actions.

## Evaluation

Visual control tasks; task return and sample efficiency.

## Contribution Type

- model
- method

## Limitation

Not designed for photorealistic human-facing game rendering.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Foundations and Taxonomies

## Similar Works

- [Dreamer](2020-dreamer.md)

## Contrasting Works

- [GameNGen](../seed_papers/2024-diffusion-models-are-real-time-game-engines.md)

## Gap Left

Scaling latent planning models toward persistent interactive visual worlds.

