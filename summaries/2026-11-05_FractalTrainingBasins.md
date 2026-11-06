# Fractal basin geometry and the limits to predictability and reproducibility in deep learning 总结

## 基本信息
- **标题**: Fractal basin geometry and the limits to predictability and reproducibility in deep learning
- **作者**: Andrew Ly、Pulin Gong
- **期刊 / 会议**: Nature Machine Intelligence 2026
- **卷期 / 文章号**: 完整在线版，待正式分页
- **发表**: 2026-11-05
- **日期来源**: Nature出版社Article网页citation_online_date；正文页为完整在线版，待正式分页
- **内容状态**: 完整 · 已基于出版社完整在线版全文完成中文六段式总结，待正式分页
- **研究方向**: 人工智能
- **DOI**: 10.1038/s42256-026-01336-3
- **PDF**: [NMI_2026_FractalTrainingBasins.pdf](papers/NMI_2026_FractalTrainingBasins.pdf)

## 一句话概括
利用分形吸引域解释为何很小的初始化扰动也可能改变神经网络最终学到的函数。

## 问题与动机
参数差别很小的初始点在训练后仍可能得到明显不同的输出。要解释这种敏感性，需要直接考察不同训练结局在初始化空间里的边界几何。

## 方法
作者先分析可解释的最小网络，再在更深网络上比较不同架构和优化器。通过测量给定扰动尺度下改变训练结局的初始化比例，估计参数空间和函数空间中的标度指数。

## 实验与结果
最小模型的相关指数估计为0.0126±0.0002（PDF第5页），说明在测量范围内减小扰动时，受影响比例下降得很慢。测试过的深层网络也呈现类似的数值特征。

## 贡献与局限
把训练敏感性与交错的吸引域联系起来，并给出可测量的指标。深层模型的结论来自有限设置下的数值证据，不能证明所有网络都有同样的边界或标度。

---
DOI: 10.1038/s42256-026-01336-3 | PDF: [NMI_2026_FractalTrainingBasins.pdf](papers/NMI_2026_FractalTrainingBasins.pdf)
