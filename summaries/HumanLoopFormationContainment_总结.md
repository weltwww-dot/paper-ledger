# Human-in-the-Loop Formation-Containment Safe Control for Multi-agent Systems via Reinforcement Learning 总结

## 基本信息

- **标题**: Human-in-the-Loop Formation-Containment Safe Control for Multi-agent Systems via Reinforcement Learning
- **作者**: Luning Yang, Pei Chi, Jiang Zhao, Yingxun Wang
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2025.3559040
- **arXiv**: 无
- **PDF**: [TAI_2026_HumanLoopFormationContainment.pdf](papers/TAI_2026_HumanLoopFormationContainment.pdf)

## 一句话概括

本文为未知动力学的非线性二阶多智能体系统设计人机协同编队-包围安全控制器，利用自适应神经网络识别动力学、actor–critic 强化学习求解最优控制，并通过局部拓扑信息在障碍环境中保持安全。

## 问题与动机

无人机和机器人编队在复杂环境中需要同时完成 leader 跟踪、队形保持和包围约束，但实际动力学通常未知，障碍物又要求控制器避免碰撞。单纯依赖全局状态或外部定位设备会增加通信和传感器负担；传统模型驱动控制也难以在未知动力学下达到最优。作者进一步引入人类操作员，让其可以与跟踪 leader 交互并通过多智能体网络影响系统，同时要求控制算法在局部连接信息下保持稳定和安全。

## 方法

作者使用自适应神经网络在线逼近 leader/follower 的未知非线性动力学，并证明识别误差渐近收敛。控制器采用 actor–critic 强化学习近似非线性系统的 Hamilton–Jacobi–Bellman 方程，以学习最优编队-包围跟踪策略；分布式控制只使用邻居和 leader 的局部拓扑信息。人机交互信号被纳入 leader 轨迹或控制输入，安全控制部分通过障碍相关约束限制系统状态，保证在未知障碍环境中完成队形包围而不破坏闭环稳定性。

## 实验与结果

仿真在包含 15 个机器人、leader 和 follower 的未知障碍环境中验证。神经网络识别参数、actor 网络和 critic 网络权重均渐近收敛；followers 最终收敛到期望凸包，多个 formation leaders 同时跟踪给定 leader 轨迹，完成 formation-containment tracking。加入人类反馈后，系统能够通过 leader 与网络局部交互调整运动，仍维持队形和安全避障。结果表明，跟踪误差渐近趋于零，控制器能够根据当前状态在线修正输入，对人类输入延迟、传感器噪声和通信延迟具有一定适应性。

## 贡献与局限

贡献在于把人机协同、未知动力学辨识、强化学习最优控制与安全编队-包围任务统一起来，并在局部信息下验证了多智能体障碍环境控制。局限是实验主要依赖仿真，模型仍需可获得状态信息和合理的网络连通性；人类输入、通信延迟和障碍感知误差的鲁棒性尚未通过真实平台系统评估。未来还需研究有向图、异构多智能体以及真实传感器条件下的时变编队任务。

---
DOI: 10.1109/tai.2025.3559040
