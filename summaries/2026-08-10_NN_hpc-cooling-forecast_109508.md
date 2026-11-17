# Edge-cloud collaboration-driven predictive modeling for high-performance computing centers 总结

## 基本信息
- **标题**: Edge-cloud collaboration-driven predictive modeling for high-performance computing centers
- **作者**: Shuaiyin Ma、Yeye Cao、Yang Liu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109508
- **发表**: 2026-08-10
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109508
- **PDF**: [NN_2026_hpc-cooling-forecast_109508.pdf](papers/NN_2026_hpc-cooling-forecast_109508.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
面向高性能计算中心液冷系统的FS-Attention结合时序特征建模与边云协作，在真实冷却运行数据上改善冷却液流量预测，并维持较低的边侧推理开销。

## 问题与动机
液冷系统的负载与热状态变化会影响流量预测，而边缘节点资源有限，单纯追求精度或模型轻量化都可能不适合在线部署。

## 方法
利用液冷系统运行数据构建预测流程，以FS-Attention捕捉多尺度时间依赖和瞬态变化，并在边云协作架构中划分训练、调参与现场推理负载。

## 实验与结果
论文使用HPC液冷系统采集的运行及冷却动态数据，与LSTM、N-BEATS、Transformer、TFT、DLinear和PatchTST等比较，报告多随机种子误差与消融；部署分析给出FS-Attention存储1.497 MB、推理延迟0.016 ms，作者指出注意力诊断并不能完整解释模型因果机制（PDF 第 5、9–11、16–17、20 页）。

## 贡献与局限
提供面向液冷流量预测的边云协作建模与部署评估，兼顾误差、瞬态适应和资源开销；现有验证依赖特定中心及平台，跨设施推广能力仍需验证。

---
DOI: 10.1016/j.neunet.2026.109508 | PDF: [NN_2026_hpc-cooling-forecast_109508.pdf](papers/NN_2026_hpc-cooling-forecast_109508.pdf)
