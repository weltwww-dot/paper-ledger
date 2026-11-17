# A hierarchical framework for multi-agent path planning using cooperative attention and Task-Correlation communication 总结

## 基本信息
- **标题**: A hierarchical framework for multi-agent path planning using cooperative attention and Task-Correlation communication
- **作者**: Ke Han、Shuaiyi Liu
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109897
- **发表**: 2026-11-09
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109897

## 一句话概括
HCAF 结合协作注意力奖励塑形、任务相关稀疏通信和双流条件注意力，在固定目标多智能体三维导航中获得有竞争力的完成率与碰撞表现，同时报告了通信和计算代价。

## 问题与动机
固定目标分配的多智能体路径规划如何改善局部与协作信息融合，同时控制通信开销并避免协调低效？

## 方法
框架通过 CARS 奖励塑形增强分布式态势感知而不改变目标分配；TDKG-CS 根据离线目标相关图与在线注意力构建稀疏通信关系；DuSCAN 使用特征线性调制，使协作特征受局部观测条件化。

## 实验与结果
作者在连续三维固定目标导航中比较多智能体控制基线，覆盖均衡目标、共享目标及不同障碍密度，并另测图处理、通信和计算成本；在 3–3、五障碍设置下，MATD3+HCAF 的任务成功率为 95.4%、个体成功率为 98.4%，且至少发生一次障碍接触的回合占 6.5%；增加障碍后成功表现下降（PDF 第 9–13 页）。结果基于仿真设定，不能直接代表真实机器人部署。

## 贡献与局限
论文将奖励塑形、动态任务相关通信和局部条件化协作融合进层级规划框架；在动态环境、通信失效和真实硬件上的安全性与扩展性尚待验证。

---
DOI: 10.1016/j.neunet.2026.109897
