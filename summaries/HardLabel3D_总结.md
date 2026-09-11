# Hard-Label Black-Box Attacks on 3D Point Clouds

## 基本信息

- 标题: Hard-Label Black-Box Attacks on 3D Point Clouds
- 作者: Daizong Liu, Yunbo Tao, Junhao Dong, Keke Tang, Pan Zhou, Wei Hu, Yew-Soon Ong
- 期刊 / 会议: IEEE Transactions on Dependable and Secure Computing 2026
- **内容状态**: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全
- DOI: 10.1109/tdsc.2026.3694723
- PDF: [TDSC_2026_HardLabel3D.pdf](papers/TDSC_2026_HardLabel3D.pdf)

- 标题: Hard-Label Black-Box Attacks on 3D Point Clouds
- 作者: Daizong Liu, Yunbo Tao, Junhao Dong, Keke Tang, Pan Zhou, Wei Hu, Yew-Soon Ong
- 期刊 / 会议: IEEE Transactions on Dependable and Secure Computing 2026
- 内容状态: 完整 · 已依据出版社正式版全文整理
- 研究方向: 信息安全

- **标题**：Hard-Label Black-Box Attacks on 3D Point Clouds
- **作者**：Daizong Liu, Yunbo Tao, Junhao Dong, Keke Tang, Pan Zhou, Wei Hu, Yew-Soon Ong
- **期刊**：IEEE Transactions on Dependable and Secure Computing, Vol. 23, No. 4, July/August 2026
- **研究方向**：三维视觉安全、黑盒对抗攻击、图谱信号处理
## 一句话概括

论文提出面向 3D 点云的 hard-label 黑盒攻击：只访问最终类别标签，先以可学习频谱融合构造决策边界，再用坐标—频谱联合、曲率感知的边界搜索生成低扰动对抗点云。

## 问题与动机

许多 3D 对抗攻击依赖模型参数、梯度或输出 logits，难以代表真实服务中的最小访问权限。hard-label 攻击只能得到最终标签，尤其难在高维点云空间中同时保持攻击成功、几何形状和局部点分布。论文还关注实际查询预算以及点云防御对攻击效果的影响。

## 方法

首先在图谱频域中把源类别与目标类别点云融合，利用可学习、类别感知的融合权重构造更接近原始形状的边界云，并通过低频约束保留整体几何。然后交替执行坐标域和频谱域 walking：频谱 walking 用较大步长跳出坐标域局部最优，坐标 walking 再细调局部扰动。几何感知边界搜索在源点云与当前边界云之间的半圆路径上利用曲率/法向信息二分搜索，减少昂贵查询。

## 实验与结果

论文在 ModelNet40 上对 PointNet、PointNet++、DGCNN、PAConv、SimpleView、CurveNet 六个模型评测，并比较多种白盒、黑盒与 hard-label 方法。方法在 CurveNet、SimpleView 等模型上显著降低扰动，报告的改进幅度最高包括 31.8% 和 17.6%；平均查询约 2405 次，且在 SOR、SRS、LPC、UPP、N2S3D 等防御下保持较强攻击性能，局部曲率、规则性和 EMD 指标也得到评估。

## 贡献与局限

论文把 hard-label 设定正式引入 3D 点云攻击，并把频谱融合、联合 walking 和曲率搜索结合起来，在不可感知性、查询效率和防御鲁棒性之间取得平衡。局限是攻击仍需数千次标签查询，并依赖点云图构造和频带超参数；对真实 LiDAR、物理世界扰动以及更强查询限制下的有效性仍需验证。

---
DOI: 10.1109/tdsc.2026.3694723
