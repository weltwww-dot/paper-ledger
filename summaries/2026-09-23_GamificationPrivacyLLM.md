# Insights on Mitigating Privacy Concerns in Gamification through LLM-Assisted Qualitative Analysis with Minimal Hallucination 总结

## 基本信息
- **标题**: Insights on Mitigating Privacy Concerns in Gamification through LLM-Assisted Qualitative Analysis with Minimal Hallucination
- **作者**: Aisvarya Adeseye、Jouni Isoaho、Mohammad Tahir
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **发表**: 2026-09-23
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3839358
- **PDF**: [TOPS_2026_GamificationPrivacyLLM.pdf](papers/TOPS_2026_GamificationPrivacyLLM.pdf)

## 一句话概括
本文研究本地大语言模型辅助分析游戏化工作场景的隐私访谈，并通过提示设计和采样控制降低幻觉、保护敏感数据。

## 问题与动机
游戏化员工系统涉及个人数据，质性访谈分析耗时且依赖研究者判断。云端模型带来敏感文本外传风险，本地模型则面临提示敏感、幻觉和分析一致性问题。

## 方法
研究使用 82 份访谈（33 名隐私专家、49 名非专家），比较本地 LLaMA、Gemma、Phi 模型与 NVivo 编码。作者设计聚焦 20 个关注点的提示优化，并测试抽样、温度、噪声和批次设置。

## 实验与结果
模型分析与专家 NVivo 编码总体较一致；非专家表述上的差异存在，但没有改变主要策略结果。研究归纳隐私主题并讨论组织实践。结果支持本地模型作为辅助工具，不证明其可以替代研究者。

## 贡献与局限
- 展示本地 LLM 用于敏感访谈分析的流程，并考察提示与生成参数影响。
- 将模型输出与不同经验群体分析结果进行对照。
- 样本和组织场景有限，研究属早期探索；其他数据、模型和编码团队仍需复现，输出应由研究者审查。

---
DOI: 10.1145/3839358
