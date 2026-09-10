# Best current practices for privacy-preserving OpenID Connect: A study of their adoption in the wild 总结

## 基本信息

- **标题**: Best current practices for privacy-preserving OpenID Connect: A study of their adoption in the wild
- **作者**: Gianluca Sassetti, Amir Sharif, Giada Sciarretta, Roberto Carbone, Silvio Ranise
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104934
- **arXiv**: 无
- **PDF**: [COSE_2026_PrivacyPreservingOIDC.pdf](papers/COSE_2026_PrivacyPreservingOIDC.pdf)

## 一句话概括

本文从OIDC规范提炼隐私保护最佳实践，并审计现实世界中的10000个提供商配置，评估这些实践的采用情况。

## 问题与动机

OIDC广泛用于身份联邦，但生态缺少连贯的隐私最佳实践及大规模现实部署证据。若配置不当，身份提供商可能暴露过多个人数据，难以满足数据最小化、保密和不可关联等隐私原则。

## 方法

作者先依据OIDC官方规格和实践趋势提出结构化隐私BCP，再采用双重研究：2022年人工审查，2025年自动化合规分析。自动分析覆盖全球10000个提供商数据集，并比较私营与国家/公共部门提供商的隐私配置。

## 实验与结果

研究显示私营业务方案总体缺少增强隐私特征，与国家方案之间存在明显差距；后者平均提供更高的隐私基线。结果说明不改变协议、仅改善部署配置也有提升空间。

## 贡献与局限

贡献是给出可部署的OIDC隐私实践清单并进行大规模野外测量。局限是配置审计只能反映观测时点和可见设置，不能完全证明运行时行为或用户实际隐私风险。

---
DOI: 10.1016/j.cose.2026.104934
