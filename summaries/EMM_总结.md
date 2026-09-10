# EMM: Plug-and-play memory-bank sampling for contrastive recommendation 总结

## 基本信息

- **标题**: EMM: Plug-and-play memory-bank sampling for contrastive recommendation
- **作者**: Zhisheng Meng、Jian Wang、Lei Li、Wenxia Chen、Ziang He
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108948
- **arXiv**: 无
- **PDF**: [NN_2026_Paper02.pdf](papers/NN_2026_EMM_MemoryBankSampling.pdf)

## 一句话概括

EMM 通过可插拔的情景记忆负采样缓解对比推荐中的弱梯度、陈旧难负样本和假负样本问题。

## 问题与动机

对比推荐的表示质量高度依赖正负样本构造。随机负样本信息不足，只选最难负样本又容易陈旧并把语义相近项目误当负样本，在稀疏反馈下造成不稳定训练。研究希望在不改动主干编码器的前提下，获得新鲜、有信息且安全的负样本。

## 方法

EMM 只作用于采样层，可接入 SGL、SimGCL 和 LightGCL 等流程。方法用 EMA 记忆库和周期性重建保持候选表示更新，再从刷新后的候选池做 Top-K 检索，并混入少量随机负样本。ID 排除和相似度窗口过滤用于降低假负样本风险，滚动刷新用于维持多样性。

## 实验与结果

文章在 Baby、Sports 和 Clothing 三个基准上，结合五个代表性基线进行评测，并报告约 15.1% 的平均总体推荐质量提升，训练成本相近。消融实验分别考察刷新机制、混合采样和安全过滤，结果支持负样本构造作为独立且有效的设计轴。

## 贡献与局限

贡献是提出不改主干的 memory-bank 负样本构造原语，并给出两时间尺度刷新、硬负样本–随机样本混合和假负样本防护。局限是评测集中在三个推荐基准与五类骨干，极端稀疏度、在线系统延迟和更大规模目录仍需验证。

---
DOI: 10.1016/j.neunet.2026.108948

