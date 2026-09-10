# Dilated multi-Layer perceptron mixer for faster neural networks 总结

## 基本信息
- **标题**: Dilated multi-Layer perceptron mixer for faster neural networks
- **作者**: Van-Dung Hoang, Xuan-Thuy Vo, Kang-Hyun Jo
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108939
- **PDF**: [NN_2026_DilatedMLPMixer.pdf](papers/NN_2026_DilatedMLPMixer.pdf)

## 一句话概括
论文引入膨胀 token mixing，扩大 MLP-Mixer 的空间感受野并降低高分辨率视觉任务的计算负担。

## 问题与动机
既有 MLP-Mixer 的空间 MLP 随分辨率产生较高复杂度，并且固定输入尺寸导致迁移时需要插值 MLP 权重。视觉下游任务需要更灵活、高效的空间交互。

## 方法
模型在 token mixing 中加入 dilated 连接，以不同间隔聚合空间位置，形成多尺度上下文；同时保留通道混合和 MLP 的简单计算路径，避免依赖 self-attention。

## 实验与结果
分类、实例分割和目标检测实验表明该方法兼顾速度与视觉任务性能。摘要未列出完整数值。

## 贡献与局限
贡献是用膨胀混合改善 MLP-Mixer 的感受野和迁移效率。局限是膨胀率、层数及硬件实现会影响实际收益。

---
DOI: 10.1016/j.neunet.2026.108939
