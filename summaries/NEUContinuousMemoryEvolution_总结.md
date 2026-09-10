# NEU: Continuous-time memory evolution for temporal interaction graph networks 总结

## 基本信息

- **标题**: NEU: Continuous-time memory evolution for temporal interaction graph networks
- **作者**: Yang Meng, Yuting Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108998
- **arXiv**: 无
- **PDF**: [NN_2026_NEUContinuousMemoryEvolution.pdf](papers/NN_2026_NEUContinuousMemoryEvolution.pdf)

## 一句话概括

NEU在时间交互图的事件更新之间连续演化节点记忆，使节点状态可以在任意时间戳查询并适应自然衰减与短期漂移。

## 问题与动机

TGN、TGAT等记忆模型通常只在交互事件发生时离散更新节点状态，把时间差当作静态输入。长时间不活跃会造成记忆陈旧，且模型无法自然给出两个事件之间任意时刻的节点状态。

## 方法

Natural Evolution Unit在嵌入读出前加入连续时间记忆演化阶段。它把时间差从调节更新的静态特征改为驱动状态动态演化的变量，用ODE式机制表达自然衰减和邻居影响逐渐消退，并以固定时间编码提高训练稳定性。

## 实验与结果

论文在时间交互图预测任务上与事件驱动记忆模型比较，结果表明连续演化能缓解稀疏节点记忆老化并改善长期预测。具体数据集和指标以全文实验表为准，未在此处补写未核对数字。

## 贡献与局限

贡献是把“事件之间不变”的记忆假设改为连续时间演化，并支持任意时间点查询。局限是连续动力学带来额外计算和建模假设，ODE形式、时间尺度和稀疏事件分布对泛化的影响仍需研究。

---
DOI: 10.1016/j.neunet.2026.108998
