# Optimizing AlphaPose with Dual Non-Local Attention for Real-Time Unsafe Behavior Detection in Mining Environments 总结

## 基本信息
- **标题**: Optimizing AlphaPose with Dual Non-Local Attention for Real-Time Unsafe Behavior Detection in Mining Environments
- **作者**: Weidong Li、Huiyong Xie、Zhenying Li、Daijun Zhang、Shuai Wang
- **期刊 / 会议**: Machine Learning 2026
- **卷期 / 文章号**: 115:252
- **发表**: 2026-10-26
- **日期来源**: Crossref published-online；不以PDF收稿或录用日期替代
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07185-w
- **PDF**: [ML_2026_AlphaPoseDualNonLocal.pdf](papers/ML_2026_AlphaPoseDualNonLocal.pdf)

## 一句话概括
结合外观目标检测与改进AlphaPose，分别识别矿工防护用品佩戴问题和姿态相关危险动作，在矿区数据及COCO上评估精度与速度。

## 问题与动机
井下光照不足、遮挡和防护装备会干扰人体关键点定位；单靠骨架也难判断安全帽、口罩是否佩戴规范，因此需要互补的外观与姿态线索。

## 方法
STFNet-A采用Swin Transformer、多尺度特征和质量焦点损失检测外观类别；Alpha-SDL-Pose用其替换AlphaPose的人体检测器，再加入空间与通道双分支非局部注意力，最后以LSTM处理姿态序列并分类动作。

## 实验与结果
11,600张矿区图像按80/20随机划分，STFNet-A达到96.9% mAP、59.6 FPS；COCO姿态估计达到74.8% mAP、49.4 FPS，mAP略低于HRNet-W48的75.2%。矿区8,600个人体姿态标注按4:1划分，表5指标由89.8升至94.9；该表标为mAP，正文却称识别准确率，不能混作普通分类准确率。速度在RTX 3060、批量1下测量，姿态模型的49.4 FPS包含人体检测与姿态估计两阶段（PDF第10、18—21页，表2、4、5）。

## 贡献与局限
分别改善矿区外观检测和姿态表示，为联合监测提供模块依据；尚未在连续监控视频上进行完整系统的端到端评估，所报FPS也不是完整监测链路吞吐率。自建数据未公开，划分未说明是否按人员或视频分组，跨矿区泛化及相邻帧泄漏风险仍缺独立验证（PDF第22—23页）。

---
DOI: 10.1007/s10994-026-07185-w | PDF: [ML_2026_AlphaPoseDualNonLocal.pdf](papers/ML_2026_AlphaPoseDualNonLocal.pdf)
