# DNN Obfuscation With Contrastive Learning for Efficient Defense Against Side-Channel Attacks 总结

## 基本信息

- **标题**: DNN Obfuscation With Contrastive Learning for Efficient Defense Against Side-Channel Attacks
- **作者**: Yidan Sun, Guiyuan Jiang, Jiayang Liu, Qian Sun, Peilan He, Siew-Kei Lam
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3697449
- **arXiv**: 无
- **PDF**: [TDSC_2026_DNNObfuscationContrastiveEfficient.pdf](papers/TDSC_2026_DNNObfuscationContrastiveEfficient.pdf)

## 一句话概括

CLOb-DNN 利用对比学习和孪生/三元组网络，在架构级与调度级共同混淆 DNN 执行轨迹，减少反复真实硬件部署，同时满足延迟约束并抵抗多种侧信道模型窃取攻击。

## 问题与动机

DNN 知识产权可能通过功耗、时序或其他侧信道被攻击者恢复，单纯的软件加密并不能阻止执行过程中暴露的层序列和调度信息。已有 DNN 混淆方法往往需要大规模硬件修改或在目标平台上重复部署评估，优化时间长、跨架构适应性差，有的只混淆架构或只混淆调度，也难以保证预定延迟。作者希望在不大幅修改后端代码的情况下，学习出稳定、可迁移且满足延迟预算的混淆配置。

## 方法

CLOb-DNN 通过对比学习构造正负混淆样本，用 triplet network 学习攻击难度、执行延迟和混淆质量之间的关系，从而减少每次候选配置都在真实设备上部署的次数。框架同时覆盖架构级混淆和调度级混淆：前者改变可观测的层结构/顺序，后者改变执行调度与时序特征；优化时显式加入延迟约束，使生成的混淆 DNN 在防护能力和运行代价之间平衡。该设计尽量避免昂贵的后端源代码修改，并针对不同状态恢复和侧信道攻击模型进行训练与评估。

## 实验与结果

作者使用多种先进侧信道攻击模型评估 DNN IP 保护效果，并在不同延迟要求下比较已有混淆方法。CLOb-DNN 将混淆时间降低约 90%，同时保持更强的攻击抵抗能力；生成的混淆网络能满足多种延迟约束，在架构和调度两类混淆同时启用时稳定性优于只覆盖单一层面的方案。实验还显示，即使考虑 TVM 等后端优化，当前先进侧信道模型对混淆层序列的恢复仍会出现超过 50% 的预测错误，说明混淆对序列窃取具有实际阻碍作用。

## 贡献与局限

贡献在于把对比学习用于减少真实硬件部署成本，并统一架构级和调度级混淆，兼顾防护强度与延迟限制。局限是混淆策略仍依赖目标硬件、编译后端和攻击模型，新的侧信道、翻译模型或对混淆配置的先验可能改变防护效果；更紧的延迟预算会压缩可用混淆空间。未来还需要扩大到更多 DNN 架构、统一建模两类混淆以及评估额外攻击向量。

---
DOI: 10.1109/tdsc.2026.3697449
