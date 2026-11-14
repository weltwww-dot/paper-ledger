# A modified artificial potential field approach for real-time robot path planning via adaptive gradient neural network 总结

## 基本信息
- **标题**: A modified artificial potential field approach for real-time robot path planning via adaptive gradient neural network
- **作者**: Zisheng Chen、Ting Li、Ying Liufu
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109605
- **发表**: 2026-09-06
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版商页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109605

## 一句话概括
用自适应梯度神经网络改进人工势场路径规划，缓解陷入局部极小和狭窄通道振荡。

## 问题与动机
能否在保留人工势场实时计算优势的同时，缓解狭窄通道振荡、局部极小和目标不可达问题，并给出收敛与安全保证？

## 方法
方法组合线性引力场、分段斥力增强与切向逃逸机制；自适应梯度神经网络依据势场梯度幅度动态调节收敛速率和运动步长。作者建立全局渐近收敛及障碍不可穿越的理论分析，并在单机器人、多机器人多目标和多机器人单目标场景中进行数值及物理引擎仿真。

## 实验与结果
论文报告三个数值场景及 Webots 物理引擎仿真均生成可行、平滑且无碰撞路径，并展示狭窄通道振荡得到抑制。现有证据是仿真验证，未报告真实移动机器人上的部署结果；作者将实体平台测试、非结构化动态障碍适应性列为后续工作（PDF 第7、12页）。

## 贡献与局限
贡献在于将梯度自适应步长与切向脱困整合进势场规划，并提供收敛和安全性质的理论论证及多场景仿真支持。实际传感器误差、硬件约束、动态复杂环境和真实机器人性能仍未验证。

---
DOI: 10.1016/j.neunet.2026.109605
