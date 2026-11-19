# Modality as heterogeneity: Node splitting and graph rewiring for multimodal graph learning 总结

## 基本信息
- **标题**: Modality as heterogeneity: Node splitting and graph rewiring for multimodal graph learning
- **作者**: Yihan Zhang、Ercan E. Kuruoglu
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109557
- **发表**: 2026-08-27
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109557

## 一句话概括
NSG将多模态图节点拆为模态子节点并按关系重连，以异构图神经网络和双分支专家减少模态混淆。

## 问题与动机
多模态图把不同模态特征合并到节点表征中，容易出现模态混淆：模态内相似性与跨模态关系被同一聚合过程混在一起，造成信息干扰和过拟合。研究尝试把模态差异直接编码为图结构，从而让消息传递区分关系类型。

## 方法
节点拆分图（NSG）将原节点转换为对应各模态的子节点，再构建节点内边与节点间边，并用局部最大生成树启发式稀疏化边集。异构图网络分别聚合自类型与跨类型关系，双分支专家处理两类结构并进行门控融合；模型据此学习模态相关表征，限制不必要的混合边以控制假设复杂度。

## 实验与结果
在Amazon-Fashion的Ele-fashion、Sports、Cloth等分类/链接任务及ABIDE、TADPOLE多模态数据上，与GCN、GraphSAGE、GAT、图MoE等比较。表8中Ele-fashion准确率从单专家86.52±0.07%提高至双分支配置87.40±0.24%；Sports链接任务的H@1、H@3、H@10和MRR均列出与基线的比较。四模态ABIDE与六模态TADPOLE实验还报告准确率、训练时间、显存和推理时间。

## 贡献与局限
方法以节点拆分和重连把模态异质性显式映射为图结构，并通过两类关系专家兼顾表达能力和计算成本；实验覆盖商品图、医学多模态数据及不同模态数。现有结果依赖构图阈值、模态可用性和数据集特征；从所报告实验看，边稀疏化对新领域图结构的敏感度及缺失模态时表现仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.109557
