# BCMDA: Bidirectional correlation maps domain adaptation for mixed domain semi-supervised medical image segmentation

## 基本信息

- 标题: BCMDA: Bidirectional correlation maps domain adaptation for mixed domain semi-supervised medical image segmentation
- 作者: Bentao Song, Jun Huang, Qingfeng Wang
- 期刊 / 会议: Neural Networks 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1016/j.neunet.2026.108877
- PDF: [NN_2026_BCMDA.pdf](papers/NN_2026_BCMDA.pdf)

- 标题: BCMDA: Bidirectional correlation maps domain adaptation for mixed domain semi-supervised medical image segmentation
- 作者: Bentao Song, Jun Huang, Qingfeng Wang
- 期刊 / 会议: Neural Networks 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

作者为 Bentao Song、Jun Huang、Qingfeng Wang；发表于 *Neural Networks* 201 (2026) 108877。论文研究混合域半监督医学图像分割（MiDSS），实验覆盖眼底、前列腺、心脏 MRI 和 Synapse 腹部 CT 数据。DOI: 10.1016/j.neunet.2026.108877
## 一句话概括

BCMDA 通过双向相关图生成虚拟标注/未标注样本，并将约束一致性混合、双向原型对齐和伪标签纠正结合起来，缓解多中心域偏移与少标签下的确认偏差。

## 问题与动机

医学分割中的不同医院、设备和扫描协议造成明显域偏移，而目标域标注通常很少。普通半监督方法会把错误伪标签反复用于训练，形成确认偏差；只做单向域适配也不能充分利用源域和目标域的结构关系。论文希望在不依赖大量目标标注的情况下，同时利用跨域相关性和类别原型提升稳定性。

## 方法

BCM（Bidirectional Correlation Maps）从源/目标特征的双向相关关系生成虚拟标注和未标注图像。KTVDB 模块用 FixMix、PDMix 以及双向 BCMix/DBCMix 进行约束一致性训练；PAPLC 模块采用带可学习原型的余弦相似度分类器，通过 BPA（双向原型对齐）减少类别原型偏移，再由 PPLC（伪标签原型学习纠正）筛除或修正不可靠伪标签。整体通过学生/教师式半监督目标和跨域原型约束共同优化。

## 实验与结果

在 Fundus 四中心的 20 个标签设置下，BCMDA Dice 为 88.95±0.15、Jaccard 为 81.03±0.22、95HD 为 7.21±0.11、ASD 为 3.45±0.03，Dice 高于 SymGD 的 87.20。Prostate 六机构的 20 标签 Dice 为 86.88±0.15（SymGD 75.89±1.36），40 标签时为 88.36，高于其 88.28 的上界基线；M&Ms 20 标签 Dice 为 85.78，5 标签仍为 82.30（SymGD 77.78）。Synapse 20% 标签时 Dice 为 71.20±0.4、ASD 为 1.65，优于 S&D 的 68.38、GenericSSL 的 60.88 和 DHC 的 48.61。消融显示各模块均有帮助，PPLC 改善最明显；显存约 4.79 GB，高于 SymGD 的 4.07 GB，但单 epoch 和单迭代更快。

## 贡献与局限

贡献是将双向相关图、约束混合和原型级伪标签校正统一到混合域半监督分割框架中，并在多模态、多中心数据上验证。局限是虚拟图像可能改变像素语义或造成纹理模糊，显存需求有所增加；当前仍需更多真实临床域、不同模态和更强标签稀缺场景验证。未来应改善图像合成质量并扩展到 CT/MRI 等多模态设置。

DOI: 10.1016/j.neunet.2026.108877
