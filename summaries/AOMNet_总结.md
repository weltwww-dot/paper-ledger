# Acoustic-optical joint underwater object detection with multi-modality correlation features matching network 总结

## 基本信息

- **标题**: Acoustic-optical joint underwater object detection with multi-modality correlation features matching network
- **作者**: Meiyan Zhang、Yuxin Lin、Jifeng Zhu、Mai Wang、Wenyu Cai
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108975
- **arXiv**: 无
- **PDF**: [NN_2026_Paper11.pdf](papers/NN_2026_AOMNet_AcousticOpticalDetection.pdf)

## 一句话概括

AOMNet 融合水下相机与声呐信息，通过跨模态特征和区域匹配提高水下目标检测。

## 问题与动机

水下相机和声呐图像对齐较弱，单一模态容易受到浑浊、光照和纹理缺失影响。针对水下声光联合检测研究不足，作者希望在特征和决策两个层面同时利用两种传感器信息。

## 方法

AOMNet 在特征层引入 CPMFM，利用轮廓、纹理相似性和预测位置优化候选区域生成。在决策层采用 PLFM+BRM，通过掩膜形态计算与仿射变换完成区域配准和匹配，以改善边界框回归。

## 实验与结果

作者在自采集的声呐–水下相机数据集上验证方法。AOMNet 的 mAP 达到 81.3%，摘要称其相较现有单模态与多模态检测模型具有明显优势。

## 贡献与局限

贡献是构建面向水下声光数据的跨模态相关特征和区域匹配流程。局限是数据集为自采集数据，规模、场景多样性和不同声呐/相机组合下的可迁移性仍需外部验证。

---
DOI: 10.1016/j.neunet.2026.108975

