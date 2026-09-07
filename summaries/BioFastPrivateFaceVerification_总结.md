# BioFast: An Efficient Privacy-Preserving Face Verification Protocol From FHE and Cryptographic Hash Functions 总结

## 基本信息

- **标题**: BioFast: An Efficient Privacy-Preserving Face Verification Protocol From FHE and Cryptographic Hash Functions
- **作者**: Parhat Abla, Rongbin Huang, Yongqiang Li, Mingsheng Wang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-21
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 隐私计算与生物特征安全
- **DOI**: 10.1109/TDSC.2026.3715522
- **arXiv**: 无
- **PDF**: [TDSC_2026_BioFastPrivateFaceVerification.pdf](papers/TDSC_2026_BioFastPrivateFaceVerification.pdf)

## 一句话概括

BioFast 通过同态打包同时计算多个特征内积，并用基于密码哈希的非交互阈值比较替代复杂混淆电路，构建高效的隐私保护人脸验证协议。

## 问题与动机

远程人脸验证需要比较客户端人脸特征与服务器模板，但服务器可能被攻破或本身不诚实，直接处理特征会泄露敏感生物信息。已有方案把全同态加密当作黑盒使用，或依赖多轮交互的混淆电路，导致旋转、通信和在线交互开销较高。论文希望在不暴露人脸特征的同时降低验证协议的时间和通信成本。

## 方法

BioFast 面向三方验证结构，使用定制的同态打包技术，将多个特征向量和多个内积压缩进环元素中并并行计算；相比依赖特定模数的中国剩余定理打包，该方法适用于环上更广泛的模数。论文还设计基于密码哈希的隐私保护非交互阈值比较协议，减少混淆电路的通信轮次，并对注册、验证、压缩因子和误报误拒进行分析。

## 实验与结果

实验比较注册和验证阶段的同态运算、通信量与时间，并考察不同特征压缩因子。结果显示，在压缩因子不超过 128 时，准确率基本接近原始设置；更大的压缩会带来准确率下降，因此作者建议在效率和准确率之间采用约 128 的设置。与相关混淆电路方案相比，哈希阈值比较的通信频率更低，总通信量约为 2.5 KB，并在多个环维度下保持较好的时间效率。

## 贡献与局限

论文把适合人脸内积的同态打包和低交互阈值比较结合起来，降低了隐私保护验证中的计算与通信开销。局限在于协议性能依赖同态参数、网络质量和特征压缩，测试主要关注受控特征及半诚实参与者；恶意客户端、模板更新、活体检测、多模态生物特征和真实移动端部署仍需进一步验证。

---
DOI: 10.1109/TDSC.2026.3715522
