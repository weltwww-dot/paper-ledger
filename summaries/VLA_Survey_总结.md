# A Survey on Vision–Language–Action Models for Embodied AI

## 基本信息

- 标题: A Survey on Vision–Language–Action Models for Embodied AI
- 作者: Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King
- 期刊 / 会议: IEEE Transactions on Neural Networks and Learning Systems 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1109/tnnls.2025.3650584
- PDF: [TNNLS_2026_VLA_Survey.pdf](papers/TNNLS_2026_VLA_Survey.pdf)

- 标题: A Survey on Vision–Language–Action Models for Embodied AI
- 作者: Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King
- 期刊 / 会议: IEEE Transactions on Neural Networks and Learning Systems 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**：A Survey on Vision–Language–Action Models for Embodied AI
- **作者**：Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King
- **期刊**：IEEE Transactions on Neural Networks and Learning Systems, Vol. 37, No. 7, July 2026
- **研究方向**：具身人工智能、视觉语言动作模型、机器人学习
## 一句话概括

论文系统综述 VLA 的组件、低层控制策略和高层任务规划器，进一步整理数据集、仿真器与基准，并总结安全、泛化和真实部署方向的挑战。

## 问题与动机

VLA 模型要把视觉观测、语言指令转化为机器人动作，连接了 VLM/LLM、强化学习、模仿学习和机器人控制。该领域发展很快，模型定义、架构和资源分散，研究者难以比较低层动作策略与高层长时程规划，也缺乏对数据稀缺、仿真到现实差距和安全问题的统一整理。

## 方法

作者先给出广义 VLA 定义，并以三条研究线组织文献：VLA 的关键组件（视觉表征、动力学、世界模型、推理等）；接收多模态输入并输出低层动作的控制策略；把长时程指令分解为子任务的高层任务规划器。综述进一步按 Transformer、扩散、三维视觉、LVLA、语言/代码式规划等维度比较技术细节，并归纳真实数据集、模拟器、任务规划和具身问答基准。

## 实验与结果

这是综述论文，没有新的统一训练实验。其结果是一个覆盖代表性方法、训练目标、动作类型、资源和评测基准的分类地图。文章归纳出低层控制与高层规划的互补关系，同时指出数据集规模与多样性、模型大小和环境泛化对 VLA 性能的重要影响，并以 Awesome-VLA 仓库持续汇总资源。

## 贡献与局限

论文贡献是给出较完整的 VLA 三线分类、对组件和控制/规划架构做技术层比较，并集中整理数据集、仿真器和基准。局限是领域迭代极快，任何静态综述都可能迅速过时；不同论文的成功率、任务和硬件设置并不完全可比。作者指出的后续重点包括安全护栏、细粒度基准、跨具身泛化、多模态融合、实时响应、多智能体协作和伦理治理。

---
DOI: 10.1109/tnnls.2025.3650584
