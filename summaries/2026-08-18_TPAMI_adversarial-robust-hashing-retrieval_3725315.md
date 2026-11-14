# Deep Supervised Adversarial Robust Hashing for Retrieval 总结

## 基本信息
- **标题**: Deep Supervised Adversarial Robust Hashing for Retrieval
- **作者**: Xingwei Zhang、Gang Zhou、Xiaolong Zheng 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15665-15682
- **发表**: 2026-08-18
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3725315

## 一句话概括
DSARH 将相似度监督与哈希码纳入端到端对抗训练，提升深度哈希检索在受扰输入下的鲁棒性。

## 问题与动机
深度哈希能高效支持跨模态和图像检索，但其对抗鲁棒性研究少于分类任务；检索通常依赖样本相似度矩阵而非显式类别标签，直接迁移分类式防御并不合适。论文探索如何利用检索自身的语义关系训练更稳定的哈希表示。

## 方法
框架用样本间语义相似性训练哈希表示，将抗扰训练纳入单模态和跨模态检索的优化。评估同时关注排序准确性和扰动下的稳定性。

## 实验与结果
作者在 Wikipedia、MIRFLICKR25K、NUS-WIDE、MS-COCO 等跨模态基准，以及 NUS-WIDE、MS-COCO 图像检索上，与深度哈希基线比较标准和鲁棒 mAP。DSARH 在多种检索相关和迁移评估下总体提升鲁棒性，跨模态标准检索也有改善；但 OOD 图像扰动（高斯噪声除外）收益有限，跨数据集鲁棒性亦未得到稳定改善（PDF 第12–14页）。

## 贡献与局限
论文说明检索专用的鲁棒训练可帮助稳定哈希表示，并观察到图文对齐方面的收益。训练成本有所增加，鲁棒性证据主要来自设定的有界扰动（PDF 第 15–16 页）。

---
DOI: 10.1109/tpami.2026.3725315
