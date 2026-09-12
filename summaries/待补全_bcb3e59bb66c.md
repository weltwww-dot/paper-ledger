# Using Class and Domain Information to Address Domain Shift in Federated Learning 总结

## 基本信息

- **标题**：Using Class and Domain Information to Address Domain Shift in Federated Learning
- **作者**：Chien-Yu Chiou，Chun-Rong Huang，Lawrence L. Latour，Yang C. Fann，Pau-Choo Chung
- **期刊 / 会议**：IEEE Transactions on Neural Networks and Learning Systems，2026
- **研究方向**：联邦学习、域偏移与原型对比学习
- **DOI**: 10.1109/TNNLS.2026.3658584
- **PDF**: [NN_2026_ClassDomainInformationAddress.pdf](papers/NN_2026_ClassDomainInformationAddress.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文提出面向域偏移的类别—域感知联邦学习框架，在客户端分离类别特征和域特征，在服务器按域聚类并进行梯度重加权的层次聚合，从而构建更稳健的全局模型。

## 问题与动机

不同客户端常从不同设备、环境或成像条件采集同一类别数据，使本地表示混入域信息、同类跨域特征分离，单纯按数据量聚合还会让客户端数量占优的域主导全局模型。传统域适应需要集中访问多域数据，而已有原型联邦学习主要对齐类别、忽略域特征，因此需要同时改善表示学习和服务器聚合。

## 方法

客户端用 CGFS 将 backbone 特征投影为类别特征和域特征，并通过逆门控与正交分离损失抑制交叉响应；HPCL 使用两组类别/域原型及类别、域对比损失和分类损失，使同类或同域特征聚拢、异类和异域特征分离，并用持续正则稳定本地更新。服务器用本地模型参数的余弦相似度聚类推断域，先在域内再在域间聚合；GMA 权重同时考虑数据量、模型相对上一轮全局模型的角度偏差和幅度差异，随后生成全局类别与域原型回传客户端。

## 实验与结果

实验采用 Digits（MNIST、USPS、SVHN、SYN）和 Office-Caltech（Caltech、Amazon、Webcam、DSLR）两个四域数据集，在受控和偏斜两种域分配下比较 FedAvg、FPL、FedTGP 等方法。受控设置使用 20 个客户端、200 轮通信和每轮 10 个本地 epoch；偏斜设置使用 100 轮通信。相对第二优方法，所提方法在受控设置的 Digits 和 Office-Caltech 平均准确率分别高 0.8% 和 3.0%，在偏斜设置分别高 1.1% 和 1.8%；消融和 t-SNE 结果显示 CGFS/HPCL 改善跨域类别对齐，GHA 缓解聚合偏置。

## 贡献与局限

论文贡献是把类别—域解耦、异构原型对比学习和梯度感知层次聚合统一到一个联邦流程，并在受控及更贴近现实的偏斜域设置中取得最佳整体结果。局限是服务器需额外进行模型聚类、域内/域间两级聚合和原型聚类，复杂度略高；域标签由模型参数相似度间接推断，方法在真实临床多医院数据上的可靠性尚未验证，作者将降低聚合开销和临床适配留作后续工作。
