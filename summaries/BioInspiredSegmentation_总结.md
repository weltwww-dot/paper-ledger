# Biologically-inspired semi-supervised semantic segmentation for biomedical imaging 总结

## 基本信息

- **标题**: Biologically-inspired semi-supervised semantic segmentation for biomedical imaging
- **作者**: Luca Ciampi、Gabriele Lagani、Giuseppe Amato、Fabrizio Falchi
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108925
- **arXiv**: 无
- **PDF**: [NN_2026_Paper05.pdf](papers/NN_2026_BiologicallyInspiredSemiSupervisedSegmentation.pdf)

## 一句话概括

本文用 Hebbian 局部学习预训练分割网络，再以少量标注数据进行半监督微调。

## 问题与动机

生物医学图像分割通常需要昂贵的像素级标注，而标注稀缺会限制深度模型训练。完全依赖反向传播也不符合作者希望借鉴的生物启发学习方式。研究因此探索无需反向传播的无监督特征发现与少量标注微调的组合。

## 方法

方法采用下采样–上采样结构的两阶段训练。第一阶段用“fire together, wire together”Hebbian 规则更新卷积和转置卷积层权重，不使用反向传播，以无监督方式发现数据特征。第二阶段仅用少量标注数据通过标准反向传播微调，并将该初始化用于现有 SOTA 方法。

## 实验与结果

作者在多个常用生物医学数据集、不同标注比例下评测。结果显示，该方法在不同标签可用程度下优于 SOTA；用 Hebbian 阶段初始化其他 SOTA 方法也能提升性能。摘要未列出各数据集的具体数值，故不补写数字。

## 贡献与局限

贡献是将生物启发局部学习与半监督分割结合，并提供可复现实验代码。局限是效果依赖网络结构、Hebbian 超参数和少量标注质量，跨模态医学图像及临床部署仍需验证。

---
DOI: 10.1016/j.neunet.2026.108925

