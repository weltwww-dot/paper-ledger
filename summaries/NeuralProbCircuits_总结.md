# Neural Probabilistic Circuits: Enabling Compositional and Interpretable Predictions Through Logical Reasoning 总结

## 基本信息

- 标题: Neural Probabilistic Circuits: Enabling Compositional and Interpretable Predictions Through Logical Reasoning
- 作者: Weixin Chen、Simon Yu、Huajie Shao et al.
- 期刊 / 会议: Machine Learning 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1007/s10994-026-07118-7
- PDF: [ML_2026_NeuralProbCircuits.pdf](papers/ML_2026_NeuralProbCircuits.pdf)

- 标题: Neural Probabilistic Circuits: Enabling Compositional and Interpretable Predictions Through Logical Reasoning
- 作者: Weixin Chen、Simon Yu、Huajie Shao et al.
- 期刊 / 会议: Machine Learning 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**: Neural Probabilistic Circuits: Enabling Compositional and Interpretable Predictions Through Logical Reasoning
- **作者**: Weixin Chen、Simon Yu、Huajie Shao et al.
- **期刊 / 卷号文章号**: Machine Learning, 115:207 (2026)
- **正式版 PDF**: [ML_2026_NeuralProbCircuits.pdf](papers/ML_2026_NeuralProbCircuits.pdf)
## 一句话概括

论文提出 Neural Probabilistic Circuits（NPC），把神经属性识别器与可进行精确概率推理的 probabilistic circuit 组合起来，让分类模型能通过属性和逻辑关系作出预测，同时输出最可能解释与反事实解释。

## 问题与动机

端到端深度网络性能强但通常是黑盒，post hoc 解释可能与真实决策依据不一致；概念瓶颈模型虽然引入可理解概念，使用高维 embedding 或无监督神经元又会损失语义透明性，线性任务头也难表达属性之间的逻辑关系。已有逻辑规则方法通常不能同时使用数据学习规则和人类预定义知识，也缺少整体误差与各模块误差之间的理论联系。

## 方法

NPC 的 attribute recognition model 输出颜色、形状、符号等属性的概率向量，task predictor 则用满足 smoothness 和 decomposability 的 probabilistic circuit 建模属性与类别的联合分布，并通过条件概率完成逻辑式分类。训练分为属性多任务学习、数据驱动或 knowledge-injected 的电路构建、端到端 joint optimization 三阶段；作者证明整体误差受模块误差线性组合上界约束，并用 brute-force MPE 找主要属性组合、用 projected gradient ascent 生成能纠正错误预测的 counterfactual explanation。

## 实验与结果

实验覆盖 MNIST-Addition（35,000 个样本）、GTSRB（39,209 张交通标志图像）、CelebA（202,599 张人脸图像）和 AwA2（37,322 张动物图像），按 8:1:1 划分，并与 CBM、Hybrid CBM、CEM、DCR 和端到端 DNN 比较。NPC(Data) 与 NPC(Knowledge) 在可解释模型中保持竞争力，在 MNIST-Addition、GTSRB 上可超过黑盒基线，复杂 CelebA/AwA2 上与 DNN 仍有小差距；数据驱动电路在 AwA2 的准确率为 68.52%，knowledge-injected 电路为 23.47%，说明复杂多值属性下结构表达能力很关键。属性干预通常改善预测，MPE 多数场景与真实属性对齐，但复杂数据集的 CE correction rate 较低。

## 贡献与局限

贡献是提出同时支持数据规则、人类规则和理论保证的透明概率电路架构，并将属性干预、MPE 与 CE 纳入可解释预测。局限包括属性识别器本身仍可能学习背景捷径，LearnSPN 电路可能过大而推理慢，手工电路又可能表达力不足；“属性足以决定类别”和“给定输入属性相互独立”假设会限制真实场景适用性，joint optimization 还可能降低概念准确率。密集概念标注、属性数增多导致的指数复杂度和大规模部署仍需解决。

---
DOI: 10.1007/s10994-026-07118-7
