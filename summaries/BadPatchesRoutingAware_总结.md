# Badpatches: routing-aware backdoor attacks on vision mixture-of-experts 总结

## 基本信息

- **标题**: Badpatches: routing-aware backdoor attacks on vision mixture-of-experts
- **作者**: Jona te Lintelo、Cedric Chan、Stjepan Picek
- **期刊 / 会议**: International Journal of Information Security 2026 · 25:175
- **研究方向**: 信息安全
- **发表**: 2026-10-16
- **内容状态**: 完整
- **内容说明**: 已亲自阅读16页出版社正式版正文，并对照表2、表7图像核验攻击与防御结果
- **DOI**: 10.1007/s10207-026-01320-3
- **PDF**: [IJIS_2026_BadPatchesRoutingAware.pdf](papers/IJIS_2026_BadPatchesRoutingAware.pdf)

## 一句话概括

BadPatches通过调整已有后门触发器在图像块中的位置，使其更容易进入视觉混合专家模型的有效路由，揭示稀疏计算并不天然带来后门安全性。

## 问题与动机

视觉MoE会选择专家、丢弃部分图像块，传统触发器可能被切碎或直接忽略。作者研究攻击者能否利用这一处理机制，在较低数据投毒比例下植入后门，而不明显损害正常分类能力（PDF第2—4页）。

## 方法

比较在所有图像块中重复触发器的BadPatches-N与基于显著性选择前景块的BadPatches-S，后者只在选中的块内放置完整触发器。它是已有触发器的路由感知应用策略，并非全新触发器；威胁模型允许攻击者同时修改训练图像和标签，显著性计算不依赖读取模型内部路由状态（PDF第3—7页）。

## 实验与结果

在V-MoE、E3、ViMoE和pMoE上，分别使用ImageNet-1K、Imagenette、CIFAR-100及CelebA进行评估。表2中，V-MoE在0.05%投毒率、方块触发器设置下，BadPatches-S的攻击成功率为84.5%，传统放置方式为1.6%。表7中，BadPatches-S经30%剪枝及5轮微调后仍有31.4%的攻击成功率，说明该防御只能缓解，不能据此宣称后门已清除（PDF第6—9、12—13页）。

## 贡献与局限

贡献是识别稀疏路由对触发器完整性和可见性的影响，并用显著性引导策略验证这一攻击面。结果限于所测模型、数据集及可改标签的投毒场景，尚未验证干净标签攻击或语言MoE。正文部分概括与表格存在数字不一致，因此上述结果按具体实验行报告，不将低投毒率下的个别成功推广到全部模型和触发器（PDF第9、13—14页）。

---
DOI: 10.1007/s10207-026-01320-3 · PDF: [IJIS_2026_BadPatchesRoutingAware.pdf](papers/IJIS_2026_BadPatchesRoutingAware.pdf)
