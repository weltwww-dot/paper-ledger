# PriRAG: Privacy-Preserving Inference for Retrieval-Augmented Large Language Models 总结

## 基本信息

- **标题**: PriRAG: Privacy-Preserving Inference for Retrieval-Augmented Large Language Models
- **作者**: Huili Wang, Yuanhong Huang, Wenjie Zheng, Pingyi Fan, Guoshun Nan, Shangguang Wang, Mengwei Xu, Tao Qi
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026年5月29日
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3698487
- **arXiv**: 无
- **PDF**: [TDSC_2026_PriRAGPrivacyPreservingInference.pdf](papers/TDSC_2026_PriRAGPrivacyPreservingInference.pdf)

## 一句话概括

PriRAG 将 RAG 检索到的原始知识压缩为面向查询、经过差分隐私保护的代理表示，在减少云端隐私暴露的同时保持 LLM 的生成质量。

## 问题与动机

云端 RAG 通常把用户或第三方知识库中的检索原文直接交给云端 LLM，可能泄露敏感信息和受保护的知识产权。已有改写或脱敏方案仍会传输部分文本，差分隐私方法又可能显著损害生成效果。因此论文希望在知识效用、隐私保护和云端部署效率之间取得可验证的平衡。

## 方法

PriRAG 使用知识编码器把检索内容映射到与目标 LLM 语义空间对齐的代理知识表示。它将内容切分为细粒度块，以查询为条件计算注意力权重，只聚合与当前问题相关的表示，并通过生成损失、教师 RAG 的知识蒸馏损失和混合训练优化编码器。部署时对块表示进行范数裁剪并加入高斯噪声，再由客户端完成检索和代理表示构造，云端仅接收查询与隐私代理表示；论文据此给出局部差分隐私保证。

## 实验与结果

论文在 7 个公开基准和 4 个 LLM 上评估 PriRAG，并与无 RAG、传统 RAG、LDP-RAG、SAGE 和 Sanitization 等方法比较。相对无 RAG，效用最高提升 21.11；在隐私预算 ε=1 时仍保持较高生成质量，而 LDP-RAG 在 ε=80 时就出现更明显的性能下降。代理表示使在线延迟接近无 RAG，知识编码器仅需微调约 20–50 MB 参数；以 Qwen2.5-32B 为后端时，两张 NVIDIA A800 上离线训练约需 33 小时。反演攻击实验中，PriRAG 恢复出的原始明文显著少于基线。

## 贡献与局限

论文贡献在于提出语义对齐的代理知识构造、查询中心表示学习和差分隐私协同推理的统一框架，并通过消融实验说明查询过滤、编码器微调和 DP 噪声各自的作用。局限是压缩在多跳推理或高冗余任务上可能产生波动，隐私—效用取舍仍依赖噪声和表示设计；实验主要覆盖论文选定的公开基准与模型，真实私有知识分布下的长期部署风险仍需继续验证。

---
DOI: 10.1109/tdsc.2026.3698487
