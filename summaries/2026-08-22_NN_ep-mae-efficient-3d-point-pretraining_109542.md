# EP-MAE: A resource-efficient masked autoencoding framework for 3D neural representation learning 总结

## 基本信息
- **标题**: EP-MAE: A resource-efficient masked autoencoding framework for 3D neural representation learning
- **作者**: Jian Zhu、Jiale Zhao、Chengxing Lin 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109542
- **发表**: 2026-08-22
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109542

## 一句话概括
EP-MAE以序列化点云分组、上下文感知掩码token丢弃和轻量动量教师减少三维掩码预训练成本，同时保留点云表征质量。

## 问题与动机
点云无序且不规则，现有掩码预训练常依赖昂贵的近邻搜索、密集解码和重型教师网络，限制大规模无标注三维数据的预训练效率。

## 方法
框架先按空间序列化方式将点云切成局部patch，避免基于k近邻的高成本分组；解码前根据序列邻域密度优先丢弃上下文支持不足的掩码token；再以学生patch嵌入的指数滑动平均构造轻量动量教师，在特征空间提供重建目标。三部分共同减少分组和解码开销。

## 实验与结果
在ModelNet40与ScanObjectNN等下游基准评估。ModelNet40上，相较Point-MAE，EP-MAE预训练加速4.06倍且分类准确率提高0.3个百分点；相较PointGPT，准确率提高0.2个百分点且预训练加速4.93倍。ScanObjectNN上，相较Point-MAE，三个划分OBJ-BG、OBJ-ONLY、PB-T50-RS在论文列出的两种旋转增强设置下，准确率增益依次为+0.69/+1.38、+1.04/+0.18、+0.84/+0.10个百分点。4.06倍是预训练耗时加速比，并非PB-T50-RS单一划分的速度结果。

## 贡献与局限
贡献是同时从点云分组、掩码解码和教师监督三处削减预训练成本，而不是只缩小主干网络。所报告证据集中于标准点云数据集和下游识别/分割；真实采集点云的传感器噪声、稀疏程度变化及更大数据规模仍需验证。

---
DOI: 10.1016/j.neunet.2026.109542
