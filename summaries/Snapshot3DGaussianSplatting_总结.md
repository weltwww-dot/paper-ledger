# Snapshot 3D Gaussian Splatting for Miniature Scenes 总结

## 基本信息

- **标题**: Snapshot 3D Gaussian Splatting for Miniature Scenes
- **作者**: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye
- **期刊 / 年份**: IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026
- **研究方向**: 计算摄影、三维重建与新视角合成
- **DOI**: 10.1109/TPAMI.2026.3688999
- **PDF**: [TPAMI_2026_Snapshot3DGaussianSplatting.pdf](papers/TPAMI_2026_Snapshot3DGaussianSplatting.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

本文提出一种由单摄像机和成对平面镜组成的快照式全环绕成像系统，并将预标定的虚拟相机视图与 3D Gaussian Splatting（3DGS）结合，用于从稀疏同步视图重建微型场景并合成新视角。

## 问题与动机

毫米至厘米尺度的微型场景常需要高倍率成像，但宏观镜头景深浅、纹理有限，导致传统 photogrammetry 和依赖场景特征的 SfM/COLMAP 难以稳定工作。若逐个移动相机采集，还难以处理动态对象，因此论文希望在一次曝光中获得覆盖 360°、且具有可靠几何标定的多视图输入。

## 方法

作者把成对镜面的设计写成 viewpoint mapping 问题，用镜面法向和位置求解目标虚拟视点；两个连续反射既能折叠光路，也能保持虚拟相机坐标系的 handedness。系统把 8 对镜面布置在两个嵌套八边形棱锥上，生成 8 个同步虚拟视图，并用非对称圆点靶标预标定相机参数。重建阶段以 3DGS 表示场景，在颜色损失之外加入 visual hull 深度约束：对位于凸包外的深度偏差施加更大权重，同时减弱凸包内部因凹面可能产生的偏差。

## 实验与结果

合成实验包含 15 个不同纹理和几何复杂度的场景，以 8 个参考视图合成 24 个新视图，并与 Hierarchical 3DGS、FSGS、DNGaussian、SparseGS 比较 SSIM、PSNR 和 LPIPS。作者报告该方法在定性和定量结果上均优于这些稀疏视图方法；visual hull 深度在低纹理场景上通常优于单目深度，但对大面积凹面场景，单目深度可能更好。真实场景中微型物体尺寸约为 0.5–5 cm，约 1 mm 的细结构也能被恢复；系统还展示了发芽植物和约 0.5 cm 瓢虫的动态新视角合成，8 视图重建平均约需 2 分钟。

## 贡献与局限

贡献包括：给出成对平面镜的视点映射与覆盖范围分析；实现可定制的同步全环绕微型场景成像原型；提出基于 visual hull 的加权深度损失以改善稀疏视图 3DGS。局限在于镜面对数量、单视图视场角和空间采样存在权衡，重建对精确标定敏感，visual hull 对凹面细节并不总是理想；未来可研究重叠虚拟视图和时间约束。DOI: 10.1109/TPAMI.2026.3688999
