# Robust out-of-distribution detection under noisy labels 总结

## 基本信息
- **标题**: Robust out-of-distribution detection under noisy labels
- **作者**: Yujin Lee、Seokho Kang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109826
- **发表**: 2026-11-03
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109826
- **PDF**: [NN_2026_NoisyLabelOOD.pdf](papers/NN_2026_NoisyLabelOOD.pdf)

## 一句话概括
将噪声标签学习与训练后的分布外检测结合，并区分训练增强对分类准确率和异常检测的影响。

## 问题与动机
训练集标签存在错误时，分类模型学到的边界会干扰分布内与分布外样本的区分。提高已知类分类准确率的策略，也可能弱化检测所用的置信度或特征信号。

## 方法
在若干噪声标签学习方案上接入不同的事后OOD评分方法。作者分别检验半监督学习中的预测锐化和Mixup，考察它们对近分布外、远分布外检测的影响。

## 实验与结果
CIFAR-10N、CIFAR-100N和Tiny-ImageNet上的OpenOOD对照显示，噪声标签学习总体有助于检测，近分布外场景受益尤其明显。部分配置中，Mixup虽提高分布内准确率，却使OOD检测退化（PDF第7–20页）。

## 贡献与局限
给出了针对检测任务调整噪声学习组件的实证依据。收益随噪声形态、检测评分和基准组合变化，三类图像基准无法代表全部真实分布偏移。

---
DOI: 10.1016/j.neunet.2026.109826 | PDF: [NN_2026_NoisyLabelOOD.pdf](papers/NN_2026_NoisyLabelOOD.pdf)
