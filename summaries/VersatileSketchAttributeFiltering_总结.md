# Versatile Sketch-Based Attribute Filtering for Hybrid Vector Search 总结

## 基本信息

- **标题**: Versatile Sketch-Based Attribute Filtering for Hybrid Vector Search
- **作者**: Adeel Aslam、Luca Gagliardelli、El Kindi Rezig、George Konstantinidis、Giovanni Simonini
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/tkde.2026.3709125
- **arXiv**: 无
- **PDF**: [TKDE_2026_VersatileSketchAttributeFiltering.pdf](papers/TKDE_2026_VersatileSketchAttributeFiltering.pdf)

## 一句话概括

本文提出一种基于属性流行度和轻量内存草图的混合向量检索方法，在不为每个属性重复建图的前提下，动态选择一跳或两跳 HNSW 搜索以兼顾召回率和查询吞吐。

## 问题与动机

混合向量检索需要同时满足向量相似度和属性谓词条件，例如按类别、数值范围或标签过滤后再返回近邻。单独使用与属性无关的 ANN 索引容易在后过滤时漏掉满足谓词的近邻；为每个属性或范围复制索引又会造成巨大的空间与维护成本。作者希望利用同一套向量图结构处理不同属性和谓词，并根据查询条件的选择性决定何时扩大搜索范围。

## 方法

方法首先在 HNSW 底层图上对节点进行聚类，并为各簇建立轻量的属性统计草图。点谓词使用 Count-Min Sketch 估计属性流行度，范围谓词使用基于累积分布的回归模型进行预测。查询时先定位向量近邻及其所属簇，再依据目标属性在该簇中的流行度决定是否执行两跳遍历；必要时才扩大候选集合，最后进行谓词过滤。该设计不依赖具体属性或谓词，能够与默认 HNSW 索引兼容。

## 实验与结果

实验在五个不同领域的真实数据集上进行，并与 ACORN、NaviX、HNSW 后过滤、两跳后过滤、IRange Graph 和 UNG 等方法比较。在 TripClick 点谓词查询中，预测方法可在 99% 召回率下达到约 3 倍于 ACORN-1 的吞吐；在 YouTube、BEIR 等数据上，交集预测版本相对 ACORN-1 获得约 3–4.4 倍加速。范围查询中，方法在 YouTube 音频嵌入上以 99% 召回率达到 237 QPS，并在正相关查询上达到 99.9% 召回率和 839 QPS；统一设置下，相比动态预测器通常获得更高召回率和 1.7–2.6 倍加速。

## 贡献与局限

- 将 HNSW 图聚类、属性流行度草图和自适应两跳搜索结合，避免针对每个属性建立独立索引。
- 同时支持点谓词和范围谓词，并在低选择性查询中改善 ANN 搜索的召回率—吞吐折中。
- 在五个真实数据集和多种属性选择性、向量相关性条件下，展示出相对现有谓词无关方法的速度和召回优势。
- 局限：性能依赖簇内属性流行度估计、查询选择性和向量—属性相关性；论文主要基于 HNSWLib 的静态索引评估，动态更新、属性分布快速变化及更复杂的联合谓词仍需要进一步验证。

---
DOI: 10.1109/tkde.2026.3709125
