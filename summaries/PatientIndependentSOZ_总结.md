# Patient-independent seizure onset zone localization with generalizable feature learning and multi-task supervision 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- **标题**: Patient-independent seizure onset zone localization with generalizable feature learning and multi-task supervision
- **作者**: Jinjie Guo, Tao Feng, Yiping Wang et al.
- **期刊 / 会议**: Neural Networks 2026
- **年份**: 2026
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109538
- **PDF**: [PatientIndependentSOZ.pdf](papers/PatientIndependentSOZ.pdf)

## 一句话概括

论文提出面向未知患者的癫痫发作起始区（SOZ）定位框架，将临床引导的跨频耦合（CFC）、通道自比较（SC）特征学习与癫痫检测辅助任务结合，以提高 SEEG 定位的跨患者泛化能力，同时保留发作起始的时间信息。

## 问题与动机

现有基于发作期 SEEG 的 SOZ 定位方法多采用患者特异训练，既受发作记录稀缺限制，也容易受到患者间发作动力学、皮层解剖和电极布置差异影响。单纯以空间 SOZ 标签监督，还可能忽略“最先出现病理放电”这一临床定义中的时间属性。因而，方法需要同时学习患者不变的病理表示，并利用发作起始及早期演化的时间线索。

## 方法

模型以图神经网络为基础，使用 CFC 模块捕捉不同频带之间与 SOZ 相关的异常交互，使用 SC 模块强调同一 SEEG 通道内的发作演化模式。训练时把 SOZ 定位作为主任务、癫痫检测作为辅助任务，通过多任务监督引入发作起始相关的时间信息；论文还用域对抗神经网络分析跨患者泛化，并将学习到的 CFC 表示与临床 PAC 指标进行生理学对照。

## 实验与结果

实验使用公开 OpenNeuro HUP 数据集和玄武医院私有临床数据集；HUP 子集最终包含 19 名患者。与多种基线及现有方法比较时，表 A.6 中所提模型在 HUP 上取得 ACC 62.96 ± 6.19%、SPE 59.73 ± 10.57%、F1 45.59 ± 16.04%、AUC 82.50 ± 9.78%，并在 AP@2、AP@5、AP@10 上分别为 65.79 ± 44.26%、63.68 ± 26.50%、61.28 ± 24.81%；私有数据上的多任务癫痫检测平均 ACC 为 84.57 ± 12.80%。学习到的 CFC 表示与临床 PAC 模式呈一致生理学趋势。

## 贡献与局限

主要贡献是建立患者独立的 SOZ 定位框架，将 CFC 与 SC 的临床引导表示学习和检测—定位多任务监督统一起来，并在公开与私有数据上验证跨患者鲁棒性及一定可解释性。局限包括患者间指标仍有明显波动，SOZ 标注本身存在临床判读差异，私有数据的外部可复现性有限；更大规模、多中心数据以及对标注不确定性的建模仍需进一步验证。

DOI: 10.1016/j.neunet.2026.109538

