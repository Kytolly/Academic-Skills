# Search Strategy

Status: Executed provisionally under user instruction to skip the Seed Set confirmation turn

Based on:

- Field Boundary: `field_boundary.md`
- Seed Papers: `seed_papers/`
- User-provided PDF: ReactiveGWM
- Read-only local Zotero search and locally available PDFs

## Search Directions

| Direction | Why It Matters | Seed Evidence | Expected Paper Types |
| --- | --- | --- | --- |
| Latent dynamics and imagination | Establishes the control-oriented world-model lineage | World Models; DreamerV3 | model / theory / method |
| Pixel-level interactive generation | Explains the move from latent prediction to human-viewable neural game engines | DIAMOND; GameNGen | model / system |
| Foundation interactive worlds | Tests scale, open-domain generalization and prompt/action interfaces | Matrix-Game 3.0; video-world-model survey | model / system / technical report |
| Autonomous actors | Separates environment response from independent NPC or agent intent | ReactiveGWM | model / dataset / evaluation |
| Explicit states and mechanics | Tests whether pixels alone capture valid game rules | StatePlay | model / dataset / benchmark |
| Long-horizon memory and real-time systems | Addresses drift, persistence, throughput and deployment | Matrix-Game 3.0; WorldRoamBench | system / model / benchmark |
| Standardized evaluation | Makes heterogeneous systems comparable | WorldMark; WorldRoamBench | benchmark / dataset / analysis |
| Transferable control mechanisms | Provides adjacent conditioning modules for action, motion, trajectories and camera control | ReactiveGWM Related Work | method / model |

## Selection Criteria

- Directly models future game/world observations from actions or control signals.
- Defines a foundational world-model learning route used by later game systems.
- Introduces a representative interactive game/world generation system.
- Contributes an evaluation protocol for action, visual quality, memory, physics, mechanics, or actor behavior.
- Offers a control mechanism that can plausibly transfer into game world modeling.

## Exclusion Criteria

- Static game asset or level generation without dynamics.
- Pure text-to-video generation without interactive conditioning.
- Pure game-playing agents with no learned transition/world model.
- Robotics or driving world models without a concrete transferable mechanism.
- Duplicate reports or model versions that add no distinct field position.

## Citation Chasing Sources

| Seed Paper | Backward References To Check | Forward Citations To Check | Reason |
| --- | --- | --- | --- |
| ReactiveGWM | DIAMOND, Genie, Oasis, Matrix-Game 2.0/3.0, LingBot-World, GameFactory, GameNGen | Not available in current environment | Direct map of player-centric predecessors and adjacent controls |
| StatePlay | Genie, ReactiveGWM, state/action world-action models | Not available | Identifies mechanics/state-aware branch |
| WorldMark | YUME, HY-World, Matrix-Game, Oasis, MIND, WorldScore | Not available | Identifies cross-model benchmark landscape |
| WorldRoamBench | MIND, iWorld-Bench, WildWorld, WBench, WorldOlympiad | Not available | Identifies long-horizon evaluation landscape |
| GameNGen | World Models, GameGAN, Genie | Not available | Neural game-engine lineage |

## Keyword Queries

| Query | Source | Purpose |
| --- | --- | --- |
| `game world model` | Local Zotero | Direct game-world-model records |
| `interactive world model` | Local Zotero | Long-horizon systems and benchmarks |
| `Diffusion Models Are Real-Time Game Engines` | Local Zotero | Locate GameNGen PDF |
| `Diffusion for World Modeling` | Local Zotero | Locate DIAMOND record |
| `world benchmark` | Local Zotero | Locate WorldMark and WorldRoamBench |
| ReactiveGWM bibliography | User-provided PDF | Backward citation discovery |

## Candidate Pool

| Paper / System | Year | Discovery Source | Why Candidate | Selected? | Reason |
| --- | --- | --- | --- | --- | --- |
| PlaNet | 2019 | ReactiveGWM citation trail | Visual latent planning foundation | Yes | Foundational |
| Dreamer | 2020 | ReactiveGWM citation trail | Latent imagination control | Yes | Foundational |
| MuZero | 2020 | ReactiveGWM citation trail | Planning with learned model | Yes | Contrasting state/value route |
| GameGAN | 2020 | GameNGen lineage | Early neural game simulator | Yes | Game-specific foundation |
| DreamerV2 | 2021 | ReactiveGWM citation trail | Discrete latent Atari world model | Yes | Foundation |
| IRIS | 2022 | World-model lineage | Transformer game world model | Yes | Architecture bridge |
| VideoComposer | 2023 | ReactiveGWM citation trail | Motion-controllable video | Yes | Transferable conditioning |
| Control-A-Video | 2023 | ReactiveGWM citation trail | Controllable video diffusion | Yes | Transferable conditioning |
| Genie | 2024 | ReactiveGWM citation trail | Generative interactive environments | Yes | Foundation model route |
| iVideoGPT | 2024 | Interactive world-model literature | Scalable autoregressive interactive video | Yes | Architecture route |
| Oasis | 2024 | ReactiveGWM citation trail | Transformer-based Minecraft-like interaction | Yes | System/application |
| Genie 2 | 2024 | ReactiveGWM citation trail | Large-scale foundation world model | Yes | System/application |
| MotionCtrl | 2024 | ReactiveGWM citation trail | Camera/object motion control | Yes | Transferable control |
| VBench | 2024 | WorldMark | Video-quality evaluation | Yes | Evaluation boundary |
| WorldScore | 2024/2025 | WorldMark | 3D-aware world consistency | Yes | Evaluation route |
| GameFactory | 2025 | ReactiveGWM citation trail | New-game creation through generative interactive video | Yes | Cross-game generation |
| Genie 3 | 2025 | ReactiveGWM citation trail | Open-ended interactive worlds | Yes | Recent high-impact system |
| PhyGenBench | 2025 | WorldMark | Physical plausibility evaluation | Yes | Evaluation transfer |
| Matrix-Game 2.0 | 2026 | ReactiveGWM citation trail | Open-source real-time streaming world model | Yes | Direct predecessor |
| LingBot-World | 2026 | ReactiveGWM citation trail | Open-source world model | Yes | Direct baseline family |
| YUME 1.5 | 2026 | WorldMark | Caption-controlled world generation | Yes | Control-interface diversity |
| HY-World 1.5 | 2026 | WorldMark | Pose-controlled world generation | Yes | Control-interface diversity |
| SANA-WM | 2026 | WorldRoamBench | Interactive world model benchmarked for long horizon | Yes | Recent system |
| MIND | 2026 | WorldMark / WorldRoamBench | Interactive generation benchmark | Yes | Memory/evaluation |
| iWorld-Bench | 2026 | WorldRoamBench | Interactive world benchmark | Yes | Evaluation |

## Selected Expansion Set

The 25 candidates above form the Selected Expansion Set. Their records are deliberately position-oriented. Items without a local source PDF are marked `Source Verified: Partial` and are not used as sole support for strong claims.

## Why These Papers

The set covers the conceptual transition from latent predictive control to pixel-level neural game engines, foundation-scale interactive video models, diverse action interfaces, explicit actor/state modeling, and the emerging benchmark ecosystem. It also includes adjacent controllable-video methods because current game world models frequently reuse those conditioning and efficiency mechanisms.

## Known Blind Spots

- Network search and forward-citation lookup were blocked by the current environment; the candidate pool is based on local Zotero holdings and backward references.
- Several 2025-2026 systems are technical reports with incomplete public reproducibility.
- Local coverage is stronger for computer-vision/video world models than for Game AI, graphics simulation, or formal game-mechanics research.
- The expansion records for YUME, HY-World, SANA-WM, MIND, and iWorld-Bench are bibliographic positions inferred from verified benchmark papers, not deep readings of their originals.
- Non-English literature, commercial systems without papers, and unpublished evaluation protocols may be underrepresented.

