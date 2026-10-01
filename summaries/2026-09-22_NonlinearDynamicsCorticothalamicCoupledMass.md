# Nonlinear dynamics of a corticothalamic coupled neural mass model reproduce the mechanism of 40 Hz ASSR generation 总结

## 基本信息
- **标题**: Nonlinear dynamics of a corticothalamic coupled neural mass model reproduce the mechanism of 40 Hz ASSR generation
- **作者**: Mu Zhu、Xiaoya Liu、Xinmeng Guo 等
- **期刊 / 会议**: Neural Networks 2026（在线发表；正式版卷期标注 2027）
- **发表**: 2026-09-22
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109683
- **PDF**: [NN_2026_NonlinearDynamicsCorticothalamicCoupledMass.pdf](papers/NN_2026_NonlinearDynamicsCorticothalamicCoupledMass.pdf)

## 一句话概括
ACT-NMM 将皮层与丘脑神经群体纳入闭环动力学模型，解释 40 Hz 听觉稳态响应的生成及同步机制。

## 问题与动机
已有神经群体模型主要描述皮层局部回路，较少统一考虑丘脑前馈传递、丘脑网状核反馈抑制和不同皮层抑制性细胞的作用。仅拟合宏观振荡，难以说明耦合强度和时间常数如何共同产生稳定响应。

## 方法
模型耦合皮层锥体细胞、PV 与 SST 中间神经元，以及丘脑中继和网状核神经元，加入双向传输延迟。作者在生理约束下扫描耦合强度与时间常数，用功率谱、相位锁定、分岔及信息结构指标分析响应。

## 实验与结果
数值仿真重现了稳定的 40 Hz 振荡；相较 20 Hz 和 30 Hz 刺激，40 Hz 的相位与频率锁定更强。结果支持皮层为主要响应发生源、丘脑承担相位对齐及中继调节的模型解释，而非独立产生强响应。

## 贡献与局限
贡献是把细胞类型差异与丘脑闭环调节连接到可解释的群体动力学。模型简化了离子电流和长程耦合，使用的锥体细胞放电率并非 EEG 或 LFP 振幅；尚需前向观测模型和实测电生理校准，不能把仿真结论当作已验证的临床指标。

---
DOI: 10.1016/j.neunet.2026.109683
