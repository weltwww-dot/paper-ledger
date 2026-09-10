# Similarity-guided state attention for visual reinforcement learning 总结

## 基本信息

- **标题**: Similarity-guided state attention for visual reinforcement learning
- **作者**: Yinfeng Zeng, Xuesong Wang, Yuhu Cheng
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109560
- **arXiv**: 无
- **PDF**: [NN_2026_SimilarityGuidedStateAttention.pdf](papers/NN_2026_SimilarityGuidedStateAttention.pdf)

## 一句话概括

SSA 利用原始与增强观察的状态嵌入相似性生成状态注意图，使视觉强化学习策略更关注任务相关区域并提高未见环境泛化。

## 问题与动机

视觉强化学习容易被冗余信息和无关因素干扰，数据增强虽有帮助，却可能造成过拟合和环境外泛化退化。作者希望通过自监督的注意图对齐获得更稳健的状态表示。

## 方法

Similarity Guidance Module 根据原始和增强观察的状态嵌入相似性，引导编码器在原始观察中聚焦任务相关区域。增强观察的注意图由状态嵌入解码得到，原增强注意图之间的余弦相似度与二元交叉熵共同构成自监督目标。

## 实验与结果

在 DeepMind Control Generalization Benchmark 上，SSA 相较代表性视觉强化学习基线取得更好的稳健性和泛化性能。实验围绕状态表示质量及下游控制策略进行比较，摘要未报告统一的具体数字。

## 贡献与局限

贡献是把相似性引导的状态注意和注意图对齐目标结合起来，减少视觉干扰。局限是验证依赖 DMControl-GB 和特定增强策略，真实机器人视觉噪声及更复杂任务上的收益仍需检验。

---
DOI: 10.1016/j.neunet.2026.109560
