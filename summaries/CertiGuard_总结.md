# CertiGuard 总结

## 基本信息

- **标题**: Certiguard: a fine-tuned LLM for mastering security certification exams
- **作者**: Chun-Ming Lai, Lien-Jung Chang, Chun-Chieh Chang, Yi-Chao Wu
- **期刊 / 会议**: International Journal of Information Security 2026
- **发表**: 2026-09-04
- **内容状态**: 完整
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01317-y
- **PDF**: [IJIS_2026_Certiguard.pdf](papers/IJIS_2026_Certiguard.pdf)
- **代码**: 未见公开代码链接

## 一句话概括

提出 CertiGuard，一个基于 LLaMA-2-7B 的资源高效网络安全认证考试训练框架，通过领域继续预训练、QLoRA 监督微调、结构化提示和 reasoning prompting，为 CISA、CRISC、CEH 与 CCNA 类问题提供答案和解释。

## 问题与动机

网络安全认证考试覆盖审计、风险控制、道德黑客和网络基础等不同领域，但传统备考材料往往分散、成本较高，对不同学习者的个性化反馈有限。通用 LLM 具备解释和多步推理能力，却需要领域知识适配与结构化引导，才能更可靠地处理认证考试中的情境判断和相近选项辨析。

## 方法

框架先在整理后的网络安全语料上对 LLaMA-2-7B 进行继续预训练，得到领域模型 Certibase，再用认证对齐的指令问答进行监督微调，并采用 4-bit NF4 量化的 QLoRA 降低显存和训练成本。部署上提供 beginner、intermediate、advanced 三个解释深度层级；评测比较多种结构化 prompt，以及 Chain-of-Thought、Logic CoT、System 2 Attention、Contrastive CoT 和 Self-consistency CoT 等推理策略。

## 实验与结果

实验使用四个认证领域的数据集：训练集共 3,194 个样本、验证集 158 个样本，测试集共 215 道题。Certibase 在无提示条件下平均准确率为 51.5%，最佳结构化提示提升至 64.1%；在推理策略比较中，CertiGuard 使用 Self-consistency CoT 的平均准确率最高，为 86.5%，其次为 Contrastive CoT 的 84.7% 和 Logic CoT 的 83.4%。论文同时报告了 95% Wilson 置信区间，并指出小规模测试集使这些提升应被视为探索性结果。

## 贡献与局限

- 贡献一：给出面向网络安全认证学习的两阶段、参数高效领域适配流程，并将认证领域覆盖映射到治理、风险、合规、网络安全和道德黑客等知识区域。
- 贡献二：系统比较结构化提示与多种 reasoning 策略，补充提示模板、数据来源限制、泄漏防范和不确定性分析。
- 局限：测试集仅覆盖每个认证约 52–56 道题，认证风格题目受版权和考试安全限制而无法完整公开；同时缺少统一的人类考生或商业工具基线，当前分级部署也还不是持续建模学习者的真正自适应系统。

---
DOI: 10.1007/s10207-026-01317-y
