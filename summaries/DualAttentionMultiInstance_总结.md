# Dual Attention Multi-Instance Learning for Identifying Autism Spectrum Disorder Using Resting-State fMRI

## 基本信息

- **标题**：Dual Attention Multi-Instance Learning for Identifying Autism Spectrum Disorder Using Resting-State fMRI
- **作者**：S. Qasim Abbas、Lianhua Chi、Feng Xia、Noorul Amin、Yi-Ping Phoebe Chen
- **期刊 / 会议**：IEEE Transactions on Artificial Intelligence 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tai.2026.3669876
- **arXiv**：无
- **PDF**：[TAI_2026_DualAttentionMultiInstance.pdf](papers/TAI_2026_DualAttentionMultiInstance.pdf)

## 一句话概括

本文提出双重注意力多实例学习框架 DAMILF，从静息态 fMRI 的局部功能连接模式中自动筛选高信息量脑区，并同时建模脑区内部与脑区之间的重要性，以提升自闭症谱系障碍诊断及亚型识别的泛化能力。

## 问题与动机

自闭症谱系障碍的功能连接异常通常只出现在部分脑区，而多站点 fMRI 数据又存在扫描仪、采集协议、年龄和个体差异带来的异质性。直接使用全脑数据会引入大量不相关区域，依赖固定脑图谱或预先标注 patch 也可能限制跨站点泛化；另一方面，患者级标签并不能告诉模型哪一个局部 patch 真正携带诊断信息。论文因此把每个受试者的多个脑部 patch 视为一个多实例 bag，在没有 patch 级标注的情况下，学习可解释的局部—全脑功能连接表征。

## 方法

作者先对 ABIDE-1 静息态 fMRI 做 CPAC 预处理，将四维时间序列转换为基于 Kendall 协调系数的三维功能连接统计图，并结合数据驱动地标和模板膨胀筛选信息丰富的区域。输入裁剪为 60×60×60 体素，再划分为 84 个 15×15×15 patch，保留地标数超过 50 的 8 个 patch。每个 patch 经过四层三维卷积网络和 patch 级空间注意力子网络，提取局部连接特征并计算 patch 分数；注意力感知特征图模块再根据 patch 重要性与相互关系进行跨 patch 加权和全局池化；最后由受试者级子网络完成 ASD/典型控制分类或 ASD 亚型预测。两个注意力层分别关注 patch 内的异常连接位置与不同 patch 对全脑判别的相对贡献。

## 实验与结果

实验使用 ABIDE-1 的 17 个站点，按平均帧位移小于 0.2 mm 筛选出 884 名受试者，其中 408 名 ASD、476 名典型控制者；采用十折交叉验证，并以准确率、敏感度、特异度和 AUC 评价二分类。DAMILF 的 ACC 为 0.8556、SEN 为 0.8553、SPE 为 0.8560、AUC 为 0.9201，三个随机种子的标准差分别约为 0.0018、0.0021、0.0016 和 0.0024；留一站点交叉验证的全站点平均 ACC、SEN、SPE、AUC 分别为 0.8115、0.8183、0.8047 和 0.8193。ASD 亚型识别的宏平均分类准确率为 0.9038，宏 F1 为 0.8539，平衡准确率为 0.8557。消融实验显示，数据驱动地标筛选、功能连接统计图以及空间注意力和跨 patch 注意力均有贡献；仅保留自适应 patch 加权时 ACC 为 0.8329，加入双重注意力后升至 0.8556。

## 贡献与局限

论文把数据驱动脑区筛选、功能连接统计表征和双层注意力 MIL 结合起来，在不需要 patch 级人工标注的情况下获得了可解释的局部—全脑诊断线索，并通过留一站点实验检验了跨扫描站点泛化。局限在于主要验证数据来自 ABIDE-1，部分站点样本很小，站点差异和预处理选择仍可能影响结果；亚型中的 PDD-NOS 样本存在明显标签重叠，模型不能替代临床诊断。未来还需要独立多中心队列、前瞻性临床验证以及更稳健的跨域校准来确认其临床可用性。

---
DOI: 10.1109/tai.2026.3669876
