# Stereo Image Coding for Machines With Joint Visual Feature Compression 总结

## 基本信息

- **标题**: Stereo Image Coding for Machines With Joint Visual Feature Compression
- **作者**: Dengchao Jin、Jianjun Lei、Bo Peng、Zhaoqing Pan、Bo Zhao、Nam Ling、Qingming Huang
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3671761
- **arXiv**: 无
- **PDF**: [TAI_2026_StereoImageCodingMachines.pdf](papers/TAI_2026_StereoImageCodingMachines.pdf)

## 一句话概括

本文提出面向机器视觉的立体图像特征压缩网络 MVSFC-Net，通过立体多尺度特征压缩模块联合消除空间、视间和跨尺度冗余，在降低码率的同时保持三维视觉任务性能。

## 问题与动机

现有图像编码研究主要面向二维图像，立体图像在存储、传输和三维分析之间的联合优化仍不充分。若直接分别压缩左右视图，会重复编码相似信息并忽略视差；若只追求视觉重建质量，又可能损害机器视觉任务。作者因此将立体图像编码用于机器视觉的任务驱动压缩作为研究问题。

## 方法

MVSFC-Net 先提取左右视图的多尺度视觉特征，再通过 SMFC 模块逐步把稀疏的立体多尺度特征变换为紧凑的联合视觉表示。SMFC 同时处理空间冗余、左右视图之间的冗余以及不同尺度之间的冗余，并利用双向条件上下文变换促进视间交互和视差补偿。压缩后的特征以码流传输，解码端直接服务于三维视觉任务，而非仅追求像素级重建。

## 实验与结果

实验比较了 MVSFC-Net 与 MPEG 推荐的机器视觉编码锚点、已有学习式立体图像压缩方法以及传统 VVC 编码标准，并在立体视觉任务与 PSNR 等失真指标下评测率失真表现。结果表明，MVSFC-Net 在压缩效率和三维视觉任务性能上均优于对比方法；高码率下，SMFC 能通过双向上下文变换实现更明显的左右视图视差补偿，低码率下虽然平坦区域增多，但仍保持任务驱动的联合表示能力。

## 贡献与局限

- 将立体图像编码用于机器视觉的任务驱动压缩，补充了二维 ICM 之外的研究场景。
- 设计 SMFC，同步建模空间、视间与跨尺度相关性，形成紧凑联合特征。
- 在压缩效率、视觉任务性能及与 VVC 的比较中验证了方法的有效性。
- 局限：方法依赖立体视图的几何和视差关系，极低码率或严重视图错配时的稳定性仍需验证；面向更多三维任务和真实传输环境的统一评价也有待扩展。

---
DOI: 10.1109/tai.2026.3671761
