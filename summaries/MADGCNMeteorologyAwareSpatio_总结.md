# MADGCN: A Meteorology-Aware Spatio-Temporal Graph Convolution Network for Long-Term Air Pollution Forecasting 总结

## 基本信息

- **标题**: MADGCN: A Meteorology-Aware Spatio-Temporal Graph Convolution Network for Long-Term Air Pollution Forecasting
- **作者**: Binwu Wang, Zhiqing Cui, Guangjun Wang, Zhengyang Zhou, Fan Meng, Jingjia Luo, Yang Wang
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3692204
- **arXiv**: 无
- **PDF**: [TKDE_2026_MADGCNMeteorologyAwareSpatio.pdf](papers/TKDE_2026_MADGCNMeteorologyAwareSpatio.pdf)

## 一句话概括

MADGCN 将空气质量序列分解、气象驱动的动态因果发现、物理邻接图与因果图卷积结合起来，并通过 PatchMixer 建模长时段依赖，从而提升长期空气污染预测在概念漂移和高污染场景下的稳定性。

## 问题与动机

现有时空图神经网络往往只在单一时间尺度上建模，预测跨度变长后难以处理季节性、长期趋势和概念漂移；气象变量也常被当作普通辅助特征，未充分利用其对污染传播的因果作用。此外，许多公开空气质量数据集覆盖范围较小、时间较短，难以验证全国尺度长期预测的泛化能力。作者因此构建更大范围的数据基准，并希望同时捕捉空间邻近关系、气象驱动的跨站点影响和多尺度时间变化。

## 方法

模型首先用 STL 将 AQI 序列分解为趋势、季节和残差，分别刻画长期分布变化、周期模式和短期扰动；再以 Granger 因果关系为基础，从 AQI 与气象历史观测中发现随时间变化的有向因果结构。因果结构与地理邻近关系共同形成物理邻接图和气象因果图，由因果感知图卷积模块联合建模站点间的扩散与影响路径。最后，PatchMixer 在分段时间序列上进行跨 patch 交互，学习局部和长期依赖，并通过季节成分增强模块改善周期预测。

## 实验与结果

作者构建 LargeAQ 数据集，覆盖中国 343 个城市、1341 个监测站以及 2016—2023 年的小时级 PM2.5 和气象数据，并在 KnowAir 的 Standard、Heating 和 Volatile 子集上验证泛化能力。与 16 个基线相比，MADGCN 在各预测跨度上总体取得最佳结果；在 24 小时预测中，MAE/RMSE 为 18.57/27.79，MAE 比 PITS 低 5.3%、比 PM2.5-GNN 低 8.3%，从 12 小时扩展到 96 小时时 MAE 增幅为 41.2%。去除图模块、物理图、因果图、气象因素或 STL 后误差均上升；与 AirFormer 相比，参数复杂度降低 3.64 倍，训练和推理时间分别降低 7.52 倍和 7.71 倍。

## 贡献与局限

贡献在于把长期序列分解、动态气象因果发现、双图时空建模和 patch 级时间学习统一为一个全国尺度空气质量预测框架，并公开了覆盖范围更大的 LargeAQ 数据。局限是 Granger 因果关系仍依赖观测数据和建模假设，缺失值处理及气象数据融合可能影响因果结构可靠性；模型训练仍需要较高算力，极端污染、突发气象和跨区域迁移场景的表现还需更多实地验证。未来可进一步引入物理约束、在线更新和多源外生数据。

---
DOI: 10.1109/tkde.2026.3692204
