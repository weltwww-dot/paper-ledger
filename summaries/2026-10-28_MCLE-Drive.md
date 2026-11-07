# Real-time multi-domain collaborative low-light image enhancement for driving safety 总结

## 基本信息
- **标题**: Real-time multi-domain collaborative low-light image enhancement for driving safety
- **作者**: Xiaoli Li、Zhiyuan Han、Kang Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109809
- **发表**: 2026-10-28
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109809
- **PDF**: [NN_2026_MCLE-Drive.pdf](papers/NN_2026_MCLE-Drive.pdf)

## 一句话概括
联合处理空间、通道和频率特征，改善夜间行车图像的可见性，并测试增强图像对目标检测的影响。

## 问题与动机
低照度会带来偏色、噪声与细节丢失。整体增亮可能放大噪点或造成局部过曝，夜间感知还需要兼顾增强质量与处理时延。

## 方法
MCLE-Net以快速傅里叶变换处理频域特征，通过稀疏空间和通道注意力筛选有用区域与特征。U形模块提取多尺度信息，门控融合按输入调整各尺度特征的贡献。

## 实验与结果
在LoLI-Street系列、LOL和LSRW等数据上，作者比较了有参考与无参考图像质量指标。论文的下游检测实验中，增强后mAP@0.5为0.887，mAP@0.5–0.95为0.854（PDF第15页）。

## 贡献与局限
把亮度恢复、细节增强和下游感知放在同一评价框架中。检测增益取决于数据、增强条件和检测器，实时性也需结合目标设备测量。

---
DOI: 10.1016/j.neunet.2026.109809 | PDF: [NN_2026_MCLE-Drive.pdf](papers/NN_2026_MCLE-Drive.pdf)
