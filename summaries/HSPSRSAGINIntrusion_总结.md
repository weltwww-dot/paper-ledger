# A hierarchical and privacy-preserving intrusion detection framework for SAGIN-enabled IIoT using graph neural networks and deep Q-learning 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：A hierarchical and privacy-preserving intrusion detection framework for SAGIN-enabled IIoT using graph neural networks and deep Q-learning
- 作者：Mueen Uddin, Sonia Khan, Fuhid Alanazi, et al.
- 期刊 / 年份：Neural Networks / 2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108876
- PDF：[HSPSRSAGINIntrusion.pdf](papers/HSPSRSAGINIntrusion.pdf)

## 一句话概括

HSP-SR把 SAGIN 的分层入侵检测、隐私保护元数据共享、GNN 拓扑建模和 deep Q-learning 响应策略结合起来，以兼顾 IIoT 安全、能耗、延迟和通信开销。

## 问题与动机

SAGIN-enabled IIoT 面临节点移动、链路异构、边缘资源受限及跨层攻击传播等问题。固定阈值或集中式检测难以适应网络状态变化，还可能造成不必要的上行传输，因此需要分层、节能、隐私保护且能自适应调整响应的框架。

## 方法

地面层使用轻量 autoencoder，并依据剩余能量、时间变化和局部拥塞自适应检测阈值；空中层融合 trust、entropy 和 freshness 进行告警；空间层用时空 GNN 建模拓扑并推断跨域攻击。跨层通信采用椭圆曲线密钥交换与 AES 加密，Deep Q-Network 在威胁、延迟、能耗和网络状态构成的 MDP 中选择缓解动作；调度和 cross-layer optimization 负责迁移工作负载。

## 实验与结果

论文使用 CSE-CIC-IDS2018 的六类攻击场景评估。HSP-SR 检测准确率为 99.42%，相对 QFL 和 SEAP 分别高 3.1 和 4.7 个百分点；误报率为 0.72%，相对 FEDRL 下降 35.4%；拥塞流量下通信数据为 8.2 MB，相对 DSFC 减少 29.3%；能耗比 HDMC 低 22.1%，所有场景端到端延迟低于 130 ms。消融实验显示移除 cross-layer optimization 后 S6 准确率降至 84.7%、延迟升至 150 ms。

## 贡献与局限

论文贡献了面向 SAGIN-IIoT 的分层安全架构、隐私保护的信任/元数据协同机制和基于 MDP 的自适应响应与调度，并以多指标实验验证收益。局限是当前策略对离散动作和有限 replay memory 依赖，对零日/多态攻击、卫星时延变化、空中链路中断及非平稳威胁环境的在线适应仍需增强。

DOI: 10.1016/j.neunet.2026.108876
