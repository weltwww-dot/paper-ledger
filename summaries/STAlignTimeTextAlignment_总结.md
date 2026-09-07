# ST-Align: A time series and text alignment framework for cross-subject multivariate time series classification 总结

## 基本信息

- **标题**: ST-Align: A time series and text alignment framework for cross-subject multivariate time series classification
- **作者**: Zhenghuang Wu, Tao Zhang, Ke Li, Yuangan Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108913
- **arXiv**: 无
- **PDF**: [NN_2026_STAlignTimeTextAlignment.pdf](papers/NN_2026_STAlignTimeTextAlignment.pdf)

## 一句话概括

ST-Align 通过“token 级匹配 + 原型级对比”的两阶段信号-文本混合对齐，将多元时间序列嵌入冻结大语言模型（LLaMA3.1-8B）语义空间，实现跨被试分类 SOTA。

## 问题与动机

多元时间序列分类（MTSC）旨在捕捉变量间时序动态以完成分类，现有方法大多只处理单模态信号数据，忽视类别文本标签蕴含的丰富语义信息，因而难以理解复杂模式并在未见数据上泛化，导致真实跨被试场景下性能欠佳。已有的时序与 LLM 融合方法存在三方面瓶颈：难以同时刻画时间依赖与通道特征；数值时间序列与 LLM 语义空间不匹配，且单一对齐方式效果有限；许多时序数据集缺少对应文本，难以获得对齐锚点。

## 方法

ST-Align 由三个核心组件构成：特征表示模块（全局 Transformer 编码器叠加正弦/余弦位置编码，配合带残差的 PatchConv 一维卷积局部编码器）、信号-文本对齐模块和冻结的预训练 LLM。文本侧由专家设计提示词驱动 LLM 生成“label + description”的结构化标签描述并经专家审核，再由 BERT-base 嵌入作为语义锚点。对齐采用两阶段混合范式：token 级对齐中，参数共享的分类编码器（CE）与匹配编码器（ME）以可学习 query 结合文本嵌入执行交叉注意力匹配，构建正例、普通负例和困难负例三元组训练集并优化匹配损失；原型级对齐则以带动态掩码的对比学习（含分类损失与温度参数化的对比损失）缓解同批多个异构信号共享同一标签造成的梯度歧义与特征坍缩。总损失为三类损失之和，随后冻结特征、对齐模块与 LLM，仅训练 Adapter 与分类头，用交叉熵损失完成跨被试微调（本研究采用 LLaMA3.1-8B）。

## 实验与结果

在四个跨域数据集上采用按受试者划分的 10 折跨被试验证（10f-CS）：HAR（30 名被试、9 通道、6 类、10,299 样本）、AW-A 空中书写（55 名被试、6 通道、26 类、21,450 样本）、WISDM（35 名被试、3 通道、6 类、8,575 样本）与 Sleep-EDF（20 名被试、1 通道、6 类、20,626 样本）。与 12 个基线（MiniRocket/MultiRocket、ConvTran/Reformer/Informer/Nonstationary Transformer/PatchTST/TimesNet/iTransformer、Time-LLM/GPT4TS/TEST）相比，ST-Align 平均准确率达 88.4%，去 LLM 版为 86.3%，均在四个数据集上最优（各数据集带 LLM 平均：HAR 95.1%、AW-A 85.9%、WISDM 92.1%、S-EDF 80.3%），且引入 LLM 使准确率提升并将变异性降低 10.6%。消融实验表明：特征骨干从 ResNet-10（70.2%）到 PatchConv+Transformer（92.1%）逐步提升；WISDM 上基线 68.5% → +token 级对齐 81.0% → +原型级对比 90.3% → 换 LLM 分类头 92.1%，两阶段累计增益 21.8%；query 长度 32 最优、增至 48 反而下降；对比度温度系数在 τ=0.07 时达到最优倒 U 峰值；LLM 规模实验中 BERT 系列（与对齐语义空间兼容）与 LLaMA3.1-8B（较去 LLM 版提升 1.8%）表现突出，而 GPT/Qwen 等不兼容模型性能较差。

## 贡献与局限

贡献：提出以文本标签为锚点、无需额外语料的信号-文本两阶段“微-宏”混合对齐框架，token 级与原型级对齐互补，显著提升跨被试泛化；模块化设计使 LLM 可即插即用，冻结大部分模块、仅微调 Adapter 与分类头，训练参数高效。局限：引入 LLM 增加推理计算开销；作者声明数据按需提供（Data will be made available on request），未公开代码与数据；未来拟探索更大规模 LLM 以进一步提升时序分类精度。

---
DOI: 10.1016/j.neunet.2026.108913
