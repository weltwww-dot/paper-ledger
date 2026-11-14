# Inductive Message Passing Over Hypergraph for Large-Scale Knowledge Graph Completion 总结

## 基本信息
- **标题**: Inductive Message Passing Over Hypergraph for Large-Scale Knowledge Graph Completion
- **作者**: Yufeng Zhang、Wei Chen、Weiqing Wang 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8293-8307
- **发表**: 2026-09-22
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3736411

## 一句话概括
真实知识图谱会出现新实体和新关系，且新旧图之间的桥接链接可能缺失。既有归纳补全工作常只预测新图内部链接，忽略跨图桥接关系；ImBridge 以关系超图传递信息，面向这类更完整的动态图谱场景。

## 问题与动机
当新实体、新关系同时出现且新旧知识图谱断连时，如何推断图内链接及连接原图与新图的桥接链接？

## 方法
关系超图构造模块把实体与关系组织为超边，并以 GraphTrans 建模超边间交互；超关系消息传递模块先表示已有实体和关系，再聚合其信息生成新元素表示。作者在三个公开知识图谱构造九种新关系比例设置，并另测公共归纳基准。

## 实验与结果
在 FB15k-237、NELL-995、YAGO3-10 构造的九个设置中，ImBridge 总体优于比较方法，尤其改善含未见关系的桥接链接预测（PDF 第 9–10 页）。但桥接链接仍比新图内部链接更难；大规模图基础模型的预训练成本高，本文构造设置也未覆盖所有真实动态图谱。

## 贡献与局限
贡献是将桥接链接和未见关系纳入同一归纳知识图谱补全框架，并用关系超图缓解原图与新图断连造成的信息缺口。局限是评估主要依赖人工构造的基准切分，跨领域真实图谱的长期演化表现仍待验证。

---
DOI: 10.1109/tkde.2026.3736411
