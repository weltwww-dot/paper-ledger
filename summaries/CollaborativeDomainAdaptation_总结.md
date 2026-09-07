# Learning from heterogeneous structural MRI via collaborative domain adaptation for late-Life depression assessment 总结

## 基本信息

- **标题**: Learning from heterogeneous structural MRI via collaborative domain adaptation for late-Life depression assessment
- **作者**: Yuzhen Gao, Qianqian Wang, Yongheng Sun, Cui Wang, Yongquan Liang, Mingxia Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108911
- **arXiv**: 无
- **PDF**: [NN_2026_CollaborativeDomainAdaptation.pdf](papers/NN_2026_CollaborativeDomainAdaptation.pdf)

## 一句话概括

本文提出基于 ViT 与 CNN 双分支协同域适应（CDA）框架，在无目标标注条件下利用异构多中心结构 MRI 可靠识别老年抑郁症。

## 问题与动机

基于结构 MRI 的老年抑郁症（late-life depression, LLD）自动识别对监测疾病进展与及时干预至关重要，但 LLD 相关 MRI 数据集的样本量往往很小（常仅为几十例），难以支撑可靠的深度学习模型训练与泛化。虽然引入辅助数据集可以扩大训练规模，但不同中心的成像协议、扫描仪硬件与人群特征差异会带来显著域偏移，削弱跨域可迁移性。现有无监督域适应（UDA）方法通常把模型视为固定统一的系统、仅关注特征分布对齐，忽视了不同架构（如 CNN 与 ViT）之间的互补性；当目标域数据极度稀缺时，其性能也难以保证。

## 方法

作者提出协同域适应（Collaborative Domain Adaptation, CDA）框架，用于基于 T1 加权 MRI 的 LLD 检测。CDA 采用双分支架构：Vision Transformer（ViT）编码器负责捕捉全局解剖拓扑结构，CNN 编码器（ResNet-34，来自 MONAI）负责提取局部纹理细节，各分支由编码器与分类器组成。训练分为三个阶段：(a) 在带标签源域（NCODE）上用 focal loss 分别监督训练两个分支；(b) 自监督目标特征适应，含“边界探索”（冻结 ViT 编码器、微调两个分类器以在无标签目标样本上最大化预测分歧）与“特征巩固”（冻结分类器、微调 CNN 编码器以最小化与已确立决策边界的分歧）；(c) 在无标签目标数据上进行协同训练：以 ViT 从弱增强目标样本生成的伪标签监督 CNN 在强增强样本上的学习，CNN 亦以同样方式反向指导 ViT，并采用基于 Jensen-Shannon 散度（JSD）的可靠性感知“双约束”机制（JSD≤τ=0.1 的一致性约束 + 置信度阈值 θ1=0.5/θ2=0.8）过滤低质量伪标签。ViT 编码器先用掩码自编码器（MAE）在 IXI、OASIS-3、BRATS 上预训练，CNN 编码器先在约 9544 例 ADNI T1 图像上做自编码器式预训练；推理时使用经协同训练增强的 CNN 分支。

## 实验与结果

作者在两个多中心基准上验证 CDA，均以 NCODE 为源域、NBOLD 为目标域，采用五折交叉验证。二元分类任务（CN-D vs. CN-N）中，CDA 取得 AUC 71.51%、ACC 70.73%、SEN 69.29%、SPE 73.09%、F1 74.99%，全面优于 TCA、JDA、SCA、DAN、DAAN、DeepCORAL、ADDA、DANN、BNM、DSAN、SHOT++、ViT-ADA、DCSC 等传统与深度域适应基线，且相对多数方法差异统计显著（p<0.05）。三分类任务（CI vs. CN-D vs. CN-N）中，CDA 总体 ACC 50.79%（CN-N 59.49%、CN-D 64.22%、CI 64.50%）、总体 SEN 42.22%，其中 CI 类 SEN 仅 12.67%，作者归因于 CI 样本过少（仅 17 例）。消融实验表明三个训练阶段均有效，完整 CDA 优于仅含部分阶段的变体；混合 ViT+CNN 主干优于同质 CNN+CNN 与 ViT+ViT 配置；双向伪标签协同优于单向协同（单向变体 AUC 最高 69.32%）；推理用 CNN 优于用 ViT（CDA-V 仅 AUC 67.30%）；非对称设计至关重要（反向角色变体 CDA-R 的 SEN 降至 57.14%）；编码器预训练带来 AUC +2.67%、ACC +3.52% 的提升。额外在 ADNI→AIBL 基准上，CDA 取得总体 ACC 68.04%、宏平均 SEN 48.85%、MCI SEN 55.13%、AD SEN 54.29%，优于 SHOT++、ViT-ADA、DCSC，说明主实验中 CI 低灵敏度源于少数类目标数据稀缺而非方法缺陷。

## 贡献与局限

主要贡献：其一，提出面向 LLD 识别的 CDA 框架，据作者所述是最早将 CNN 与 ViT 以双分支交叉监督方式结合以应对异构域偏移的工作之一，发挥局部纹理与全局拓扑的互补优势；其二，提出可靠性感知的 JSD 双约束协同训练策略，在严格无监督设置下过滤伪标签噪声、降低模式坍缩风险；其三，在两个多中心基准上的大量实验表明 CDA 一致优于现有方法，并公开了源代码（GitHub: yzgao2017/CDA）。局限：当前主干架构固定，未针对 LLD 任务做进一步架构优化；对分布偏移更极端的全新成像中心的泛化性尚待评估；研究仅使用 T1 结构 MRI 单模态，扩展至多模态神经影像（如功能 MRI、DTI）是未来方向。

---
DOI: 10.1016/j.neunet.2026.108911
