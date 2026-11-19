# Tempered fractional rabies dynamics with deep neural surrogate modeling: Analysis, computation, and prediction 总结

## 基本信息
- **标题**: Tempered fractional rabies dynamics with deep neural surrogate modeling: Analysis, computation, and prediction
- **作者**: Mohamed Nidhal Sallami、Ouissem Ben Fredj、Praveen Agarwal 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109788
- **发表**: 2026-10-19
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109788

## 一句话概括
论文建立带指数记忆衰减的八舱室人—犬狂犬病模型，并训练神经代理器近似其数值解，以加快多情景、多步预测。

## 问题与动机
狂犬病潜伏期和进展时间具有记忆特征，经典常微分模型难以表达历史影响；而分数阶模型的非局部求解成本较高，反复仿真不便。作者希望兼顾生物学可解释的记忆衰减、模型基本性质与高效的自由运行预测。

## 方法
模型用阶数 ξ∈(0,1] 的 tempered Caputo 导数替代经典导数，λ控制历史影响的指数衰减；八个舱室描述人群及犬群感染过程。作者证明非负性、有限时间有界性和解的存在唯一性，并分析基本再生数阈值。数值求解采用乘积积分预测—校正法；代理网络以短历史窗的对数状态预测对数状态增量，先做单步训练，再用可微多步 rollout 微调。

## 实验与结果
单步测试 RMSE=0.4121、MAE=0.1303、R²=0.999998。40天基准情景自由运行的平均 R²=0.9990、平均 RMSE=3.32；对27个 tempered 参数情景，R²均值为0.9989±0.0021，连续采样情景套件为0.9973±0.0031。近无 tempering 区域（λ<0.05）自由运行明显退化，λ=0的部分轨迹 R²<0。

## 贡献与局限
论文把分数阶记忆与可校验的流行病动力学性质、神经代理多步预测结合，报告了从单步到自由运行的验证及消融。结果支持 tempered 参数范围内高效复现数值求解器，但代理预测的是模型轨迹而非真实疫情；λ接近0时长记忆导致误差累积，真实监测数据校准、参数不确定性与外部有效性仍需研究。

---
DOI: 10.1016/j.neunet.2026.109788
