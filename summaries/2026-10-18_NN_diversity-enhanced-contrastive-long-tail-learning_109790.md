# Learning long-tailed representations via diversity-enhanced contrastive learning 总结

## 基本信息
- **标题**: Learning long-tailed representations via diversity-enhanced contrastive learning
- **作者**: Yibo Xu、Wenyi Zhao、Bin Zheng 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109790
- **发表**: 2026-10-18
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109790

## 一句话概括
DECL 通过多分支图像多样化增强与多尺度对比学习，扩充尾类视觉表征并强化类间分界，缓解长尾分类中少数类样本和特征多样性不足。

## 问题与动机
长尾数据中的尾类样本稀少，重复过采样容易过拟合，欠采样又丢失多数类信息；仅做重加权也未创造尾类内部变化。作者关注如何生成语义相关、又不模糊类别边界的多样视图，并让对比目标有效利用这些表征。

## 方法
DECL 包含多样性增强图像模块 DIA、特征提取器和多样性感知对比模块 DCL。DIA 用多分支增强和跨样本拼接构造变化丰富的图像组合；提取器编码增强视图；DCL 以类别原型组织监督对比，并结合跨尺度对齐，让同类特征聚合、异类分离。实验在 CIFAR-LT、ImageNet-LT 与 iNaturalist 2018 上比较长尾基线，并通过模块消融检验 DIA、DCL 和尺度项。

## 实验与结果
作者报告 CIFAR100-LT Top-1 为60.4%，CIFAR10-LT 为85.1%，ImageNet-LT 为59.8%，iNaturalist 2018 为74.2%。在 CIFAR100-LT、不平衡因子0.1的跨尺度消融中，加入跨尺度项后总体准确率由59.2%升至60.3%，Few-shot准确率由39.0%升至42.6%，收益主要落在中尾类。

## 贡献与局限
DECL 将多样视图与原型对比结合，四个长尾基准及消融显示竞争力，跨尺度项尤其帮助 Few-shot 类。结果依赖既定数据划分和骨干，向语义复杂或持续变化的分布迁移仍需评估。

---
DOI: 10.1016/j.neunet.2026.109790
