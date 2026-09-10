## 基本信息

- **标题**：ShadowCode: Toward (Automatic) External Prompt Injection Attack Against Code LLMs
- **研究方向**：代码大语言模型安全、外部 prompt injection
- **作者**：Yuchen Yang、Yiming Li、Hongwei Yao、Bingrun Yang、Yiling He、Tianwei Zhang、Dacheng Tao、Zhan Qin
- **期刊 / 年份**：IEEE Transactions on Dependable and Secure Computing，2026
- **DOI**:10.1109/TDSC.2026.3703498
- **PDF**：[TDSC_2026_ShadowCodeAutomaticExternalPrompt.pdf](papers/TDSC_2026_ShadowCodeAutomaticExternalPrompt.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 ShadowCode：仅把短小、非功能性的诱导扰动植入代码上下文，就能在代码补全过程中自动诱导 Code LLM 生成攻击者指定的恶意代码。

## 问题与动机

既有 backdoor 攻击通常需要干预训练数据或模型参数，adversarial attack 又难以实现精确的恶意目标；传统间接 prompt injection 则多依赖人工编写长指令、固定插入位置和较大的 token 预算。现实中，攻击者可能通过复制代码、安装依赖包或污染 RAG 知识库影响用户的代码上下文，而非功能性扰动还可能绕过静态分析和 sandboxing。

## 方法

ShadowCode 将删除、添加或修改类恶意目标表示为“位置代码—目标代码”输出 tuple，并用必要条件代码、无关 noise code、位置代码和目标代码模拟受害者上下文。它以目标代码的自回归生成概率构造损失，用 greedy gradient search 和 beam search逐 token 优化扰动；forward reasoning enhancement 提高目标前几个 token 的权重，keyword-based perturbation design 从 tuple 中选择少量关键词以降低最终长度。生成的扰动可经依赖、直接复制或 RAG 进入上下文。

## 实验与结果

实验覆盖三种语言（Python、Java、C/C++）、13 个恶意目标（含三个直接目标和 Top-10 CWE Known Exploited Vulnerabilities），形成 31 个 threat cases；HumanEval、HumanEval-X、CodeXGLUE、MBPP 和 Eval-Plus 共七个子数据集，超过 14,000 个样本。ShadowCode 在 CodeGemma-2b、CodeGemma-7b 和 CodeGeeX2-6b 上平均 ASR 超过 80%，最高平均值为 86.6%；在商业应用中，CodeGeeX 和 GitHub Copilot 的 ASR 分别最高为 93.3% 和 90.4%。默认使用 10 个扰动 token 加 2 个关键词，论文还报告语义分析难以区分注入代码，并在删除 50% 字符后仍保持较高 ASR。

## 贡献与局限

贡献包括：定义面向 Code LLM 的 external prompt injection 攻击范式；提出能在不可控上下文中自动生成短扰动的 ShadowCode；在开源模型和商业集成应用上系统验证有效性、灵活性、隐蔽性与迁移性。局限是仍不能完全绕过人工代码审查，代码来源审计、sandboxing 和限制 LLM 权限可能降低风险，且当前只研究 code completion，代码摘要和翻译场景留待后续工作。
