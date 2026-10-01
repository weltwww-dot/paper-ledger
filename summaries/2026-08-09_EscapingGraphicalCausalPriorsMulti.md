# Escaping graphical causal priors: Multi-generator cooperation for rationalization 总结

## 基本信息
- **标题**: Escaping graphical causal priors: Multi-generator cooperation for rationalization
- **作者**: Wei Liu、Zhiying Deng、Lang Gao 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **发表**: 2026-08-09
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104601
- **PDF**: [AIJ_2026_EscapingGraphicalCausalPriorsMulti.pdf](papers/AIJ_2026_EscapingGraphicalCausalPriorsMulti.pdf)

## 一句话概括
MGR 以多个生成器共同训练同一预测器，从不同 rationale 候选中提高因果特征的稳定性，减轻传统 rationalization 对伪相关和退化捷径的过拟合。

## 问题与动机
常见 rationalization 通过预测准确率评价所选文本片段，但与标签相关的非因果线索也可能得到高分；单个生成器还可能选出无意义的简单模式，令预测器与生成器形成退化协作。既有方法通常分别处理这两类问题，且因果图方法依赖难以检验的假设。作者希望从概率建模角度同时缓解两种失效。

## 方法
MGR 用不同初始化的多个生成器分别从同一输入抽取 rationale，并将候选交给共享预测器联合优化；训练时多样候选促使预测器不依赖单一捷径，推理时只需保留一个生成器。扩展方法 MGR-VRM 为生成器设置不同的 rationale 稀疏度，以拓展候选邻域、降低生成器趋同，并可共享编码器以节省资源。论文还从伪相关发生概率和 rationale 多样性给出理论分析。

## 实验与结果
实验覆盖六个文本分类集（BeerAdvocate、HotelReviews）及带人工伪相关的 GOODMotif 图分类集，比较 RNP、Noise-RAT、Inter-RAT、GRAT 等方法，并补充 BERT 与 LLaMA-3.1-8B-Instruct 对照。Beer 三项任务在约 10% 稀疏度下，MGR-VRM 的 F1 分别为 66.2、68.8、62.2；约 30% 稀疏度时 Beer-Appearance 的召回率为 96.1%。GOODMotif 上 F1 为 48.6，高于 RNP 的 44.1。作者还报告 MGR-VRM 训练可一次产出三种稀疏度，并以共享编码器降低资源开销。

## 贡献与局限
- 将伪相关与生成器退化置于统一的概率视角分析，并提出多生成器协作框架。
- 以不同稀疏度扩展候选邻域，使多种解释长度可由一次训练获得。
- 结论主要由带人工 rationale 标注的文本和合成图分类基准支持；因果特征占优等理论分析依赖文中设定，不能据此保证任意真实语料都能识别因果关系。作者将重点定位为解释提取，而非提升分布外预测。

---
DOI: 10.1016/j.artint.2026.104601
