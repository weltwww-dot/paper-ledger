# PVCA: Privacy-Preserving and Verifiable Cross-System Authorization for Platoon Communications in VANETs 总结

## 基本信息

- **标题**: PVCA: Privacy-Preserving and Verifiable Cross-System Authorization for Platoon Communications in VANETs
- **作者**: Hang Liu, Yang Ming, Chenhao Wang, Yi Zhao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-05-27
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3697662
- **arXiv**: 无
- **PDF**: [TDSC_2026_PVCAPrivacyPreservingVerifiable.pdf](papers/TDSC_2026_PVCAPrivacyPreservingVerifiable.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 PVCA，通过优化的匿名 IBBE、policy-hiding ABE、跨系统授权令牌和零知识证明，实现车辆编队间从 IBBE 密文到 ABE 密文的直接、隐私保护且可验证的授权转换。

## 问题与动机

不同密码系统下的车辆编队合并需要让一个编队的成员访问另一个编队广播的数据；若采用解密后再加密，会增加延迟并影响实时指令。既有跨系统转换方案通常不能直接支持多接收者编队，且密文可能泄露车辆身份或属性，RSU 的转换结果也缺乏完整、实用的验证和公平机制。作者因此同时关注跨系统直接授权、身份/属性隐私、转换可验证性以及抗串通和经典 VANET 攻击。

## 方法

PVCA 以优化的 anonymous IBBE 保护原编队成员身份：在身份空间中加入 dummy identity，并用多项式技术避免传输完整身份集合。policy-hiding ABE 隐藏访问策略中的属性值集合并支持 large universe；授权令牌将 PHP 的身份密钥盲化，使 RSU 能把 IBBE 密文直接转换为 ABE 密文而不能取得该密钥。作者受 Fujisaki–Okamoto transformation 启发，将数据并入随机数 s=H2(M||σ)，使接收方能检查恢复结果；ZKPoK 证明用于证明属性匹配和辅助信息计算正确，同时避免泄露秘密密钥。系统流程包含初始化、编队建立、数据广播、跨编队授权和跨编队访问等阶段。

## 实验与结果

作者在桌面计算机和 Raspberry Pi 4 Model B 上实现原型，并用 NS-2 模拟双向八车道公路；原型使用 128-bit 安全等级的 Type A pairing、ECDSA/secp256k1，测试数据大小为 149 bytes。令 l=n1=n=30 时，PVCA 的加密时间为 0.14 s，而对比方案为 4.54、22.82、2.19、3.39 和 1.66 s；转换时间为 5.70 ms，而对比值为 34.98、11.37、11.73 和 334.86 ms；原密文解密为 0.04 s。授权令牌大小为 17.24 KB、原密文大小为 2.23 KB，较对比方案分别至少减少 15.20% 和 78.07%；编队规模为 10 时，仿真吞吐量在数据广播和跨编队访问中分别为 0.46 和 0.88 Mbps。

## 贡献与局限

本文把匿名 IBBE 与 policy-hiding ABE 连接为直接的跨系统编队授权，并在 chosen-plaintext、抗串通、可验证性和公平性模型下给出安全定理；原型和网络仿真显示其在资源受限车辆环境中的可行性。局限是原密文和授权策略相关密文大小随身份集合和访问策略线性增长；作者将大规模编队通信中的常数或次线性密文增长列为未来方向。全文还把更强 CCA 安全、降低 PKG 信任和车辆追踪/撤销作为可扩展讨论，而不是基础方案的主要实测结果。

---
DOI: 10.1109/tdsc.2026.3697662
