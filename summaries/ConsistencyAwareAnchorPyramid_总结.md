# Consistency-Aware Anchor Pyramid Network for Crowd Localization 总结

## 基本信息

- **标题**：Consistency-Aware Anchor Pyramid Network for Crowd Localization
- **作者**：Xinyan Liu、Guorong Li、Yuankai Qi、Zhenjun Han、Anton van den Hengel、Nicu Sebe、Ming-Hsuan Yang、Qingming Huang
- **期刊 / 日期语义**：IEEE Transactions on Pattern Analysis and Machine Intelligence；原始出版：2024（全文注明 2024-04-29，版权为 © 2024 IEEE）；当前版本/任务 JSON 条目年份：2026
- **研究方向**：人工智能
- **DOI**:10.1109/TPAMI.2024.3392013
- **PDF**：[TPAMI_2026_ConsistencyAwareAnchorPyramid.pdf](papers/TPAMI_2026_ConsistencyAwareAnchorPyramid.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 CAAPN，通过按局部人群密度自适应生成锚点，并让训练阶段额外匹配与测试阶段相同排序标准的预测，解决拥挤场景中的锚点分配失衡和训练—推理排名不一致问题。

## 问题与动机

点回归式人群定位在训练时通常依据分类分数和到真值的距离选取 top-(M) 预测，而测试时只依据分类分数，造成训练目标与实际推理规则不一致。固定且均匀的锚点在同一图像的稀疏区会过剩、密集区会不足；人工点标注的局部偏移又会使常规计数损失产生不精确的密度估计。作者因此同时改进锚点数量、空间先验、计数监督和匹配过程。

## 方法

CAAPN 包含 Adaptive Anchor Generator（AAG）和 Localizer with Augmented Matching（LAM）。AAG 将图像划分为 16×16 区域，用计数分支预测局部人数，从训练数据的 K-means 聚类得到不同密度下的空间分布先验，并生成 1、4、8 锚点的三层金字塔（UCF-QNRF 使用 1、8、16）；Cascade Region Loss 与 Integer Loss 共同减轻点标注偏移和取整误差。LAM 先按距离与分类分数做 Hungarian 匹配，再按分类分数选择与测试一致的 top-(M) 预测，并用 Inverse Probability 策略重新分配相应真值。

## 实验与结果

实验在 ShanghaiTech A/B、UCF-QNRF、JHU-CROWD++ 和 NWPU-Crowd 五个基准上使用 VGG-16、HRNet-W48、ConvNeXt-S 特征比较。VGG-16 下 ShanghaiTech 的 σ=8 F1 达 78.0，高于同特征 TopoCount 的 73.6；JHU-CROWD++ 上相对 TopoCount 在 σ=4 和 σ=8 的 F1 分别提升 3.7 和 2.3 个百分点。NWPU-Crowd 上 HRNet-W48 在宽松/严格阈值下的 F1/Recall 分别为 78.6/76.8 与 72.7/71.1。LAM 在五个数据集带来的 F1 增益为 1.2、0.7、0.75、0.9、0.4；用常规 L2 替代 CCL 时 MAE 为 69.2 而 CCL 为 60.8，F1 下降 4.2 个百分点。

## 贡献与局限

主要贡献是提出能随密度和空间分布变化的锚点金字塔，以及显式对齐训练与推理选择规则的增强匹配；同时提出对标注偏移更稳健的级联计数损失，并在五个数据集上验证有效性。局限方面，实验显示三种特征在平均目标边长超过 64 像素后召回率均开始下降，说明大目标的感受野仍有限；锚点先验和金字塔层级需要依赖训练数据分布设定，论文未报告跨数据域自动迁移或极端密度之外的泛化结果。
