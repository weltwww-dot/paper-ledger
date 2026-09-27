# Sequential Estimation of Remaining Useful Life Through VAE-Based Deep Reinforcement Learning With Reward Shaping 总结

## 基本信息
- **标题**: Sequential Estimation of Remaining Useful Life Through VAE-Based Deep Reinforcement Learning With Reward Shaping
- **作者**: Hima Soni、Vibha Patel、Arnav Modanwal et al.
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-09-22
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07152-5
- **PDF**: [ML_2026_VAERemainingUsefulLife.pdf](papers/ML_2026_VAERemainingUsefulLife.pdf)

## 一句话概括
本文把变分自编码器构造的退化状态代理环境与 actor-critic 深度强化学习结合，以序贯策略优化设备剩余寿命预测。

## 问题与动机
工业设备剩余寿命估计通常依赖监督序列模型，难以在潜在状态空间中逐步修正退化轨迹。作者探索如何压缩多传感器信息，同时利用序贯决策优化预测，并比较奖励设计的影响。

## 方法
变分自编码器将传感器数据编码为潜变量并充当强化学习代理环境；TD3 与 PPO 策略在潜在空间迭代优化退化轨迹。实验比较不同奖励形式，并在 NASA C-MAPSS FD002 上与 LSTM、MLP 比较。

## 实验与结果
PPO 在 12 种配置中的 11 种呈现更稳定收敛；加权余弦相似度奖励在 10 种配置中取得具有较大效应量的可比精度。最佳变体 RMSE 为 0.1262，较论文所列 LSTM、MLP 基线改善 26.7%–40.3%。

## 贡献与局限
- 整合生成式潜变量表征、序贯策略优化和奖励塑形用于 RUL 估计。
- 系统比较策略和奖励配置对稳定性及精度的影响。
- 验证主要依赖单一基准与学习得到的代理环境；其他设备、真实传感器漂移及在线部署仍需验证。

---
DOI: 10.1007/s10994-026-07152-5
