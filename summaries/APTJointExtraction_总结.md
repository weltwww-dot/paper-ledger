# Joint entities and relations extraction method for complex scenarios of APT attack threat intelligence analysis 总结

## 基本信息

- **标题**: Joint entities and relations extraction method for complex scenarios of APT attack threat intelligence analysis
- **作者**: Rui Qi, Ga Xiang, Lu Sun, Zicheng Tan, Jun Cao, Qunsheng Yang, Mingyue Cheng
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104960
- **arXiv**: 无
- **PDF**: [COSE_2026_APTJointExtraction.pdf](papers/COSE_2026_APTJointExtraction.pdf)

## 一句话概括

本文针对复杂 APT 威胁情报场景提出本体（CAPTIO）、数据集（CAPTIER）与基于嵌套实体跨度的联合抽取模型（APT-OTJE）三位一体的解决方案，在 CAPTIER 与 HACKER 数据集上分别取得 7% 与 25.2% 的 F1 提升。

## 问题与动机

网络安全防御正从被动转向主动，需要对非结构化网络威胁情报（CTI）文本自动抽取实体与关系，转换为（主语、关系、宾语）结构化三元组以构建知识图谱，从而揭示 APT 攻击者与战术之间的隐藏关联。然而现有研究存在三个关键挑战：其一，现有本体难以充分表示复杂 APT 攻击场景，联合抽取任务常把三元组约束在固定类型模板中，过度简化真实场景；其二，公开可用的 APT 知识图谱数据集稀缺，缺少标准化基准妨碍公平评测；其三，APT 攻击路径在知识图谱中呈链式或发散结构，导致重叠三元组问题突出，尤其是涉及攻击模式（AP）实体的主语-宾语重叠（SOO）与嵌套实体重叠（NEO），而多数联合抽取模型对此处理能力有限。本文还观察到 APT 相关情报常含链式叙述，进一步加剧了重叠三元组的抽取难度。

## 方法

作者先形式化定义了四类重叠三元组：实体对重叠（EPO）、单实体重叠（SEO）、主语-宾语重叠（SOO）与嵌套实体重叠（NEO），并聚焦其中在 APT 场景最常见的 SEO、SOO、NEO 三类。针对本体不足，提出包含 13 个实体类型与 12 个关系类型的 APT 本体 CAPTIO，加入 Credentials、Observed Data、Configuration 等攻击阶段细节实体及方向性依赖关系语义，并支持与 STIX 标准双向映射。基于该本体人工标注约 1500 条来自高价值 ATT&CK 案例的情报实例，构建公开数据集 CAPTIER（7053 个实体、5907 条关系、388 种唯一三元组类型，选取 48 种高频类型验证）。核心贡献是 APT-OTJE 联合抽取模型，由语义嵌入层（采用领域预训练模型 SecureBERT Plus）、特征提取层（在 FPE 基础上提出跨任务门控 CTG，动态感知与过滤实体/关系任务的共享特征）、实体位置编码器（指数分桶相对位置编码 EPE）、实体跨度识别器（ESR）、三元组区域编码器（TRE，按 Before/After/Contain/Included/Overlap 五类实体对区域编码）与重叠三元组抽取器（OTE，多头 Biaffine 注意力）构成；训练阶段用真实实体指导关系模块以减少噪声，损失为 NER 与关系模块二元交叉熵之和。

## 实验与结果

实验在单块 NVIDIA V100 上以 PyTorch 实现（150 epoch、隐藏 512、batch 16、学习率 2e-5、阈值 0.5），CAPTIER 每 epoch 约 20 秒、全程约 1.7 小时，推理延迟约 4 ms/句。基线为 SpERT、FPE 与威胁情报领域的 SMIEN。在 CAPTIER 上，本文 NER F1 达 0.763（SpERT 0.730、FPE 0.713），关系三元组 F1 达 0.516（SpERT 0.432、FPE 0.407、SMIEN 0.442），总体 F1 较既有方法提升 7%；在清理后的 HACKER 数据集（3593 句、6071 条关系三元组、22 种关系类型）上仅比较关系模块，本文 F1 达 0.699（SMIEN 0.447、SpERT 0.423、FPE 0.383），提升 25.2%。面向三类重叠三元组，SEO 因数量更多较易识别（CAPTIER F1 0.251），SOO 模式多变多样识别最差（F1 0.098），NEO 受数据量限制（占数据集仅 6.4%）。为缓解 NEO 数据不足，采用边界扰动、同类实体替换、补充三元组三种上采样策略，分别使 NEO 的 F1 提升 +6.42%、+4.86%、+6.75%（其中补充高频三元组最有效）。消融实验显示 SecureBERT 使实体性能提升 4%、关系性能提升 4.9%，CTG 对实体模块改善更明显，EPE 与 TRE 均有效，多头 Biaffine 在 128 头（0.516）优于 1/64/256 头。案例分析对比 SpERT 与 FPE，APT-OTJE 在 SEO、SOO、NEO 场景中表现更稳健。

## 贡献与局限

- 贡献一：系统性定义 APT 领域四类重叠三元组（EPO/SEO/SOO/NEO）并聚焦三类核心问题，填补该领域系统性定义与实验研究的空白。
- 贡献二：提出面向复杂 APT 场景的 CAPTIO 本体（13 实体类型、12 关系类型），细化了攻击阶段细节与语义方向性关系，并支持 STIX 双向映射。
- 贡献三：构建并公开高质量标注数据集 CAPTIER（约 1500 实例、7053 实体、5907 关系），缓解 APT 知识图谱基准稀缺问题。
- 贡献四：提出基于嵌套实体跨度的 APT-OTJE 联合抽取模型（CTG 跨任务门控、分桶相对位置编码、区域编码与多头 Biaffine），在 CAPTIER 与 HACKER 上相对基线分别提升 7% 与 25.2% 的 F1。
- 局限：训练数据各三元组类型数量不均衡，呈 31 至 542 次出现的长尾分布，且不同评审专家标注存在标签不一致噪声；上采样增强会使模型不成比例偏向 SEO 并可能引入语义不一致的伪阳性风险，在类型分布不同的场景下不可靠；模型依赖 SecureBERT，主要适用于英文 CTI 文本，跨语言迁移仍待解决；尚缺乏 token 级可解释性（如注意力可视化）分析，未来将优先扩充数据集并针对重叠三元组特点增强模型鲁棒性。

---
DOI: 10.1016/j.cose.2026.104960
