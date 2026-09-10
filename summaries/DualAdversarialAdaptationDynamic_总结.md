# Dual Adversarial Adaptation With Dynamic Labeling Mechanism for Semisupervised Cross-Well Lithology Identification 总结

## 基本信息

- **标题**: Dual Adversarial Adaptation With Dynamic Labeling Mechanism for Semisupervised Cross-Well Lithology Identification
- **作者**: Ji Chang, Jing Li, Tao Shen, Dewen Liang, Yunbo Zhao, Shaoqun Dong, Yu Kang, Wenjun Lv
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TAI.2026.3679484
- **arXiv**: 无
- **PDF**: [TAI_2026_DualAdversarialAdaptationDynamic.pdf](papers/TAI_2026_DualAdversarialAdaptationDynamic.pdf)

## 一句话概括

论文提出带动态标注机制的双对抗域适配方法，通过同时处理井内类别分布差异和跨井域差异，在目标井仅有少量标注时提升岩性识别能力。

## 问题与动机

跨井岩性识别同时面临标签稀缺、不同井测井分布不一致以及同一口井中不同地层的井内分布 divergence。只做跨井对齐会把同井内不同类别混在一起，固定伪标签阈值又容易在训练早期引入错误监督。作者因此希望在减少两类分布差异的同时，动态选择可信目标伪标签并强调与目标井相似的源样本。

## 方法

共享特征提取器由一维卷积和通道注意力组成。井内对抗模块为每个岩性类别设置类别判别器，用分类概率软分配未标注目标样本；跨井对抗模块通过域判别器学习域不变表示。动态标签调整包含两部分：全局阈值和类别阈值随目标域平均置信度逐步更新，筛选可靠伪标签；预训练独立域判别器估计源样本相对目标域的密度比，对相似源样本加权。总损失联合源分类、加权跨域适配、井内适配和伪标签损失。

## 实验与结果

实验使用中国东部油田六口真实勘探井、六条测井曲线，每个样本包含沿深度方向的 33 个点；目标井默认仅取各类别 10% 标注，并以宏平均召回率评价。A→B 和 B→A 的宏召回率分别为 86.44% 和 91.67%；C→D 和 D→C 分别为 90.15% 和 83.97%。摘要报告在目标井仅有 10% 标签时，相比现有方法平均提高 12.6% 的宏平均召回率。标签比例降到 5% 和 1% 时性能虽下降，但方法保持最佳或次佳；消融实验中逐步加入跨井、井内、动态伪标签和源重加权模块，完整模型表现最好。

## 贡献与局限

贡献包括：将井内类别对齐与跨井域适配统一到双对抗框架；以动态全局/类别阈值和源样本重加权改善伪标签质量与训练稳定性；在真实井场数据和极低标注比例下验证有效性。局限是数据来自单一油田区域，跨盆地、跨仪器和更多岩性类别的泛化尚未充分验证；混合地层和类别不平衡仍导致白云岩等少数类易被误分，作者也提出后续需加强类别不平衡建模。

---
DOI: 10.1109/TAI.2026.3679484
