# Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

Resource: local Zotero PDF; arXiv:2604.08995

Year: 2026

Venue: Technical report

Source Verified: Yes

Discovery Source: Zotero search and ReactiveGWM citation chasing

## Research Problem

How can an interactive video world model jointly achieve high-resolution real-time generation and minute-long spatial-temporal consistency?

## Field Position

Represents the system-scaling branch: data engine, long-horizon memory, streaming autoregression, distillation, quantization, and real-time deployment.

## Assumption

Large-scale heterogeneous video-pose-action-prompt data plus explicit memory retrieval can reduce drift and support persistent interactive environments.

## Method

- Industrial-scale synthetic, AAA-game, and augmented real-video data engine.
- Residual modeling and re-injection of imperfect generated frames for self-correction.
- Camera-aware memory retrieval and injection.
- Multi-segment autoregressive DMD distillation, quantization, and VAE pruning.

## Input/Output

Input: video context, camera pose/action, prompt, and retrieved memory.

Output: streaming 720p interactive video.

## Evaluation

Reported up to 40 FPS with a 5B model and stable memory consistency over minute-long sequences; larger 2x14B configuration improves quality, dynamics, and generalization.

## Paper Visual Evidence

No final capture added; Figure 1 is a candidate for the system architecture and memory route.

## Contribution Type

- model
- system
- dataset

## Limitation

System scale and data dependence make reproducibility expensive; evaluation focuses on camera/action-conditioned worlds rather than independent NPC intent or explicit mechanics.

## Primary Research Cluster

Real-Time Systems and Long-Horizon Memory

## Secondary Research Clusters

- Pixel-Level Generative Simulation
- Transfer and Generalization

## Similar Works

- [GameNGen](2024-diffusion-models-are-real-time-game-engines.md)

## Contrasting Works

- [ReactiveGWM](2026-reactivegwm.md)
- [StatePlay](2026-stateplay.md)

## Gap Left

Persistent entity/state semantics, affordable training, causal interaction, and controllable autonomous agents inside the long-horizon world.

## Notes

This paper is a strong systems comparator but not a direct NPC autonomy baseline.

