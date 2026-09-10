# TrustTiny-HAR: Selective, Open-Set, and Calibrated Activity Recognition on Microcontrollers 总结

## 基本信息

- **标题**: TrustTiny-HAR: Selective, Open-Set, and Calibrated Activity Recognition on Microcontrollers
- **作者**: Ismail Lamaakal, Chaymae Yahyati, Yassine Maleh, Khalid El Makkaoui, Ibrahim Ouahbi
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3676723
- **arXiv**: 无
- **PDF**: [TAI_2026_TrustTinyHARSelectiveOpen.pdf](papers/TAI_2026_TrustTinyHARSelectiveOpen.pdf)

## 一句话概括

TrustTiny-HAR 把 int8 时序骨干、蒸馏信任头和流式保形预测结合到微控制器上，使活动识别系统能够校准置信度、识别未知活动并在证据不足时安全拒答。

## 问题与动机

可穿戴设备和环境传感器希望在微控制器本地完成活动识别，以满足隐私、低延迟和低功耗要求，但传统 TinyML 模型多为封闭集分类器，遇到未见活动、佩戴位置变化或传感器异常时会高置信度地做出错误判断。后处理校准通常缺少随数据流变化的覆盖保证，而集成模型或复杂不确定性头又超出微控制器的 RAM、Flash 和能耗预算。作者因此希望在端侧同时解决开放集识别、置信度校准和选择性预测问题，并在拒答后只上传紧凑特征而非原始信号。

## 方法

系统以 int8 深度可分离一维 CNN 或因果 TCN 为时序骨干，在其上加入蒸馏信任头，联合输出校准类别概率和 OOD 代理分数。OOD 分数由教师信号蒸馏而来，结合 logits 能量与 prototype/Mahalanobis 距离；轻量流式保形层维护端侧分位数，根据目标覆盖率生成接受阈值。当输入证据不足时系统拒答，并可选地发送 32–64 维特征 sketch 给更强的验证器，避免传输原始传感器数据。系统通过 leave-one-subject-out 评估未见类别、佩戴位置偏移和注入异常。

## 实验与结果

在 UCI HAR、PAMAP2 和 WISDM 上，TrustTiny-HAR 在保持端侧资源约束的同时提升可靠性。UCI HAR 的宏平均 F1 为 93.8，ECE 降至 2.4%；对未见活动的 AUROC 达到 0.96，对佩戴位置偏移的 FPR@95 为 0.22。在目标覆盖率 90% 下，使用仅含 128–512 个窗口的缓冲区即可达到约 6.1% 的选择性风险。nRF52840 和 STM32L4 实测相对 TinyCNN 的额外能耗低于 10%，并保持紧凑的 RAM/Flash 占用；消融显示保形层主要改善风险-覆盖控制，int8 量化相对 fp32 的 F1 损失约为 0.3 个百分点。

## 贡献与局限

贡献在于将开放集、校准、选择性拒答和端侧资源约束纳入同一 TinyML HAR 流程，并在真实微控制器上报告准确率、校准、延迟、内存和能耗。局限是保形覆盖保证依赖校准缓冲区与数据交换性，持续概念漂移、极少样本新活动和多传感器缺失可能破坏风险估计；32–64 维 sketch 交由更强模型处理还涉及额外通信和隐私治理。测试数据集与设备范围仍有限，医疗和安全关键场景需要更长期、多用户现场验证。

---
DOI: 10.1109/tai.2026.3676723
