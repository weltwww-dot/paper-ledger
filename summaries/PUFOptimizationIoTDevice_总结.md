# PUF optimization for IoT device authentication 总结

## 基本信息

- **标题**: PUF optimization for IoT device authentication
- **作者**: Raúl Aparicio-Téllez, Miguel Garcia-Bosque, Guillermo Díez-Señorans, Concepcion Aldea, Santiago Celma
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104958
- **arXiv**: 无
- **PDF**: [COSE_2026_PUFOptimizationIoTDevice.pdf](papers/COSE_2026_PUFOptimizationIoTDevice.pdf)

## 一句话概括

论文用轻量权重掩码优化补偿型测量 PUF，在不改变硬件架构的情况下提升物联网设备认证的可辨识性。

## 问题与动机

PUF 利用芯片制造差异生成设备唯一响应，但物联网设备同时受安全性和资源开销约束。既有提高 PUF 可辨识性的方案常需额外逻辑或逐设备调参，限制了规模化部署，因此论文研究可泛化的低开销优化。

## 方法

作者在 PUF 熵源提取的参数上施加两参数权重掩码，再进行响应位比较；该过程也可理解为用特定初值初始化补偿测量 PUF 的计数器。优化采用 BFGS，在少量训练设备上搜索参数，再在更大设备集合上验证泛化，不改变 PUF 硬件架构。

## 实验与结果

作者在多个公开 PUF 数据库和不同类型 PUF 上测试，并以 Equal Error Rate（EER）衡量可辨识性。结果显示 EER 最多可改善两个数量级；少量设备得到的最优掩码能够泛化到更大的设备集，同时不需要额外硬件资源。

## 贡献与局限

论文贡献了面向补偿型测量 PUF 的低开销优化策略，并验证了跨设备泛化。局限是掩码规模会影响搜索复杂度和优化时间，实验主要依赖公开数据库；未来可研究不同掩码结构和其他优化算法。

---
DOI: 10.1016/j.cose.2026.104958
