# PrivAnalogy: An Analogy Mechanism-Based Privacy Protection Framework for LLM Prompts 总结

## 基本信息

- **标题**: PrivAnalogy: An Analogy Mechanism-Based Privacy Protection Framework for LLM Prompts
- **作者**: Yixuan Song, Chundong Wang, Xumeng Wang, Yongxin Zhao, Zheli Liu, Qingbo Hao, Hao Lin, Yuhan Tian
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-22
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 隐私保护与大模型安全
- **DOI**: 10.1109/TDSC.2026.3715975
- **arXiv**: 无
- **PDF**: [TDSC_2026_PrivAnalogyLLMPromptPrivacy.pdf](papers/TDSC_2026_PrivAnalogyLLMPromptPrivacy.pdf)

## 一句话概括

PrivAnalogy 在客户端用类比表达替换提示中的敏感信息，再把模型回复映射回原始语境，在阻断云端直接接触隐私的同时保持用户所需的回答质量。

## 问题与动机

用户发送给云端 LLM 的提示可能包含姓名、地址、医疗或工作信息，直接上传会带来隐私泄露和提示反演风险；但粗暴删除或随机扰动又可能破坏问题语义和模型效用。由于 LLM 对输入细微变化很敏感，论文希望在客户端完成语义层面的隐私变换，并使云端模型仍能理解用户真实意图。

## 方法

框架包含四个功能模块，其中类比选择和类比还原是核心。类比选择模块依据本地差分隐私原则，把敏感实体转换成语义相近但不直接暴露原值的表达，再将保护后的提示发送给云端模型；类比还原模块对模型生成回复与原始提示进行语义对齐，把必要的上下文恢复给用户，同时尽量不让云端看到原始敏感内容。整个过程在客户端完成隐私变换和恢复。

## 实验与结果

作者在三个数据集上比较 PrivAnalogy 与 InferDPT 配合 SANTEXT+、RANTEXT 和 CUSTEXT+ 的方案。平均提示反演攻击抵抗力分别达到对比方案的 1.79 倍、1.37 倍和 1.65 倍，同时保持稳定的回复质量。结果说明，类比机制比单纯文本替换更能兼顾敏感信息隐藏与上下文可理解性。

## 贡献与局限

论文提出了客户端类比选择—云端处理—客户端类比还原的提示隐私保护流程，把局部差分隐私与语义对齐结合起来，并提供开源实现。局限在于类比质量、实体识别和回复还原可能随领域、语言和提示复杂度变化，客户端仍需承担本地处理成本；面对强大的上下文推断、连续对话关联和多模态敏感信息时，隐私保证和效用仍需进一步验证。

---
DOI: 10.1109/TDSC.2026.3715975
