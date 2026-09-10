# CEMTNet: a cognitive emotion modulated network for multimodal depression detection 总结

## 基本信息

- **标题**: CEMTNet: a cognitive emotion modulated network for multimodal depression detection
- **作者**: Yujie Huo, Hongyu Gao, Weng Howe Chan, Ahmad Najmi Bin Amerhaider Nuar
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108907
- **arXiv**: 无
- **PDF**: [NN_2026_CEMTNetMultimodalDepression.pdf](papers/NN_2026_CEMTNetMultimodalDepression.pdf)

## 一句话概括

论文提出 CEMTNet，从音频和文本中联合建模情绪一致性、细粒度线索和情绪趋势，以提升自动抑郁检测。

## 问题与动机

早期抑郁识别具有公共卫生意义，但多模态方法常受到跨模态情绪不一致、细微情绪线索难提取和动态变化难建模的影响。作者因此关注更稳健的音频—文本融合。

## 方法

CEMTNet 包含 Cognitive Consistency Inference Mechanism（CCIM）、Emotion-Modulated Structured Attention（EMSA）和 Contrastive Emotion Trend Modeling（CE-TM）。CCIM 按估计的情绪一致性动态调整融合权重，EMSA 用情绪感知多头注意力抽取细粒度线索，CE-TM 将对比学习与时间趋势建模结合。

## 实验与结果

在 DAIC-WOZ 和 EATD-Corpus 上，CEMTNet 的准确率为 0.92，F1 为 0.92，召回率为 0.93，并优于文中比较的先进方法。消融实验和案例分析进一步支持三个模块的有效性与稳健性。

## 贡献与局限

贡献是把情绪一致性、结构化注意力和趋势对比学习统一到音频—文本抑郁识别中。局限是数据集和模态范围有限，模型在真实临床场景、跨文化分布和诊断责任边界上的有效性仍需独立验证。

---
DOI: 10.1016/j.neunet.2026.108907
