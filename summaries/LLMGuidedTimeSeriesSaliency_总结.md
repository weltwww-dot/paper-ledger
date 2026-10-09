# Large Language Model Guided Series Saliency Module for Accurate and Interpretable Multivariate Time Series Forecasting 总结
## 基本信息
- **标题**: Large Language Model Guided Series Saliency Module for Accurate and Interpretable Multivariate Time Series Forecasting
- **作者**: Qingyi Pan、Liyuan Wang、Xiaoyu Chen 等
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-07
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07045-7
- **PDF**: [ML_2026_LLMGuidedTimeSeriesSaliency.pdf](papers/ML_2026_LLMGuidedTimeSeriesSaliency.pdf)

## 一句话概括
论文提出可插入多变量时间序列预测模型的 Series Saliency（SS）模块，让模型在利用局部波动的同时显式感知趋势，并将同一机制用于特征解释；大型语言模型（LLM）分别参与趋势融合引导和自然语言解释。

## 问题与动机
深度预测模型能拟合非线性关系，却容易过度关注短期起伏，对趋势及变量间的时间—特征关联利用不足；锯齿、尖峰等局部模式也会干扰解释。统计模型较易解释但受线性、平稳性假设限制，因此作者希望在不替换现有预测骨干的前提下兼顾预测与解释（第2–3页）。

## 方法
方法将滑动窗口中的时间与变量维度组织成 series image，对各变量作 Gaussian smoothing 得到趋势，再用可学习掩码逐点混合原序列与趋势。训练时，DeepSeek-V3 接收均值、标准差、波动性等统计量，提示其识别平稳与高波动区域并指导掩码；不把原始序列片段放入提示。模型另接 Auto-Regressive（AR）支路，与可替换的深度预测器共同输出。解释阶段更新 SS 以估计特征重要性，并借助 LLM 生成文字说明；平滑正则项旨在抑制尖峰式异常。论文的理论分析给出输入空间探索及平滑性方面的性质，这些保证不等同于实测精度提升（第6–12页）。

## 实验与结果
预测实验涵盖 Air Quality、Industry、Exchange Rate、Weather 等规则采样数据，并在北京多站点空气质量数据上模拟 10% 和 30% 时间点缺失；比较统计模型及 CNN、GRU、LSTNet、Transformer、TimeMixer 等骨干。作者报告 SS 对多种骨干有插件式收益，消融也显示移除 LLM 引导或 AR 支路会使表现退化。解释实验在 Air Quality、Industry、Exchange Rate 上比较多种方法；表8的 AUCORR 越低越好，SS 分别为 0.02333、0.06857、0.01885，均优于表中对照方法（第13–18、27–30页）。

## 贡献与局限
贡献在于把趋势感知做成兼顾训练和解释的通用模块，并以统计提示将 LLM 的领域知识接入趋势融合；实验覆盖多种骨干、数据与解释基线。局限是预测收益主要由所列数据集、预测设置和消融支持；AUCORR 衡量扰动特征对预测的影响，不能单独证明解释符合领域专家认知或改善实际决策。后一限制是由其评估设计推得，论文未报告受控的专家决策实验（第27–30页）。

---
DOI: 10.1007/s10994-026-07045-7
