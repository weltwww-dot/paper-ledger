# Typed signed-monotone dual Choquet–Stieltjes networks for semantically constrained grouped prediction 总结

## 基本信息
- **标题**: Typed signed-monotone dual Choquet–Stieltjes networks for semantically constrained grouped prediction
- **作者**: Jih-Jeng Huang、Chin-Yi Chen
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109550
- **发表**: 2026-08-29
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109550

## 一句话概括
TSM-DCSN以带方向约束的双Choquet–Stieltjes分支建模不利、获益及中性特征组间的非加性交互，并给出局部参数恢复理论。

## 问题与动机
在信用、医疗等分组预测中，特征组具有语义方向：某些指标增加应降低风险，另一些应提高结果；同时特征间存在非加性交互。普通神经网络难以保证方向单调，单纯加性模型又无法表达交互。论文关注如何在保留可解释语义约束时实现非线性预测，并分析参数是否可从特定响应中恢复。

## 方法
模型先按领域定义把输入划分为不利、获益和中性组，映射为带类型的分数；不利分支与获益分支分别采用触发和否决型Choquet–Stieltjes聚合，再由共享阈值规律组合。容量用块k可加Möbius支持限制交互阶数。理论给出符号单调性、指定探针下精确局部逆恢复，以及有界扰动下的稳定误差界；中性分量可选，但不属于所证明的符号预测器。

## 实验与结果
实验分为探针恢复噪声压力测试和五个分组表格基准（含Credit Default、CKD、Diabetes 130、South German Credit、Early Stage Diabetes）。确定性探针扰动ε从0增至10⁻²时，表6安全率保持1.00；ε=10⁻³时最终RMSE为7.527×10⁻³。五数据集资源表比较TSM-DCSN与零违反参考模型的时间、迭代和内存等统计；参数敏感性表以十个重复划分作描述性比较，k=2、九个阈值结点为默认配置。

## 贡献与局限
贡献主要是把语义方向约束、非加性双分支聚合及局部恢复/稳定理论放进同一模型族；实证设计明确对齐理论适用范围，并报告五组表格数据。论文没有宣称广泛基准准确率全面胜出；逆恢复只针对指定探针及其局部参数，稳定界依赖有界扰动假设，领域分组语义也需由使用者提供。

---
DOI: 10.1016/j.neunet.2026.109550
