# Federated Unlearning Activated Backdoor Attacks 总结

## 基本信息

- **标题**: Federated Unlearning Activated Backdoor Attacks
- **作者**: Jian Chen、Wenlong Shi、Chengyu Hu、Jianfeng Lu、Ahmed M. Abdelmoniem、Chen Wang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3703139
- **arXiv**: 无
- **PDF**: [TDSC_2026_FederatedUnlearningActivatedBackdoor.pdf](papers/TDSC_2026_FederatedUnlearningActivatedBackdoor.pdf)

## 一句话概括

本文提出 FedUBA，揭示联邦遗忘流程本身可能被恶意遗忘请求利用来激活后门，并通过隐蔽触发器、敏感样本选择和恶意遗忘请求在不明显影响干净数据效用的情况下改变模型行为。

## 问题与动机

联邦遗忘旨在从已训练模型中移除客户端数据，以满足隐私保护和合规要求，但现有研究主要关注遗忘效率，对遗忘过程的安全性关注不足。攻击者不必在联邦训练阶段直接投毒，而可以把后门行为隐藏到影响样本和遗忘请求中，等待模型执行遗忘时再触发。作者研究这种“遗忘激活后门”对不同遗忘算法和聚合规则的影响。

## 方法

FedUBA 由三个阶段组成：先生成与目标类别语义相关且尽量隐蔽的后门触发器；再用黑盒敏感性分析找出对后门样本预测影响最大的本地样本；最后构造恶意遗忘请求，使全局模型错误地遗忘这些影响样本，从而放大后门样本的目标类别预测。作者还引入随机选择版本进行对照，并在 FedEraser、KNOT、FUKD 等遗忘设置下考察攻击效果、干净精度和遗忘后的模型效用。

## 实验与结果

实验使用 PathMNIST、CIFAR-10、GTSRB、CIFAR-100 和 Tiny-ImageNet 等数据，并以 MobileNetV2、ResNet18、VGG11 等模型进行联邦训练。总体结果显示，仅触发 0.5% 的恶意遗忘请求即可达到约 80% 的后门攻击成功率；在 IID 设置下，PathMNIST 与 CIFAR-10 的攻击成功率最高约 89%，GTSRB 约 65%，而干净样本准确率前后变化通常在约 1% 内。加入知识蒸馏式遗忘后，IID 场景的平均全局准确率分别为 PathMNIST 75.17%、CIFAR-10 82.75%、GTSRB 91.30%；非 IID 场景分别为 70.88%、82.94% 和 90.86%。

## 贡献与局限

- 首次系统揭示联邦遗忘机制可被用作后门激活面，而非只作为数据删除工具。
- 用敏感样本选择把触发器影响集中到遗忘过程，提升隐蔽性和攻击效率。
- 在多数据集、多遗忘算法和 IID/非 IID 设置下验证攻击有效性及对干净模型效用的有限影响。
- 局限：攻击者需要获得目标模型及一定的替代数据，并依赖可提交恶意遗忘请求；不同遗忘协议的审计、请求认证和样本影响检测可能降低攻击可行性。

---
DOI: 10.1109/tdsc.2026.3703139
