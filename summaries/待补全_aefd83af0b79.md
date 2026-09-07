# GenIA: Generative Index Advisor for Dynamic Workloads and Data 总结

## 基本信息

- **标题**: GenIA: Generative Index Advisor for Dynamic Workloads and Data
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 数据工程
- **DOI**: 10.1109/tkde.2026.3698793
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

An ideal index advisor needs to effectively manage changes in workload and data, but current approaches fall short in both effectiveness and efficiency because of intrinsic limitations in their frameworks. Heuristic-based methods struggle with efficiency due to their rigid algorithms and lack of adaptive learning capabilities. Reinforcement learning techniques often fail to consistently reach an optimal policy. Classification methods require vast amounts of labeled workloads that include optimal indexes. Additionally, none of the learning-based strategies are equipped to handle shifts in data. To overcome these limitations, this paper presents a new index advisor for dynamic workloads and data, GenIA, which learns to generate a sequence of the recommended index configuration based on historical experience. The generative framework of GenIA avoids erroneous trials to explore bad actions and reliance on high-quality positive and negative examples. Specifically, its novelty exhibits in three aspects. (1) GenIA is empowered with novel attention mechanisms to capture implicit relationships between indexable columns. (2) GenIA combines comprehensive features extracted from workloads, data manipulation statements, and underlying data to effectively capture workload shifts and subtle data shifts. (3) GenIA adopts a novel perturbation-based training strategy to enhance the diversity of training samples and to improve the model parameters' robustness. Extensive experiments on various benchmarks under varying levels of workload and data shifts demonstrate that GenIA outperforms SOTA heuristic-based IA Extend on average by about 7.5%, while utilizing less than 1% of the inference time, and surpasses SOTA learning-based IA SWIRL by 25% − 30% in scenarios with significant workload and data shifts.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tkde.2026.3698793
