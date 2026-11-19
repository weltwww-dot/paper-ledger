# Physics-informed adjoint neural network for parametric PDE-constrained optimal control problems 总结

## 基本信息
- **标题**: Physics-informed adjoint neural network for parametric PDE-constrained optimal control problems
- **作者**: Shaojie Zeng、Zhaoxing Han、Qinghui Zhang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109668
- **发表**: 2026-09-21
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109668

## 一句话概括
PIANN 提出两种物理约束伴随网络，在参数变化的 PDE 最优控制中联合近似状态、伴随变量，并从最优性条件恢复控制量。

## 问题与动机
参数化 PDE 控制需重复数值求解；PINN还要平衡方程、边界及 KKT 条件的损失。作者尝试用网络联合学习状态、伴随与控制，减少罚项调节并提升精度。

## 方法
PIANN1 用单网同时表示状态 y 和伴随 p，以最优性条件训练，再由 p 计算并投影控制以满足盒约束。PIANN2 用双网交替拟合状态与伴随，分开学习 KKT 条件而免设其罚参数。两法在参数化坐标配点训练，与 FEM、PINN、PINN2、PECANN 比较，覆盖椭圆控制、奇异几何和三维问题。

## 实验与结果
七组数值实验覆盖控制约束、参数几何、角点奇异和三维区域。例1中 PIANN1 的状态 L2 误差为2.1643×10⁻¹⁰，PIANN2 为1.5255×10⁻¹⁰；控制 L2 误差分别为2.1076×10⁻¹⁰和4.2204×10⁻¹⁰，均低于对照方法。L形区域实验中 PIANN1 的状态/控制 L2 误差为1.6834×10⁻⁴/1.9086×10⁻⁴，PIANN2 为8.9478×10⁻⁴/1.4642×10⁻³，显示网络优劣随问题而变。

## 贡献与局限
单网紧凑，双网避免调 KKT 罚系数，控制均由伴随结果导出。多类数值实验显示高精度，但两法在不同几何上的表现不一；工程外推和部署成本仍需评估。

---
DOI: 10.1016/j.neunet.2026.109668
