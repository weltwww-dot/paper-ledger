# Bellman error centering 总结

## 基本信息

- **标题**: Bellman error centering
- **作者**: Xingguo Chen, Yu Gong, Jinguo Ye, Chao Li, Shangdong Yang, Wenhao Wang
- **期刊 / 会议**: Neural Networks 201 (2026) 108896
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108896
- **arXiv**: 无
- **PDF**: [NN_2026_BellmanErrorCentering.pdf](papers/NN_2026_BellmanErrorCentering.pdf)

## 一句话概括

本文通过双时间尺度分析证明基于价值的奖励中心化在数学上等价于 Bellman 误差中心化，据此提出 on-policy CTD 与 off-policy CTDC 两类居中时序差分算法并给出收敛证明，在多个基准环境中取得了优于 TD/TDC 基线的稳定性与性能。

## 问题与动机

现代强化学习（如 AlphaGo、基于 RLHF 的大语言模型）训练代价极其高昂，亟需提升算法效率。针对持续型任务，Naik 等（2024）提出的奖励中心化方法——on-policy 的 Simple Reward Centering (SRC) 与 off-policy 的 Value-based Reward Centering (VRC)——通过减去估计的平均奖励来提升连续任务上的性能、对奖励偏移的鲁棒性以及在表格 Q-Learning、DQN 和线性逼近下的收敛性。然而仍存在三大挑战：(1) 奖励中心化与其他 RL 算法的集成并非易事，其内部机制未被充分理解；(2) 在大状态空间配合函数逼近时的收敛性缺乏证明；(3) 其收敛到的最终解不明确。

## 方法

作者用双时间尺度视角重新审视两类奖励中心化更新规则：SRC 中快时间尺度递推收敛到平均奖励，可重写为对即时奖励做中心化，因而是严格意义上的"奖励中心化"；而 VRC 的快尺度递推收敛到期望 Bellman 误差，故其本质是对 TD 误差做中心化，即 Bellman 误差中心化 (BEC)，与 SRC 有本质区别。基于 BEC，作者定义了居中 Bellman 算子并推导出表格情形下的居中 Bellman 不动点，以及线性函数逼近下的居中 TD 不动点（即 centered TD fixed point）。随后以最小化居中 Bellman 误差（MSCBE）为目标、用半梯度方法导出 on-policy Centered Temporal Difference (CTD) 算法；由于 off-policy CTD 无法保证收敛，作者仿照 TDC 引入梯度修正项，提出最小化投影居中 Bellman 误差（MSPCBE）的 Centered TDC (CTDC) 算法。收敛性证明基于 Borkar 及 Borkar–Meyn 的多时间尺度随机逼近理论：定理 1 给出 on-policy CTD 几乎必然收敛到居中不动点 A⁻¹b，定理 2 给出 off-policy CTDC 的相应收敛保证，定理 3 则论证了将学习到的标量 ω 视为动态势函数可实现最优策略不变性。

## 实验与结果

实验以 TD 与 TDC 为基线，覆盖策略评估与控制两类任务：在经典反例 2-state counterexample 与 Baird's counterexample 上验证收敛性（TD 在此发散）；控制任务先采用表格价值函数（Maze、Cliff Walking），再用 tile coding 线性逼近（Mountain Car、Acrobot，5 组 tilings）。所有实验独立运行 50 次取均值与标准差。结果表明：预测任务中 TD 呈发散趋势、TDC 稳定收敛，CTD 与 CTDC 均收敛，且 CTD/CTDC 在 2-state 上收敛速度显著快于 TDC、在 Baird's 上略慢于 TDC；表格控制任务中四类算法最终都收敛到相同最优解，而 CTD/CTDC 收敛明显更快，在 Mountain Car 与 Acrobot 上不仅收敛更快、最终精度也显著更优。参数敏感性实验（指标 RMSCBE，参数候选见 Table 2）显示鲁棒性层级为 CTDC > CTD > TDC > TD：2-state 中 TD 在 α≥0.01 时迅速发散、仅在 α≤0.001 的极窄区间保持低误差；CTD 在 β∈[0.0005, 0.1] 宽区间内稳定（RMSCBE<0.2），Baird's 中 CTD 有效 α 区间比 TDC 扩大 10 倍，CTDC 在最优参数组合下可将 RMSCBE 降至 0.2 以下；β 的最优区间为 [0.0005, 0.01]。此外，数值分析解释了 off-policy CTD 经验上的反常收敛：2-state 中 off-policy TD 的矩阵为负定（等于 −0.2），而 CTD 矩阵为正定（等于 0.25）；Baird's 中 TD 关键矩阵存在负特征值，CTD 关键矩阵半正定；引理 1 证明一般两状态示例中 off-policy CTD 矩阵恒正定。

## 贡献与局限

主要贡献：(1) 证明 VRC 与 BEC 数学等价，将其与 SRC（直接奖励中心化）区分开来，揭示了 VRC 的核心是误差调整而非奖励调整；(2) 在线性函数逼近下证明 BEC 收敛到居中 TD 不动点，超越 Naik 等仅有的表格情形证明；(3) 设计 on-policy CTD 与 off-policy CTDC 算法，在标准假设下给出收敛证明并保持最优策略不变性；(4) 实验表明其稳定性和性能优于 TD/TDC 基线，代码开源在 https://github.com/GameAI-NJUPT/BEC。局限方面：off-policy CTD 缺乏形式化收敛证明（仅经验上稳定，可能受重要性采样比引起的方差放大与无界误差影响），为此才需要带修正项的 CTDC；BEC 目前主要适用于预测与线性函数逼近框架，作者将未来工作指向扩展到 λ-return、传统 RL 算法以及策略梯度与 actor-critic 方法。

---
DOI: 10.1016/j.neunet.2026.108896
