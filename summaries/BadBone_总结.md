# BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning 总结

## 基本信息

- **标题**: BadBone: Backdoor Attacks Against Backbone Models in Visual Prompt Learning
- **研究方向**: 信息安全
- **作者**: Ziqing Yang, Rui Wen, Xinlei He, Yun Shen, Michael Backes, Yang Zhang
- **期刊 / 会议**: IEEE TIFS 2026
- **发表**: 2026-06-01
- **内容状态**: 完整
- **DOI**: 10.1109/TIFS.2026.3698596
- **arXiv**: 2605.31246
- **PDF**: [TIFS_2026_BadBone.pdf](papers/TIFS_2026_BadBone.pdf)
- **代码**: https://github.com/TrustAIRLab/BadBone

## 一句话概括

提出 BadBone，首个针对视觉提示学习中 backbone 模型的后门攻击：用双层优化把后门注入骨干模型，使下游采用 prompt learning 的任务继承漏洞，而提示学习过程本身不被篡改。

## 问题与动机

提示学习（prompt learning）因其简单有效而被广泛采用，但其安全性研究不足。现有后门攻击多针对提示学习过程本身；BadBone 转而攻击更底层的 backbone 模型——用户拿预训练骨干做视觉提示学习微调时，后门被「传染」到下游任务，攻击者只需一个与下游分布相似的 shadow dataset，无需访问目标任务。

## 方法

双层优化（bi-level optimization）：外层优化注入后门的骨干模型，内层模拟受害者的微调流程，使后门在微调后仍存活；支持 targeted 与 untargeted 两种模式。攻击保持预训练与下游任务的正常效用（utility），只让目标下游任务继承后门漏洞。

## 实验与结果

在三个不同领域的模型与数据集上评测：CIFAR-10 上针对 ResNet50 的 targeted 后门攻击成功率达到 98.66%，较基线提升 86.22%（数字来自原文）。对六个 SOTA 模型级防御（Neural Cleanse、ABS、MNTD、NAD、CLP、D-BR）逐一评估，结果显示这些防御对被后门化的骨干模型基本无效。

## 贡献与局限

- 贡献一：首次在 backbone 层面注入后门并传染到 prompt learning 下游任务，暴露该范式的深层风险。
- 贡献二：对六个主流模型级防御的系统评估，表明现有防御手段失效，为防御研究提出明确新课题。
- 局限：攻击依赖与下游分布相似的 shadow dataset；有效且实用的防御仍是开放方向。

---

DOI: 10.1109/TIFS.2026.3698596
