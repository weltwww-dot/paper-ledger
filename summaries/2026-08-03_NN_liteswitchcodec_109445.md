# LiteSwitchCodec: Neural speech coding with token space quantization and causal U-Net for personalized real-time communications 总结

## 基本信息
- **标题**: LiteSwitchCodec: Neural speech coding with token space quantization and causal U-Net for personalized real-time communications
- **作者**: Xusheng Yang、Wei Xiao、Zixiang Wan 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109445
- **发表**: 2026-08-03
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109445

## 一句话概括
LiteSwitchCodec针对个性化实时语音转换级联时延，在离散token域用因果U-Net联合转换与编码，指标具竞争力，但基线设置不完全一致。

## 问题与动机
如何低时延实现个性化语音编码？

## 方法
有限标量量化形成token，因果U-Net作音色适配，token shaping补偿高频损失并分阶段训练。

## 实验与结果
与OPUS、Lyra、EnCodec、DAC、FunCodec及转换模型比较语音质量；LiteSpeechCodec以1.67M参数实现有竞争力的重建，转换评估涵盖多码率（PDF第8–10页）。

## 贡献与局限
提出token域实时个性化编码；基线采样率和码率不同，真实链路验证有限。

---
DOI: 10.1016/j.neunet.2026.109445
