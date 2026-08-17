# Dream to Control: Learning Behaviors by Latent Imagination

Resource: ReactiveGWM Reference [13]

Year: 2020

Venue: ICLR

Source Verified: Partial

Discovery Source: Citation chasing

## Research Problem

How can behavior be learned efficiently inside a differentiable latent world model?

## Field Position

Canonical latent-imagination actor-critic route.

## Assumption

Latent imagined trajectories preserve reward- and control-relevant information.

## Method

Learn latent dynamics, then optimize actor and value models over imagined rollouts.

## Input/Output

Input: observations, actions, rewards. Output: latent model and policy.

## Evaluation

Visual control and sample efficiency.

## Contribution Type

- model
- method

## Limitation

Optimizes agent performance rather than world realism or human interactivity.

## Primary Research Cluster

Latent Dynamics and Imagination-Based Control

## Secondary Research Clusters

- Foundations and Taxonomies

## Similar Works

- [PlaNet](2019-planet.md)
- [DreamerV2](2021-dreamerv2.md)

## Contrasting Works

- [WorldMark](../seed_papers/2026-worldmark.md)

## Gap Left

Human-facing evaluation and explicit actor/mechanics semantics.

