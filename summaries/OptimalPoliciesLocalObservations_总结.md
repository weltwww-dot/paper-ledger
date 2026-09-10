# Learning Optimal Policies With Local Observations for Cooperative Multiagent Reinforcement Learning

## 基本信息

- **标题**: Learning Optimal Policies With Local Observations for Cooperative Multiagent Reinforcement Learning
- **作者**：He Kong、Qianli Xing、Qi Wang、Hechang Chen、Runliang Niu、Zhiyi Duan、Shiqi Wang、Yi Chang、Irwin King
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3673692
- **arXiv**：无
- **PDF**：[NN_2026_OptimalPoliciesLocalObservations.pdf](papers/NN_2026_OptimalPoliciesLocalObservations.pdf)

## 一句话概括

本文从局部观测下的潜在状态恢复与最优策略可达性出发，提出 UMARL 多智能体强化学习方法，通过可见性加权注意力、个体权重分解和互信息正则改善协作探索与价值分配。

## 问题与动机

协作多智能体强化学习通常采用集中训练、分散执行，但执行阶段每个智能体只能看到局部观测，部分可观测性会造成状态混淆、探索不足和信用分配困难。论文希望在不要求执行阶段共享全局状态的前提下，理论说明局部观测何时能够支持个体与团队的最优策略，并设计可学习的表示和价值分解机制，使智能体既能关注有效可见信息，又能主动探索潜在的有用状态。

## 方法

论文证明，在适当的潜在状态表示下，局部观测可以支持最优个体策略和全局策略；在集中训练、分散执行框架中，还可以从局部观测近似恢复相关信息。基于此提出 UMARL：注意力与频率加权可见性矩阵用于构造统一表示的 ARN；个体加权网络 IWN 使用非负权重完成价值分解并保持个体—全局最优一致性；潜在状态恢复模块以互信息下界正则 LSR 鼓励探索有价值的隐藏状态。整体以 DRQN 为基础，通过时序差分目标与 `λL_MI` 联合训练，形成端到端的局部观测策略学习框架。

## 实验与结果

实验覆盖 m-step 矩阵博弈、Level-Based Foraging、StarCraft II/SMAC 和 Google Research Football，并与 12 个代表性基线比较。在 m=10 矩阵博弈中，UMARL 的收益达到 13，优于 QMIX 约 10 的水平；在 LBF 中收敛更快且获得更高回报。在 SMAC 的 8 个地图上，UMARL 在 5 个地图取得最佳表现并获得最高平均排名，所述实验中只有 UMARL 完成了 3s vs 5z 任务；在 GRF 中也改善了整体策略表现，但部分探索可能进入无关区域。方法参数量略有增加，但换来了较稳定的协作收益和胜率。

## 贡献与局限

论文把局部观测下的潜在状态可达性分析与可见性加权表示、保持 IGM 的价值分解和互信息探索结合起来，为 CTDE 场景中的局部策略学习提供理论与算法方案。局限在于实验主要建立在 QMIX 式单调价值分解骨干上，互信息探索仍可能访问无关状态；方法也集中于价值型 MARL，对策略梯度或其他策略型方法的适配尚未解决。后续可研究更一般的价值表示、无关探索抑制和策略型多智能体算法。

---
DOI: 10.1109/tnnls.2026.3673692
