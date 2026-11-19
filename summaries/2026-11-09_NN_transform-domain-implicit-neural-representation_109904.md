# A unified framework for compact and multiresolution implicit neural representation via transform domain methods 总结

## 基本信息
- **标题**: A unified framework for compact and multiresolution implicit neural representation via transform domain methods
- **作者**: Qibiao Li、Hongbo Gao、Muyang Sun 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109904
- **发表**: 2026-11-09
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109904

## 一句话概括
框架将多尺度编码映射至傅里叶或小波域并交由专属子解码器处理，以正交正则减少冗余，在多类信号重建中兼顾质量与存储开销。

## 问题与动机
位置编码频带与网格分辨率层空间频率特性不同，常见解码器却统一处理拼接特征。作者将编码异质性对应到解码分解，以兼顾全局结构和局部细节。

## 方法
将编码拆成分量，按结构施加傅里叶、小波、球谐或恒等变换，再送入专属子解码器并求和。重建损失外加入采样内积构成的正交正则，鼓励分支互补。理论以编码诱导的Hilbert空间分析有限分解；网格辐射场以逐层信号流让高分辨率分量利用低层上下文细化。

## 实验与结果
评测Kodak图像拟合、Stanford 3D距离场及三组辐射场。Kodak模型21.00 MB，30k步得33.20 dB PSNR、0.933 SSIM；Instant-NGP为42.19 MB、33.15 dB、0.930。Synthetic-NeRF上模型22.86 MB、32.50 dB、0.957，Instant-NGP为32.96 dB、0.959。Dragon几何重建IoU为1.000，Chamfer距离0.00190。

## 贡献与局限
Lego去除正交损失后PSNR/SSIM由26.20/0.874降至25.60/0.857；Dragon的IoU由1.000降至0.995，Chamfer由0.00190升至0.00247。方法统一变换域解码与近似正交，但质量速度并非处处领先：Synthetic-NeRF略低于Instant-NGP，训练约42分钟而其约3.4分钟。正交性仅由采样正则鼓励，动态场仍待研究。

---
DOI: 10.1016/j.neunet.2026.109904
