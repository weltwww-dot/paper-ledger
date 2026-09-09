# Cross-Corpus Speech Emotion Recognition Based on Dynamically Filtering Multistage Diffusion Model 总结

## 基本信息

- **标题**: Cross-Corpus Speech Emotion Recognition Based on Dynamically Filtering Multistage Diffusion Model
- **作者**: Jingjie Yan、Boyan Sun、Yuebo Yue、Xiaoyang Zhou、Ying Liu
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3681265
- **arXiv**: 无
- **PDF**: [TAI_2026_CrossCorpusSpeechEmotion.pdf](papers/TAI_2026_CrossCorpusSpeechEmotion.pdf)

## 一句话概括

本文提出动态过滤多阶段扩散模型 DFMDM，通过“生成—过滤—增强”迭代过程筛除不符合目标语料分布的伪样本，提升跨语料语音情感识别的迁移效果。

## 问题与动机

跨语料语音情感识别面临录音环境、说话人、语言风格和情感分布差异，目标语料标注样本又通常不足。现有生成式迁移方法可以补充伪样本，但生成样本与目标域声学—语义特征未必对齐，低质量样本甚至会把噪声引入迁移过程。作者希望在生成目标域样本的同时建立动态质量控制机制，并通过迭代增强逐步提高伪样本的域一致性。

## 方法

DFMDM 采用三阶段迭代优化。第一阶段用条件扩散模型和对抗域分类器引导生成具有目标域特征的伪样本；第二阶段根据伪样本与目标域特征的相似度动态调整阈值，过滤明显偏离目标域的低质量样本；第三阶段将保留下来的伪目标样本与源域样本混合，再生成更接近目标域的样本，形成“生成—过滤—增强”的闭环。该过程在训练期间逐步更新伪样本质量，而不是一次性使用固定阈值或静态生成数据。

## 实验与结果

实验使用 CASIA、EmoDB、eNTERFACE 和 IEMOCAP 四个语料库，按照八种跨语料迁移方向评估无偏准确率（UAR）和加权准确率（WAR）。在 C→B 任务中，DFMDM 的 UAR 达到 66.66%，高于 DADR 的 63.61%、MDSA 的 65.59% 和 L-DA 的 58.13%，WAR 达到 68.39%；在类别不平衡的 EmoDB 相关迁移任务中仍保持较高 WAR。阈值和策略消融表明，动态过滤与迭代增强共同改善伪样本的分布一致性，生成样本的声学特征也更接近真实目标域样本。

## 贡献与局限

- 将条件扩散生成、动态伪样本过滤和源—目标混合增强组织成可迭代的跨语料迁移流程。
- 通过动态相似度阈值降低低质量伪样本对情感分类器的干扰，改善类别不平衡条件下的迁移表现。
- 在四个语料库和多种迁移方向上取得比主流方法更好的 UAR/WAR，并用可视化验证生成样本的域一致性。
- 局限：多阶段扩散过程计算开销较大，对高质量声谱图特征和预处理差异较敏感；当前主要使用单模态语音信息，后续可探索轻量扩散结构和多模态情感特征。

---
DOI: 10.1109/tai.2026.3681265
