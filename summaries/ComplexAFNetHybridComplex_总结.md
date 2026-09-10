# Complex AFNet: A Hybrid Complex-Valued Deep Network for Atrial Fibrillation Detection 总结

## 基本信息

- **标题**: Complex AFNet: A Hybrid Complex-Valued Deep Network for Atrial Fibrillation Detection
- **作者**: P S Pritish Kumar Mahali, Diptiman Mohanta, Tushar Sandhan
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-03-06
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TAI.2026.3671218
- **arXiv**: 无
- **PDF**: [TAI_2026_ComplexAFNetHybridComplex.pdf](papers/TAI_2026_ComplexAFNetHybridComplex.pdf)

## 一句话概括

论文提出 C-AFNet，将 ECG 片段转为 GASF/GADF 图像并分别作为复数输入的实部与虚部，通过实值—复值混合卷积建模幅度与相位耦合，以提高房颤检测的准确性和可解释性。

## 问题与动机

房颤，尤其是短暂、间歇性的阵发性房颤，容易在常规临床检查中漏检。依赖 R-R 间期等手工节律特征的方法难以捕捉细微形态，而多数深度模型在实值域中把幅度和相位信息分开处理，忽略了二者的耦合关系。作者因此希望用复值表示保留 ECG 的互补时序信息，并兼顾临床解释。

## 方法

模型先用 Gramian Angular Summation Field（GASF）和 Gramian Angular Difference Field（GADF）把一维 ECG 片段编码为二维几何表示，再将两者作为复值输入的实部和虚部。C-AFNet 交替使用实值卷积层与复值卷积层，结合改进 ReLU、残差连接和双流归一化，在较稳定的训练基础上提取相位敏感特征。Grad-CAM 与 integrated gradients 用于分析模型关注的区域和两种 GAF 表示的类别作用。

## 实验与结果

在包含 1436 条 ECG 记录的 PhysioNet AF 数据集上，C-AFNet 达到 95.63% 测试准确率、96.43% 精确率、92.05% 召回率和 94.15% F1，相比现有方法分别提高 1.52 个百分点的准确率和 2.1 个百分点的 F1。模型在 MIT-BIH AF 数据库和 MIMIC PERform AF 数据集上进行外部泛化测试；解释性分析显示，正常节律判断更关注 GADF，房颤判断更关注 GASF。模型计算量为 20.41 GFLOPs，优于所比较模型的综合表现但不属于轻量网络。

## 贡献与局限

贡献在于提出把 GASF/GADF 作为复值分量的混合复值 CNN，并通过外部数据、消融实验和 Grad-CAM/IG 同时验证性能、泛化与可解释性。局限是复值训练需要专门的初始化和归一化，20.41 GFLOPs 可能限制超低功耗边缘部署；全文实验也尚未替代大规模临床验证。后续可面向边缘优化、更多心律类别、多模态输入和无标注 ECG 预训练。

---
DOI: 10.1109/tai.2026.3671218
