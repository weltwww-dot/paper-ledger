# Dynamic event-triggered optimized control for nonlinear multi-agent systems via reinforcement learning 总结

## 基本信息

- **标题**: Dynamic event-triggered optimized control for nonlinear multi-agent systems via reinforcement learning
- **作者**: Xiaoli Ruan、Shaowei Liang、Tao Peng、Ailong Wu、Ze Tang、Jianwen Feng
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108976
- **arXiv**: 无
- **PDF**: [NN_2026_DynamicEventTriggeredControl.pdf](papers/NN_2026_DynamicEventTriggeredControl.pdf)

## 一句话概括

本文结合多智能体 Actor–Critic、MLP 逼近和动态事件触发机制，实现资源受限非线性多智能体系统的鲁棒优化控制。

## 问题与动机

高阶非线性多智能体系统面临通信资源有限和环境不确定性两类部署瓶颈。持续采样会增加通信开销，未知非线性又使控制器设计困难。研究目标是在保证稳定性的同时减少数据交换并增强对传感器噪声的鲁棒性。

## 方法

作者构建动态事件触发的优化一致性跟踪控制框架，用 MLP 逼近未知非线性。多智能体 Actor–Critic 强化学习利用一致性信息调节参数，动态事件触发控制器在线调整采样误差阈值。Lyapunov 分析用于证明闭环稳定性并排除 Zeno 行为。

## 实验与结果

文章在代表性多电机系统上进行数值研究。结果表明，相较独立学习方法，所提方法减少了通信开销，并对传感器噪声表现出更强鲁棒性；摘要未给出可复核的统一数值，故不额外补写。

## 贡献与局限

贡献是把动态触发采样、优化控制和多智能体强化学习统一起来，并给出稳定性理论。局限是证据主要来自仿真多电机系统，真实通信丢包、异步执行和大规模智能体下的成本仍需实验。

---
DOI: 10.1016/j.neunet.2026.108976
