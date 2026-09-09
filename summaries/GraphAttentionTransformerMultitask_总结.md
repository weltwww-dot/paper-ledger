# Graph Attention Transformer With Multitask Learning for Motion Prediction in Autonomous Driving 总结

## 基本信息

- **标题**: Graph Attention Transformer With Multitask Learning for Motion Prediction in Autonomous Driving
- **作者**: Chuan Hu、Hao Jiang、Peichuan Lang、Biao Yang、Xiaobo Chen、Hao Chen
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3672361
- **arXiv**: 无
- **PDF**: [TAI_2026_GraphAttentionTransformerMultitask.pdf](papers/TAI_2026_GraphAttentionTransformerMultitask.pdf)

## 一句话概括

本文提出 GATran 多任务图注意力 Transformer，将车辆轨迹预测与横纵向驾驶意图估计联合建模，并通过特征融合和时空交互模块提升复杂交通场景下的多模态预测能力。

## 问题与动机

车辆运动预测既要处理历史轨迹和道路语义，也要捕捉周围车辆的动态交互以及驾驶行为的不确定性。现有方法常将轨迹回归作为单一任务，或缺少有效的语义、交互信息融合，在长时域预测和强交互场景中容易产生误差。作者希望用驾驶意图这一辅助任务帮助模型理解轨迹变化的原因，并通过图结构和 Transformer 同时建模局部交互与时间依赖。

## 方法

GATran 由特征融合、时空交互和运动解码三个模块组成。特征融合模块将目标车辆的历史运动与语义、动态信息编码为查询、键和值；时空交互模块使用多头图注意力和时间编码建模目标车辆与周围车辆的关系；运动解码器将任务拆分为轨迹预测和驾驶意图估计，并通过包含三个专家的混合专家网络生成多模态轨迹。训练时轨迹任务使用负对数似然损失，意图任务使用横向和纵向交叉熵损失，两个任务联合端到端优化。

## 实验与结果

实验使用 NGSIM 的 US-101、I-80 以及 HighD 数据集，将 8 秒片段划分为 3 秒历史观测和 5 秒预测目标，并以 minRMSE、minADE、minFDE 评价轨迹质量。在统一多模态协议下，GATran 相较当前最佳基线 CDSTraj，在 NGSIM 和 HighD 上的 minRMSE 分别降低 51% 和 21%；长时域 4–5 秒预测的平均改进分别达到 61% 和 19%。消融实验表明，移除时空交互模块会造成最明显的误差上升；完整模型在 NGSIM 上横向/纵向意图准确率为 0.98/0.93，在 HighD 上为 0.99/0.99，说明多任务设计和交互建模均有贡献。

## 贡献与局限

- 将轨迹预测和驾驶意图估计统一为多任务问题，使意图信息能够反向帮助多模态运动预测。
- 结合特征融合、多头图注意力、时间编码和混合专家解码器，增强对复杂时空交互和行为差异的表达能力。
- 在 NGSIM 与 HighD 上显著降低长时域预测误差，并通过模块消融验证各组成部分的作用。
- 局限：当前工作主要聚焦个体车辆运动预测，尚未把预测结果与运动规划、控制等下游任务联动，距离完整自动驾驶系统仍有集成空间。

---
DOI: 10.1109/tai.2026.3672361
