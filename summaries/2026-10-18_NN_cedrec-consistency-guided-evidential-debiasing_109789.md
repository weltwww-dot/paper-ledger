# Consistency-guided evidential debiasing for multimodal recommendation 总结

## 基本信息
- **标题**: Consistency-guided evidential debiasing for multimodal recommendation
- **作者**: Lin Pan、Zhiqiang Pan、Honghui Chen
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109789
- **发表**: 2026-10-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109789

## 一句话概括
CEDRec结合模态偏差证据与语义一致性门控，在维持有竞争力排序的同时降低多模态推荐的物品曝光集中度。

## 问题与动机
图像或文本中的强单模态信号可能主导推荐，普通融合又会稀释这种偏差信号；若不判断跨模态语义是否一致，去偏还可能误罚内容可靠的物品。

## 方法
在图推荐骨干上加入证据偏差网络，以邻域分歧和流行度构造弱监督先验，用Dempster-Shafer简化形式融合风险证据，该形式等价于noisy-OR；语义瓶颈提炼共享信息并调节惩罚，PCGrad缓解排序与压缩目标的梯度冲突。

## 实验与结果
三个Amazon子集经过五核过滤和8∶1∶1随机划分，五次运行报告均值与标准差。Baby上NDCG@20为4.63±0.03%，低于DuGRec的4.88±0.06%；Gini@20为76.83±0.06%，低于PGL的78.91±0.06%。相同骨干下各项指标优于EliMRec和M-Debias，另有Netflix跨场景验证。

## 贡献与局限
方法把偏差强度和语义一致性分开建模，展示了曝光均衡与排序质量的折中。Gini仅衡量曝光集中度，不能直接证明因果去偏；固定预提取特征、物品级门控忽略用户差异，以及先验构建对物品数量的平方复杂度，限制了可靠性和扩展性。

---
DOI: 10.1016/j.neunet.2026.109789
