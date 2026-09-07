# Utilizing Everyday Textures as Concept-Based Explanations for Deep Learning Model Prediction of Glioma Biomarker Status 总结

## 基本信息

- **标题**: Utilizing Everyday Textures as Concept-Based Explanations for Deep Learning Model Prediction of Glioma Biomarker Status
- **作者**: Rayyan Akhand, Farzad Alizadeh, Thanh Binh Nguyen, Nick D. James, Sreeraman Rajan, Rebecca E. Thornhill
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3681537
- **arXiv**: 无
- **PDF**: [TAI_2026_EverydayTexturesGlioma.pdf](papers/TAI_2026_EverydayTexturesGlioma.pdf)

## 一句话概括

本文利用日常图像纹理作为高层“概念”，通过 TCAV 框架解释 ResNet50 模型在 MRI 上对胶质瘤 IDH 生物标志物状态的分类决策，探索概念级可解释性在神经影像 AI 中的应用。

## 问题与动机

胶质瘤是罕见但致命的中枢神经系统肿瘤，其影像学评估依赖经验且存在主观差异，人工智能辅助分类虽性能可观，却因“黑箱”特性难以在临床落地。现有可解释性方法多以像素等低层特征解释预测，与人类基于高层抽象概念的认知方式不一致。本研究聚焦 IDH（异柠檬酸脱氢酶）生物标志物（IDH-wt 与 IDH-mut）分类，旨在用日常纹理这类可被人类理解的图像概念，量化深度模型内部表征对各概念的敏感度，弥合 AI 预测与人类理解之间的鸿沟。

## 方法

采用公开的 UCSF-PDGM 数据集，最终纳入 494 例（391 例 IDH-wt、103 例 IDH-mut），每例选取 ADC、T1c、T2、FLAIR 四种 MRI 序列；对每个 3D 序列选取肿瘤核心（NCR）面积最大的中心层面，裁剪肿瘤区域并缩放到 224×224 输入。为每种 MRI 对比训练一个基于 ResNet50 的 2D CNN（Keras+TensorFlow），用 Hyperband 优化密集层单元数、批大小与 dropout，并按受试者划分训练/验证/独立测试集（测试集占 5%，n=24）。可解释性采用 TCAV 框架：以 Describable Textures Dataset（DTD）的 47 类日常纹理为概念、MS-COCO 的 5000 张图像为随机反例，在模型的早、中、晚三个瓶颈层用逻辑回归训练概念激活向量（CAV），计算概念敏感度与 TCAV 分数，并用 Welch t 检验（Bonferroni 校正后 α≈0.00106）比较两组差异。

## 实验与结果

四个序列模型的独立测试集指标为：ADC 模型准确率 0.882、精确率 0.667、召回率 0.8、F1 0.727、AUC 0.875；T1c 模型准确率 0.961、精确率 1.0、召回率 0.8、F1 0.889、AUC 0.984；T2 模型准确率 0.882、精确率 0.75、召回率 0.6、F1 0.667、AUC 0.825；FLAIR 模型准确率 0.882、精确率 0.667、召回率 0.8、F1 0.727、AUC 0.875。TCAV 分析显示 IDH-wt 与 IDH-mut 预测的概念敏感度总体呈反向关系：如 ADC 模型中“honeycombed”概念早层对 wt 为 0.11、对 mut 为 0.83；“woven”概念对 wt 预测得分从早层 0.859（p<0.05）到中间 0.909（p<0.01）到晚层 0.974（p<0.001），而对 mut 各层均不超过 0.3。T1c 模型中“stratified”概念对 wt 各层均高于 0.99，对 mut 则为 0.00±0.00；T2 模型中“crystalline”“gauzy”“veined”对 wt 持续 ≥0.90，而 mut 仅“stratified”显著；FLAIR 模型对 wt 几乎所有概念在各层 ≥0.90（仅中间层“polka-dotted”例外），对 mut 则很少超过随机水平 0.5。FLAIR 模型中两组 TCAV 均值差异显著的概念占比在早层达 0.915、晚层 0.851。

## 贡献与局限

主要贡献有三：一是构建四种 MRI 序列特定的、用于区分 IDH-wt/IDH-mut 的深度模型；二是提出以 DTD 日常纹理作为图像概念、评估概念激活向量（CAV）分数的可解释性框架，可在不改动、不重训模型的前提下给出全局性概念归因；三是系统比较了四种 MRI 对比度下两类预测之间的概念激活差异。局限方面：仅用单一中心层面而非完整 3D 肿瘤体积训练，可能高估分类性能；独立测试集过小（n=24）限制了统计把握度；TCAV 依赖概念激活与随机激活线性可分的假设，对抽象复杂概念未必成立（可改用 Concept Gradients 等非线性框架）；TCAV 分数只反映相关性而非因果；DTD 概念间存在冗余（如“polka-dotted”与“dotted”）；概念由人工定义且需人工标注样例，可能引入偏差并遗漏关键概念。未来工作建议通过聚类、用户调研等方法精化概念集，并评估概念解释的完整性及临床医生对其的实际认可度。

---
DOI: 10.1109/tai.2026.3681537
