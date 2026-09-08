# Causal evidence that language models use confidence to drive behaviour 总结

## 基本信息

- **标题**: Causal evidence that language models use confidence to drive behaviour
- **作者**: Dharshan Kumaran、Nathaniel Daw、Simon Osindero et al.
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **发表**: 2026-09-07
- **内容状态**: 完整 · 已基于开放获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01293-x
- **arXiv**: 无
- **PDF**: [NMI_2026_ConfidenceBehaviour.pdf](papers/NMI_2026_ConfidenceBehaviour.pdf)

## 一句话概括

研究通过增强或抑制模型内部的置信度信号，提供了大语言模型利用置信度决定回答还是拒答的因果证据。

## 问题与动机

大语言模型在不确定时能否适当拒答，直接关系到系统可靠性。仅观察回答内容与置信度之间的相关性，无法说明模型是否真正以内部置信信号驱动行为，因此需要可干预的因果检验。

## 方法

作者设计四阶段范式：先测量无拒答选项时的基线置信度，再分析模型的隐式拒答阈值；随后用 activation steering 增强或抑制置信信号，并通过中介分析验证作用路径；最后要求模型按不同置信水平拒答，考察其能否调整策略。

## 实验与结果

置信度对拒答的效应量约比替代机制高一个数量级；增强置信信号会降低拒答率，抑制则提高拒答率，中介分析显示置信度重新分布是主要机制。GPT-4o 阶段中，加入拒答后已回答问题的准确率由 63.7% 升至 69.1%，体现覆盖率与准确率的权衡。

## 贡献与局限

贡献在于从相关性推进到内部机制的因果干预，并揭示 token 概率与口头置信度只是更丰富内部表示的有损读出。局限是研究聚焦问答拒答场景；这种元认知控制能否推广到长期智能体任务、分布偏移及对抗提示，仍需进一步验证。

---
DOI: 10.1038/s42256-026-01293-x
