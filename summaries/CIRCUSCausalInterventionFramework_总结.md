# CIRCUS: A Causal Intervention-Based Framework for Enhancing Counterfactual Fairness in Trained Classifiers

## 基本信息

- **标题**: CIRCUS: A Causal Intervention-Based Framework for Enhancing Counterfactual Fairness in Trained Classifiers
- **作者**：Qifen Yang、Yuhui Deng、Jiande Huang、Lijuan Lu、Peng Zhou、Geyong Min
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3670269
- **arXiv**：无
- **PDF**：[NN_2026_CIRCUSCausalInterventionFramework.pdf](papers/NN_2026_CIRCUSCausalInterventionFramework.pdf)

## 一句话概括

本文提出由 CITGAN 和 CIRCUS 组成的因果干预公平性框架，先按结构因果模型生成反事实歧视样本，再进行标签偏差校正和分类器重训练，以降低已训练模型的反事实不公平。

## 问题与动机

反事实公平要求同一个体在改变敏感属性后的反事实世界中仍保持一致预测，但传统数据增强或 VAE 方法往往不能严格保留结构因果模型中的变量依赖，生成的反事实样本可能不符合真实因果关系。论文希望在不完全重建分类器的情况下，找到真正会因敏感属性及其代理路径而改变预测的样本，再用这些样本修正分类器的偏差，同时尽量保持原有分类效用。

## 方法

CITGAN 分三阶段工作：用带 KL 正则和 HGR 独立性约束的编码器从观测数据推断外生变量；按照因果图拓扑顺序为每个内生变量配置子生成器，逐步生成具有因果依赖的表格数据；最后用 WGAN-GP、重构损失和动态权重联合训练。CIRCUS 在此基础上先利用分类损失梯度和敏感属性后代节点的因果关联度选择干预特征，生成靠近决策边界的反事实歧视样本；再在这些样本附近进行局部小步干预扩充样本，最后执行标签偏差校正并重新训练分类器。该流程同时评估传统 DNN 和 ResNet。

## 实验与结果

实验使用 Adult、Credit、Bank、Bail 和 Nutrition 五个公平性数据集，并以分类效用、Jensen–Shannon 散度、Wasserstein 距离、相关性误差和线性/核 MMD 评价。CITGAN 在合成数据的 AUC 差异指标上优于所有对比方法，平均 ACD 和 AUD 相对第二名分别改善约 17.6% 和 67.5%；在 Adult 和 Credit 上的 JSD 分别比次优方法好约 75.5% 和 77.8%。采用 CIRCUS 进行公平性增强时，DNN 的 MMDL 和 MMDK 相对第二名平均下降 39.7% 和 40.4%，ResNet 上分别下降 56.7% 和 54.5%，同时保持较稳定的分类性能。消融实验显示，结合梯度大小与因果后代关联度的特征选择比随机或仅按梯度选择产生更多有效歧视样本。

## 贡献与局限

论文把外生变量推断、因果拓扑生成和面向决策边界的干预统一到一个公平性修正流程中，既提高了反事实样本的结构可信度，也减少了对敏感属性代理路径的隐性偏差。局限在于 CIRCUS 当前主要适用于可微分类器，依赖预先给定或可靠学习的因果图，并需要在生成样本量、干预步长和公平性—效用之间调参；对决策树等非光滑模型的适用性尚未验证。后续可扩展到非可微模型、自动因果结构学习和更高效的超参数优化。

---
DOI: 10.1109/tnnls.2026.3670269
