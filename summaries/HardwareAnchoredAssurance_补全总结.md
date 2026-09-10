# Hardware-anchored assurance: A trusted resilience framework for critical edge infrastructure 总结

## 基本信息
- **标题**: Hardware-anchored assurance: A trusted resilience framework for critical edge infrastructure
- **作者**: Xinzhu Jiang, Bo Zhao, Peiwen Chen, Chunyu Yang, Juncheng Tong
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105137
- **PDF**: [COSE_2026_HardwareAnchoredAssurance.pdf](papers/COSE_2026_HardwareAnchoredAssurance.pdf)

## 一句话概括
TRCI 以硬件信任为锚点，把动态软件策略与可信恢复结合，面向云边连续体提供韧性保障。

## 问题与动机
固件等关键工件易成为 APT 目标，ROM 缺少灵活性，软件代理又扩大可信计算基并面临提权。系统被攻陷后，安全目标应从绝对阻止转向可检测和可恢复。

## 方法
TRCI 通过 Dual-Lock 协同 NVPM、TPM、Secure Execution Environment、watchdog 与远程 Resilience Authority。它检测并限制篡改，使受损状态无法被密码学隐藏，并执行确定性可信恢复。

## 实验与结果
生产级 x86 硬件上关键配置文件的端到端可信恢复延迟为 74 ms，并展示跨平台恢复能力。

## 贡献与局限
贡献是提出硬件—软件跨层韧性架构。局限是不能阻止所有内存态 Ring-0 绕过、物理篡改、侧信道和大规模 DoS，也不适合严格硬实时控制。

---
DOI: 10.1016/j.cose.2026.105137
