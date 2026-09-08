# Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation 总结

## 基本信息

- **标题**: Distribution-Free Deviation Bounds and the Role of Domain Knowledge in Learning via Model Selection with Cross-Validation Risk Estimation
- **作者**: Diego Marcondes、Cláudia Peixoto
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-07
- **内容状态**: 完整 · 已基于公开摘要与开放获取 PDF 完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07150-7
- **arXiv**: 2303.08777v3
- **PDF**: [incremental.pdf](papers/incremental_e816d2adf30b.pdf)

## 一句话概括

论文为“利用交叉验证风险进行模型选择”的完整学习流程建立分布无关偏差界，并用带偏序结构的 Learning Space 说明领域知识如何改善泛化。

## 问题与动机

交叉验证广泛用于风险估计和模型选择，但嵌入训练与选择整体流程后的理论保证仍不充分。尤其需要解释候选模型族的组织方式如何影响泛化，以及领域知识何时真正有助于选择模型。

## 方法

作者以 VC 维为基础推导整个流程的偏差界，覆盖有界与无界损失，并对后者扩展既有结果。Learning Space 把候选模型按复杂度与包含关系组织成偏序集合，从而把领域知识编码进模型空间与搜索过程。

## 实验与结果

研究通过案例和高维线性回归模拟，将两种 Learning Space 与最小二乘、LASSO、岭回归比较，并改变先验知识与真实目标的一致程度。摘要报告，当模型空间与目标匹配且搜索高效时，该方法可取得数量级上的性能提升。

## 贡献与局限

贡献包括给出统一的分布无关理论界，并形式化领域知识影响泛化的路径。局限是显著收益依赖先验知识与真实目标相符，偏序模型空间的构造和高效搜索在复杂任务中可能困难，模拟结论仍需真实数据验证。

---
DOI: 10.1007/s10994-026-07150-7
