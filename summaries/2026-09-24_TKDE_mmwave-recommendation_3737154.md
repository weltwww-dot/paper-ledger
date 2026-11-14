# Tackling the Modality Inhibitance Effect With Wavelet-Based Modality Integration in Multi-Modal Recommendation 总结

## 基本信息
- **标题**: Tackling the Modality Inhibitance Effect With Wavelet-Based Modality Integration in Multi-Modal Recommendation
- **作者**: Rongqing Kenneth Ong、Andy W. H. Khong
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8499-8514
- **发表**: 2026-09-24
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3737154

## 一句话概括
MMWave研究多模态推荐中的模态抑制现象，利用小波提取各模态关键信号，再以结构图学习和自适应调节整合信息。

## 问题与动机
新增模态可能带来噪声与冗余，使双模态模型扩展到三模态后反而退化；常见融合方式难以辨别互补信号和无效信息。

## 方法
小波分解并重建模态特征以保留重要成分，构造单模态及融合图传播高阶关系，再用跨权重调节模态与融合表示，配合对比学习训练。

## 实验与结果
在四个真实数据集上与基线比较，MMWave在报告指标上的平均提升为6.48%；消融任一关键组件均使表现下降，结构感知图学习的移除影响尤为明显（PDF第9–11、15页）。

## 贡献与局限
结果支持小波筛选与结构融合共同缓解模态抑制；三模态评估主要依赖TikTok数据，污染时文本可靠性较弱，且图构造预处理成本未计入部分效率比较（PDF第13–15页）。

---
DOI: 10.1109/tkde.2026.3737154
