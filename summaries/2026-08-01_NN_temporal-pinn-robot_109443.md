# Temporal compensation physics-informed neural network modeling repetitive small-range rotation inverse dynamics 总结

## 基本信息
- **标题**: Temporal compensation physics-informed neural network modeling repetitive small-range rotation inverse dynamics
- **作者**: Fangyu Li、Man Li、Honggui Han
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109443
- **发表**: 2026-08-01
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109443

## 一句话概括
TC-PINN针对机器人小幅往复运动迟滞导致的逆动力学误差，融合物理约束和时序补偿，在七自由度机械臂上降低扭矩误差，验证范围有限。

## 问题与动机
如何建模重复小范围运动迟滞并保持物理一致性？

## 方法
累积轨迹编码运动历史，物理结构估计动力学和摩擦，Linformer拟合分频残差，分阶段训练。

## 实验与结果
七自由度机械臂实验比较OLS、SMM、DeLaN+NSCF、FIDM；总MAE表列9.40×10⁻⁴ Nm，摘要报告9.65×10⁻⁴ Nm，均优于基线，并评估强迟滞（PDF第7–9页）。

## 贡献与局限
结合物理结构和时序残差建模；总误差报告略有差异，跨平台未验证。

---
DOI: 10.1016/j.neunet.2026.109443
