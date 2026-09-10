# Training instabilities favor flatter solutions in gradient descent 总结
## 基本信息
- **标题**: Training instabilities favor flatter solutions in gradient descent
- **作者**: Lawrence Wang, Stephen J. Roberts
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108874
- **arXiv**: 无
- **PDF**: [NN_2026_TrainingInstabilitiesFlatterSolutions.pdf](papers/NN_2026_TrainingInstabilitiesFlatterSolutions.pdf)
## 一句话概括
本文说明梯度下降越过经典稳定阈值后，Hessian主特征向量旋转会推动参数探索更平坦的损失区域，从而可能改善泛化。
## 问题与动机
经典分析把最大Hessian特征值定义的阈值视为稳定边界，但现代深度网络常在边界之外取得更好表现。论文解释训练不稳定与平坦解、泛化之间的关系。
## 方法
作者提出RPE几何机制，分析不稳定训练中Hessian主特征向量的旋转，并扩展到随机梯度下降。恢复不稳定性的Adam设置用于区分不稳定性效应和小批量噪声。
## 实验与结果
结果显示特征向量旋转随学习率增加，推动探索并趋向平坦极小值；在随机GD中平坦化仍存在，恢复不稳定性的Adam实验进一步改善泛化。
## 贡献与局限
贡献是给出不稳定性产生平坦偏好的几何解释。局限是平坦度、学习率和网络结构会影响结论，框架对更多自适应优化器的适用性仍待研究。
---
DOI: 10.1016/j.neunet.2026.108874
