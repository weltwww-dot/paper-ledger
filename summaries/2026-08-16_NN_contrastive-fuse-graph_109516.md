# Fast and featureless node representation learning with partial pairwise supervision 总结

## 基本信息
- **标题**: Fast and featureless node representation learning with partial pairwise supervision
- **作者**: Sujan Chakraborty、Saptarshi Bej
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109516
- **发表**: 2026-08-16
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109516

## 一句话概括
Contrastive FUSE将图模块度优化与部分成对监督结合，在多种规模图数据上学习节点表示，并在分类表现与计算效率之间取得折衷。

## 问题与动机
节点表示学习常需节点属性或大量监督，而大型图上的表示训练成本高，有限的成对相似与不相似标签尚未被充分利用。

## 方法
框架从图拓扑优化社区结构，以部分成对监督构造对比约束，并将结构表示与监督信号联合用于节点嵌入；节点属性不作为其嵌入学习的必要输入。

## 实验与结果
在Cora、CiteSeer、PubMed、WikiCS、Amazon Photo、ArXiv及大规模Products图上评估分类、运行时间和可扩展性；结果显示方法总体具有竞争力且开销较低，但不同下游分类器和数据集上的优势并不一致（PDF 第 5–8、11 页）。

## 贡献与局限
将全局社区结构与稀疏成对监督结合，提供不依赖节点属性的可扩展嵌入方案；监督噪声、标签稀少程度和下游模型仍会影响收益。

---
DOI: 10.1016/j.neunet.2026.109516
