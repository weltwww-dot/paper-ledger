# DAG-NAS : An explainable neural architecture search framework for reinforcement learning 总结

## 基本信息

- **标题**: DAG-NAS : An explainable neural architecture search framework for reinforcement learning
- **作者**: Taegun An、Changhee Joo
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108901
- **arXiv**: 无
- **PDF**: [NN_2026_Paper04.pdf](papers/NN_2026_DAGNAS_ExplainableArchitectureSearch.pdf)

## 一句话概括

DAG-NAS 在强化学习中搜索标量级 DAG 神经网络，以较少参数获得可解释策略和价值网络。

## 问题与动机

强化学习中的神经架构通常依赖人工设计，状态变量又常常冗余且相关。传统 NAS 更重视性能，难以说明哪些输入特征驱动了决策，也不利于调试和压缩模型。研究目标是把架构搜索与输入级特征选择、解释性结合起来。

## 方法

作者把前馈网络表示为由标量级操作和连接组成的有向无环图。搜索阶段对操作和连接进行可微优化，随后离散化并剪枝。该框架同时搜索 Actor-Critic PPO 的 actor 与 critic 网络，并通过保留关键路径展示决策所依赖的信息。

## 实验与结果

文章在多个强化学习任务上比较搜索得到的架构。结果显示，DAG-NAS 的性能与基线相当，同时参数量显著更少，并能突出关键特征和决策路径；摘要未给出统一数值，因此不补写具体百分比。

## 贡献与局限

贡献是提出标量级 DAG 搜索空间，让 NAS 兼顾轻量化和解释性。局限是搜索成本、解释路径对任务和状态表示的依赖，以及在 PPO 之外其他 RL 算法上的适用性仍需进一步研究。

---
DOI: 10.1016/j.neunet.2026.108901

