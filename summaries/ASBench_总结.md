# ASBench：图像异常合成基准

## 基本信息

- 标题: ASBench: Image Anomalies Synthesis Benchmark for Anomaly Detection
- 作者: Qunyi Zhang, Songan Zhang, Jiaqi Liu, Jinbao Wang, Xiaoning Lei, Guoyang Xie, Guannan Jiang, Zhichao Lu
- 期刊 / 会议: IEEE Transactions on Artificial Intelligence 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能
- DOI: 10.1109/tai.2026.3680823
- PDF: [TAI_2026_ASBench.pdf](papers/TAI_2026_ASBench.pdf)

- 标题: ASBench: Image Anomalies Synthesis Benchmark for Anomaly Detection
- 作者: Qunyi Zhang, Songan Zhang, Jiaqi Liu, Jinbao Wang, Xiaoning Lei, Guoyang Xie, Guannan Jiang, Zhichao Lu
- 期刊 / 会议: IEEE Transactions on Artificial Intelligence 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 人工智能

- **标题**：ASBench: Image Anomalies Synthesis Benchmark for Anomaly Detection
- **作者**：Qunyi Zhang, Songan Zhang, Jiaqi Liu, Jinbao Wang, Xiaoning Lei, Guoyang Xie, Guannan Jiang, Zhichao Lu
- **期刊**：IEEE Transactions on Artificial Intelligence, Vol. 7, No. 9, September 2026
- **研究方向**：工业异常检测、异常合成、视觉基准
## 一句话概括

ASBench 将异常图像合成从检测系统的附属步骤中独立出来，用 12 种合成方法、4 条检测流水线和 5 个数据集，系统评估合成质量与检测效用之间的关系。

## 问题与动机

工业异常检测常受异常样本稀缺和标注成本高限制，异常合成因此成为重要的数据扩充手段。但已有工作通常只报告“合成后检测器变好多少”，缺乏对合成方法本身的可复现实验规范，也较少分析跨数据集泛化、合成/真实数据配比和合成图像指标是否真的预测检测性能。

## 方法

论文建立 ASBench 评测协议，把合成算法与下游检测器解耦，并从四个维度组织实验：跨数据集和检测流水线的泛化、合成样本与真实样本的比例、合成图像内在质量指标与异常检测性能的相关性、不同合成器混合使用的策略。基准覆盖 12 种异常合成方法、4 条检测流程和 5 个数据集，配套公开代码以便复验。

## 实验与结果

系统实验揭示了当前异常合成方法在跨场景迁移、数据配比和质量指标解释方面的局限：合成图像的单一视觉质量分数并不总能代表检测收益，混合不同合成器也需要考虑互补性而非简单堆叠。四维结果为选择合成方法和设计未来检测流水线提供了可操作的经验。

## 贡献与局限

论文贡献是提出专门评估异常合成的基准框架，提供多数据集、多流水线和多方法的统一比较，并把合成质量与检测结果联系起来。局限是基准结论受所选数据集、合成器和检测器覆盖范围影响；真实工业缺陷、三维/视频异常及持续扩展的新型生成方法仍需要纳入后续版本。

---
DOI: 10.1109/tai.2026.3680823
