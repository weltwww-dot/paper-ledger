# DA-S2RL: Disease-aware shared-specific representation learning for heterogeneous image-EHR Alzheimer’s disease diagnosis 总结

## 基本信息
- **标题**: DA-S2RL: Disease-aware shared-specific representation learning for heterogeneous image-EHR Alzheimer’s disease diagnosis
- **作者**: Wei Wang、Yu Shi、Juan Cheng、Yu Liu
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），109760；2027为卷期年份，不替代2026年在线首发
- **发表**: 2026-10-19
- **日期来源**: 正式PDF首页Available online 19 October 2026
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109760
- **PDF**: [NN_2026_DAS2RLAlzheimerDiagnosis.pdf](papers/NN_2026_DAS2RLAlzheimerDiagnosis.pdf)

## 一句话概括
DA-S2RL把脑影像与结构化病历组织为共享疾病语义和模态特异诊断残差，减少直接拼接造成的冗余，用于阿尔茨海默病相关分类。

## 问题与动机
影像呈现脑结构或代谢特征，病历记录症状与行为，两者既有共同信息，也有各自的诊断线索。简单融合可能混淆这些角色，因此论文希望在对齐跨模态信息的同时保留互补线索。

## 方法
分别编码影像和病历，在ADNI中先融合MRI与PET，再由SCC模块分离共享表示与特异残差。疾病标签条件化的对比学习促进共享语义对齐，互信息约束抑制冗余，双向注意力细化两类表示，最后融合影像、病历和联合分支的预测。

## 实验与结果
筛选并对齐后，ADNI保留300名受试者、NACC保留650名，每人仅一条多模态样本。AD/MCI/CN三分类的固定受试者划分准确率为93.48%、93.81%；五次随机种子实验的平均准确率为91.74%±1.82%、91.34%±2.01%，与单次成绩应分开理解（PDF第5—7页，表1—5）。NACC使用多序列MRI与病历，不含PET。

## 贡献与局限
通过共享—特异表示和分支消融，研究异质医疗信息的互补性，并用SHAP与影像热图辅助解释。实验要求完整且时间匹配的多模态输入，排除了缺失样本；两个队列分别评估，不是未经再训练的跨中心迁移或前瞻临床验证。解释结果反映模型关联，不能据此确立病因、治疗效果或临床可用性（PDF第5、7—11页）。

---
DOI: 10.1016/j.neunet.2026.109760 | PDF: [NN_2026_DAS2RLAlzheimerDiagnosis.pdf](papers/NN_2026_DAS2RLAlzheimerDiagnosis.pdf)
