# Unified Table Understanding via Context-Aware Cell Embedding Learning 总结

## 基本信息
- **标题**: Unified Table Understanding via Context-Aware Cell Embedding Learning
- **作者**: Willy Carlos Tchuitcheu、Tan Lu、Arthur Van Beersel 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(11)，7830-7840
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3731233
- **PDF**: [TKDE_2026_unified_context_aware_table_embeddings_3731233.pdf](papers/TKDE_2026_unified_context_aware_table_embeddings_3731233.pdf)
- **开放许可**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) · 出版社原件，未经修改

## 一句话概括
表格若被压平成文本，单元格值的行列语境容易丢失，也难形成可跨任务复用的表示。UTUEL 通过上下文感知单元格嵌入，在一次学习后支持问答、表检索、列类型标注和单元格检索。

## 问题与动机
能否学习一次表格表示，并在不同理解任务中复用而无需为每项任务重新训练？

## 方法
框架以语义元路径编码单元格及行列上下文，采用联合嵌入预测架构训练编码器和预测器；单元格表示可池化到列或整表，供多类任务调用。

## 实验与结果
在新基准及大规模数据集上评估；WikiSQL-Lookup 含 11,324 个查询、4,242 张表，UTUEL 表示可无重训迁移到表检索，并在检索上优于通用嵌入器，同时在列类型标注和单元格检索保持竞争力（PDF 第 8–10 页）。编码器为 2.9–11.8M 参数，但复杂比较或聚合查询仍较难。

## 贡献与局限
贡献是可复用的上下文单元格表示及跨任务评估，模型规模小于所比较的大型基线。证据依赖特定基准与嵌入器；摘要所述跨任务竞争力不意味着复杂表格推理已解决。

---
DOI: 10.1109/tkde.2026.3731233 | PDF: [TKDE_2026_unified_context_aware_table_embeddings_3731233.pdf](papers/TKDE_2026_unified_context_aware_table_embeddings_3731233.pdf)
