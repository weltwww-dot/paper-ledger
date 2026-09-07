# Revealing and Overcoming Fairness Confusion in Out-of-Distribution Detection 总结

## 基本信息

- **标题**: Revealing and Overcoming Fairness Confusion in Out-of-Distribution Detection
- **作者**: Zhaohui Hu, Haotian Wang, Jialu Zhou, Chuan Li, Da Huang, Long Lan
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109564
- **arXiv**: 无
- **PDF**: [NN_2026_FairnessConfusionOOD.pdf](papers/NN_2026_FairnessConfusionOOD.pdf)

## 一句话概括

本文提出公平分布外检测问题，用 Fair-OOD 指标刻画敏感属性及其诱发特征偏移造成的"公平混淆"，并提出半监督方法 PACT 同时提升 OOD 检测能力、保证公平并消除公平混淆。

## 问题与动机

现有的分布外（OOD）检测研究主要关注微调策略与打分函数设计，却忽略了公平性指标，导致受敏感属性（如图像背景）影响的数据可能产生不可靠预测。作者指出敏感属性不仅会作为捷径线索直接影响 OOD 判定，还会诱发特征偏移（Feature Shift, FS），间接干扰已学表示，从而形成一种被定义为"公平混淆（Fairness Confusion, FC）"的现象。基于 BAR 动作识别数据集的案例分析表明：即使模型在 ID 分类上满足公平性，各敏感属性组的 OOD 检测错误率仍明显不同（A=a′ 组 ID 与 OOD 错误率分别约为 64.39% 与 35.61%）；而特征偏移会显著推高边缘群体（A=a′）的 OOD 检测错误率。此外，通过反例论证，传统公平指标 Demographic Parity（DP）与 Equal Opportunity（EO）只考虑敏感属性、忽视特征偏移，无法可靠识别此类不公平，直接套用现有去偏方法也不足以解决该问题。

## 方法

作者首先形式化定义了 Fair OOD Detection 问题（Problem 1），要求模型同时实现可靠的 ID/OOD 判定与针对敏感属性和特征偏移的组级公平。为量化公平混淆，提出统一指标 Fair-OOD（Definition 1），比较"无 FS 条件下不同敏感组的正确判定概率"与"边缘组内有无 FS 时的正确判定概率"两组互补差异。随后提出半监督方法 Predictive Adaptive Calibration（PACT），由两部分组成：特征分布正则化（FDR）约束同一 ID 类内的特征表示高度紧凑、增大类间及与 OOD 特征的距离，抑制敏感属性相关特征变化；预测分布校准（PDC）在不需要 OOD 数据敏感属性标签的前提下，用 Wasserstein 距离放大正确分类 ID 样本与 OOD 样本预测分布之间的间隔，为 FS 干扰预留裕量。总体目标为 L = Lce + Loe + αLFDR + βLPDC，并提供理论保证（Theorem 1 给出类内特征方差上界，Theorem 2 给出特征偏移下预测分布变化的有界性）。

## 实验与结果

实验在 BAR、CIFAR-10-C 与 ImageNet-100-C 三个数据集上进行，主干为 ResNet-18，对比三类基线：post-hoc 方法（MSP、MLP、T2FNorm、Energy、ITP、SCALE）、带辅助 OOD 数据的微调方法（OE、Energy-OE、DAL、DiverseMix、MVOL）以及公平表示学习方法（DFA、SelecMix、BCSI、DPR、ALFA）。结果显示：(a) 未施加 PACT 前各方法 Fair-OOD 显著偏高（如 MSP 在 BAR 上 Fair-OOD 达 27.10%），表明 Fair-OOD 能识别传统公平指标发现不了的 FC；(b) PACT 大幅提升 OOD 检测性能，在大规模多类基准 ImageNet-100-C 上 AUROC 达 96.43%、FPR95 为 17.50%，较最强基线取得 11.46% 的绝对 AUROC 提升；(c) PACT 同时优化传统公平指标与 Fair-OOD（如 CIFAR-10-C 上 DP 降至 0.50、Fair-OOD 降至 1.59，AUROC 达 89.50），且与现有公平指标不冲突；(d) 消融实验显示 PDC 在 BAR 上把 Fair-OOD 从 25.00% 降至 8.33%、平均精度从 72.42% 提至 72.68%，FDR 与 PDC 组合取得最佳整体性能，且均优于简化替代（LSupCon、LEuc）；(e) PACT 优化可惠及其他 OOD 打分方法，在较宽超参范围（β∈[0,6]、τ∈[0.1,0.5] 及全部 α）内稳健优于 SOTA，计算开销与 OE、Energy 相当（ImageNet-100-C 上运行时间约 296–298 秒、GPU 显存约 15.95GB）。

## 贡献与局限

贡献包括：首次在 OOD 检测中系统纳入公平性考量，提出包含敏感属性与特征偏移双重影响的 Fair OOD Detection 新问题；设计能原理化识别公平混淆的 Fair-OOD 指标；提出同时保证公平、提升 OOD 检测并缓解公平混淆的 PACT 算法并给出理论保证；通过真实数据集实验验证了指标与方法的有效性。局限方面：形式化分析主要针对二值敏感属性与特征偏移设定（虽可推广到类别型）；PACT 的 PDC 与 OOD 暴露目标依赖辅助 OOD 训练数据，且公平混淆检测依赖按样本到类中心距离阈值（70 分位）估计的 FS 状态，实际场景中敏感属性标签不可得时该估计方式存在近似性。

---
DOI: 10.1016/j.neunet.2026.109564
