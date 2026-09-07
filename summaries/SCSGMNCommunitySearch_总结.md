# Self-Supervised Similar Community Search Based on Graph Matching Network 总结

## 基本信息

- **标题**: Self-Supervised Similar Community Search Based on Graph Matching Network
- **作者**: Runhuai Chen, Yuxiang Wang, Tianxing Wu, Zhiyuan Yu, Xiaoliang Xu, Xiangyu Ke, Yuanshi Zheng
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-06-29
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 图数据分析与检索
- **DOI**: 10.1109/TKDE.2026.3707934
- **arXiv**: 无
- **PDF**: [TKDE_2026_SCSGMNCommunitySearch.pdf](papers/TKDE_2026_SCSGMNCommunitySearch.pdf)

## 一句话概括

SCS-GMN 用社区凝聚性、规模和密度定义统一相似度，通过相似度引导的自监督图匹配同时学习节点和结构特征，实现快速的相似社区搜索。

## 问题与动机

相似社区搜索要在信息网络中找到与查询社区相似的结果社区，可用于社交营销、推荐和网络分析。已有神经子图匹配或图对齐方法缺少有效的社区级相似度定义，过度依赖节点属性，忽略结构对应关系；同时，高质量人工标注社区稀缺，限制了监督训练。论文希望以无标签方式学习可迁移的社区匹配表示。

## 方法

作者提出融合社区凝聚性、规模和密度的统一相似度指标，作为训练信号衡量查询社区与结果社区的整体匹配程度。SCS-GMN 基于图匹配网络，通过相似度引导的自监督学习联合对齐节点特征和结构特征；面向大图，进一步采用候选子图生成和图匹配 Transformer，先筛选潜在候选，再完成精细匹配。

## 实验与结果

在 7 个真实数据集上的实验显示，SCS-GMN 返回社区的平均相似度达到 96.65%，平均查询时间约 64.5 ms。相较次优方法，社区相似度提高 14.61%，推理速度约提升 2 倍；结果说明，加入结构匹配和自监督信号能够减少节点特征缺失导致的匹配失败，并适应较大信息网络。

## 贡献与局限

论文贡献了社区级多指标相似度、自监督图匹配模型以及面向大图的候选生成流程，减少了对人工社区标注的依赖。局限在于社区定义、候选规模和相似度权重会影响结果，实验网络主要来自已有数据集；动态图社区、异构图、对抗性节点属性和超大规模在线搜索仍需进一步验证。

---
DOI: 10.1109/TKDE.2026.3707934
