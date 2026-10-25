# Machine learning methods for DDoS attack detection in software-defined networks 总结

## 基本信息
- **标题**: Machine learning methods for DDoS attack detection in software-defined networks
- **作者**: Atul Kumar、Bhisham Sharma、Vishesh Tanwar、Panos Liatsis
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25:180
- **发表**: 2026-10-24
- **日期来源**: Crossref published-online；不以PDF收稿或录用日期替代
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01354-7
- **PDF**: [IJIS_2026_MLDDoSSDN.pdf](papers/IJIS_2026_MLDDoSSDN.pdf)

## 一句话概括
比较六类传统分类器及互信息特征筛选在SDN DDoS检测中的效果，并通过更严格划分和特征审计，揭示近满分结果中的数据集偏差。

## 问题与动机
高检测率未必代表能识别后续流量：采集时间、主机标识、重复样本或直接定义类别的字段，都可能形成捷径。论文同时考察准确率、特征数量和离线推理成本，而非提出新分类器。

## 方法
对DDoS-SDN和APA-DDoS采用训练集内拟合的预处理、互信息排序及Top-5/Top-12筛选，比较LR、SVM、KNN、决策树、随机森林和XGBoost。除70/30分层随机划分外，补充时间顺序、未见主机划分、逐特征审计及训练集交叉验证；SVM因成本未参与交叉验证。

## 实验与结果
DDoS-SDN全19特征下，XGBoost随机划分准确率为100%，时间顺序划分降至93.33%；Top-5使KNN准确率升至99.97%，离线延迟由约0.76降至0.007毫秒/流。APA-DDoS去除标识后仅剩65种特征向量，PSH字段又直接区分两种攻击，故只用于审计、不据此排列模型优劣（PDF第11、13—14、21、23、27页，表8—10、15、17、19）。

## 贡献与局限
将特征成本分析与数据泄漏审计结合，说明应先核验基准再比较模型。主要分类结论来自单一Mininet仿真数据集，随机测试样本中仍有6.55%的特征向量在训练集出现；延迟也是离线CPU测量，未验证真实控制器负载、在线缓解效果或未知攻击泛化（PDF第24—25页）。

---
DOI: 10.1007/s10207-026-01354-7 | PDF: [IJIS_2026_MLDDoSSDN.pdf](papers/IJIS_2026_MLDDoSSDN.pdf)
