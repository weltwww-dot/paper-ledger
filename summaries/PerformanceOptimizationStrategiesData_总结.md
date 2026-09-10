# Performance Optimization Strategies for Data Transmission From Edge to Cloud: A Review 总结

## 基本信息

- **标题**: Performance Optimization Strategies for Data Transmission From Edge to Cloud: A Review
- **作者**: Jian Liu, Yangyang Lin, Ziguang Fu, Gexi Lin, Guodao Sun, Zhu Xiao, Yilong Zhang, Dongdong Zhao, Peng Chen, Ronghua Liang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-05-12
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/tkde.2026.3692662
- **arXiv**: 无
- **PDF**: [TKDE_2026_PerformanceOptimizationStrategiesData.pdf](papers/TKDE_2026_PerformanceOptimizationStrategiesData.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文系统评述边缘到云数据传输的性能优化，将研究归纳为无损、有损和混合三类，并进一步提出面向带宽、能耗、时延与数据质量权衡的统一优化框架。

## 问题与动机

IoT 数据持续增长，而边缘设备在计算、存储、带宽和能源方面受限，原始数据传云会产生显著传输成本。既有综述多集中于无线传感器网络、单一压缩/预测技术或协议层优化，缺少针对 edge-to-cloud 数据传输策略的系统梳理。由于资源动态耦合且应用对时延、能耗、准确性等目标的优先级不同，该问题本质上是多目标权衡而非只追求压缩率。

## 方法

作者先通过 Google Scholar、IoT/系统领域期刊和会议检索，再追踪引用、参考文献和研究者主页，并排除只在外围章节提及传输优化、只关注 WSN 或只做协议层优化的工作。分类框架按数据保真度划分为无损（无损压缩、增量/全同步）、有损（有损压缩、预测传输）和混合策略，同时整理数据类型、硬件、压缩方法、开源性及压缩率/吞吐/时延/资源等指标。论文提出 cost-centric 统一模型，将带宽 B、能耗 E、端到端时延 L 与质量效用 U(Q) 纳入约束优化，并给出静态归一化和动态弹性权重，以及 Edge-Cloud Transmission Score（ECTS）用于归一化比较。

## 实验与结果

本文是综述论文，未报告独立的受控实验、统一数据集上的新模型训练或统计显著性实验；结果主要来自文献编码、分类和趋势分析。文中汇总显示，压缩率出现在超过 62% 的研究中，吞吐/传输时间/带宽利用率出现在超过 55% 的研究中，而纳入 CPU、内存和能源约束的研究仅超过 26%；约 65% 的被综述工作未开放实现，约 35% 发布了代码，涉及的边缘设备类型超过 30 种。作者据此指出现有工作普遍存在目标分散、AI 在线适配开销高、评价平台与数据集不统一、跨场景迁移性有限、保真度过度配置及边缘协作不足等问题。

## 贡献与局限

本文贡献在于把压缩、同步和预测置于同一 edge-to-cloud 传输视角，梳理三十年技术演化，并用成本模型和 ECTS 明确多目标权衡。未来方向包括资源/任务/上下文感知的自适应范式、动态多目标优化、低开销多变量 AI 预测、统一开放基准，以及边缘协作和多模态/LLM 辅助。作为综述，其结论依赖纳入文献的报告质量与指标可比性；全文未提供统一复现实验来验证 ECTS 在真实系统中的决策效果。

---
DOI: 10.1109/tkde.2026.3692662
