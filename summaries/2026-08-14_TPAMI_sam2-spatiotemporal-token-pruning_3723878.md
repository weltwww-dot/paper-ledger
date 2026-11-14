# Accelerating SAM2 With Efficient Memory Attention Module via Spatiotemporal Token Pruning 总结

## 基本信息
- **标题**: Accelerating SAM2 With Efficient Memory Attention Module via Spatiotemporal Token Pruning
- **作者**: Fachrina Dewi Puspitasari、Chaoning Zhang、Avilasha Mandal 等
- **期刊 / 会议**: IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **卷期 / 文章号**: 48(11)，15605-15616
- **发表**: 2026-08-14
- **日期来源**: IEEE 正式 PDF 的 Date of publication
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1109/tpami.2026.3723878

## 一句话概括
该方法按视频分割对边界辨识和时间跟踪的需求裁剪 SAM2 记忆注意力中的冗余时空 token，以降低推理开销。

## 问题与动机
如何缩短 SAM2 随历史帧增长的记忆注意力序列，同时尽量保留维持边界质量和跨帧追踪所需的信息？

## 方法
方法为记忆 token 计算难度、时间显著性和置信偏差三类分数，并按 Transformer 层偏重空间或时间信息的差异选择保留项；剪枝在推理时直接实施，无需重新训练。

## 实验与结果
作者在 SA-V、DAVIS 2017、LVOS、YouTube-VOS 及多种提示式视频分割数据集上评估分割质量和速度。半监督视频分割中平均 J&F 仅下降约 1.2 分，提示式零样本设置下相对 SAM2 掩码或点提示约下降 0.6 分；吞吐提升约 1.7 倍，计算量最多减少 42%，记忆 token 最多压缩 87.44%（PDF 第 6–7 页）。消融显示，评分组合及保留 pointer token 均影响性能（PDF 第 7–8 页）。

## 贡献与局限
贡献是将任务相关的边界完整性和时间可追踪性纳入 token 压缩准则，并展示无需再训练即可加速 SAM2。局限是微小、细长目标和长视频中的时序漂移仍较脆弱；自适应阈值虽可改善部分边界案例，也会增加剪枝计算开销（PDF 第 9–10 页）。

---
DOI: 10.1109/tpami.2026.3723878
