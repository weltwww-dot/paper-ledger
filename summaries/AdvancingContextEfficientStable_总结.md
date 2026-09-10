# Advancing In-Context Learning for Efficient and Stable Medical Report Generation 总结

## 基本信息

- **标题**: Advancing In-Context Learning for Efficient and Stable Medical Report Generation
- **作者**: Mingjie Li, Rui Liu, Zeyi Shi, Mingfei Han, Lina Yao, Zhihui Li, Xiaojun Chang, Kilian M. Pohl, Md Tauhidul Islam, Lei Xing
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026-05-04
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3689780
- **arXiv**: 无
- **PDF**: [TPAMI_2026_AdvancingContextEfficientStable.pdf](papers/TPAMI_2026_AdvancingContextEfficientStable.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出 Principal In-Context Vectors（PCVs），从少量多模态医疗示例的扰动变化中提取稳定语义方向，并在不更新模型参数的情况下引导视觉语言模型生成更准确、更稳定的医疗报告。

## 问题与动机

医疗报告生成需要配对图像—文本数据，但临床数据受隐私、标注成本和机构差异限制。标准 in-context learning 依赖很长的示例提示，计算代价高，并可能产生不一致、幻觉或临床不准确的描述。论文希望在无需针对新中心或疾病重新训练的前提下，稳定视觉—语言表示并提升临床事实性。

## 方法

作者以 MedCLIP-ViT、Q-Former 和冻结的 LLaMA-2-7B-chat 构建 R2VLM，仅训练视觉提示生成器。对图像—报告示例及随机 masking 扰动提取各层最后报告 token 的 multimodal context vectors（MCVs），再对扰动诱导的隐变量位移做 PCA，取第一主成分作为 PCV；全文报告该方向在各层保留超过 93% 的扰动能量。推理时将各层 PCV 加到查询的所有 token 位置并做范数归一化，默认调制系数 β=5，从而保留原查询上下文而抑制不稳定方向。

## 实验与结果

实验覆盖 IU-Xray、MIMIC-CXR、CheXpert Plus、PEIR Gross 和 Longitudinal-MIMIC，使用 BLEU、CIDEr、ROUGE-L、METEOR 及 CheXpert 的 F1/Precision/Recall。IU-Xray 上 R2VLM 的 CIDEr 从 0.427 提升到 0.449；跨中心零样本中，R2VLM+PCVs 的 CIDEr 在 IU→MIMIC 由 0.142 升至 0.157、反向由 0.280 升至 0.288，F1 可由 0.208 升至 0.258。纵向任务中 F1 达到 0.372、METEOR 由 0.216 升至 0.235；100 个病例的盲评中，放射科医生偏好 PCV 报告的比例为 52.3%，Fleiss κ=0.73。

## 贡献与局限

PCV 将扰动不变性、低秩语义提取和 latent steering 结合成可插拔、training-free 的医疗 VLM 适配机制；平衡类别的 56 个示例通常已足够，且在 182M 到 27B 参数模型上仍能提供额外收益。现有跨模态实验只涉及 X-ray 与宏观病理照片，尚未证明对 CT/MRI 或非英语报告的泛化；受算力限制，也未完成 27B 模型的全监督微调，因此与大模型任务特定微调的性能差距仍未确定。

---
DOI: 10.1109/tpami.2026.3689780
