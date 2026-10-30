# Beyond membership inference: Distributional leakage in diffusion models 总结

## 基本信息
- **标题**: Beyond membership inference: Distributional leakage in diffusion models
- **作者**: Sergio Barezzani、Pasquale Coscia、Stefano Ferrari、Vincenzo Piuri
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105214
- **发表**: 2026-10-24
- **日期来源**: 出版社正式PDF首页Available online；2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105214
- **PDF**: [COSE_2026_DiffusionDistributionalLeakage.pdf](papers/COSE_2026_DiffusionDistributionalLeakage.pdf)

## 一句话概括
将检索偏好、补全重建差距和前景定位结合起来，审计扩散模型对训练相关分布的偏好，补充单一成员推断分数无法覆盖的隐私风险。

## 问题与动机
成员推断效果会受数据来源和语义差异影响；攻击得分低也不足以说明生成模型没有保留训练相关信息，需要从多种可观测行为审计分布偏好。

## 方法
在狗和车辆两个语义域构造成员代理集与外部集，借助CLIP、DINOv2比较生成样本的检索邻近性；用遮挡补全后的SSIM、PSNR衡量重建差距，并用前景分离检查泄漏信号的位置。

## 实验与结果
三种Stable Diffusion变体在多项检索与重建分析中表现出训练相关分布偏好。表2中特定同数据设置的成员推断AUC为0.999，改用LAION代理成员测试后为0.761或0.798，说明高攻击得分对数据构造敏感，不能直接外推为真实训练样本识别率（PDF第4—9页，表2—3）。

## 贡献与局限
提供互补的分布泄漏审计指标，并揭示前景语义与数据来源的影响。LAION筛选集只是未知真实训练分布的代理，正检索或重建差距不证明逐字记忆；多分析共用同一基准，其一致性不构成统计独立证据，结论也受选定模型和嵌入空间限制（PDF第12—13页）。

---
DOI: 10.1016/j.cose.2026.105214 | PDF: [COSE_2026_DiffusionDistributionalLeakage.pdf](papers/COSE_2026_DiffusionDistributionalLeakage.pdf)
