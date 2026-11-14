# Robust Audio-Visual Question Answering With Missing Modality in Training and Testing 总结

## 基本信息
- **标题**: Robust Audio-Visual Question Answering With Missing Modality in Training and Testing
- **作者**: Jinxing Zhou、Zhangbin Li、Di Hu 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15347-15364
- **发表**: 2026-08-13
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3723653

## 一句话概括
该研究针对训练和测试阶段都可能缺失音频或视觉输入的音视频问答，提出先重建缺失模态、再预测答案的两阶段框架。

## 问题与动机
当训练和推理样本都可能缺少音频、视觉或两者时，如何在不依赖完整模态配对监督的情况下维持问答性能？

## 方法
第一阶段根据现存模态和问题文本重建缺失特征：密集时间尺度重建模块融合多粒度信息，多模态依赖建模模块捕捉音频、视觉与问题之间的关系；关系对比学习和跨样本伪标签为重建提供监督。第二阶段冻结重建网络并接入既有 AVQA 主干完成答案预测。

## 实验与结果
作者从 MUSIC-AVQA、MUSIC-AVQA-R 和 AVQA 构造训练及测试均含模态缺失的评测版本，并比较多种 AVQA 主干和缺失率。在 MUSIC-AVQA-TM 的不同缺失情形下，方法整体优于把缺失特征置零的完整模态基线和 LTR；随缺失率上升，两类方法性能都会下降（PDF 第 11 页）。下游音视频识别中，AVEL 和 PSP 主干分别达到 65.6% 和 68.1% 准确率，较直接处理缺失输入高 16.3 和 16.9 个百分点（PDF 第 15 页）。

## 贡献与局限
贡献是将模态重建与问答主干分阶段训练，并用跨模态关系和伪目标缓解缺失模态没有真实特征标签的问题；作者还展示了其在音视频识别上的迁移潜力。局限是评测由现有数据集构造的缺失模态版本完成，真实设备失效及更复杂缺失机制仍需验证。

---
DOI: 10.1109/tpami.2026.3723653
