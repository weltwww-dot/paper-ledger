# Shallow connection: A subtle weaving of layers with self-knowledge distillation 总结

## 基本信息
- **标题**: Shallow connection: A subtle weaving of layers with self-knowledge distillation
- **作者**: Hengyi Huang、PingFan Wu、Jianhao Zhou 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109906
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109906

## 一句话概括
论文提出 SC-SKD，以浅层旁路汇合不同深度特征生成在线自蒸馏信号，并用跨分支混合增强表征多样性。

## 问题与动机
常见自蒸馏主要让深层监督浅层，容易忽略浅层结构信息及各层表征互补。作者希望让不同深度共同参与决策，同时避免推理阶段增加模型负担。

## 方法
在层级骨干上接入浅连接模块，融合多层特征并经辅助决策头向多个层级传递教师信息；跨分支特征混合随机插值不同支路中间表征。训练结束后移除旁路与辅助头，主干独立推理。

## 实验与结果
作者在 CIFAR 系列及 ImageNet-1K 等分类基准与自蒸馏方法比较，并用消融、CKA/余弦相似度、t-SNE 和 Grad-CAM 分析表征。ImageNet-1K 上 top-1 为 70.57%，较基线高 0.86 个百分点；CIFAR-100 的可视化显示类间分离改善。

## 贡献与局限
主要贡献是把浅层到决策层的并行信息路径引入无外部教师蒸馏，且部署时不保留训练支路。局限是训练需额外计算和显存，多项蒸馏损失与手工支路拓扑带来调参负担；论文也指出权重梯度不一致可能影响收敛。

---
DOI: 10.1016/j.neunet.2026.109906
