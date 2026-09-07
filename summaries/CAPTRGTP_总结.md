# CAPTR-GTP: Class-aware prompting and token refinement with graph token propagation for few-shot ViTs 总结

## 基本信息

- **标题**: CAPTR-GTP: Class-aware prompting and token refinement with graph token propagation for few-shot ViTs
- **作者**: Mohammed Al-Habib, Zuping Zhang, Abdulrahman Noman
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108934
- **arXiv**: 无
- **PDF**: [NN_2026_CAPTRGTP.pdf](papers/NN_2026_CAPTRGTP.pdf)

## 一句话概括

提出 CAPTR-GTP 少样本 ViT 分类框架，通过不确定性感知 token 精炼、类别感知提示与稀疏图 token 传播保留而非丢弃 token 信息，在四个域内与四个跨域基准上达到最先进或相当性能。

## 问题与动机

少样本学习中 Vision Transformer（ViT）面临持续障碍：密集自注意力会放大杂乱场景中的背景交互；仅依赖最终层 [CLS] token 或静态原型会遗漏细粒度线索；在标签稀缺时统一的 patch 池化忽略了 token 可靠性。此外，许多 ViT 适配器依赖 token 相似度匹配或合并策略，往往丢弃或过度压缩 token 造成信息丢失，且源域与目标域存在分布偏移时性能会急剧下降。作者认为应保留并传播 token 信息而不是丢弃它们，据此提出 CAPTR-GTP 框架。

## 方法

CAPTR-GTP 是两阶段的 ViT 元学习框架。第一阶段在 ImageNet-1k 上用掩码图像建模（MIM）预训练 ViT-Small 骨干（75% 随机掩码，1700 个 epoch）；第二阶段进行情节式元微调，仅解冻最后 Lb=2 个 Transformer 块。不确定性感知模块用 Monte Carlo dropout（T=10 次随机前向）估计逐 token 方差并结合自注意力影响力打分，通过 Variance-Consistent Sampling 门保留高置信 token、衰减或丢弃高方差不可靠 patch。Class-Aware Prompt Refinement（CAPR）把过滤后支持集的类别原型 μc 与离散度 σc 经两层 MLP 映射为可学习的类别提示 token，经 LayerNorm 与可学习缩放后前置到 token 序列作为类别锚点。随后双层注意力在 Metis 划分（每情节 20 个簇）内做簇内自注意力、跨簇注意力并回传全局上下文；最后稀疏 top-k（k=32）图 token 传播（GTP）在每情节固定邻居掩码下刷新边权，做特征传播与带重启的标签传播，其 logits 与原型 logits 融合预测。训练目标为交叉熵加类分离正则（L_meta = α·L_CE + β·L_sep）。

## 实验与结果

在 5-way 1-shot/5-shot 协议下评估四个域内基准与四个跨域基准。域内结果（1-shot/5-shot）：miniImageNet 达 74.50%±0.09 / 89.05%±0.28，tieredImageNet 达 77.50%±0.32 / 91.40%±0.27，CIFAR-FS 达 81.40%±0.60 / 92.50%±0.28，FC100 达 50.73%±0.55 / 66.75%±0.50，超越或媲美 CPEA、IISNet、SAFF、ASLM 等强基线（ViT-S，22M 参数）。跨域（miniImageNet→CropDiseases、EuroSAT、ISIC、ChestX，600 个 episode 的平均准确率±95% CI）分别达 79.87%±0.36 / 95.33%±0.23、71.18%±0.60 / 87.24%±0.44、37.23%±0.36 / 53.89%±0.81、24.14%±0.22 / 29.34%±0.32，其中 CropDiseases 相比 MF-ViT 基线提升 +9.69/+8.85 个百分点。逐步消融显示各模块贡献累积：冻结 ViT 61.20/73.80 → 加元微调 68.35/82.42 → 加双层注意力 69.90/85.10 → 加 GTP 70.20/86.10 → 加不确定性加权 70.36/86.50 → 加 CAPR 达 74.50/89.05（CAPR 贡献最大，+4.14/+2.55 个百分点）；MIM 预训练优于 DINO、监督预训练与随机初始化，T=10、方差阈值 τ=0.35、微调 2 块最优。计算开销为 4.3 GMac、峰值显存 6.9 GB、每 episode 61.0/99.5 ms（1/5-shot），低于多数比较方法。

## 贡献与局限

贡献：首次将不确定性感知 token 加权、类别感知提示精炼与双层图注意力统一到单一少样本 ViT 流水线；以 MIM 预训练骨干加有限微调并配合稀疏固定邻居图传播，保留稀有线索、缓解过平滑与背景噪声；在四个域内与四个跨域基准上全面验证并给出充分的模块级消融与可视化分析。局限：MC dropout 不确定性估计需多次随机前向，推理延迟高于单次前向编码器，不利于严格实时部署；token 图构建采用 episode 内固定划分并依赖剪枝阈值、簇数等超参数，跨数据集可能需要调参；MC dropout 主要刻画认知不确定性，未显式建模偶然（aleatoric）噪声；在强上下文干扰下仍有注意力被干扰物吸引的失败案例。

---
DOI: 10.1016/j.neunet.2026.108934
