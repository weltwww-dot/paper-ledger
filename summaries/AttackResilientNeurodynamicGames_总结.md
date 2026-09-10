# Attack-resilient adaptive distributed neurodynamic approach for solving noncooperative games 总结

## 基本信息

- **标题**: Attack-resilient adaptive distributed neurodynamic approach for solving noncooperative games
- **作者**: Zhijie Chen, Jianing Chen, Xinwen Bu, Sitian Qin
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108920
- **arXiv**: 无
- **PDF**: [NN_2026_AttackResilientNeurodynamicGames.pdf](papers/NN_2026_AttackResilientNeurodynamicGames.pdf)

## 一句话概括

论文提出具备随机/离散切换通信和自适应机制的分布式神经动力学方法，使受探索攻击、因果攻击和外部扰动影响的非合作博弈仍能收敛。

## 问题与动机

非合作博弈中的参与者通常有私有不等式约束，通信网络还可能遭受窃听等探索攻击或篡改信息的因果攻击。固定切换序列会积累信息泄露风险，外部扰动也会破坏求解稳定性。

## 方法

连续时间方案让通信拓扑在有限个有向强连通图中随机切换，并用奇异摄动技术分析收敛；扰动观测器负责拒止外部扰动。针对因果攻击和通信受限，论文进一步给出离散时间切换方案、自适应惩罚机制，并明确排除 Zeno 行为。

## 实验与结果

仿真结果显示，方法相较现有方案具有更快收敛、更强攻击韧性和更好的动态适应性。自组织自动驾驶车辆网络的应用案例进一步验证了实际效用；论文摘要未给出具体误差数字。

## 贡献与局限

贡献是把随机通信切换、扰动拒止和攻击韧性统一到分布式神经动力学博弈求解中，并给出收敛证明。局限是理论条件和网络拓扑假设较强，真实通信丢包、攻击协同和大规模异构车辆上的效果仍需实测。

---
DOI: 10.1016/j.neunet.2026.108920
