# MSTE-CAN: Multi-channel Spatial-Temporal Encoding and Coordinate Attention-based ResNet for high-efficiency CAN bus intrusion detection 总结

## 基本信息

- **标题**: MSTE-CAN: Multi-channel Spatial-Temporal Encoding and Coordinate Attention-based ResNet for high-efficiency CAN bus intrusion detection
- **作者**: Luofei Jia, Jian Zhang, Lingxuan Li, LingYun Yan, Dafei Lin, Zhongyi Zhou
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105133
- **PDF**: [COSE_2026_MSTE_CAN.pdf](papers/COSE_2026_MSTE_CAN.pdf)

## 一句话概括

提出 MSTE-CAN：把一维 CAN 总线报文流编码成多通道时空图像（多通道时空编码 MSTE + 坐标注意力 ResNet-18），在严格边缘计算时延约束下实现高精度、可字节级定位的 CAN 总线入侵检测。

## 问题与动机

CAN 总线缺少内建安全机制，车辆边缘设备算力与时延受限；既要高精度检测细微的伪造/注入攻击，又要满足实时性。传统一维时序检测方法难以同时捕获空间、时间与统计维度的攻击特征，且轻量模型与检测精度之间存在权衡。

## 方法

把离散 1D CAN 报文序列重构成高判别力的 2D 视觉表示：MSTE 将车辆流量分解为三个正交物理维度并各编码为一个互补视觉通道——空间状态（R）、时间差分（G）、统计偏移（B），生成 27×9×3 特征张量并经最近邻缩放为 224×224×3 三通道图像；分类用轻量 ResNet-18，并在最浅层（Conv1/浅层残差块）集成坐标注意力（CA），保留细粒度空间结构以支持字节级异常定位，同时控制计算开销。

## 实验与结果

在 Car-Hacking-Dataset 上达到测试准确率 99.96%、ROC-AUC 0.9999、FPR 0.03%、FNR 0.06%；跨数据集（ROAD）准确率 95.85%，并在 HCRL 等平台评估跨平台攻击表征。消融确认坐标注意力置于最浅层可在异常定位与推理速度间取得最优平衡。

## 贡献与局限

- 贡献一：MSTE 编码——把 CAN 流量按空间/时间/统计三维正交信息转成多通道图像，暴露传统一维方法难以捕获的攻击签名。
- 贡献二：浅层坐标注意力 ResNet-18 的轻量配置，支持字节级异常定位与边缘实时部署。
- 局限：结果来自公开数据集（含 Car-Hacking/ROAD/HCRL），真实车载多 ECU 复杂场景与对抗性攻击下的鲁棒性仍需更多验证。

---

DOI: 10.1016/j.cose.2026.105133
