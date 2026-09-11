# PrivAnalogy：基于类比机制的 LLM 提示隐私保护框架

## 基本信息

- 标题: PrivAnalogy: An Analogy Mechanism-Based Privacy Protection Framework for LLM Prompts
- 作者: Yixuan Song, Chundong Wang, Xumeng Wang, Yongxin Zhao, Zheli Liu, Qingbo Hao, Hao Lin, Yuhan Tian
- 期刊 / 会议: IEEE Transactions on Dependable and Secure Computing 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1109/TDSC.2026.3715975
- PDF: [TDSC_2026_PrivAnalogyLLMPromptPrivacy.pdf](papers/TDSC_2026_PrivAnalogyLLMPromptPrivacy.pdf)

- 标题: PrivAnalogy: An Analogy Mechanism-Based Privacy Protection Framework for LLM Prompts
- 作者: Yixuan Song, Chundong Wang, Xumeng Wang, Yongxin Zhao, Zheli Liu, Qingbo Hao, Hao Lin, Yuhan Tian
- 期刊 / 会议: IEEE Transactions on Dependable and Secure Computing 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

- **标题**：PrivAnalogy: An Analogy Mechanism-Based Privacy Protection Framework for LLM Prompts
- **作者**：Yixuan Song, Chundong Wang, Xumeng Wang, Yongxin Zhao, Zheli Liu, Qingbo Hao, Hao Lin, Yuhan Tian
- **期刊**：IEEE Transactions on Dependable and Secure Computing, Vol. 23, No. 5, September/October 2026
- **研究方向**：提示隐私、LLM 安全、客户端隐私保护
## 一句话概括

PrivAnalogy 在客户端用语义类比替换提示中的敏感信息，再把云端回答映射回原始语境，尽量阻断提示隐私泄露而保持 LLM 的回答效用。

## 问题与动机

提示可能包含姓名、地址、医疗或工作信息，直接发送给云端 LLM 会带来泄露和提示反演风险；删除或随机扰动又会破坏上下文，导致回答质量下降。论文希望把隐私变换放在客户端，并找到比简单文本替换更能保留语义和推理可用性的保护机制。

## 方法

框架由客户端的敏感信息识别/类比选择、云端 LLM 处理和客户端类比还原构成。类比选择依据本地差分隐私思想，把敏感实体转换成不直接暴露原值但保持语义关系的表达；云端只处理保护后的提示；类比还原模块再把回复对齐到用户原始语境。作者将类比机制与文本隐私变换、回复语义恢复结合，兼顾隐私和任务效用。

## 实验与结果

在三个数据集上，论文把 PrivAnalogy 与 InferDPT 配合 SANTEXT+、RANTEXT、CUSTEXT+ 的方案比较。平均提示反演攻击抵抗力分别达到对比方案的约 1.79、1.37 和 1.65 倍，同时维持稳定回复质量，表明类比表达相较直接替换更能保留上下文可理解性。

## 贡献与局限

论文提出客户端类比选择—云端处理—客户端还原的提示隐私流程，并将隐私随机化与语义对齐结合。局限是类比质量、实体识别和回复还原会受领域、语言及提示复杂度影响，连续对话关联、多模态敏感信息和强上下文推断下的隐私保证仍需验证。

---
DOI: 10.1109/TDSC.2026.3715975
