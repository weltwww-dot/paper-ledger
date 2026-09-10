# Contrastive Mixture Diffusion Models 总结

## 基本信息

- **标题**: Contrastive Mixture Diffusion Models
- **作者**: Jen-Tzung Chien；Chih-Chun Chen
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **研究方向**: 文本扩散生成、连续—离散建模
- **DOI**: 10.1109/tpami.2026.3687180
- **PDF**: [TPAMI_2026_ContrastiveMixtureDiffusionModels.pdf](papers/TPAMI_2026_ContrastiveMixtureDiffusionModels.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出 CMD，将连续词嵌入扩散与吸收式离散 mask 噪声统一为 Gaussian–Dirac 混合扩散，并用对比学习塑造“先易后难”的词生成顺序，从而提升非自回归文本生成的质量与采样效率。

## 问题与动机

连续扩散适合在嵌入空间平滑生成，但直接处理离散 mask token 时，训练与反向去噪的概率过程不匹配，已有方法还常将混合分布的 KL 对齐项过度简化。另一方面，文本生成若先生成高频、简单词，再补充低频、具体词，通常更有利于尽早形成句子结构，因此需要同时解决混合噪声的理论建模和 easy-first 生成偏好。

## 方法

CMD 把 mask 视为吸收状态，在每个扩散步以 Dirac 分量表示 mask、以 Gaussian 分量表示连续词嵌入，推导前向后验并用 Gaussian 混合的乘积/变分上下界近似 KL 对齐损失。嵌入层以 mask 为锚点加入 triplet loss：高频词被拉近、低频词被推远，形成由简单到复杂的嵌入结构；训练目标联合 triplet、KL 对齐和重构损失，采样时用 DPM-solver++ 等快速方法反向去噪。

## 实验与结果

模型采用 12 层、12 头、768 维的 BERT-base 编码器，约 9,100 万参数，在 QQP（约 400K 对问题）释义任务上与 D3PM、DiffuSeq、DiffuSeq-v2 等比较，并评估开放域对话、文本简化及 OpenWebText 困惑度。CMD 在 QQP 的 BLEU 和 ROUGE-L 上优于 DS-v2，较少采样步时 BERTScore 也更有优势，推理计算量与 DS/DS-v2 相近；在 GPT-2 small 的 OWT 验证集、10 步设置下，困惑度相对 DS-v2、MD4、MDLM 分别下降 24.7%、19.7% 和 15.8%，GPT-2 medium 的最低困惑度为 14.21。消融表明同时保留 KL 与 triplet loss 最有效，但长采样过程中的优势会减弱。

## 贡献与局限

论文贡献是给出连续—离散文本扩散的 Gaussian–Dirac 概率表述、可实现的混合 KL 对齐近似，以及由对比嵌入驱动的 easy-first 生成机制。局限是 KL 采用近似并通过误差阈值筛选训练项，triplet loss 还会增加训练开销；采样步数很大时，对比嵌入带来的优势衰减，长程生成可能需要重新 mask 等策略。作者提出未来可将 easy-first 扩展到情感、同理心等属性控制。

---
DOI: 10.1109/tpami.2026.3687180
