# When Erasure Fails: Benchmarking Content Removal in Diffusion Models via Vocabulary Substitution Attack 总结

## 基本信息

- **标题**: When Erasure Fails: Benchmarking Content Removal in Diffusion Models via Vocabulary Substitution Attack
- **作者**: Na Ruan, Chaohao Fu, Tu Huang, Zhaoguo Mei
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3707740
- **arXiv**: 无
- **PDF**: [TDSC_2026_VocabularySubstitutionAttack.pdf](papers/TDSC_2026_VocabularySubstitutionAttack.pdf)

## 一句话概括

提出词表替换攻击（VSA）及其语义鲁棒扩展（SR-VSA），证明现有扩散模型遗忘（unlearning）方法只破坏了"敏感词—图像"的常见关联而非真正删除概念，攻击者仅篡改词嵌入即可使被遗忘的有害内容重新生成。

## 问题与动机

大规模文生图扩散模型（如 Stable Diffusion）易被恶意提示滥用，生成色情、暴力、侵权等内容；为此社区提出多种基于微调的扩散模型遗忘方法（如 ESD、UCE、MACE、SA 等），试图让模型"忘记"特定概念。然而现有研究只验证了表面遗忘效果，缺乏统一评测基准：由于模型泛化能力强，仅仅破坏模型与敏感词的关联会制造"已成功遗忘"的错觉。作者因此质疑：这些方法是否真的剥夺了模型生成不安全概念的能力，以及如何可靠地评测被遗忘后的扩散模型。

## 方法

作者观察发现，基于微调的遗忘方法都只是不同程度地破坏文本提示与输出图像之间的连接，而扩散模型的强泛化能力会"消化"这些扰动，形成假性遗忘。据此提出词表替换攻击（VSA）：不改动被遗忘算法微调过的模块（UNet、文本编码器、VAE），只修改与主模块无关的词嵌入层，在嵌入空间中搜索能重建"文本—有害图像"关联的替代表示，再将该嵌入替换进词表，使所有包含该攻击词的提示都重新生成被删内容；优化采用以原始 Stable Diffusion 为参照的对比蒸馏损失并结合 PGD 投影。进一步针对 BPE 分词导致的 Token 过特异性（如 "van gogh" 与 "vangogh" 的 token 完全不相交），提出语义鲁棒版本 SR-VSA，通过构造同义词集并联合优化全部相关 token，辅以语义一致性正则，将攻击从 token 级提升到概念级，并给出两条理论定理支撑。

## 实验与结果

在 Stable Diffusion v1.4 上评估 9 种最新遗忘模型（SLD-M、ESD-x/u、FMN、AC、SA、UCE、MACE、SalUn、DoCo），覆盖概念遗忘（色情、暴力、非法活动）、风格遗忘（Picasso、Monet 等艺术家）和物体遗忘（取自 Imagenette）三类任务，以对抗提示攻击 UnlearnDiffAtk（UDA）为基线，用外部分类器准确率衡量攻击成功率：NudeNet 检测色情、基于 WikiArt 微调的 129 类 ViT 识别风格、ImageNet 上的 ResNet-50 识别物体。结果显示 VSA 在全部任务上一致优于 UDA：VSA 保留原提示、仅隐蔽替换关键词嵌入，生成图像语义准确，而 UDA 提示常无意义；MACE 因封闭式交叉注意力精炼表现最好；SA 看似鲁棒实则依赖 Fisher 信息矩阵导致生成分布坍缩、正常图像质量下降，属破坏性防御。VSA 具可复用性（同一词嵌入对所有含该词的提示生效，逼近原始 SD 水平），约 20 个 epoch 即达稳定攻击效果，50 epoch 全部攻击在 20 分钟内完成。SR-VSA 分析显示主攻击词仅覆盖语义变体总 token 的 9%–20%（如 "van gogh" 仅覆盖 10 个 token 中的 2 个）；对 Picasso，同义词间 CLIP 风格相似度标准差从 0.0255 降至 0.0013（19.6 倍提升），24 个测试同义词中 22 个（91.7%）获得正向提升。

## 贡献与局限

贡献：系统剖析现有扩散模型遗忘方法并揭示其"看似有效遗忘"的固有脆弱性；提出 VSA，仅替换词表即可高效恢复不安全内容生成能力，相对传统对抗提示方法在效率、语义保持和可复用性上均有优势；以 VSA 全面评测最多 9 种遗忘模型，细致分析其成败关键。防御启示：遗忘不应被当作模块局部微调问题，未来防御需联合考虑 token 嵌入、上下文文本表示与 UNet 去噪行为，可对部署组件做哈希/签名级完整性校验，并将 VSA/SR-VSA 用作自适应压力测试。局限：VSA 依赖对词表的修改能力（主要对应玻璃箱/灰箱威胁场景），且单次词表修改对未列入同义词集的罕见拼写仍可能失效；SA 等防御的"虚假鲁棒"提示当前评测指标可能低估真实风险，论文未给出完整防御方案，仅提出设计要求。

---
DOI: 10.1109/tdsc.2026.3707740
