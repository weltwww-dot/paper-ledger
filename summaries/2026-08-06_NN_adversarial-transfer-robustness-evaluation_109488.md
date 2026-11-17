# TD-CAG: Enhancing adversarial transferability via curvature awareness and spatial dislocation 总结

## 基本信息
- **标题**: TD-CAG: Enhancing adversarial transferability via curvature awareness and spatial dislocation
- **作者**: Hailing Kuang、Chen Wan、Xiaohai Lu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109488
- **发表**: 2026-08-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109488

## 一句话概括
比较视觉分类模型在迁移扰动下的表现，说明单一模型上的鲁棒性评估可能低估跨模型风险。

## 问题与动机
常见评测集中在单一分类器，难以反映同一类输入变化跨模型时的影响范围。

## 方法
作者在同一实验协议下比较多个模型与对照方法，考察源模型变化、输入变化与迁移鲁棒性之间的关系，并用消融衡量不同因素的贡献。

## 实验与结果
在多个分类网络及稳健视觉 Transformer 上比较黑盒迁移成功率，并扩展到图文检索；分类基准中加入模块后的提升范围为 0.1–33.2 个百分点，图文检索结果显示组合方法并非在所有目标模型上最佳（PDF 第5–11页）。

## 贡献与局限
论文为跨模型鲁棒性评估提供了对照。结果依赖基准中的模型、数据以及扰动范围，部署前应使用与实际威胁相符的评测。

---
DOI: 10.1016/j.neunet.2026.109488
