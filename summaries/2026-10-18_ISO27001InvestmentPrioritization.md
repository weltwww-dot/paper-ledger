# Prioritizing selected ISO/IEC 27001 implementation investment items using multi-criteria decision analysis 总结

## 基本信息
- **标题**: Prioritizing selected ISO/IEC 27001 implementation investment items using multi-criteria decision analysis
- **作者**: Sadrettin Çodur、Fatih Tiryaki
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25:177
- **发表**: 2026-10-18
- **日期来源**: Crossref published-online；录用日期2026-10-10不替代在线发表日
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01347-6
- **PDF**: [IJIS_2026_ISO27001InvestmentPrioritization.pdf](papers/IJIS_2026_ISO27001InvestmentPrioritization.pdf)

## 一句话概括
用专家排序和多准则决策分析，为资源受限组织筛选ISO/IEC 27001实施初期应优先关注的投资事项。

## 问题与动机
组织往往无法同时投入所有安全建设事项，需要把有限资源分配给更紧迫的项目。论文研究的是选定投资项的规划优先级，不是对标准全部控制措施作普遍排序。

## 方法
邀请10位信息安全与IT专业人士，对10个投资领域及适用性声明（SoA）共11项排序，允许并列。RANCOM将序位判断转为比较矩阵并归一化权重，再用Copeland、PageRank交叉核对，并逐次剔除一位专家检验排序稳定性。

## 实验与结果
三种方法均把服务器机房、系统冗余与备份、灾难恢复中心排在前三；RANCOM权重分别为0.1669、0.1554、0.1372。留一专家分析中，排序与基线的Spearman相关系数为0.9269—0.9977，前三项及前五名总体稳定，中低位则存在方法差异与接近的权重（PDF第8—10页，表3—5）。这些结果衡量专家偏好及排序稳定性，不是安全效能实测。

## 贡献与局限
提供可复核的专家决策流程，并用不同聚合方法及敏感性分析降低单一排序方法的影响。样本仅10位专家，未直接测量成本、风险降低或实施后绩效，也未建模项目依赖；具体投入顺序仍须结合行业、基础设施和组织风险调整，不能将稳定排序等同于更高安全收益（PDF第11—12页）。

---
DOI: 10.1007/s10207-026-01347-6 | PDF: [IJIS_2026_ISO27001InvestmentPrioritization.pdf](papers/IJIS_2026_ISO27001InvestmentPrioritization.pdf)
