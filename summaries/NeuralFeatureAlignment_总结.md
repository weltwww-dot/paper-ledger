# Neural feature alignment between large language models and brain activities: A knowledge-based framework for cross-modal analysis 总结

## 基本信息

- **标题**: Neural feature alignment between large language models and brain activities: A knowledge-based framework for cross-modal analysis
- **作者**: Zhejun Zhang, Wenqing Zhou, Shuo Zhang, Xinhang Li, Lin Zhang, Lei Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108916
- **arXiv**: 无
- **PDF**: [NN_2026_NeuralFeatureAlignment.pdf](papers/NN_2026_NeuralFeatureAlignment.pdf)

## 一句话概括

本文提出可解释的跨模态 Feature Alignment（FA）框架，借助 NFA/AGOP 将大语言模型内部表示转化为语义可解释特征并与多尺度 EEG 特征对齐，证明 FA 分数能强预测模型能力（与六项基准相关 r=0.736–0.886）并揭示模型深度与训练策略对“类脑对齐”的非单调影响。

## 问题与动机

大语言模型（LLM）与大脑表征对齐研究多依赖 brain-score、RSA 等整体式指标，只能回答“整体有多像”，无法揭示是哪些细粒度特征对应哪些认知过程，且过度依赖单一指标存在 Goodhart's Law 风险。作者基于 Neural Feature Ansatz（NFA）理论——其 Average Gradient Outer Product（AGOP）能提取具有可解释语义内容的特征——提出知识工程式 FA 框架：先把 LLM 黑箱状态转化为显式语义概念（NNFPP 特征传播路径），再与反映不同认知过程的 EEG 特征（ERP 的 N400/P100/P200 与 δ、θ、β 频带功率）系统映射，从而刻画“计算—认知”细粒度对应，并检验这些对齐指标是否捕获模型的功能性属性。

## 方法

FA 框架分四步：①用 DERCo 英语自然阅读任务文本输入，逐层提取 LLM 隐藏状态，按 NFA 理论以 AGOP 矩阵（输出对隐状态梯度的外积均值）和注意力 value 投影矩阵构造的 Neural Feature Matrices（NFM，随机化 RNFM 作对照）提取特征方向，取 top-k=10 特征向量、激活最高的 m=20 个 token 组成词汇集，用 Claude 3.7 Sonnet 打主题标签（Gemini 2.0 Flash 复核）；以特征向量为节点、相邻层 Spearman 相关为边构造 NNFPP，比较最大强度（MS）与首特征（FF）两种路径策略。②在 DERCo 数据集（22 名英语母语被试 RSVP 阅读 5 篇格林童话，32 通道、1000 Hz）上，于 32 电极、额/中央/颞/顶/枕五脑区与全脑三个空间尺度提取共 45 类 EEG 特征，主分析聚焦有认知对应的 6 个特征。③FA 分数定义为同一输入下 LLM 特征激活向量与 EEG 特征向量的 Pearson 相关绝对值 |r|。④以（EEG 特征×层四分位×通道）共 5760 个三元组关联 15 个 LLM 变体（Qwen2.5 0.5B–14B 的 base/instruct/math 及 DeepSeek-R1-Distill-Qwen）在 IFEval、BBH、MATH、GPQA、MUSR、MMLU-PRO 六项基准上的性能，并用置换检验、混淆回归、ICC、混合效应模型、层扰动实验、TMNRED 中文 EEG 跨语言复现及 RSA/Brain-Score 对照验证稳健性。代码已开源（https://github.com/Mochizuki-BUPT/Neural-Feature-Alignment）。

## 实验与结果

框架构建方面，9 种 NNFPP 构造方法（AGOP/NFM/RNFM × FF/MS/RF）比较中 AGOP+MS 综合最优，双因素 ANOVA 显示特征提取（F(2,666)=106.25, p<0.001）与路径策略（F(2,666)=429.29, p<0.001）主效应及交互均显著；AGOP 提取词组的语义一致性（M=1.85）显著高于 PCA（1.51）、L2 范数（1.71）与随机基线（1.23）。核心验证上，最优三元组的 FA 分数与六个 LLM 基准强相关 r=0.736–0.886（均 p<0.001，FDR 校正后 86.3% 关联仍显著），控制参数规模后偏相关均 >0.82，Qwen 家族内 r=0.89–0.95，域外基准 GSM8K r=0.882、ARC-C r=0.860、TruthfulQA r=0.846（CV<3.5%）；置换检验 token 级显著率 27.0%（5.4 倍富集）、block 级 19.5%（3.9 倍），词汇混淆回归 R²<0.012%；对 Qwen2.5-7B 逐层注入噪声的扰动实验中，30 个组合的 FA 与基准性能同步下降且 13 个层间下降相关显著为正，支持 FA 的功能相关性。模式分析上，6 个特征均显示显著的层四分位×脑区交互（如 N400: F(15,14616)=8.77, p<0.001），对齐随网络深度呈倒 U 型、Q3→Q4 显著下降，N400 对齐峰值在枕区 Q1、P100 在额区 Q3、P200 在顶区 Q2。计算因素上：参数规模影响全部显著但非单调（N400 在 7B 达峰后 14B 回落）；指令微调（IFT）在聚合上增强全部 6 个特征的对齐（N400/P100/P200/δ 显著，p<0.01），7B/14B 效果最强；知识蒸馏（KD，DeepSeek-R1-Distill 对原版 Qwen2.5）选择性增强 N400 对齐（聚合 t=6.89, p<0.001, d=0.057，14B 达 d=0.075）同时显著抑制 P100/P200、δ/θ/β 对齐，即优先保留语义对应而牺牲感知类对齐。跨语言复现（TMNRED 中文自然阅读 EEG 数据集，30 名被试）与行为验证支持结论普适性：核心模式全部复现，低可预测性词的 N400 FA 更高（t=−3.55, p<0.001, d=−0.196，复现经典 N400 效应），θ/δ/β 对高可预测词 FA 更高；RSA/Brain-Score 确认 IFT 增强、倒 U 型层轨迹等总体方向，但无法捕获 KD 的选择性调制；扩展 γ 频带复现关键模式，θ–γ PAC 趋势一致但未达显著（RSVP epoch 约 0.5 s 短于稳健估计所需的约 10 s 窗口）。

## 贡献与局限

贡献：①提出跨模态可解释的 FA/NNFPP 框架，把整体式对齐推进到“语义特征—认知过程”的细粒度映射，克服 brain-score/RSA 不可解释的局限；②通过基准相关、层扰动、置换检验、跨语言复现等多重证据表明 FA 分数可作为神经科学启发的 LLM 评测指标（r=0.736–0.886），把“类脑程度”转化为可工程化度量的设计目标；③系统刻画 15 个 LLM 变体，揭示参数规模非单调、IFT 总体增强、KD 语义优先的复杂调制，为训练更符合认知机制的 AI 提供依据；④人工评阅一致性高（3 名评阅人 ICC=0.974，与 LLM 标签无显著差异），且 45 类 EEG 特征与额外 γ/PAC 验证说明框架可扩展。局限：32 通道 EEG 使连通性/源级分析受逆问题不适定约束，需高密度 EEG 或颅内记录扩展；FA 本质是相关性指标，因果性结论需 TMS、闭环 EEG 扰动等人类侧干预（列为未来方向）；是否能用对齐目标训练直接增强模型能力未在本研究回答；θ–γ PAC 等特征受 epoch 长度限制未达显著；当前验证局限于两套自然阅读数据集与 Transformer LLM，向更多架构、语料与脑成像模态推广仍是开放工作。

---
DOI: 10.1016/j.neunet.2026.108916
