# PD²Net: A Prototype-Guided Generative Copy-Move Forgery Image Detection and Distinguishment Framework 总结

## 基本信息

- **标题**: PD²Net: A Prototype-Guided Generative Copy-Move Forgery Image Detection and Distinguishment Framework
- **作者**: Jingyu Wang、Jie Nie、Niantai Jing et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于开放获取全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3699314
- **arXiv**: 无
- **PDF**: [TDSC_2026_PD2Net.pdf](papers/TDSC_2026_PD2Net.pdf)

## 一句话概括

PD²Net 以可学习的源区域和篡改区域原型为先验，构造角色受约束的生成式表示，从而同时定位并区分复制—移动伪造中的两个同分布区域。

## 问题与动机

复制—移动伪造把同一图像中的源区域复制到另一位置，因此源区与篡改区具有近乎相同的数据分布。现有判别式方法缺少明确角色约束，往往能发现相似区域，却难以稳定判断哪一块是来源、哪一块经过篡改。

## 方法

方法引入两个独立可学习原型，分别表示源区和篡改区先验，并通过原型—特征交互迭代优化角色受约束表示。Suspect Region Selection 与 Suspect Region Re-identification 模块进一步删除假阳性像素，形成原型引导的对象级精细目标。

## 实验与结果

作者在 USC-ISI、CASIA v2.0 和 CoMoFoD 数据集上进行了广泛实验，结果支持该框架在复制—移动伪造检测与源/篡改区域区分上的有效性和稳健性。公开摘要未列出统一的具体指标，因而不额外推断数值优势。

## 贡献与局限

贡献是把角色原型和生成式表示引入同分布伪造区域区分，并以两级疑似区域精炼降低假阳性。局限是评估集中于既有数据集；面对生成式编辑、强后处理、跨数据集分布变化及超高分辨率图像时仍需验证。

---
DOI: 10.1109/tdsc.2026.3699314
