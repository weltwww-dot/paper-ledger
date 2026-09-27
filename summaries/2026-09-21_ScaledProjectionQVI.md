# Scaled projection neural network for quasi-variational inequalities 总结

## 基本信息
- **标题**: Scaled projection neural network for quasi-variational inequalities
- **作者**: Mohammed Alshahrani、Qamrul Hasan Ansari
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-21
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109667
- **PDF**: [NN_2026_ScaledProjectionQVI.pdf](papers/NN_2026_ScaledProjectionQVI.pdf)

## 一句话概括
本文构造以正定矩阵加权投影为核心的神经动力系统，并给出明确条件下求解拟变分不等式的指数收敛保证。

## 问题与动机
拟变分不等式的可行集随状态变化，较固定可行集问题更难分析。已有投影动力系统与矩阵预条件网络分别处理相关子问题，如何在状态依赖可行集下兼顾几何预条件和稳定性仍有挑战。

## 方法
作者将可行集表示为固定闭凸集经收缩映射平移后的集合，并以固定对称正定矩阵定义度量投影。再证明平衡点与原问题解等价，以加权 Lyapunov 函数推导全局指数收敛条件、步长区间及 Euler 离散化性质。

## 实验与结果
理论表明，当单调性强度超过由 Lipschitz 常数、平移收缩率及矩阵界共同决定的条件时，连续系统全局指数收敛，Euler 离散化保持认证速率。五类应用实验展示预条件效果；证书未覆盖但数值收敛的情况只是经验结果。

## 贡献与局限
- 统一分析状态相关可行集、矩阵加权投影和投影神经动力系统。
- 给出显式稳定性条件与可计算步长窗口。
- 保证依赖较强条件；仅有单调性不足以确保收敛，条件外的行为不由本文证书保证。

---
DOI: 10.1016/j.neunet.2026.109667
