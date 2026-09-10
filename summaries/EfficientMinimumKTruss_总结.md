# Efficient Minimum $k$-Truss Search: A Decomposition-Based Approach 总结

## 基本信息

- **标题**: Efficient Minimum $k$-Truss Search: A Decomposition-Based Approach
- **作者**: Qifan Zhang, Yang Liu, Kaiqiang Yu, Shengxin Liu, Cheng Long, Xun Zhou
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/TKDE.2026.3701433
- **arXiv**: 无
- **PDF**: [TKDE_2026_EfficientMinimumKTruss.pdf](papers/TKDE_2026_EfficientMinimumKTruss.pdf)

## 一句话概括

本文提出最小 (k)-truss 搜索问题及其分解式 DSA 算法，把原问题转化为具有遗传性的边型 (s)-plex 子问题，并通过分支限界显著加速高凝聚子图发现。

## 问题与动机

传统 (k)-truss 通常寻找包含最多顶点的结构，但最大 (k)-truss 可能过大、稀疏且混入不相关节点，难以直接用于社区发现、推荐或蛋白质复合体识别。作者提出寻找顶点数最少的非平凡 (k)-truss，以获得更紧密、更易解释的子图。困难在于 (k)-truss 不具备遗传性，任意诱导子图不一定仍是 (k)-truss，直接枚举顶点或边会产生指数级搜索。

## 方法

论文先证明最小 (k)-truss 问题是 NP-hard，并设计基于顶点枚举和启发式上界的 MTEnum 基线。核心方法 DSA 引入边型 (s)-plex：每条边至少包含 (|V|-s-2) 个三角形；该结构具有遗传性，因此可以安全使用分支限界和剪枝。作者把最小 (k)-truss 分解为一系列大小约束的 (s)-plex 子问题，按 (s) 从小到大搜索，找到首个可行子图即可停止。子问题由 FastEPX 和更强的分治版 DCFastEPX 求解，并配合最大 (k)-truss 预处理、分支策略、上界和削减规则；算法还扩展到个性化搜索与 Top-c 搜索变体。

## 实验与结果

作者在 Intel 2.10 GHz CPU、128 GB 内存上，用 Epinions、Youtube、Flixster、Wiki、UCLA、Harvard、Google、Webbase、Skitter 和合成 RGG 等 10 个图数据集比较 DSA、MTEnum 及去除启发式的 MTEnum 变体。所有方法时间上限为 24 小时；DSA 在 Epinions 上比两个 MTEnum 版本快五个数量级以上，并在不同 (k) 值和代表性图上持续取得最佳运行时间，且能稳定找到最小 (k)-truss。大图抽样实验显示运行时间随图规模增长而增加，DCFastEPX 整体优于 FastEPX。案例研究中，AMiner 引文网络的最小 16-truss 含 18 位作者和 150 条合作边，对 2018 年新增合作预测准确率为 66.67%；DBLP 学者协作中，最小 7-truss 仅含 9 个作者、33 条边、密度 0.917，而普通 7-truss 含 44 个作者、200 条边、密度 0.211。蛋白质复合体预测在 (k=4) 时最小 (k)-truss 的 PPV 为 0.752，高于最大 (k)-truss 的 0.471。

## 贡献与局限

本文将“寻找最小而非最大 (k)-truss”确立为新的凝聚子图问题，证明其复杂性，并用具有遗传性的 (s)-plex 分解避免原始 (k)-truss 枚举的结构性困难。实验说明最小结构通常更稠密、更适合识别紧密社区和功能模块。局限在于问题本身 NP-hard，图规模、密度和 (s) 增大仍会推高搜索成本；当前实现主要是单机算法，作者提出的后续方向是并行化 DSA，以进一步扩大可处理图规模。

---
DOI: 10.1109/TKDE.2026.3701433
