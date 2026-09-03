# Hard-Label Black-Box Attacks on 3D Point Clouds 总结

## 基本信息

- **标题**: Hard-Label Black-Box Attacks on 3D Point Clouds
- **研究方向**: 信息安全
- **作者**: Daizong Liu, Yunbo Tao, Junhao Dong, Keke Tang 等 (et al.)
- **期刊 / 会议**: IEEE TDSC 2026
- **发表**: 2026-05-19
- **DOI**: 10.1109/tdsc.2026.3694723
- **arXiv**: 2412.00404
- **PDF**: [TDSC_2026_HardLabel3D.pdf](papers/TDSC_2026_HardLabel3D.pdf)

## 一句话概括

提出首个面向 3D 点云的 hard-label 黑盒攻击方法：攻击者只能获得模型的最终预测标签，通过频谱感知的决策边界算法生成高质量对抗点云。

## 问题与动机

深度传感器在 3D 安全关键场景中日益普及，点云模型已被证明易受对抗攻击。现有 3D 攻击几乎都假设白盒设置或可访问输出 logits 的黑盒设置，严重依赖受害模型的参数或中间输出，在真实场景（拿不到模型细节）中难以部署。hard-label 设置更贴近现实，但此前在 3D 领域基本空白。

## 方法

基于频谱感知的决策边界算法：先用可学习的频谱融合策略（learnable spectrum-fusion strategy）在频谱域融合不同类别的点云，构造不破坏原始几何的中间样本，构建类别感知的决策边界；再设计迭代的坐标-频谱联合优化（iterative coordinate-spectrum optimization），配合曲率感知的边界搜索（curvature-aware boundary search）沿决策边界移动，用微小扰动生成对抗点云，并提升查询效率。

## 实验与结果

在 ModelNet40（12,311 个 CAD 模型）上评测。攻击在多种 3D 架构上实现显著扰动缩减：在 CurveNet 上改进 31.8%，在另一架构上改进 17.6%；扰动幅度小于现有黑盒方法，与白盒方法持平；面对几何类防御（如 SRS）时仍保持性能优势，差距最高 21.1%（数字来自原文）。

## 贡献与局限

- 贡献一：首次将 hard-label 黑盒设置引入 3D 点云对抗攻击，贴近真实部署场景。
- 贡献二：频谱融合决策边界 + 曲率感知坐标-频谱迭代优化，兼顾攻击成功率与不可感知性。
- 局限：仍需多次标签查询，代价高于白盒；几何防御下优势有所收窄（最高差距 21.1%），更鲁棒的防御与攻击仍是开放问题。

---

DOI: 10.1109/tdsc.2026.3694723
