# Robust Reinforcement Learning via Leveraging Historically Optimal Policy With Regulation of Performance 总结

## 基本信息

- **标题**: Robust Reinforcement Learning via Leveraging Historically Optimal Policy With Regulation of Performance
- **作者**: Qinglong Chen；Fei Zhu
- **期刊 / 年份**: IEEE Transactions on Neural Networks and Learning Systems，2026
- **研究方向**: 强化学习、对抗鲁棒性
- **DOI**: 10.1109/tnnls.2026.3670947
- **PDF**: [NN_2026_RobustReinforcementLeveragingHistorically.pdf](papers/NN_2026_RobustReinforcementLeveragingHistorically.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出 HORP，通过历史上表现最优的策略指导当前策略优化，并结合性能感知调整与熵调节的对抗训练，提高强化学习策略在状态空间攻击下的自然性能、鲁棒性和对未知攻击的泛化能力。

## 问题与动机

强化学习策略容易受到观测扰动影响，并可能对训练期间见过的特定扰动过拟合。现有基于对抗者的训练主要依赖试错交互，缺少结构化的策略改进方向；维护大量针对不同攻击者的策略又会增加计算与样本成本，因此需要兼顾指导性、扰动多样性和效率的训练机制。

## 方法

HORP 将历史最优策略作为教师、当前策略作为学生，以策略价值差距和策略分布散度构造指导价值函数，把学习集中到仍有改进空间的动作区域。方法同时维护三个学生策略，并用性能感知控制器按性能差距调整策略替换/重置节奏；熵调节对抗训练则根据近期扰动幅度注入自适应不确定性，在利用性样本与探索性样本之间进行受总变差约束的概率选择，以避免扰动熵塌缩。

## 实验与结果

实验覆盖 Hopper、Walker2d、HalfCheetah 和 Ant 四个 MuJoCo 环境，对比 ATLA-PPO、PA-ATLA-PPO、WocaR-PPO、PROTECTED-PPO 和 ACoE-PPO，并使用随机、RS、MAD、SA-RL、PA-AD 五类攻击。结果显示，HORP 在前三个环境取得更高自然回报；在 Ant 上 PROTECTED-PPO 的自然回报为 5884±102，高于 HORP 的 5634±28（p<0.05），但 HORP 在多数攻击设置下保持竞争力并在多种动态攻击中表现稳定。每项主要评估基于 50 个回合、10 个随机种子；HORP 样本效率接近 ATLA-PPO，训练时间快于 PROTECTED-PPO但约为 WocaR-PPO 和 ACoE-PPO 的两倍。

## 贡献与局限

论文贡献是把历史策略的显式指导、性能感知的多策略优化和熵调节扰动多样性整合到一个鲁棒 RL 框架中，并通过消融与动态攻击实验验证三部分的作用。局限是当前主要针对有界 ℓp 状态扰动，尚未覆盖光照等语义畸变或局部贴片攻击；多策略交互也带来高于轻量基线的计算开销。作者将视觉强化学习中的真实攻击与跨环境无监督泛化列为后续方向。

---
DOI: 10.1109/tnnls.2026.3670947
