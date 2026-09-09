# Enhancing Stability of Probabilistic Model-Based Reinforcement Learning by Adaptive Noise Filtering 总结

## 基本信息

- **标题**: Enhancing Stability of Probabilistic Model-Based Reinforcement Learning by Adaptive Noise Filtering
- **作者**: Wenjun Huang、Xinrui Yue、Yidong Chen、Tianfu Sun、Yunduan Cui
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3672453
- **arXiv**: 无
- **PDF**: [NN_2026_EnhancingStabilityProbabilisticModel.pdf](papers/NN_2026_EnhancingStabilityProbabilisticModel.pdf)

## 一句话概括

本文提出稳定化模型策略优化 SMBPO，用自适应噪声过滤同时抑制概率动力学模型和策略更新中的异常噪声与模型偏差，从而提升基于模型强化学习的训练稳定性和样本效率。

## 问题与动机

基于模型的强化学习通过学习环境动力学减少交互成本，但概率模型的不确定性、预测异常维度和模型偏差会在长时域滚动预测中累积，并进一步误导策略和价值函数更新。模型无关方法虽然稳定，却通常需要大量真实交互。作者希望在保留模型式方法样本效率的同时，过滤模型误差造成的有害信号。

## 方法

SMBPO 的自适应噪声过滤（ANF）包含两个层面：对概率动力学模型的预测分布检查异常维度并进行修正，对策略更新中的预测状态和价值函数执行裁剪，以减弱模型偏差传播。模型训练稳定后，SMBPO 引入批归一化加速策略学习。整体框架通过模型、actor 和 critic 的协同更新，把噪声过滤放在模型预测和决策优化两个误差来源上，而不是只在最终策略上做修正。

## 实验与结果

作者在五个 MuJoCo 控制基准和一个灵巧手场景上进行评测，并与模型无关及基于模型的强化学习基线比较。SMBPO 将训练时间降低约 90%，累计奖励比现有强基线提高约 50%，在灵巧手 HandReach 场景中也表现出较快收敛和较高平均回报；但在奖励更稀疏的 HandManipulateEgg 与 HandManipulateBlock 上仍然较困难。论文还报告 DroQ 为达到类似任务效果需要超过 SMBPO 20 倍的交互量。

## 贡献与局限

- 提出同时作用于概率模型预测和策略/价值更新的自适应噪声过滤机制。
- 结合裁剪和批归一化，在保持模型式强化学习样本效率的同时提高训练稳定性。
- 在 MuJoCo 与灵巧手任务上显著减少训练时间并提升累计奖励。
- 局限：静态状态裁剪可能使策略过于保守，长时域预测中过滤机制可能丢失关键信息，Q 值裁剪也可能引入漂移；真实机器人部署仍需处理传感器、执行器和动力学不确定性。

---
DOI: 10.1109/tnnls.2026.3672453
