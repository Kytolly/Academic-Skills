# VideoComposer: Compositional Video Synthesis with Motion Controllability

Resource: ReactiveGWM Reference [36]

Year: 2023

Venue: NeurIPS

Source Verified: Partial

Discovery Source: ReactiveGWM citation chasing

## Research Problem

How can multiple spatial and temporal conditions be composed for controllable video generation?

## Field Position

Adjacent controllable-video method providing reusable conditioning ideas rather than a complete world model.

## Assumption

Motion, appearance, text, depth, sketch, and other conditions can share a compositional generative backbone.

## Method

Conditional video diffusion with compositional motion controls.

## Input/Output

Input: text and auxiliary motion/structure conditions. Output: controlled video.

## Evaluation

Video quality and condition alignment.

## Contribution Type

- model
- method

## Limitation

Open-loop clips do not establish causal action-conditioned simulation or persistent state.

## Primary Research Cluster

Transferable Control Mechanisms

## Secondary Research Clusters

- Pixel-Level Generative Simulation

## Similar Works

- [Control-A-Video](2023-control-a-video.md)
- [MotionCtrl](2024-motionctrl.md)

## Contrasting Works

- [ReactiveGWM](../seed_papers/2026-reactivegwm.md)

## Gap Left

Converting compositional controls into closed-loop game actions and actor intentions.

