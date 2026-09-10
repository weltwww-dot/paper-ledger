# Multi-scale pyramid fusion with overlap density attention module for crowd counting 总结

## 基本信息

- **标题**: Multi-scale pyramid fusion with overlap density attention module for crowd counting
- **作者**: Avinash Rohra, Baoqun Yin, Aakash Kumar, Ajeet Kumar Bhatia, Hazrat Bilal, Yanzhe Wang, Munawar Ali
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108983
- **arXiv**: 无
- **PDF**: [NN_2026_MultiScalePyramidFusionCrowd.pdf](papers/NN_2026_MultiScalePyramidFusionCrowd.pdf)

## 一句话概括

MSPF用重叠密度注意、多尺度金字塔融合和特征增强改善密集场景中遮挡、尺度变化和个体重叠造成的人群计数误差。

## 问题与动机

高密度人群图像常同时包含严重遮挡、个体重叠和巨大尺度差异，单一尺度特征难以生成可靠密度图。准确计数对公共安全和拥挤环境分析具有实际意义。

## 方法

编码器先以多个感受野提取特征；重叠密度注意模块分别关注重叠与非重叠区域，多尺度金字塔融合模块自适应整合不同尺度信息，特征增强模块进一步细化空间表示，最后回归人群密度图。

## 实验与结果

实验使用作者提出的Highly-Packed-Crowd数据集和四个具有挑战性的公开基准。全文报告MSPF在准确性、鲁棒性和效率方面优于对比方法，但未在此处补写未经逐表核对的具体指标。

## 贡献与局限

贡献是针对重叠区域设计密度注意并将其与金字塔融合联合。局限是性能依赖密度标注和场景分布，极端遮挡、跨场景泛化以及部署时的计算成本仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.108983
