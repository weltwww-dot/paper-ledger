# Position-aware Attentional Neural Network for Review-based Recommendation 总结

## 基本信息

- **标题**: Position-aware Attentional Neural Network for Review-based Recommendation
- **作者**: Yuanpeng Jiang、Teng Long、Zhangbing Zhou
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109585
- **arXiv**: 无
- **PDF**: [NN_2026_Paper06.pdf](papers/NN_2026_PAAN_PositionAwareRecommendation.pdf)

## 一句话概括

PAAN 将评论中词语和句子的位置信息纳入注意力，以提升稀疏交互下的评论推荐。

## 问题与动机

评论包含用户偏好和物品属性，但现有评论推荐主要利用词汇和语义线索，忽略重要信息在评论中的位置分布。稀疏用户–物品交互进一步放大了这一问题。研究希望显式建模位置并改善用户与物品表示的对齐。

## 方法

PAAN 的 position-aware excitation 模块把可学习位置嵌入与上下文特征结合，重新校准注意力并突出信息性 token。双重交叉注意力进一步对齐用户和物品表示，使评论特征参与结构化、个性化的相关性学习。

## 实验与结果

模型在 Digital Music、Health and Personal Care、Home and Kitchen、Movies and TV、Yelp 五个高度稀疏数据集上进行评分预测。相较基线，全文报告 MSE 平均改善 2.49%、MAE 平均改善 4.86%，并持续优于已有评论推荐方法。

## 贡献与局限

贡献是把位置作为评论推荐的一等信号，并以双交叉注意力连接用户–物品表示。局限是结果集中在评分预测和五个数据集，位置编码在不同语言、评论结构和非评分推荐任务中的泛化仍需验证。

---
DOI: 10.1016/j.neunet.2026.109585

