# Class-Imbalanced Learning via Multitask Multiobjective Feature Selection 总结

## 基本信息

- **标题**: Class-Imbalanced Learning via Multitask Multiobjective Feature Selection
- **作者**: Ruwang Jiao, Naoki Masuyama, Yusuke Nojima
- **期刊 / 年份**: IEEE Transactions on Artificial Intelligence, 2026
- **研究方向**: 机器学习方法；类别不平衡学习与进化特征选择
- **DOI**: 10.1109/tai.2026.3673680
- **PDF**: [TAI_2026_ClassImbalancedMultitaskMultiobjective.pdf](papers/TAI_2026_ClassImbalancedMultitaskMultiobjective.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 CIL-MTFS 多任务多目标特征选择方法，在不人为重采样的原始不平衡数据上，同时优化整体分类性能、特征稀疏性和少数类性能，并通过跨任务基因转移共享互补特征。

## 问题与动机

类别不平衡使常规分类器偏向多数类，高维特征又带来过拟合、稀疏性和组合搜索爆炸；两者叠加时，少数类往往更难泛化。重采样会改变数据分布或放大噪声，而只强调少数类的特征选择又可能损害整体性能，因此需要在保留原始数据语义的同时兼顾分类质量和降维效果。

## 方法

CIL-MTFS 构造两个相关任务：T1 是带约束的双目标优化，最小化 balanced classification error rate 和选中特征比例，并排除训练误差劣于全特征方案的子集；T2 使用按类别样本量和当前分类误差动态确定的 cost-sensitive error，重点改善少数类。算法分别维护两个种群，通过条件触发的跨任务基因转移，在 T1 的少数类表现偏差较大时引入 T2 的有利特征，再用单点交叉、位翻转变异和各自的环境选择更新种群；最终返回 T1 的可行非支配特征子集。

## 实验与结果

作者在来自生物医学、金融、雷达和识别等领域的 17 个真实不平衡数据集上比较 CIL-MTFS、NSGA-II、DAEA、MFFS、BSOEA、PRDH、IMFWA 和 MEL，采用约 70%/30% 训练—测试划分、KNN 与加权 SVM，并独立运行 30 次。相较全特征方案，CIL-MTFS 在至少 12/17 个数据集上改善 MCER、F1-score 或 G-mean，同时大幅减少特征；例如 Yeoh-2002-v1 从 2526 个特征选约 51 个且 MCER 从 7.5376% 降至 2.7779%，CNS 从 7129 个选约 1053 个且 MCER 从 14.290% 降至 10.437%。在七个主要对比方法中，CIL-MTFS 的 F1 在 7/17 个数据集上最好，并在消融实验中相较两个单任务版本显著提升多项指标。

## 贡献与局限

贡献包括：把整体性能—稀疏性任务与少数类性能任务统一为进化多任务问题；设计依据类别误差自适应触发的跨任务基因转移；在高维、少样本数据上取得较强分类表现并输出可解释的特征子集。局限是 T1 的可行性约束可能使最终子集偏大，且当前实验主要是二分类任务；少数数据集上降维会增加误差。作者提出后续研究长尾多分类、进一步减少特征，以及结合样本清洗和样本选择处理标签噪声。

---
DOI: 10.1109/tai.2026.3673680
