# Logits-Level Balanced Machine Unlearning for LLM-Based Recommendation System 总结

## 基本信息

- **标题**: Logits-Level Balanced Machine Unlearning for LLM-Based Recommendation System
- **作者**: Chenchen Tan, Xinghao Li, Youyang Qu, Cunjian Chen, Shujie Cui, Longxiang Gao
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3660137
- **arXiv**: 无
- **PDF**: [NN_2026_LogitsLevelBalancedMachine.pdf](papers/NN_2026_LogitsLevelBalancedMachine.pdf)

## 一句话概括

本文提出面向 LLM 推荐系统的双阶段机器遗忘方法，用 GA 先削弱目标记忆，再通过修改教师 logits 的知识蒸馏恢复合理输出，并用双适配器和性能维护模块平衡遗忘效果与推荐质量。

## 问题与动机

LLM 推荐系统会记忆用户偏好、推荐内容和可能包含隐私或版权的信息，当用户提出删除请求时，完整重训代价很高，而直接梯度反转又容易造成输出崩溃。传统知识蒸馏可能因为修改前后的标签差异太小而无法产生足够的遗忘信号，单一适配器同时承担遗忘和恢复任务还会产生梯度冲突。作者因此将“删除目标关联”和“恢复非目标能力”拆成可控的阶段与模块。

## 方法

方法先冻结原 LLMRec 作为教师模型，对目标 token 及其嵌入空间中相似的 token 修改 logits，降低敏感输出概率，再让学生模型通过 KL 散度学习修改后的教师分布。训练前使用 GA 使学生模型适度偏离原有目标知识，最终损失是加权 GA 损失与 KL 损失的组合。模型只更新插入 Transformer 注意力层后的轻量瓶颈适配器，另设一组冻结的性能维护适配器；当保留数据上的 ROUGE 低于阈值时，才解冻维护适配器并用少量保留数据恢复通用推荐能力。该双适配器设计避免遗忘与恢复直接争用同一组参数，同时支持针对不同模型架构的 rank 和相似 token 抑制参数调节。

## 实验与结果

实验覆盖 LLaMA 7B/13B、GPT-NEO 125M/2.7B 和 T5 Large/3B，并与 GA、NPO、IHL、EUL、SKD 五类方法比较；数据来自 Amazon Product Reviews、Yelp Review Full 和 MovieLens，增强后的 Amazon 与 Yelp 数据分别含 1500 和 2000 个样本，目标遗忘规模主要测试 32 与 128 个样本，另有 LLaMA-7B 的 256 样本收敛实验。结果显示，GA 虽能把目标集 ACC/BLEU 压低，却会造成保留集效用崩溃；本文方法在六种模型配置中保持较低目标准确率，同时保留较高的保留集 ACC、ROUGE-L 和更稳定的训练过程。解码器模型通常在 rank 位移 (K\approx10\)–100、相似 token 抑制数约 5–10 时达到较好的遗忘—效用折中；GPT-NEO 用户信息遗忘实验中，(el_5) 接近零，MIA 成功率接近随机猜测的 0.5。Steam 大规模案例包含超过 700 万条交互、约 25 万用户，并模拟删除 1000 个样本及语义改写、噪声扰动请求，方法仍保持较稳定的遗忘和保留能力。

## 贡献与局限

本文把 GA 驱动的知识反转、logits 级知识蒸馏、轻量适配器和自适应性能维护组合起来，在不完整重训的前提下实现更细粒度的推荐系统遗忘。双适配器使目标删除和效用恢复相互隔离，MIA 和用户信息抽取指标也提供了隐私层面的验证。局限在于公开 LLMRec 遗忘基准和真实部署数据仍不足，Amazon、Yelp 等数据经过 GPT-4 增强，合成描述不能完全代表商业系统；高频删除请求会增加累计训练负担，阈值和批处理还需要访问控制、限流、审计以及可认证删除保证。

---
DOI: 10.1109/TNNLS.2026.3660137
