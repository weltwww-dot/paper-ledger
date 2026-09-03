# Robust backdoor attacks against fine-tuning-based transfer learning 总结

## 基本信息

- **标题**: Robust backdoor attacks against fine-tuning-based transfer learning via self-attention distillation
- **研究方向**: 信息安全
- **作者**: Ziyang Zhuo, Yilun Lyu, Xu Ma, Yuan Ma, Hongwei Zhou, Jiankang Wei
- **期刊 / 会议**: JCS 2026
- **发表**: 2026-08-10
- **DOI**: 10.1177/0926227x261476666

## 一句话概括

提出 RBA-SAD：一种通过自注意力蒸馏实现的鲁棒后门攻击，能在微调式迁移学习中存活，并以不可感知噪声作为触发器规避输入净化类防御。

## 问题与动机

后门攻击在良性输入上表现正常、触发条件下输出攻击者指定结果，威胁模型完整性。但迁移学习（尤其微调）是主流训练范式，微调过程往往会清除后门，使已有攻击失效。

## 方法

通过分层、自顶向下的自注意力蒸馏（self-attention distillation）操纵模型对触发器的识别能力，使其经受微调冲击；用不可感知噪声作为触发器规避基于输入净化的防御；优化触发器生成实现多层特征碰撞，使中毒样本在各层的表征与干净样本相似。

## 实验与结果

在三个基准迁移学习任务上，RBA-SAD 攻击成功率超过 97%，并对七种 SOTA 后门防御保持隐蔽（数字来自原文摘要）；还泛化到 Vision Transformer、ImageNet 规模迁移与 LoRA 参数高效微调等场景。

## 贡献与局限

- 贡献一：首次针对微调式迁移学习提出自注意力蒸馏型鲁棒后门攻击。
- 贡献二：多层特征碰撞的触发器优化同时对抗微调与输入净化防御，跨架构与高效微调可泛化。
- 局限：评测集中于图像分类迁移任务，其他模态与防御场景待扩展。

---

DOI: 10.1177/0926227x261476666
