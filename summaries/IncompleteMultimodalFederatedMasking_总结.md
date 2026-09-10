# Incomplete Multimodal Federated Learning via Masking and Contrasting Prototypes 总结

## 基本信息

- **标题**: Incomplete Multimodal Federated Learning via Masking and Contrasting Prototypes
- **作者**: Guangyin Bao, Qi Zhang, Duoqian Miao, Zixuan Gong, Chaochao Chen, Liang Hu, Longbing Cao
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-03-23
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3658522
- **arXiv**: 无
- **PDF**: [NN_2026_IncompleteMultimodalFederatedMasking.pdf](papers/NN_2026_IncompleteMultimodalFederatedMasking.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出 PmcmFL，通过共享原型库把缺失模态表示为具有类别语义的 mask，并用原型对比学习协调客户端表示，从而提升复杂模态缺失和非 IID 条件下的多模态联邦学习性能。

## 问题与动机

现实客户端可能同时拥有不完整的图像—文本数据，而已有多模态联邦学习方法主要覆盖单模态客户端或模态完整的多模态客户端。将缺失模态置零会把本应学习的多模态任务变成不一致的单模态任务，并加剧客户端与服务器之间的 task drift。论文因此同时关注训练阶段和推理阶段的随机模态缺失。

## 方法

PmcmFL 在服务器维护图像、文本和融合表示三类低维类别原型，并以参与客户端的类别中心进行加权聚合。训练时，用与标签类别对应的原型替代缺失模态，构造 task-calibrated loss，使融合模块仍由原始任务监督；推理时，则通过 model-free 或 model-based matching 找到跨模态原型，并可用 ProtoMix 融合多个相关原型。针对非 IID 引起的 client drift，方法把融合原型作为对比学习目标加入 proximal loss，最后仍通过 FedAvg 聚合模型。

## 实验与结果

实验在由 VQAv2 筛得的 tinyVQA 上进行，数据含 310 个类别、64,000 个训练样本和 5,000 个测试样本，训练数据按 Dirichlet α=0.1 分到 30 个客户端，并测试 0.1–0.5 的缺失率。PmcmFL 在训练和推理同时缺失时各缺失率均取得最好结果；在单模态推理中，model-based 原型匹配最高达到 27.502%，较基线提升 23.840%，简单缺失场景较 CreamFL 提升 3.38%。消融显示 Prototype Mask 和 Prototype Contrast 对 Acc@sum 的增益分别为 11.168% 和 7.430%；tinyVQA 中原型库只使每轮通信开销增加 0.32%。

## 贡献与局限

论文将原型库、任务校准 mask、模型无关的缺失模态推理和原型对比正则统一到一个联邦框架中，并验证了其对复杂缺失、非 IID、通信效率和投毒扰动的作用。局限在于原型跨数据集的一致性仍不足，推理阶段的原型匹配精度有限；原型库虽难以直接重构客户端样本，但仍可能泄露客户端数据分布，隐私保护尚待研究。

---
DOI: 10.1109/tnnls.2026.3658522
