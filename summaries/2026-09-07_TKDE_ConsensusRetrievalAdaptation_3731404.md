# Consensus-Guided Multi-Match Adaptation With Uncertainty-Calibrated Thresholding for Test-Time Cross-Modal Retrieval 总结

## 基本信息
- **标题**: Consensus-Guided Multi-Match Adaptation With Uncertainty-Calibrated Thresholding for Test-Time Cross-Modal Retrieval
- **作者**: Yuanpeng He、Chung-Ju Huang、Lijian Li 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8024-8041
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3731404

## 一句话概括
在目标域图文检索中用多个候选匹配形成共识，缓解测试时分布变化带来的性能下降。

## 问题与动机
检索需要保留图文之间细粒度、双向的相似关系。分类式测试时适应通常只生成单个伪标签，容易把噪声匹配固化。

## 方法
作者汇总多个高置信候选作为学习信号，再按匹配不确定性筛选更新对象。适应阶段仅更新偏置，降低对预训练表征的改动。

## 实验与结果
论文按图像到文本和文本到图像两个方向报告检索效果，比较分布变化和模态质量下降下的表现。共识匹配和置信筛选共同帮助保留原有图文相似结构（PDF 第 1、6 页）。

## 贡献与局限
框架把测试时适应落实到样本间匹配。效果取决于初始检索器能否提供足够可信的候选，目标域缺少有效匹配时更新更困难。

---
DOI: 10.1109/tkde.2026.3731404
