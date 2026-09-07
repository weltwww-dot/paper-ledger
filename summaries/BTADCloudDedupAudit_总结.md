# Enabling Transparent Integrity Auditing and Secure Deduplication Over Encrypted Cloud Storage Based on Blockchain 总结

## 基本信息

- **标题**: Enabling Transparent Integrity Auditing and Secure Deduplication Over Encrypted Cloud Storage Based on Blockchain
- **作者**: Yang Yang, Tianqing Zhu, Wenting Shen, Yanjiao Chen, Shanshan Li, Fei Chen, Jing Chen
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-17
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 云安全与数据安全
- **DOI**: 10.1109/TDSC.2026.3714758
- **arXiv**: 无
- **PDF**: [TDSC_2026_BTADCloudDedupAudit.pdf](papers/TDSC_2026_BTADCloudDedupAudit.pdf)

## 一句话概括

BTAD 将随机掩码、区块链透明去重和轻量哈希式所有权证明结合，在加密云存储中同时保护数据所有权隐私、审计完整性并抵抗重复伪造攻击。

## 问题与动机

加密云存储能够保护内容隐私，但安全去重和完整性审计通常会暴露用户拥有关系或去重模式；用户离线时，云服务商维护的去重关系还可能退化，攻击者也可能伪造重复文件以绕过所有权验证。论文希望在不泄露所有权隐私的前提下，让第三方能够公开验证数据完整性，并保持去重带来的存储效率。

## 方法

BTAD 用随机掩码处理文件标签和完整性证明，为不同用户生成不可链接的审计证据；将密文文件与所有者之间的去重关系记录在区块链上，由云服务商和用户共同维护透明去重状态；同时设计基于哈希的概率性所有权证明，避免每次验证都传输和检查完整文件。论文给出数据隐私、不可伪造、所有权隐私和抵抗去重模式退化等安全分析。

## 实验与结果

作者从计算、通信、存储和链上 gas 开销等方面比较 BTAD 与相关方案，实验结果支持其在完整性审计和安全去重上的效率优势。结果显示，后续更新可独立处理，整体开销随文件数量近似线性增长；在不同去重率下，BTAD 以较低 gas 消耗换取更强的所有权隐私与重复伪造防护，整体性能优于对比协议。

## 贡献与局限

论文首次把区块链透明去重、加密云完整性审计和概率所有权证明统一到一个协议中，改善了所有权隐私和云端去重模式退化问题。局限在于系统引入链上状态维护、第三方审计和概率验证，区块链可用性、链上费用、用户密钥管理及高频动态数据更新仍可能成为部署瓶颈。

---
DOI: 10.1109/TDSC.2026.3714758
