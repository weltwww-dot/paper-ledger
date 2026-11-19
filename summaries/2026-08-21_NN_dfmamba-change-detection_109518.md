# DFMamba: Difference-enhanced and adaptive frequency-aware Mamba for change detection 总结

## 基本信息
- **标题**: DFMamba: Difference-enhanced and adaptive frequency-aware Mamba for change detection
- **作者**: Panli Yuan、Xingbiao Zhao、Renlong Hang
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109518
- **发表**: 2026-08-21
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109518

## 一句话概括
DFMamba 将差异增强、频率感知与 Mamba 序列建模结合，用于双时相影像变化检测。

## 问题与动机
既有 Mamba 变化检测模型未显式精细建模时相差异，差异提取会放大无关噪声，难以捕捉细微变化边界。

## 方法
差异增强 Mamba 融合模块 DBMF 去除双时相共有成分，提取差异对比特征；自适应频率感知模块 AFA 用可学习滤波系数生成频域信号，抑制差异增强引入的高频噪声并强化变化边界。

## 实验与结果
在 LEVIR-CD、LEVIR-CD+、WHU-CD、SYSU、CDD 五个基准与现有方法比较。LEVIR-CD 消融中基线 F1/IoU 为90.22%/82.18%，DBMF+AFA 为92.65%/86.31%；GFLOPs 从43.81降至43.14，参数量由98.12M增至99.19M，推理时间由31.22 ms增至33.22 ms。

## 贡献与局限
将差异对比提取和自适应频域抑噪结合，兼顾变化边界与冗余噪声。精度收益伴随约2 ms推理变慢；实验局限于五个遥感基准，实际跨传感器与跨地区迁移仍须另行评估。

---
DOI: 10.1016/j.neunet.2026.109518
