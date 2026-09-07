# Revealing and Defending Against Backdoor Threats in Short-Term Federated Learning 总结

## 基本信息

- **标题**: Revealing and Defending Against Backdoor Threats in Short-Term Federated Learning
- **作者**: Kaiyang Wang, Lixing Chen, Gaolei Li, Qiang Zhang, Hongwei Li, Jianhua Li, Yong Fang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3707924
- **arXiv**: 无
- **PDF**: [TDSC_2026_ShortTermBackdoorFL.pdf](papers/TDSC_2026_ShortTermBackdoorFL.pdf)

## 一句话概括

本文面向全局模型收敛前即终止训练的短期联邦学习场景，提出隐蔽后门攻击方法 ESBA（利用约束损失、训练惯性投毒与集中式更新优化）与基于参数分布统计异常检测与 HDBSCAN 聚类的后门防御机制 PDFM，实验证明 ESBA 可绕过九种先进防御、PDFM 可抵御六种先进攻击。

## 问题与动机

联邦学习（FL）后门攻击的既有研究大多假设 FL 为长期过程：训练可在收敛后持续，攻击者在全局模型接近收敛时发动快速攻击植入持久后门。然而在边缘计算、物联网与医疗等实际场景中，计算与通信开销是主要瓶颈，训练常在全局模型达到预设收敛或固定轮数后即提前终止，形成"短期 FL"场景，攻击者必须在收敛前完成后门注入。该场景带来新挑战：良性模型更新不再接近零，且良性更新与后门更新差异区间的边界更大。同时，现有基于余弦相似度等指标的异常检测防御已被隐蔽攻击通过损失约束等手段绕过，需要探索新的检测指标。

## 方法

本文提出三组件协同的早期阶段后门攻击方法 ESBA。其一，恶意客户端在毒化数据集上以任务损失加自定义约束损失 L_backdoor = Ltask + αLcons 训练后门模型：借鉴贝叶斯先验思想，用上一轮聚合的全局模型近似均值、用毒化数据上的损失梯度反映各参数维度重要性，约束对全局任务重要维度的改动，使后门嵌入在与全局任务关联较小的维度并抑制重要维度参数剧变。其二，惯性投毒机制追踪全局模型历史训练阶段的累积更新方向 vectoracc，在梯度下降时仅保留与累积更新方向符号一致的梯度维度，使恶意更新顺应全局模型的短期优化趋势、贴近良性更新。其三，恶意客户端对全部后门更新做集中式优化：在 L2 范数约束聚合扰动的条件下最大化后门更新与其干净更新之间的余弦相似度，使各更新引入的扰动在聚合时相互抵消。防御侧，作者观察到恶意客户端特定参数维度的统计分布与良性客户端显著不同，提出基于参数分布的过滤机制 PDFM：利用累积惯性方向 vectoracc 选取方向一致的参数维度，累积每个客户端的历史更新向量 H_i 后计算所选维度的均值与方差作为特征 d_i=(mean, var)，再用 HDBSCAN 聚类，将最大簇视为良性并仅聚合这些更新；每轮时间与空间复杂度分别为 O(Nt·K+Nt²) 与 O(N·K+Nt²)。

## 实验与结果

作者在 CIFAR-10、CIFAR-100、GTSRB、Tiny-ImageNet、IMDB 与 Obscene 六个数据集上评估，采用 BAC（后门任务准确率）与 CA（干净任务准确率）两项指标。图像任务设 100 个客户端（含 10 个恶意）、ResNet-18、Dirichlet 采样非独立同分布数据，文本任务（IMDB、Obscene，BERT）设 20 个客户端（含 4 个恶意）。攻击对比 Neurotoxin、3DFed、CerP、FCBA、ModelReplace 五种方法：在 CIFAR-10/CIFAR-100 上既有方法存在攻击时机局限，提前持续攻击时 Neurotoxin、CerP 无法达到理想 BAC，ModelReplace、3DFed 显著损害原任务准确率；ESBA 无论面对 FedAvg 还是防御机制均不损害 CA 并达到理想 BAC。在 GTSRB 模拟损失低于 0.5 且轮间下降小于 0.01 即停止训练的场景下，除 ESBA 外仅 ModelReplace 在部分防御下达到理想 BAC 且有损 CA，ESBA 能绕过全部九种防御（Deepsight、FLAME、FLDetector、Foolsgold、MMetrics、RFOUT、RLR、SNOWBALL、NC+DP）。消融实验表明移除惯性投毒、约束损失或集中式优化（ESBA-RI/RL/RO）任一机制都会显著降低攻击效果。在 LLM 微调场景（IMDB 训练 5 轮、Obscene 10 轮）中 ESBA 同样能绕过全部防御，而多数为小模型设计的防御在此场景失效。防御侧，PDFM 面对 ESBA 与四种代表性攻击时最大 BAC 不超过 15%，且 CA 无明显下降；其变体 PDFM-T、PDFM-LH、PDFM-AH 削弱防御效果，验证了历史更新聚合、累积惯性方向选维等设计的必要性。在异步 FL（70% 无延迟、20% 延迟一轮、10% 延迟两轮）下 ESBA 仍接近 100% BAC，PDFM 将 BAC 压至 GTSRB 4.57%、CIFAR-10 10.19%、CIFAR-100 0.98%；在客户端离线（每轮 20% 概率上传失败、服务器随机选 10 个更新、共 300 轮）的 Tiny-ImageNet 场景中，ESBA 在除 PDFM 外的所有防御下均能成功植入后门。

## 贡献与局限

主要贡献包括：首次系统研究短期 FL 场景下的后门攻击问题，提出可持续攻击整个训练过程并在全局模型收敛前完成注入的隐蔽攻击方法 ESBA；探索了基于参数分布统计（均值与方差）的新异常检测指标，并据此结合 HDBSCAN 提出可扩展的防御机制 PDFM；在六个数据集、五种攻击与九种防御下开展全面实验，验证了攻击与防御的有效性。局限与开放问题方面：ESBA 与动态触发器或边缘样本策略结合（ESBA-C、ESBA-EC）在对抗特定防御时 BAC 出现明显下降，仍需针对性优化；作者指出 LLM 微调场景中多数现有防御失效，暴露了严重后门威胁，亟需面向该场景的专用防御；未来工作拟将 ESBA 与更先进的 FL 攻击策略结合，并发展更强大的攻击及对应防御。

---
DOI: 10.1109/tdsc.2026.3707924
