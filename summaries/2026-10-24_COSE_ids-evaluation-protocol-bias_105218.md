# How evaluation protocol choices inflate intrusion detection accuracy: A three-dataset systematic study 总结

## 基本信息
- **标题**: How evaluation protocol choices inflate intrusion detection accuracy: A three-dataset systematic study
- **作者**: Mohammed Berhili、Omar Chaieb、Mohammed Benabdellah
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173，文章号105218
- **发表**: 2026-10-24
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105218

## 一句话概括
在三个入侵检测基准上量化验证集切分和预处理如何影响准确率。

## 问题与动机
常见的入侵检测评估流程会在多大程度上抬高准确率？与随机种子敏感性和预处理泄漏相比，哪种协议选择对报告结果影响更大？

## 方法
研究使用 UNSW-NB15、NSL-KDD 与 CIC-IDS2017，比较未打乱训练文件后切分验证集的做法与分层随机切分，并考察多个随机种子和预处理环节。实验以同一模型在验证集与官方测试集的准确率差值量化偏差，从而尽量隔离协议本身带来的变化。

## 实验与结果
对10个种子取平均后，UNSW-NB15 的偏置验证准确率为98.91%，官方测试准确率88.45%，差10.46个百分点；NSL-KDD分别为99.94%和80.42%，差19.52个百分点。CIC-IDS2017因预处理已随机分层，差仅0.01%。作者指出数据排序结构解释了部分落差，结论限于所评三套基准和协议（PDF 第7、11页）。

## 贡献与局限
研究量化了评估协议而非模型结构本身造成的准确率膨胀，说明跨论文比较需要报告数据顺序、切分和预处理细节。所用基准存在各自的数据构造与标签限制，其他数据集、漂移环境及不同评估方案仍需单独验证。

---
DOI: 10.1016/j.cose.2026.105218
