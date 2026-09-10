# TrCLIP-VAD : Weak supervised video anomaly detection by improving CLIP training with text rewriting 总结
## 基本信息
- **标题**: TrCLIP-VAD : Weak supervised video anomaly detection by improving CLIP training with text rewriting
- **作者**: Shengjie Shen, Ziteng Guo, Yahui Li, Liejun Wang, Zhiqing Guo
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108951
- **PDF**: [NN_2026_TrCLIPVAD.pdf](papers/NN_2026_TrCLIPVAD.pdf)
## 一句话概括
TrCLIP-VAD用大语言模型重写视频文本描述，并以局部—全局多尺度Mamba增强弱监督视频异常检测。
## 问题与动机
CLIP式VAD常依赖简单标签提示，难以表达异常行为的高层语义；帧扩增时固定文本也限制视觉—语言对齐。
## 方法
模型先生成视频标题，再用LLM上下文学习重写标题；LGM-Mamba捕捉局部和全局时间依赖，随机选择标题与视觉特征配对以增加语义变化。
## 实验与结果
在XD-Violence和UCF-Crime上取得作者报告的最新水平性能。摘要未提供可安全复述的统一指标。
## 贡献与局限
贡献是将文本重写纳入弱监督VAD并增强时序融合。局限是依赖文本质量、提示措辞和视频域分布，LLM成本与跨场景稳定性仍需评估。
---
DOI: 10.1016/j.neunet.2026.108951
