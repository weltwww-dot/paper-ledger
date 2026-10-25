# Super-resolution for reliable industrial inspection under mixed degradations 总结

## 基本信息
- **标题**: Super-resolution for reliable industrial inspection under mixed degradations
- **作者**: Deyuan Mi、Ling Li、Donghao Miao、Taoxi Zhu、Yaping Jia
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），109787；2027为卷期年份，不替代2026年在线首发
- **发表**: 2026-10-18
- **日期来源**: 正式PDF首页Available online 18 October 2026
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109787
- **PDF**: [NN_2026_MixedDegradationIndustrialSR.pdf](papers/NN_2026_MixedDegradationIndustrialSR.pdf)

## 一句话概括
SynSR把结构先验和伪影抑制引入超分辨率重建，研究如何在混合退化下保留有助于工业缺陷定位的细节，而不只追求图像清晰。

## 问题与动机
模糊、噪声、压缩和分辨率损失会掩盖细小缺陷，重建产生的锐化纹理又可能被误识别为异常。较高的重建质量分数，因此未必带来更可靠的下游检测。

## 方法
从低分辨率输入提取Sobel与Laplacian结构响应，用PriorGate调节注意力特征更新，并通过AOR-Conv的空间—通道门控抑制不稳定响应。各超分前端在相同测试退化下比较；PatchCore和DeSTSeg架构保持不变，但分别使用对应重建后的正常样本训练。

## 实验与结果
在MVTec AD与MPDD上进行合成混合退化评估。中等退化、4倍超分时，DeSTSeg的PRO分别为0.9411和0.9719，高于双三次上采样的0.9084和0.9102；这属于区域定位指标，不是图像分类准确率。MVTec AD关闭已知退化参数条件后，PRO仍为0.9375，但各项指标并非全面领先（PDF第5—6、9—10页，表5、8）。

## 贡献与局限
把重建伪影控制与下游定位共同纳入评估，但结构先验并不直接识别缺陷，低对比异常仍可能被弱化。退化全部由人工合成，基线主要直接使用官方预训练权重，不能将结果解释为相同训练预算下的全面优势，更不能直接外推至自然退化产线或部署可靠性（PDF第5、10页）。

---
DOI: 10.1016/j.neunet.2026.109787 | PDF: [NN_2026_MixedDegradationIndustrialSR.pdf](papers/NN_2026_MixedDegradationIndustrialSR.pdf)
