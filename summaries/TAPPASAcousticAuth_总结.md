# Use Your PIN Securely: Acoustic-Based Second-Factor User Authentication With Enhanced Tap Biometrics 总结

## 基本信息

- **标题**: Use Your PIN Securely: Acoustic-Based Second-Factor User Authentication With Enhanced Tap Biometrics
- **作者**: Feiyu Han, Zelei Wang, Yuanhao Feng, Jinyang Huang, Meng Li, Panlong Yang, Zhangjie Fu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-06
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3710224
- **arXiv**: 无
- **PDF**: [TDSC_2026_TAPPASAcousticAuth.pdf](papers/TDSC_2026_TAPPASAcousticAuth.pdf)

## 一句话概括

TAPPASS 利用 PIN 输入时手指敲击产生的手部反射超声信号，提取设备绑定且用户特有的敲击生物特征，作为 PIN 的第二因素认证。

## 问题与动机

PIN 容易受到肩窥、暴力尝试和指纹残留等攻击，而单纯增加复杂度并不能证明当前操作者就是设备主人。已有敲击或行为生物特征方案又常受环境干扰、不同密码模式和长期行为变化影响。论文希望在不改变用户 PIN 习惯的前提下，获得稳定、可区分并能随时间适应的新型第二因素。

## 方法

系统在用户输入 PIN 时发射并接收手部反射的超声信号，从敲击动作中提取与设备和用户相关的声学特征。作者设计结合对抗学习与对比学习的联合深度表征框架，提升特征的区分性和一致性；同时提出轻量、可解释的逐帧增强策略提高训练效率，并用增量学习进行长期适配和新用户扩展。

## 实验与结果

实验包含 50 名参与者，TAPPASS 平均认证准确率达到 93.24%，比现有最佳方法高 14.48 个百分点。在持续 8 周的纵向研究中，认证性能波动很小，标准差仅为 1.42%，显示出较好的长期稳定性。结果说明声学敲击特征可以在 PIN 之外提供有效的设备绑定身份信息。

## 贡献与局限

论文把手部反射超声、敲击行为表征、对抗—对比学习和增量适配组合为完整的第二因素认证方案，并特别验证了长期稳定性。局限在于参与者规模和设备、输入姿态及环境覆盖仍有限，声学传感可能受到手机结构和使用场景影响；未来需要评估更强的重放、仿制、传感器污染攻击及大规模用户持续部署。

---
DOI: 10.1109/TDSC.2026.3710224
