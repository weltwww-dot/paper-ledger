# DAMFusion: An end-to-end degradation-aware multi-modal image fusion framework 总结

## 基本信息
- **标题**: DAMFusion: An end-to-end degradation-aware multi-modal image fusion framework
- **作者**: Junjie Ma、Peng Hu、Yi Li
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109822
- **发表**: 2026-11-03
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109822
- **PDF**: [NN_2026_DAMFusion.pdf](papers/NN_2026_DAMFusion.pdf)

## 一句话概括
根据输入的退化特征选择少量专家，将受损的红外、可见光或医学图像融合为保留互补信息的图像。

## 问题与动机
多模态图像可能同时出现亮度不足、模糊、分辨率损失和噪声。固定的融合过程很难针对不同输入决定应保留哪种模态的哪些特征。

## 方法
DAMFusion以两阶段自编码器为骨干，将CLIP提供的退化语义接入两组异构稀疏专家，分别支持退化特征处理与融合。基于互信息和KL散度的约束减少路由塌缩，促进专家分工。

## 实验与结果
论文比较了红外–可见光与医学图像融合，并在M3FD、LLVIP和MSRS上汇总消融。完整模型综合表现较好，个别指标仍由其他配置领先（PDF第6–11页）。

## 贡献与局限
提供了让融合网络随退化组合调整专家的机制。退化建模依赖伪真值，陌生退化的表现仍需检验，专家网络也会增加部署开销。

---
DOI: 10.1016/j.neunet.2026.109822 | PDF: [NN_2026_DAMFusion.pdf](papers/NN_2026_DAMFusion.pdf)
