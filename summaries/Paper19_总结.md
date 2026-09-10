# Bi-directional attention network with drop aggregation for microRNA-disease association prediction 总结

## 基本信息

- **标题**: Bi-directional attention network with drop aggregation for microRNA-disease association prediction
- **作者**: Yan-Fang Yang、Yue Gao、Ming-Li Cui、Ying-Lian Gao、Yan-Li Wang、Jin-Xing Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108942
- **arXiv**: 无
- **PDF**: [NN_2026_BADMDA_MicroRNADiseaseAssociation.pdf](papers/NN_2026_BADMDA_MicroRNADiseaseAssociation.pdf)

## 一句话概括

BADMDA 通过多核自适应融合、DropAGG 和双向注意力预测潜在 microRNA–疾病关联。

## 问题与动机

发现 microRNA 与疾病的潜在关系有助于理解病理机制和药物研发。现有模型对异构生物资源利用不足，特征提取简单，难以表达 miRNA 与疾病之间的复杂非线性关系。研究希望融合多源相似性并减轻图表示过平滑。

## 方法

CKA-MKL 自适应学习不同相似性核的权重，构建带属性的 miRNA–疾病二部图。DropAGG 学习多层特征并缓解过平滑，双向注意力捕捉疾病与 miRNA 的相互依赖，最后用多层感知器推断新关联。

## 实验与结果

在 HMDD v2.0 和 HMDD v3.2 上，BADMDA 的 AUC 分别为 0.9372 和 0.9533，AUPR 分别为 0.9348 和 0.9525，并超过十种先进方法。肺部肿瘤和肝细胞癌案例分析进一步支持其生物学相关性。

## 贡献与局限

贡献是将异构相似性自适应融合、图聚合和双向注意力整合到关联预测中。局限是预测质量依赖 HMDD 标注和相似性构造，案例验证不能等同于实验生物学确认，潜在关联仍需外部实验验证。

---
DOI: 10.1016/j.neunet.2026.108942
