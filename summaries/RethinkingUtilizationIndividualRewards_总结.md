# Rethinking the Utilization of Individual Rewards in Multiagent Reinforcement Learning With Sparse Team Rewards 总结

## 基本信息

- **标题**: Rethinking the Utilization of Individual Rewards in Multiagent Reinforcement Learning With Sparse Team Rewards
- **作者**: Yang Zhang, Yunjian Xu, Chengwei Zhang, Chao Wang, Zhihe Yang, Bo Tang, Edward Chung
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TNNLS.2026.3658520
- **arXiv**: 无
- **PDF**: [NN_2026_RethinkingUtilizationIndividualRewards.pdf](papers/NN_2026_RethinkingUtilizationIndividualRewards.pdf)

## 一句话概括

论文提出 CLOT，通过带策略一致性约束的多智能体策略优化动态平衡团队奖励与个体奖励，使个体奖励既能缓解稀疏反馈，又不把学习策略带离团队最优目标。

## 问题与动机

合作 MARL 中团队奖励常在任务成功时才出现，导致信用分配和探索困难。直接把个体奖励与团队奖励相加，可能让各智能体追逐局部目标，产生与团队最优策略不一致的协同行为；已有知识迁移方法又依赖特定个体奖励形式，难以适配不同环境和奖励尺度。论文因此把“利用个体奖励”和“保持团队策略一致”同时作为优化目标。

## 方法

CLOT 将混合策略的团队回报约束为与最优团队策略一致，并用拉格朗日对偶把约束转为可优化目标。拉格朗日乘子由训练动态更新：个体奖励有害时提高团队奖励权重，个体奖励有益时降低该权重。算法为混合策略和团队策略分别构造扩展 TD 误差，结合策略相似性近似、PPO 式裁剪比率以及由精确加减 KL 项得到的目标重构，避免同时从两种策略采样的低效率。

## 实验与结果

实验覆盖 SMAC、MPE 和 GRF。SMAC 中团队胜利奖励为 20，个体奖励包括击杀奖励 10 和生命值相关奖励；CLOT 在所有简单地图达到 100%，多数困难和超困难地图取得最高胜率。GRF 两个任务中胜率均超过 60%。MPE 中，CLOT 在 Spread 的团队奖励约为 10、Attack 中超过 20，并在 50 个捕食者和 20 个猎物的大规模环境取得最佳团队表现；2M 步训练耗时约 2 天 21 小时，略高于 MAPPO 的 2 天 8 小时和 IRAT 的 2 天 18 小时。与 LAIES/LIIR 结合后，胜率和收敛速度在多个地图提升；个体奖励放大 3 倍或 5 倍时性能变化控制在 30% 内。

## 贡献与局限

贡献包括：用显式策略一致性约束处理个体奖励导致的目标偏移；通过动态拉格朗日乘子适配有益、误导或冲突的个体奖励；在多环境、多种奖励设计和大规模设置下验证兼容性。局限是大规模实验训练成本仍较高，方法依赖混合策略与团队策略足够接近的相似性假设；论文也指出未来需进一步检验更复杂任务和更一般的策略分布偏离情形。

---
DOI: 10.1109/TNNLS.2026.3658520
