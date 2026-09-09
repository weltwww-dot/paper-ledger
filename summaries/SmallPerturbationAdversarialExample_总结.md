# Small-Perturbation Adversarial Example Detection via Proactive Decision Boundary Bending 总结

## 基本信息

- **标题**: Small-Perturbation Adversarial Example Detection via Proactive Decision Boundary Bending
- **作者**: Nankun Mu、Qi Xia、Fengyi Jiang、Hongyu Huang、Di Zhang、Xiaowei Yang、Bei Gong、Weizhi Meng、Xinyu Lei
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3707542
- **arXiv**: 无
- **PDF**: [TDSC_2026_SmallPerturbationAdversarialExample.pdf](papers/TDSC_2026_SmallPerturbationAdversarialExample.pdf)

## 一句话概括

该文提出 PDBB（主动决策边界弯折），通过主动改造目标模型使决策边界呈现可判别的凹凸形态，从而高精度检出扰动极小的对抗样本，且几乎不损失干净样本精度。

## 问题与动机

深度神经网络极易受到对抗样本攻击。其中小扰动对抗（SPA）攻击因扰动幅度极微、在特征空间中引起的变化极小，比一般对抗样本更难被发现，威胁更为严重。然而现有防御方案多针对扰动较大的一般对抗样本设计：非检测类方案（如对抗训练、输入净化）往往需要牺牲模型精度换取防御能力，检测类方案也主要面向一般对抗样本，缺少专门面向 SPA 的检测方法。

## 方法

PDBB 采取"主动"姿态——防御者不再被动观察模型，而是主动修改目标模型以利于检测。它包含两个关键部件：其一，采用样本扰动训练策略训练目标 DNN，使模型获得期望的弯折决策边界；其二，提出基于投影的辅助度量方法，精确刻画给定测试样本邻域内决策边界的凹凸性，据此区分 SPA 样本与良性样本。设计目标是在保持与原始模型可比的干净准确率的同时，实现高真阳性率与低假阳性率。

## 实验与结果

实验在 MNIST、Fashion-MNIST、CIFAR-10、SVHN 四个数据集上展开，彩色数据集使用 ResNet-18、ResNet-34 与 DenseNet-121，攻击涵盖 PGD、C&W 等一般攻击以及 FAB、FMN、SuperDeepFool、Square 等小扰动攻击，并构造 SPA-AutoAttack 组合攻击，硬件为 NVIDIA GeForce RTX 4090。主要结果：干净精度方面，PDBB 与干净模型基本持平，CIFAR-10 上 DenseNet-121 的 PDBB 模型达 94.46%，略高于干净模型的 94.00%；检测方面，CIFAR-10 上 ResNet-18 的平均检测准确率达 99.08%，多数情形下 TPR 超过 95.00%、平均 F1 高于 98.00%，而 FPR 保持在 1.00% 以下；面对 SPA-AutoAttack，平均 TPR 为 98.00%、F1 为 98.65%。与 LID、MD、SID 三种基线相比，在 CIFAR-10 的 ResNet-18 上这三者的平均检测准确率分别为 75.01%、79.74%、86.00%，比 PDBB 低 24.07、19.34、13.08 个百分点；MD 对 C&W 攻击尚有约 92.84% 准确率与 97.44% AUC，但对 FAB 攻击骤降至 73.70% 与 79.58%，而 PDBB 在各类攻击下稳定保持在 90% 以上。SVHN 上 ResNet-18/ResNet-34/DenseNet-121 的平均检测准确率为 99.35%、99.10%、99.12%，AUC 为 95.43%、95.63%、95.68%。训练开销方面，CIFAR-10 与 SVHN 上单轮训练时间由 11.89 秒增至 12.95 秒，约增加 8.9%。

## 贡献与局限

- 提出首个面向小扰动对抗样本的主动式检测思路 PDBB，与既有被动检测形成范式差异。
- 通过样本扰动训练主动塑造决策边界，并用基于投影的度量刻画边界凹凸性，实现高精度检测。
- 在四个数据集、三种模型、多种 SPA 与一般攻击下取得当前最优的检测性能，且干净精度几乎不下降、开销仅增约 8.9%。
- 局限：需修改并重新训练目标模型，对无法改动模型的场景不适用；扰动样本数量随类别数平方增长，在 ImageNet-1K 这类千类任务上额外样本量巨大、训练成本显著上升；对更优主动式方案的探索仍是开放方向。

---
DOI: 10.1109/tdsc.2026.3707542
