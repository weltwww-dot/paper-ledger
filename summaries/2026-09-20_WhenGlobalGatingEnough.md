# When global gating is enough: Admission-time hubness control in anisotropic vector retrieval systems 总结

## 基本信息
- **标题**: When global gating is enough: Admission-time hubness control in anisotropic vector retrieval systems
- **作者**: Prashant Kumar Pathak、Tarun Kumar Sharma
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-20
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105178
- **PDF**: [COSE_2026_GlobalGatingHubness.pdf](papers/COSE_2026_GlobalGatingHubness.pdf)

## 一句话概括
本文提出在文档写入向量库时，以少量哨兵查询执行全局准入门控，阻止恶意文档利用向量枢纽性反复进入 RAG 检索结果。

## 问题与动机
高维嵌入中，少数向量可能成为大量查询的近邻；攻击者可构造与广泛查询都相似的文档污染 RAG 上下文。周期性扫描会留下暴露窗口，并需反复遍历整个语料，因此作者转向逐条写入时检查。

## 方法
作者比较候选文档嵌入与一组哨兵查询，以全局阈值判断其是否具有异常广泛的可检索性。评估覆盖 10 万篇 BEIR 文档、不同编码器及 HNSW 索引，并比较全局与领域专用门控。

## 实验与结果
所测设置下，攻击召回率为 1.00、AUROC 约为 1.00，良性自然枢纽误报约 1%。领域专用阈值未带来明显收益；加入 HNSW 的索引构建开销约增 3.1%，约 1.2% 的索引决策改变。梯度优化攻击的召回率为 0.91±0.07。

## 贡献与局限
- 将防护从周期性审计转为增量准入控制，减少随语料规模增长的全库扫描。
- 结果支持在所测语料与编码器下采用单一全局门控。
- 研究局限于选定数据与单向量表示；自然产生的高枢纽文档可能被误拦，实际部署仍需来源溯源与复核。

---
DOI: 10.1016/j.cose.2026.105178
