# Diffusion models with progressive gradient variation for imperceptible and transferable adversarial attack 总结

## 基本信息
- **标题**: Diffusion models with progressive gradient variation for imperceptible and transferable adversarial attack
- **作者**: Jia-Hua Fan、Heng-Ru Zhang、Fan Min
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109888
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109888

## 一句话概括
DPGT在扩散反向去噪的多个阶段逐步施加潜变量梯度扰动，并以反馈控制决定何时停止，提升跨模型攻击迁移性，同时权衡图像感知质量。

## 问题与动机
扩散式对抗攻击若只在单一时间步优化潜变量，后续去噪可能逐渐削弱对抗信号，导致对不同架构模型的迁移效果不足。作者关注如何让攻击影响贯穿生成轨迹，并在增强攻击迁移性的同时避免不必要扰动损害图像质量。

## 方法
DPGT在预训练扩散模型的潜空间中工作，沿反向去噪轨迹逐步注入基于分类器梯度的扰动，使攻击影响能够跨时间步持续累积。目标同时考虑误导分类、维持图像结构以及削弱文本—图像语义对齐。反馈控制模块监测生成图像的分类结果；达到连续成功次数阈值后停止扰动，余下步骤正常去噪。论文提供偏重最大迁移效果的DPGT-S与控制扰动、折中感知质量的DPGT-A两种策略。

## 实验与结果
实验使用ImageNet-Compatible的1000张299×299图像，并在CUB-200-2011和Stanford Cars上评估；比较四类攻击，报告非代理模型平均准确率（越低表示迁移攻击越强）、FID和LPIPS，并测试防御条件。ImageNet-Compatible上DPGT-A非代理平均准确率为33.5%，对照DiffAttack为38.2%；在同扰动预算L2=23.6的比较中，DPGT-A为64.3%，DiffAttack为66.1%。分析还显示，分类器对真实类别的平均置信度在去噪末段快速形成：t=5至0由0.234升至0.737。

## 贡献与局限
研究把攻击设计从单步扰动扩展为跨去噪轨迹的持续调节，并以成功反馈终止优化，提供攻击强度与图像质量之间的可调折中。多数据集和防御实验支持迁移性提升，但不同指标并不一致：作者报告LPIPS仅属中等，FID与LPIPS对图像质量的反映也可能分歧；DPGT-S与DPGT-A的效果依赖成功阈值，且实验局限于指定生成骨干、分类器和数据集，不能直接推及任意模型或实际部署。

---
DOI: 10.1016/j.neunet.2026.109888
