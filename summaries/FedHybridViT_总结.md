# FedHybrid-ViT: A Federated-Hybrid Framework for Generalizable Deepfake Detection on Heterogeneous Data 总结
## 基本信息
- **标题**: FedHybrid-ViT: A Federated-Hybrid Framework for Generalizable Deepfake Detection on Heterogeneous Data
- **作者**: Abdullah Mohammad Sakib、Md. Mohashin Hossain、Mahedy Hasan Foysal 等
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-07
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07171-2
- **PDF**: [ML_2026_FedHybridViT.pdf](papers/ML_2026_FedHybridViT.pdf)

## 一句话概括
FedHybrid-ViT 把 ResNet-18 与 ViT-Base/16 双分支特征融合后置于 FedAvg 联邦训练中，尝试在不集中交换原始人脸图像的条件下提升异质来源深伪检测能力。

## 问题与动机
集中式检测器可能依赖特定数据集的伪影，在来源变化时泛化下降；联邦学习虽避免汇集原始数据，客户端分布不一致又可能使训练不稳。作者将问题概括为泛化与联邦异质性并存，重点考察五个地区样本合并后的来源差异（第2–3页）。

## 方法
先从视频抽取并裁剪人脸，构建包含 Africa、Asia、Europe、Korea、USA 五地区的51,222张真假图像；预训练 ResNet-18 分支提取局部融合痕迹、压缩伪影，ViT-Base/16 分支建模跨面部区域的全局关系，两路向量拼接后分类。训练使用 FedAvg：合并数据按索引分给3个逻辑客户端，每轮各端本地训练后按样本量加权聚合，共5轮、每端每轮3个本地 epoch。地区不是客户端划分，故实验中的 non-IID 指合并数据的来源异质性，而非五个地区各自独立持有数据（第6–12页）。

## 实验与结果
测试集从合并数据随机分层留出20%；比较集中式和联邦 CNN、ViT、混合模型。在异质合并集上，FedHybrid-ViT 准确率为94.55%（表2四舍五入为94.6%），高于联邦 CNN 的93.1%与联邦 ViT 的92.0%，接近集中式混合模型的95.10%；表3报告其 AUC 为0.925、F1为94.55%。该结果支持所设随机留出测试上的优势，不是跨独立数据集的外部泛化检验（第14–16页）。

## 贡献与局限
工作展示了局部 CNN 伪影特征与 ViT 全局表征结合的联邦方案，并在所构造的跨地区混合数据上超过单分支联邦基线。研究自身指出，混合模型计算量较高，联邦更新仍可能遭梯度反演攻击，未提供差分隐私等形式化保护。另据实验设计，三个客户端由混合数据索引切分，测试也来自同一数据池；因此结果尚不能证明真实地区隔离部署或未见来源上的泛化能力（第7、11–12、14–18页）。

---
DOI: 10.1007/s10994-026-07171-2
