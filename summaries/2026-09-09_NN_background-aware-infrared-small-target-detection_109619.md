# Background-aware decoupling and multi-granularity fusion-reconstruction approach for infrared small target detection 总结

## 基本信息
- **标题**: Background-aware decoupling and multi-granularity fusion-reconstruction approach for infrared small target detection
- **作者**: Xin Pan、Tao Chen、Huayue Chen
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109619
- **发表**: 2026-09-09
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109619

## 一句话概括
BAMFNet将红外图像迭代分解为背景与稀疏小目标，分别增强背景上下文和保留目标像素，再进行多粒度融合重建。

## 问题与动机
红外小目标只占少量像素，容易与复杂背景纹理混淆；常见多层下采样会平滑甚至丢失目标像素，造成漏检和虚警。既有方法往往强化目标而未充分建模背景，无法有效消除背景干扰。

## 方法
BAMFNet将图像拆为背景B与小目标T，借鉴低秩背景和稀疏目标先验构造可学习迭代更新。背景分支BFEM提取连续结构，GL-PAAM以局部/全局层级融合和patch注意力筛选关键背景区域；目标分支STEM以空洞卷积替代池化，模拟稀疏近端更新而不降低分辨率。MGFRM用1×1、3×3、5×5卷积汇聚细、中、粗粒度信息，逐阶段提升目标—背景对比。

## 实验与结果
在NUDT-SIRST、IRSTD-1k和SIRST-Aug上与传统低秩/局部方法及ACM、DNANet、UIUNet、SCTransNet、MSHNet等比较，评价mIoU、F1、检测率Pd和虚警率Fa。BAMFNet三集mIoU/F1/Pd/Fa分别为94.45%/97.14%/98.41%/1.22×10⁻⁵、66.05%/79.55%/91.40%/4.91×10⁻⁵、75.10%/85.78%/98.62%/30.71×10⁻⁵。SIRST-Aug合成背景干扰下虽有最高Pd，但Fa明显高于若干基线；消融和多粒度核分析用于检验模块作用。

## 贡献与局限
贡献在于把背景抑制与微弱目标保留并列建模，并将低秩—稀疏分解思想转为端到端可学习迭代，再以多粒度重建融合。NUDT-SIRST上mIoU/F1达94.45%/97.14%，SIRST-Aug上检测率98.62%，但虚警率30.71×10⁻⁵，显示合成尖锐干扰可穿透背景先验并被目标增强分支放大；复杂背景仍是实质局限。

---
DOI: 10.1016/j.neunet.2026.109619
