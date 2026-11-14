# Efficient and Effective Federated Unlearning via Adaptive Data Partitioning 总结

## 基本信息
- **标题**: Efficient and Effective Federated Unlearning via Adaptive Data Partitioning
- **作者**: Zhigang Wang、Jiahao Li、Ning Wang 等
- **期刊 / 会议**: IEEE Transactions on Knowledge and Data Engineering 2026
- **卷期 / 文章号**: 38(12)，8152-8166
- **发表**: 2026-09-22
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1109/tkde.2026.3736816

## 一句话概括
论文提出自适应分区联邦遗忘框架，试图在撤销客户端数据影响时兼顾遗忘效率与模型精度，重点处理非独立同分布和多次撤销。

## 问题与动机
分片可将重训限制在局部，但分片隔离会损害精度；客户端参与随机、数据分布异质又使遗忘代价和模型质量难以同时控制。

## 方法
框架结合个性化聚合、动态均衡分片和按撤销概率排序的调度，并用稀疏化权重减少推理时贡献很小的子模型。

## 实验与结果
在MNIST、Fashion-MNIST、CIFAR-10、FEMNIST和Shakespeare等设置中，分片方法的恢复收敛轮数为2–10，较FATS最多快60倍；动态均衡在连续撤销时还降低通信开销（PDF第9–13页）。

## 贡献与局限
方法把准确率、分片平衡和撤销代价纳入同一设计；实验将客户端数限制为200，且隐私风险缓解依赖可信洗牌或TEE等额外机制，不能据此视作完整隐私保证（PDF第8–10页）。

---
DOI: 10.1109/tkde.2026.3736816
