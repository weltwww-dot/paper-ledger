# A spatiotemporal wind power forecasting method based on dual-view graph fusion and dual-granularity residual learning 总结

## 基本信息

- **标题**: A spatiotemporal wind power forecasting method based on dual-view graph fusion and dual-granularity residual learning
- **作者**: Zhiyong Fan, Zhengdong Jiang, Min Xia, Shuai Zhang, Ying Yan
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108923
- **arXiv**: 无
- **PDF**: [NN_2026_SpatiotemporalDualViewGraphNetwork.pdf](papers/NN_2026_SpatiotemporalDualViewGraphNetwork.pdf)

## 一句话概括

针对风电机群功率预测，提出基于物理空间邻近与历史功率统计相关双视角图融合及粗细双粒度残差时序学习的 ST-DVGN 网络，预测精度与缺失观测鲁棒性均优于基线。

## 问题与动机

风功率受风速风向等不稳定因素影响而间歇多变，精准预测对电网调度与大规模并网至关重要。现有时空图神经网络（ST-GNN）大多依赖单一静态图结构，表征能力有限且对机位节点数据缺失敏感；而动态图、异构图或多图建模方法往往只从单一视角建模，或将多视角过早聚合进统一图结构，难以保留各结构视角的独立信息。本文由此出发，研究无需复杂动态图更新或异构假设即可融合多视角结构信息、并在观测不完整时保持稳定预测的时空图学习框架。

## 方法

提出 Spatiotemporal Dual-View Graph Network（ST-DVGN），整体流水线为 Y = Temporal(Spatial(X))。核心模块一为双视角图融合（DVGF）：依据风机地理欧氏距离（小于阈值 τ 则连边、权重为 1）构建物理视角图，依据历史功率输出的皮尔逊相关系数 |r(xi, xj)| 构建全连接统计视角图；两图分别经各自独立 GCN 层与一层共享 GCN 层处理，得到四个尺度的空间特征，经图平均池化后由多尺度注意力加权融合（softmax 权重 α，加权和 s(t)），实现跨视角特征对齐与冗余抑制。核心模块二为残差增强双粒度时序（REDGT）：细粒度 LSTM 学习空间特征序列的局部波动；同时用窗口 k、步长 s 的滑动平均构造粗粒度序列，经粗粒度 LSTM 提取长期趋势特征并经线性投影上采样回原分辨率；最后将原始空间特征、细粒度与上采样趋势特征做逐元素残差融合，经 MLP 输出功率预测。训练采用 δ=1 的 Huber 损失。

## 实验与结果

基于 SDWPF 数据集（SCADA 系统、134 台风机、每 10 分钟采样），以 MAE、RMSE、R² 为指标。消融（单步预测）：去除统计视角或物理视角使 RMSE 分别上升约 36% 与 43%，去除共享 GCN、注意力融合、粗粒度路径与残差增强分别使 RMSE 上升约 70%（Model 4，RMSE 0.150）、67%（Model 5，0.147）与 17%（Model 6，0.103），完整 ST-DVGN 取得 MAE 0.052 / RMSE 0.088 / R² 0.990 最优。对比实验涵盖 10 分钟（1 步）、1 小时（6 步）、2 小时（12 步）三种预测长度，基线含 LSTM、GCN、TCN、Informer、CNN-LSTM、STGCN、STAGCN、ENDCC-AGCN-LSTM 及 ST-DVGN-TCN：短时预测 ST-DVGN 的 RMSE 为 0.088，比 STAGCN 低 14%、比 ENDCC-AGCN-LSTM 低 6%；2 小时预测 ST-DVGN 的 RMSE 为 0.292，较 ENDCC-AGCN-LSTM（0.443）降低约 34%，MAE 降低约 38%。复杂度上 ST-DVGN 仅 0.357M 参数、平均推理约 271.8ms，远低于 ENDCC-AGCN-LSTM（1.472M、约 1883ms）。簇级观测缺失鲁棒性实验（层次聚类将风场分为 25 簇，缺失 1–3 个簇、每簇 50% 或 100% 丢失，前向填充插值，重复 25 次）：ST-DVGN 在所有缺失场景下 MAE/RMSE 均最低，最严峻的三簇完全缺失下 RMSE（约 0.095）比最强基线 ENDCC-AGCN-LSTM 低约 14%，RMSE 最大退化仅约 6%，且方差更小、退化更平缓。

## 贡献与局限

贡献：从双视角图学习角度重新审视风电机群功率预测，无需动态图更新或异构图假设即融合物理邻近与功率统计相关两种结构视角，更具工程可行性；设计含独立/共享 GCN 与多尺度注意力融合的多级特征融合框架，提升跨视角一致表征与总体精度；提出残差增强双粒度时空耦合框架，并行建模短期波动与长期趋势并缓解深层网络退化；在簇级节点观测不完整等非理想条件下仍保持稳定的预测性能，具备较强的鲁棒性与实用性。局限：基于固定图结构建模，未涉及跨风场/跨工况的迁移能力与大规模部署下的计算开销问题；文中也指出未来可探索跨风场迁移学习，以及在不失信息连接的前提下对图进行稀疏化以降低计算成本。

---
DOI: 10.1016/j.neunet.2026.108923
