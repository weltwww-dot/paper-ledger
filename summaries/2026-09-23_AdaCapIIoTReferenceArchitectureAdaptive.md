# AdaCap-IIoT: A reference architecture for adaptive blockchain-enabled CapBAC 总结

## 基本信息
- **标题**: AdaCap-IIoT: A reference architecture for adaptive blockchain-enabled CapBAC
- **作者**: Argiro Anagnostopoulou、Dimitris Gritzalis、Ioannis Mavridis
- **期刊 / 会议**: Computers & Security 2026（在线发表；正式版卷期标注 2027）
- **发表**: 2026-09-23
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105155
- **PDF**: [COSE_2026_AdaCapIIoTReferenceArchitectureAdaptive.pdf](papers/COSE_2026_AdaCapIIoTReferenceArchitectureAdaptive.pdf)

## 一句话概括
AdaCap-IIoT 提出一种区块链辅助的自适应能力访问控制架构，使工业物联网授权随风险和数据流变化而调整。

## 问题与动机
现有区块链 CapBAC 往往只检查访问时的令牌，缺少统一的能力生命周期、撤销、隐私验证及授权后信息流监控。工业设备又受到资源和时延约束，频繁上链难以兼顾实时性与敏感信息保护。

## 方法
架构把链上信任锚与边缘验证、执行分离，以零知识证明核验能力而不暴露完整身份和令牌内容。模块化合约记录承诺及撤销证据，边缘侧依据上下文和信息流风险调整授权范围、有效期、委托权及撤销优先级。

## 实验与结果
论文通过文献比较与架构分析梳理既有方案在适应性、隐私和生命周期管理上的缺口，并给出动态授权流程和威胁覆盖分析。它属于参考架构研究，未报告实现原型的吞吐、时延或真实工业负载实验，因此不能声称性能改善已经测得。

## 贡献与局限
贡献是把授权后的数据流风险反馈纳入能力生命周期，并明确链上审计与链下执行的职责。安全性依赖账本、授权发行者和边缘节点等信任假设；证明开销、撤销传播、同步及受损边缘节点下的韧性仍需实现与验证。

---
DOI: 10.1016/j.cose.2026.105155
