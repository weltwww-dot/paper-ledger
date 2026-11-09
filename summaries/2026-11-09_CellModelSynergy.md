# Multimodal cell foundation models require synergistic integration beyond alignment 总结

## 基本信息
- **标题**: Multimodal cell foundation models require synergistic integration beyond alignment
- **作者**: Till Richter、Eric Zimmermann、James Hall 等
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **卷期 / 文章号**: 完整在线版，待正式分页
- **发表**: 2026-11-09
- **日期来源**: Nature出版社Article网页citation_online_date；正文为完整在线版，待正式分页
- **内容状态**: 完整 · 已基于出版社完整在线版全文完成中文六段式总结，待正式分页
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01328-3
- **PDF**: [NMI_2026_CellModelSynergy.pdf](papers/NMI_2026_CellModelSynergy.pdf)

## 一句话概括
提出协同信息评分，检验细胞模型融合组织图像和基因表达后，能否获得超出最强单模态的任务信息。

## 问题与动机
大规模配对测量不足时，常把冻结的单模态编码器接到一个融合层。融合模型得分提高，可能只是保留了原有的共享信号。对于连接组织形态与基因表达的任务，两种测量有时提供的是互补线索。

## 方法
作者以部分信息分解为出发点，用线性探针估计融合表征相对最强单模态的收益，分类用宏平均F1，回归用决定系数。理论分析考察冻结编码器下的对齐目标为何偏向捕获线性冗余，以及它对非线性协同信号的限制。

## 实验与结果
作者在肺纤维化、发育期人胸腺和乳腺癌三套空间转录组数据上比较10种融合方法。胸腺的生态位分类中，DCCA和CoMM的协同信息评分分别为0.142和0.120，直接拼接为0.072。所测常规任务上，微调优势单模态更节省标注样本（PDF第4、8页）。

## 贡献与局限
提供了判断何时值得融合的诊断指标。实测评分依赖任务、冻结表征、线性探针与单模态基线。较低的评分只表明该配置下额外收益有限，较弱模态仍可能含有其他任务所需的生物信息。

---
DOI: 10.1038/s42256-026-01328-3 | PDF: [NMI_2026_CellModelSynergy.pdf](papers/NMI_2026_CellModelSynergy.pdf)
