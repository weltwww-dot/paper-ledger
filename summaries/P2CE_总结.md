# P²CE 总结

## 基本信息

- **标题**: P²CE: Model-Agnostic Plausible Pareto-Optimal Counterfactual Explanations
- **作者**: Arthur Hendricks Mendes de Oliveira, Giovani Valdrighi, Marcos Medeiros Raimundo
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-01
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07143-6
- **PDF**: [ML_2026_P2CE.pdf](papers/ML_2026_P2CE.pdf)

## 一句话概括

提出 P²CE，一个模型无关的算法：生成可行（plausible）且 Pareto 最优的反事实解释，给用户提供不同可行性指标间的多样化最优权衡。

## 问题与动机

机器学习在贷款审批、求职等社会应用中日益普及，公平与透明引发关注，反事实解释帮助用户理解并可能改变不利决策。现有方法难以兼顾可行性、合理性（plausibility）与计算效率。

## 方法

P²CE 采用辅助隔离森林（isolation forest）异常检测器，确保解释符合数据分布（plausible）；利用 SHAP 值加速优化，使算法与底层模型无关；生成 Pareto 最优反事实集，覆盖不同可行性定义之间的权衡。

## 实验与结果

在三个数据集上实验，P²CE 在解质量与计算效率上均优于相关方法（原文摘要未给出具体数字）。

## 贡献与局限

- 贡献一：模型无关的可行 Pareto 最优反事实生成算法，兼顾质量与效率。
- 贡献二：隔离森林保证分布一致性 + SHAP 加速的组合策略。
- 局限：具体数字原文摘要未提供；更大规模与更多决策场景的验证待展开。

---

DOI: 10.1007/s10994-026-07143-6
