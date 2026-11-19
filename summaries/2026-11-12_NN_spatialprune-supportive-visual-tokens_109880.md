# Spatialize before pruning: Multimodal large language model sparsification with supportive tokens 总结

## 基本信息
- **标题**: Spatialize before pruning: Multimodal large language model sparsification with supportive tokens
- **作者**: Zhong Ji、Renmanda Na、Chen Tang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109880
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109880

## 一句话概括
SpatialPrune是一种免训练的多模态大模型视觉token压缩方法。它在剪枝前保留图像token的二维空间关系，并从被删token中筛出有补充价值的内容压缩回后续层，降低视觉计算量时尽量保住问答所需信息。论文表1最后的Acc.(%)是相对未剪枝模型归一化的性能保留率，不是VQA绝对准确率。

## 问题与动机
许多视觉token剪枝方法把图像token视为一维序列，可能受位置偏差影响，删掉局部但关键的物体或关系；被剪token通常直接丢弃，也会造成信息损失。论文研究如何在无需微调的前提下，同时保留空间布局和回收有用的冗余信息，以支持图像与视频问答的高压缩推理。

## 方法
SpatialPrune先按二维空间位置进行token选择，使保留集合覆盖图像区域而非单纯依序截取。随后计算已删token与保留token的语义相似度，将不冗余且具有补充性的token筛出，再聚类并重建为少量代表token，注入后续层。方法包含空间选择与支持token压缩两个模块，并在不同视觉token保留率下评估。

## 实验与结果
作者在LLaVA等图像多模态模型和Video-LLaVA上测试多个图像、视频问答基准。LLaVA-1.5-7B保留192/576个视觉token（减少66.7%）时，表1的归一化性能保留率为98.8%，SparseVLM为97.8%；这不是绝对平均准确率。表中原始任务分数如GQA为60.5（SparseVLM 59.5），VQAv2为77.2（75.6），MME为1800（1787）。Video-LLaVA保留320/2048个token（减少84.4%）时，平均准确率为51.2%，SparseVLM为45.9%；此处是表2三个视频问答基准Acc.的平均值。

## 贡献与局限
方法将空间结构感知选择与被剪token回收结合，消融结果显示两模块合用优于单独使用；在较高压缩率下，图像及视频任务表现相对稳健。比如表中支持token压缩带来MME及POPE改善。不过极端压缩时仍有性能下降，且不同基准对相似度阈值敏感；其效果来自离线基准，实际部署收益还取决于模型结构和推理实现。

---
DOI: 10.1016/j.neunet.2026.109880
