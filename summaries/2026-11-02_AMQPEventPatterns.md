# A newly generated dataset and pattern-driven approach for detecting AMQP Denial-of-Service attacks 总结

## 基本信息
- **标题**: A newly generated dataset and pattern-driven approach for detecting AMQP Denial-of-Service attacks
- **作者**: Munmun Swain、Sushant Kuril、Nikhil Tripathi 等
- **期刊 / 会议**: Computers & Security 2026
- **卷期 / 文章号**: 173（2027），文章号105225
- **发表**: 2026-11-02
- **日期来源**: 出版社正式 PDF 首页 Available online，2027 为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.105225
- **PDF**: [COSE_2026_AMQPEventPatterns.pdf](papers/COSE_2026_AMQPEventPatterns.pdf)

## 一句话概括
构建 AMQP 流量基准，并用协议事件的顺序和时间关系识别异常通信。

## 问题与动机
常见入侵检测数据集很少记录 AMQP 应用层事件。只看流量总量也容易漏掉速率较低、持续时间较长的异常，而物联网端设备的算力和内存有限。

## 方法
作者在受控测试床采集正常通信和五类拒绝服务场景，用正常事件序列学习时序特征，再根据偏离程度告警。检测器同时考察事件顺序和延迟，计算负担较小。

## 实验与结果
在统一测试数据上，事件模式分析的检测率为 98.53%，误报率为 0.30%。随机森林的检测率为 98.96%，误报率为 2.30%（PDF 第 15 页）。

## 贡献与局限
公开的协议级数据为比较检测器提供了共同基准。结果来自受控环境，低强度异常仍可能混入正常波动，对更复杂的规避行为也只有分析，尚缺专门实测。

---
DOI: 10.1016/j.cose.2026.105225 | PDF: [COSE_2026_AMQPEventPatterns.pdf](papers/COSE_2026_AMQPEventPatterns.pdf)
