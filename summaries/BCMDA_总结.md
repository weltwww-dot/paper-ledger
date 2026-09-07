# BCMDA: Bidirectional correlation maps domain adaptation for mixed domain semi-supervised medical image segmentation 总结

## 基本信息

- **标题**: BCMDA: Bidirectional correlation maps domain adaptation for mixed domain semi-supervised medical image segmentation
- **作者**: Bentao Song, Jun Huang, Qingfeng Wang
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108877
- **arXiv**: 2603.24691
- **PDF**: [NN_2026_BCMDA.pdf](papers/NN_2026_BCMDA.pdf)

## 一句话概括

针对混合域半监督医学图像分割（MiDSS）的域偏移与确认偏差问题，提出 BCMDA 框架：用双向相关图构建虚拟域桥接知识迁移，并结合可学习原型余弦相似度分类器做双向原型对齐与伪标签校正。

## 问题与动机

传统半监督医学图像分割（SSMS）假设标注与未标注数据同分布，但现实中标注数据往往来自单一机构、未标注数据来自多中心/多扫描设备，存在明显的域间分布差异（domain shift），即 MiDSS 场景。该场景有两个核心难点：(1) 标注与未标注数据分布差异阻碍知识迁移；(2) 未标注数据学习效率低导致严重的确认偏差（confirmation bias）。既有方法均有不足：UDA 假设源域标注充足，LE-UDA 只支持单一未标注目标域，首个 MiDSS 方法 SymGD 采用单向傅里叶变换与统一 copy-paste 构造中间域，但变换后数据仍与未标注数据差异较大，且未处理确认偏差。

## 方法

基于 Mean Teacher 架构（U-Net 骨干、EMA 更新教师网络）提出双向相关图域自适应（BCMDA），包含两大组件。**KTVDB（虚拟域桥接知识迁移）**：先由教师网络特征计算标注与未标注图像间的双向相关图（BCM），用相关图引导的图像合成（CIS）互相用对方像素合成图像；合成图与原图按固定比例 MixUp（FixMix）构成分布对齐的虚拟域数据，并用渐进动态 MixUp（PDMix，混合比随训练进度自适应）构造动态虚拟标注数据；随后执行双重双向 CutMix（DBCMix）：先在固定虚拟域内做初始知识迁移，再在动态虚拟标注数据与强增广真实未标注数据间做逐步迁移。**PAPLC（原型对齐与伪标签校正）**：以可学习原型余弦相似度（CosSim）分类器替代随机分类器，构造虚拟域/真实域两个分类器并做双向原型对齐（BPA），获得更平滑紧凑的特征；再以 CosSim 分类器的高置信预测生成校正掩码来修正 Linear 分类器的预测（PPLC），缓解确认偏差。训练用 Lce+Ldice 掩码损失，监督信号取虚拟与真实未标注预测的平均；推理仅用学生网络的 Linear 分类器。

## 实验与结果

在 Fundus（4 域，视杯/视盘）、Prostate（6 机构，T2 MRI 前列腺）、M&Ms（4 厂商 MRI，LV/MYO/RV 心腔）三个公共多域数据集上评测，并额外在 Synapse 3D 腹部多器官（13 类器官）上验证泛化性；指标含 Dice、Jaccard、ASD、95HD。仅 20 张标注时：Fundus 平均 Dice 88.95%、Jaccard 81.03%、95HD 7.21mm、ASD 3.45mm，比 SOTA SymGD（Dice 87.20%）高 1.75%，甚至超上界（88.45%）0.5%；Prostate 20 张标注 Dice 86.88%，比 SymGD 75.89% 高 10.99%，40 张时 Dice 88.36% 超过上界 88.28%；M&Ms 20 张标注 Dice 85.78%、ASD 1.75mm，5 张标注时仍有 Dice 82.30%，比 SymGD 高 4.52%。Synapse（20% 标注）平均 Dice 71.20%、ASD 1.65mm，优于 S&D-Messenger（68.38%）、GenericSSL（60.88%）与 DHC（48.61%）。全部对比 p 值 < 0.01。消融显示 FixMix+PDMix、BPA、PPLC 各组件均有效，替换为 FDA 增益有限；PPLC 生成的伪标签质量与稳定性最高。复杂度上 BCMDA 每轮 70.88s、显存 4.79GB，优于 SymGD（101.31s、4.07GB）。

## 贡献与局限

- 提出新型 MiDSS 域自适应框架 BCMDA，利用双向相关图（BCM）做标注/未标注数据的双向分布对齐，缓解域偏移。
- 提出 KTVDB：BCM 合成数据经 FixMix 与 PDMix 构建对齐虚拟域，并以双重双向 CutMix（DBCMix）实现高效的知识桥接迁移。
- 提出 PAPLC：基于 CosSim 分类器的双向原型对齐（BPA）兼顾原型获取与特征对齐，原型伪标签校正（PPLC）显著缓解确认偏差。
- 三个公共多域数据集全面超越 SOTA，并在 3D Synapse 上验证了可扩展性，极少标注下仍稳定。
- 局限：图像合成依赖跨图像相关性，对困难样本可能误读像素语义、产生结构错误与模糊纹理，进而影响分割；未来拟生成更高质量特征图、细化合成流程，并探索 CT/MRI 等多模态成像间的域自适应。

---
DOI: 10.1016/j.neunet.2026.108877
