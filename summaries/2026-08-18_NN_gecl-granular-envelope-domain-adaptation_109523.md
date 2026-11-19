# GECL: Fine-grained granular envelope contrastive learning for unsupervised domain adaptation 总结

## 基本信息
- **标题**: GECL: Fine-grained granular envelope contrastive learning for unsupervised domain adaptation
- **作者**: Pufei Li、Pin Wang、Yongming Li 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109523
- **发表**: 2026-08-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109523

## 一句话概括
GECL 为每个类别构造多个细粒度特征包络，并用包络引导对比学习和一致性约束进行无监督域适应。

## 问题与动机
类别级域适应常把同类样本压成单一原型，忽略类内多样性和概念漂移，可能造成目标域负迁移及特征簇结构粗糙。

## 方法
按局部纯度准则递归划分特征空间，生成多个类别包络作为细化原型；通过样本到包络的对比目标增强判别性，再以包络引导一致性正则约束预测与结构对齐，联合处理域差异。

## 实验与结果
在 Office-Home、Office-31、VisDA-2017 和 DomainNet 四个无监督域适应基准上，以分类测试准确率评估跨域迁移。Office-Home 的12个迁移任务平均准确率为75.8%，表1列出的逐任务均值包括 Ar→Cl 60.6%、Cl→Ar 74.2%、Rw→Pr 87.3%；Office-31 六任务平均91.7%（排除接近饱和的 D↔W 后为87.6%）；VisDA-2017 12类平均87.5%；DomainNet归纳式设置平均54.8%，比文中最佳对照 DLRE 高1.5个百分点。Office-Home消融中完整模型均值75.7%，同时移除对比损失和一致性正则后降至69.6%；以单类质心替代细粒度包络的变体为74.3%。

## 贡献与局限
以多包络表示类别内部结构，减少单原型对多模态类分布的压缩，并把结构信息用于对比和一致性学习。包络质量依赖特征空间与纯度准则；当前证据主要来自视觉域适应基准，概念漂移更强的现实分布仍需验证。

---
DOI: 10.1016/j.neunet.2026.109523
