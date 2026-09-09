# Hybrid Convolution Reparameterization for Efficient Deep Learning-Based Nonprecipitation Echo Recognition and Removal 总结

## 基本信息

- **标题**: Hybrid Convolution Reparameterization for Efficient Deep Learning-Based Nonprecipitation Echo Recognition and Removal
- **作者**: Jianwei Si、Lei Han、Lejian Zhang、Chuanxin Li
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3675666
- **arXiv**: 无
- **PDF**: [NN_2026_HybridConvolutionReparameterizationEfficient.pdf](papers/NN_2026_HybridConvolutionReparameterizationEfficient.pdf)

## 一句话概括

本文提出 RepNPE-Net 及混合卷积重参数化技术 HCR，利用双流卷积与位置高效局部注意力识别并去除天气雷达中的非降水回波，同时在推理阶段显著降低计算开销。

## 问题与动机

地物杂波、海杂波和电磁干扰会在天气雷达反射率图像中产生非降水回波，造成降水范围和强度误判。已有深度学习方法能够改善识别效果，但通常计算量较大；已有重参数化方法又主要处理并行多分支结构，对深度可分离卷积与逐点卷积组成的多卷积结构融合不足。作者因此希望在保持去回波准确率的同时，获得适合大范围气象业务部署的轻量推理网络。

## 方法

RepNPE-Net 包含重参数化双流卷积模块 RepDCM 和重参数化注意力双流卷积模块 RepADCM，分别融合普通卷积与深度可分离残差卷积，以提取互补的局部与全局空间特征。RepADCM 中加入位置高效局部注意力（PELA）块，使网络更多关注具有气象意义的空间位置。HCR 在训练阶段保留多分支、多卷积结构，在推理阶段将深度卷积、逐点卷积及分支结构折叠为等价的单卷积，从而降低参数量和推理时间。

## 实验与结果

实验使用 FY-4A 静止气象卫星亮温观测，并结合雨量站、RCR 和 CREF 等资料建立非降水回波识别与去除数据。与 RepViT 基线相比，RepNPE-Net 的准确率提高 0.022，召回率和 POD 均提高 0.058，CSI 提高 0.045，HSS 提高 0.046；消融实验显示，双流卷积、PELA 和 HCR 逐步加入后多数指标持续改善。跨区域测试表明，在上海区域训练、山东区域直接应用时，模型除 FAR 和 PREC 外的多数指标优于对比网络。推理阶段网络平均时间由未重参数化版本的 2.78 秒降至 1.88 秒，覆盖中国区域的总处理时间为 5.28 小时。

## 贡献与局限

- 提出面向非降水回波识别与去除的 RepNPE-Net，将双流卷积、PELA 注意力和结构重参数化统一到一个网络中。
- 提出 HCR，使深度可分离卷积和多分支、多卷积结构能够在推理阶段融合为等价单卷积，兼顾精度与部署效率。
- 在多项分类指标、跨区域泛化和整国区域处理时间上验证了方法的实用价值。
- 局限：训练和验证数据主要来自中国上海、山东区域，气候与雷达条件的地域偏差可能限制全球泛化；作者计划引入 NOAA、ECMWF 等全球数据进一步验证。

---
DOI: 10.1109/tnnls.2026.3675666
