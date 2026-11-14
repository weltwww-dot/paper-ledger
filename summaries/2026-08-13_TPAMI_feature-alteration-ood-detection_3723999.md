# Feature-Alteration Robustness for Out-of-Distribution Detection 总结

## 基本信息
- **标题**: Feature-Alteration Robustness for Out-of-Distribution Detection
- **作者**: Xue Jiang、Feng Liu、Zhen Fang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15112-15124
- **发表**: 2026-08-13
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3723999

## 一句话概括
FAR 利用模型对分布内特征扰动后仍保持稳定、而分布外特征偏离更明显的现象进行分布外样本检测。

## 问题与动机
能否直接利用预训练骨干网络中间特征对有界扰动的响应差异，识别分布外输入并与已有检测分数互补？

## 方法
FAR 在中间特征图上施加受控特征变换，再比较前景与背景响应偏差形成检测分数；论文分析了该分数与前景—背景差异的关系，并将 FAR 与已有分类器分数及特征后处理方法融合。

## 实验与结果
实验在 ImageNet、CIFAR 和 Waterbirds 等分布外检测基准上比较多种分数与骨干网络。ImageNet-1K 上，FAR+ASH 在四个 OOD 测试集平均 AUROC 为 95.97%、FPR95 为 19.56%；作者还报告其对背景相关伪相关场景有效（PDF 第 7、10 页）。扩展到检测和分割骨干的结果仅作为图像级预筛查的探索性证据，论文明确不主张像素级或实例级泛化（PDF 第 10–11 页）。

## 贡献与局限
贡献是提出面向中间特征图的防御性 OOD 检测信号，并展示其与已有方法组合的互补性。局限是检测需要额外特征处理和后续层计算，作者报告推理延迟约增加 7%、理论 FLOPs 增加约 19.8%；非分类骨干上的结果也尚不足以证明任务级泛化（PDF 第 9–11 页）。

---
DOI: 10.1109/tpami.2026.3723999
