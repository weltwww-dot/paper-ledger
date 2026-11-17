# FASFF: Frequency domain information-aided spatial domain feature fusion for RGBT tracking 总结

## 基本信息
- **标题**: FASFF: Frequency domain information-aided spatial domain feature fusion for RGBT tracking
- **作者**: Jianming Zhang、Jun Long、Yonghang Liu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109500
- **发表**: 2026-08-13
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109500

## 一句话概括
本文提出 FASFF，将频域注意、跨模态协同和空间—频率交互用于 RGB—热红外目标跟踪，以利用两种模态的互补信息。

## 问题与动机
既有 RGB-T 跟踪方法常局限于空间域或频域内融合，未充分利用两域和两种传感模态的互补性，恶劣场景下稳定性因此受限。

## 方法
频域注意增强模块通过离散余弦变换突出信息频率，并以跨模态协同注意细化特征；空间—频率交互融合模块再联合更新两域表示并输出跟踪结果。

## 实验与结果
在 RGBT210、RGBT234 与 LasHeR 上与多种跟踪器比较，报告成功率及其他跟踪指标，并分析低照度、背景干扰等条件；作者称方法在多个基准保持稳定且总体具有竞争力。具体结果受数据集和场景划分限制，不能直接推出实际部署性能（PDF 第 7–10 页）。

## 贡献与局限
研究将频率线索用于 RGB-T 特征协同，并在三套基准上验证该设计；传感器差异和未覆盖环境下的泛化仍需进一步测试。

---
DOI: 10.1016/j.neunet.2026.109500
