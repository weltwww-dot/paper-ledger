# Reservoir computing with neural activity inputs predicts behavior and neural dynamics in mouse decision-making 总结

## 基本信息

- **内容状态**: 完整 · 已基于全文完成中文六段式总结
- 标题：Reservoir computing with neural activity inputs predicts behavior and neural dynamics in mouse decision-making
- 作者：Yutaro Ueoka, Hayato Maeda, Shuo Wang, et al.
- 期刊 / 年份：Neural Networks / 2026
- 研究方向：人工智能
- DOI：10.1016/j.neunet.2026.109584
- PDF：[HybridInputReservoirMouse.pdf](papers/HybridInputReservoirMouse.pdf)

## 一句话概括

论文提出 hybrid-input reservoir computer（HRC），把小鼠行为任务输入与记录到的神经 spike 活动共同输入 reservoir，用于预测身体运动并探查未记录神经动力学。

## 问题与动机

全脑神经活动难以完整测量，而只使用任务变量的人工神经网络又缺少生物学背景，难以反映真实决策回路。作者希望利用部分已记录神经活动，通过 reservoir 的内部动力学扩展表示，从而改善行为预测并获得对未记录活动的可检验线索。

## 方法

作者比较只接收任务相关输入的 artificial-input RC（ARC）和额外接收小鼠神经活动的 HRC。HRC 使用来自皮层或皮层下区域的 spike 输入，内部连接保持随机且不训练，只训练输出权重；研究通过身体运动预测、不同脑区和 spike 数量、神经群体解码、近/远神经元比较及伪失活分析，评估外部神经输入和内部生成活动的作用。

## 实验与结果

研究使用小鼠头固定音调频率辨别任务的数据；14只雄性小鼠中有6只记录了身体运动，模型按 session 以前80%训练、后20%测试。HRC使用皮层或皮层下 spike 输入时，身体运动预测优于 ARC；改进不仅来自额外输入，也来自 HRC 内部生成的活动。HRC 单元的活动与记录神经元更接近，并呈现与任务事件和选择相关的时间模式，提示其可能包含难以直接记录的神经活动成分。

## 贡献与局限

论文展示了将真实神经活动注入简单 reservoir、以数据增强方式扩展神经动力学表示的可行性，并把行为预测与潜在未记录活动联系起来。局限是记录神经元数量、脑区覆盖和任务范围有限，伪失活结果与光遗传抑制并不完全一致；随机固定内部连接和部分固定超参数也限制了生物学解释，仍需更多脑区记录、动物实验和可训练或 connectome-based reservoir 验证。

DOI: 10.1016/j.neunet.2026.109584
