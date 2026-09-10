# A Low-Rank Perspective on Similarity Matrix Completion 总结

## 基本信息

- **标题**: A Low-Rank Perspective on Similarity Matrix Completion
- **作者**: Changyi Ma, RunSheng Yu, Xiao Chen, Youzhi Zhang, Zhen Lei
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026年
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TKDE.2026.3702548
- **arXiv**: 无
- **PDF**: [TKDE_2026_LowRankPerspectiveSimilarity.pdf](papers/TKDE_2026_LowRankPerspectiveSimilarity.pdf)

## 一句话概括

论文提出融合对称性、半正定性和低秩性的相似度矩阵补全框架，通过因子化和新型低秩正则项，在不完整数据上同时提升相似度估计精度与检索效率。

## 问题与动机

真实信息检索中的特征缺失会造成相似度矩阵不完整，进而影响检索排序和下游任务。传统相似度矩阵补全方法主要利用半正定约束，面对规模大、缺失率高的数据时可能计算昂贵，也不能充分利用相似度矩阵的低秩结构。论文因此关注如何在保留有效相似度关系的同时降低补全成本并给出理论保证。

## 方法

作者构建同时满足对称、半正定和低秩属性的相似度矩阵补全框架，引入专门的Cholesky因子化技术，以学习较小的因子矩阵而不是完整相似度矩阵。为加强最优性保证，论文提出新的“更低秩”矩阵性质，并设计相应正则项。基于这些设计，作者给出SMCFN和SMCRN两种算法，分别采用Frobenius范数及逐行Frobenius范数形式，并证明估计保证、无伪局部极小点以及算法收敛等性质。

## 实验与结果

实验在ImageNet（1200万样本、1000维）、MNIST（6万样本、784维）、CIFAR-10（6万样本、1024维）、PROTEIN（2.3万样本、357维）和GoogleNews（300万词、300维）上进行，与多类缺失数据插补、矩阵补全和相似度矩阵补全方法比较。以RMSE、Recall@top20%和nDCG@top20%评估时，SMCFN/SMCRN在五个数据集上取得一致的补全和检索优势；摘要报告其相对现有方法最高可降低42% RMSE、提高15% Recall，并保持最高效率。实验还验证了低秩性质，且运行时间随缺失率变化时优于比较方法。

## 贡献与局限

主要贡献是把低秩因子化、半正定约束和相似度检索任务统一起来，并以理论与实验证明SMCFN/SMCRN的精度和效率。局限是大规模数据上截断SVD和核范数最小化仍可能带来较高计算开销；作者将开发更简单高效的SVD近似方法列为未来工作，当前实验也主要覆盖五个公开数据集。

---
DOI: 10.1109/TKDE.2026.3702548
