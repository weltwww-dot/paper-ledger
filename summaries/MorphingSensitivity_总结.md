# Morphing-Based Sensitivity Analysis 总结

## 基本信息

- **标题**: Morphing-Based Sensitivity Analysis: A Comparative Study of Linear and Non-linear Temporal Transformations in TSC Robustness
- **作者**: Antónia Brito, Duarte Folgado, Carlos Soares, Moisés Santos
- **期刊 / 会议**: Machine Learning 2026
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07132-9
- **PDF**: [ML_2026_Morphing.pdf](papers/ML_2026_Morphing.pdf)

## 一句话概括

提出 tsMIST（Time Series Model Sensitivity Test）框架：对来自不同类别的边界实例对进行变形（morphing），用两个度量总结分类器沿变形路径切换类别的点，从而定位时序分类器的决策边界，并证明变形算子的选择会实质性地影响敏感性分析结论。

## 问题与动机

部署在医疗等高风险领域的机器学习模型，必须对类别间细微且有语义意义的时间变化保持准确与鲁棒。现有时间序列分类器的敏感性分析方法通常只报告聚合鲁棒性，不验证其度量是否反映分类器决策边界的位置，也不清楚依赖的变形算子（morphing operator）的选择是否影响结论——而真实边界信号往往正是时间性的而非幅度性的。

## 方法

从不同类别的真实实例中取边界对进行变形，通过两个度量 tsMIST_Avg 与 tsMIST_Std 总结分类器预测沿变形路径切换类别的点；形式化证明 tsMIST_Avg 估计边界位置的条件，指出其常见的参考值 0.5 反映的是源-目标对称假设而非普适目标；对比线性插值与路径插值（PathI，通过动态时间规整对应关系在时间上滑动匹配特征，而非混合幅度）。

## 实验与结果

在 10 个真实医学时间序列数据集与 4 个分类器上验证：InceptionTime 的决策边界最鲁棒，Catch22 最脆弱；当判别信号是时间性而非幅度性时，线性变形在结构上无法恢复边界位置，而 PathI 能精确恢复；两者在估计边界位置上系统性地不同，但一致性无实际差异，且 PathI 更贴近保留原始信号的时间结构（论文未报告具体数值指标）。

## 贡献与局限

- 贡献一：首个把敏感性分析锚定到决策边界位置的时间序列模型敏感性测试框架（tsMIST）。
- 贡献二：证明并实证变形算子选择（线性 vs 时间路径插值）显著影响结论，主张其应被论证与报告，把边界感知的敏感性分析纳入 Responsible AI 评估。
- 局限：实验结论以定性对比为主，论文未报告具体数值指标；框架在更广任务与模型上的适用性待扩展。

---

DOI: 10.1007/s10994-026-07132-9
