# Flexible Motion Stylization via Multi-Modality Latent Diffusion Model 总结

## 基本信息
- **标题**: Flexible Motion Stylization via Multi-Modality Latent Diffusion Model
- **作者**: Wenfeng Song、Xingliang Jin、Shuai Li 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15488-15505
- **发表**: 2026-08-20
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3722736

## 一句话概括
本文提出 MM-LDM，以多模态潜空间扩散模型根据文本风格、动作内容和轨迹条件生成风格化运动，同时尽量保留原动作语义。

## 问题与动机
动作风格迁移需要在风格表达与内容保持之间取得平衡；当风格由文本或参考动作给出、且还需遵循轨迹时，多种条件可能相互竞争，使生成结果偏离原动作意图。

## 方法
MM-LDM 在扩散去噪过程中联合接收动作内容、文本或动作风格以及轨迹条件，并以多条件去噪器区分主要内容与辅助条件的作用。针对宽泛文本风格描述，系统另用 LLM parser 将描述拆解为身体部位相关的细化表征，增强局部控制。

## 实验与结果
作者在 HumanML3D 和 Motion-X 上与动作风格化基线比较生成质量、内容保持、风格表现、轨迹保持及脚滑。HumanML3D 的定量结果显示 MM-LDM 在多数比较方法中取得更好的 FMD，且除偏向重建原动作的 STGCN+AdaIN 外，脚滑指标 FSF 最低（PDF 第10–11页）。与动作空间扩散相比，潜空间版本生成 60 帧平均用时 0.220 秒，对方为 7.690 秒；动作空间版本的风格表现 SRA 则低 8.34，反映效率与风格/内容取舍（PDF 第12页）。

## 贡献与局限
该工作把文本风格、动作风格与轨迹条件纳入同一扩散生成流程，并提供面向部位的文本解析以细化控制。当前证据主要来自论文所设定的动作数据与基准，复杂文本解析的稳定性和对未见动作分布的泛化仍需进一步评估。

---
DOI: 10.1109/tpami.2026.3722736
