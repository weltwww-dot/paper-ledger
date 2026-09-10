# Position-Sensitive painterly image harmonization 总结

## 基本信息

- **标题**: Position-Sensitive painterly image harmonization
- **作者**: Han Guo、Bolun Zheng、Qianyu Zhang、Canjin Wang、Yayun Wang、Heng Jin、Qiankun Li、Jun Yin、Guodao Zhang、Zongpeng Li
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108872
- **arXiv**: 无
- **PDF**: [NN_2026_Paper08.pdf](papers/NN_2026_PositionSensitivePainterlyHarmonization.pdf)

## 一句话概括

本文利用插入位置相关的全局与局部风格信息，改善照片对象融入绘画时的局部协调性。

## 问题与动机

绘画中的笔触、纹理和颜色混合具有空间变化，插入对象附近的局部风格可能与整幅画不同。已有方法多只对齐全局绘画风格，忽略插入位置的局部一致性。研究因此把位置作为风格协调的核心条件。

## 方法

方法提出 Position-aware Adaptive Instance Normalization（PAIN）模块，同时融合全局和局部背景风格。另设计 position-sensitive supervision 来检测局部风格不一致，并指导对象与背景在插入位置的协调。

## 实验与结果

作者在公开基准数据集上开展广泛实验，比较现有绘画图像协调方法。全文结果表明，该方法在视觉协调和相关定量评价上具有竞争力；当前全文摘要片段未提供可安全复述的完整数值，故不补写具体数字。

## 贡献与局限

贡献是把局部位置条件引入 painterly image harmonization，并联合全局与局部风格。局限是方法依赖绘画风格和插入区域的可学习分布，对极端艺术媒介、复杂遮挡和主观审美评价的适应性仍有限。

---
DOI: 10.1016/j.neunet.2026.108872

