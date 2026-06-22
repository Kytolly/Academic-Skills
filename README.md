# Paper Reading Skills

这是一组辅助论文阅读的 Codex skills。核心目标不是“把每篇论文都读完”，而是在阅读开始前先识别当前阅读动机，再根据动机选择合适的阅读策略、关注点和产出格式。

很多低效阅读来自一个隐蔽问题：开始读之前并没有说清楚自己要从论文里拿到什么。这个项目把论文阅读拆成一组常见动机，让每次阅读都能先回答：

- 我现在为什么读这篇论文？
- 我应该重点看哪些部分？
- 我这次阅读应该产出什么？
- 读到什么程度就可以停？

## 项目结构

```text
.
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
└── 09-risk-objection/
    └── SKILL.md
```

## 使用方式

阅读开始前，先用一两个问题明确当前阅读动机，再直接选择对应编号的动机 skill。若动机还不清楚，可以先对照下方“阅读动机”表格判断：这次阅读最需要产出什么，以及读到什么程度就可以停。

后续每个动机 skill 会逐步补充：

- 适用场景
- 阅读前提问
- 阅读顺序
- 重点关注章节
- 信息抽取模板
- 产出格式
- 停止条件

## 阅读动机

| 编号 | 动机 | 典型产出 | 适用阶段 |
| --- | --- | --- | --- |
| 01 | 了解领域全貌 | 领域研究地图 | 刚进入方向，问题还没定 |
| 02 | 寻找研究问题 | 候选研究问题列表 | 已知道领域大概情况，但不知道切哪里 |
| 03 | 验证问题是否真实 | 问题依据 / problem justification | 有初步 idea，但担心是伪问题 |
| 04 | 寻找理论依据 | 理论支柱 | 问题已有，但需要理论地基 |
| 05 | 寻找方法启发 | 方法候选库 | 问题初步确定，正在设计方法 |
| 06 | 确定方法设计 | method commitment outcome | 方法启发之后，研究者准备认领、稳定或阻断自己的方法 |
| 07 | 寻找实验设计 | experiment plan / baseline pressure matrix / claim-metric map | 方法基本确定，需要证明 claim、选择 baseline 和指标 |
| 08 | 形成论文表达 / 研究定位 / 引用支撑 | research framing package | 问题、方法或实验主张稳定，准备写 introduction、related work、proposal 或 paper |
| 09 | 排雷和反驳自己 | risk list / objection list | idea 成型前后，尤其是过于兴奋时 |

## 核心使用场景

这个项目面向的不是“帮我总结几篇论文”这种一次性需求，而是研究早期最容易卡住的几个真实场景：刚进方向时不知道读什么，读了一批论文后不知道题目切哪里，有了 idea 又担心问题是伪问题，写 proposal 或论文时还缺少理论地基。

普通做法往往是先攒论文、做摘要、画表格，然后指望读到一定数量后自然产生判断。这个项目的思路相反：先明确当前研究动作要解决什么决策，再组织阅读。每个 skill 都对应一个具体场景，目标是让阅读产出可以直接服务下一步研究判断，而不是停留在“我好像理解了”的模糊状态。

### 01 了解领域全貌：从论文清单变成领域地图

适用场景：你刚进入一个方向，只知道一个大概关键词，比如“LLM agent evaluation”或“RAG hallucination”，但还不知道这个领域有哪些分支、代表工作、常用方法、评测套路和未解决问题。

常见做法是让 AI 或搜索引擎给一批“必读论文”，然后按顺序读摘要。问题是，这样很容易得到一堆互相并列的论文摘要，却不知道它们之间是什么关系：哪些是奠基工作，哪些只是应用变体，哪些定义了 benchmark，哪些代表一个已经拥挤的路线。

这里的产品设计是把“找论文”升级成“建地图”。用户先和 agent 一起圈定当前要看的边界，再用一组覆盖面足够广的论文建立领域坐标。阅读时关注的也不是复述论文内容，而是判断每篇论文在领域里的位置：它解决什么问题，依赖什么假设，采用哪条方法路线，怎么评价，留下什么空白。

这样做的优势是，读完后用户得到的不是一堆摘要，而是一张可以用来做决策的领域地图：哪些方向已经饱和，哪些地方证据薄，哪些 gap 可能变成研究机会。它特别适合选题前期、开题准备、related work 前置调研，以及进入一个陌生方向时快速建立判断力。

### 02 寻找研究问题：从“有 gap”到“可执行的问题”

适用场景：你已经大概知道一个领域，也看到了一些 gap，但不知道哪个 gap 值得变成自己的研究问题。这个阶段最痛苦的地方通常不是没有想法，而是想法太多：有的更容易做实验，有的更新颖，有的更适合系统论文，有的更贴近长期方向。

常见做法是直接让 AI brainstorm 研究问题，或者从 related work 的 future work 里挑一句。这样的问题看起来很顺，但经常缺少三个东西：它和已有文献的真实关系、它与用户目标的匹配程度、以及它能不能被实验或研究设计真正落地。

这里的产品设计是把“选题”做成一个比较过程。它不直接宣布某个题目最好，而是先帮助用户说清楚当前写作意图：是想稳妥地产出实验结果，还是追求新颖性，是偏系统构建，还是偏高水平 venue 的问题包装。然后再把领域地图里的研究机会切成多个候选角度，让用户比较每个角度适合什么、牺牲什么、主要风险是什么。

这样做的优势是，研究问题不再是灵感产物，而是一个经过取舍的选择结果。用户最后拿到的不是一句 question，而是一张可以继续推进的问题卡：它说明为什么重要、证据来自哪里、可能怎么验证、风险在哪里、什么条件下才值得继续投入。这比普通 brainstorm 更慢一点，但更适合真正要写 proposal、做实验或推进论文的人。

### 03 验证问题是否真实：在投入方法设计前先拷问动机

适用场景：你已经有一个初步 research question，甚至已经开始想方法了，但心里不确定这个问题是不是真的成立：用户或系统里是否真的存在这个痛点，已有工作是否已经解决，引用是否真的支持你的动机，问题范围会不会太大。

常见做法是带着兴奋感继续往方法上冲，等写 introduction 或被导师、reviewer 追问时才发现动机站不稳。另一个常见做法是泛泛地做 risk list，但风险没有和具体论证句子绑定，最后也不知道哪些话能写、哪些话不能写。

这里的产品设计是把问题动机当成一个需要被审问的对象。它会模拟一个挑剔读者会问的问题：这个问题真的存在吗？有没有真实场景支撑？引用是不是只支持了较弱的说法？现有工作是否已经覆盖？你的动机表述有没有过度泛化？目标用户或应用场景是否清楚？

这样做的优势是，用户可以在投入方法、实验和写作之前，先得到一个更诚实的判断：这个问题可以继续推进，还是需要补证据、缩小范围、换一种说法，甚至暂时放弃。它尤其适合 idea 成型早期、proposal 动机段落写作前、和导师讨论前，以及任何“我觉得这个问题很重要，但不知道别人会不会买账”的时刻。

### 04 寻找理论依据：让理论支撑论证，而不是装饰引用

适用场景：你的问题已经比较稳定，也确认它不是明显的伪问题，但写作时还缺少更深的解释框架。你不只是想说“这个现象存在”，还想说明为什么它值得被这样理解，哪些概念关系能支撑你的 framing。

常见做法是搜索几个听起来相关的理论名词，然后把它们放进 introduction 或 related work。这样做的问题是，理论很容易变成装饰：看起来高级，但没有真正支撑论文里的关键判断，也说不清它能支持什么、不能支持什么。

这里的产品设计是先从研究问题本身出发，找出哪些判断真的需要理论支持。比如，是要解释某种失败为什么会发生，还是要说明某类行为为什么会影响信任、决策或长期效果。只有先确定这些需要支撑的判断，再去寻找合适的理论传统，理论才不会变成泛泛的背景知识。

这样做的优势是，理论最终服务于论文论证。用户得到的不是一串理论名字，而是更清楚的问题 framing：哪些 claim 有理论支柱，哪些 claim 只能谨慎表述，哪些经验问题不能靠理论替代证据。它适合写 proposal、introduction、theoretical framing，也适合在一个偏经验的问题需要提升概念深度时使用。

### 05 寻找方法启发：从论文方法变成候选方法库

适用场景：你的研究问题已经有了初步边界，甚至已经知道大概要干预哪个失败环节，但还不知道方法应该长什么样。这个阶段的核心需求不是马上发明一个完整方法，而是从论文里收集可迁移的机制、模块、训练流程、推理流程、数据构造方式或优化目标。

常见做法是直接搜索“相关方法”，然后把几篇论文的 architecture 拼在一起。问题是，这样很容易把论文里的完整方法当成可以直接搬走的答案，也容易忽略自己的问题到底需要哪些能力：有些模块看起来高级，但并不对应当前问题的关键失败；有些方法来自相邻问题，真正可迁移的其实只是其中一个很小的机制。

这里的产品设计是把“找方法”拆成三步。第一步先从 source research question 或 source problem brief 里拆出 Method Needs，明确方法需要解决什么失败、在什么 intervention point 起作用、输入输出是什么、成功信号是什么。第二步再围绕这些 needs 做 targeted method search，从 same-problem、adjacent-problem 和 far-analogy papers 中提取 Method Patterns。第三步才把通过 transfer mapping 的 patterns 组合成 3-5 个 Candidate Methods，并记录它们覆盖了哪些 needs、弱点在哪里、哪些地方仍然只是 provisional。

这样做的优势是，方法启发不会变成随手拼装。用户最后拿到的是一个可审计的 Method Candidate Library，而不是一个被过早宣布为“最终方法”的 architecture。它保留了论文启发的来源、迁移边界、可用和不可用的部分，也为后续 method commitment、experiment design、research framing 和 risk objection 留出清楚的入口。

### 06 确定方法设计：从候选灵感变成研究者认领的方法

适用场景：你已经有了一个比较像方法的东西：可能是 method inspiration 里选出的一个 Candidate Method，可能是几个候选方法的混合，也可能是你自己在聊天或笔记里写出的 rough method。现在的问题不再是“还能参考什么”，而是这个方法是否足够稳定，能不能被你作为论文里的核心方法认领，并进入实验设计、research framing 或风险排雷阶段。

常见做法是让 AI 从候选方案里“综合一个最终方法”，然后顺手写成 method section 的口吻。这样看起来推进很快，但风险很大：方法的 source 不清楚，哪些部分是借来的、哪些部分是自己主张的说不清，mechanistic claim 也没有被攻击过。更麻烦的是，用户可能还没有真正承诺这个方法，后续实验却已经默认它是最终设计。

这里的产品设计是把“确定方法”做成一个收敛和承诺流程。它先把输入规范成 exactly one Source Method，并绑定到 exactly one Method Commitment Source Problem；然后回看已有的本地 artifacts，包括 problem reality check、method needs、method patterns、transfer mapping 和 candidate methods，保留上游已经暴露的脆弱点。之后再重建方法 anatomy，明确 Method Thesis、Mechanistic Claim、核心机制、模块、输入输出、训练或推理流程、novelty boundary、assumptions、weakest link 和 downstream pressure points。

这样做的优势是，方法不是被 agent 偷偷“定稿”，而是经过攻击和确认后成为研究者拥有的设计。高风险维度会用 challenge questions 逐个追问，结构性决定会写进 decision log，最后只会得到一种明确状态：committed、provisionally-committed、needs-redesign 或 reject-current-method。只有真正 committed 的方法才适合进入后续实验设计和写作链路；其他状态会明确记录 blocker、重设计方向或拒绝理由，避免把不稳定的方法继续往下游传。

### 07 寻找实验设计：把 claim 变成可验证的证据链

适用场景：方法已经有雏形，最好已经经过 method commitment，但还不知道应该用什么任务、数据、baseline、metric、ablation 或 human evaluation 来证明它。这个阶段的核心不是单独找一串 baseline 或指标，而是把每个关键 claim 映射到可观察证据。

常见做法是先列几个热门 benchmark，再补几个常见指标。问题是，这样很容易得到一套看起来完整但不能真正回答 mechanistic claim 的实验：baseline 不知道在压力测试什么，metric 也不知道对应哪个论证句子。

这里的产品设计是把找 baseline 和找指标合并进 experiment design。它先拆出 claim-evidence map，再选择 task/dataset，写 baseline pressure matrix 和 claim-metric map，最后补上 ablation、control 和 failure interpretation。用户最后拿到的是一条实验论证链：这个 claim 用哪个 setting 测、和谁比、看什么指标、什么结果算支持、什么失败说明方法哪里不成立。

### 08 形成论文表达：把当前研究放进相似工作的比较框架里

适用场景：你的问题、方法或实验主张已经比较稳定，现在需要把它写成一篇论文能成立的样子：故事怎么讲，最相近的工作是谁，差异在哪里，哪些 claim 有引用支撑，哪些出彩点值得放到 introduction、related work 或 proposal 里。

原来“引用支撑”“定位差异化”“学习写作套路”看起来像三个动作，但真实写作时它们通常绑在一起发生。你不会脱离相似研究去判断某个 claim 是否该写，也不会脱离 close work 去学 gap 怎么包装；所谓写作套路，本质上也是观察别人如何把自己的贡献放进已有研究之间。

这里的产品设计是把三件事合并成 Research Framing Workflow。它先确认当前研究源，例如 Research Question Card、Committed Method Design、实验计划或草稿，再建立 Close Work Set。阅读这些相似工作时同时抽取 claim support、positioning matrix、story spine、contribution highlights 和 writing moves。用户最后拿到的不是零散素材，而是一份 research framing package：它说明论文故事、相似工作边界、可写 claim、不可过度声称的地方、差异化表述和可迁移的写作结构。

### 09 排雷和反驳自己：在太顺的时候找最强攻击

适用场景：你的 idea 已经成型，甚至已经有了问题、方法和实验路线，但担心自己只看到了支持材料，没有认真面对最可能被 reviewer 或导师攻击的地方。

常见做法是泛泛列一些 limitation，或者等到投稿前才补 rebuttal 话术。问题是，这样的风险整理通常太晚，也太软：它没有真正找负面证据、相似工作压力、假设漏洞、可行性风险和实验失败解释。

这里的产品设计是把排雷作为一个独立的攻击流程。它不服务于把故事讲得更漂亮，而是专门问：最强反对意见是什么？现有工作是否已经做了近似版本？关键假设有没有证据？实验失败会说明什么？哪些 claim 应该提前降级？用户最后得到的是 reviewer-style objection list 和初步 response，不是润色后的 confidence。
