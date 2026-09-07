# DECODE: Domain-Aware Continual Domain Expansion for Motion Prediction 总结

## 基本信息

- **标题**: DECODE: Domain-Aware Continual Domain Expansion for Motion Prediction
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3683469
- **arXiv**: 无
- **PDF**: [incremental.pdf](papers/incremental_b6cc221e8ffb.pdf)

## 一句话概括

Motion prediction is essential for autonomous vehicles to navigate complex environments and anticipate the behavior of other traffic participants. As new driving scenarios emerge, models must be continually updated without retraining from scratch. We propose DECODE, a continual learning framework that starts from a pre-trained generalized model and incrementally expands specialized models for distinct domains. Unlike existing approaches that pursue a single unified model, DECODE explicitly balances specialization and generalization through dynamic model selection. It employs a hypernetwork for parameter generation, which reduces storage costs, and utilizes a normalizing flow for real-time domain inference via likelihood estimation. Outputs from specialized and generalized models are fused using Bayesian uncertainty estimation. This integration ensures optimal performance in familiar conditions while maintaining robustness in novel scenarios. Extensive experiments show DECODE achieves a low forgetting rate of 0.044 and an average minADE of 0.584 m, outperforming prior methods and generalizing well across diverse driving domains. Furthermore, we demonstrate that DECODE can be extended beyond motion prediction to general continual learning tasks such as image classification, showcasing its broad applicability.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tpami.2026.3683469
