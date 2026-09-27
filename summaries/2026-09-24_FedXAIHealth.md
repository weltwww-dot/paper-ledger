# Explainable Federated Learning for Trustworthy Thoracic Disease Detection Under Non-IID Data Distributions 总结

## 基本信息
- **标题**: Explainable Federated Learning for Trustworthy Thoracic Disease Detection Under Non-IID Data Distributions
- **作者**: Suresh Arumugam、A. Sindhu、M. N. Saroja et al.
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-24
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07174-z
- **PDF**: [ML_2026_FedXAIHealth.pdf](papers/ML_2026_FedXAIHealth.pdf)

## 一句话概括
FedXAI-Health 在五个非 IID 模拟医院客户端上联合训练胸部疾病分类模型，并结合 SHAP 与 Grad-CAM 展示预测依据。

## 问题与动机
医院影像受隐私法规与机构边界限制，难以集中训练；不同医院病例分布不一致也会影响联邦模型性能和解释稳定性。作者评估分布式训练并提供可视化解释。

## 方法
研究使用 NIH ChestX-ray14，按患者划分训练测试集并模拟五个非 IID 客户端，以 EfficientNetB0 和 FedAvg 聚合训练；用 SHAP、Grad-CAM 展示模型关注区域，并重复实验三次。

## 实验与结果
论文报告 FedAvg 宏平均 AUC 为 0.8060，较集中式 EfficientNetB0 高约 2.0%。可视化解释显示模型关注与预测相关区域。该结果基于单一公开数据集的客户端划分模拟，并非多家医院真实协作试验。

## 贡献与局限
- 在非 IID 联邦设置下结合胸部疾病多标签分类与两种解释方法。
- 采用患者级划分以减少训练测试泄漏风险，并与集中式基线比较。
- 客户端来自单一数据集模拟，需真实多中心独立验证；热图和特征归因不能单独证明临床可信或因果解释能力。

---
DOI: 10.1007/s10994-026-07174-z
