# Extending the scale generalization of the Vision Transformer without fine-tuning 总结

## 基本信息
- **标题**: Extending the scale generalization of the Vision Transformer without fine-tuning
- **作者**: Kai Jiang、Peng Peng、Youzao Lian 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109446
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109446

## 一句话概括
MSViT针对ViT改变输入尺度导致频率信息和空间先验退化，以频谱约束嵌入和尺度自适应注意力改善分类，但部分评估使用多尺度训练。

## 问题与动机
如何减轻分辨率变化引起的纹理损失和感受野退化？

## 方法
YCbCr patch作DCT并学习频率权重，结合水平垂直自适应注意力和重参数化位置编码。

## 实验与结果
在ImageNet-1K、真实标签集、ImageNet-V2测分类和效率，并评估多种分辨率；报告跨尺度准确率较稳定并分析高频衰减（PDF第8–10页）。

## 贡献与局限
提出频谱与感受野联合设计；多尺度训练结果不代表任意尺度免适配。

---
DOI: 10.1016/j.neunet.2026.109446
