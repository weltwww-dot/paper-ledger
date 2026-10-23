# PassCluster: A New Segmented Password Cracking Model 总结

## 基本信息
- **标题**: PassCluster: A New Segmented Password Cracking Model
- **作者**: Hu Xiong、Kaiwen Xing、Xudong Yang 等
- **期刊 / 会议**: ACM Transactions on Privacy and Security 2026
- **发表**: 2026-10-21
- **日期来源**: Crossref published-online；PDF可见2026/10出版标记，不据此伪造具体日
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1145/3859248
- **PDF**: [TOPS_2026_PassCluster.pdf](papers/TOPS_2026_PassCluster.pdf)

## 一句话概括
PassCluster从训练密码中的字符邻接关系学习分段，再以LSTM建模片段序列，用于研究密码猜测和强度评估。

## 问题与动机
字符级模型的单元可能过细，PCFG结构又可能过粗，两者都可能错失密码内部的依赖关系。论文希望用数据驱动的分段，在结构表达与细节建模之间取得平衡。

## 方法
将可打印ASCII字符构成加权邻接图，用Louvain社区检测划分字符类别，并把连续同类字符合为片段。LSTM学习片段序列的条件概率，结合采样和Monte Carlo猜测次数估计评估模型，另构建密码强度计原型。

## 实验与结果
使用八个历史泄漏数据集，评估站内和跨站设置。正文报告在10^7—10^10猜测范围，较FLA的平均提升分别为5.5%和5.2%；但10^20预算表中，站内相对FLA的平均变化为−0.04%。摘要的跨站85.5%是对OMEN比较范围的上限，不能当作普遍平均提升（PDF第14—15页，表6）。

## 贡献与局限
以字符聚类改善分段概率建模，但实验仅覆盖筛选后的6—20位可打印ASCII密码，不能外推到所有语言或现代认证场景。超大预算依赖概率/猜测次数估计，部分生成基线实际只能生成约10^10个候选，不能把10^20表格理解为同等规模的实际穷举实验；高预算下也并非优于所有模型（PDF第5—9、15—21页）。

---
DOI: 10.1145/3859248 | PDF: [TOPS_2026_PassCluster.pdf](papers/TOPS_2026_PassCluster.pdf)
