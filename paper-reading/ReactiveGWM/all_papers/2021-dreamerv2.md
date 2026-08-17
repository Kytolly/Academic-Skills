# Mastering Atari with Discrete World Models (DreamerV2)

Resource: ReactiveGWM Reference [15]

Year: 2021

Venue: ICLR

Source Verified: Partial

Discovery Source: Citation chasing

## Research Problem

Can discrete latent dynamics support strong Atari control through imagination?

## Field Position

Discrete-representation extension of Dreamer and an important bridge to tokenized world models.

## Assumption

Categorical latent variables better capture multimodal visual dynamics for Atari.

## Method

Discrete recurrent state-space model plus actor-critic learning on imagined trajectories.

## Input/Output

Input: Atari observations/actions/rewards. Output: discrete latent rollouts and policy.

## Evaluation

Atari agent performance and data efficiency.

## Contribution Type

- model
- method

## Limitation

Agent-return evaluation does not measure interactive rendering quality or world persistence.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Pixel-Level Generative Simulation

## Similar Works

- [Dreamer](2020-dreamer.md)
- [IRIS](2022-iris.md)

## Contrasting Works

- [ReactiveGWM](../seed_papers/2026-reactivegwm.md)

## Gap Left

Relating discrete task latents to controllable high-resolution video generation.

