# Self-expression property theory guided multi-modal brain graph learning 总结

## 基本信息
- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: Self-expression property theory guided multi-modal brain graph learning
- **作者**: Xuexiong Luo, Jia Wu, Sheng Zhang, Jian Yang, Amin Beheshti, Bo Du, Shan Xue, Quan Z. Sheng
- **期刊 / 会议**: Artificial Intelligence 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104576
- **PDF**: [BrainMMSelfExpression.pdf](papers/BrainMMSelfExpression.pdf)

## 一句话概括
BrainMM 将多属性脑图、跨尺度对比图神经网络和 self-expression property theory 结合，用于多模态脑疾病预测，并生成可解释的共识脑图。

## 问题与动机
现有多模态脑图方法常直接把简单连接剖面作为节点属性，难以充分描述脑连接网络；健康人与患者脑图差异可能很小，单模态表示的判别性不足。简单注意力融合也难以刻画模态互补关系，不易识别与疾病有关的脑区和连接。

## 方法
作者扩展多属性脑图特征，并设计跨尺度对比图神经网络，学习每种成像模态的多层、判别性表示。随后利用 self-expression property theory 提取多模态脑图的互补关系并生成 consensus graph，再用注意力机制自适应融合共性特征与各模态特征；共识图用于定位疾病相关脑区和连接。

## 实验与结果
论文在三个脑疾病数据集上进行脑疾病预测、消融、鲁棒性、训练时间和参数敏感性实验。BrainMM 整体优于多种对比方法；病理分析识别出的网络和连接与医学研究发现一致。随机增删连接后性能会下降但小扰动下仍具竞争力；模型训练时间高于部分基线，但作者认为小规模脑图上仍可接受。

## 贡献与局限
贡献是把多属性/跨尺度表示学习、self-expression 互补关系建模和可解释共识图统一到多模态脑图分析中，并以三个数据集验证效果。局限是解释主要为定性或关联性分析，医学交叉验证有限；脑图规模和样本量也较小，临床泛化与因果层面的病理结论需要进一步验证。

---
DOI: 10.1016/j.artint.2026.104576

