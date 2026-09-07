# NTRU-CLSC: Efficient Quantum-Resistant NTRU Lattice-Based Certificateless Signcryption Scheme for VANETs 总结

## 基本信息

- **标题**: NTRU-CLSC: Efficient Quantum-Resistant NTRU Lattice-Based Certificateless Signcryption Scheme for VANETs
- **作者**: Lu Wei, Yufeng Xi, Ruonan Ying, Jing Zhang, Hong Zhong, Jie Cui
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3707071
- **arXiv**: 无
- **PDF**: [TDSC_2026_NTRUCLSC.pdf](papers/TDSC_2026_NTRUCLSC.pdf)

## 一句话概括

面向车载自组织网络（VANETs），提出基于 NTRU 格的高效抗量子无证书签密方案 NTRU-CLSC，兼顾机密性、认证与批量验证效率。

## 问题与动机

VANETs 中车辆通过 OBU 与 RSU/应用服务器实时交换敏感数据，面临数据篡改、身份伪造与轨迹隐私泄露等威胁；量子计算又使基于离散对数和大整数分解的传统密码（ECC、双线性对）不再安全。现有 NTRU/格基无证书方案大多只支持身份认证而不提供机密性，或依赖一般格导致开销过高；同时普遍缺少对公钥替换攻击与长期固定密钥累积攻击的防护，高并发场景下缺少可扩展的批量验证手段。

## 方法

NTRU-CLSC 以多项式环运算构建无证书签密：KGC 使用 Antrag 陷门算法生成主公私钥，将用户公钥绑定到 KGC 主陷门以防公钥替换攻击；车辆与 AS 通过高斯采样生成部分私钥并结合本地秘密值形成完整密钥，消除证书管理与密钥托管问题。方案包含初始化、匿名化（假名）、初始密钥生成、动态密钥更新（周期刷新密钥抵御累积攻击）、签密（含拒绝采样与时间戳/计数器防重放）、解签密、RSU 侧无效密文过滤与打包、批量解签密等阶段，并借助假名技术与 TA 实现条件隐私保护与恶意车辆追踪。

## 实验与结果

在 Ubuntu 24.04、i7-11700 CPU、16GB RAM 环境下，取 p=512、q=12289、σ=2.0，目标 NIST 安全等级 1（128 位安全），每项操作执行 50 次取平均。签密与解签密开销分别为 121.42 ms 与 53.08 ms，三个阶段总计算开销 227.49 ms，相比 Yu 等（441.10 ms）、Prajapat 等（382.13 ms）、Ali 等（430.19 ms）、Sinha 等（468.63 ms）等现有方案总开销降低约 12.7%–51.5%，解签密阶段较 Module-LWE 类方案约快 25%。通信开销为固定 |m|+5|Z*q|+|t|=2824 字节。基于 Veins/OMNeT++/SUMO 的仿真（直行高速路段、车速 20 m/s、车辆密度 10–100）显示，其传输时延维持在 27–44 ms；密度达到 100 时延迟不超过 45 ms、丢包率低于 14.7%，在延迟与丢包控制上均优于对比方案。

## 贡献与局限

- **贡献**: 提出面向 VANETs 的首个将后量子安全与批量验证相结合的 NTRU 格无证书签密方案；集成 Antrag 陷门、动态密钥更新与批量验证，可抵抗公钥替换、累积及重放攻击；在随机预言机模型下基于 R-SIS 与 R-LWE 困难性证明了不可伪造性与 IND-CCA2 机密性；实验与仿真表明计算与通信开销显著优于现有抗量子签密方案。
- **局限**: 安全性证明基于随机预言机模型；仿真仅固定单一车速（20 m/s）的直行路段场景，通信开销分析为理论估算；作者未讨论真实车联网多跳拓扑与更高车速下的全面性能表现。

---
DOI: 10.1109/tdsc.2026.3707071
