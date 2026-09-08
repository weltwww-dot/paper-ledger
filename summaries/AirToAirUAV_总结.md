# An Efficient and Accurate YOLO-Based Framework for Air-to-Air UAV Detection 总结

## 基本信息

- **标题**: An Efficient and Accurate YOLO-Based Framework for Air-to-Air UAV Detection
- **作者**: Rijun Wang、Xianglong Teng、Chunhui Yang et al.
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构获取全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109609
- **arXiv**: 无
- **PDF**: [NN_2026_AirToAirUAV.pdf](papers/NN_2026_AirToAirUAV.pdf)

## 一句话概括

论文以三种轻量模块改造 YOLO，在复杂空中背景下提升小型无人机目标检测精度，同时把模型规模控制到适合资源受限飞行平台实时部署的水平。

## 问题与动机

低空交通和多无人机协同要求飞行器实时识别周围空中目标，但远距离无人机尺寸小、背景复杂且机载算力有限。较重检测器难以部署，普通轻量 YOLO 又容易在多尺度特征和小目标表达上损失精度。

## 方法

框架加入 ASF-P 增强多尺度特征融合，以 AB-CGLU 的注意力机制强化关键目标表示，并用 ADown 实现高效下采样。三者共同改善小目标信息保留、背景抑制与计算效率，在紧凑网络中兼顾准确率和速度。

## 实验与结果

主数据集上，模型达到 98.1% Precision、84.4% Recall、91.6% mAP@0.5 和 57.1% mAP@0.5:0.95，仅含 2.03M 参数、存储为 4.7MB；mAP@0.5 比 YOLOv8n 高 12.6 个百分点，并超过若干更重的 YOLO 变体。三个独立跨数据集实验也显示较强泛化能力。

## 贡献与局限

贡献是提供兼顾高精度、轻量化和跨数据集表现的空对空无人机检测方案。局限是视觉检测仍会受极端天气、强眩光、运动模糊和超远距离目标影响；真实飞行中的延迟、功耗及安全冗余还需系统级测试。

---
DOI: 10.1016/j.neunet.2026.109609
