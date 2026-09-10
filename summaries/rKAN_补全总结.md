# rKAN: Rational Kolmogorov-Arnold networks 总结

## 基本信息
- **标题**: rKAN: Rational Kolmogorov-Arnold networks
- **作者**: Alireza Afzal Aghaei, Mehdi Hosseinzadeh, Kourosh Parand
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108888
- **PDF**: [NN_2026_rKAN.pdf](papers/NN_2026_rKAN.pdf)

## 一句话概括
rKAN 用有理函数和 Jacobi 多项式构造 Kolmogorov-Arnold network 的可学习函数，改善非线性逼近与物理信息学习的灵活性。

## 问题与动机
KAN 的函数基元决定其表达能力、数值稳定性和训练难度。需要比固定样条更灵活、同时可控制奇异性和参数效率的函数表示。

## 方法
作者以有理函数参数化 KAN 的可学习映射，并结合 Jacobi polynomial 基础构造 rKAN。网络通过分子、分母参数表示复杂非线性，同时在训练中约束分母以避免数值奇异。

## 实验与结果
函数逼近、物理信息深度学习和神经网络基准实验显示 rKAN 具有竞争力的拟合与泛化表现。全文摘要未给出统一具体数值。

## 贡献与局限
贡献是提出有理函数化 KAN。局限是奇异点、初始化和高维优化可能影响稳定性，实际大模型的计算开销仍需评估。

---
DOI: 10.1016/j.neunet.2026.108888
