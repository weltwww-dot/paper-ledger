# CC-Net: A cross-hierarchical context-aware network for medical image segmentation 总结

## 基本信息

- **标题**: CC-Net: A cross-hierarchical context-aware network for medical image segmentation
- **作者**: Xiaoyan Zhang、Zheng Zhao、Weiqiang Sun、Yongqin Zhang、Chunlin Yu、Xiangfu Meng
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108950
- **arXiv**: 无
- **PDF**: [NN_2026_Paper03.pdf](papers/NN_2026_CCNet_CrossHierarchicalContextAware.pdf)

## 一句话概括

CC-Net 显式交互不同层级特征，以提升复杂病灶和细粒度结构的医学图像分割。

## 问题与动机

医学图像中的病灶边界和细小结构需要同时利用浅层空间细节与深层语义信息。传统 U 形网络多在同层跳连，跨层级互补不足，导致模糊边界、小病灶和复杂形态难以准确分割。研究因此关注跨层级和跨分支的上下文建模。

## 方法

CC-Net 包含 Cross-Hierarchical Feature Aggregation（CFA）、Global Feature Aggregation（GFA）、Cross-Branch Semantic Supplement（CSS）和 Enhanced Feature（EF）四个模块。CFA 分别聚合浅层与深层特征，GFA 构建多层统一全局表示，CSS 将全局语义补充到两条分支，EF 强化目标区域并抑制背景噪声。

## 实验与结果

作者在六个公开医学图像数据集上进行实验，并与现有分割方法比较。全文报告 CC-Net 在全部评价指标上持续优于 state-of-the-art 方法；摘要没有给出统一的单一百分比，因此不额外补写未核验数字。

## 贡献与局限

贡献是把跨层级特征交互提前并贯穿分支融合过程，同时保留浅层结构和深层语义。局限是模型复杂度、不同数据集上的泛化条件以及临床工作流中的实际收益仍需更多评估。

---
DOI: 10.1016/j.neunet.2026.108950

