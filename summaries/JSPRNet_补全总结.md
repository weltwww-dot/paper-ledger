# JSPR-Net: A Jacobian-stabilized physics-informed residual neural network for breast cancer detection and fractional-order disease progression modeling 总结

## 基本信息
- **标题**: JSPR-Net: A Jacobian-stabilized physics-informed residual neural network for breast cancer detection and fractional-order disease progression modeling
- **作者**: Vetrivel Muthupandi, Arul Joseph Gnanaprakasam, Pandit Vivek Kumar Pandey
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108944
- **PDF**: [NN_2026_JSPRNet.pdf](papers/NN_2026_JSPRNet.pdf)

## 一句话概括
JSPR-Net 将 Jacobian 稳定化残差网络与物理信息约束结合，用于乳腺癌检测和分数阶疾病进展建模。

## 问题与动机
检测任务需要判别特征，进展模型还需满足合理动力学。普通网络缺少物理一致性，物理信息网络又可能出现梯度不稳定，因此需要兼顾两者。

## 方法
JSPR classifier 负责数据驱动检测，Caputo-Fabrizio 分数阶导数描述疾病动力学；physics-informed 损失把数据拟合和方程约束联合起来，Jacobian 稳定化改善训练敏感性和梯度传播。

## 实验与结果
乳腺癌检测和分数阶模型实验显示，方法能同时获得有效分类与稳定动力学拟合。全文摘要未给出具体指标。

## 贡献与局限
贡献是统一分类、分数阶建模和稳定化训练。局限是物理方程假设影响适用范围，临床多中心和长期随访数据仍需验证。

---
DOI: 10.1016/j.neunet.2026.108944
