# Robust Multi-label Classification via Preference Learning 总结

## 基本信息

- **标题**: Robust Multi-label Classification via Preference Learning
- **作者**: Vu-Linh Nguyen, Xuan-Truong Hoang, Sébastien Destercke, Cassio de Campos, Van-Nam Huynh
- **期刊 / 会议**: Machine Learning 2026
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07147-2
- **PDF**: [ML_2026_Multilabel.pdf](papers/ML_2026_Multilabel.pdf)

## 一句话概括

把多标签分类（MLC）问题转化为序结构学习（order structure learning），利用序的丰富结构来改进并鲁棒化多标签分类，并研究预测贝叶斯最优序结构的任务。

## 问题与动机

多标签分类在真实数据中常面临标签噪声与不平衡，模型鲁棒性不足。序结构蕴含标签间丰富的偏好关系，如何把 MLC 形式化为序结构学习并利用其结构提升鲁棒性，是一个未被充分挖掘的方向。

## 方法

形式化描述多标签分类如何转换为序结构学习与预测任务：标签的偏好关系被建模为序，模型学习并预测贝叶斯最优的序结构；在此基础上研究两种对序结构有利的设置——带噪声与不平衡标签的鲁棒多标签分类，以及带部分弃权（partial abstention）的多标签预测。

## 实验与结果

在噪声与不平衡标签的鲁棒多标签分类、以及部分弃权预测两类设置中实验，验证序结构学习在这些场景的价值（论文未报告具体数值指标）。

## 贡献与局限

- 贡献一：首次把多标签分类系统性地形式化为序结构学习，把标签偏好结构引入预测。
- 贡献二：为噪声/不平衡标签下的鲁棒预测与部分弃权预测提供统一视角。
- 局限：论文未报告具体数值指标；更大规模数据集与更复杂标签结构的验证待后续工作。

---

DOI: 10.1007/s10994-026-07147-2
