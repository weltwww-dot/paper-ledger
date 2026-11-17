# CBS-PINN: Coordinated training to address nonlocality and spectral stiffness in the Calogero-Bogoyavlenskii-Schiff-type equation 总结

## 基本信息
- **标题**: CBS-PINN: Coordinated training to address nonlocality and spectral stiffness in the Calogero-Bogoyavlenskii-Schiff-type equation
- **作者**: Ting-Ting Jia、Ya-Juan Li、Jun Long 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109460
- **发表**: 2026-08-03
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109460

## 一句话概括
CBS-PINN以课程优先级和曲率加权协调非局部项与高阶导数的训练，在所测 CBS 型方程中降低相对 L2 误差，但对其他方程族的适用性尚未确立。

## 问题与动机
CBS 型方程的非局部项会传播初边值误差，高阶混合导数又造成谱刚性，常规同时优化各损失项可能不稳定，如何协调训练？

## 方法
方法由课程优先级逐步安排初始、边界与方程残差约束，并以曲率加权根据损失面的曲率调整各项权重，组合成 CBS-PINN；通过自动微分训练连续解函数。

## 实验与结果
在二维 CBS 型方程孤子解实验中，使用解析解对照；相对 L2 误差为 2.69×10⁻³，低于 vanilla PINN 的 2.31×10⁻¹、SA-PINN 的 4.33×10⁻³，梯度幅值加权 LRA 为 8.37×10⁻¹；扩展方程实验也报告误差改善，但结论来自有限合成问题（PDF 第 10–12 页）。

## 贡献与局限
针对非局部误差传播与谱刚性设计相互补充的训练协调机制，并以多个 CBS 型算例验证；尚需独立基准、不同采样方案及更复杂边界条件下的检验。

---
DOI: 10.1016/j.neunet.2026.109460
