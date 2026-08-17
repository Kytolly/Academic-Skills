# Field Boundary

Status: Confirmed

Workspace: `paper-reading/ReactiveGWM/`

## Research Target

研究游戏世界模型如何从玩家视角预测或生成可交互游戏环境，并进一步支持玩家动作控制、NPC 自主行为、玩家-NPC 动态交互、游戏机制一致性、长时序稳定性和跨游戏泛化。

## In Scope

- 基于视频生成、扩散模型、Transformer 或混合架构的游戏世界模型。
- action-conditioned 与 controllable game world models。
- NPC autonomy、reactive NPC、multi-agent interaction 与策略控制。
- 玩家控制和 NPC 行为的解耦表示与条件注入。
- 显式游戏状态、规则和机制一致性。
- 长时序记忆、实时推理和流式生成。
- 基于模拟器、游戏录像、合成数据或自动标注的数据构建。
- 跨游戏、跨场景、跨角色的迁移和泛化。
- 视觉质量、动作跟随、策略遵循、交互物理、记忆与机制一致性评估。

## Out of Scope

- 不使用世界模型的传统 NPC 路径规划或纯策略强化学习。
- 与动态模拟无关的静态资产、地图或关卡生成。
- 只优化画质、没有动作或状态转移条件的视频生成。
- 与游戏世界模型没有直接方法联系的机器人和自动驾驶世界模型。
- 只学习游戏代理策略、但不学习环境预测或交互模拟的工作。

## Time / Venue Boundary

重点覆盖 2020-2026 年，必要时回溯 2018-2019 年的基础世界模型工作。允许 CV、ML、Game AI、Graphics、Agents 和 Interactive Simulation 社区的会议论文、期刊论文、arXiv 预印本、公开技术报告、项目页、数据集与 benchmark 论文。

## User Goal

建立可迁移的研究笔记，理解游戏世界模型的主要分支、方法路线、数据与评估方式，定位 ReactiveGWM，并形成有论文证据支持的研究机会。

## Stop Condition

- 能解释主要研究集群和方法路线。
- 每个集群有代表论文及其假设、输入输出和评估模式。
- 能区分像素生成、动作控制、NPC 自主性、状态/机制建模、长时序记忆和评估标准化。
- 能说明 ReactiveGWM 的位置、贡献、局限及其相邻研究方向。
- 形成可继续转化为 Research Question Cards 的研究机会候选。

## Boundary Rationale

该边界以“可交互的生成式游戏模拟器”为核心，同时保留传统潜变量世界模型作为理论与方法基础。它排除仅做静态内容生成或纯代理控制的工作，以避免把世界建模、游戏生成和游戏 AI 混成同一领域。

## Revision Log

| Version | Change | Reason |
| --- | --- | --- |
| v1 | 初始边界 | 由 Agent 提议 |
| v2 | 确认完整游戏世界模型范围，并以 ReactiveGWM 为入口 | 用户确认 |

