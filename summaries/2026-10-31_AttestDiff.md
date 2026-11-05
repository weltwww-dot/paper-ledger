# Same publisher, changed authority: Release-bound semantic differencing of PyPI attestations 总结

## 基本信息
- **标题**: Same publisher, changed authority: Release-bound semantic differencing of PyPI attestations
- **作者**: Qingshui Xue、Pandong Xue、Zhimin Wang 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105209
- **发表**: 2026-10-31
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105209
- **PDF**: [COSE_2026_AttestDiff.pdf](papers/COSE_2026_AttestDiff.pdf)

## 一句话概括
比较同一发布者连续发行所绑定的工作流权限，识别软件包身份不变但发布权限发生变化的安全审查线索。

## 问题与动机
发布证明能够关联身份与提交，却不能保证发布工作流始终安全。只监控发布者变更或单次快照，会遗漏身份不变时触发器、令牌、运行器与依赖边界的变化。

## 方法
AttestDiff重建证明所指提交的准确工作流，抽取传递发布切片，再按有方向的语义规则比较权限扩张、限制和上下文缺失。保留新旧证据与未知情况，通过独立规则基线和外部审阅核对候选质量。

## 实验与结果
350个热门PyPI项目得到862个快照、720个同身份发行对，保留59对候选。两位外部审阅者最终认为33/59值得安全审查，21为良性维护，5缺公开上下文。另从290个有文本变更但未告警的发行对中随机抽59个，均判良性；未覆盖全部非告警或文本未变对，不能估计完整召回率（PDF第1、5—9页）。

## 贡献与局限
提供可追溯的纵向权限审查单元，降低原始变更带来的审查噪声。热门项目便利样本、公开GitHub工作流及有限历史限制代表性；审查价值不等于漏洞成立，未审阅全部非告警对也不能排除漏报。

---
DOI: 10.1016/j.cose.2026.105209 | PDF: [COSE_2026_AttestDiff.pdf](papers/COSE_2026_AttestDiff.pdf)
