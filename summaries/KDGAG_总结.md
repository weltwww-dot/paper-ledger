# KD-GAG: Knowledge-Distilled Graph-Augmented Generation via Preference-Aware Subgraph Pruning 总结

## 基本信息

- **标题**: KD-GAG: Knowledge-Distilled Graph-Augmented Generation via Preference-Aware Subgraph Pruning
- **作者**: Long Zhao、Yin Xu、Yanyan Wang et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109587
- **arXiv**: 无
- **PDF**: [NN_2026_KDGAG.pdf](papers/NN_2026_KDGAG.pdf)

## 一句话概括

KD-GAG 把教师大模型的语义抽取与推理能力蒸馏到小模型以高效构建知识图谱，并依据生成器回答质量学习子图剪枝策略，使 GraphRAG 检索内容更符合生成器偏好。

## 问题与动机

GraphRAG 能利用知识图谱表达复杂依赖，但现有方法常忽视知识图谱构建质量，构图需多次调用大模型且成本高；检索优化还可能召回过多无关信息，并缺少检索器与生成器知识偏好的协同。

## 方法

教师大模型先以多步知识抽取和融合产生高质量图谱训练数据，再微调较小的学生模型，实现高效端到端知识图谱构建。检索阶段根据生成器最终回答质量计算奖励，进行偏好优化，学习保留有效证据、删除无关三元组的子图剪枝策略。

## 实验与结果

作者在 HotpotQA、2WikiMQA、Natural Questions 和 MedHop 四个问答基准上评估，覆盖多跳、开放域和生物医学推理。结果显示 KD-GAG 在不同设置下保持稳定且有竞争力的性能，同时提高知识图谱构建和检索效率，并表现出低资源适应性。

## 贡献与局限

贡献是同时优化 GraphRAG 的构图效率和生成器偏好对齐，而不是只改进检索模块。局限是学生模型会继承教师产生数据的偏差，奖励依赖生成器回答质量；换用不同生成器、知识领域或快速更新语料时可能需要重新蒸馏与对齐。

---
DOI: 10.1016/j.neunet.2026.109587
