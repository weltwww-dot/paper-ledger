# Label Distribution Enhancement-Based Label Completion for High-Noise-Ratio Crowdsourcing 总结

## 基本信息
- **标题**: Label Distribution Enhancement-Based Label Completion for High-Noise-Ratio Crowdsourcing
- **作者**: Tong Wu、Liangxiao Jiang、Wenjun Zhang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15097-15111
- **发表**: 2026-08-11
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3721048

## 一句话概括
本文提出 LDELC，在高噪声众包标注场景中先估计工人质量，再增强标签分布并传播补齐缺失标注。

## 问题与动机
众包标签矩阵往往同时存在缺失和错误标注；许多补全方法主要针对噪声较低的情况，噪声较高时直接传播标签可能把不可靠意见扩散到更多样本。

## 方法
LDELC 先依据工人标注表现区分高、低质量工人，为前者估计类别概率分布，为后者结合原始噪声标签初始化分布并进行增强；随后迭代传播各标签分布至收敛，以收敛分布的最大概率类别填充缺失项。补全后的数据可继续输入现有标签集成方法。

## 实验与结果
在两个高噪声真实数据集 Leaves、Income 及 34 个模拟数据集上，作者将补全结果接入五种标签集成算法。34 个模拟数据集的平均集成准确率中，LDELC 对多数算法取得 58.18%–58.76%，而 WSLC 对应为 46.78%–48.64%；相较 LDPLC，LDELC 也在五种集成算法上均提高平均准确率（PDF 第10–11页）。

## 贡献与局限
本文针对高噪声情形把工人质量估计与低质量工人标签分布增强结合起来，并以真实与模拟数据验证其对后续标签集成的帮助。评估所覆盖的真实数据集数量有限，且效果依赖工人质量划分与噪声结构；论文未证明在任意众包平台分布下都能保持相同收益。

---
DOI: 10.1109/tpami.2026.3721048
