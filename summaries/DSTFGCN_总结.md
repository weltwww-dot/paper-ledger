# DSTFGCN: A dynamic spatial-temporal fusion graph convolution network for traffic flow forecasting 总结
## 基本信息
- **标题**: DSTFGCN: A dynamic spatial-temporal fusion graph convolution network for traffic flow forecasting
- **作者**: Tianyi Pan, Xinyuan Zhou, Shiyong Lan, Wenwu Wang, Hongyu Yang, Zheng Li, Zhiang Hou, Yao Ren
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108989
- **PDF**: [NN_2026_DSTFGCN.pdf](papers/NN_2026_DSTFGCN.pdf)
## 一句话概括
DSTFGCN通过门控时间演化和动态空间融合，同时预测交通网络中的局部与全局流量变化。
## 问题与动机
循环模型常偏重局部时间依赖，预定义或简单自适应邻接矩阵又难反映真实交通关系，因而需要动态时空建模。
## 方法
模型用门控膨胀因子演化捕捉局部时间依赖，用节点独立的时间图演化学习全局依赖，再融合动态空间和时间表示。
## 实验与结果
在6个真实世界交通数据集上，作者报告DSTFGCN超过主流方法；本文不补写未逐表核对的误差数值。
## 贡献与局限
贡献是同时动态化时间依赖和空间关系。局限是图结构可能依赖具体城市，异常事件、缺失传感器和跨城市迁移仍需验证。
---
DOI: 10.1016/j.neunet.2026.108989
