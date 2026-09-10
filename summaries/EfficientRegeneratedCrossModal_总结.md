# An Efficient Regenerated Cross-Modal Hashing: Improving Existing Hash Codes With the Arbitrary Length 总结

## 基本信息

- **标题**: An Efficient Regenerated Cross-Modal Hashing: Improving Existing Hash Codes With the Arbitrary Length
- **作者**: Kaihang Jiang, Wai Keung Wong, Xiaozhao Fang, Weijun Sun, Guoxu Zhou, Shengli Xie, Xiaochun Cao
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 跨模态检索、多模态哈希
- **DOI**: 10.1109/TPAMI.2026.3688816
- **PDF**: [TPAMI_2026_EfficientRegeneratedCrossModal.pdf](papers/TPAMI_2026_EfficientRegeneratedCrossModal.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出 RCMH 作为现有跨模态哈希模型的高效增强模块，在不从头迭代重训的情况下，把已部署的 hash codes 转换为任意目标长度并提升图文检索质量。

## 问题与动机

传统跨模态哈希模型部署后通常固定 bit length；若要适应不同检索场景或改进效果，往往需要重新设计并训练模型，成本高且结果未必更好。现有 label enhancement 可能把原本为 0 的标签扩散为正值，线性共同子空间又难以保留图像的线性属性和文本的非线性属性，变量迭代还会增加训练时间和内存。因此需要利用既有代码进行低成本、任意长度的再生成。

## 方法

RCMH 先用保留原标签正负结构、引入负信息并融合多模态相似性的 label augmentation 构造增强标签矩阵；再以相似性矩阵监督 SMF，并通过正交投影将现有代码初始化到任意目标长度。随后对图像特征做线性正交重构、对文本特征用 tanh 非线性投影，逐样本比较两者与连续表示的相似度，以 competitive strategy 选择更合适的二值表示。最后再次使用 regenerate hashing term，在保留已有代码信息的同时生成最终代码。变量按闭式解顺序更新，仅非线性文本投影使用梯度下降，实验将 RCMH 迭代次数设为 1。

## 实验与结果

作者在 IAPR TC-12、MIR-Flickr、NUS-WIDE 和 MS-COCO 四个公开数据集上，与浅层和深层跨模态哈希方法比较 MAP、TOP@100、Precision-Recall 等指标，每个实验运行 10 次取平均。RCMH 在 IAPR TC-12 上相对基线的 MAP 与 TOP@100 约提升 2%，在 MIR-Flickr 的 MAP 提升约 1–2%，在 NUS-WIDE 上 MAP 最优但 TOP@100 个别设置低于 LADH，在 MS-COCO 上各项指标均有优势。将 RCMH 作为插件增强九个 SOTA 基线时，ALECH、WASH、DOCMH、LADH、ROHLSE 等约获得 5% 改进；从 16 到 128 bit 等转换实验表明性能主要取决于目标长度而非原长度。RCMH 迭代 1 次即可达到最佳 MAP，且训练时间和内存开销低于比较方法；竞争实验还显示非线性文本特征在多数样本对中被选中。

## 贡献与局限

贡献包括：提出无需全量迭代优化的任意 bit length 转换框架；以线性—非线性竞争重构保留模态特性；通过再生项稳定增强已有模型并降低成本。局限是效果仍受输入已有 hash codes 质量影响，NUS-WIDE 的 TOP@100 并非所有设置最优，且方法的主要验证依赖四个公开数据集和预提取特征；作者指出进一步结合深度端到端特征和更复杂真实场景仍值得研究。

---
DOI: 10.1109/TPAMI.2026.3688816
