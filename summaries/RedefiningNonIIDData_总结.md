# Redefining Non-IID Data in Federated Learning for Computer Vision Tasks: Migrating From Labels to Embeddings for Task-Specific Data Distributions 总结

## 基本信息

- **标题**: Redefining Non-IID Data in Federated Learning for Computer Vision Tasks: Migrating From Labels to Embeddings for Task-Specific Data Distributions
- **作者**: Kasra Borazjani, Payam Abdisarabshali, Naji Khosravan et al.
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence, 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3677838

## 一句话概括

论文指出，用标签分布偏斜模拟联邦学习 non-IID 数据并不能反映非分类视觉任务的异质性，因而提出从任务特定 embedding 出发构造数据分布的新基准。

## 问题与动机

现有 FL 研究多用 Dirichlet 分布对类别标签进行划分，这对分类任务直观有效，却无法描述深度估计、边缘检测、重着色等任务真正关注的视觉结构。相同场景标签的图像可能具有不同的任务表征，不同标签的图像也可能在某一任务看来相似，导致传统评测低估异质性对性能的影响。

## 方法

作者对每个视觉任务微调预训练 CLIP，从任务模型倒数第二层提取数据 embedding，再用 K-means 聚类，并对聚类后的数据点应用 Dirichlet 分配到 25 个客户端，形成 embedding-based data heterogeneity。研究在统一 encoder–decoder 架构下评估 FedAvg、FedProx、SCAFFOLD、FedRep 和 FedAmp，并用跨任务通用的损失指标比较影响。

## 实验与结果

实验基于 Taskonomy 的 7 个代表性视觉任务，进行 20 轮全局聚合；同时比较 class-based 与 embedding-based 划分。embedding-based 划分在非分类任务上稳定产生随异质性变化的性能差距，而标签划分通常看不出该差距；对 FedAvg，论文报告观察到的损失最高约增加 60%，且这一现象在多种 FL 方法中一致。

## 贡献与局限

论文贡献是提出面向任务视角的 embedding-based non-IID 定义、可复用的视觉 FL 基准和任务相似性分析方向，揭示传统标签基准对性能的系统性高估。局限是 embedding 提取和客户端划分在基准阶段集中完成，且实验集中于 Taskonomy 与选定模型；隐私化的分布统计、层选择、任务层级和不确定性评估仍需扩展。

---
DOI: 10.1109/tai.2026.3677838
