# FA-Mamba: frequency attention driven Mamba for multimodal remote sensing classification 总结

## 基本信息

- **标题**: FA-Mamba: frequency attention driven Mamba for multimodal remote sensing classification
- **作者**: Danian Yang, Daixun Li, Jitao Ma, Yibing Lu, Yunsong Li, Leyuan Fang, Weiying Xie
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108931
- **arXiv**: 无
- **PDF**: [NN_2026_FAMambaRemoteSensing.pdf](papers/NN_2026_FAMambaRemoteSensing.pdf)

## 一句话概括

FA-Mamba 将频域注意力与线性复杂度的 Mamba 结构结合，用于多模态遥感分类中的互补特征融合。

## 问题与动机

不同遥感模态中的噪声和冗余会阻碍融合。Transformer 的计算成本较高，Mamba 虽提高效率，却主要建模时空域，频域信息利用不足，限制了融合表示的判别性。

## 方法

FA-Mamba 以 Mamba 为主干并引入频率注意力，增强互补的频域特征。论文还设计协调融合注意力，通过沿不同方向整合空间提示来捕获模态间长程关联，同时保持线性复杂度。

## 实验与结果

论文在三个公共多模态遥感数据集上进行实验，报告相对先进方法取得更好性能，总体平均精度达到 95.84%。实验还用于验证频率模块、融合模块和计算效率设计的作用。

## 贡献与局限

贡献是将频域建模引入 Mamba 式多模态遥感分类，并兼顾效率和全局融合。局限是结果依赖所选遥感数据集与模态配准质量，跨传感器、跨区域和极端噪声条件仍需更多验证。

---
DOI: 10.1016/j.neunet.2026.108931
