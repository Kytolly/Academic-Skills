# Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero)

Resource: ReactiveGWM Reference [28]

Year: 2020

Venue: Nature

Source Verified: Partial

Discovery Source: Citation chasing

## Research Problem

Can planning succeed with a learned model that predicts only quantities necessary for decision-making rather than reconstructing observations?

## Field Position

Contrasting task-centric world-model route based on reward, value, and policy prediction.

## Assumption

Decision-equivalent latent dynamics can omit full environment reconstruction.

## Method

Learn representation, dynamics, and prediction functions integrated with tree search.

## Input/Output

Input: histories and actions. Output: latent transitions, reward/value/policy and planned action.

## Evaluation

Atari and board-game performance.

## Contribution Type

- model
- method

## Limitation

Not a visual simulator and therefore unsuitable as a direct human-playable world model.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Foundations and Taxonomies

## Similar Works

- [Dreamer](2020-dreamer.md)

## Contrasting Works

- [GameNGen](../seed_papers/2024-diffusion-models-are-real-time-game-engines.md)

## Gap Left

Understanding which semantics must be explicitly rendered or retained for interactive human use.

