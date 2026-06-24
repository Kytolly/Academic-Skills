# Paper Reading Skills

语言：[English](README.md) | 简体中文

> 一个面向研究过程的 Codex skill 套件，把论文阅读转化为结构化的研究决策。

Paper Reading Skills 是一组面向科研早期阶段的 Codex skills。它的目标不是孤立地总结论文，而是帮助研究者在不同研究阶段中，围绕明确的阅读动机组织论文阅读，并把阅读结果沉淀为可以继续推进研究的持久产物。

很多低效阅读并不是因为论文太难，而是因为开始阅读前没有说清楚：

* 我为什么要读这些论文？
* 我现在要解决哪个研究决策？
* 我应该重点关注论文的哪些部分？
* 这次阅读最后应该产出什么？
* 读到什么程度就可以停止？

本项目把论文阅读拆成一组常见研究动作，并为每个动作设计对应的 workflow、输入边界、阅读策略、产出格式和停止条件。

---

## 核心想法

普通论文阅读通常以“读完论文”为目标，而本项目以“完成研究判断”为目标。

例如：

* 刚进入一个方向时，不应该急着总结论文，而应该先建立 field map。
* 有了初步 idea 时，不应该马上设计方法，而应该先做 problem reality check。
* 方法有雏形后，不应该让 AI 直接写成最终方案，而应该经过 method commitment。
* 准备写论文时，不应该泛泛找 related work，而应该围绕 close work、claim support 和 positioning 来组织表达。

因此，每个 skill 都对应一个具体研究阶段，并产出可以继续被下游 workflow 使用的 artifacts。

---

## Skill Map

| 阶段 | Skill | 它帮助回答的研究问题 | 主要产出 |
| ---- | ----- | -------------------- | -------- |
| 01 | Field Map | 这个领域有哪些主要分支、方法路线和研究机会？ | 领域图谱 / 研究簇 / 研究机会候选 |
| 02 | Research Question | 哪些 gap 可以变成可执行的研究问题？ | 研究问题卡片 |
| 03 | Problem Reality Check | 这个问题是真问题，还是只是看起来合理？ | 问题论证 / 风险记录 |
| 04 | Theoretical Grounding | 这个问题背后有没有可以支撑 framing 的理论依据？ | 理论 grounding 包 |
| 05 | Method Inspiration | 有哪些论文机制可以迁移成候选方法？ | 方法候选库 |
| 06 | Method Commitment | 当前方法是否足够稳定，能否被研究者认领？ | committed / provisional / redesign / rejected 方法结果 |
| 07 | Experiment Design | 如何把 claim 转化为可验证的实验设计？ | 实验计划 / baseline pressure matrix / claim-metric map |
| 08 | Research Framing | 如何把当前研究放入论文叙事和相关工作比较中？ | 研究 framing 包 |
| Extra | Workspace Presentation | 如何把已有研究 workspace 变成可浏览、可交接的界面？ | 交互式 presentation workspace |

---

## Workflow

这些 skills 被设计成一条研究管线：

```text
Field Map
  |
  v
Research Question
  |
  v
Problem Reality Check
  |
  v
Theoretical Grounding
  |
  v
Method Inspiration
  |
  v
Method Commitment
  |
  v
Experiment Design
  |
  v
Research Framing
  |
  v
Workspace Presentation
```

这条管线并不是严格线性的。用户可以根据当前研究状态，从任意阶段开始。

例如：

* 如果用户刚进入一个领域，可以从 `01-field-map` 开始。
* 如果用户已经有一个 idea，但不确定它是否成立，可以从 `03-problem-reality-check` 开始。
* 如果用户有多个候选方法，可以从 `06-method-commitment` 开始。
* 如果用户已经有稳定方法，并希望设计实验，可以从 `07-experiment-design` 开始。

---

## 使用示例

### 1. 进入一个新的研究方向

用户目标：

> I want to understand LLM agent evaluation, but I do not know the main branches yet.

推荐 skill：

```text
01-field-map
```

预期产出：

* field boundary
* seed paper set
* paper position records
* research clusters
* opportunity candidates
* static HTML field report

---

### 2. 把模糊 gap 转化为研究问题

用户目标：

> I found several gaps in related work, but I do not know which one is worth pursuing.

推荐 skill：

```text
02-research-question
```

预期产出：

* candidate research questions
* motivation notes
* feasibility risks
* evidence requirements
* recommended next step

---

### 3. 压力测试一个研究 idea

用户目标：

> I have an idea, but I am worried the problem may already be solved or not important enough.

推荐 skill：

```text
03-problem-reality-check
```

预期产出：

* problem existence check
* evidence support
* prior-solution risk
* motivation safety notes
* recommended reframing or stop condition

---

### 4. 收敛到一个方法

用户目标：

> I have several candidate methods and want to decide what my final method should be.

推荐 skill：

```text
06-method-commitment
```

预期产出：

* source method
* method reconstruction
* challenge questions
* decision log
* method commitment status
* downstream routing suggestion

---

## 如何使用

克隆仓库：

```bash
git clone https://github.com/snake-fan/Paper-Reading-Skills.git
cd Paper-Reading-Skills
```

每个编号目录都包含一个 Codex skill：

```text
01-field-map/
02-research-question/
03-problem-reality-check/
04-theoretical-grounding/
05-method-inspiration/
06-method-commitment/
07-experiment-design/
08-research-framing/
workspace-presentation/
```

使用 skill 之前，先判断当前研究状态：

```text
I am currently trying to:
- understand a field
- find a research question
- verify whether a problem is real
- find theoretical support
- get method inspiration
- commit to a method
- design experiments
- frame the paper
```

然后在 Codex 中调用对应 skill。

示例 prompt：

```text
Use the field-map skill to help me map the research field of memory safety in LLM agents.
I want to identify major branches, representative papers, evaluation settings, saturated areas, and possible research opportunities.
```

---

## 产出理念

每个 skill 都旨在产出持久的研究 artifacts，而不是临时聊天总结。

这些产出应该是：

* 可追溯：重要 claims 应该能连接回论文或上游 artifacts。
* 面向决策：每个 artifact 都应该帮助用户完成一个研究判断。
* 可复用：下游 skills 应该能够消费上游产出。
* 有边界：每个 workflow 都应该有清晰的停止条件。
* 诚实面对不确定性：薄弱证据、未解决风险和不安全 claims 都应该被明确记录。

---

## 设计原则

### 1. 动机优先的阅读

本项目假设论文阅读应该从用户当前的研究动机开始，而不是从通用总结模板开始。

### 2. Artifact 驱动的 workflow

每个 skill 都会写出结构化 artifacts，避免研究进展消失在聊天历史中。

### 3. 人类拥有关键决策

Agent 可以提出、组织、质疑和总结，但重要的研究承诺应该始终对用户可见，并由用户认领。

### 4. 下游路由纪律

不是所有产出都应该进入下游。例如，薄弱问题不应该自动进入方法设计，provisional method 也不应该被当成 experiment-ready method。

### 5. 证据敏感的 framing

本项目避免把弱证据包装成强 claim。它会记录哪些内容可以安全表达，哪些还需要更多支持，以及哪些说法应该避免。

---

## 仓库结构

```text
.
├── README.md
├── README.zh-CN.md
├── 01-field-map/
│   └── SKILL.md
├── 02-research-question/
│   └── SKILL.md
├── 03-problem-reality-check/
│   └── SKILL.md
├── 04-theoretical-grounding/
│   └── SKILL.md
├── 05-method-inspiration/
│   └── SKILL.md
├── 06-method-commitment/
│   └── SKILL.md
├── 07-experiment-design/
│   └── SKILL.md
├── 08-research-framing/
│   └── SKILL.md
└── workspace-presentation/
    ├── SKILL.md
    ├── references/
    └── templates/
```

---

## 当前状态

已完成：

* core skill structure
* field map workflow
* research question workflow
* problem reality check workflow
* theoretical grounding workflow
* method inspiration workflow
* method commitment workflow
* experiment design workflow
* research framing workflow
* workspace presentation workflow

进行中：

* improving cross-skill artifact compatibility
* refining workflow gates and status routing
* adding more example workspaces
* improving presentation templates
