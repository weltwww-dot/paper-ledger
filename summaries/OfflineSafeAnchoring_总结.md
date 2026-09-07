# Offline constrained policy optimization with safe anchoring 总结

## 基本信息

- **标题**: Offline constrained policy optimization with safe anchoring
- **作者**: Diyuan Hou, Longyang Huang, Pu Feng, Wenjun Wu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108865
- **arXiv**: 无
- **PDF**: [NN_2026_OfflineSafeAnchoring.pdf](papers/NN_2026_OfflineSafeAnchoring.pdf)

## 一句话概括

面向安全离线强化学习提出带"安全锚定"的离线约束策略优化算法（OCPO-SA）：利用拉格朗日对偶给出离线约束策略优化的解析解，证明策略序列单调改进并对最坏情形代价给出上界，再用 CVAE 从离线数据蒸馏安全动作分布以限制策略更新，在 Safety-Gymnasium 与 Bullet-Safety-Gym 的全部测试环境中达成安全，平均代价较最优基线降低 24%。

## 问题与动机

强化学习在安全关键场景（自动驾驶、机器人等）的落地受安全约束与离线学习分布漂移的双重挑战制约：在线试错代价高且风险不可接受，而从静态数据集学习又容易因策略诱导的状态-动作分布偏离数据集而产生价值高估。在安全离线 RL 中，分布外（OOD）动作不仅造成价值高估，还常引发代价低估，进而导致真实部署中的灾难性安全违规。已有方法（如 CPQ、COptiDICE）将安全离线 RL 建模为多约束优化，但普遍缺乏约束策略优化问题的理论解析解，难以分析性能单调性，实际中仍可能违反代价约束。

## 方法

作者将安全离线 RL 建模为带累积代价约束与行为策略正则（KL 约束）的约束策略优化问题。首先通过拉格朗日对偶与 KKT 条件推导出该问题的解析闭式解（定理 1），其形式为行为策略按奖励、代价优势加权的指数族分布；随后证明按该式迭代更新可保证近似单调的性能改进（定理 2）并把最坏情形期望代价界定在行为策略代价加显式上界之内（定理 3）。为落地实现，提出安全锚定（safe anchoring）机制，含三部分：安全数据过滤（按折扣累积代价筛出安全轨迹子集）、安全策略蒸馏（在该子集上以 CVAE 训练安全行为策略）、双重安全约束策略优化（把解析最优策略投影到参数化高斯策略空间，损失含归一化的奖励/代价 Q 项与到安全锚定策略的行为正则项，并用 PID-Lagrangian 自适应更新乘子），从而将策略更新限制在安全动作区域、抑制 OOD 动作。

## 实验与结果

在 DSRL 平台的 Safety-Gymnasium 与 Bullet-Safety-Gym 两个基准上评估，涉及 CarButton/CarCircle/CarGoal/CarPush、BallRun、CarRun、DroneRun、AntRun、BallCircle、DroneCircle、AntCircle 等 16 个任务（表 2 结果取 3 个随机种子各 10 轮评估的平均）；对比基线包括 BC、BC_safe、CDT、BCQ-Lag、CPQ、FISOR、COptiDICE。结果表明 OCPO-SA 在所有测试环境中实现 100% 安全合规，平均代价较最优基线降低 24%，并在 16 个环境中 8 个取得最佳奖励；与 Transformer 型 CDT、扩散型 FISOR 相比，MLP actor-critic 架构训练成本更低。消融实验显示去掉行为约束或安全锚定会显著恶化性能与代价控制，PID-Lagrangian 较标准 Lagrangian 在复杂环境下收敛更快；代价阈值（10/20/50/100）敏感性实验显示算法能把代价稳定收敛到设定阈值附近。实验平台为 Ubuntu 20.04（CUDA 11.8、Torch 1.13.1、safety-gymnasium 0.4.0、bullet-safety-gym 1.4.0），双 RTX 3090Ti GPU。

## 贡献与局限

- 贡献一：推导出离线约束策略优化问题的解析解，并证明迭代更新的近似单调性能改进与最坏情形代价上界，为安全离线 RL 提供理论保证。
- 贡献二：提出 CVAE 蒸馏的"安全锚定"机制（安全数据过滤＋安全策略蒸馏＋双重安全约束优化），显式限制策略更新、抑制违反安全约束的 OOD 动作。
- 贡献三：提出完整算法 OCPO-SA，在两大基准上以更低资源实现全面安全与更优的奖励-代价平衡。
- 局限：文中的"安全"指基准协议下的约束满足而非所有部署场景的零违规；扩展到高维连续控制任务可能需要更大的生成模型；性能依赖数据集覆盖度与安全分布；奖励-代价权衡受约束与正则超参数控制。

---
DOI: 10.1016/j.neunet.2026.108865
