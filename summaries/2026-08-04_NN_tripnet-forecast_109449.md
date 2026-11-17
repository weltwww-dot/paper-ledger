# TRiP-Net: Risk-driven adaptive patching for financial time series forecasting 总结

## 基本信息
- **标题**: TRiP-Net: Risk-driven adaptive patching for financial time series forecasting
- **作者**: Wuzhida Bao、Guangyang Tian、Yuting Cao 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109449
- **发表**: 2026-08-04
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109449

## 一句话概括
TRiP-Net针对金融波动与固定patch不匹配，按局部下行风险调整分段，在两类指数预测中优于所测基线，但历史预测不代表未来收益。

## 问题与动机
如何按局部风险调整金融序列patch粒度？

## 方法
局部下行波动估计风险并自适应分段，结合动态卷积、跨度位置表示和掩码对齐预测收盘价。

## 实验与结果
NASDAQ和S&P 500作5/10/20步预测；S&P 500五步MAE 70.48、RMSE 93.62、MAPE 1.26%，风险分段消融优于固定、多尺度及随机方式（PDF第6–8页）。

## 贡献与局限
提出风险感知分段；仅两指数历史评估，样本外稳定性未确立。

---
DOI: 10.1016/j.neunet.2026.109449
