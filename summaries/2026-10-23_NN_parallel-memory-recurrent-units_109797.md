# Parallelizable memory recurrent units 总结

## 基本信息
- **标题**: Parallelizable memory recurrent units
- **作者**: Florent De Geeter、Gaspard Lambrechts、Damien Ernst 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109797
- **发表**: 2026-10-23
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109797
- **PDF**: [NN_2026_parallel-memory-recurrent-units_109797.pdf](papers/NN_2026_parallel-memory-recurrent-units_109797.pdf)
- **开放许可**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) · 出版社原件，未经修改

## 一句话概括
论文提出记忆循环单元（MRU）这一并行序列建模框架，并给出可训练的双稳记忆循环单元（BMRU）。其设计利用多稳态保存持久记忆，同时让内部状态在每个输入时刻收敛至稳定点，从而把逐时递归转为可并行扫描的计算。作者还将 BMRU 与状态空间模型结合，尝试兼顾瞬态动力学和长期记忆。

## 问题与动机
线性状态空间模型易并行训练且推理更新高效，但其单稳态使历史信息逐渐衰减；具有多稳态记忆的非线性 RNN 又通常难以沿序列维并行。论文关注能否在不放弃持久状态的情况下，使循环单元兼容 parallel scan，并在长依赖任务上保有实用表现。

## 方法
作者先形式化具有内部时钟的 RNN，允许状态在相邻输入间反复更新并取其收敛平衡点；再定义具多稳态、无衰减记忆的 MRU。具体 BMRU 采用双稳动力学与代理梯度训练，将平衡点计算写成可扫描的递推形式；通过与 SSM 混合，补足瞬态响应能力。

## 实验与结果
论文在多项长程依赖及序列基准上比较 BMRU、常见 RNN 和 SSM，并报告 BMRU 能解决依赖距离较长的任务，混合模型可同时利用持久与瞬态动态；另检查并行扫描实现和训练表现（PDF 第1页、第8–12页）。实验支持概念可行性，但摘要没有给出可概括为统一优势的单一数值，结果依任务而异。

## 贡献与局限
主要贡献是将多稳态持久记忆与序列维并行计算结合，并提供可训练的 BMRU 实例及 SSM 混合方向。评估集中于论文所选任务和实现；无限时内部收敛是模型构造理想化条件，实际计算以有限迭代近似，且现有结果不足以说明其在大规模真实序列或生成推理中的普遍效率优势。

---
DOI: 10.1016/j.neunet.2026.109797 | PDF: [NN_2026_parallel-memory-recurrent-units_109797.pdf](papers/NN_2026_parallel-memory-recurrent-units_109797.pdf)
