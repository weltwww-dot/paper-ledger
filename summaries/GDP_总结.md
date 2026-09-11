# Generative Distribution Prediction: A Unified Approach to Multimodal Learning 总结

## 基本信息

- 标题: Generative Distribution Prediction: A Unified Approach to Multimodal Learning
- 作者: Xinyu Tian、Xiaotong Shen
- 期刊 / 会议: Machine Learning 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1007/s10994-026-07148-1
- PDF: [ML_2026_GenDistPred.pdf](papers/ML_2026_GenDistPred.pdf)

- 标题: Generative Distribution Prediction: A Unified Approach to Multimodal Learning
- 作者: Xinyu Tian、Xiaotong Shen
- 期刊 / 会议: Machine Learning 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**: Generative Distribution Prediction: A Unified Approach to Multimodal Learning
- **作者**: Xinyu Tian、Xiaotong Shen
- **期刊 / 卷号文章号**: Machine Learning, 115:209 (2026)
- **正式版 PDF**: [ML_2026_GenDistPred.pdf](papers/ML_2026_GenDistPred.pdf)
## 一句话概括

Generative Distribution Prediction（GDP）先学习给定输入下的完整条件响应分布，再从该分布生成样本并按用户指定的损失做 risk minimization，以统一处理表格、文本、图像及其组合上的点预测、分位数、众数、captioning 和问答。

## 问题与动机

传统多模态方法通常为每种模态配置监督预测头，只输出条件均值、分位数或单个标签，容易丢失分布形状、不确定性和联合依赖，也难以用同一决策原则适应不同预测目标。异构数据在维度、结构和统计性质上差异很大，因此需要把“估计条件分布”和“针对任务选择预测规则”分开，并支持源域知识迁移到目标域。

## 方法

GDP 包含两步：用条件生成器近似目标条件分布，必要时用 dual-level shared embeddings 从源域迁移并微调到目标域；然后为每个输入生成 m 个响应样本，最小化指定损失的经验风险得到点预测。条件扩散模型是主要实现，并通过 Wasserstein generation error 与 synthetic sampling error 建立风险界：增加 m 只能降低采样误差，生成器失配、缺失模式或校准不足仍需改进生成器本身。

## 实验与结果

在自适应分位数回归中，GDP 的平均 RMSE 为 1.139（Case I）和 1.191（Case II），低于 DQR 的 1.193 和 1.279 及 XGBoost 的 1.345 和 1.342；模态回归两种模拟情形的 RMSE 为 0.5039 和 0.6498，对 RegMS2d 的 1.1912 和 1.0311 分别改善约 57% 和 37%。多模态基准中，GDP 在 UTKFace 的年龄 RMSE 为 7.511、Shopee-IET 准确率为 0.944；Yelp 上 GDP-tr 的 Cohen’s kappa 为 0.520。COCO captioning 中 diffusion-GDP 和 BLIP-GDP 的平均相似度为 0.6994 和 0.7099；WikiQA 问答中 GDP 平均相似度为 0.7935。

## 贡献与局限

贡献包括一个与生成骨干和损失函数解耦的分布式预测原则、扩散 GDP 的风险理论，以及用共享嵌入进行多模态域适配的实现。局限是正式统计保证主要覆盖 diffusion-GDP，BLIP 和 LLM 实验是经验性展示；生成质量决定最终上限，m 增大带来近似线性的推理采样成本，且在生成器失配、幻觉、校准或模式覆盖不足时单纯增加样本无效，需进一步研究更广泛生成模型的理论与效率。

---
DOI: 10.1007/s10994-026-07148-1
