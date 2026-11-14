# Adversarial Purification by Consistency-Aware Latent Space Optimization on Data Manifolds 总结

## 基本信息
- **标题**: Adversarial Purification by Consistency-Aware Latent Space Optimization on Data Manifolds
- **作者**: Shuhai Zhang、Jiahao Yang、Hui Luo 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，14681-14698
- **发表**: 2026-08-14
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1109/tpami.2026.3720823

## 一句话概括
本文提出 CMAP，通过在预训练一致性模型的潜空间中优化生成样本，恢复输入的干净数据结构并提升分类器面对对抗扰动时的稳健性。

## 问题与动机
生成式净化需要消除输入中的对抗性偏差，同时保留图像的语义与结构；净化过强会改变干净样本，净化不足则难以恢复有效分类特征。

## 方法
CMAP 利用一致性模型的一步确定性生成，在多个潜向量上联合优化像素与感知一致性，并约束潜向量集合的均值、方差接近模型的先验分布。最终对多个生成结果进行预测投票，以降低单个潜向量偏离数据流形所带来的影响。

## 实验与结果
作者在 CIFAR-10 与 ImageNet-100 上与对抗训练和净化基线比较，并评估多种标准强度与较高强度扰动。高强度设置下，论文报告 CMAP 相对所比较净化基线的鲁棒准确率提升为 43.43%–46.93%（L∞）及 6.33%–8.24%（L2）（PDF 第12页）；在 ImageNet-100 的净化图像保真度比较中，CMAP 的 SSIM 为 0.847，高于最佳基线的 0.784（PDF 第12页）。论文亦指出，面向此类生成净化框架的更强专用白盒评估仍有待研究（PDF 第10页）。

## 贡献与局限
该方法用一致性生成和多样本投票改善所测场景的鲁棒性及结构保真。推理成本受采样数和优化过程影响，针对防御自适应改变的威胁仍需更充分评估。

---
DOI: 10.1109/tpami.2026.3720823
