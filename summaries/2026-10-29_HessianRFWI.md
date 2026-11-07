# Rethinking neural network reparameterized full waveform inversion: A Hessian perspective 总结

## 基本信息
- **标题**: Rethinking neural network reparameterized full waveform inversion: A Hessian perspective
- **作者**: Peng Jiang、Sihan Chen、Yuxiao Ren 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109806
- **发表**: 2026-10-29
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109806
- **PDF**: [NN_2026_HessianRFWI.pdf](papers/NN_2026_HessianRFWI.pdf)

## 一句话概括
用海森矩阵谱解释神经网络重参数化如何稳定全波形反演，并据此改进收敛与抗扰动能力。

## 问题与动机
全波形反演对初始模型和局部极小值敏感。神经网络重参数化带来的隐式约束可缓解这些问题，但哪些方向受到约束、为何会影响高频细节拟合，需要从优化过程解释。

## 方法
作者分析迭代中海森矩阵的谱及特征向量，发现重参数化倾向于沿由低频信息主导的大特征值方向更新。为加快收敛，先用Adam形成稳定的低频模型，再用L-BFGS加快高频拟合。为提高稳健性，另以海森矩阵的迹正则化目标函数。

## 实验与结果
在声学Marmousi及Overthrust合成模型上，混合优化器改善了细节拟合，海森迹正则在所测扰动条件下获得更稳定的反演结果（PDF第5、13–16页）。

## 贡献与局限
建立了网络重参数化、曲率与反演频率成分的联系。估计海森迹增加计算开销，合成声学实验对真实地震数据及更复杂物理模型的外推仍需验证。

---
DOI: 10.1016/j.neunet.2026.109806 | PDF: [NN_2026_HessianRFWI.pdf](papers/NN_2026_HessianRFWI.pdf)
