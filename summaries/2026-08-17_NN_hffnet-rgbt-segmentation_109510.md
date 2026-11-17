# HFFNet: Hierarchical feature fusion network for lightweight RGB-T semantic segmentation 总结

## 基本信息
- **标题**: HFFNet: Hierarchical feature fusion network for lightweight RGB-T semantic segmentation
- **作者**: Xiaoling Wu、Xiaofei Zhou、Liuxin Bao 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109510
- **发表**: 2026-08-17
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109510

## 一句话概括
HFFNet通过多尺度RGB-热红外特征融合与层级整合实现轻量语义分割，在论文评测的RGB-T基准上改善多模态信息利用并控制模型复杂度。

## 问题与动机
RGB与热红外图像的互补信息有助于复杂光照下分割，但跨模态与多层特征融合会增加模型开销，且小目标和边界仍具挑战。

## 方法
多尺度特征融合模块以并行级联的深度可分离卷积整合两种模态，层级整合模块再投影并融合不同层级特征，以较轻结构连接细节和高层语义。

## 实验与结果
作者在RGB-T语义分割基准上与现有方法比较，并进行模块消融及复杂度评估，报告整体分割性能和轻量化表现；论文结论同时指出边界细化与小目标建模仍是后续改进方向（PDF 第 7–12 页）。

## 贡献与局限
提出适配RGB-T语义分割的轻量多尺度与层级融合架构，并通过基准比较和消融检验模块作用；现有结果不能消除边界和小目标上的剩余误差。

---
DOI: 10.1016/j.neunet.2026.109510
