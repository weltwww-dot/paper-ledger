# Energy-preserving shifted bipartite graph learning for unpaired large-scale multi-view clustering 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Energy-preserving shifted bipartite graph learning for unpaired large-scale multi-view clustering
- 作者：Xingfeng Li, Jiawei Peng, Zhongwen Wang, et al.
- 期刊 / 年份：Neural Networks / 2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108952
- PDF：[ESBGLMultiViewClustering.pdf](papers/ESBGLMultiViewClustering.pdf)

## 一句话概括

论文提出 ESBGL，通过锚点对齐、二部图对齐和能量保持的 shifted learning，解决完全未配对的大规模多视图聚类问题。

## 问题与动机

许多 anchor-based 多视图聚类方法假设不同视图的样本完全配对，但异步采集、传输丢失和时空差异会破坏这种对应关系。未配对数据还会造成跨视图锚点数量不平衡、分布不公平和顺序错乱，使二部图结构难以融合；已有方法也常有较高的时间或空间复杂度。

## 方法

ESBGL先利用先验锚点图监督无监督锚点学习，使不同视图的锚点在数量、分布和顺序上更一致；再以最佳视图为参照，用旋转矩阵对齐各视图二部图，并按重构损失加权形成共识图。最后构造 shifted Laplacian，把原本位于大特征值端的重要能量信息转移到用于聚类的小特征值端，从而同时保留聚类结构和显著能量。

## 实验与结果

论文在 Mnist、MSRCv1、YTF100、YTF20、YTF10、Animal 和 RGBD 等数据集上，与浅层、anchor-based 和深度方法比较。ESBGL在多项 ACC、NMI、PUR 和 F-score 指标上取得最佳或竞争性结果；例如在 Mnist* 上 ACC/NMI/PUR/F-score 为 87.55/76.21/87.55/78.99，在 Animal* 和 RGBD* 上 ACC 分别为 34.37 和 43.93。复杂度分析给出 ESBGL 约为 O(vn) 的内存和时间成本，明显低于对比的 O(vn²) 内存及 O(3vn³+n³) 时间方案。

## 贡献与局限

论文贡献了面向完全未配对多视图数据的锚点监督对齐机制、共识二部图学习框架及能量保持的 shifted 学习范式，并通过实验验证了性能和效率。局限在于实验主要覆盖文中选定的数据集与未配对设置，对更复杂缺失模式、极端视图异步性和参数敏感性的泛化仍需进一步验证。

DOI: 10.1016/j.neunet.2026.108952
