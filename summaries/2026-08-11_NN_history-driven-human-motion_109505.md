# Repetitive history-driven fuzzy Markov networks for long-term human motion prediction 总结

## 基本信息
- **标题**: Repetitive history-driven fuzzy Markov networks for long-term human motion prediction
- **作者**: Jiacheng Luo、Jianqi Zhong、Jianhua Ji 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109505
- **发表**: 2026-08-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109505

## 一句话概括
本文提出 RFN，以模糊状态建模和历史重复模式引导扩散预测，改善长时程三维人体动作预测的精度与多样性。

## 问题与动机
不同关节运动幅度差异大，统一注意机制也可能忽略历史序列中的周期重复模式，导致长程预测误差和时间不连贯。

## 方法
模糊 Markov 噪声生成模块根据关节变化特征调节噪声，历史重复驱动模块结合局部与全局时间依赖，并以回顾式重放细化扩散去噪过程。

## 实验与结果
在 Human3.6M 与 HumanEva-I 上同多种动作预测基线比较，使用 ADE、FDE、多模态误差和多样性等指标；论文报告 RFN 在 ADE/FDE 及多模态指标上优于所比方法。不同数据集动作与预测时长有限，长时预测结果仍受分布变化影响（PDF 第 10–15 页）。

## 贡献与局限
RFN 将关节差异和历史重复线索纳入扩散式动作预测，并在两个基准上报告精度及多样性收益；跨人群、动作类型和实际交互环境的泛化仍待验证。

---
DOI: 10.1016/j.neunet.2026.109505
