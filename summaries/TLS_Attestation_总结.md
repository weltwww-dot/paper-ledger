# Collusion-Minimized TLS Attestation Protocol for Decentralized Applications 总结

## 基本信息

- **标题**: Collusion-Minimized TLS Attestation Protocol for Decentralized Applications
- **作者**: Uğur Şen, Murat Osmanoğlu, Oğuz Yayla et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing · 2026
- **发表**: 2026-09-01
- **日期来源**: openalex-publication-date，保留来源精度；预印本日期不替代期刊发表时间
- **内容状态**: 完整 · 已对照现有PDF审校中文六段式；版本按本条记录
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3716834
- **版本**: 出版社正式正文（含内容已定稿的Early Access）
- **PDF**: [TDSC_2026_TLS_Attestation.pdf](papers/TDSC_2026_TLS_Attestation.pdf)

## 一句话概括

Πcoll-min将TLS证明改造成可导出、可联合验证的形式，减少去中心化应用中证明者与验证者共谋的风险，并避免按验证者逐次重复TLS会话。

## 问题与动机

智能合约需要可信的链下数据，而传统DCTLS依赖指定验证者，难以公开验证，也可能出现证明者与验证者共谋。简单复制验证会使证明者成本随验证者数量线性增加。

## 方法

通过dx-DCTLS把不可验证的两方计算组件替换为可验证组件，使单次TLS证明能够导出。结合分布式可验证随机函数与门限签名，多名辅助验证者联合验证和签署；作者形式化门限证明不可伪造性，并在密码学假设下给出安全论证。

## 实验与结果

原型比较DECO-DON复制基线，并评估多组门限规模。WAN1参数下，稳态单次证明约29秒，而三名活跃验证者重复DECO约34.8秒，后者随门限增长。WAN结果由实测计算成本叠加解析网络模型得到；证明者开销相对验证者规模保持常数，不代表全系统零增长。

## 贡献与局限

贡献是在兼容现有TLS服务器的前提下实现联合可验证的隐私证明，并降低重复验证成本。安全依赖门限、密码原语和底层DCTLS；请求语义及响应完整性仍需应用层约束，初始化、带宽和实现审计成本也不可忽略。

---
DOI: 10.1109/tdsc.2026.3716834 | PDF: [TDSC_2026_TLS_Attestation.pdf](papers/TDSC_2026_TLS_Attestation.pdf)
