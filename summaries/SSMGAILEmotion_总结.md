# Self-supervised multi-modal imitation learning under skewed trajectory demonstrations 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: Self-supervised multi-modal imitation learning under skewed trajectory demonstrations
- **作者**: Yawen Zhao, Yue Chen, Fei Zhu
- **期刊 / 会议**: Neural Networks 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109582
- **PDF**: [SSMGAILEmotion.pdf](papers/SSMGAILEmotion.pdf)

## 一句话概括

论文提出 SSM-GAIL，用自监督未来状态预测、模式感知对比学习和频率感知动态缩放因子，改善偏斜专家轨迹下的多模态模仿学习，使策略更好地区分并复现常见和稀有行为模式。

## 问题与动机

实际专家示范往往包含多个行为模式，但不同模式的轨迹数量严重不均衡；标准 GAIL 或依赖静态状态—动作快照的方法容易发生模式坍塌、遗忘少数模式，并难以表示行为随时间演化的动态差异。论文还指出，真实系统的评估常依赖视频，因此仅有状态指标不足以反映生成行为是否匹配目标模式。

## 方法

SSM-GAIL 分两阶段训练：第一阶段给判别器特征提取器增加解码器，用多步未来状态预测的均方误差进行自监督预训练，以学习动态相关表示；第二阶段在对抗模仿学习中，对中间特征加入 InfoNCE 模式感知对比损失，使同模式样本聚集、异模式样本分离。随后根据 mini-batch 中的模式频率设计动态缩放因子，对少数模式的条件奖励信号加权；论文还以预训练 R3D-18 视频特征计算 VMPCA，作为状态评估之外的事后视频指标。

## 实验与结果

实验覆盖 2D-Trajectory、Reacher、Pusher、Walker2D、Hopper 和 PandaReach 等多模态环境，并以偏斜比 ρ=20 构造主要示范设置。SSM-GAIL 在多数任务上取得更高 NMI、较低 ENT，并在严重偏斜下保持较好的模式分离和模式纯度；消融显示，去除 DSF 后 NMI 平均下降 0.044、ENT 上升 0.063，去除自监督预训练后 NMI 下降 0.031、ENT 上升 0.040，去除对比学习后 NMI 下降 0.019、ENT 上升 0.047。预测步长敏感性分析中，H=4 在六个环境的平均 NMI 和 ENT 上取得总体最佳折中，VMPCA 也为生成视频与对应专家模式的匹配提供了补充证据。

## 贡献与局限

主要贡献是把动态自监督表示、模式对比解耦和频率重加权结合到偏斜多模态 GAIL 中，并同时提供状态—动作与视频模式一致性评价。局限是方法仍依赖少量带模式标识的数据来稳定模式感知学习；自动模式发现、在更复杂领域中的样本效率、可扩展性，以及 Walker2D 中接触相位与平滑未来状态预测之间的失配，仍需进一步解决。

DOI: 10.1016/j.neunet.2026.109582

