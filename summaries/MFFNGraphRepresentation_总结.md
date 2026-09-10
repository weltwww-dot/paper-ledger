# Beyond pairwise dependence: A multi-filter fusion network for graph representation learning 总结

## 基本信息

- **标题**: Beyond pairwise dependence: A multi-filter fusion network for graph representation learning
- **作者**: Hui Yan, Ling Guo, Guoguo Ai, Xin Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108906
- **arXiv**: 无
- **PDF**: [NN_2026_MFFNGraphRepresentation.pdf](papers/NN_2026_MFFNGraphRepresentation.pdf)

## 一句话概括

MFFN用不同阶邻接/拉普拉斯结构上的Fourier展开和语义自适应掩码学习多种图谱滤波器，突破传统成对依赖。

## 问题与动机

多项式图滤波器通常依赖成对网络结构，高阶多项式又可能导致过平滑、过挤压或记忆训练图的一阶拉普拉斯而过拟合。需要表达高阶关系并适应复杂图信号的谱滤波机制。

## 方法

MFFN在不同阶关联的拉普拉斯矩阵上进行Fourier展开，用单纯形复形编码特征值，建立不同阶之间的交互。随后以Fourier基近似多个谱滤波器，并通过语义自适应mask按图信号选择合适响应。

## 实验与结果

实验包括滤波器拟合、节点分类和图分类。结果表明MFFN能够学习任意图谱滤波器，并在节点级与图级分类任务中取得优于对比方法的性能。

## 贡献与局限

贡献是把高阶单纯形结构、Fourier滤波器融合和语义自适应选择统一起来。局限是多阶矩阵和多滤波器会增加存储与计算，作者也指出后续需要进一步提升MFFN效率。

---
DOI: 10.1016/j.neunet.2026.108906
