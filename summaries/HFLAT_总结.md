# Hierarchical fusion and local-aware transformer for occluded person re-identification 总结

## 基本信息

- **标题**: Hierarchical fusion and local-aware transformer for occluded person re-identification
- **作者**: Haishun Du、Chuaner Huang、Linbing Cao、Jieru Li、Wenzhe Zhang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108883
- **arXiv**: 无
- **PDF**: [NN_2026_Paper21.pdf](papers/NN_2026_HFLAT_OccludedPersonReID.pdf)

## 一句话概括

HFLAT 通过层级融合、前景背景分离和局部感知注意力提升遮挡行人重识别。

## 问题与动机

遮挡行人重识别需要在缺失身体区域时匹配同一行人。现有 Transformer 方法常平等处理图像 patch，未充分强调关键区域，也难以隔离背景并提取细粒度局部特征。研究目标是提高遮挡和复杂背景下的身份判别能力。

## 方法

Feature Hierarchical Fusion Module 按 patch 对全局特征的重要性分层融合，增强关键区域。Feature Separation Module 用 patch 级显著性分析区分前景和背景，减轻遮挡与背景干扰。Local Feature Extraction Module 通过局部感知多头注意力限制特征交互范围，强化细粒度局部建模。

## 实验与结果

在 Occluded-DukeMTMC、Occluded-ReID、Market1501 和 DukeMTMC-ReID 上，HFLAT 达到当前 state-of-the-art。四个数据集的 Rank-1 分别为 79.6%、89.8%、95.9% 和 90.6%，mAP 分别为 64.7%、84.9%、90.8% 和 82.2%。

## 贡献与局限

贡献是把 patch 重要性、前景背景分离和局部注意力统一到遮挡 ReID Transformer 中。局限是结果依赖现有基准和遮挡分布，真实摄像头变化、极端遮挡以及模型计算开销仍需评估。

---
DOI: 10.1016/j.neunet.2026.108883

