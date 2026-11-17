# Fast multipole attention: A scalable multilevel attention mechanism for text and images 总结

## 基本信息
- **标题**: Fast multipole attention: A scalable multilevel attention mechanism for text and images
- **作者**: Yanming Kang、Giang Tran、Hans De Sterck
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109847
- **发表**: 2026-11-05
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109847
- **PDF**: [NN_2026_fast-multipole-attention_109847.pdf](papers/NN_2026_fast-multipole-attention_109847.pdf)
- **开放许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · 出版社原件，未经修改

## 一句话概括
快速多极注意力以分层表示近邻与远距离交互，将自注意力的时间复杂度降至 O(n log n)、内存复杂度降至 O(n)，并在文本与视觉基准上取得有竞争力的结果。

## 问题与动机
如何在保留全局上下文交互的同时，缓解长序列和高分辨率输入下标准自注意力的二次复杂度？

## 方法
FMA 采用受快速多极方法启发的分治层级：近距离 token 保持细粒度交互，远距离 token 通过逐层变粗的可学习基函数交互；论文分别实现一维文本版本和二维视觉版本。

## 实验与结果
作者在自回归与双向语言建模，以及图像分类和语义分割基准上比较高效注意力方法；一维版本在显著降低内存使用时匹配或超过部分基线，二维版本在报告的视觉任务上优于强视觉 Transformer 基线（PDF 第 7–13 页）。这些结论依赖具体基准和实现，不能直接推出所有任务均无精度损失。

## 贡献与局限
研究提出可扩展到文本与图像的多层注意力机制，并给出其复杂度分析和经验验证；不同数据规模、硬件与任务上的收益仍需独立评估。

---
DOI: 10.1016/j.neunet.2026.109847 | PDF: [NN_2026_fast-multipole-attention_109847.pdf](papers/NN_2026_fast-multipole-attention_109847.pdf)
