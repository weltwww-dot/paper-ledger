# STEANet: Efficiently learning spatio-temporal affective representations from videos 总结

## 基本信息
- **标题**: STEANet: Efficiently learning spatio-temporal affective representations from videos
- **作者**: Jin Zhou、Yun Yi、Hanli Wang 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **卷期 / 文章号**: 362，文章号104660
- **发表**: 2026-11-14
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104660 | 📄 [AIJ_2026_steanet-spatiotemporal-video-emotion_104660.pdf](papers/AIJ_2026_steanet-spatiotemporal-video-emotion_104660.pdf)
- **PDF许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 一句话概括
STEANet在预训练视觉Transformer中加入轻量时序与空间适配器，以较少可训练参数提取视频情绪线索。

## 问题与动机
视频情绪识别需要同时理解跨帧变化与帧内局部线索，逐帧特征方法难以充分表达时空情绪信息；完整微调视频模型又带来较高训练成本。作者检验能否在图像预训练CLIP-ViT上用参数高效迁移学习补足视频建模能力。

## 方法
STEANet以CLIP-ViT为骨干，在STE-ViT块中并联两个瓶颈适配器：TEA沿时间维对局部patch序列做一维卷积，提取跨帧情绪变化；SEA通过切片、降维和1×1二维卷积编码空间局部上下文，再升维接回主干。只微调适配器参数，结合原有注意力保留全局表征；分类使用视频级特征。

## 实验与结果
在VideoEmotion-8、Ekman-6等四个视频情绪数据集及Diving-48细粒度动作集评测，并比较全量微调、既有参数高效方法和适配器消融。Ekman-6上加入TEA与SEA后Top-1准确率为60.64%；论文报告相对AdaptFormer提升4.28%。在Ekman-6扩大卷积核反而降低准确率；全12个ViT块插入适配器取得VE-8 56.72%、EK-6 60.64%。

## 贡献与局限
研究展示了以视觉单模态骨干和少量可训练适配器联合学习时空情绪线索的方案，并在多个情绪集及动作识别集报告竞争性结果。其代价是适配器带来额外计算与训练、测试时间；情绪类别仍有视觉相似导致的混淆（如Ekman-6的快乐与惊讶）。作者将音频融合列为后续方向，因此当前主方法的主要结果不能视为完整多模态情绪识别证据。

---
DOI: 10.1016/j.artint.2026.104660 | 📄 [AIJ_2026_steanet-spatiotemporal-video-emotion_104660.pdf](papers/AIJ_2026_steanet-spatiotemporal-video-emotion_104660.pdf)
