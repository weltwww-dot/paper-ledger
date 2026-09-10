# APKOS: Accurate and Privacy-Preserving Keyword Spotting for Intelligent Voice Assistant Systems 总结

## 基本信息

- **标题**: APKOS: Accurate and Privacy-Preserving Keyword Spotting for Intelligent Voice Assistant Systems
- **作者**: Peijia Zheng, Jingyi Chen, Zhuoyuan Chen, Huiyu Zhou
- **期刊 / 会议**: ACM TOPS 2026
- **发表**: 2026-08-26
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3838797
- **arXiv**: 无
- **PDF**: [TOPS_2026_APKOSPrivacyPreservingKWS.pdf](papers/TOPS_2026_APKOSPrivacyPreservingKWS.pdf)

## 一句话概括

APKOS 面向云端语音助手的第二阶段关键词唤醒验证，利用 CKKS 同态加密和专门设计的 HE 友好 CNN，在保护语音语义安全的同时提升加密域关键词识别的准确率、鲁棒性和效率。

## 问题与动机

云端语音助手通常把本地设备捕获的语音发送到服务器处理，误唤醒可能导致约 10 秒至 1 分钟的私密语音泄露。直接在同态加密数据上执行关键词唤醒虽能避免服务器看到明文，但受限于乘法深度、密文计算开销以及 ReLU 等操作不兼容等问题，现有方案的性能和效率仍不足。论文因此研究一种能够在 CKKS 语义安全约束下保持高精度的实值 CNN 架构。

## 方法

APKOS 采用 CKKS 作为底层同态加密方案，并构造面向关键词唤醒的 HE 友好残差网络。作者提出 PReLUR 实值多项式激活函数，以适应加密计算并改善训练稳定性；提出融合层，将激活与池化相关计算合并，把部分密文操作转为明文操作，从而减少高成本的密文乘法和乘法深度。网络还使用针对时序语音特征的卷积核扩展策略，重点增大首层卷积核，并利用 SIMD 对批量音频进行并行推理。系统在客户端加密后由云端完成第二阶段 KWS 验证，云端只处理密文。

## 实验与结果

实验在 Ubuntu 18.04.5、Intel Xeon Gold 6145、125 GB RAM 上使用 C++、HEAAN 和 CKKS 实现；数据采用 Google Speech Commands v1/v2，分别包含 65,000 个 30 词样本和 105,000 个 35 词样本，音频从 16 kHz 重采样到 8 kHz，并在 30/35/40 dB 噪声条件下测试。APKOS 在 GSC v1/v2 上的准确率分别为 82.1% 和 80.1%，30 dB 噪声下为 81.9% 和 77.3%；相较 CryptCNet，批处理摊销推理时间为 6.3 秒，而对方为 16.4 秒。融合层将总运行时间从 6854.24 秒降至 6487.27 秒；客户端加密、序列化和传输的总非服务器开销为 42.9 ms。与 HE 适配的明文模型相比，APKOS 达到 80.1% 且训练稳定，而 MatchboxNet 未收敛，QKWS、BCResNet 和 AttentionRNN 的适配准确率分别为 77.5%、75.8% 和 67.3%。

## 贡献与局限

- 贡献一：提出结合 PReLUR、融合层、残差网络和卷积核扩展的 APKOS，实现语义安全的云端加密关键词唤醒，并在准确率、鲁棒性、F1、ROC 和 PR 等指标上优于对比安全方案。
- 贡献二：通过复杂度、运行时间、端到端开销和明文模型 HE 适配实验，说明专门面向同态加密设计网络比直接改造普通语音模型更稳定、更高效。
- 局限与开放问题：实验主要基于相对受控的英语基准数据，尚未系统覆盖非英语语音、不同口音和多人重叠语音；6.3 秒是批量 SIMD 的摊销服务器成本，并非单查询延迟。后续仍需研究大词汇连续语音的加密识别，以及 FPGA/ASIC 等硬件加速下的实时性。

---
DOI: 10.1145/3838797
