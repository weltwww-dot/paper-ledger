# ContractDB: Secure and Efficient Integration of Large Legacy Data With Blockchain DApps 总结

## 基本信息

- **标题**: ContractDB: Secure and Efficient Integration of Large Legacy Data With Blockchain DApps
- **作者**: Yingjie Xue, Xinyi Luo, Meiqi Li, Kaiping Xue, Yunshu Wang, Lutong Chen
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-08
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 区块链与分布式系统
- **DOI**: 10.1109/TDSC.2026.3711164
- **arXiv**: 无
- **PDF**: [TDSC_2026_ContractDBVerifiableDApp.pdf](papers/TDSC_2026_ContractDBVerifiableDApp.pdf)

## 一句话概括

ContractDB 把大型遗留数据的存储和查询外包给可验证数据库，通过认证字典、认证集合操作和可争议更新机制，为区块链 DApp 提供低成本的复杂查询验证。

## 问题与动机

链上保存大规模数据非常昂贵，以太坊智能合约原生查询能力也难以支持范围条件和多条件组合查询；直接把数据放到链下又会削弱结果可信度。现有可验证数据库在结果验证成本和公开更新方面仍有不足。论文希望让 DApp 在不把全部数据上链的情况下，仍能验证外部数据库返回的查询结果。

## 方法

ContractDB 由区块链智能合约和外部可验证数据库组成，数据与复杂查询在链下执行，合约只验证结果证明。作者使用认证字典表示记录和键值关系，使用认证集合操作支持相等、范围及集合组合查询，并设计可争议更新机制：更新结果由公开验证，发生争议时再进入核验流程，从而降低每次更新的链上成本。

## 实验与结果

实验表明，ContractDB 能在 220 行数据表上验证包含 6 个混合等值和范围条件的合取查询，成本约 240 万 gas；若直接把相同数据存入合约，成本超过 360 亿 gas，且仍不支持范围或多条件查询。结果说明，外部可验证数据库能够显著降低数据密集型 DApp 的存储和查询验证成本。

## 贡献与局限

论文贡献了面向 DApp 的可验证数据库框架、认证数据结构和公开可验证更新机制，解决链上数据昂贵与复杂查询不足之间的矛盾。局限在于证明生成、链下数据库可用性和争议处理仍需可信的系统运营，实验规模和查询类型也有限；更大数据量、频繁更新、恶意服务端和跨链场景的性能与激励机制仍需研究。

---
DOI: 10.1109/TDSC.2026.3711164
