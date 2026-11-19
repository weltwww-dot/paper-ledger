# Parameter-controlled multiscroll chaos and extreme multistability in memristive Hopfield neural network with application to secure communication 总结

## 基本信息
- **标题**: Parameter-controlled multiscroll chaos and extreme multistability in memristive Hopfield neural network with application to secure communication
- **作者**: Daxun Huang、Qiang Lai
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109909
- **发表**: 2026-11-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109909

## 一句话概括
论文构造参数可控的忆阻 Hopfield 网络，分析多卷混沌与共存吸引子，并演示其混沌序列用于图像通信。

## 问题与动机
忆阻神经网络的多卷动力学通常需额外非线性函数或改动结构，增加实现复杂度；作者寻求仅调节函数参数就能改变卷数和振幅的方案。

## 方法
在磁通控制忆阻器中嵌入调制取整函数，并作为 Hopfield 网络耦合突触，建立多卷忆阻网络。通过参数控制卷数及振幅，分析不同初值下混沌、极限环和点吸引子的共存；再用生成序列构造三维多元幅移差分混沌移位键控通信方案。

## 实验与结果
数值动力学分析配合 STM32F103 数字硬件验证，示波器展示单至四卷吸引子。通信演示传输三幅 256×256、每通道8 bit的 RGB 图像；在 M=16、Eb/N0=20 dB 的设置下，文中展示接收并恢复图像，合计 1,572,864 bit。

## 贡献与局限
贡献是用参数而非网络结构改动调控多卷动力学，并将其用于混沌载波通信演示。图像可视恢复和硬件吸引子验证支持可行性，但不能单独证明现代密码学安全；从报告实验看，攻击模型、密钥管理及与标准通信方案的全面安全比较仍有限。

---
DOI: 10.1016/j.neunet.2026.109909
