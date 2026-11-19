# FL-SEHGT: Federated Learning-Based Heterogeneous Graph Transformer with Squeeze-and-Excitation for ASD Identification 总结

## 基本信息
- **标题**: FL-SEHGT: Federated Learning-Based Heterogeneous Graph Transformer with Squeeze-and-Excitation for ASD Identification
- **作者**: Yepeng Zhang、Yuzhong Chen、Hailin Sun 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109663
- **发表**: 2026-09-19
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109663

## 一句话概括
FL-SEHGT 将静息态 fMRI 构成带脑功能网络关系类型的异质图，以联邦异质图 Transformer 联合多站点训练，并用 SE 权重解释重要网络与脑区。

## 问题与动机
自闭症谱系障碍辅助识别受限于功能连接特征提取、模型可解释性和多中心原始影像共享的隐私顾虑。作者研究能否利用脑网络间异质关系提高多站点分类表现，同时在不集中原始影像的训练方式下呈现与诊断相关的网络特征。

## 方法
模型把脑区设为节点、不同功能网络连接设为关系类型，由异质图 Transformer 聚合跨网络信息；Squeeze-and-Excitation 模块重标定网络与脑区表征，提供模型内的重要性权重。各站点本地更新模型并参与联邦聚合，研究在 ABIDE I 的站点规模和样本量异质条件下评估；解释分析进一步检查重要网络的连接差异及其与 ADOS 评分的关联。

## 实验与结果
ABIDE I 共871名受试者、17个站点。17站点联邦结果平均准确率63.45%；样本超过40人的10站点子集为70.54%，高于 GAFD 的58.63%及 LG-FedAvg 的57.11%。但合并五折评估中 SEHGT 的 F1 为0.642，低于 SVM 的0.662，显示准确率/AUC优势未覆盖所有阈值相关指标。重要特征涉及默认模式、小脑和执行控制网络。

## 贡献与局限
工作把脑网络关系编码进联邦异质图，并以 SE 权重提供候选影像解释。多中心比较显示较大站点子集表现较好；小站点结果较低或波动，且 F1 不占优，不能直接用于诊断。联邦训练不等于差分隐私，脑区解释仍需独立队列验证。

---
DOI: 10.1016/j.neunet.2026.109663
