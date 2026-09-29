# CausalCACTUS: A Causally Consistent and Context-Aware Framework for Counterfactual Explanations 总结

## 基本信息
- **标题**: CausalCACTUS: A Causally Consistent and Context-Aware Framework for Counterfactual Explanations
- **作者**: Zhendong Wang、Diego García、José M. Enguita 等
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-28
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07155-2
- **PDF**: [ML_2026_CausalCACTUS.pdf](papers/ML_2026_CausalCACTUS.pdf)

## 一句话概括
CausalCACTUS 在生成反事实解释时同时维护用户指定的背景约束和特征之间的因果依赖，使“改什么才能改变预测”更具可操作性。

## 问题与动机
反事实解释常要求少改特征、保持情境合理，但仅优化接近度可能给出违背因果规律的建议；只关注因果关系的方法又可能忽略用户不希望改变的背景条件。完整的结构因果模型通常也难以获得。

## 方法
框架扩展 CACTUS，先由数据驱动的 ReX 方法学习有向无环因果图，再在变分自编码器潜在空间施加因果可行性与用户情境约束，并采用分阶段优化改善搜索稳定性。它不要求预先提供完整的结构方程，但仍依赖所学因果图的质量。

## 实验与结果
在信用风险、收入预测和教育等领域的五个公开表格数据集上，方法相较原 CACTUS 改善情境对齐与因果一致性指标，同时在有效性、邻近度和稀疏性方面保持竞争力。消融揭示有效性与情境约束之间存在权衡，不能把单一指标提升理解为各项性能同时最优。

## 贡献与局限
贡献是把自动发现的因果结构与情境约束联合纳入潜在空间反事实搜索。若学到的图漏边、或潜在空间重建失真，建议仍可能不可靠；论文证据集中于表格数据，图像和时间序列上的适用性需另行验证。

---
DOI: 10.1007/s10994-026-07155-2
