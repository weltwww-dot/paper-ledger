# HiFiVe: High-fidelity vehicle generation leveraging auto-regressive 2D generative priors 总结

## 基本信息
- **标题**: HiFiVe: High-fidelity vehicle generation leveraging auto-regressive 2D generative priors
- **作者**: Hongli Xiao、Youjian Zhang、Qi Zheng 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109534
- **发表**: 2026-08-20
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109534

## 一句话概括
HiFiVe以粗网格约束预训练二维生成先验，无需额外训练即可逐视角改善车辆纹理，并借助法线优化补充几何细节。

## 问题与动机
车辆三维生成常出现纹理模糊、局部结构不足；联合生成多视图又受到固定机位、分辨率和微调成本限制，如何在保持跨视角一致性的同时提升细节？

## 方法
框架用Flux.2逐步细化图像，依据粗网格深度将历史视图重投影，并按视线与表面法线的对齐程度融合纹理。车辆双侧对称先验缩短自回归路径，减少误差累积；随后由MoGe-2估计法线，以频率自适应加权的网格优化恢复高频结构。

## 实验与结果
在SketchFab-Cars的50个模型和3DRealCar的50张输入图像上，与TRELLIS、Hunyuan3D等比较。真实车辆集FID由TRELLIS的90.42降至85.35，纹理质量指标整体领先；但合成集Chamfer距离为0.0119，略差于TRELLIS的0.0116，不能据此宣称几何精度全面领先。

## 贡献与局限
贡献是将几何同步、多视图纹理融合与法线细化组合成免训练增强流程。局限是依赖合理的初始网格，对非对称贴花或结构可能产生镜像失真；真实集的几何评价主要反映语义对齐，尚不能替代真值几何验证。

---
DOI: 10.1016/j.neunet.2026.109534
