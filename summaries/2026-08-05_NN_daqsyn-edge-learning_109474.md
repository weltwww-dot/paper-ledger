# DAQSyn: A decentralized adaptive quantization-aware synchronous framework in heterogeneous on-device AI networks 总结

## 基本信息
- **标题**: DAQSyn: A decentralized adaptive quantization-aware synchronous framework in heterogeneous on-device AI networks
- **作者**: Misbah Bibi、Qazi Waqas Khan、Syed Ali Yazdan 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109474
- **发表**: 2026-08-05
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109474
- **PDF**: [NN_2026_daqsyn-edge-learning_109474.pdf](papers/NN_2026_daqsyn-edge-learning_109474.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
DAQSyn 联合自适应量化、同步和性能加权聚合以适配异构边缘设备，实验显示可在较低位宽下维持约 81%–82% 准确率并缩短等待时间，但结论受测试平台与任务范围限制。

## 问题与动机
如何在设备能力和数据分布不同的去中心化边缘网络中兼顾模型精度、通信开销与同步等待？

## 方法
各设备按计算和通信能力自适应调整量化精度，结合 BSP 同步机制与性能感知聚合，并在异构硬件测试床上评估收敛、准确率、等待时间和模型大小。

## 实验与结果
使用 CIFAR 与合成 RGB-D 数据，并在异构边缘设备测试床比较固定精度及自适应量化方案；受限设备使用较低位宽仍达到约 81%–82% 准确率，报告的等待时间约为 10–29 ms，文中也展示不同量化方案的压缩与等待时间权衡（PDF 第7–16页）。

## 贡献与局限
将量化精度、同步和加权聚合纳入统一的资源感知去中心化学习框架；真实部署规模、设备组合和更广泛任务上的可扩展性尚需进一步验证。

---
DOI: 10.1016/j.neunet.2026.109474 | PDF: [NN_2026_daqsyn-edge-learning_109474.pdf](papers/NN_2026_daqsyn-edge-learning_109474.pdf)
