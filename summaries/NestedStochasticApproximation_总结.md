# Beyond Likelihood Ratio Bias: Nested Multi-time Scale Stochastic Approximation for Likelihood-Free Parameter Estimation 总结

## 基本信息

- **标题**: Beyond Likelihood Ratio Bias: Nested Multi-time Scale Stochastic Approximation for Likelihood-Free Parameter Estimation
- **作者**: Zehao Li, Zhouchen Lin, Yijie Peng
- **期刊 / 会议**: Machine Learning · 2026 · 115:250
- **发表**: 2026-10-17
- **日期来源**: Crossref published-online与出版社页面核验；9月20日为录用日期而非发表日期
- **内容状态**: 完整
- **内容说明**: 已阅读正式正文、理论条件和数值实验；结论按具体仿真设定表述
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07175-y
- **版本**: 出版社正式版（Version of Record），64页
- **PDF**: [ML_2026_NestedStochasticApproximation.pdf](papers/ML_2026_NestedStochasticApproximation.pdf)

## 一句话概括

提出嵌套多时间尺度随机逼近（NMTS），避免直接相除两个带噪声的蒙特卡洛估计量，改善无显式似然条件下的参数推断。

## 问题与动机

排队系统等模拟器可以生成数据，却往往无法直接计算似然。若用似然及其导数的随机估计量作比值来估计得分函数，分母噪声会引入偏差，使常规单时间尺度更新不稳定、增加模拟样本也代价较高（PDF第1—4页）。

## 方法

用快时间尺度递推跟踪参数得分，慢时间尺度更新待估参数，避免显式随机除法。对后验推断，结合外层样本平均近似与并行内层跟踪器来优化证据下界；并扩展为似然网络和后验网络以不同频率训练的方案（PDF第8—11、25—26页）。

## 实验与结果

在最大似然、后验估计与三阶段餐饮排队模拟中比较NMTS和单时间尺度方法STS，控制样本、初始化和训练预算。所测后验参数误差改善约1—2个数量级；一个最大似然实验的平均CPU耗时为0.70秒对0.72秒。排队案例说明模拟校准可行，并非真实餐饮生产部署验证（PDF第27—34页）。

## 贡献与局限

贡献是将去比值偏差的递推与嵌套推断统一，并给出收敛性、渐近分布及速率分析。理论依赖平滑性、估计器矩条件、似然正下界和步长分离等假设；神经网络扩展还需似然逼近偏差递减。有限仿真结果不能保证任意复杂模型全局最优，也不意味着消除所有近似误差（PDF第4、12—26页）。

---
DOI: 10.1007/s10994-026-07175-y | PDF: [ML_2026_NestedStochasticApproximation.pdf](papers/ML_2026_NestedStochasticApproximation.pdf)
