# A Survey on Loss-based Regularization for Model Generalization 总结

## 基本信息
- **标题**: A Survey on Loss-based Regularization for Model Generalization
- **作者**: Yaxing Huang、Chenhe Zhang、Renjun Xu、Qinghai Zhang
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-10
- **内容状态**: 完整
- **内容说明**: 已依据出版社全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07139-2
- **PDF**: [ML_2026_LossBasedRegularizationSurvey.pdf](papers/ML_2026_LossBasedRegularizationSurvey.pdf)

## 一句话概括
本文先从适定性、稳定性与一致性建立正则化的理论视角，再按惩罚对象系统梳理 loss-based 正则化方法，并以小规模基准示例展示其效果。

## 问题与动机
机器学习正则化方法虽多，但其数学基础、有效条件及方法间关系缺乏连贯解释；仅拟合有限且含噪的训练数据也容易过拟合。作者因此将正则化联系到病态问题与经验风险最小化，试图统一理论分析和方法分类（PDF第2–6页）。

## 方法
文章分析奇异值截断与 Tikhonov 正则化，说明后者等价于带二范数惩罚的最小二乘，并在适当条件下证明其可降低线性回归的均方误差；进而提出正则化模型应在惩罚趋零时收敛回原模型的一致性原则及一组充分条件（PDF第11–19页）。综述部分依惩罚对象分为权重（范数、稀疏、低秩）、输出、输入梯度和经验风险损失函数，归纳各类方法的机制、适用情境与选择因素（PDF第23–25、37–42页）。

## 实验与结果
作者以 ERM 为基线，在 VGG16、VGG16-BN 及 CIFAR-10、CIFAR-100 上比较 SAM、AMP、gradient norm 和 GMP。表中最高准确率分别为 93.48%、72.72%、95.12% 和 75.96%，对应 AMP、GMP、gradient norm、gradient norm；ERM 对应值为 92.93%、71.14%、94.19%、74.49%（PDF第43页）。作者说明该比较仅作示例，各方法均使用基础数据增强，不能视为全面基准。

## 贡献与局限
贡献在于将线性正则化理论与现代 loss-based 方法衔接，提出可用于设计线性及非线性正则器的一致性准则，并提供按惩罚对象组织的分类与选择参考。作者指出不存在适用于所有任务的最佳正则器，现有方法多针对特定任务，面对跨模型或流式等复杂数据时仍不足（PDF第43页）。另从证据范围看，文中定量对比仅涉及四种方法、两种模型和两个数据集，结果适合说明示例情境，不足以支持广泛的性能排序。

---
DOI: 10.1007/s10994-026-07139-2 · PDF: [ML_2026_LossBasedRegularizationSurvey.pdf](papers/ML_2026_LossBasedRegularizationSurvey.pdf)
