# Rethinking Multi-Modal Image Super-Resolution: The Key Role of Cross-Modal Consistency Prior 总结

## 基本信息
- **标题**: Rethinking Multi-Modal Image Super-Resolution: The Key Role of Cross-Modal Consistency Prior
- **作者**: Jingyi Xu、Xin Deng、Yutong Wang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15330-15346
- **发表**: 2026-08-13
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3723450

## 一句话概括
TLCNet 以更贴合跨模态高频差异的 T 分布一致性先验和空间自适应退化模型，提升多模态图像超分辨率的细节恢复。

## 问题与动机
如何从高分辨率引导模态中提取有益边缘信息，同时避免模态差异带来的伪纹理，并适应非均匀退化？

## 方法
作者先分析引导图像与目标图像拉普拉斯响应的模态差异，提出 T 分布多模态一致性先验（TMC），再用逐元素乘性的退化矩阵刻画空间变化的低分辨率成像过程。随后将 ADMM 优化步骤展开为可学习的 TLCNet，使先验和退化参数共同参与迭代重建。

## 实验与结果
实验覆盖 RGB 引导深度、全色锐化和 RGB 引导热成像三类任务、9 个数据集。模态差异在九个数据集上均更符合 T 分布拟合而非高斯或拉普拉斯拟合（PDF 第 4 页）；RGB-D 任务中，TLCNet 相对次优方法的平均 RMSE 在 4×、8×、16× 放大下分别降低 0.08、0.14、0.23（PDF 第 8 页）。在 RGB-D-D 的 16×测试上，RMSE 从 RSAG 的 2.49 降至 2.37，推理约快 5.9 倍（PDF 第 15 页）。

## 贡献与局限
贡献在于把实测的重尾跨模态差异转化为一致性先验，并以可解释展开网络统一处理多种模态任务。局限是实证集中于三类超分辨率任务及所选数据集，尚不能据此断言其他模态或成像条件下同样有效。

---
DOI: 10.1109/tpami.2026.3723450
