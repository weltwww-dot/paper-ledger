# Parallel Secure Pattern Matching With Differential Privacy and Consistency Checking 总结

## 基本信息

- **标题**: Parallel Secure Pattern Matching With Differential Privacy and Consistency Checking
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3698857
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

Secure Pattern Matching (SPM) aims to identify all occurrences of a target pattern within a text while preserving data confidentiality and has vital applications in bioinformatics, digital forensics, and cloud-based healthcare. However, existing SPM schemes often suffer from limited scalability on large scale datasets and provide insufficient correctness assurances under outsourced cloud settings. To address these limitations, we propose PSPM, a parallel SPM framework built upon secure multi-party computation (MPC), supporting both single- and multi-pattern queries with comprehensive wildcard functionality. The proposed scheme integrates differentially private Read and Write primitives to obfuscate memory access patterns and enable secure, oblivious data operations. To enhance efficiency, the input text is divided into overlapping sliding windows, each processed in parallel under SIMD-style execution. Each window performs bidirectional scanning to fully leverage parallelism and maximize throughput. For single-pattern queries, local matching is achieved through a border-array–based algorithm, while multi-pattern matching employs an MPC-adapted Aho–Corasick automaton. We design a lightweight cross-consistency checking mechanism that validates outputs via wildcard-augmented variants, thereby enabling detection of inconsistency-inducing single-path computation faults under the standard non-colluding semi-honest setting. Formal security proofs and extensive experimental evaluations on large genomic datasets demonstrate that our framework outperforms prior SPM protocols by up to 1.73× in single-pattern tasks and 10.56× in multi-pattern tasks.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tdsc.2026.3698857
