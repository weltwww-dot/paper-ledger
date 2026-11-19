# Multistability of delayed recurrent neural networks with piecewise non-monotonic activation functions and its applications to associative memory 总结

## 基本信息
- **标题**: Multistability of delayed recurrent neural networks with piecewise non-monotonic activation functions and its applications to associative memory
- **作者**: Rumeng Wang、Guici Chen、Shiping Wen 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109644
- **发表**: 2026-09-15
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109644

## 一句话概括
论文构造带可调振荡频率的分段非单调激活函数，证明其可提高时滞递归神经网络的平衡点与稳定记忆状态数量，并将其用于噪声下的联想记忆。

## 问题与动机
既有时滞递归网络常用单调或饱和激活函数，稳定平衡点数量受分段数限制，若单纯增加分段又会提高结构复杂度。作者研究能否通过激活函数内的振荡机制扩展多稳态结构，并在稳定性、参数扰动和记忆提取方面给出理论与数值依据。

## 方法
作者设计余弦型分段非单调激活函数，用频率参数控制状态空间的振荡区间；借助 Poincaré–Miranda 定理构造平衡点，并结合 Lipschitz 条件和局部渐近稳定性分析证明其存在与稳定。理论进一步给出：在适当耦合条件下，n 个神经元可有至少 (4k+2)n 个平衡点，其中 (2k+2)n 个局部渐近稳定。随后以二维网络仿真、耦合参数扰动及联想记忆实验检验稳定状态、吸引域和精确回忆表现。

## 实验与结果
例1取 k=1、激活函数 cos(2s)，二维系统有36个平衡点、16个稳定点；扫描 b∈[0.01,0.52]、c∈[0.01,0.26]时稳定点数保持16，所测初值收敛率100%。独立例2取 k=2、cos(4s)，稳定点表列36组坐标。噪声模式可恢复，容量和经验吸引域优于分段线性网络。

## 贡献与局限
工作以可调振荡频率扩展多稳态容量，给出平衡点和局部稳定点的理论下界，并用参数扰动、联想记忆仿真验证。测试中其容量和经验吸引域优于分段线性网络；结论依赖特定激活函数及耦合条件，数值例子集中于低维系统。

---
DOI: 10.1016/j.neunet.2026.109644
