# Intrusion detection datasets for Cyber-Physical Systems: Taxonomy, challenges, and opportunities 总结

## 基本信息
- **标题**: Intrusion detection datasets for Cyber-Physical Systems: Taxonomy, challenges, and opportunities
- **作者**: Vagner E. Quincozes、Silvio E. Quincozes、Célio Albuquerque、Diego Passos、Daniel Mossé
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105217
- **发表**: 2026-10-24
- **日期来源**: 出版社正式PDF首页Available online；2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105217
- **PDF**: [COSE_2026_CPSIntrusionDatasetTaxonomy.pdf](papers/COSE_2026_CPSIntrusionDatasetTaxonomy.pdf)

## 一句话概括
建立信息物理系统入侵检测数据集的分类体系，并用统一实验检查攻击分布、网络与物理特征及数据集局限对检测评价的影响。

## 问题与动机
传统IT数据难以表示水务、电网和工业过程的物理约束；数据集按场景定制、攻击不均衡和文档不足，使高准确率难以跨研究比较。

## 方法
按应用场景、攻击类别、特征类型、采集来源及物理组件梳理数据集；通过SEF-CPS框架在七个公开数据集上比较随机森林、决策树和XGBoost，并用宏平均指标和SHAP补充分析。

## 实验与结果
表6中BATADAL三个模型的准确率约0.80—0.82，宏平均F1却仅0.51—0.56；只有少量特征的Laso宏平均F1为0.46—0.48。这些差异说明类别失衡和特征覆盖会掩盖在整体准确率之下，不能只按单一高分评价数据质量（PDF第11—15页，表6—8）。

## 贡献与局限
贡献是可复用的数据集描述、比较与缺口诊断框架，并非提出新检测器或新采集数据集。实验限于七个基准和三类树模型，未直接验证跨系统迁移或真实部署效果；特征扩充、数据增强和更复杂攻击覆盖主要作为后续方向提出（PDF第12、16页）。

---
DOI: 10.1016/j.cose.2026.105217 | PDF: [COSE_2026_CPSIntrusionDatasetTaxonomy.pdf](papers/COSE_2026_CPSIntrusionDatasetTaxonomy.pdf)
