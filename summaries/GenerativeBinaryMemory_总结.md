# Generative binary memory: Pseudo-Replay class-Incremental learning on binarized embeddings 总结

## 基本信息

- **标题**: Generative binary memory: Pseudo-Replay class-Incremental learning on binarized embeddings
- **作者**: Yanis Basso-Bert, William Guicquero, Anca Molnos, Romain Lemaire, Antoine Dupret
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108884
- **arXiv**: 无
- **PDF**: [NN_2026_GenerativeBinaryMemory.pdf](papers/NN_2026_GenerativeBinaryMemory.pdf)

## 一句话概括

GBM在二值嵌入空间中生成伪回放样本，使类增量学习同时适用于普通网络和资源受限的二值神经网络。

## 问题与动机

类增量学习需要学习新类而不遗忘旧类，但保存原始数据或运行大型生成模型代价较高。嵌入二值化有利于嵌入式部署，却使旧类分布的表达和回放更加困难。

## 方法

GBM使用Bernoulli混合模型在潜在二值空间模拟类别分布的多种模式，并生成合成二值伪实例。专门的特征二值器使方法可接入常规DNN，也能直接支持BNN；伪回放用于约束新旧类表示。

## 实验与结果

在带二值器的ResNet-18上，GBM相对最新方法在CIFAR100平均精度提高2.9%，在TinyImageNet提高1.5%；在BNN增量学习中最终精度提高3.1%，并在CORE50上实现4.7倍内存减少。

## 贡献与局限

贡献是提出面向二值嵌入的生成式伪回放，并兼顾普通DNN与BNN。局限是混合模型假设和二值表示可能限制复杂类分布，长序列增量任务、真实传感器数据和生成样本偏差仍需检验。

---
DOI: 10.1016/j.neunet.2026.108884
