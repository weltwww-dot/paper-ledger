# Multiobjective Simulated Annealing-Based Stopwords Substitution for Rubbish Text Attack 总结

## 基本信息

- **标题**: Multiobjective Simulated Annealing-Based Stopwords Substitution for Rubbish Text Attack
- **作者**: Chen Li, Xinghao Yang, Ao Wang, Yongshun Gong, Baodi Liu, Weifeng Liu
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-03-24
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3675368
- **arXiv**: 无
- **PDF**: [NN_2026_MultiobjectiveSimulatedAnnealingStopwords.pdf](papers/NN_2026_MultiobjectiveSimulatedAnnealingStopwords.pdf)

## 一句话概括

本文提出 MOSA-S2，用无意义 stopwords 替换语义词，并以多目标模拟退火生成保持模型原预测、却对人类更不可理解的 rubbish text，用于授权的模型鲁棒性评估与防御改进。

## 问题与动机

文本对抗样本通常研究模型对微小变化的过度敏感，而 rubbish examples 关注模型对大量、语义相关变化的过度不敏感。既有方法把修改率和模型置信度压成单一目标，容易陷入局部最优；删除词或替换介词等简单操作也限制了样本的多样性。系统地暴露这种失配，有助于评估模型是否真正利用上下文语义并设计防御。

## 方法

MOSA-S2 依据词重要性优先选择不重要词，并以 stopwords 构造单词和双词复合扰动。候选样本先经过模型查询，仅保留预测标签不变的样本，再用 Pareto 非支配排序同时优化模型置信度 MC 和修改率 MR。模拟退火中的 Metropolis 接受概率允许暂时接受较差候选以跳出局部最优，温度下限随输入长度自适应；另有词性约束变体改善可读性，使语义偏离与人类判断之间形成可控评估。

## 实验与结果

作者在 MR、IMDB、AG News、SNLI、MRPC、QQP 六个数据集上攻击 CNN、LSTM、BERT、RoBERTa、ALBERT、DistilBERT 和 XLNet，并与 Input Reduction（IR）和 AGPS 比较，每个数据集随机取 500 个实例。MOSA-S2 的平均 MC 比 IR 高 11.39%、比 AGPS 高 3%，平均 MR 分别高 6.54% 和 4.19%；PPL 比 IR 高 29.84%、比 AGPS 高 13.05%。在 MRPC 的 BERT 消融中，去除非支配排序使 MC/MR 下降 7.06%/4.22%，去除温度接受机制使平均 MC/MR 下降 3.75%/3.25%；扩大词表时，MR 的 PPL 从 100.78 增至 259.18，MC 从 98.73% 升至 99.96%。

## 贡献与局限

贡献是：将 stopwords 替换、词重要性复合扰动和多目标退火结合，提升 rubbish text 的不可理解性与模型置信度保持；跨六类任务和七种模型揭示了 NLP 模型对无意义序列的过度不敏感，且对抗再训练能缓解该问题。局限是当前评估仍集中于文本分类和既有模型，未来需检验预训练语言模型及解释方法，并研究过度敏感与过度不敏感之间的鲁棒性折中。

---
DOI: 10.1109/TNNLS.2026.3675368
