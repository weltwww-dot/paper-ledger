# GTPF: Modality-specific graph transformer with prompt-aware fusion for multimodal sentiment analysis 总结

## 基本信息
- **标题**: GTPF: Modality-specific graph transformer with prompt-aware fusion for multimodal sentiment analysis
- **作者**: Haolong Zheng、Yan Leng、Jianing Wu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109498
- **发表**: 2026-08-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109498

## 一句话概括
本文提出 GTPF，将模态专属图 Transformer 与提示感知融合结合，以改善文本、音频和视觉信号间关系建模及多模态情感分析。

## 问题与动机
多模态情感模型若忽略各模态自身结构或仅作简单融合，可能难以捕捉跨模态互补关系和细粒度情绪线索。

## 方法
为不同模态构建图结构表示并采用图 Transformer 编码，再通过提示感知融合整合模态信息，完成情感回归与分类任务。

## 实验与结果
在 CMU-MOSI 与 CH-SIMS 等基准上与现有多模态方法比较；摘要报告 CMU-MOSI 的 MAE 相对第二名改善最高 13.76%，CH-SIMS 的相关系数提高 6.01%、五分类准确率提高 5.03%。这些是相对改变量，评测范围限于所用语料与指标（PDF 第 8–10 页）。

## 贡献与局限
研究显示模态专属图建模与提示引导融合在所测情感语料上有效；对语料偏差、语言迁移和真实场景情绪识别的适用性尚需评估。

---
DOI: 10.1016/j.neunet.2026.109498
