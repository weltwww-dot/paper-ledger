# Plan of Knowledge：面向时序知识图谱问答的检索增强大语言模型

## 基本信息

- 标题: Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering
- 作者: Ying Zhang, Xinying Qian, Yu Zhao, Baohang Zhou, Xuhui Sui, Xiaojie Yuan
- 期刊 / 会议: IEEE Transactions on Knowledge and Data Engineering 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1109/tkde.2026.3718295
- PDF: [TKDE_2026_PlanOfKnowledge.pdf](papers/TKDE_2026_PlanOfKnowledge.pdf)

- 标题: Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering
- 作者: Ying Zhang, Xinying Qian, Yu Zhao, Baohang Zhou, Xuhui Sui, Xiaojie Yuan
- 期刊 / 会议: IEEE Transactions on Knowledge and Data Engineering 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**：Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering
- **作者**：Ying Zhang, Xinying Qian, Yu Zhao, Baohang Zhou, Xuhui Sui, Xiaojie Yuan
- **期刊**：IEEE Transactions on Knowledge and Data Engineering, Vol. 38, No. 10, October 2026
- **研究方向**：时序知识图谱问答、检索增强生成、LLM 推理
## 一句话概括

Plan of Knowledge（PoK）把复杂时序问题拆成子目标序列，并用对比式时序检索选择语义和时间都匹配的事实，从而提升 LLM 的 TKGQA 推理准确性和可解释性。

## 问题与动机

时间知识图谱问答不仅要求理解实体关系，还要处理事件发生顺序、时间范围和相对时间约束。传统 TKG 嵌入或图神经网络难以表达复杂问题语义；LLM 虽有较强语言理解能力，却容易出现时序推理错误、知识缺失和幻觉。论文因此把显式规划与时序知识检索结合。

## 方法

PoK 模块依据可用工具和问题结构，把复杂问题分解为有序子目标，作为检索与推理的中间计划。与此同时，作者构建带对比学习检索机制的时间知识库，使候选事实不仅在语义上相关，也在时间维度上对齐；LLM 按计划逐步调用检索结果完成答案。结构化计划提供推理轨迹，时序检索则为每一步补充可验证事实。

## 实验与结果

论文在四个时序知识图谱问答基准上评估检索与最终问答性能。PoK 在检索精度和推理准确率上均取得明显提升，最高绝对提升 35.3 个百分点；消融结果也支持子目标分解与对比时序检索的互补作用。

## 贡献与局限

论文贡献是提出面向 TKGQA 的“规划+对比时序检索”框架，缓解 LLM 的时间推理幻觉，并让答案形成更清晰的中间推理链。局限是评测主要集中于现有基准和结构化时间知识图谱；开放域、多跳不完整图谱、事实持续更新及更复杂自然语言时间表达下的泛化仍需检验。

---
DOI: 10.1109/tkde.2026.3718295
