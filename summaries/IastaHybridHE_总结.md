# Iasta: An Efficient Cipher for Hybrid Homomorphic Encryption in Cloud-Assisted IoT 总结

## 基本信息

- **标题**: Iasta: An Efficient Cipher for Hybrid Homomorphic Encryption in Cloud-Assisted IoT
- **作者**: Bo Yang, Liquan Chen, Chenyue Yin, Ziyan Zhang, Shang Gao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-21
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 密码学与物联网安全
- **DOI**: 10.1109/TDSC.2026.3715690
- **arXiv**: 无
- **PDF**: [TDSC_2026_IastaHybridHE.pdf](papers/TDSC_2026_IastaHybridHE.pdf)

## 一句话概括

Iasta 是面向云辅助物联网混合同态加密的流密码，通过低 AND 深度、低随机性和分支并行同态求值，降低客户端加密及服务器转换开销。

## 问题与动机

物联网设备资源、带宽和存储受限，而全同态加密虽然支持密文计算，却会产生严重的密文膨胀和计算延迟。混合同态加密让客户端先使用对称密码、服务器再转换为 FHE 格式，能够降低带宽，但现有方案仍存在客户端计算成本高、服务器同态转换重以及随机性消耗大的问题。论文希望设计更适合整数型 HHE 的密码结构。

## 方法

Iasta 采用多项式模运算支持非二元明文空间，并使用基于旋转的线性变换生成随机矩阵，减少仿射层所需随机性。作者以双 S 盒非线性层替代原有设计，在保持目标安全级别的同时减少轮数；在 SEAL 库中进一步实现分支并行同态求值，结合分层和逆旋转处理密文布局，以降低从对称密文到 FHE 计算的转换开销。

## 实验与结果

作者在 SEAL 中将 Iasta 与面向有限域、已知速度较快的 Pasta 实现比较。结果显示，客户端吞吐量约提高 2 倍，同时存储成本降至一半；服务器侧吞吐量提高约 3–5 倍，运行时间加速约 2 倍。实验表明，Iasta 在整数型混合同态加密的客户端轻量性和服务器并行求值方面具有优势。

## 贡献与局限

论文贡献了适配 HHE 的非二元流密码结构、低随机性线性变换、双 S 盒设计和分支并行同态求值实现。局限在于性能依赖 SEAL、底层 FHE 参数和硬件后端，安全性与实现正确性还需要更广泛的密码分析；真实物联网设备、密钥管理、不同聚合算子及恶意云端模型下的部署成本仍需评估。

---
DOI: 10.1109/TDSC.2026.3715690
