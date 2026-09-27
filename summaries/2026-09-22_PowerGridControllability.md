# Situational awareness through security-based analysis of controllability and observability in power grids 总结

## 基本信息
- **标题**: Situational awareness through security-based analysis of controllability and observability in power grids
- **作者**: Mohammed Asiri、Neetesh Saxena、Subhash Lakshminarayana
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-22
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105156
- **PDF**: [COSE_2026_PowerGridControllabilityAwareness.pdf](papers/COSE_2026_PowerGridControllabilityAwareness.pdf)

## 一句话概括
本文以电网可控性和可观测性指标衡量网络攻击对电力系统态势感知能力的结构性影响。

## 问题与动机
电力系统的网络控制与物理过程深度耦合，攻击可能削弱操作员观测或调节系统状态的能力，却未立即造成停电。传统告警未必体现这类系统级能力退化，作者因而引入控制理论指标。

## 方法
研究建立电网与通信控制过程的联合仿真，构造可控性、可观测性指标，并注入虚假控制命令、负荷重分配和虚假数据注入三类攻击，比较攻击前后的能力变化。

## 实验与结果
仿真中虚假命令注入使可控性下降 25.8%、可观测冗余下降 32.6%；负荷重分配使控制能力下降 13.4%；虚假数据注入使可观测性裕度下降 33.5%。不同攻击呈现不同影响模式。

## 贡献与局限
- 将可控性、可观测性变化作为电力系统网络攻击影响的量化态势指标。
- 通过多种攻击情景的联合仿真展示指标区分能力。
- 证据来自仿真模型与有限攻击场景；真实电网复杂拓扑、噪声和运行限制下的预警效用仍需实测验证。

---
DOI: 10.1016/j.cose.2026.105156
