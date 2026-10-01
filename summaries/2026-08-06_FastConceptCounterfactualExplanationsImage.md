# Fast concept-based counterfactual explanations for image classification 总结

## 基本信息
- **标题**: Fast concept-based counterfactual explanations for image classification
- **作者**: Ruihan Zhang、Tim Miller、Krista A. Ehinger 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-08-06
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104599
- **PDF**: [AIJ_2026_FastConceptCounterfactualExplanationsImage.pdf](papers/AIJ_2026_FastConceptCounterfactualExplanationsImage.pdf)

## 一句话概括
FCCE 在语义概念空间中直接求解图像分类反事实，以较低计算开销生成能说明“改变哪些概念会改变类别”的解释。

## 问题与动机
像素级反事实常缺乏语义可读性，生成模型又需迭代采样，优化方法也依赖搜索；已有概念方法还受分割质量或人工筛选限制。作者希望兼顾可理解性、忠实度与交互速度。

## 方法
方法先用特征图上的无监督概念表示和线性分类头近似 CNN 决策，再将输入概念向量投影到目标类别决策边界，得到闭式反事实。为提升合理性，另以目标类中心构造变化方向，并用 top-k 筛选形成稀疏概念说明；最终将结果映回原 CNN 检验忠实度。

## 实验与结果
在 CUB 上对 197 人开展模型失误识别实验，FCCE 组准确率为 89.88%，高于 CVE 的 50.89%、ACE 的 68.47% 和 ICE 的 82.95%。CUB、MNIST、ImageNet 评估中，相对 logit gap 低于 0.3%；解析求解低于 10⁻⁵ 秒，单样本解释端到端开销约 10⁻² 秒。

## 贡献与局限
论文给出概念空间闭式反事实方法，并同时验证人类决策效用、原模型忠实度和运行时间。作者指出其效果依赖概念空间质量；人类实验聚焦 CUB 的细粒度模型失误识别，其他任务和领域的效用仍需验证。扩散模型只作为延迟参照，并非同数据集上的解释质量基线，因此速度结果不能外推为各项性能均优于生成方法。

---
DOI: 10.1016/j.artint.2026.104599
