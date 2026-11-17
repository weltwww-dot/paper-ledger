# F2Mamba: Fine-grained forgery-aware Mamba for image manipulation localization 总结

## 基本信息
- **标题**: F2Mamba: Fine-grained forgery-aware Mamba for image manipulation localization
- **作者**: Zi-Ying Zhao、Nan-Run Zhou、Ya-Yuan Luo 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109473
- **发表**: 2026-08-05
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109473

## 一句话概括
F2Mamba 融合多尺度全局表征与细粒度取证线索，在图像篡改定位基准上优于多种比较模型，但对极小篡改区域和弱取证线索仍易失效。

## 问题与动机
如何在较低计算开销下同时利用全局依赖和局部取证痕迹，实现像素级篡改区域定位？

## 方法
以 VMamba 提取多尺度全局特征，细粒度伪造感知适配器融合局部线索，并由伪造引导解码器和条件随机场细化掩码边界。

## 实验与结果
在 CASIAv1、NIST16、IMD2020、Coverage 等公开数据集及两种测试协议下，与 11 种基线比较；Protocol-CAT 平均 F1 为 69.92%、IoU 为 61.26%，扰动测试覆盖 JPEG 压缩、模糊和噪声，但失败案例显示极小区域及弱线索仍难定位（PDF 第6–14页）。

## 贡献与局限
将局部取证线索、全局建模和边界细化整合为统一定位框架，并报告跨数据集、扰动和效率评估；对模糊等图像退化的稳健性仍有限，结果应作为数字取证辅助证据而非单独裁定依据。

---
DOI: 10.1016/j.neunet.2026.109473
