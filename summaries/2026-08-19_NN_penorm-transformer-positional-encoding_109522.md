# PeNorm: Enhancing positional discriminability in transformers through normalization-based encoding optimization 总结

## 基本信息
- **标题**: PeNorm: Enhancing positional discriminability in transformers through normalization-based encoding optimization
- **作者**: Xilong Zhang、Ruochen Liu、Xuefeng Liang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109522
- **发表**: 2026-08-19
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109522

## 一句话概括
PeNorm 通过归一化优化位置编码的尺度与分布，提升 Transformer 对细粒度位置上下文的区分能力。

## 问题与动机
正弦和可学习绝对位置编码在相邻或结构相似位置上可能不够可分，影响模型识别重复模式与细粒度顺序关系。

## 方法
提出 PeNorm，在位置维度上对正弦/余弦位置编码分量做归一化，并配合可学习仿射参数与尺度参数，改善位置向量的分布和区分度；可用于多种位置编码形式。理论分析给出一个具体构造：三层 Transformer Encoder 在特定编码设置下可识别 Parity-Odd（奇数位置上的1的数量为偶数）任意长度字符串。该命题是对特定形式语言的表达能力证明，范围不等同于一般位置任务上的普遍准确性保证。

## 实验与结果
实证覆盖形式语言识别、WMT 2014 英德/英俄机器翻译和 GPT-BERT 语言建模。形式语言部分为每种语言生成10,000条正负平衡样本，按8:1:1划分训练/验证/测试；机器翻译使用 WMT14 En-De（约460万训练句对）及 En-Ru（约250万），并报告 BLEU、ChrF2++、COMET。一个可复核结果是附录英德五种随机种子实验中 SAPE 基线 BLEU 均值28.33，加入 PeNorm 后为28.44；ChrF2++由55.31升至55.43，COMET由82.40升至82.49。理论部分则是针对特定 Parity-Odd 形式语言的构造性证明：存在三层 Transformer Encoder 配合适当位置编码可识别任意长度字符串，不代表一般位置任务或所有数据集都达到完美准确率。

## 贡献与局限
贡献是把位置向量间的可分性作为可操作的几何目标，以位置维归一化增强不同位置表征，并在形式语言、机器翻译和语言建模任务中检验。三层网络的理论结果只针对 Parity-Odd 及文中构造的适当位置编码；实际翻译实验的增益幅度较小且随编码和指标变化，不能据此推断所有位置敏感任务都能完美预测。

---
DOI: 10.1016/j.neunet.2026.109522
