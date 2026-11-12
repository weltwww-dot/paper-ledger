# Adaptive dynamic programming for self-triggered optimal control in industrial spatiotemporal processes 总结

## 基本信息
- **标题**: Adaptive dynamic programming for self-triggered optimal control in industrial spatiotemporal processes
- **作者**: Binyan Li、Xiaopeng Cao、Biao Luo 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109853
- **发表**: 2026-11-10
- **日期来源**: 出版社正式 PDF 首页 Available online，2027 为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109853
- **PDF**: [NN_2026_SelfTriggeredADP.pdf](papers/NN_2026_SelfTriggeredADP.pdf)

## 一句话概括
用自触发自适应动态规划控制工业时空过程，在每次更新时预先决定下一次更新时间。

## 问题与动机
受强耗散偏微分方程描述的过程具有空间耦合和非线性。固定周期更新会产生较多计算，事件触发又往往需要持续监测触发条件。

## 方法
作者以空间基函数近似系统状态，用评论家网络逼近价值函数，执行器网络学习控制策略。自触发机制结合稳定性约束估计下一次更新时刻。

## 实验与结果
工业过程模型的数值仿真显示，控制量、网络权重和系统状态逐步收敛，性能指标有界，控制更新间隔呈非周期分布（PDF 第 8–9 页）。

## 贡献与局限
论文将自触发策略与偏微分方程系统的学习控制结合，并分析闭环稳定性及触发间隔。验证来自模型仿真，真实生产线的测量误差与实时成本仍需实测。

---
DOI: 10.1016/j.neunet.2026.109853 | PDF: [NN_2026_SelfTriggeredADP.pdf](papers/NN_2026_SelfTriggeredADP.pdf)
