# Fixed-time synchronization of clifford biquaternion neural networks with two-sided coefficients and application to multispectral image protection 总结

## 基本信息
- **标题**: Fixed-time synchronization of clifford biquaternion neural networks with two-sided coefficients and application to multispectral image protection
- **作者**: Chenyang Li、Yanlin Zhang、Kit Ian Kou 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109528
- **发表**: 2026-08-20
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109528

## 一句话概括
论文为双侧系数 Clifford 双四元数神经网络设计固定时间同步控制，并演示同步状态用于多光谱图像保护。

## 问题与动机
非交换超复数乘法下，双侧系数网络具有左右交互结构，常规复数模型难以统一表达；同步收敛时间若依赖初始误差，也难给出统一上界。

## 方法
用八维 Clifford 双四元数表示网络并拆分为四个复子代数子系统，设计广义复符号控制器，推导不依赖初始同步误差的固定时间上界；并与指数型、有限时间控制作理论比较。

## 实验与结果
二神经元和四神经元案例及确定性非均匀网络数值实验支持理论条件；测试不同初始误差时，提出控制器在所测设置中达到阈值的时间最短。图像保护实验在盐椒噪声密度 5×10⁻⁴ 时，平均 PSNR 37.170 dB、平均 UACI 0.042653、正确像素 99.854%。

## 贡献与局限
给出适用于非交换双侧系数网络的固定时间同步条件，并展示超复数状态在多光谱图像保护中的用法。图像保护演示不证明抗密码分析能力；噪声鲁棒指标只对应所列扰动密度和该实验方案。

---
DOI: 10.1016/j.neunet.2026.109528
