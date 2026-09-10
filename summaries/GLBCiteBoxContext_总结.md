# Box-enhanced context fusion for citation intent classification 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Box-enhanced context fusion for citation intent classification
- 作者：Jinwen Yang, Zhijuan Du
- 期刊 / 年份：Neural Networks / 2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108962
- PDF：[GLBCiteBoxContext.pdf](papers/GLBCiteBoxContext.pdf)

## 一句话概括

GLB-Cite 将引用标记的局部位置、全文上下文和 box embedding 融合，用于更准确地识别科学文献中的 citation intent。

## 问题与动机

引用意图分类不仅取决于引用前后的文本，还与引用标记在段落或文档中的位置及其上下文层级关系有关。仅使用文本语义可能难以区分语义相近、边界模糊的意图类别，因此需要同时建模语义和位置结构信息。

## 方法

模型先用 GL-Fusion 融合局部引用标记和全局上下文，再把表示映射到向量空间和 box 空间。向量分支负责语义区分，box 分支通过几何重叠表达上下文与意图类别的关系；两条分支联合优化，以平衡语义表达与边界建模能力。

## 实验与结果

论文在 SciCite 和 ACL-ARC 两个公开数据集上进行比较，并报告 macro-F1、消融和可视化分析。GLB-Cite 在 SciCite 和 ACL-ARC 上的 F1 分别为 87.69% 和 79.79%，在两项数据集上均达到文中报告的 state-of-the-art；消融结果支持局部/全局融合及 box 表示对性能的贡献。

## 贡献与局限

论文把 citation marker 的位置感知、全局上下文融合和 box embedding 结合到统一分类框架中，并通过两个数据集验证有效性。局限是 ACL-ARC 上的 F1 仍低于 80%，且实验依赖现有 SciBERT 表示；更强的科学文本编码器、更灵活的几何表示和跨领域泛化仍有待研究。

DOI: 10.1016/j.neunet.2026.108962
