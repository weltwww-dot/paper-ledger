# Intermittent discrete adaptive event-triggered synchronization of state-dependent switching neural networks and its application 总结

## 基本信息
- **标题**: Intermittent discrete adaptive event-triggered synchronization of state-dependent switching neural networks and its application
- **作者**: Xiaoman Liu、Lianglin Xiong、Xiaodi Li 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109566
- **发表**: 2026-08-30
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109566

## 一句话概括
论文以间歇运行和离散自适应事件触发协调含时滞、半马尔可夫跳变的切换神经网络，给出均方指数同步的充分条件。

## 问题与动机
状态依赖切换网络同时受到随机模式变化与时变延迟影响，频繁监测和固定触发阈值容易增加通信与控制开销，如何让资源使用随同步误差调整？

## 方法
每个时间窗开始时根据同步误差决定激活宽度，仅在激活区间的离散采样点检测事件，并依据当前与上次传输状态的差异更新阈值。研究为激活和休眠区间构造不同的Lyapunov–Krasovskii泛函，将同步充分条件表述为线性矩阵不等式；正采样间隔排除了无限密集触发。

## 实验与结果
两组数值仿真验证同步，另用Baboon、Peppers展示图像加解密。无半马尔可夫跳变的比较算例中，平均控制周期ACP为0.4015，模式依赖自适应事件触发基线为0.2381，采样数据控制为0.0862；ACP按总受控时长除以触发次数，越大表示触发更稀疏。

## 贡献与局限
贡献是联合调整激活时长和触发阈值，并在指定模型假设下证明同步。局限是证据主要来自低维数值算例，理论依赖有界且全局Lipschitz连续的激活函数等条件；图像熵和像素相关性只能说明有限统计性质，不能证明密码系统安全。

---
DOI: 10.1016/j.neunet.2026.109566
