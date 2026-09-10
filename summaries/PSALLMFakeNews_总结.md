# Beyond semantics: Exploiting propagation structures with dual-adapter LLMs for fake news detection 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Beyond semantics: Exploiting propagation structures with dual-adapter LLMs for fake news detection
- 作者：Aojie Si, Shizhan Chen, Xiaobao Wang, Yueheng Sun, Jiaai Guo
- 期刊 / 年份：Neural Networks，2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.108904
- PDF：[PSALLMFakeNews.pdf](papers/PSALLMFakeNews.pdf)

## 一句话概括

论文提出 PSALLM，将新闻传播结构与文本语义共同注入 LLM，并用双适配器和域相似度感知的自适应蒸馏区分跨域稳定结构与域特定结构，从而提升开放世界、跨域假新闻检测的泛化能力。

## 问题与动机

LLM 降低了生成逼真假新闻的成本，使依赖内容语义的封闭分布检测器更容易失效。传播树和用户交互图包含相对稳定、较难通过表面改写操纵的行为关系，但普通 LLM 主要处理扁平文本，缺少显式建模传播的时间和拓扑依赖。同时，传播结构虽有跨域共性，也存在不可忽略的域偏差，需要兼顾不变模式与域特定变化。

## 方法

PSALLM以 LLaMA 为 backbone，构造 graph-enhanced prefix，将传播结构特征和语义信息共同送入预训练 LLM。Non-Weight Decay Adapter（ANWD）用于捕捉跨域不变结构，Weight Decay Adapter（AWD）用于建模域特定结构变化；两者渐进训练，并通过基于域相似度的 adaptive distillation 动态调整贡献。论文采用 zero-shot 跨域评估，目标域支持集不包含样本或域特定信息。

## 实验与结果

论文在四个真实跨域数据集上进行实验：Twitter15→Twitter16、Twitter16→Twitter15、Twitter→Twitter_COVID19 和 Weibo→Weibo_COVID19，并与内容、图模型及 GraphLLM 等基线比较。PSALLM在四种迁移方向上持续优于 state-of-the-art 基线；在域偏移更大的 Twitter→Twitter_COVID19 和 Weibo→Weibo_COVID19 上优势更明显。消融表明移除任一适配器、蒸馏或自适应系数都会降低表现；案例研究也显示，在传播结构偏离源域时，PSALLM能正确分类而 GraphLLM误分类。

## 贡献与局限

贡献包括：提出面向跨域假新闻检测的传播结构增强 LLM；用双适配器解耦稳定结构与域敏感变化；设计域相似度引导的自适应蒸馏并以 zero-shot 实验验证。局限是实验依赖四个社交媒体数据集和有限传播节点，作者代码在匿名期结束后发布；对更长、更噪或对抗性传播过程，以及其他 LLM 架构和平台的外推仍需进一步验证。

---
DOI: 10.1016/j.neunet.2026.108904
