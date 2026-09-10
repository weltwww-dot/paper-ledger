# Efficient Structure-Aware Discrete Clustering via Multi-Order Anchor Graphs

## 基本信息

- **标题**: Efficient Structure-Aware Discrete Clustering via Multi-Order Anchor Graphs
- **作者**：Ben Yang、Xuetao Zhang、Yu Zhou、Haoxin Wu、Feiping Nie、Badong Chen
- **期刊 / 会议**：IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：数据工程
- **DOI**：10.1109/tkde.2026.3700798
- **arXiv**：无
- **PDF**：[TKDE_2026_EfficientStructureAwareDiscrete.pdf](papers/TKDE_2026_EfficientStructureAwareDiscrete.pdf)

## 一句话概括

本文提出 ESADC 多阶锚图离散聚类方法，通过融合不同阶次的样本—锚点图并直接优化离散聚类指示矩阵，在不进行特征值分解的情况下兼顾结构表达能力和计算效率。

## 问题与动机

锚图能把大规模聚类中的样本关系压缩到少量锚点，但单一阶次的图难以同时表达局部邻域和更高阶结构；传统谱聚类还需要特征值分解，计算和存储成本较高。论文希望利用多阶图传播补充结构信息，并将图学习、图融合和离散聚类放进一个直接优化框架，以减少中间连续松弛带来的额外开销。

## 方法

ESADC 先构造稀疏样本—锚点亲和矩阵 `A`，再用 `B^(v)=A(AᵀA)^(v−1)` 生成不同阶次的关系图。模型学习各阶图的融合权重，将融合后的样本图与归一化的一热聚类指示矩阵对齐，并通过正交旋转矩阵 `H` 处理离散指示与图结构之间的对应关系。优化变量包括图表示、聚类指示和阶次权重，采用快速坐标下降/交替最小化求解，避免特征值分解。锚点由 10 次随机初始化的 K-means 生成并取平均，以改善结果稳定性。

## 实验与结果

实验覆盖 Derma、Control、CoraOS、NUS、CoraHA、SearchSP、Biomedical 和 StackOF 八个数据集，使用 ACC、NMI、Purity、ARI 和 F-score 评价。ESADC 在 Derma 上 ACC 为 97.71、ARI 为 93.29，在 Control 上 ACC 为 96.04，在 CoraOS 上 ACC 为 53.61，在 CoraHA 上 ACC 为 49.00；相较代表性对比方法，多个数据集同时取得更高聚类质量。运行时间方面，Derma 和 Control 仅约 0.0206 s 和 0.0225 s，NUS 约 0.3114 s；在较大数据集上仍保持较短或有竞争力的时间。阶次实验表明 `V=3` 通常最优，阶次过高会产生过度平滑。

## 贡献与局限

论文把多阶锚图、可学习融合和离散聚类统一起来，在避免谱分解的同时提升了若干数据集上的聚类精度和速度，并通过阶次消融与运行时间实验解释了设计选择。局限在于方法主要依赖图亲和关系；当数据结构弱、关系含义模糊或缺少语义/上下文信息时，图融合可能无法充分区分簇。后续可引入任务驱动的图构造、多视图信息和半监督约束，并进一步研究超大规模场景下的内存和并行实现。

---
DOI: 10.1109/tkde.2026.3700798
