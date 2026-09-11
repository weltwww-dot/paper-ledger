# BadBone：视觉提示学习中针对骨干模型的后门攻击

## 基本信息

- 标题: BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning
- 作者: Ziqing Yang, Rui Wen, Xinlei He, Yun Shen, Michael Backes, Yang Zhang
- 期刊 / 会议: IEEE Transactions on Information Forensics and Security 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1109/TIFS.2026.3698596
- PDF: [TIFS_2026_BadBone.pdf](papers/TIFS_2026_BadBone.pdf)

- 标题: BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning
- 作者: Ziqing Yang, Rui Wen, Xinlei He, Yun Shen, Michael Backes, Yang Zhang
- 期刊 / 会议: IEEE Transactions on Information Forensics and Security 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

- **标题**：BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning
- **作者**：Ziqing Yang, Rui Wen, Xinlei He, Yun Shen, Michael Backes, Yang Zhang
- **期刊**：IEEE Transactions on Information Forensics and Security, Vol. 21, 2026
- **研究方向**：视觉提示学习、后门攻击、模型安全
## 一句话概括

BadBone 在预训练视觉骨干中注入可迁移后门，使下游用户进行 visual prompt learning 时自动继承攻击效果，而无需篡改目标任务的提示学习过程。

## 问题与动机

现有视觉提示学习后门研究多直接攻击提示或训练流程，但实际用户通常从外部获取预训练 backbone，再在自己的任务上学习 prompt。若骨干已经被污染，攻击可跨任务传播；而攻击者往往看不到目标数据。论文研究如何只用与目标分布相似的 shadow dataset，预先把后门植入 backbone 并在下游微调后保持有效。

## 方法

BadBone 采用双层优化：外层优化带触发器的骨干模型，内层模拟受害者在视觉提示学习中的微调，使后门在提示训练后仍能存活。框架支持 targeted 与 untargeted 攻击，在维持干净数据正常效用的同时，令触发样本在下游任务中产生指定或异常预测。该设计把攻击面从 prompt 学习过程上移到共享骨干。

## 实验与结果

作者在三个领域的数据和模型上测试攻击迁移，并与多种后门方法比较。在 CIFAR-10/ResNet50 的 targeted 设置中，报告的攻击成功率达到 98.66%，相对基线提升 86.22%。对 Neural Cleanse、ABS、MNTD、NAD、CLP、D-BR 六类模型级防御的评估显示，现有防御对这种 backbone 后门基本不足。

## 贡献与局限

论文首次系统展示视觉提示学习中骨干级后门的“传染”风险，并用双层优化实现无需访问目标任务的攻击。局限是攻击效果依赖 shadow dataset 与目标分布的相似性、触发器和微调配置；跨架构、跨模态提示及真实模型供应链中的检测与修复仍需专门防御。

---
DOI: 10.1109/TIFS.2026.3698596
