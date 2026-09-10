# Secure and verifiable coercion-resistant electronic exam 总结

## 基本信息

- **标题**: Secure and verifiable coercion-resistant electronic exam
- **作者**: Mohammadamin Rakeei, Rosario Giustolisi, Gabriele Lenzini, Dhekra Mahmoud, Jannik Dreier, Pascal Lafourcade
- **期刊 / 会议**: J. Cybersecurity 2026
- **发表**: 2026-01-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1093/cybsec/tyag022
- **arXiv**: 无
- **PDF**: [CYSEC_2026_Paper.pdf](papers/CYSEC_2026_Paper.pdf)

## 一句话概括

论文提出 Secure CREX（SCREX）电子考试协议，在攻击者获得所有秘密信息的强强制威胁下，通过安全分配、不可窃听信道和可验证机制保持考试的隐私、公平与抗强制性。

## 问题与动机

电子考试需要同时满足认证、保密、完整性、匿名性、正确性以及个体和普遍可验证性。已有 CREX 协议只考虑部分秘密泄露，且其分配子协议缺少形式化安全证明；在更强的强制模型下，攻击者可能通过公开通信识别不合作方并破坏匿名提交与单盲性。因此，论文重新刻画强制威胁并补足协议的可验证性。

## 方法

作者定义攻击者可获得受害者全部秘密（包括概率加密随机数）的强强制模型，并分析已有 CREX 的弱点。SCREX 包含注册、分配、测试、评分和通知五个阶段，利用安全指数混合网络生成伪名，并以不可窃听信道保护关键通信。新的分配协议用加密承诺和指定验证者零知识证明让考官只知道自己的试卷子集；评分阶段对问答矩阵进行安全置换，再由多个考官评分。协议性质以 applied π-calculus 和 ProVerif 形式化验证。

## 实验与结果

论文的评估是形式化分析而非数据集实验。ProVerif 证明 SCREX 的认证、评分和子集保密性质成立；在规定的诚实角色假设下，隐私、强制抵抗和个体可验证性均得到验证。分析还显示，原 CREX 在强强制模型下的 Anonymous Submission 与 Single-Blindness 会失效，而 SCREX 通过不可窃听信道恢复这些性质。普遍可验证性无法由 ProVerif 直接遍历所有考生，需要结合手工归纳证明推广。

## 贡献与局限

- 贡献一：提出“所有秘密泄露给攻击者”的更强电子考试强制定义。
- 贡献二：发现 CREX 在该模型下的攻击，并设计包含安全分配与可验证性的 SCREX。
- 贡献三：用 ProVerif 自动验证认证、保密、隐私、强制抵抗及可验证性。
- 局限：结论依赖考试机构与混合网络等角色在相应性质下保持诚实，普遍可验证性仍需手工归纳补充；论文主要给出形式化安全保证，未报告真实部署规模或可用性评估。

---
DOI: 10.1093/cybsec/tyag022
