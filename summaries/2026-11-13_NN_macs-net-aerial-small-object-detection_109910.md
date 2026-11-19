# MACS-Net: Multi-scale semantic alignment and context spatial gating for small object detection in aerial images 总结

## 基本信息
- **标题**: MACS-Net: Multi-scale semantic alignment and context spatial gating for small object detection in aerial images
- **作者**: Zhilu Cao、Yuzhen Xu、Wentao Lyu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109910
- **发表**: 2026-11-13
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109910

## 一句话概括
MACS-Net 在 YOLO11s 上加入上下文空间门控与多尺度语义对齐，改善航拍小目标特征融合和背景抑制。

## 问题与动机
航拍小目标像素少、密集且易受背景干扰，常规跨尺度上采样融合还会造成语义漂移与空间错位，导致漏检和相邻目标难分。

## 方法
骨干网络加入轻量上下文空间门控块（CSGB），增强高层小目标响应；颈部网络构建多尺度语义对齐 FPN，以残差语义流对齐模块（RSFA）把深层语义映射到浅层坐标，并用跨阶段部分多尺度卷积块（CSP_MSCB）强化尺度上下文。

## 实验与结果
在两个航拍检测数据集上与 YOLO 系列及其他检测器比较，使用精确率、召回率、mAP@0.5、mAP@0.5:0.95、参数量和 GFLOPs，并进行模块消融。表格区分同设置重训结果与引用结果；对比覆盖 SIMD。

## 贡献与局限
将空间抑噪与语义坐标对齐分别放在骨干和颈部，目标是兼顾密集小目标区分及模型开销。评价仍是有限数据集上的离线检测；对不同传感器、跨区域泛化及部署时延的结论需以全文表格所列实验设置为界。

---
DOI: 10.1016/j.neunet.2026.109910
