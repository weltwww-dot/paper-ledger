# Mutual information-guided dynamic cross-view graph learning for robust multi-view clustering 总结

## 基本信息
- **标题**: Mutual information-guided dynamic cross-view graph learning for robust multi-view clustering
- **作者**: Tingting Chen、Yijian Fu、Zinan Peng 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109871
- **发表**: 2026-11-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109871

## 一句话概括
MIGDCGL结合动态构图、图传播前的跨视图交互与互信息可靠性加权，改善低质量视图干扰下的多视图聚类。

## 问题与动机
多视图聚类既要利用互补信息，又要避免噪声视图拖累融合表示。固定邻接图容易保留错误连接，独立编码后再融合又使视图交互不足；一味强化一致性还可能压制各视图的判别信息。

## 方法
方法在变换后的特征空间动态构图，以视图专属相似度阈值过滤连接；图卷积前注入自适应加权的共享上下文。随后用各视图与全局表示之间的经验互信息调节对比损失，并结合K-means硬分配和DDC聚类正则，交替更新表示、图与聚类分配。

## 实验与结果
在十二个基准数据集上与七种方法比较，报告十次独立运行的ACC、NMI和纯度均值。Yale的ACC为0.8424，高于最强基线MVCformer的0.7815；Caltech五视图ACC为0.9643，高于DFP-GNN的0.9457。但Fashion及Caltech三、四视图未全面领先，消融和高斯特征噪声实验进一步检验组件作用。

## 贡献与局限
贡献在于把可靠构图、早期信息交换和可靠性加权对齐纳入统一优化。局限是大规模样本图的时间与内存成本，互信息受离散化及视图自贡献影响；鲁棒性仅验证完整视图下的合成高斯扰动，尚不能外推到缺失视图或结构化噪声。

---
DOI: 10.1016/j.neunet.2026.109871
