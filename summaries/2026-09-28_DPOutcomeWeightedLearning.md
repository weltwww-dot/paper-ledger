# Differentially Private Stochastic Gradient Descent for Outcome Weighted Learning 总结

## 基本信息
- **标题**: Differentially Private Stochastic Gradient Descent for Outcome Weighted Learning
- **作者**: Aoli Yang、Jun Fan、Yunwen Lei 等
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-28
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07168-x
- **PDF**: [ML_2026_DPOutcomeWeightedLearning.pdf](papers/ML_2026_DPOutcomeWeightedLearning.pdf)

## 一句话概括
论文为结果加权学习设计差分隐私随机梯度下降算法，在学习个体化治疗规则时同时分析医疗记录隐私与决策效用。

## 问题与动机
精准医疗需要从患者特征、所受治疗和治疗结局中学习谁适合哪种方案，但这些数据高度敏感。常见隐私学习分析多面向普通输入—输出样本，未直接覆盖“特征—行动—回报”形式及治疗规则的价值损失。

## 方法
作者在结果加权分类目标的每次随机梯度更新中加入高斯噪声，给出差分隐私保证，并从稳定性、泛化和优化误差出发分析所得规则的超额价值。理论分别覆盖 logistic 损失、hinge 损失，以及通过 Moreau 包络平滑的 hinge 损失。

## 实验与结果
论文推导三类损失下的效用收敛界，并用经验实验检验隐私保护与决策效用之间的关系，显示平滑技术具有实际价值。理论保证依赖文中对损失、梯度和采样方式的条件，不能视为任何临床数据与任意训练配置下都自动成立。

## 贡献与局限
贡献是把差分隐私 SGD 扩展到个体化治疗的结果加权学习，并以超额价值而非普通分类精度讨论效用。实验与证明支持所设条件下的方法；临床部署仍需验证数据偏倚、治疗安全性和特定隐私预算下的实际收益。

---
DOI: 10.1007/s10994-026-07168-x
