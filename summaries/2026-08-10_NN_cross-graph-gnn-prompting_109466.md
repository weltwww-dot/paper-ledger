# A cross-graph tuning-free GNN prompting framework 总结

## 基本信息
- **标题**: A cross-graph tuning-free GNN prompting framework
- **作者**: Yaqi Chen、Shixun Huang、Lei Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109466
- **发表**: 2026-08-10
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109466
- **PDF**: [NN_2026_cross-graph-gnn-prompting_109466.pdf](papers/NN_2026_cross-graph-gnn-prompting_109466.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
CTP 以自监督提示图实现无需下游调参的跨图少样本预测，在节点分类上取得显著优势，但链路预测的收益随数据集而异。

## 问题与动机
能否仅在源图上自监督预训练，使 GNN 无需目标图参数更新便迁移到未见图及不同类型的少样本节点分类和链路预测？

## 方法
框架从邻域构造伪类别，采样支持样本和查询并构建局部上下文，以提示图连接样本、查询与标签节点；结构平衡增强、标签正交约束和属性重建辅助目标共同提升表征区分度，部署时不更新模型参数。

## 实验与结果
在 arXiv 节点分类、ConceptNet、FB15K-237 与 NELL 链路预测上，与多种提示及对比基线比较；arXiv 的 3 至 40 类准确率均高于对照，链路预测则呈数据集和类别数相关的胜负变化（PDF 第7–10页）。

## 贡献与局限
将跨同质与异质图的自监督、免调参提示用于节点分类和链路预测，并通过组件消融验证示例采样、上下文构造及图学习目标的作用；当前评估覆盖的任务类型仍有限，链路预测表现并非在所有设定中领先。

---
DOI: 10.1016/j.neunet.2026.109466 | PDF: [NN_2026_cross-graph-gnn-prompting_109466.pdf](papers/NN_2026_cross-graph-gnn-prompting_109466.pdf)
