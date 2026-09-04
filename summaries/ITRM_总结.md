# Imagining Trajectories for Anomaly Detection in Reinforcement Learning from Images 总结

## 基本信息

- **标题**: Imagining Trajectories for Anomaly Detection in Reinforcement Learning from Images
- **作者**: Tom Haider, Karsten Roscher, Stephan Günnemann
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-08-28
- **内容状态**: 完整
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10994-026-07126-7
- **PDF**: [ML_2026_ITRM.pdf](papers/ML_2026_ITRM.pdf)

## 一句话概括

提出 ITRM，一种完全 agent-agnostic 的视觉强化学习异常检测方法：基于循环状态空间世界模型的预测潜表征与参考嵌入的相似性比较检测异常输入，不依赖策略内部表征。

## 问题与动机

检测异常输入是强化学习智能体在真实环境安全部署的关键前提。异常检测在其他领域研究充分，但在 RL 中仍具挑战：高维感官观测与复杂时序依赖使现有方法受限，且多数方法依赖已训练智能体的内部表征，造成策略与安全机制的耦合，不利于独立部署安全监控。

## 方法

核心观察：对名义环境动力学的偏离可通过世界模型潜表征的差异识别。具体利用循环状态空间模型（recurrent state-space model）的预测组件生成确定性潜在嵌入，作为异常检测的规范性参考；通过相似性准则把预测潜特征与名义嵌入参考集比较；在世界模型潜空间操作，可捕获语义上有意义的偏离，且不需要访问策略内部。

## 实验与结果

广泛实验与消融表明检测性能强：在 Anomaly-Gym 基准上优于现有基线，平均 AUROC 0.853、FPR95 0.279（数字来自原文摘要）。

## 贡献与局限

- 贡献一：首个无需策略内部访问的 agent-agnostic 视觉 RL 异常检测方法，解耦策略与安全机制。
- 贡献二：世界模型潜空间预测-比较框架，在 Anomaly-Gym 上显著优于基线。
- 局限：评测集中于 Anomaly-Gym 基准；更多真实环境的部署验证待后续工作。

---

DOI: 10.1007/s10994-026-07126-7
