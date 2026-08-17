# Diffusion Models Are Real-Time Game Engines (GameNGen)

Resource: local Zotero PDF; https://gamengen.github.io

Year: 2024

Venue: arXiv:2408.14837 (local Zotero record dated 2025)

Source Verified: Yes

Discovery Source: Zotero search and ReactiveGWM Reference [34]

## Research Problem

Can a neural generative model replace the manually coded update-and-render loop of a complex game while remaining playable in real time?

## Field Position

Foundational real-time diffusion game-engine route. It establishes high-fidelity action-conditioned DOOM simulation as a viable system target.

## Assumption

Gameplay trajectories collected from an RL agent cover enough state-action transitions to train an autoregressive diffusion simulator.

## Method

Two stages: train an RL agent and record gameplay; train an augmented Stable Diffusion model to predict the next frame from prior frames and actions. Conditioning augmentation reduces autoregressive drift.

## Input/Output

Input: recent game frames and a stream of player actions.

Output: the next rendered frame, autoregressively repeated at interactive speed.

## Evaluation

DOOM simulation at approximately 20 FPS, PSNR 29.4, human distinguishability for short clips, and qualitative long-trajectory behavior.

## Paper Visual Evidence

No final capture added in this run; its Figure 1 is a system demonstration rather than the clearest evidence for ReactiveGWM's research question.

## Contribution Type

- model
- system

## Limitation

Single-game training, player-centric control, expensive data generation, and limited explicit representation of state, rules, NPC intent, or reusable interaction logic.

## Primary Research Cluster

Pixel-Level Generative Simulation

## Secondary Research Clusters

- Real-Time Systems and Long-Horizon Memory

## Similar Works

- [Diffusion for World Modeling](2024-diffusion-for-world-modeling.md)
- [Matrix-Game 3.0](2026-matrix-game-3.md)

## Contrasting Works

- [ReactiveGWM](2026-reactivegwm.md)
- [StatePlay](2026-stateplay.md)

## Gap Left

How to represent autonomous actors and game mechanics rather than learn them only as pixel-transition regularities.

## Notes

The paper explicitly distinguishes interactive world simulation from ordinary video generation.

