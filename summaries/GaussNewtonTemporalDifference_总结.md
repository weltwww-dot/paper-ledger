# Gauss–Newton Temporal Difference Learning With Nonlinear Function Approximation 总结

## 基本信息

- **标题**: Gauss–Newton Temporal Difference Learning With Nonlinear Function Approximation
- **作者**: Zhifa Ke, Junyu Zhang, Zaiwen Wen
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3661291
- **arXiv**: 无
- **PDF**: [NN_2026_GaussNewtonTemporalDifference.pdf](papers/NN_2026_GaussNewtonTemporalDifference.pdf)

## 一句话概括

本文提出 Gauss–Newton 时序差分学习（GNTD），用近似 Gauss–Newton 步优化非线性函数逼近下的 Bellman 误差，在 ReLU 网络等设置下给出更好的样本复杂度，并取得更快收敛和更高强化学习回报。

## 问题与动机

非线性函数逼近是深度强化学习扩展到复杂状态空间的基础，但传统 TD 方法在非线性参数化下的有限样本理论和数值稳定性仍有限，双重采样问题也使直接优化均方 Bellman 误差困难。作者希望在保持 Q 学习目标的同时，利用二阶曲率信息加快优化，并给出适用于神经网络和一般光滑函数逼近的非渐近收敛分析。

## 方法

GNTD 每次迭代对一种均方 Bellman 误差执行 Gauss–Newton 更新，并使用 target network 构造目标，避免双重采样。论文分析了不精确 Gauss–Newton 步，给出可用低成本矩阵迭代近似更新的实现；实际算法采用 K-FAC 风格近似降低矩阵计算开销。理论上，作者分别研究 ReLU 神经网络和一般光滑函数逼近，证明在温和条件下可有限样本收敛到全局最优 Q 函数，并把方法扩展到 GNDQN 及连续控制中的 GNTD3+BC。

## 实验与结果

实验覆盖 OpenAI Gym 的在线策略优化、CartPole-v1 和 Acrobot-v1 离线离散控制，以及基于 D4RL/MuJoCo 的连续控制任务。在线任务中，PG-GNTD 在 Hopper、Walker2d 和 Swimmer 上比 PG-TD 收敛更快，并在所有任务取得更高最终回报；离散任务中，GNTD 相比 TD 在收敛速度、最终回报和 Bellman 误差上均更优，加入 target-network 动量后的 GNDQN 也优于 DQN。连续任务中，GNTD3+BC 使用批大小 256、学习率 `0.0003`、阻尼率 `0.0003`，在多种数据集类型下相较 TD3+BC 获得更高最终回报和更低方差。理论结果给出 ReLU 网络约为 `\tilde O(ε^-1)` 的样本复杂度，优于现有神经 TD 的 `O(ε^-2)`；一般光滑函数逼近达到 `\tilde O(ε^-1.5)`。

## 贡献与局限

贡献包括：把 Gauss–Newton 更新引入非线性 TD 学习；同时给出不精确更新的高效实现和有限样本全局收敛理论；在在线、离线、离散和连续 RL 任务中验证了速度与回报优势。局限是实际计算仍依赖 K-FAC 或其他矩阵近似，网络规模扩大时二阶统计量的存储与更新成本可能成为瓶颈；理论依赖独立同分布采样等条件，复杂 actor–critic 交互和强非平稳数据下的收敛性质仍待研究。

---
DOI: 10.1109/tnnls.2026.3661291
