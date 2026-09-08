# SWIFT-KD: Sliding Window Intelligent Federated Transformer Learning with Knowledge Distillation for Building Energy Prediction 总结

## 基本信息

- **标题**: SWIFT-KD: Sliding Window Intelligent Federated Transformer Learning with Knowledge Distillation for Building Energy Prediction
- **作者**: Jessica Al Achy、Hassan Harb、Abdallah Makhoul
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-07
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07153-4
- **arXiv**: 无
- **PDF**: [ML_2026_SWIFTKD.pdf](papers/ML_2026_SWIFTKD.pdf)

## 一句话概括

SWIFT-KD 将分层滑动窗口 Transformer 与联邦知识蒸馏结合，在不集中建筑数据的前提下兼顾长序列建模、预测精度和边缘端通信效率。

## 问题与动机

建筑能耗预测有助于提升能源效率，但跨建筑部署受到隐私法规、数据异质性和通信资源限制。传统联邦学习既难以高效处理长时间序列，又需频繁传输完整模型参数，对资源受限的边缘设备负担较重。

## 方法

框架把长能耗序列分解为相互重叠的窗口，用分层 Transformer 同时提取局部规律与长期依赖。联邦端通过知识蒸馏传递软预测而非完整权重，使参与方保护原始数据的同时共享知识并压缩通信量。

## 实验与结果

在 100 栋异构建筑的 ASHRAE 数据集上，方案取得 R²=0.9708、RMSE=92.24 kWh、MAE=44.58 kWh；相较标准 FedAvg 提升 21%，相较集中式训练提升 13.3%。通信量降低约 300 倍，并在两个通信轮次内达到峰值性能。

## 贡献与局限

贡献在于统一解决联邦建筑能耗预测中的长序列与高通信开销问题，并展示快速收敛能力。局限是公开摘要只报告单一数据集和既定规模，跨气候区域、参与方掉线及隐私攻击下的稳健性仍待验证。

---
DOI: 10.1007/s10994-026-07153-4
