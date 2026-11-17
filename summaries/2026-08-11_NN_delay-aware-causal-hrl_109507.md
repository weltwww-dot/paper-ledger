# DECHRL: Empowerment-driven delay-aware causal hierarchical reinforcement learning 总结

## 基本信息
- **标题**: DECHRL: Empowerment-driven delay-aware causal hierarchical reinforcement learning
- **作者**: Chenran Zhao、Dianxi Shi、Haotian Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109507
- **发表**: 2026-08-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109507

## 一句话概括
DECHRL在因果层级强化学习中显式学习延迟分布并以延迟感知赋能目标稳定探索，在离散任务和连续PointMaze中对多种延迟设置表现出优于对照方法的成功率。

## 问题与动机
动作影响可能经过不确定的多步延迟才显现，忽略延迟会使因果发现、子目标分解和层级策略学习失稳。

## 方法
框架联合估计多步因果依赖及其延迟分布，再据此构造子目标层级；延迟感知赋能目标鼓励子策略在延迟不确定性下维持有效探索，并以低层执行结果支持高层决策。

## 实验与结果
在2D-Minecraft、MiniGrid和PointMaze任务中比较不同延迟处理基线，并分析延迟随机性、建模尺度和赋能目标；连续PointMaze中DECHRL在所测延迟条件下成功率最高，但连续任务整体较离散任务更难，且结果来自模拟任务（PDF 第 8、11–13 页）。

## 贡献与局限
把多步因果延迟建模与层级策略学习及赋能探索结合，实验显示其在模拟离散和连续控制任务中有较强延迟适应性；结论尚需在真实环境及更广泛任务中验证。

---
DOI: 10.1016/j.neunet.2026.109507
