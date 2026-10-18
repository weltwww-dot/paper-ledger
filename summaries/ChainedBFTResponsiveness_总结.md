# Unraveling Responsiveness of Chained BFT Consensus With Network Delay 总结

## 基本信息

- **标题**: Unraveling Responsiveness of Chained BFT Consensus With Network Delay
- **作者**: Yining Tang, Mohan Yu, Qihang Luo et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing · 2026
- **发表**: 2026-07-01
- **日期来源**: 出版社正式PDF第1页Date of publication；卷期及current version不替代首次在线日期
- **内容状态**: 完整
- **内容说明**: 已对照15页正式版复核方法、实验及边界，主agent亲自审定中文
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3708552
- **版本**: 出版社正式版（Version of Record），15页，卷/期/页23/5/11018-11032
- **PDF**: [TDSC_2026_ChainedBFTResponsiveness.pdf](papers/TDSC_2026_ChainedBFTResponsiveness.pdf)

## 一句话概括

用马尔可夫决策过程寻找链式拜占庭容错共识的最坏攻击策略，再通过实现实验检验响应性在网络延迟和恶意节点存在时的收益。

## 问题与动机

节点都遵循协议时的吞吐量和延迟比较，难以说明共识在攻击下还能保持多少性能。响应性允许按实际网络延迟推进，但恶意领导者可能利用协议规则削弱这种优势。

## 方法

为CHS、2CHS和FHS设计状态、对手动作、转移与奖励，求使链增长率或提交率最差的攻击策略，并接入Bamboo平台。链增长率衡量主链加入诚实区块的速率，提交率衡量区块提交事件频率；两者不是同一指标（PDF第3—11页）。

## 实验与结果

在理论评估中，恶意比例由0升至0.3时，CHS链增长率从0.333降至0.046，FHS从0.5降至0.073。响应性的优势随攻击比例上升而缩小；固定及波动网络延迟下的实现实验总体支持这一趋势。这些为模型设定下的指标值，不是实网每秒交易数（PDF第9—12页）。

## 贡献与局限

贡献是连接最坏情形策略搜索与可执行平台验证，揭示响应性收益的攻击边界。分析聚焦全局稳定时间GST之后，假定固定恶意比例和理想化攻击者协调；未覆盖自适应腐化和激励型攻击，异质广域网延迟可能改变具体结果（PDF第13—14页）。

---
DOI: 10.1109/tdsc.2026.3708552 | PDF: [TDSC_2026_ChainedBFTResponsiveness.pdf](papers/TDSC_2026_ChainedBFTResponsiveness.pdf)
