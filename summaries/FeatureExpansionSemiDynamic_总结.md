# Feature Expansion With Semi-Dynamic Feature Sets (SDFS) and LLM-Powered Explainability: A Novel Approach to Discovering Missing Features 总结

## 基本信息

- **标题**: Feature Expansion With Semi-Dynamic Feature Sets (SDFS) and LLM-Powered Explainability: A Novel Approach to Discovering Missing Features
- **作者**: Elaheh Hosseini, Soodeh Nikan
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-04-07
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TAI.2026.3681539
- **arXiv**: 无
- **PDF**: [TAI_2026_FeatureExpansionSemiDynamic.pdf](papers/TAI_2026_FeatureExpansionSemiDynamic.pdf)

## 一句话概括

本文提出半动态特征集（SDFS）网络，把每个样本的潜在缺失特征作为可学习输入，与模型参数共同更新，再用 LLM 为新特征生成可解释标签，以提升表格和时间序列预测。

## 问题与动机

传统特征选择假设初始特征空间已经完整，降维还可能丢失隐藏但有用的信息；复杂系统中的关键变量未必能由现有特征的线性或非线性关系直接恢复。作者将问题转为特征扩展：不收集新数据，而是在训练中估计可能缺失的维度，并分析它们与预测目标的关系，尤其关注小型、复杂表格数据。

## 方法

Tabular-SDFS 使用一个含 128 个隐藏单元的单隐层 MLP，将静态特征和每个训练样本的动态特征共同输入。动态特征先用随机、均值/标准差或 PCA 初始化，随后直接按梯度更新，学习率固定为 1；L2 权重衰减 λ=1e−5 和 patience=3 的 early stopping 用于缓解快速过拟合。时间序列版本以 LSTM 为预测器，按 z-normalized 形状余弦相似度为验证/测试窗口匹配最相近训练窗口，再按中心化 Frobenius 范数缩放其动态特征。最后结合 SHAP、相关性和 LLM 为动态特征命名。

## 实验与结果

作者使用六个表格数据集（包括 Wine Quality、Pima Indians Diabetes、Breast Cancer Wisconsin、Census Income、Parkinson’s Disease Detection、Diabetes Health Indicators）和 ETTh1、Air Quality UCI 两个时间序列数据集，采用 80/10/10 划分。Wine Quality 上 SDFS 的准确率为 0.85、F1 为 0.77、ROC-AUC 为 0.87，均高于基线的 0.82、0.63、0.83；五个随机划分的 F1 从 0.369±0.034 提升到 0.620±0.047。时间序列上，ETTh1 的 MAE/RMSE 从 0.54/0.75 降至 0.41/0.63，Air Quality UCI 的 MAE 从 91.2 降至 85.04；LLM 标签的 E5 cosine 均高于 0.81，最高 BERTScore F1 为 0.77。

## 贡献与局限

贡献是：提出按样本学习潜在缺失维度的 SDFS，并统一覆盖表格分类与时间序列回归；结合 SHAP 和 LLM 将动态特征从黑盒变量转化为带统计依据的解释标签，并以多数据集、随机划分和交叉验证检验稳定性。局限是动态特征需逐样本更新，时间序列的相似度匹配成为明显时间瓶颈；特征扩展在原始空间已充分表达时可能引入噪声，未来需并行化和优化扩展流程。

---
DOI: 10.1109/TAI.2026.3681539
