# Dual-Tree Complex Wavelet Driven Hierarchical Spatial-Frequency Fusion Learning for Robust Deepfake Detection 总结

## 基本信息

- **标题**: Dual-Tree Complex Wavelet Driven Hierarchical Spatial-Frequency Fusion Learning for Robust Deepfake Detection
- **作者**: Rui Sun, Yifan Zhang, Xiaolu Yu, Meng Li, Jun Gao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-13
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 计算机视觉
- **DOI**: 10.1109/TDSC.2026.3712721
- **arXiv**: 无
- **PDF**: [TDSC_2026_HSFFDeepfakeDetection.pdf](papers/TDSC_2026_HSFFDeepfakeDetection.pdf)

## 一句话概括

论文将层次化空间—频率融合与双树复小波的多子带增强结合，学习不同尺度和方向上的伪造痕迹，以提升深度伪造检测在跨数据集场景中的鲁棒性。

## 问题与动机

生成模型不断提高伪造图像的逼真度，传统依赖明显纹理或边界的检测特征容易消失；不同生成器还会留下不同频率和方向的隐式痕迹。仅使用空间特征难以稳定识别跨域伪造，单独使用频率特征又可能缺少语义和方向信息。论文因此希望同时建模多尺度空间线索、频率异常和方向性伪造模式。

## 方法

作者提出层次化空间—频率融合模块 HSFF，通过多尺度特征提取和频率注意力，自适应融合不同层次的频率信息，突出跨尺度异常。进一步提出协同多子带增强 CMSE，将双树复小波变换与预训练视觉特征结合，显式建模六个方向子带之间的关系。两个模块共同形成空间—频率—方向联合表示，用于分类深度伪造内容。

## 实验与结果

论文在多个基准数据集上与多种先进方法比较，并开展消融实验。跨数据集测试中，在具有挑战性的 Celeb-DFv2 和 DFDC 上，方法分别取得 97.2% 和 89.1% 的 AUROC；结果表明，融合层次频率信息和方向子带后，模型对生成器变化和跨数据集分布差异更稳健。

## 贡献与局限

论文贡献了结合 HSFF 与 DTCWT 的联合空间—频率—方向检测架构，并将预训练视觉特征用于多子带协同建模，重点改善跨域泛化。局限在于模型仍依赖训练数据中的伪造分布和预训练视觉表示，对新型生成器、压缩和社交平台处理的迁移能力仍需更广泛验证；真实场景中的开放集检测和计算成本也值得进一步研究。

---
DOI: 10.1109/TDSC.2026.3712721
