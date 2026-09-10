# The Adversarial Game Between Detection and Evasion: A Survey of Anti-Detection Techniques for Machine-Generated Texts 总结

## 基本信息

- **标题**: The Adversarial Game Between Detection and Evasion: A Survey of Anti-Detection Techniques for Machine-Generated Texts
- **作者**: Deyu Meng、Tad Gonsalves
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109562
- **arXiv**: 无
- **PDF**: [NN_2026_Paper18.pdf](papers/NN_2026_AntiDetectionMachineGeneratedTexts.pdf)

## 一句话概括

本文按 PRISMA 2020 系统梳理机器生成文本检测与规避之间的攻防博弈。

## 问题与动机

大型语言模型普及带来大量机器生成文本检测器，也催生针对检测器的规避攻击。已有综述更多关注检测技术，较少系统分析攻击与防御的动态关系。研究希望汇总攻击类型、检测器表现和可用防御证据。

## 方法

作者遵循 PRISMA 2020，系统综合 27 项关于机器生成文本检测攻击及其防御的研究。文章将规避策略分为水印攻击、改写攻击、提示攻击和对抗文本攻击，并整理不同检测器上的攻击与防御性能。

## 实验与结果

本文是系统综述，不训练新的检测器。结果是对报告性能的汇编与比较，指出不同攻击会改变检测器表现，而对应防御证据仍不完整。作者还提供分类文献、论文链接及可用代码和数据仓库。

## 贡献与局限

贡献是把 MGTD 的检测、规避和防御放入同一攻防框架。局限是仅纳入 27 项研究且各文献的文本生成器、检测器、指标和威胁模型不同，横向数字比较存在明显限制。

---
DOI: 10.1016/j.neunet.2026.109562

