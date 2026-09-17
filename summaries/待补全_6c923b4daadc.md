# Towards distinguishing cybersecurity attacks and safety faults in distributed energy resources-rich smart grids: a systematic literature review 总结

## 基本信息

- **标题**: Towards distinguishing cybersecurity attacks and safety faults in distributed energy resources-rich smart grids: a systematic literature review
- **作者**: Fabien Sechi、Nadia Saad Noori、Charu Sharma 等
- **期刊 / 会议**: International Journal of Information Security 2026
- **发表**: 2026-09-16
- **内容状态**: 完整 · 已依据出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01308-z
- **arXiv**: 无
- **PDF**: [INTE_2026_DistinguishingCybersecurityAttacksSafety.pdf](papers/INTE_2026_DistinguishingCybersecurityAttacksSafety.pdf)

## 一句话概括

论文系统综述 DER 高渗透智能电网中区分网络攻击与安全故障的方法、数据和验证难点，强调两类事件可产生相似异常，因而需要可辨识的检测与分类流程。

## 问题与动机

分布式能源接入扩大攻击面并增加运行复杂性；恶意篡改、设备失效和自然扰动可能留下相近观测。若不能区分根因，处置可能把攻击误当故障，或错过真实安全事件。

## 方法

作者按数据来源、检测与分类方法、应用场景和评估实践梳理文献，覆盖传感器、智能电表、网络流量、相量测量与天气数据，并比较监督、无监督和深度学习方法的适用条件。

## 实验与结果

综述纳入的 25 项主要研究中，只有 6 项在同一评估设置下显式尝试区分网络攻击和物理安全故障。作者指出数据真实性、标签质量、可解释性、可扩展性和泛化仍是关键缺口，真实 DER 测试床对验证尤为重要。

## 贡献与局限

工作把攻击—故障根因区分明确为 DER 智能电网的独立研究问题，并归纳数据、模型和验证层面的缺口。作为 SLR，它不直接部署新检测器，结论也受纳入研究质量和异构测试环境限制。

---
DOI: 10.1007/s10207-026-01308-z
