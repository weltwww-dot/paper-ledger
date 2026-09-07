# How security-related stress and self-efficacy influence actual behavior: An empirical study 总结

## 基本信息

- **标题**: How security-related stress and self-efficacy influence actual behavior: An empirical study
- **作者**: Seth Hastings, Tyler Moore, Bradley Brummel, Sal Aurigemma
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104948
- **arXiv**: 无
- **PDF**: [COSE_2026_SecurityStressEfficacyBehavior.pdf](papers/COSE_2026_SecurityStressEfficacyBehavior.pdf)

## 一句话概括

本文将安全相关压力与自我效能问卷同真实的多因素认证日志结合，实证发现压力显著增加认证失败后的离开时间，且总体自我效能呈倒 U 型关系——中等水平表现最优、过高疑似过度自信。

## 问题与动机

多因素认证（MFA）已成为组织网络防御的基石，但其真实效果取决于用户如何体验与执行安全任务；先前行为网络安全研究大多用问卷收集"行为意图"而非真实行为，而意图与实际行为之间存在明显脱节。学界（如 Warkentin 等）把直接测量真实安全行为称为行为网络安全的"圣杯"，但现实中此类数据难以获取。作者因此提出一个实证驱动思路：把关于自我效能与压力的问卷回答，与描述真实 MFA 表现的观测日志数据结合起来，检验心理前因对真实认证行为的影响。

## 方法

问卷调查于 2020 年 10 月至 2021 年 1 月在作者所在大学进行（167 人完成、162 人参与），测量三个构念：Security-Related Stress（SRS，含 Overload、Complexity、Uncertainty 三个子构念，1–7 Likert）、New General Self-Efficacy（NGSE，1–5 Likert）以及由 Computer Self-Efficacy 改编的 Security-Related Self-Efficacy（SRSE，面向 2FA 场景）。认证行为数据取自 2021 年 11 月至 2022 年 12 月共 13 个月的 Azure 登录日志，按 Hastings et al. (2024) 方法提取完整交互事件，过滤后得到 21,071 个 MFA 事件、109 名用户（平均每用户每月约 16 个事件）。性能指标包括成功率、成功排名、平均耗时、被锁定天数、失败后离开时间（Time Away）与摩擦率（Friction）。作者提出 21 条探索性假设，先后做单预测回归、加入控制变量（时间周期 Period、MFA 第二因素类型、事件数 NumEvents）的多预测回归（对数变换以作弹性解释），并把 NGSE/SRSE 分为低/中/高三档进行分类回归。

## 实验与结果

构念信度良好（Cronbach's α 0.78–0.92），除 Complexity（AVE=0.45）外各构念收敛效度达标，多重共线性可接受（最大 VIF=1.80）。简单回归仅支持 21 条假设中的 4 条：Overload 与成功率负相关（β=−0.06，p<0.01）、与成功率排名负相关、与 Time Away 正相关（β=0.80）；Uncertainty 与 Time Away 正相关（β=1.07，即不确定性提高 10% 对应失败后离开时间增加 10.7%）。反直觉的是 NGSE 与成功率显著负相关（β=−0.19，p<0.01）。多回归中 Overload 仍显著降低成功率（−0.07，p<0.001）并延长 Time Away（10% 超载≈7.6% 离开时间增加），Uncertainty 亦显著延长 Time Away（0.77，p<0.05），NGSE 对成功率维持负效应；SRSE 单独不显著。控制变量方面：与短信验证相比，OATH Code 用户成功率更低、耗时更短、被锁定天数更少但离开时间与摩擦更高；"记住设备"选项大幅降低耗时（−3.27）、锁定天数（−0.33）与摩擦（−0.92）。将 NGSE 分档后发现倒 U 型模式：低 NGSE 用户成功率比中档低 8%（−0.08，p<0.001）、摩擦高 80%，高 NGSE 用户成功率与中档相当但摩擦高 177%（1.02，p<0.001）且失败后离开时间更多；高 SRSE 用户成功率比中档高 5%（0.05，p<0.01）。整体成功率均值为 0.94，Friction 均值 0.07。

## 贡献与局限

主要贡献有三：一是提供了 21,071 个 MFA 事件、109 名企业用户的纵向真实行为数据集；二是将 SRS 与 NGSE/SRSE 双重效能构念结合，检验其对认证成功、错误与锁定率的影响；三是发现"倒 U 型"效能—表现模式，提示过度自信是安全认证行为研究中被忽视的因素，并示范了认证日志这一普适数据源的价值。局限包括：问卷与日志采集相隔约两年，特质可能漂移、无法捕捉状态性效应；样本以高校师生为主，Time Away、锁定天数等时间成本效应可能被高估；Complexity 收敛效度不足且全程无显著关系；属探索性研究，21 条假设仅 4 条获得支持，数据不可共享。未来可开展定向培训实验、多时点心理测量、扩大样本多样性并探索与企业合作获取日志。

---
DOI: 10.1016/j.cose.2026.104948
