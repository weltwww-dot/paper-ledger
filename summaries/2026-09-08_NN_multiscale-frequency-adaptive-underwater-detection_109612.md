# MFAFNet: Multiscale frequency-adaptive fusion network for domain generalized underwater object detection 总结

## 基本信息
- **标题**: MFAFNet: Multiscale frequency-adaptive fusion network for domain generalized underwater object detection
- **作者**: Yongjie Yu、Hui Chen、Chunlei Ben 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109612
- **发表**: 2026-09-08
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109612

## 一句话概括
MFAFNet以小波频率增强、交叉门控特征提取和多尺度自适应融合，提升水下目标检测在未知水域退化与域偏移下的稳定性。

## 问题与动机
水下吸收、散射、浑浊和光照变化造成图像退化，训练水域与部署水域差异会让检测特征失稳。常规多尺度融合难以同时利用全局结构、局部边缘及跨尺度语义，导致未知域定位和识别下降。

## 方法
MFAFNet由三部分组成：FAENet对输入作低/高频分解并自适应增强全局结构与局部边缘纹理，频率变换比较显示离散小波变换效果最好；FCGA结合部分卷积与空间—通道交叉门控提取鲁棒表征；MAFNet将多尺度特征统一尺寸，经级联增强与注意力交互，再自适应融合语义和细节。

## 实验与结果
在URPC2020、DUO、RUOD及S-UODAC2020评估域内、源到目标和跨数据集泛化，并另测Brackish、TrashCAN。URPC2020→DUO时AP/AP50为48.0%/74.6%，高于YOLOv11m的43.1%/68.0%；URPC2020→S-UODAC2020为28.8%/59.7%，高于RT-DETR的25.0%/52.9%。在Brackish上AP/AP50为86.0%/98.6%，TrashCAN为61.5%/76.8%；参数15.5M、FLOPs 55.2G。

## 贡献与局限
方法面向跨水域域泛化，把频域分解与门控多尺度融合结合，在多数据集跨域评估中优于所列检测基线；消融也显示小波频率变换优于不使用变换及FFT/DCT配置。评估仍基于有限公开水下数据和固定划分，真实海域设备变化、极端浑浊及持续域漂移尚需验证。

---
DOI: 10.1016/j.neunet.2026.109612
