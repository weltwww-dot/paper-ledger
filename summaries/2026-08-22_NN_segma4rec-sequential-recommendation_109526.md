# SeGMA4Rec: Learning stable sequential representations through semantic graph propagation and hierarchical contrastive alignment 总结

## 基本信息
- **标题**: SeGMA4Rec: Learning stable sequential representations through semantic graph propagation and hierarchical contrastive alignment
- **作者**: Wanna Cui、Hak-Keung Lam
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109526
- **发表**: 2026-08-22
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109526 | 📄 [NN_2026_segma4rec-sequential-recommendation_109526.pdf](papers/NN_2026_segma4rec-sequential-recommendation_109526.pdf)
- **PDF许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 一句话概括
SeGMA4Rec 用语义物品图补足稀疏交互，并以注意力引导视图增强和多层对比对齐稳定序列推荐表示。

## 问题与动机
短而稀疏的交互序列难以形成可靠用户表示；随机增强可能删掉关键行为，常见对比目标只约束最终层，交互图也难连接从未共现但语义相关的物品。

## 方法
从预训练文本嵌入构建物品语义图，并按推荐目标自适应修正边权传播关系；序列编码器注意力引导概率式视图采样以保留重要交互，再通过多层级对比目标对齐增强视图与编码层。

## 实验与结果
在四个基准数据集评估并与序列推荐方法比较，多数设置报告统计显著提升；还测试不同骨干的泛化。Beauty 数据上 GRU4Rec 加方法后 NDCG@10/Recall@10 从 0.0150/0.0284 升至 0.0313/0.0615；BERT4Rec 对应从 0.0300/0.0601 升至 0.0433/0.0825。

## 贡献与局限
把全局语义关系和序列级层次约束结合，避免仅靠随机删减行为或最终层对比。局限包括依赖预训练文本语义图，以及深层编码器上的对齐行为尚未充分探索；推荐离线指标不等同在线业务收益。

---
DOI: 10.1016/j.neunet.2026.109526 | 📄 [NN_2026_segma4rec-sequential-recommendation_109526.pdf](papers/NN_2026_segma4rec-sequential-recommendation_109526.pdf)
