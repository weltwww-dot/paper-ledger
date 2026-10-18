# FlowCrypt: Flow-Based Lightweight Encryption With Near-Lossless Recovery for Cloud Photo Privacy 总结

## 基本信息

- **标题**: FlowCrypt: Flow-Based Lightweight Encryption With Near-Lossless Recovery for Cloud Photo Privacy
- **作者**: Xiaohui Yang, Ping Ping, Feng Xu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing · 2026
- **发表**: 2026-07-09
- **日期来源**: 出版社正式PDF第1页Date of publication；卷期及current version不替代首次在线日期
- **内容状态**: 完整
- **内容说明**: 已对照16页正式版复核方法、实验及边界，主agent亲自审定中文
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3710932
- **版本**: 出版社正式版（Version of Record），16页，卷/期/页23/5/11215-11230
- **PDF**: [TDSC_2026_FlowCrypt.pdf](papers/TDSC_2026_FlowCrypt.pdf)

## 一句话概括

FlowCrypt把密钥驱动的图像拆分与可逆流网络结合，在无需参考图的条件下实现照片加密与近无损恢复。

## 问题与动机

部分学习式图像加密依赖外部密码模块、辅助参考图，或在处理时丢弃信息，影响恢复质量。论文希望兼顾正确密钥下的高保真恢复、错误密钥下的扰乱效果与常见失真鲁棒性。

## 方法

用PBKDF2从用户密钥派生掩码及条件映射，将图像拆成互补表示，经共享参数的可逆仿射耦合网络加解密。训练联合恢复、密文均匀性与邻像素相关性损失，并以可微噪声层模拟JPEG、模糊、噪声和裁剪（PDF第6—8页）。

## 实验与结果

在DIV2K的800张图像上训练，于DIV2K、COCO、ImageNet、CelebA-HQ评估。正式版报告正确密钥恢复的PSNR约115dB，并优于所比较的ERIE基线；指定替代模型攻击中，攻击者恢复PSNR低于15dB、SSIM低于0.3。两组数字对应不同恢复者与条件，不能混用（PDF第8—13页）。

## 贡献与局限

贡献是将密钥条件拆分、可逆网络和密文统计约束结合。浮点误差使其仍非严格无损；经验攻击及随机性指标不能替代形式化密码安全保证，实际安全还受密码熵和PBKDF2参数影响。移动端适用性没有真实手机部署实测支撑（PDF第5、9、13—15页）。

---
DOI: 10.1109/tdsc.2026.3710932 | PDF: [TDSC_2026_FlowCrypt.pdf](papers/TDSC_2026_FlowCrypt.pdf)
