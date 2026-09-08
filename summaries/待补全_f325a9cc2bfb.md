# CoreKD: A Context-Aware Local Region Structural Contrastive Knowledge Distillation Framework for Object Detection 总结

## 基本信息

- **标题**: CoreKD: A Context-Aware Local Region Structural Contrastive Knowledge Distillation Framework for Object Detection
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已依据现有摘要完成中文结构化整理；具体细节以全文为准
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3672967
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

知识蒸馏(KD)旨在将知识从繁琐的老师转移到轻量级学生身上,从而在不牺牲性能的情况下降低整体模型的复杂性.为了验证CoreKD的功效,我们对公共MS COCO 2017和PASCAL VOC数据集进行了广泛的实验.

## 问题与动机

知识蒸馏(KD)旨在将知识从繁琐的老师转移到轻量级学生身上,从而在不牺牲性能的情况下降低整体模型的复杂性.

## 方法

知识蒸馏(KD)旨在将知识从繁琐的老师转移到轻量级学生身上,从而在不牺牲性能的情况下降低整体模型的复杂性.目前的方法往往过分注重像素级的知识转让,而忽略本地化和背景信息。为了解决这个问题,我们提出了一个新的具有上下文意识的局部区域结构对比性知识蒸馏框架(CoreKD),用于物体检测任务.具体而言,我们采用了一种基于补丁的语义结构蒸馏法(PSD),促进高效的本地化宝贵知识的转让。

## 实验与结果

为了验证CoreKD的功效,我们对公共MS COCO 2017和PASCAL VOC数据集进行了广泛的实验.这些结果显示,CoreKD显著提高了学生在物体检测任务中的性能,表明其能够传递宝贵的知识.

## 贡献与局限

这些制约因素可能转移学生和教师之间的区域背景信息,大大提高学生探测器模拟背景依赖性的能力。

---
DOI: 10.1109/tnnls.2026.3672967
