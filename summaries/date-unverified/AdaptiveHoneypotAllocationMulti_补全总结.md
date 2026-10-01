# Adaptive Honeypot Allocation in Multi-Attacker Networks via Bayesian Stackelberg Games 总结

## 基本信息
- **标题**: Adaptive honeypot allocation in multi-attacker networks via Bayesian Stackelberg Games
- **作者**: Dongyoung Park, Gaby G. Dagher
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104949
- **PDF**: [COSE_2026_AdaptiveHoneypotAllocationMulti.pdf](papers/COSE_2026_AdaptiveHoneypotAllocationMulti.pdf)

## 一句话概括
论文用多攻击者 Bayesian Stackelberg 博弈、攻击路径分析和动态信念更新，自适应部署有限蜜罐资源。

## 问题与动机
多个攻击者具有不同目标偏好、利用能力和成本，网络规模扩大后蜜罐配置组合复杂度迅速增长。静态或单攻击者模型难以利用 IDS 观测调整防御。

## 方法
防守者作为领导者、多个攻击者作为跟随者，按网络距离分层，对各层子博弈使用混合整数规划，再通过逆向归纳形成策略。每轮根据观测到的攻击行动更新攻击者类型信念并重新分配蜜罐。

## 实验与结果
方法在几轮内阻止攻击成功，并可扩展到 500 个节点和 1500 多条边，同时保持近秒级总运行时间；表现优于 greedy 与 random 部署。

## 贡献与局限
贡献是统一建模多攻击者异质性和在线防御适应。局限是尚未覆盖协同攻击、零日利用、部分可观测和异质安全措施。

---
DOI: 10.1016/j.cose.2026.104949
