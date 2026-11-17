# TAMTRL: Teacher-aligned reward reshaping for multi-turn reinforcement learning in long-context compression 总结

## 基本信息
- **标题**: TAMTRL: Teacher-aligned reward reshaping for multi-turn reinforcement learning in long-context compression
- **作者**: Li Wang、Yandong Wang、Xin Yu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109492
- **发表**: 2026-08-14
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109492

## 一句话概括
本文提出 TAMTRL，以同一语言模型在教师侧筛选上下文中的概率信号重塑逐轮奖励，改善长文档分块压缩任务中的多轮强化学习信用分配。

## 问题与动机
长文档需分块读取并反复更新记忆，而仅用最终答案奖励难以判断各轮记忆更新的贡献；依赖外部评审或过程奖励模型又会增加成本和估计噪声。

## 方法
将长文档处理建模为多轮记忆更新过程；训练时由教师侧相关文档上下文提供对齐信号，以归一化对数概率形成逐轮奖励，学生执行时仅依赖局部观察，不需外部模型。

## 实验与结果
在七个长上下文基准、Qwen3-0.6B 与 Qwen3-1.7B 等设置下比较强基线，论文报告 TAMTRL 的平均相对提升为 2.03%，并分析训练动态、奖励设计及数据规模；教师筛选噪声测试显示平均准确率仅有小幅波动。结论限于所测模型和基准任务（PDF 第 6–8 页）。

## 贡献与局限
该方法提供不依赖外部评审器的逐轮信用分配方案，并在多基准评测中改善长上下文表现；其效果仍受基准、教师筛选质量与模型规模设定约束。

---
DOI: 10.1016/j.neunet.2026.109492
