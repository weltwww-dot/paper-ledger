# IRAW: Novel invisible and robust adversarial watermark perturbations for digital image protection 总结

## 基本信息
- **标题**: IRAW: Novel invisible and robust adversarial watermark perturbations for digital image protection
- **作者**: Jinchao Liang, Yangcheng Chen, Shuwu Chen, Xiaolong Liu
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于核验 PDF 全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109011
- **PDF**: [NN_2026_IRAW.pdf](papers/NN_2026_IRAW.pdf)

## 一句话概括
IRAW 在 DCT 域联合优化不可见水印和对抗扰动，使图像兼顾 JPEG 兼容、版权追踪和主动防止 AI 分析。

## 问题与动机
传统水印主要事后取证，不能阻止未经授权的自动分类和索引。社交媒体 JPEG 压缩又要求保护方案保持隐蔽与鲁棒。

## 方法
框架把水印嵌入与对抗扰动作为协同优化任务，采用 basin hopping、交叉和自适应变异搜索扰动模式，并在 DCT 频域适配 JPEG 流程。

## 实验与结果
实验验证不可见性、压缩鲁棒性与主动对抗保护效果，结果支持 IRAW 相比被动水印具有防御潜力。摘要未列出统一数字。

## 贡献与局限
贡献是将版权追踪扩展为主动对抗保护。局限是效果依赖攻击模型与图像处理链，对自适应检测器和其他压缩协议仍需验证。

---
DOI: 10.1016/j.neunet.2026.109011
