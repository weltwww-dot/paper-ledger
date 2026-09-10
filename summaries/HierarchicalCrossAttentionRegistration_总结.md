# Hierarchical cross-attention guided deformable registration with multi-level feature fusion for medical images 总结

## 基本信息

- **标题**: Hierarchical cross-attention guided deformable registration with multi-level feature fusion for medical images
- **作者**: Dongdong Wan, Jiaxuan Jiang, Yuee Li, Wenyan Li, Zhong Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108908
- **arXiv**: 无
- **PDF**: [NN_2026_HierarchicalCrossAttentionRegistration.pdf](papers/NN_2026_HierarchicalCrossAttentionRegistration.pdf)

## 一句话概括

HCA-Morph以空间对应感知和跨尺度注意力构建无监督可变形配准框架，在脑MRI配准中兼顾精度、效率和可解释性。

## 问题与动机

医学图像配准服务于纵向诊断、手术规划和解剖分析，但传统优化方法计算密集且依赖参数设置。深度模型又常难以捕捉不同解剖结构的对应关系，且多尺度融合与可解释性不足。

## 方法

SCAM从局部到全局学习移动图像与固定图像之间的可解释空间对齐；CSAM动态融合多层级特征以提高表示一致性。整个框架以无监督方式学习形变场，使配准目标直接约束图像对齐而不依赖人工形变标注。

## 实验与结果

在OASIS和IXI脑MRI数据集上，Dice分别为0.845和0.834，HD95分别为1.365和1.725；模型参数量为2.05MB，是对比方法中最小者，并取得可比或更好的精度。

## 贡献与局限

贡献是将层级交叉注意、空间对应建模与多级融合结合，并以小模型实现高效配准。局限是验证范围集中于两个脑MRI数据集，无监督目标对域变化、其他器官和临床流程的适用性仍需检验。

---
DOI: 10.1016/j.neunet.2026.108908
