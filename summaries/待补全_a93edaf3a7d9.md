# Multiobjective Simulated Annealing-Based Stopwords Substitution for Rubbish Text Attack 总结

## 基本信息

- **标题**: Multiobjective Simulated Annealing-Based Stopwords Substitution for Rubbish Text Attack
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3675368
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

Modern natural language processing (NLP) models exhibit extreme sensitivity toward text adversarial examples, while their opposite insensitivity to text rubbish examples is greatly underestimated. Text rubbish examples usually refer to highly modified sentences that appear nonsensical to humans but can keep the model's prediction unchanged, which are significant in model robustness evaluation, improvement, and interpretation. Existing methods usually design a single objective optimization method to simultaneously maximize the modification rate and the model confidence (MC) with some text modification strategies, such as word deletion and preposition substitution. However, the single objective optimization easily falls into local optima due to the conflicting objectives, and the simple text modification strategies greatly limit the diversity of rubbish examples. To address these problems, we propose a multiobjective simulated annealing-based stopword substitution (MOSA-S2) algorithm with three major merits. First, the MOSA-S2 replaces the input words with meaningless stopwords and employs importance-based composite perturbation to simulate word substitution, enhancing the quality and diversity of the rubbish sample generation. Second, we formulate a multiobjective simulated annealing method to adaptively determine the priority of word replacements, which can escape local optima with a controlled probability and balance multiple objectives via Pareto dominance. Third, we design a grammatically constrained variant to enhance the readability of rubbish text, while maximizing its semantic deviation from the original to mislead human judgment. We evaluate the effectiveness and efficiency of our method on six text datasets by attacking seven popular neural models. Extensive experimental results demonstrate the superiority of our MOSA-S2 and reveal the fact that modern NLP models may not fully comprehend the textual semantics, as they make the same prediction with even higher confidence for nonsensical text sequences.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tnnls.2026.3675368
