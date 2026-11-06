# DiffuMSMO: A multi-modal diffusion model for extractive multi-modal summarization with multi-modal output 总结

## 基本信息
- **标题**: DiffuMSMO: A multi-modal diffusion model for extractive multi-modal summarization with multi-modal output
- **作者**: Jingqiang Chen、Yunyun Wang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109844
- **发表**: 2026-10-31
- **日期来源**: 出版社正式PDF首页的Available online，2027为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109844
- **PDF**: [NN_2026_DiffuMSMO.pdf](papers/NN_2026_DiffuMSMO.pdf)

## 一句话概括
用新闻领域的跨模态表征和两条扩散分支，从原新闻中抽取互相匹配的摘要句子与图片。

## 问题与动机
多模态新闻摘要既要选出信息充分的文本，也要找能补充文本的图片。把两种模态独立选择容易造成图文错配。

## 方法
先微调CoCa，让新闻图文在对比、匹配和对齐任务中形成联合表征。随后分别用扩散分支推断目标句子和图片的表征，再从原始候选中选择对应内容。

## 实验与结果
在MSMO基准上，模型取得ROUGE-1 45.37、ROUGE-2 21.42、ROUGE-L 41.68和图片精度79.05。对照方法在ROUGE-2和图片精度上仍有更高值。去掉图片扩散分支后，图片精度降至55.09（PDF第8页，表3及消融）。

## 贡献与局限
将跨模态一致性用于抽取式图文摘要，并展示两条分支的作用。评估集中在一个新闻基准，结论受原文候选质量和扩散推断开销限制。

---
DOI: 10.1016/j.neunet.2026.109844 | PDF: [NN_2026_DiffuMSMO.pdf](papers/NN_2026_DiffuMSMO.pdf)
