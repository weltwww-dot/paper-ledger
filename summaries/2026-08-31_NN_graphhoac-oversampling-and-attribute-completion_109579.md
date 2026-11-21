# Heterogeneous graph neural networks via oversampling and attribute completion 总结

## 基本信息
- **标题**: Heterogeneous graph neural networks via oversampling and attribute completion
- **作者**: Huibo Liu、De Hu、Yan Zhang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109579
- **发表**: 2026-08-31
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109579

## 一句话概括
GraphHOAC将高阶拓扑过采样与自监督属性补全结合，缓解异构图中节点类型数量失衡和属性缺失共同造成的表示偏差。

## 问题与动机
异构图中稀少的节点类型可能提供关键语义，却在多数类型主导的消息传播中被淹没；若同时缺失属性，单独做补全或均衡采样难以消除这种交互偏差。

## 方法
先用metapath2vec获取拓扑嵌入，从一阶相似邻居与符合类型约束的高阶邻居中合成少数节点。随后通过带RGCN的掩码图自编码器学习属性，并用拓扑引导的注意力补全缺失表示；MAGNN整合表示，以属性、边重构和预测损失联合优化。

## 实验与结果
在ACM、DBLP、IMDB上进行节点分类和聚类，各组实验重复5次。ACM训练比例10%时，Macro-F1为95.21%，HeGAE-AC为93.17%，高2.04个百分点；ACM聚类ARI为0.7712，对应基线为0.7430。过采样和补全模块消融总体支持联合建模。

## 贡献与局限
贡献是面向属性缺失图显式处理跨节点类型的不均衡，并提供可插入补全模型的均衡模块。优势并非覆盖所有设置：DBLP低训练比例下的Macro-F1落后于HeGAE-AC；数据集规模描述存在内部差异，且复杂度包含节点数平方项，大图扩展能力仍需验证。

---
DOI: 10.1016/j.neunet.2026.109579
