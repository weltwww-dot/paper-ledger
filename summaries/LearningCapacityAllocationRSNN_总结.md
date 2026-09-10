# Learning capacity allocation for stable sequential learning in recurrent spiking neural networks 总结

## 基本信息

- **标题**: Learning capacity allocation for stable sequential learning in recurrent spiking neural networks
- **作者**: Yingchao Yu, Yaochu Jin, Kuangrong Hao, Yuchen Xiao, Yuping Yan, Hengjie Yu, Zeqi Zheng, Wenxuan Pan
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109590
- **arXiv**: 无
- **PDF**: [NN_2026_LearningCapacityAllocationRSNN.pdf](papers/NN_2026_LearningCapacityAllocationRSNN.pdf)

## 一句话概括

IP2-RSNN 把“允许哪些参数适应”作为序列学习的上游问题，在任务族层面分配脉冲神经元的内在可塑性，以提高稳定性和可解释性。

## 问题与动机

连续更新参数会造成干扰、失稳和旧知识丢失，但多数方法只研究如何更新，默认整个模型均匀可适应。作者认为有限学习容量的分配位置本身决定了序列学习动力学。

## 方法

IP2-RSNN 是两阶段框架：先在任务族层面选择内在神经元可塑性，再评估该分配在连续任务中的效果。研究对象是 recurrent spiking neural networks，重点调整时间常数、阈值等内在参数，并与均匀或错误分配进行对照。

## 实验与结果

在多种认知启发的延迟响应任务族上，任务依赖的容量分配比错误分配具有更好的学习稳定性和适应效率；均匀内在适应未达到同等稳定性。结果还显示分配会形成神经元和网络层面的结构化专门化，附加 Rotated MNIST 实验也支持其优势。

## 贡献与局限

贡献是把学习容量分配明确化，并展示它对 RSNN 稳定序列学习和结构专门化的影响。局限是任务族和网络规模仍受实验设置限制，如何自动学习更复杂任务分解及迁移到真实时序数据仍待研究。

---
DOI: 10.1016/j.neunet.2026.109590
