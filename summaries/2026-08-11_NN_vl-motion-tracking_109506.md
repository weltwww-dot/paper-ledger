# A unified decision-driven framework: Long-term tracking via visual-language models with motion estimation 总结

## 基本信息
- **标题**: A unified decision-driven framework: Long-term tracking via visual-language models with motion estimation
- **作者**: Liqiang Liu、Lingling Yang、Feng Huang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109506
- **发表**: 2026-08-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109506

## 一句话概括
VL-METrack以训练免调的在线决策融合运动估计和视觉语言定位，在OTB、LaSOT与TNL2K上取得有竞争力的长时跟踪表现，同时降低对复杂跨模态联合训练的依赖。

## 问题与动机
视觉语言长时跟踪在遮挡、目标丢失和外观变化下容易漂移，且复杂模型训练与计算开销限制部署。

## 方法
以预训练定位网络提供目标位置和置信度，低置信时结合光流与相关滤波进行运动补偿和局部细化；再用运动趋势校正、动态模板更新及多模板全局重检测恢复跟踪。

## 实验与结果
在OTB、LaSOT、TNL2K及多属性场景上评测；边界框初始化时LaSOT AUC/PRE为68.9/68.4，OTB99为70.8/82.9，语言初始化的LaSOT为63.1/62.3。消融显示运动估计加入后指标进一步提升；方法仍依赖预训练定位器，运动趋势校正对随机运动有限（PDF 第 6、8、10 页）。

## 贡献与局限
将长时跟踪的补偿与重检测组织为置信度驱动的在线后处理，避免为该框架另行联合训练；多数据集结果支持其精度与效率折衷，但其鲁棒性仍受运动可预测性和基础定位器质量约束。

---
DOI: 10.1016/j.neunet.2026.109506
