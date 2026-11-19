# A unified foundation model for heterogeneous EEG signal modeling via language-aligned semi-supervised learning 总结

## 基本信息
- **标题**: A unified foundation model for heterogeneous EEG signal modeling via language-aligned semi-supervised learning
- **作者**: Ziman Ye、Muyun Jiang、Jiaqi Zhu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109544
- **发表**: 2026-08-22
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109544

## 一句话概括
USEA以冻结语言模型编码任务标签语义，将有标签EEG与无标签EEG纳入同一半监督表征学习框架，提升跨数据集、跨任务的统一建模能力。

## 问题与动机
EEG在设备、被试和任务间差异明显，现有基础模型多采用先自监督预训练、再逐任务监督微调的流程，容易依赖任务专属分类头并适应单一数据集。不同任务的标签语义也未充分用于跨任务对齐。

## 方法
USEA共享单一EEG骨干，不为每个任务配置专属分类头。有标注样本的标签文本由冻结语言模型编码，作为语义目标与EEG表示按余弦相似度对齐；无标签数据则通过自回归重建EEG token进行自监督学习。统一优化使全标注、少标注和无标注数据可共同训练。

## 实验与结果
论文在BCIC-IV-2a、OpenBMI-MI、SEED及其他运动想象、情绪识别和稳态视觉诱发数据集评估平衡准确率与Kappa。标签文本正确对应时，BCIC-IV-2a平衡准确率/Kappa为0.6502/0.5336，SEED为0.7245/0.6018；打乱文本对应后分别降至0.2512/0.0016及0.3341/0.0015，支持语义对齐确有作用。

## 贡献与局限
方法以语言语义作为跨任务监督桥梁，并让不同标签量的数据共享同一表征骨干。研究主要在实验室采集EEG上验证；作者指出极少通道的可穿戴设备需要适配，因此对低通道、噪声更强的真实场景泛化仍不确定。

---
DOI: 10.1016/j.neunet.2026.109544
