# Regional climate risk assessment from climate models using probabilistic machine learning 总结

## 基本信息
- **标题**: Regional climate risk assessment from climate models using probabilistic machine learning
- **作者**: Zhong Yi Wan、Ignacio Lopez-Gomez、Robert Carver 等
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **发表**: 2026-09-28
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01308-7
- **PDF**: [NMI_2026_RegionalClimateRisk.pdf](papers/NMI_2026_RegionalClimateRisk.pdf)

## 一句话概括
GenFocal 把粗分辨率气候投影转成概率化的区域天气样本，使热浪、复合高温湿度和热带气旋等局地风险得以评估。

## 问题与动机
全球气候模型分辨率不足以直接支持地方规划；物理降尺度生成大量极端事件样本的计算代价很高，而传统统计法往往忽略变量间和时空上的关联。自由运行的气候模拟又无法与真实天气逐时配对，限制了常规监督学习。

## 方法
模型分两步处理：先校正粗尺度模拟的系统偏差，再用条件扩散模型对校正后的序列作时空超分辨率采样。超分辨率阶段利用再分析数据构建配对训练样本，但整体流程不要求把每场气候模拟事件与同一天真实天气一一对应。

## 实验与结果
美国区域评估中，GenFocal 对夏季热指数第 99 百分位的平均偏差较统计降尺度基线降低超过 35%，温湿极端事件尾部依赖的平均误差降低 44%；论文还检验持续热浪和热带气旋风险。投影结果是模型条件下的概率估计，不应被当成特定地点未来事件的确定预言。

## 贡献与局限
贡献是把偏差校正、概率生成与局地复合风险分析连接起来，并可高效生成大量样本。结果仍受原始气候模拟、再分析资料及训练区域代表性约束；在其他地区、未来气候分布和罕见灾害上的可靠性仍需持续检验。

---
DOI: 10.1038/s42256-026-01308-7
