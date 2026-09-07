# MARSNet: A convolutional attention residual shrinkage network for RNA-protein binding site prediction 总结

## 基本信息

- **标题**: MARSNet: A convolutional attention residual shrinkage network for RNA-protein binding site prediction
- **作者**: Wei Wang, Chengyu Xing, Zhenxi Sun, Xianfang Wang, Guangsheng Wu, Yun Zhou
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108922
- **arXiv**: 无
- **PDF**: [NN_2026_MARSNet.pdf](papers/NN_2026_MARSNet.pdf)

## 一句话概括

提出融合残差收缩与双注意力机制的多尺度卷积网络 MARSNet，在 RBP-24 基准上以平均 AUROC 0.957 实现 RNA-蛋白结合位点预测的先进水平，且对小规模数据集尤为稳健。

## 问题与动机

RNA 结合蛋白（RBP）通过识别特定 RNA 元件调控转录后基因表达，准确鉴定其结合位点对理解基因调控与疾病机制至关重要。基于 CLIP 的湿实验手段（如 CLIP、HITS-CLIP、PAR-CLIP）耗时、昂贵且含噪声，促使发展序列级计算方法。已有深度学习预测器在实际中仍面临挑战：CLIP 序列的实验噪声会产生虚假信号、部分 RBP 标注数据稀缺易致过拟合，且模型输出难以关联已知结合偏好与基序。因此需要既稳健又高效的轻量架构。

## 方法

MARSNet 采用顺序多尺度窗口编码，窗口长度取 101/201/301/401（重叠 50），对 RNA 四字母表进行 one-hot 编码并处理边界，以同时捕获局部基序与长程上下文。每个窗口尺度上，核心特征提取器 ARSNet 集成 2D 卷积（学习类基序模式）与残差收缩块单元（RSBU）：残差分支通过可学习软阈值将低幅激活（多为噪声）置零，并结合轻量注意力模块 ECA（一维卷积建模跨通道交互）与 CBAM（通道+空间注意力）增强信息特征。各窗口尺度预测按固定权重 [0.1, 0.2, 0.4, 0.3] 加权融合，最终模型含 N=4 个融合组/阶段并对各组平均输出；另实现异构融合基线 MARSNet-F（简单平均 ARSNet、CNN、SACNN-BiLSTM、SACNN-BiGRU 四类骨干）以对比融合策略。实现采用 PyTorch、RMSprop（学习率 1×10⁻³、权重衰减 1×10⁻⁴）、batch size 128、训练 50 epoch，可在单张 NVIDIA RTX 3080 上完成训练。

## 实验与结果

在公开的 RBP-24 基准（24 个 RBP 数据集）上按 GraphProt 预定义划分实验，并以 CD-HIT（相似度 0.8）去冗余。最终 MARSNet 平均 AUROC 0.957、AP 0.875、MCC 0.821（Acc 0.909、Recall 0.913、Precision 0.907、F1 0.910）。消融显示单阶段多尺度融合（N=1）平均 AUC 0.949，优于各单窗口 ARSNet（101/201/301/401 分别为 0.908/0.928/0.938/0.930）；随融合阶段 N 增大性能提升并在 N=4 起饱和（N=1→5 的 AUC 为 0.949/0.954/0.956/0.957/0.958），故取 N=4。去掉 ECA 或 CBAM 后 AUC 分别降至 0.954 与 0.955；同质多尺度融合（0.957）优于异构平均基线 MARSNet-F（0.952），也优于 CNN（0.946）、SACNN-BiLSTM（0.930）、SACNN-BiGRU（0.929）。与现有方法对比（GraphProt 0.890、MCNN 0.950、CRMSNet 0.945、PIONet 0.954、RMDNet 0.952）MARSNet 平均 AUC 最高，Wilcoxon 符号秩检验显著优于 GraphProt/MCNN/CRMSNet，与 2025 年新模型持平，且在小规模数据集上表现突出。计算方面 N=4 模型参数约 0.88M、训练约 75 s/epoch、推理约 230 ms/千序列（N=1 时 55 ms）。可解释性上，卷积滤波器基序经 TOMTOM 匹配 CISBP-RNA（q<0.05），识别到 HNRNPC、TIAL1 的 U-rich 偏好；TARDBP 病例研究中，由 CBAM 空间注意力导出的显著图聚焦 UG-rich 区，模拟突变使结合概率从野生型 0.982 骤降至突变型 0.125。

## 贡献与局限

主要贡献：将残差收缩软阈值与 ECA、CBAM 双轻量注意力结合进多尺度窗口融合框架，有效抑制噪声并捕获上下文依赖的结合特征；在 RBP-24 上取得平均 AUROC 0.957 的先进性能并显著优于经典基线，对小样本数据集稳健；通过基序发现与 TARDBP 模拟突变病例研究验证了模型的生物学相关性，可识别致病突变与功能性结合决定簇，代码已开源（github.com/HNUBioinformatics/MARSNet）。局限方面，融合更多阶段会单调增加训练与推理耗时，需要权衡精度与计算成本；异构骨干简单平均（MARSNet-F）不如同质多尺度重复融合，融合策略仍需进一步探索。

---
DOI: 10.1016/j.neunet.2026.108922
