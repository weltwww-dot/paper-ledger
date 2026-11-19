# Adaptive multimodal visual tracking via parameter-efficient vision transformers 总结

## 基本信息
- **标题**: Adaptive multimodal visual tracking via parameter-efficient vision transformers
- **作者**: Yixin Xu、Wenkang Zhang、Tianyang Xu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109531
- **发表**: 2026-08-20
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109531

## 一句话概括
SwitchTrack以动态模态融合桥和按传感器切换的低秩适配器统一RGB-D、RGB-T与RGB-E目标跟踪，在多个公开基准上兼顾跟踪表现和适配开销。

## 问题与动机
RGB、热红外、深度和事件传感器各有适用场景，现有跟踪器常为每种组合单独训练，造成参数冗余；固定融合权重也难适应模态质量随场景变化。目标是共用跟踪骨干，同时动态整合输入并低成本适配不同模态。

## 方法
SwitchTrack将各模态嵌入统一Transformer跟踪器，以Dynamic Bridge根据模态特征生成融合权重，并通过通道注意力整合信息。骨干主体共享冻结，LoRA适配器插入注意力和前馈层；推理时仅启用当前传感器组合对应的适配器，减少重复微调参数。

## 实验与结果
SwitchTrack在LasHeR（RGB-T）、RGBT234、VisEvent（RGB-E）、DepthTrack及VOT-RGBD2022等基准评估。融合对照中，Dynamic Bridge在LasHeR的PR为69.7、VisEvent的PR为77.6、DepthTrack的F-score为60.4；参数量为0.46M，计算量为28.36M MACs（表4单位栏标注为M），即0.02836 GMACs。这些指标分别对应不同数据集和指标。模态专属LoRA的秩设置为RGB-D 4、RGB-T 2、RGB-E 8。

## 贡献与局限
方法把模态自适应融合与任务选择式LoRA放进单一跟踪架构，降低多传感器方案重复训练和存储需求。论文也承认事件流稀疏且噪声较大，融合仍需改进；现有实验基准和场景不能完全代表更广泛传感器组合。

---
DOI: 10.1016/j.neunet.2026.109531
