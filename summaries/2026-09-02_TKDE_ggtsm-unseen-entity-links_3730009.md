# Adaptive Knowledge Distillation With GCN–GAT Teacher–Student Models for Link Prediction on Out of Entity Triples 总结

## 基本信息
- **标题**: Adaptive Knowledge Distillation With GCN–GAT Teacher–Student Models for Link Prediction on Out of Entity Triples
- **作者**: Han Liu、Haiyan Bai、Guokai Shi 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，7929-7942
- **发表**: 2026-09-02
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3730009

## 一句话概括
GGTSM 面向知识图谱中训练时未出现实体的链接预测，采用 GCN–GAT 教师—学生蒸馏并结合子图信息，试图减轻新实体嵌入稀疏及对已知邻居的依赖。教师根据关系与节点注意力生成自适应蒸馏权重，学生再对含未见实体的三元组进行引导式推断。作者在 FB15k-237、WN18RR 和 NELL-995 上评测。

## 问题与动机
传统知识图谱嵌入通常为已见实体学习独立向量，遇到新实体时缺少训练嵌入；依靠邻居聚合的方法又会在邻接稀少时失效。论文研究如何从已有图谱结构迁移关系知识，使模型在无需外部文本特征的条件下预测含未见实体的三元组。

## 方法
GGTSM 以混合 GCN–GAT 教师学习实体和关系表示，并依据关系与节点注意力自适应加权蒸馏信号。子图模块整合局部邻接和批次结构，为新实体建立粗表示，再在教师输出指导下细化学生表示；测试协议专门构造训练未见实体的链接预测任务。

## 实验与结果
FB15k-237、WN18RR、NELL-995 三个数据集上，论文报告相对基线平均 MRR 提升0.15，Hits@1、Hits@3、Hits@10 分别平均提升18%、41%、63%（PDF 第1页、第5–10页）。参数量约为2.38M、4.99M、6.23M；论文指出部分子图缓存等非训练结构未计入，且训练时间高于部分基线（PDF 第12页）。

## 贡献与局限
工作将自适应蒸馏、图卷积/注意力和子图初始化用于开放实体链接预测，并报告多个基准上的指标改善。评估依赖特定静态数据集划分，不能充分代表真实知识图谱的持续时间演化；模型开销统计未覆盖全部非参数缓存，新实体几乎无结构信息时仍受可用关系上下文限制。

---
DOI: 10.1109/tkde.2026.3730009
