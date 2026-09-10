# ThermalGaussian++: Improving Alignment and Resolution for ThermalGaussian 总结

## 基本信息

- **标题**: ThermalGaussian++: Improving Alignment and Resolution for ThermalGaussian
- **作者**: Rongfeng Lu, Chi Zhu, Quan Chen, Le Zhang, Ming Lu, Tingyu Wang, Haofan Ren, Yitian Xue, Yunfei Guo, Chenggang Yan
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/TPAMI.2026.3689388
- **arXiv**: 无
- **PDF**: [TPAMI_2026_ThermalGaussianImprovingAlignmentResolution.pdf](papers/TPAMI_2026_ThermalGaussianImprovingAlignmentResolution.pdf)

## 一句话概括

论文提出 ThermalGaussian++，在 3D Gaussian Splatting 中联合建模 RGB 与热成像，并通过多模态位姿优化和联合超分辨率重建解决跨设备不对齐、热图低分辨率以及场景存储开销问题。

## 问题与动机

热成像包含人眼不可见的温度信息，但现有热场景三维重建通常依赖传统几何流程或 NeRF，难以同时兼顾重建质量、渲染速度和实际部署成本。热图纹理弱、存在拖影，导致 SfM 难以估计热相机位姿；而高分辨率热相机价格高，低分辨率输入又会限制细节。作者还指出，公开数据集缺少成对、跨视角一致且无水印的 RGB–热图数据。

## 方法

方法以 3DGS 为基础，使用 RGB 图像进行几何初始化，再将注册后的热图纳入多模态高斯学习，并加入针对 RGB/热模态的联合正则化与热成像平滑约束，以减少单一模态过拟合和冗余高斯。ThermalGaussian++进一步加入多模态位姿优化模块，直接从未对齐的 RGB–热图输入中学习相对位姿；同时用多模态联合超分辨率重建模块，从低分辨率热图恢复高分辨率热场。论文还发布 RGBT-Scenes 与更高分辨率、非对齐输入的 RGBT-Scenes++ 数据集。

## 实验与结果

实验在单张 NVIDIA 3090 GPU 上进行，渲染分辨率为 640×480，每组比较训练 30K 次迭代。评价指标为 PSNR、SSIM 和 LPIPS。对齐输入下，方法的热图平均 PSNR 比基线提高 1.3 dB，RGB 平均 PSNR 比原始 3DGS 提高 1.1 dB；未对齐输入下，相比此前方法热图 PSNR 平均提高约 5 dB。对 RGBT-Scenes++ 的低分辨率实验中，超分辨率模块使热模态 PSNR 提高约 2 dB、RGB 模态提高近 10 dB。多模态正则化后模型存储量约为直接使用 3DGS 的 8%，另一个配置也实现约 48% 的存储降低。

## 贡献与局限

贡献包括：提出可同时渲染 RGB 与热图的 3DGS 框架；用位姿优化和联合超分辨率提高非对齐、低分辨率场景的可用性；发布两个真实世界数据集并展示多模态约束对 RGB 重建的反向促进作用。局限是实验主要依赖自采集数据和固定相机/温度条件，论文未给出更广泛设备与动态场景验证；温度值查询还依赖特定色彩图—温度映射和 KNN 检索，跨设备温度标定的泛化仍待研究。

---
DOI: 10.1109/TPAMI.2026.3689388
