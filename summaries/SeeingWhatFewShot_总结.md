# Seeing What Few-Shot Learners See: Contrastive Cross-Class Attribution for Explainability 总结

## 基本信息

- **标题**: Seeing What Few-Shot Learners See: Contrastive Cross-Class Attribution for Explainability
- **作者**: Lingfeng Chen、Panhe Hu、Zhen Liu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3672242
- **arXiv**: 无
- **PDF**: [NN_2026_SeeingWhatFewShot.pdf](papers/NN_2026_SeeingWhatFewShot.pdf)

## 一句话概括

本文提出与分类器无关的对比跨类别归因方法 C3A 及其 episodic 版本 C3A-E，利用局部描述子和类间对比关系生成少样本学习的细粒度、可解释归因图。

## 问题与动机

少样本学习需要在每类只有少量标注样本时识别未见类别，但现有模型往往难以说明预测依据，且许多解释方法依赖特定分类器结构。尤其在医疗等数据难以大量标注的场景，无法解释模型关注的局部证据会削弱可信部署。作者希望在不改动骨干网络和分类头的条件下，解释查询样本以及整个 episodic 学习过程。

## 方法

C3A 将支持样本按目标类与对比类划分，在冻结的骨干网络特征上构造局部描述子。它把朴素贝叶斯最近邻思想与 Fisher 得分归因结合起来，分别计算类内相似性和类间相似性，再以两者的对比差异衡量局部区域对目标类别的贡献。对查询图像逐像素或逐局部块进行平均颜色替换即可得到归因图；C3A-E 则把同样的过程应用到 episode 中的支持样本，以分析模型如何利用少量支持证据。

## 实验与结果

作者在四个少样本学习基准上评测 C3A/C3A-E，并覆盖 Conv64F、ResNet12、ResNet18 和 ViT 等骨干。归因质量使用 insertion-AUC（iAUC）和 deletion-AAC（dAAC）等指标衡量，方法相对现有解释方法分别取得 19.72% 和 25.88% 的绝对提升。超参数分析表明，在实验设置中邻居数 k=10、局部块 padding 为 6、每类使用 1 个支持样本时表现稳定，而且该设置可迁移到 ResNet18 与 ViT，不需要为每种架构进行大规模调参。

## 贡献与局限

- 提出适用于多种少样本骨干的 C3A 与 episodic 解释方法。
- 通过类内/类间对比和局部描述子保留细粒度证据，能够给出像素级反事实归因。
- 在四个基准和多种骨干上改善归因质量，并支持查询预测与 episodic 学习两种解释视角。
- 局限：逐像素或逐局部块扰动的计算成本较高；方法依赖支持集的代表性，支持样本不足或分布偏移时，类间对比归因可能不稳定。

---
DOI: 10.1109/tnnls.2026.3672242
