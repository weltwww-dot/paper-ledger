# APO: Anchored policy optimization by leveraging unsampled actions in continuous spaces 总结

## 基本信息
- **标题**: APO: Anchored policy optimization by leveraging unsampled actions in continuous spaces
- **作者**: Weijun Luo、Yingzhuo Liu、Hongsong Tang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109476
- **发表**: 2026-08-05
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109476

## 一句话概括
APO 通过约束未采样动作区域的策略概率比改善连续控制训练稳定性，在 MuJoCo 多数基准上优于比较策略，但额外采样带来运行开销且动作数阈值依任务而异。

## 问题与动机
PPO 只约束已采样动作会使未采样动作区域的策略分布漂移，能否显式约束该区域以改善连续控制优化？

## 方法
在 PPO 目标中加入未采样动作比率正则，对新旧策略在未采样动作区域的概率比进行锚定，并分析策略改进界及正则权重和动作数的影响。

## 实验与结果
在 MuJoCo 连续控制基准上与 PPO-Clip、PPO-Penalty、SPO、TRPO 及熵正则 PPO 比较，报告多随机种子的回报与稳定性；APO 在多数环境取得较高回报，但增加未采样动作数量会影响吞吐，过大的固定正则权重在部分任务引发不稳定（PDF 第6–10页）。

## 贡献与局限
将策略更新约束扩展至未采样动作区域并提供相应理论分析；未采样动作数具有任务依赖性，训练效率与性能之间仍需权衡。

---
DOI: 10.1016/j.neunet.2026.109476
