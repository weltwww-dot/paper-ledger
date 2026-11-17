# Distribution aware soft alignment with boundary pseudo label correction for unsupervised visible-infrared person re-identification 总结

## 基本信息
- **标题**: Distribution aware soft alignment with boundary pseudo label correction for unsupervised visible-infrared person re-identification
- **作者**: Hongyang Fu、Jin Wang、Xiaoshuai Niu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109512
- **发表**: 2026-08-13
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109512

## 一句话概括
DASBC利用分布感知软对齐和边界伪标签修正改善无监督可见光-红外行人重识别，在SYSU-MM01与RegDB上取得具有竞争力的检索结果。

## 问题与动机
无监督可见光-红外行人重识别缺少身份标注，跨模态聚类对应关系含糊且边界样本容易产生错误伪标签。

## 方法
DASA以概率软对齐表达跨模态簇关联强弱，保留不确定关系；BPLC识别并修正聚类边界样本伪标签，再以模态内学习和跨模态监督联合训练表征。

## 实验与结果
在SYSU-MM01和RegDB上与无监督重识别基线比较，并报告消融、随机种子和参数分析；SYSU-MM01全搜索设置下Rank-1为57.01%、mAP为53.00%，多随机种子结果显示仍存在波动（PDF 第 3、6、10、12–13 页）。

## 贡献与局限
针对软簇对应和边界伪标签两类噪声分别设计校正模块，并在两个可见光-红外基准上评估；性能依赖伪标签质量，跨场景和真实部署表现尚待验证。

---
DOI: 10.1016/j.neunet.2026.109512
