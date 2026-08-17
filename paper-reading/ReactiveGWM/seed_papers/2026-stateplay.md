# StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation

Resource: local Zotero PDF; https://jimntu.github.io/stateplay_page/; arXiv:2607.26754

Year: 2026

Venue: arXiv preprint

Source Verified: Yes

Discovery Source: Zotero search

## Research Problem

Pixel-level game world models may look plausible while violating health, skill-meter, timer, attack-validity, and termination rules. Can explicit game-state prediction improve mechanics consistency?

## Field Position

Defines the state-aware/mechanics-consistent branch and exposes the limitation of treating a playable game as pixels plus actions alone.

## Assumption

Internal game state cannot always be reliably recovered through pixel supervision, but synchronized state-frame-action data can make rules learnable.

## Method

A mixture-of-transformers-style architecture maintains specialized visual and state branches while allowing cross-modal interaction. Modality-specific objectives jointly predict frames and states so predicted states guide mechanics-consistent generation.

## Input/Output

Input: gameplay frames, player actions, and state variables such as health, skill meter, and timer.

Output: future visual frames and predicted game-state trajectories.

## Evaluation

SF3 synchronized state-frame-action dataset; normalized L1 below 0.06 for state prediction; reported 18.6% improvement in mechanics fidelity while maintaining visual quality and controllability.

## Paper Visual Evidence

No final capture added yet; Figure 1 and Figure 2 are high-value candidates for a future visual-evidence update.

## Contribution Type

- model
- dataset
- method

## Limitation

Requires privileged or extractable game-state annotations and is evaluated on one fighting-game setting.

## Primary Research Cluster

Structured State and Mechanics Consistency

## Secondary Research Clusters

- Pixel-Level Generative Simulation
- Evaluation and Benchmarking

## Similar Works

- [ReactiveGWM](2026-reactivegwm.md)

## Contrasting Works

- [GameNGen](2024-diffusion-models-are-real-time-game-engines.md)

## Gap Left

Learning portable state schemas and game rules without privileged engine access, and combining state mechanics with autonomous actor intent.

## Notes

StatePlay and ReactiveGWM address complementary omissions: internal mechanics versus autonomous NPC intent.

