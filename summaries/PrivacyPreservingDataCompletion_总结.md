# Privacy-Preserving Data Completion With Location and Value Obfuscation in Spatial Crowdsourcing 总结

## 基本信息

- **标题**：Privacy-Preserving Data Completion With Location and Value Obfuscation in Spatial Crowdsourcing
- **作者**：Wenbin Liu、Hao Du、Lanxin Li、Qi Deng、Liang Wang、Funing Yang、En Wang、Jie Wu
- **期刊 / 年份**：IEEE Transactions on Dependable and Secure Computing，2026
- **研究方向**：信息安全
- **DOI**:10.1109/TDSC.2026.3697883
- **PDF**：[TDSC_2026_PrivacyPreservingDataCompletion.pdf](papers/TDSC_2026_PrivacyPreservingDataCompletion.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出同时扰动位置和数值的差分隐私数据补全框架，把用户位置映射到对补全更有价值的区域，并依据预测的时空关系调整上报值，从而在保护位置隐私的同时降低补全误差。

## 问题与动机

空间众包的观测通常稀疏，数据补全需要详细的时空位置与数值信息，而这些信息可能暴露用户移动模式、健康状况和生活习惯。仅对位置加噪会破坏补全所依赖的空间—时间相关性，且被映射位置上的原始数值不再一致；已有方法还可能带来较高计算开销。因此作者关注隐私预算、补全可用性、位置重要性和端侧效率之间的联合权衡。

## 方法

框架由预测模型、混淆机制和补全模型组成。基于历史数据训练的 Transformer 预测模型输出位置重要性矩阵 (I) 与数值关系矩阵 (R)；线性规划以 (I) 为目标，在 ε-差分隐私约束下构造位置混淆概率矩阵 (K)，使报告位置更偏向能支持补全的关键区域。用户按 (K) 采样混淆位置，并用 (v'_r=v_i-R[ell_i,ell_r]) 调整数值；作者用直径 2-critical 图把差分隐私约束的复杂度从完全图情形的 (O(|L|^3)) 降到 (O(|L|^2))，服务器再用预训练的 ST-Transformer 完成数据。

## 实验与结果

实验使用五个真实数据集：北京空气质量（NO2、PM2.5）、伦敦天气（风速、湿度）和加州高速公路交通流，均以 32 个传感器为基础，并比较 DU-Min、L-SRR、Geo-Ind、Average、Laplace 和 Self。以 5 名感知用户、ε=ln 4 为例，所提方法在各数据集上的补全误差始终最接近无混淆的 True；多变量混淆时仍取得最低 MAE 与 RMSE。消融显示重要性矩阵和关系矩阵都能改善结果，预测模型损失权重整体以 λ=0.8 最优；模拟攻击下位置推断成功率约为 4%，Average 基线约为 2%，作者认为这是换取补全准确性的可接受代价。Pixel 9a 端侧推理延迟为 0.660 ms/次，100 次估计能耗为 0.082438 mWh；优化线性规划在位置数超过 100 前仍未达到约 10 s 的耗时阈值。

## 贡献与局限

主要贡献是把位置选择与数值校正统一到差分隐私数据补全流程中，并用预测得到的关键位置和动态时空关系同时提升数据可用性与补全准确性；直径 2-critical 图和端侧轻量推理也改善了可部署性。局限是实验数据均为标量时序，模型尚未处理图像等非标量数据；在缺少历史数据的新区域会出现冷启动问题，且当前框架未显式建模轨迹关联、跨时段链接或语义先验攻击。作者将多变量/非标量扩展、跨轮隐私预算管理和攻击感知混淆策略列为后续方向。
