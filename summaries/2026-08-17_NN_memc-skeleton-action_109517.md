# MEMC: Masked modeling with efficient and minimal contrastive learning for self-supervised skeleton-based action recognition 总结

## 基本信息
- **标题**: MEMC: Masked modeling with efficient and minimal contrastive learning for self-supervised skeleton-based action recognition
- **作者**: Yingfei Wu、Wenming Cao、Xinpeng Yin
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109517
- **发表**: 2026-08-17
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109517

## 一句话概括
MEMC以先掩码骨架建模、后对比学习的级联训练降低目标冲突，并结合骨架拓扑先验，在NTU RGB+D及PKU-MMD动作识别评测中取得有竞争力的自监督表征。

## 问题与动机
掩码重建偏重保留细粒度结构，而对比学习强调语义不变性，同时优化可能产生梯度冲突并增加训练难度。

## 方法
先以掩码骨架建模学习结构与运动表征，再通过层 graft 预训练进行对比式语义细化；另用骨架拓扑距离先验传播关节关系，并采用频带感知对比表征。

## 实验与结果
在线性评估中，MEMC在NTU-60跨主体/跨视角为86.8%/90.5%，NTU-120为79.2%/80.5%，PKU-MMD Part II为56.4%；在NTU-60半监督评估中1%标注跨主体准确率为69.3%。结果来自特定骨架基准和协议，真实视频及跨数据域表现未由这些实验确定（PDF 第 7–10 页）。

## 贡献与局限
以顺序级联整合结构重建与语义对比学习，并用拓扑先验强化骨架关系，在多个标准协议上取得较强结果；收益仍依赖骨架输入质量、预训练流程与评测数据分布。

---
DOI: 10.1016/j.neunet.2026.109517
