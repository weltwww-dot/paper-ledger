# Fusion of Supervised Feature Selection and Unsupervised Clustering for Multinuclei Classification of MER Signals in DBS for Parkinson's Disease

## 基本信息

- **标题**: Fusion of Supervised Feature Selection and Unsupervised Clustering for Multinuclei Classification of MER Signals in DBS for Parkinson's Disease
- **作者**：Xiang Lu、Xuexin Du、Peng Lun、Yande Ren
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tnnls.2026.3675818
- **arXiv**：无
- **PDF**：[NN_2026_FusionSupervisedFeatureSelection.pdf](papers/NN_2026_FusionSupervisedFeatureSelection.pdf)

## 一句话概括

本文面向帕金森病脑深部刺激手术中的微电极记录信号，提出“随机森林特征筛选—模糊聚类—低置信样本复核”的三类核团识别流程，以较少的复核样本区分不确定带、丘脑底核和黑质。

## 问题与动机

脑深部刺激手术需要在术中准确定位丘脑底核等关键核团，但微电极记录信号存在核团边界模糊、噪声和高维特征冗余等问题。既有研究多将任务简化为丘脑底核与非丘脑底核二分类，并依赖专家逐条标注，难以在实时场景中识别多个相邻核团。论文希望在维持临床标签可靠性的同时，减少大规模人工标注负担，并严格避免同一患者信号在训练和测试之间泄漏。

## 方法

研究收集 121 名接受脑深部刺激手术患者的连续尖峰信号，先进行 300–5000 Hz Butterworth 带通滤波，再以 2 秒窗口、50% 重叠切分。作者提取 17 个时域特征，包括放电计数、放电率、脉冲间隔、爆发率、爆发持续时间、尖峰幅值以及偏度、峰度、均方根等统计量。随机森林通过三折交叉验证优化尖峰/爆发阈值并按平均不纯度下降筛选特征；随后在归一化的 9 个高贡献特征上做 PCA 和模糊 C 均值聚类，以隶属度划分高置信、待复核和噪声样本。最终用轻量 EEGNet1D 进行三分类，并与 SVM、KNN、谱聚类、GMM 和 HDBSCAN 比较。

## 实验与结果

数据按患者划分为 80 名训练、20 名验证和 21 名测试患者，分类目标为不确定带、丘脑底核和黑质。专家一致标注训练下，EEGNet1D 测试准确率为 92.97%，高于 SVM 的 89.54% 和 KNN 的 89.63%；纯 FCM 聚类标签训练的准确率为 90.51%。采用 FCM 加置信度复核后，测试准确率达到 92.71%，三类 AUC 均超过 0.97，且 4327 个样本可自动标注，仅 483 个低置信样本需要复核，人工介入率约 10%。该方案优于 GMM 复核的 88.75%，并在丘脑底核和黑质等易混淆类别上保持较均衡的 F1 表现。

## 贡献与局限

论文把监督式特征重要性分析和无监督软聚类结合起来，形成了可验证的三类核团自动标注流程，在接近专家标注精度的同时显著减少复核量，并以患者级划分增强了临床泛化评估的可信度。局限在于数据来自单一医疗来源，当前只覆盖三类核团，边界样本仍存在丘脑底核与黑质混淆；固定的置信度阈值和人工复核环节也限制了完全自动化。后续可融合局部场电位、神经影像和电极定位信息，并设计随核团类别和电极深度自适应的置信度策略。

---
DOI: 10.1109/tnnls.2026.3675818
