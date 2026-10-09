# Attack Tree Distance: A Practical Examination of Tree Similarity Measurement within Cybersecurity 总结

## 基本信息
- **标题**: Attack Tree Distance: A Practical Examination of Tree Similarity Measurement within Cybersecurity
- **作者**: Nathan Schiele、Olga Gadyatskaya
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **发表**: 2026-09-30
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3850236
- **PDF**: [TOPS_2026_AttackTreeDistance.pdf](papers/TOPS_2026_AttackTreeDistance.pdf)

## 一句话概括
论文研究如何比较不同人员绘制的攻击树，提出五种距离度量，并设计一套结合基本结构变换与人工树样本的理论和实验验证流程。语义相似度能帮助匹配措辞不同但含义接近的节点，不过各距离方法适用情形不同。

## 问题与动机
攻击树用于描述攻击目标及其子步骤，但现实模型常由不同专家、工具或生成方法构建，节点名称和树结构未必一致。传统语义等价判断只能区分两棵树是否相同，无法表达“相似但不完全相同”；这限制了攻击树库的去重、威胁模型整理，以及将自动生成树与人工参考树进行比较。

## 方法
作者先用 SBERT 句向量及余弦相似度比较节点标签，再构造 Label Distance（LD）、Tree Edit Distance（TED）、Radical Distance（RD）、Multiset Distance（MSD）和它们的加权组合 WSD。验证包含两部分：对节点增删、标签变更、子节点换序等基本变换检查度量行为；并由 39 名莱顿大学网络安全辅修本科生绘制同一情境的攻击树、扩展原树及自选情境树，使用样本比较结果与多维尺度图评估距离是否符合预期（第 14—15 页）。

## 实验与结果
作者认为，基于语义的标签比较比纯字符串距离更能保留含义：例如“door open”与“open door”的 SBERT 相似度为 0.992，而归一化 Levenshtein 相似度为 0（第 18 页）。结合理论变换和人工树数据，LD、TED、RD、WSD 在多数验证情形中表现可用，MSD 未通过相应有效性验证；没有一种方法在所有情形下都完美符合预期。论文强调这些结果支持特定条件下的相似树识别，而非证明距离值就是普适的真实威胁相似度。

## 贡献与局限
论文给出攻击树标签与结构的五种比较方案，并提出可复用的双路径验证方法，为攻击树库整理和评估 AI 生成模型提供研究起点。实验参与者是学生而非安全从业者，树样本与任务情境有限；语义阈值及组合权重也可能随数据集、专家措辞和模型变化。作者还指出，部分度量不满足距离度量的全部公理。因此，应用到真实专家模型前仍需针对目标语料校准，并以从业者样本继续检验。

---
DOI: 10.1145/3850236
