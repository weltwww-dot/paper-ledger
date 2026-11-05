# Web tracking analysis on top websites through OpenWPM analytics enhancements 总结

## 基本信息
- **标题**: Web tracking analysis on top websites through OpenWPM analytics enhancements
- **作者**: Fernando J. Almenara Sotomayor、Antonio Ruiz-Martínez
- **期刊 / 会议**: International Journal of Information Security 2026
- **卷期 / 文章号**: 25，文章号182
- **发表**: 2026-11-02
- **日期来源**: 出版社官网citation_online_date与Published；正式PDF未印首发日，未拿接收日替代
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01356-5
- **PDF**: [IJIS_2026_OpenWPMTracking.pdf](papers/IJIS_2026_OpenWPMTracking.pdf)

## 一句话概括
增强OpenWPM的指纹识别与分析能力，联合测量热门网站的Cookie、网页存储、分析工具和浏览器指纹追踪。

## 问题与动机
不同追踪机制往往被分开研究，难以看清网站如何组合有状态与无状态识别手段。JavaScript指纹又可能绕过只针对Cookie的防护，检测工具自身的盲区也会影响统计。

## 方法
扩展OpenWPM-Data-Analytics的JavaScript行为判据，对热门1000网站开展统一测量，并以人工检查的已知追踪样本和隐私导向网站验证检测。区分不同指纹类别、网络请求与存储机制，保留可复核的分析依据。

## 实验与结果
热门网站中接近三分之一检出指纹机制，约半数使用网页分析工具。已知追踪验证集的120个机制实例中，52真阳性、65真阴性、3假阴性，准确率97.50%；这不是整个热门网站样本的分类准确率（PDF第12页）。

## 贡献与局限
提供可扩展的联合测量流程及追踪生态证据。Canvas规则会漏掉可见且尺寸正常的画布指纹；单次受控访问也难覆盖地域、交互和同意状态变化，观察到某API调用不等于证明全部访问均实施同样追踪。

---
DOI: 10.1007/s10207-026-01356-5 | PDF: [IJIS_2026_OpenWPMTracking.pdf](papers/IJIS_2026_OpenWPMTracking.pdf)
