# Benefiting From OOD Samples in Open-Set Semi-Supervised Object Detection 总结

## 基本信息

- **标题**: Benefiting From OOD Samples in Open-Set Semi-Supervised Object Detection
- **作者**: Yiqi Zou, Kuo Wang, Jichang Li, Chuan Wang, Shuangyin Liu
- **期刊 / 会议**: IEEE TNNLS 2026
- **发表**: 2026-06-15
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3659534

## 一句话概括

针对开放集半监督目标检测（OSSOD），提出"有效利用而非完全过滤"未标注数据中的分布外（OOD）样本：以实例级一致性正则 + OOD 感知对比学习 + 原型多度量自适应匹配提升检测性能。

## 问题与动机

OSSOD 放宽了半监督目标检测（SSOD）的封闭集假设：未标注数据同时含分布内（ID）与分布外（OOD）样本。现有方法试图从无标注数据中完全滤除 OOD 样本再做常规半监督学习；本文发现有效利用 OOD 样本反而能促进特征学习、提升开放集条件下 ID 类别的检测性能。

## 方法

对无标注图像上所有检测实例（含 OOD）做精炼的实例级一致性正则（ICR）；提出 OOD 感知对比学习（OCL），在类内特征空间聚拢 ID 对象、推开 OOD 样本，增强 ID 特征紧致性并拉大 ID/OOD 判别；基于判别特征设计原型多度量自适应匹配（MAM），按类别自适应度量样本与类原型的多尺度特征相似性来识别 ID/OOD，从而从无标注数据挖掘更可靠的 ID/OOD 样本。

## 实验与结果

原文摘要确认方法在开放集设置下有效提升 ID 检测性能，具体数字未在摘要给出。

## 贡献与局限

- 贡献一：首个论证 OOD 样本可被利用（而非仅过滤）以提升 OSSOD 性能。
- 贡献二：ICR + OOD 感知对比学习 + 原型多度量自适应匹配的组合框架。
- 局限：具体性能数字原文摘要未提供；更复杂开放集分布与更大规模评测待展开。

---

DOI: 10.1109/tnnls.2026.3659534
