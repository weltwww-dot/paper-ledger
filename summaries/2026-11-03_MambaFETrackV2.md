# Mamba-FETrack V2: Revisiting state space model for frame-event based visual object tracking 总结

## 基本信息
- **标题**: Mamba-FETrack V2: Revisiting state space model for frame-event based visual object tracking
- **作者**: Shiao Wang、Ju Huang、Qingchuan Ma 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109823
- **发表**: 2026-11-03
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109823
- **PDF**: [NN_2026_MambaFETrackV2.pdf](papers/NN_2026_MambaFETrackV2.pdf)

## 一句话概括
以动态提示和状态空间融合联合处理RGB帧与事件流，改善复杂场景中的目标跟踪。

## 问题与动机
普通相机易受快速运动、弱光和模糊影响，事件相机可补充运动变化，但两种传感器的时间和信号特性不同，需要随场景调整融合方式。

## 方法
从共享提示池选择适合当前RGB与事件特征的动态提示，交由FEMamba联合融合。跟踪头估计目标位置并依据置信分数更新模板。

## 实验与结果
论文在COESOT短时任务以及FE108、FELT长时任务上比较跟踪效果。FELT含1044个序列，按730个训练、314个测试划分。对照及消融支持动态提示和融合设计（PDF第6–7页）。

## 贡献与局限
把状态空间融合用于短时和长时的双传感器跟踪。实际应用需成对传感数据，效果依赖传感器配置和时空对齐，模型结构的计算优势也需结合部署平台测量。

---
DOI: 10.1016/j.neunet.2026.109823 | PDF: [NN_2026_MambaFETrackV2.pdf](papers/NN_2026_MambaFETrackV2.pdf)
