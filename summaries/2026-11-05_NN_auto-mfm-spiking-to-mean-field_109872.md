# Automated derivation of mean field models from spiking neural networks for the simulation of brain dynamics 总结

## 基本信息
- **标题**: Automated derivation of mean field models from spiking neural networks for the simulation of brain dynamics
- **作者**: Roberta M. Lorenzi、Marialaura De Grazia、Claudia A.M. Gandini Wheeler Kingshott 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109872
- **发表**: 2026-11-05
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109872 | 📄 [NN_2026_auto-mfm-spiking-to-mean-field_109872.pdf](papers/NN_2026_auto-mfm-spiking-to-mean-field_109872.pdf)
- **PDF许可**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## 一句话概括
Auto-MFM将生物物理脉冲神经网络（SNN）的微观连接和神经元响应自动映射为描述群体活动的均场模型（MFM），以便在保留关键动态的同时降低模拟复杂度。研究以小脑皮层为案例，并进一步探索病理样式的回路变化。

## 问题与动机
SNN能刻画单神经元放电和细致连接，但大规模仿真代价高；MFM更适合群体与全脑尺度，却往往依赖人工调参，且简化可能丢失空间组织和输入输出关系。本文关注如何从已有生物物理SNN系统化提取连接参数、神经元传递函数并校准MFM，使微观机制可以可靠转译到中观模型。

## 方法
Auto-MFM从SNN提取神经元群体及突触参数，以轴突同步的相位锁定值（PLV）加权突触汇聚度，并将突触权重与动力学参数映射为MFM参数。对各群体的数值输入输出曲线进行拟合，再用NSGA-II多目标优化传递函数，使模型匹配放电响应及斜率等特征。研究将工具用于小鼠小脑多层回路，并通过改变颗粒细胞输入突触电导构建低兴奋至高兴奋的模型族。

## 实验与结果
研究比较小脑SNN与MFM在不同苔藓纤维输入频率下的群体响应，并考察共济失调样浦肯野细胞改变及高兴奋配置。整体上，MFM保留主要输入输出趋势；GoC群体因内部异质性较强，出现约16 Hz的最大偏差。模拟共济失调样树突简化时，浦肯野细胞输入输出斜率由对照的0.23降至0.08。颗粒细胞兴奋性突触电导提高60%时，模型预测其输出最高约240 Hz，并将兴奋变化传播至下游群体。

## 贡献与局限
论文提出可复用的微观到中观自动转译流程，将结构参数映射、同步加权和传递函数优化结合，减少构建区域特异MFM时的人工试错。小脑案例展示了模型对输入响应及病理参数扰动的表达能力，也给出从已知参数向前模拟、从群体表现反推参数的应用思路。作者强调MFM与SNN互补，群体均质化造成的误差仍存在，其他神经元模型与脑区的泛化需要继续验证。

---
DOI: 10.1016/j.neunet.2026.109872 | 📄 [NN_2026_auto-mfm-spiking-to-mean-field_109872.pdf](papers/NN_2026_auto-mfm-spiking-to-mean-field_109872.pdf)
