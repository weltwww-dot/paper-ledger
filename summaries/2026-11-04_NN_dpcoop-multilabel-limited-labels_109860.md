# DPCoOp: Dual positive context optimization for multi-label recognition with limited annotations 总结

## 基本信息
- **标题**: DPCoOp: Dual positive context optimization for multi-label recognition with limited annotations
- **作者**: Chuhan Peng、Lizhuo Zhang、Zhiqiang Pan 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109860
- **发表**: 2026-11-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109860

## 一句话概括
DPCoOp 通过以其他类别的正向证据估计类别缺失、融合双正向提示并聚合双尺度视觉特征，改善了有限标注下的多标签识别，但效果仍受数据集和部分标签设定约束。

## 问题与动机
在多标签图像只有部分正负标签时，如何利用视觉语言预训练模型减少对稀缺标注的依赖并更可靠地判断类别缺失？

## 方法
框架在 CLIP 提示学习基础上引入 OCAN 模块，以其他类别存在分数推断目标类缺失分数；Mix 模块交叉加权融合两个正向提示，并在视觉主干后加入自适应平均池化以整合双尺度特征。

## 实验与结果
论文在多个多标签识别基准及部分标注、零样本等设定下与提示学习基线比较，报告 DPCoOp 在有限标注识别上取得更好的总体结果，组件消融支持 OCAN、提示融合与双尺度视觉表征的作用（PDF 第 8–14 页）。性能依数据集、标注比例和评价设定变化。

## 贡献与局限
论文把缺失类别判断转化为利用其他类别正向语义的估计，并结合视觉尺度信息改进提示学习；对类别共现关系变化及标注噪声的跨数据集泛化仍需检验。

---
DOI: 10.1016/j.neunet.2026.109860
