# FARCLUSS: fuzzy adaptive rebalancing and contrastive uncertainty learning for semi-supervised semantic segmentation 总结

## 基本信息
- **标题**: FARCLUSS: fuzzy adaptive rebalancing and contrastive uncertainty learning for semi-supervised semantic segmentation
- **作者**: Ebenezer Tarubinga、Jenifer Kalafatovich、Seong-Whan Lee
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109494
- **发表**: 2026-08-13
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109494

## 一句话概括
本文提出 FARCLUSS，将模糊伪标签、不确定性加权、类别重平衡与原型对比正则结合，以提高少标注语义分割对边界和少数类的利用效率。

## 问题与动机
半监督分割中的硬阈值会丢弃不确定像素，伪标签噪声和类别不均衡也会使少数类学习不足；研究关注如何保留有用的不确定监督而控制其噪声。

## 方法
采用教师—学生框架，以 top-K 软伪标签保留候选类别分布，依据像素熵动态加权，并按类别频次重平衡损失；再以高置信像素原型进行轻量对比约束。

## 实验与结果
在 Pascal VOC 与 Cityscapes 的多种标注比例上比较既有方法并做组件消融；例如 ResNet-101 的 1/8 标注设置，完整模型在 Pascal VOC 与 Cityscapes 的 mIoU 分别为 78.2 和 78.5，消融结果显示各组件均有贡献。结果来自特定数据集和半监督划分，跨场景泛化仍需验证（PDF 第 6、9–10 页）。

## 贡献与局限
研究将不确定性由筛除条件转化为软监督和动态权重，并在所测分割基准上取得有竞争力的结果；不同数据集上的最优组件权衡仍可能变化。

---
DOI: 10.1016/j.neunet.2026.109494
