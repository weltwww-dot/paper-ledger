# Tree of Thoughts 总结

## 基本信息

- 标题: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- 作者: Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- 期刊 / 会议: NeurIPS 2023
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.48550/arXiv.2305.10601
- PDF: [NeurIPS_2023_ToT.pdf](papers/NeurIPS_2023_ToT.pdf)

- 标题: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- 作者: Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- 期刊 / 会议: NeurIPS 2023
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**：Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- **作者**：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- **会议与年份**：37th Conference on Neural Information Processing Systems（NeurIPS 2023）
## 一句话概括

论文提出 Tree of Thoughts（ToT）推理框架，把大语言模型的中间推理组织成可生成、评估、搜索的“思维”树，使模型能够探索多条路径、前瞻并在必要时回溯，从而处理 Chain-of-Thought 难以解决的规划与搜索问题。

## 问题与动机

标准语言模型在推理时仍主要按 token 从左到右生成；Chain-of-Thought 虽然加入中间步骤，但通常仍沿单一路径展开，缺少对不同后续、整体进展和错误分支的显式比较。论文借鉴人类问题求解中的组合搜索与启发式规划，将需要探索、策略性前瞻或关键早期决策的任务表示为搜索问题。

## 方法

ToT 将输入和已有中间步骤表示为树状态，并围绕四个设计问题展开：如何分解 thought、如何从状态生成候选 thought、如何用语言模型评估状态、以及采用何种搜索算法。候选生成可采用独立采样或顺序提议；评估可对每个状态给出 value，也可在多个状态间投票。论文使用 breadth-first search（Game of 24、Creative Writing）或 depth-first search（Mini Crosswords），并利用剪枝、前瞻和回溯控制搜索；该框架不需要额外训练。

## 实验与结果

实验使用温度 0.7 的 GPT-4，覆盖 Game of 24、Creative Writing 和 5×5 Mini Crosswords。Game of 24 的 100 个较难实例中，IO、CoT、CoT-SC 的成功率分别为 7.3%、4.0%、9.0%，ToT 在 breadth 1 和 5 时分别为 45% 和 74%；100 次采样的最佳 CoT 为 49%。Creative Writing 中，GPT-4 自动连贯性评分为 IO 6.19、CoT 6.93、ToT 7.56，人类比较中 ToT 胜过 CoT 的样本为 41 对 21 对。Mini Crosswords 中 ToT 的正确字母、单词和整题成功率为 78%、60% 和 20%（4/20），使用 oracle 最佳状态时为 82.4%、67.5% 和 35%（7/20）。附录还报告了 GSM8K 与 StrategyQA 的 zero-shot 结果，以及 GPT-3.5 和成本分析。

## 贡献与局限

论文的主要贡献是提出一个模块化的 thought-level 搜索框架，将候选生成、语言模型自评估与 BFS/DFS 结合，并在数学、创作和词语填字任务上验证探索与回溯的价值；它也把 IO、CoT、CoT-SC 等视为受限的 ToT 特例。局限包括：ToT 的计算量和 API 成本明显高于 IO/CoT，启发式评估可能误剪枝，实验主要集中在三个相对简单且专门设计的任务；对于 GPT-4 已经擅长的任务未必值得采用。论文还指出，面向真实环境的更强自主决策可能带来滥用风险，而外部知识获取和更高效的搜索仍是开放问题。

---

DOI: 10.48550/arXiv.2305.10601
