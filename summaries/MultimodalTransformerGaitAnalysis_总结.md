# Multimodal Transformer-Based Gait Analysis and Deep Learning Model for Slip-Resistant Footwear Evaluation

## 基本信息

- **标题**: Multimodal Transformer-Based Gait Analysis and Deep Learning Model for Slip-Resistant Footwear Evaluation
- **作者**：Shaghayegh Chavoshian、Atena Roshan Fekr
- **期刊 / 会议**：IEEE Transactions on Artificial Intelligence 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tai.2026.3681277
- **arXiv**：无
- **PDF**：[TAI_2026_MultimodalTransformerGaitAnalysis.pdf](papers/TAI_2026_MultimodalTransformerGaitAnalysis.pdf)

## 一句话概括

本文融合步态时间序列、鞋底图像、鞋底材料和人体测量信息，以 Transformer 回归模型预测个体化鞋类抗滑性能，揭示干冰和湿冰环境下预测可靠性的明显差异。

## 问题与动机

机械摩擦测试可以提供标准化的鞋底抗滑指标，但难以反映真实行走中的个体步态、环境变化和人体差异；仅汇总多名参与者的结果又会掩盖个体的生物力学特征。论文以最大可接受倾角（MAA）为抗滑性能指标，希望通过人本步态数据与鞋底视觉/材料信息的多模态融合，实现更贴近真实使用情境的个体化评估，并比较湿冰、干冰环境下的泛化能力。

## 方法

研究在受控冰面环境中让参与者逐步增加坡度，直到第一次滑倒，再以回退确定 MAA。视频经 MediaPipe 提取全身关键点，得到步长、关节角、质心速度、躯干稳定性等 18 类生物力学变量；通过 Pearson 相关、互信息和 PageRank 网络分析筛选关键特征。步态序列重采样为 30 帧并映射到 64 维，经过两层、每层四头注意力的 Transformer 编码器；鞋底图像由 ImageNet 预训练的 MobileNet 提取，另加入硬度、鞋底材料、身高和体重，最后用带 ReLU、dropout 的全连接回归头预测 MAA。训练使用 RMSE 损失、十折交叉验证和早停，并分别对湿冰与干冰建模。

## 实验与结果

数据来自 18 名参与者、84 类冬季鞋和 578 次摄像步行试验，最终结果按湿冰和干冰各 289 次进行分析。网络分析稳定筛出了右膝角、脚跟着地时质心速度、步长、躯干稳定性、体重和身高等关键变量。十折交叉验证中，干冰的 RMSE 为 1.34±0.34°、MAE 为 1.05±0.28°、MAPE 为 10.48±3.58%、R² 为 0.45±0.09；湿冰对应 RMSE 为 2.34±0.43°、MAE 为 1.92±0.43°、MAPE 为 21.45±6.89%、R² 为 0.47±0.12。留一受试者验证只使 RMSE 增加约 6.1%–6.2%，说明对未见参与者仍有一定泛化能力，但湿冰误差和折间波动明显更大。

## 贡献与局限

论文把个体步态时序、鞋底纹理和材料属性放入同一预测框架，证明引入生物力学信息能够比只使用鞋类属性更准确地估计抗滑性能，并给出按环境区分的误差、偏差和未见受试者分析。局限在于参与者年龄范围偏窄，多数低于 30 岁，且疲劳、滑倒经历和心理因素未被充分控制；固定 30 帧重采样也可能丢失脚跟着地等事件的绝对时间。后续应扩大年龄和人群覆盖，采用可变长度或时间扭曲建模，并在更多真实环境中验证。

---
DOI: 10.1109/tai.2026.3681277
