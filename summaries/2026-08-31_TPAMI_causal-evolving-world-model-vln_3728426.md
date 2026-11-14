# Toward a Causally-Inspired Evolving World Model for Vision-and-Language Navigation in Continuous Environments 总结

## 基本信息
- **标题**: Toward a Causally-Inspired Evolving World Model for Vision-and-Language Navigation in Continuous Environments
- **作者**: Xuan Yao、Junyu Gao、Changsheng Xu
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15648-15664
- **发表**: 2026-08-31
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3728426

## 一句话概括
E-CWM 通过观测与表征层面的干预及在线记忆演化，提升连续环境视觉语言导航在未见场景中的稳健性。

## 问题与动机
连续环境导航需要把语言指令转成低层移动决策，而训练场景中的外观和表征偏差可能成为捷径相关性，使策略在新环境失效。本文关注如何借助反事实式世界模型减弱这些混杂因素，并在部署过程中适应变化环境。

## 方法
E-CWM 将导航建模为因果启发的部分可观测决策过程，在观测层和内部表征层构造干预，并通过世界模型执行反事实滚动预测以改进策略；在线演化机制持续更新混杂因素记忆缓冲区，测试阶段主要通过缓冲区更新适应，而非依赖梯度更新网络参数。

## 实验与结果
研究在 R2R-CE、RxR-CE 基准上与导航方法比较，并用 TurtleBot4 在实验室验证。R2R-CE 未见验证集上 SR 和 SPL 分别提高 5.2、5.1；RxR-CE 单目设置下 SR 为 31.47、SPL 为 24.14，较所比较基线高 4.81、4.03；机器人实验中整体优于基线（PDF 第10–11、14页）。

## 贡献与局限
工作把双层干预、反事实策略细化和在线记忆演化整合进连续环境导航世界模型，并同时报告模拟基准与实体机器人验证。实体部署仅在实验室环境开展，TurtleBot4 无板载 GPU，RGB-D 数据需传至外部笔记本推理，因此尚未证明资源受限设备上的完全自主实时部署（PDF 第14–15页）。

---
DOI: 10.1109/tpami.2026.3728426
