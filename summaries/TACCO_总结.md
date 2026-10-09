# TACCO: Actor–Critic Contrastive Optimization for OOD Action Mitigation in Offline Reinforcement Learning 总结
## 基本信息
- **标题**: TACCO: Actor–Critic Contrastive Optimization for OOD Action Mitigation in Offline Reinforcement Learning
- **作者**: Haotian Zhang、Chen Wang、Jun Moon
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-07
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07170-3
- **PDF**: [ML_2026_TACCO.pdf](papers/ML_2026_TACCO.pdf)

## 一句话概括
TACCO 在 TD3+BC 离线强化学习框架中加入 actor 或 critic 表征上的对比学习，训练策略区分数据支持的状态—动作与分布外（OOD）动作，以减轻价值外推误差。

## 问题与动机
离线强化学习只能使用固定数据集，策略改进时可能提出数据很少覆盖的动作；critic 对这些动作的价值估计不可靠，容易过估并导致策略不稳。既有方法多从行为约束或保守价值正则化处理，论文转而直接在状态—动作表示空间区分受支持和可疑样本（第2–3页）。

## 方法
TACCO 保留 TD3+BC 的行为克隆约束，并设计两种按奖励结构使用的 SupCon 变体。稠密奖励场景采用 TACCO-A，在 actor 编码器上对比：数据集动作是正样本，随机动作和来自下一状态的策略动作与当前状态错配，作为两类负样本。稀疏奖励场景采用 TACCO-B，在 critic 表征上将高 Q 值且双 Q 网络分歧较小的状态—动作对筛为可靠样本，再同时约束可靠样本与其余样本。对比损失塑造表示空间，目标是让策略远离缺乏数据支撑的动作；它并不直接给出 OOD 的真实标签（第8–13页）。

## 实验与结果
作者在 D4RL 的 MuJoCo 与 Adroit 共27项任务上比较 TACCO 和 CQL、IQL、DT、TD3+BC、DTQL、O-DICE 等方法，报告5个随机种子的均值及95%置信区间。论文称 TACCO 在27项任务中有16项排名前二。与参数对齐的 TD3+BC 比较时，hopper-medium-replay 的归一化分数由65.58升至101.31，hopper-random 由20.90升至31.70；并非每项任务都提升，因此整体结果不应读成普遍优势（第15–17、23页）。

## 贡献与局限
贡献是将 OOD 缓解机制落实到 actor/critic 的状态—动作表征，并依据稠密或稀疏奖励选择对比位置与样本构造；消融结果也支持 actor、critic 的分工设计。证据集中在 D4RL 的 MuJoCo、Adroit 离线基准，且总体报告基于5个种子；实际在线交互、其他环境分布及更多随机性下的稳定性仍需验证。这一局限来自实验范围，而不是对方法在未测任务上的结论（第15–23页）。

---
DOI: 10.1007/s10994-026-07170-3
