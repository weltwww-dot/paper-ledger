# GSLoRa: Gradient spectral alignment for low-rank adaptation 总结

## 基本信息
- **标题**: GSLoRa: Gradient spectral alignment for low-rank adaptation
- **作者**: Qingyun Lin、Lilan Peng、Zhendong Wu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109436
- **发表**: 2026-08-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109436

## 一句话概括
GSLoRA针对LoRA收敛和梯度噪声问题，以任务梯度谱校准低秩更新，在多类语言任务改善表现，但增加初始化成本。

## 问题与动机
如何利用任务梯度确定有效低秩适配方向？

## 方法
对多批梯度协方差作谱分解并缩放主方向初始化低秩矩阵，双投影降噪并动态调整特征值。

## 实验与结果
在T5-Base GLUE及LLaMA 2-7B生成任务比较微调方法；梯度方差报告为标准LoRA的38.2%，GSLoRA约7M参数、19.75GB显存、222分钟/轮，另需6分钟初始化（PDF第7–10页）。

## 贡献与局限
提出梯度谱引导的参数高效微调；结论限于所测任务且含预处理成本。

---
DOI: 10.1016/j.neunet.2026.109436
