# Sparse Traffic Accident Risk Forecasting With Spatial-Temporal Knowledge Graphs 总结

## 基本信息

- **标题**: Sparse Traffic Accident Risk Forecasting With Spatial-Temporal Knowledge Graphs
- **作者**: Shengnan Guo, Yan Lin, Wei Chen, Weiwen Tang, Haochen Lv, Rongzhi Zhou, Junliang Lin, Youfang Lin, Huaiyu Wan
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-06-30
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 时空数据挖掘与智能交通
- **DOI**: 10.1109/TKDE.2026.3706345
- **arXiv**: 无
- **PDF**: [TKDE_2026_STKGRiskTrafficAccident.pdf](papers/TKDE_2026_STKGRiskTrafficAccident.pdf)

## 一句话概括

STKGRisk 构建交通事故时空知识图谱，结合历时嵌入、时空图网络和零膨胀混合泊松解码器，同时预测道路段与出租车区域的事故风险并识别高风险区域。

## 问题与动机

交通事故风险同时受道路、天气、时段、交通流和周边环境等多源动态因素影响，现有模型难以表达这些高阶交互；事故数据又高度稀疏，零值过多，模型可能在回归指标上看似有效，却无法准确识别真正的高风险区域。论文希望在道路段和出租车区域两个空间粒度上统一建模，并解决零膨胀问题。

## 方法

STKGRisk 首先构建交通事故空间—时间知识图谱，用历时嵌入捕捉多源因素与事故之间随时间变化的高阶关系。随后设计多层、多视角的时空图网络编码器，分别建模道路段和出租车区域的空间相关与时间相关。最后使用零膨胀混合泊松解码器，区分结构性零值、低风险计数和高风险事故发生模式，改善稀疏风险数据的预测。

## 实验与结果

作者在三个真实交通事故数据集上进行实验，并与现有时空预测、图网络和事故风险模型比较。STKGRisk 在道路段和区域粒度的风险预测任务上整体达到最优或接近最优，尤其在高风险区域识别方面表现突出；结果说明知识图谱能够补充多源因素关系，零膨胀解码器也能减少模型只优化低风险多数样本的问题。

## 贡献与局限

论文提出了面向事故风险分析的空间—时间知识图谱、双粒度时空编码器和零膨胀混合泊松预测组件，兼顾数值预测和高风险识别。局限在于数据集、城市交通结构和传感器质量会影响迁移，知识图谱构建及历时关系更新也需要额外成本；极端事故、实时预测、跨城市泛化和因果解释仍需进一步验证。

---
DOI: 10.1109/TKDE.2026.3706345
