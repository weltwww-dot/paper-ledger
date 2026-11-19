# An end-to-end hierarchical aware mining network for underwater object detection in ambiguous scenes 总结

## 基本信息
- **标题**: An end-to-end hierarchical aware mining network for underwater object detection in ambiguous scenes
- **作者**: Gaoli Zhao、Kefei Zhang、Junping Song 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109924
- **发表**: 2026-11-14
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109924

## 一句话概括
论文提出端到端层级感知特征挖掘网络，针对水下模糊场景中的目标检测组织多层级特征。

## 问题与动机
水下小目标、低对比、复杂背景和伪装会使目标特征与背景混淆；分类置信度与定位结果也可能不一致。论文针对跨尺度信息弱及检测头任务协同不足提出改进。

## 方法
HAMNet 包含上下文门控特征金字塔 CGFPN 和任务一致检测头 TCDH。CGFPN 用分组特征聚焦单元 GFF 与多层特征调制 MFM 做跨层上下文增强和自适应融合；TCDH 建立分类与回归的特征交互，联合优化两项预测。

## 实验与结果
在 DUO、UTDAC 水下数据集上评估，论文报告 DUO 多项 AP、AP50、AP75 指标达到最佳。DUO 消融中 ResNet 基线 AP 为57.5%；仅加 TCDH 为65.1%；GFF 与 MFM 同时加入时 AP 为68.3%、AP_S 为56.2%，高于两模块单独启用的65.4%与65.7% AP。

## 贡献与局限
贡献是将层级上下文挖掘与分类定位协同放入端到端检测器，并通过消融显示两模块互补。作者指出现有水下数据集覆盖不了环境与成像质量的全部变化；真实海域和跨设备泛化仍需更多验证。

---
DOI: 10.1016/j.neunet.2026.109924
