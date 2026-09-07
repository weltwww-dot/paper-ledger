# Beyond Single-Pair Attacks: Disrupting Vision-Language Pre-Training Models With Dual-Semantic Frequency Stealth 总结

## 基本信息

- **标题**: Beyond Single-Pair Attacks: Disrupting Vision-Language Pre-Training Models With Dual-Semantic Frequency Stealth
- **作者**: Haiqi Zhang, Ziqiang Li, Hao Tang, Zechao Li
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01（电子版发布 2026-07-14，录用 2026-07-11，刊于 Vol. 23, No. 5, 2026 年 9–10 月期）
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3713210
- **arXiv**: 无
- **PDF**: [TDSC_2026_DualSemanticFrequencyStealth.pdf](papers/TDSC_2026_DualSemanticFrequencyStealth.pdf)

## 一句话概括

提出 DSFG-Attack：以"双语义引导（排斥对抗文本＋吸引非相似图像锚点）＋频域约束（限制低频扰动）"两阶段生成隐蔽且可迁移的多模态对抗样本，显著提升黑盒攻击成功率，并能跨任务、跨模型迁移到 GPT-4o 与 Qwen 2 等大模型。

## 问题与动机

Vision-Language Pre-training（VLP）模型（融合型如 ALBEF/TCL，对齐型如 CLIP）在图文检索等任务上表现优异，但与单模态模型一样对对抗扰动高度脆弱，构成实际安全威胁。现有方法（Co-Attack、SGA、DRA 等）大多只在孤立的单图像—文本对上最大化语义分歧，扰动易过拟合源模型，跨模型黑盒迁移性差；同时大多忽视对抗样本的隐蔽性（stealth），生成的可检测扰动在真实场景中一触即穿。作者提出需同时解决两个核心挑战：如何在未知目标模型上保持可泛化的语义错位（可迁移性），以及如何在扰动时保持视觉与文本的感知自然度（隐蔽性）。

## 方法

本文提出 Dual-Semantic Frequency-Guided Transferable Attack（DSFG-Attack），分两阶段进行：(1) 图像引导文本攻击（Image-Guided Text Attack）：对每条 caption 逐 token 掩码并计算与固定图像嵌入的跨模态重要性，选出最关键的词；在 GloVe 词嵌入空间中按余弦相似度阈值 γ=0.7 生成语义相近的候选集合，替换为最小化与配对图像相似度的候选词（扰动预算 εt=1，即仅改一个词），保持语法与语义通顺；(2) 文本引导图像攻击（Text-Guided Image Attack）：先在 mini-batch 内选出与原图像余弦相似度最低的非相似图像作为语义锚点 ins，然后联合优化双语义目标 Lsem=[λDT−(1−λ)AI]+（DT 为对抗文本—图像散度使二者相互排斥，AI 为图像—锚点吸引度），并用二维离散小波变换（DWT）把图像分解为低频近似与三个高频细节子带，惩罚对抗图像与原始图像低频重建差的 L1 范数 Lfreq=‖īm−ī′m‖₁，把扰动约束在人类视觉不敏感的高频纹理区；最终以 L=Lsem+βLfreq 联合优化，默认 λ=0.9、β=1.2、batch M=8、Adam 学习率 0.001、迭代 100 次。方法还依据"跨模型语义关系保持"的几何性质（非相似点对间距跨模型有界保持），论证以非相似锚点引导可使错位在目标模型上仍成立。

## 实验与结果

实验在 Flickr30K（31,783 个图文对，每图 5 条 caption；抽取 1,000 对）与 MSCOCO（123,287 对；抽取 5,000 对）上进行，以图文检索 R@1 的攻击成功率（ASR）为指标，源/目标模型覆盖融合型（ALBEF、TCL，ViT-B/16 图像编码器）与对齐型（CLIPViT、CLIPCNN，ResNet-101）。主要结果：摘要报告的典型黑盒设置（源 TCL→目标 CLIPViT，Flickr30K）ASR 平均提升 5.08%；白盒方面攻击 ALBEF 时 TR 平均 +2.59%、IR 平均 +2.43%；跨类型迁移 ALBEF→CLIPViT 比 DRA 平均高 3.42%、TCL→CLIPCNN 平均高 6.31%，同类型 TCL→ALBEF 平均高 2.2%；按架构看 ViT→CNN 迁移强于反向：CLIPViT→CLIPCNN 达 TR 50.88%、IR 58.33%，而 CLIPCNN→CLIPViT 仅 40.40%、52.20%。隐蔽性四指标（ℓ2、SSIM、CIEDE2000、低频 LF 失真，对照 SGA 在 2/255、8/255、16/255 像素预算下）：λ=0.9 时 ℓ2 范数比强基线低 4.32、CIEDE2000 低 125.98、SSIM 保持 0.99、LF 失真显著更低；λ=0.1 时 ℓ2 仅 0.01（对照像素法 16/255 预算为 779.19）。跨任务：以 ALBEF 在 MSCOCO 上生成对抗图像攻击做 captioning 的 BLIP（β=0.2），BLEU-4 下降 0.7%、CIDEr 下降 2.4%。跨模型：ALBEF 生成的对抗图像（β=0）成功使 GPT-4o 把三人场景误判为一人、把鳄鱼误认为恐龙，使 Qwen 2 把手持物误认为麦克风、把搏斗场景误判为普通互动。消融：λ 在 0.1–1.0 扫描选 0.9；β 在 {0,0.2,…,5.0} 扫描选 1.2；六种交互策略（t-i、i-t、i-t-i、t-i-t、t-i-t-i、t-i-t-i-t）中两阶段 t-i 以最低成本取得强迁移；频域约束相比像素级仅黑盒 ASR 略降而隐蔽性大幅提升；双语义引导较单对引导进一步降低匹配分数（示例对 0.1623→0.1502）；非相似锚点优于随机目标（TR 44.44% vs 44.03%，IR 53.96% vs 53.90%，ALBEF→CLIPCNN）。

## 贡献与局限

贡献：(1) 提出双语义引导攻击框架，利用非相似样本作为语义锚点制造"合理但错误"的语义漂移，缩小白盒与黑盒攻击成功率差距并提升迁移性；(2) 引入频域（DWT 低频惩罚）约束，将图像扰动限制在高频不可感知区，兼顾强攻击与高视觉保真度；(3) 提出嵌入空间的语义保持文本扰动（GloVe 近邻、单词替换），避免 BERT-Attack 等词级方法产生的标点错位、下划线、重复等可检测伪影；(4) 以多指标（ASR 与 ℓ2/SSIM/CIEDE2000/LF）在多 VLP 模型、跨任务（检索→captioning）与跨模型（VLP→MLLM）场景验证，暴露了可传播至 GPT-4o、Qwen 2 的真实可迁移风险。局限与未来方向：(1) 跨任务迁移性仍有限，面向检索优化的扰动迁移到 visual grounding 等其他任务时效果下降，作者归因于检索特定损失导致的任务过拟合，以及不同任务模型依赖的特征对频域扰动敏感度不一致；(2) 作为 VLP 频域扰动领域的开创性工作，缺少直接可比的频域基线，只能与像素级方法对照（本文扰动强度显著更低）；(3) 未来需探索任务无关、可泛化到多样多模态系统的对抗扰动公式。

---
DOI: 10.1109/tdsc.2026.3713210
