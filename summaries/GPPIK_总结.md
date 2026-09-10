# Gaussian processes with prior-model-informed kernel for dynamical system modeling 总结

## 基本信息

- **标题**: Gaussian processes with prior-model-informed kernel for dynamical system modeling
- **作者**: Shengbing Tang、Chen Xiao、Bin He、Na Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109569
- **arXiv**: 无
- **PDF**: [NN_2026_Paper07.pdf](papers/NN_2026_GPPriorModelKernel.pdf)

## 一句话概括

GP-PI-K 将解析物理模型或不完美模拟器融入高斯过程核函数，以改善动力系统外推。

## 问题与动机

高斯过程能提供不确定性估计并吸收先验知识，但在训练区域外通常外推较差。仅把先验模型放入均值函数，可能无法充分影响相似性结构。研究希望保留高斯过程的不确定性优势，同时改善一步和多步预测。

## 方法

作者提出 prior-model-informed kernel（GP-PI-K）。先用先验模型变换输入空间，再对变换结果应用 RBF 或 Matérn 等基础核，使先验动力学相似的输入具有相应相似性。另加入标准残差核，修正先验模型与真实系统之间的偏差。

## 实验与结果

文章在多个基准动力系统上与标准 GP、物理信息或神经网络均值 GP、深度核学习比较。结果显示 GP-PI-K 在一步和多步预测、不确定性估计与校准，以及主动学习和基于模型的强化学习等下游任务中持续优于基线。

## 贡献与局限

贡献是把先验动力学直接编码进核函数，而不是只作为均值修正。局限是性能依赖先验模型的质量和变换设计；先验严重错误、维度很高或系统发生结构变化时的稳定性仍需研究。

---
DOI: 10.1016/j.neunet.2026.109569

