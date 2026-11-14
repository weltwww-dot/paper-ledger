# FedMMSR: Federated Multi-Modal Recommendation With Structural Guidance and Robust Integration 总结

## 基本信息
- **标题**: FedMMSR: Federated Multi-Modal Recommendation With Structural Guidance and Robust Integration
- **作者**: Jiahe Xu、Weiming Liu、Pengyang Zhou 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8181-8196
- **发表**: 2026-09-22
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tkde.2026.3736499

## 一句话概括
FedMMSR面向联邦多模态推荐，在用户交互留在客户端的条件下利用公开商品内容补足项目关系，并改善模态融合的抗噪性。

## 问题与动机
客户端只看到稀疏且异质的交互，服务器汇总的项目表示不完整；噪声和模态间优化冲突也会削弱多模态信息的收益。

## 方法
服务器分别从文本、视觉特征构造项目图并以图卷积传播结构信息；客户端使用抗噪损失和个性化冲突感知更新，协调ID协同信号与模态表示。

## 实验与结果
在Amazon Baby、Sports、Clothing和Electronics四个数据集上，FedMMSR优于比较的ID联邦及多模态联邦方法，并在噪声、缺失模态情形保持较强表现；缺失文本造成的下降通常大于缺失视觉（PDF第8–10页）。

## 贡献与局限
结果支持结构引导与自适应融合的组合价值，但项目图需精确两两相似度计算，时间为项目数平方级；论文未证明该步骤可扩展到超大商品目录（PDF第5、11页）。

---
DOI: 10.1109/tkde.2026.3736499
