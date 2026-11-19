# Cross-city few-shot spatiotemporal graph forecasting via masked pre-training and prompt tuning 总结

## 基本信息
- **标题**: Cross-city few-shot spatiotemporal graph forecasting via masked pre-training and prompt tuning
- **作者**: Xianwei Guo、Zhiyong Yu、Jiangtao Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109553
- **发表**: 2026-08-27
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109553

## 一句话概括
ST-MPPT先在数据丰富城市进行空间与时间解耦掩码预训练，再以记忆检索生成输入自适应提示，迁移到少样本目标城市。

## 问题与动机
城市交通预测常面临新城市数据稀缺，直接迁移源城市模型会受空间结构和时间分布差异影响；现有预训练未充分提取时空元知识，固定知识检索提示也难适配不同目标城市。

## 方法
ST-MPPT分别用空间和时间Transformer编码器对源城市数据进行掩码重建预训练，形成空间、时间表征。下游阶段将编码表示构成图结构并增强时空预测器；提示网络从可学习的时空键值记忆库检索相关信息，自适应加权、融合为输入相关提示，调节冻结预训练编码器以适应目标城市，仅用少量目标样本微调。

## 实验与结果
在METR-LA、PEMS-BAY、Didi-Chengdu和Didi-Shenzhen四个真实数据集上进行跨城少样本预测，与统计、常规STGNN、预训练和迁移基线比较，报告5、15、30分钟MAE/RMSE，并用t检验标记显著差异。消融中METR-LA 5分钟MAE：仅空间掩码2.69、仅时间掩码2.57，完整提示/自适应配置约2.40；PEMS-BAY对应值约1.15、1.12和1.05。

## 贡献与局限
方法将解耦时空掩码预训练与可检索、可适配提示结合，面向跨城市少样本迁移，并在四个城市数据集上比较多种预测基线。提示记忆和预训练效果可能依赖源城市覆盖范围、目标城市采样量与元训练配置；从所报告实验看，极端分布变化和长期交通制度变化尚未评估。

---
DOI: 10.1016/j.neunet.2026.109553
