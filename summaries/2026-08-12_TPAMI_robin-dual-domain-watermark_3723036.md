# ROBIN++: Unified Copyright Protection and Tamper Localization for Diffusion Models via Dual-Domain Synergistic Watermarking 总结

## 基本信息
- **标题**: ROBIN++: Unified Copyright Protection and Tamper Localization for Diffusion Models via Dual-Domain Synergistic Watermarking
- **作者**: Huayang Huang、Siqi Zeng、Qian Wang 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15287-15300
- **发表**: 2026-08-12
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1109/tpami.2026.3723036

## 一句话概括
本文提出 ROBIN++，在扩散模型生成图像中协同嵌入稳健版权水印与易损定位水印，以同时验证来源并定位篡改区域。

## 问题与动机
生成图像水印通常需要在经历压缩、编辑等变化后仍可识别，同时又要对局部篡改敏感；把两种目标耦合在同一信号域，容易造成稳健性与定位精度之间的冲突。

## 方法
ROBIN++ 将稳健版权信号置于频域，将局部定位信号置于潜空间，并在验证阶段通过双分支检测交互利用全局频谱先验和局部篡改线索。若检测到被篡改区域，空间到频率的修正步骤用未受影响区域统计量修复潜特征，降低篡改内容对频域提取的干扰。

## 实验与结果
作者在 Stable Diffusion v2 上优化方法，并在生成图像退化、局部修补篡改和跨模型迁移设置下与基线比较。加入空间定位水印后，定位 IoU 从 0.543 升至 0.947，再加入频率到空间协同后升至 0.971；空间到频率修正使版权验证鲁棒性由 0.970 升至 0.973（PDF 第11页）。在 Stable Diffusion v2.1 上训练后迁移到 SD v1.4，ROBIN++ 的定位 F1 为 0.765（PDF 第12页）。

## 贡献与局限
该方案把版权认证与篡改定位分配到不同信号域，再通过双向信息交互联合验证，实验展示了消融收益及跨版本迁移结果。表现依赖生成模型、退化类型和攻击评测范围；更广泛的模型架构与自适应移除攻击仍是验证边界。

---
DOI: 10.1109/tpami.2026.3723036
