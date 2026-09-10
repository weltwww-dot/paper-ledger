# Multi-source domain open-set deep transfer adversarial network for operating performance assessment 总结

## 基本信息

- **标题**: Multi-source domain open-set deep transfer adversarial network for operating performance assessment
- **作者**: Yan Liu, Lulu Fu, Yulu Xiong, Siqi Wang, Fei Chu, Chenhui Bao, Fuli Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108981
- **arXiv**: 无
- **PDF**: [NN_2026_MDODTAN.pdf](papers/NN_2026_MDODTAN.pdf)

## 一句话概括

MDODTAN面向电熔镁炉的新生产过程，把多源域对抗迁移与开放集未知等级细分结合起来进行操作性能评估。

## 问题与动机

新生产过程初期通常没有性能等级标签，还可能出现源域未见的新等级。传统多源开放集适应把所有未知类合成一类，无法提供更细的性能诊断和等级区分。

## 方法

模型为每个源域配置任务分类器，以提升已知等级识别；通过已知/未知等级相似性矩阵为目标样本生成伪标签，并以多源域对抗训练缩小源—目标域间的已知等级差距。该流程旨在同时识别已知等级并细分多个未知等级。

## 实验与结果

实验围绕电熔镁炉过程操作性能评估开展。作者报告该方法相对现有方法获得更高的开放集评估精度，并能正确区分多个未知性能等级；摘要未给出具体数值。

## 贡献与局限

贡献是把未知等级细分纳入多源开放集POPA，而不是简单拒识未知类。局限是伪标签和相似性矩阵可能受域偏移、类别比例与过程工况影响，跨炉型和真实在线变化下的稳定性仍需验证。

---
DOI: 10.1016/j.neunet.2026.108981
