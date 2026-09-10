# V-Sparse: From temporal-spatial visual semantic compression to coarse-to-fine interaction for text-video retrieval 总结

## 基本信息
- **标题**: V-Sparse: From temporal-spatial visual semantic compression to coarse-to-fine interaction for text-video retrieval
- **作者**: Xin Liu, Shibai Yin, Jun Wang, Wei Li, Xingyang Wang, Jiaxin Zhu, Yubing Shen, Yee-Hong Yang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108982
- **PDF**: [NN_2026_VSparse.pdf](papers/NN_2026_VSparse.pdf)

## 一句话概括
V-Sparse 通过文本引导的时空视觉语义压缩和粗到细交互提升文本到视频检索。

## 问题与动机
文本短而视频视觉信息丰富，仅计算整体相似度难以高精度匹配。CLIP 类方法仍受到视觉冗余和模态信息量不平衡影响。

## 方法
Temporal VSC 在帧级、Spatial VSC 在 patch 级压缩视觉特征，减少冗余并保留查询相关语义。CFI 模块联合对齐句子—帧、句子—patch 和词—patch。

## 实验与结果
六个基准数据集实验报告 V-Sparse 在文本视频检索上取得 state-of-the-art 结果；摘要截取未给出具体 Recall 数字。

## 贡献与局限
贡献是把语义压缩和多粒度交互放入统一框架。局限是压缩可能误删关键线索，大规模索引延迟和域外视频适应性仍需评估。

---
DOI: 10.1016/j.neunet.2026.108982
