# Disk-Resident Vector Similarity Search: A Survey 总结

## 基本信息
- **标题**: Disk-Resident Vector Similarity Search: A Survey
- **作者**: Yitong Song、Huiling Li、Zheng Wu 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8118-8137
- **发表**: 2026-09-07
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3731393
- **PDF**: [TKDE_2026_disk_resident_vector_search_survey_3731393.pdf](papers/TKDE_2026_disk_resident_vector_search_survey_3731393.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
向量规模增长和内存成本推动相似度检索转向磁盘驻留，但块布局、随机 I/O 与动态更新使其设计不同于内存索引。本文系统梳理磁盘向量检索，将方法归纳为 IVF、图和树三类，并总结查询、维护与开放问题。

## 问题与动机
磁盘驻留向量检索有哪些索引设计取舍，现有方法在查询、更新和存储硬件变化下还缺什么？

## 方法
综述按索引结构分类，进一步整理构建、块感知布局、查询执行、更新维护及常用数据集；同时定义 ANN、范围检索和过滤 ANN 等任务，并计算数据集难度指标。

## 实验与结果
这是技术综述而非新算法对照实验；作者用统一工具计算常见数据集的相对对比度等难度指标，并据此指出数据集难度差异会影响基准可比性（PDF 第 16 页）。综述指出既有工作多针对本地 SSD，云存储、混合查询与持续更新仍缺统一方案（PDF 第 17 页）。覆盖范围受纳入文献及数据集所限，分类也不等同于独立性能验证。

## 贡献与局限
提供磁盘驻留向量检索的统一分类框架，并将索引结构与布局、I/O 查询、维护机制联系起来，整理可复现评测资源和研究方向。其证据是文献综合而非系统新实验，结论可能随硬件与后续研究变化。

---
DOI: 10.1109/tkde.2026.3731393 | PDF: [TKDE_2026_disk_resident_vector_search_survey_3731393.pdf](papers/TKDE_2026_disk_resident_vector_search_survey_3731393.pdf)
