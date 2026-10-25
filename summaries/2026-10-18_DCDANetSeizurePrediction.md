# DCDA-Net: A depthwise convolution dilated attention network with temporal weighted loss for seizure prediction 总结

## 基本信息
- **标题**: DCDA-Net: A depthwise convolution dilated attention network with temporal weighted loss for seizure prediction
- **作者**: Xingchen Dong、Haotian Li、Qiangqiang Chen 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），109785；2027为卷期年份，不替代2026年在线首发
- **发表**: 2026-10-18
- **日期来源**: 正式PDF首页Available online 18 October 2026
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109785
- **PDF**: [NN_2026_DCDANetSeizurePrediction.pdf](papers/NN_2026_DCDANetSeizurePrediction.pdf)

## 一句话概括
DCDA-Net结合逐通道卷积、膨胀注意力和时间加权损失，从多频段EEG中学习患者个体的发作前模式，用于癫痫发作预测。

## 问题与动机
发作前信号随时间变化，临近发作的片段通常更有辨识度。统一样本权重和混合通道建模可能弱化这些线索，因此论文希望兼顾时序依赖与通道信息。

## 方法
将4秒EEG片段分解为五个频段，逐通道卷积提取局部特征，再以多尺度膨胀注意力融合较长程关系。训练时提高更接近发作的发作前片段权重；按患者进行留一发作事件交叉验证，测试事件与该患者其他训练事件分开。

## 实验与结果
CHB-MIT与SH-SDU分别保留106和72次发作。CHB-MIT的片段准确率为97.56%，患者平均事件敏感度为97.69%、误报率为0.0232次/小时；SH-SDU对应事件指标为96.05%和0.0395次/小时。事件评估设3分钟预测间隔、30分钟发生窗口；患者平均敏感度不等于把所有发作合并后的检出比例（PDF第4、8—9页，表1—5）。

## 贡献与局限
以时间加权训练和通道分析增强个体预测，但这些是回顾性、患者内结果，不是跨患者或前瞻临床验证。SH-SDU缺少发作起始区域标注，通道重要性不能直接当作可靠病灶定位；实时部署和患者独立评估仍是后续工作（PDF第14—15页）。

---
DOI: 10.1016/j.neunet.2026.109785 | PDF: [NN_2026_DCDANetSeizurePrediction.pdf](papers/NN_2026_DCDANetSeizurePrediction.pdf)
