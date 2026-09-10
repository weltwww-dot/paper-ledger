# Dual object graph and bisimulation metric for object-goal navigation in unfamiliar environment 总结

## 基本信息

- **标题**: Dual object graph and bisimulation metric for object-goal navigation in unfamiliar environment
- **作者**: Yiyue Meng, Chi Guo, Aolin Li, Kang Zhou
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108921
- **arXiv**: 无
- **PDF**: [NN_2026_DualObjectGraphBisimulationNavigation.pdf](papers/NN_2026_DualObjectGraphBisimulationNavigation.pdf)

## 一句话概括

论文提出双对象图 DOG 和双模拟度量 BM，分别改善视觉表示与导航策略，使智能体能在陌生环境中寻找目标物体并减少死循环。

## 问题与动机

物体目标导航需要从第一视角视觉观察中同时学习有信息量的表示和稳健策略。背景、视角变化以及循环和卡死状态会使仅依赖当前局部观察的策略失效。

## 方法

DOG 由当前对象图和历史对象图组成，分别编码实时对象关系以及长期的类别接近性和空间相关性。BM 是自监督强化学习技术，将行为相似的观察聚到表示空间中，保留任务相关信息并为策略提供摆脱死锁的信号。

## 实验与结果

实验在 AI2-Thor 和 RoboThor 环境中进行，结果显示该方法提升了陌生环境导航的有效性和效率。真实世界部署实验进一步支持其迁移能力；摘要未给出统一的具体提升数字。

## 贡献与局限

贡献是把当前—历史对象关系与行为等价表示结合到物体目标导航中。局限是验证仍主要依赖仿真环境及特定视觉对象图构造，复杂真实场景中的检测误差和长期记忆成本仍需评估。

---
DOI: 10.1016/j.neunet.2026.108921
