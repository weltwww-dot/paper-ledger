# Evolution Rather Than Degradation: Structure-Guided Elastic Consensus Learning for Multimodal Knowledge Graph Completion 总结

## 基本信息

- **标题**: Evolution Rather Than Degradation: Structure-Guided Elastic Consensus Learning for Multimodal Knowledge Graph Completion
- **作者**: Yameng Liu, Shuai Zheng, Zhenfeng Zhu, Yunhui Xu, Yan Zhuang, Yao Zhao, Kunlun He
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3710321
- **arXiv**: 无
- **PDF**: [TKDE_2026_EvolutionRatherThanDegradation.pdf](papers/TKDE_2026_EvolutionRatherThanDegradation.pdf)

## 一句话概括

本文提出结构引导的弹性共识学习 SECL，先用实体结构抑制不可靠视觉/文本模态的语义偏差，再对难对齐实体施加更有针对性的弹性对比学习，从而避免多模态共识学习反而造成性能退化。

## 问题与动机

多模态知识图谱补全通常把结构、图像和文本表示通过对比学习对齐，但辅助模态可能包含噪声、缺失或语义偏差，强行追求所有模态的一致性会把不可靠信息传播到实体表示中，出现“模态退化”。视觉/文本表示与图结构的语义粒度也不一致，简单 InfoNCE 难以识别哪些实体值得重点对齐。作者希望利用图结构作为可信协调信号，保留有用的跨模态共识，同时抑制不可靠特征和容易被忽略的难样本。

## 方法

SECL 包含结构引导的多模态表示协调（SMRH）和弹性对比学习（ECL）。SMRH 以实体的结构上下文为协调器，选择性压制 CLIP 视觉/文本表示中的无关特征，使其向可信的结构语义靠拢；ECL 根据实体的对齐难度调整优化关注度，提升困难实体的跨模态共识，而不是对所有样本施加同等强度的对齐。模型在结构、视觉和文本表示之间学习弹性共识，并用稀疏与对比损失控制噪声。实验使用 CLIP-ViT-L/14 获取视觉/文本表示，在无图像的 YAGO15K 上使用已有视觉嵌入和 BERT 文本表示。

## 实验与结果

作者在 FB15K-237、WN18RR、YAGO15K、MKG-W 和 MKG-Y 五个基准上，用 Hits@1/3/10、MRR 和 MR 评价知识图谱补全。WN18RR 上，SECL 相比最强基线 HKA 的 Hits@1 提升 6.2%，MRR 提升 5.1%；在 FB15K-237 的 Hits@1、Hits@3、Hits@10 和 MRR 上均取得显著优势，配对检验的 p 值分别为 0.021、0.032、0.009 和 0.013。YAGO15K 在没有为该方法提供图像的情况下仍在各项指标上取得最优结果；MKG-W 上 Hits@1/MRR 相对提升 7.4%/4.6%，MKG-Y 上提升 3.9%/7.5%。消融结果表明去掉 SMRH 后 WN18RR 的 Hits@1 和 MRR 分别下降 4.10% 和 3.42%，去掉弹性共识学习也会削弱性能；嵌入维度 5,000 在效果与复杂度之间取得较好折中。

## 贡献与局限

贡献在于识别“盲目跨模态一致性”导致的模态退化现象，并用结构引导和难样本弹性对比学习把共识学习变成可信的模态演化。局限是结构信息本身若不完整或含噪，可能把错误先验传给视觉/文本表示；不同知识图谱的图像质量、文本粒度和关系稀疏性也会影响超参数选择。方法使用较高维的多模态嵌入，部署成本和实体规模扩展性仍需进一步评估，对动态知识图谱及更多缺失模态情形也需要持续验证。

---
DOI: 10.1109/tkde.2026.3710321
