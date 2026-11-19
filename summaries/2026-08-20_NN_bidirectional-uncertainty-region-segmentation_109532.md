# Bidirectional uncertainty-aware region learning for semi-supervised medical image segmentation 总结

## 基本信息
- **标题**: Bidirectional uncertainty-aware region learning for semi-supervised medical image segmentation
- **作者**: Shiwei Zhou、Xin Liu、Haifeng Zhao 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109532
- **发表**: 2026-08-20
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109532

## 一句话概括
论文提出双向不确定区域学习：用有标注数据强化高不确定区域监督，用无标注数据侧重可信区域以压制伪标签噪声，从而更充分利用困难区域信息。

## 问题与动机
半监督医学分割的伪标签错误常聚集在边界等高不确定区域。直接丢弃这些像素会同时丢失有价值的结构信息；但在无标注数据上盲目强化它们，又会放大错误监督。

## 方法
方法以预测熵估计像素不确定性，并按分位数划分区域。对有标注图像采用不确定区域学习（URL），提高困难位置的监督权重；对无标注图像采用可信区域学习（CRL），降低高不确定伪标签对训练的干扰。该策略可接入Mean Teacher、BCP和ABD等基线，分别设置区域阈值。

## 实验与结果
在ACDC、LA和PROMISE12数据集比较半监督基线。ACDC仅5%标注时，结合ABD的模型Dice为89.73%，优于原ABD的88.96%；10%标注时，结合BCP的Dice为90.40%，原BCP为88.84%。在ACDC上与BCP相比，方法FLOPs由3.49G增至3.53G，训练时间由3.15小时增至3.52小时，显示小幅额外成本。

## 贡献与局限
核心贡献是按标注状态反向处理不确定区域，既利用可靠真值攻克难点，又避免无标注噪声污染模型，并能与多种基线组合。局限是95%/99%分位阈值及权重仍属经验设定，跨数据集需调节；作者也指出尚缺少更细粒度的动态调整机制。

---
DOI: 10.1016/j.neunet.2026.109532
