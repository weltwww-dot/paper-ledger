# KSNet: Advancing autism prediction via KAN-based graph convolution and multi-source data fusion 总结

## 基本信息

- **标题**: KSNet: Advancing autism prediction via KAN-based graph convolution and multi-source data fusion
- **作者**: Chuang Wang, Dongyan Li, Sixiang Sun, Junli Liu, Yuanyuan Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108892
- **arXiv**: 无
- **PDF**: [NN_2026_KSNetAutismPrediction.pdf](papers/NN_2026_KSNetAutismPrediction.pdf)

## 一句话概括

提出基于 KAN 图卷积（KANGCN）与受试者关系卷积（SRGCN）的 KSNet 框架，融合 fMRI 脑网络与表型信息用于自闭症谱系障碍（ASD）诊断，在 ABIDE 数据集 CC200 图谱上以 89.7% 准确率、93.5% AUC 显著超越现有方法并识别出与文献一致的脑区生物标志物。

## 问题与动机

ASD 是神经发育障碍，现有诊断主要依赖行为观察与临床评估，缺乏客观生物学标志物且易受主观经验影响。静息态 fMRI 脑功能连接与脑网络分析为早期 ASD 检测提供了新途径，但主流方法存在明显局限：将 BOLD 时间序列折叠为静态连接后仅用线性变换与固定激活函数做消息传递，难以刻画脑区间的非线性交互；静态或浅层图结构、固定邻域阈值降低跨数据集鲁棒性；对个体变异与群体关系的建模不足；表型信息多以简单拼接方式融合，无法结构化利用受试者间关系；深层图网络还面临过平滑问题与多中心数据的跨站点噪声干扰。

## 方法

KSNet 是一个多源特征融合框架，流程包括脑网络构建、KANGCN 特征提取、SRGCN 受试者关系建模与分类。脑网络构建用带多头自注意力的时序编码器提取 BOLD 时间序列特征，经 FC 生成器产出非负且任务导向的功能连接矩阵，并为每个 ROI 增加可学习的位置编码。KANGCN 将常规 GCN 的固定激活替换为基于 Kolmogorov–Arnold 表示定理的可学习 B-spline 函数（三次 B 样条、grid size 为 5、[−1,1] 区间 8 个控制节点，Φ(x)=SiLU(x)·W_base+B(x)·W_spline），使每条边具备独立的非线性变换能力；随后用可学习的节点重要性评分（sigmoid 归一化）以保留比例 γ=0.7 选择关键脑区并动态压缩图，抑制噪声连接。SRGCN 依据性别、年龄（|Δage|<2）、诊断、IQ（|ΔIQ|<10）构建受试者亲和图，与 KANGCN 嵌入经高斯核计算的相似度矩阵做 Hadamard 乘积融合，形成跨个体异构关系图；堆叠多层图卷积并经可学习权重自适应融合各层表示以缓解过平滑，最后经 KAN 层输出分类概率。总损失为交叉熵 + 组损失（类内聚拢、类间分离）+ 互信息损失 + 对比损失的加权组合（α=0.3、β=0.01、γ=0.001）。

## 实验与结果

实验基于 ABIDE 多中心数据集（17 个国际站点、1112 例高质量 fMRI 与表型数据，含 539 例 ASD 与 573 例正常对照），经 CCS/CPAC 预处理，采用 AAL116 与 CC200 两套图谱、五折交叉验证与 SEN/SPEC/ACC/AUC 指标，Adam（lr 1×10⁻³、权重衰减 1×10⁻⁴）、batch size 16、500 epoch、PyTorch 与单张 RTX 3090。完整 KSNet 在 CC200 上达 SEN 91.6%、SPEC 88.6%、ACC 89.7%、AUC 93.5%，在 AAL116 上达 SEN 79.8%、SPEC 71.9%、ACC 83.7%、AUC 89.1%；相对最佳基线 PLSNet（CC200 ACC 75.9%）准确率提升 13.8 个百分点。消融显示去掉 SRGCN 后性能暴跌（ACC 72.0%、AUC 72.0%），去掉 KANGCN 后 ACC 降至 85.1%，去掉节点筛选后 SEN 略升但 SPEC/AUC 下降，说明三组件均关键。KANGCN 参数研究表明 3 层 GCN、128 隐层、grid size 5、spline order 3 为最佳配置（AUC 达 93.5%），过大的 grid size 与深层组合会出现 NaN 数值不稳定；表型消融中仅 age+gender 最优，加入 IQ（约 30% FIQ 缺失、插值引入噪声）或站点信息（17 站点分布不平衡、属元数据而非生物学特征）均使性能下降。六种 GNN 架构对比中 DFConv 表现最好。模型约 3.62M 参数（KANGCN 预测器占 3.52M），单次前向约 0.43 GFLOPs，训练约 3 s/epoch（总时长约 2.8 h），推理约 19 ms/受试者。可视化显示 KSNet 学到长程依赖连接模式，ASD 组在前中央回、缘上回、外侧枕叶皮层与额中回等区域连接显著增强，与既往 ASD 文献报告一致。

## 贡献与局限

主要贡献：提出 KANGCN，将 KAN 的可学习 B-spline 函数近似嵌入图卷积层，提升非线性脑连接建模能力并保持网络拓扑的生物学合理性；引入节点选择机制对图稀疏化并筛选判别性脑区，为 ASD 生物标志物发现提供定量证据；提出 SRGCN，通过表型与连接导出的嵌入相似度构建跨个体异构关系图，以分层融合实现多源信息深度集成；整体框架识别出的关键脑区与既有医学研究中的 ASD 生物标志物定位高度吻合，提供生物学可解释的临床诊断支持。局限方面，论文未显式评估小样本场景（但 17 中心数据集本身体现站点间异质性）；未来工作拟探索小样本与多模态数据、优化图构建与损失函数，并发展更透明、更具临床可操作性的模型。

---
DOI: 10.1016/j.neunet.2026.108892
