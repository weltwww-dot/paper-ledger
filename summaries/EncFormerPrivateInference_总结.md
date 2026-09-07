# EncFormer: Secure and Efficient Transformer Inference Over Encrypted Data 总结

## 基本信息

- **标题**: EncFormer: Secure and Efficient Transformer Inference Over Encrypted Data
- **作者**: Yufan Zhu, Chao Jin, Khin Mi Mi Aung, Xiaokui Xiao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-17
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 隐私计算与安全机器学习
- **DOI**: 10.1109/TDSC.2026.3714715
- **arXiv**: 无
- **PDF**: [TDSC_2026_EncFormerPrivateInference.pdf](papers/TDSC_2026_EncFormerPrivateInference.pdf)

## 一句话概括

EncFormer 通过阶段兼容布局、低通信 CKKS—MPC 转换和边界成本决策，降低加密 Transformer 推理中的重排、通信和非线性计算开销。

## 问题与动机

机器学习即服务会让不可信服务提供方接触用户输入和模型输出，医疗、法律和金融文本尤其需要隐私保护。现有 FHE—MPC 混合方案受限于低效同态核、通信密集的 MPC 非线性协议以及昂贵的两种密码计算转换；若只选择 FHE 或 MPC，也难以同时满足 Transformer 的线性层、布局和非线性需求。

## 方法

EncFormer 将 Transformer 推理视为 FHE、MPC、张量布局和转换边界的联合设计问题。作者提出阶段兼容模式，使相邻 FHE 内核能够复用布局并减少重排；设计安全的复数 CKKS—MPC 转换，压缩边界数据；再以成本模型和 PhantomFHE 决策规则选择 FHE—MPC 分界。针对非线性函数，论文还设计通信高效的 MPC 协议，并进行 GPU 优化。

## 实验与结果

作者在 GPT-2、BERT 和 BERT-large 风格模型上评估。相较 BOLT，EncFormer 的推理通信和端到端延迟平均分别降低约 30.4 倍和 9.9 倍；相较 BumbleBee，分别降低 2.6 倍和 2.1 倍；相较 BLB，分别降低 1.4 倍和 1.3 倍。与匹配后端的纯 FHE 流水线相比，BERT-base 端到端延迟降低 1.9–3.5 倍，并在选定 GLUE 任务上保持接近明文推理的准确率。

## 贡献与局限

论文把加密布局、FHE—MPC 转换和非线性执行统一为可优化的协同设计，显著减少了私有 Transformer 推理成本。局限是安全模型主要覆盖半诚实两方，不覆盖恶意对手、侧信道和流量无关调度；部分非线性仍依赖任务特定蒸馏，实验结果受 A100 后端和网络配置影响，不能直接推断到任意硬件、任务或长上下文自回归模型。

---
DOI: 10.1109/TDSC.2026.3714715
