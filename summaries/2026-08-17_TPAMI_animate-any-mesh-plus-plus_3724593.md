# AnimateAnyMesh++: A Flexible Feed-Forward Framework for High-Fidelity Text-Driven Mesh Animation 总结

## 基本信息
- **标题**: AnimateAnyMesh++: A Flexible Feed-Forward Framework for High-Fidelity Text-Driven Mesh Animation
- **作者**: Zijie Wu、Chaohui Yu、Fan Wang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，13802-13816
- **发表**: 2026-08-17
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3724593

## 一句话概括
AnimateAnyMesh++ 通过扩充动态网格数据、改进网格时序压缩和 rectified-flow 生成器，实现可变长度的文本驱动网格动画。

## 问题与动机
在 4D 训练数据稀缺且网格拓扑和动作长度多变时，如何从文本为任意三维网格生成细节稳定、时间连贯的动画？

## 方法
作者将 DyMesh-XL 的动态网格身份数从 6 万扩展至 30 万，重设计带拓扑感知注意力和顶点法线特征的 DyMeshVAE-Flex，并用分块轨迹压缩处理长序列、以时间相关梯度权重平滑块间衔接。rectified-flow 生成器同步支持可变长度训练与推理。

## 实验与结果
论文与多类 4D 生成方法比较，并评估不同序列长度和模块消融。相对前作 AnimateAnyMesh，方法同时提高运动幅度（AMD 0.0043 对 0.0035）、降低局部刚性误差（2.7×10⁻⁵ 对 3.0×10⁻⁵）和自交率（0.37% 对 0.54%）（PDF 第 9 页）。统一模型在训练未见的 48 帧长度上表现与训练长度基本持平（PDF 第 10 页）。

## 贡献与局限
贡献是扩展动态网格数据集并联合改善长序列压缩、局部几何保真和跨块时间连续性。局限是可用 4D 动态数据仍远少于图像、视频或静态 3D 数据，而且自动生成的动作描述质量不足会限制文本对齐能力（PDF 第 12–13 页）。

---
DOI: 10.1109/tpami.2026.3724593
