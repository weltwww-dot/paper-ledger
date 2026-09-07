# Can Vibration Patterns Identify Users? Authentication for Smartphone-Watch Collaboration 总结

## 基本信息

- **标题**: Can Vibration Patterns Identify Users? Authentication for Smartphone-Watch Collaboration
- **作者**: Zicheng Cui, Zhihai Yang, Zhiquan He, Chenxu Kong, Jianhua He, Jianxin Li, Pinghui Wang, Zhiquan Liu
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-06-05
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3700835
- **arXiv**: 无
- **PDF**: [TDSC_2026_VIPVibrationAuthentication.pdf](papers/TDSC_2026_VIPVibrationAuthentication.pdf)

## 一句话概括

论文提出 VIP 双终端身份认证系统，利用智能手机与智能手表在自然触摸过程中的振动传播差异识别用户，并通过 TouchFormer 融合跨设备、异步的多轴响应信号。

## 问题与动机

密码、指纹等传统认证方式容易受到伪造、肩窥和重放攻击影响，且凭据泄露后难以持续区分真实用户。已有行为生物特征方案常依赖特定交互任务，生理特征方案又可能需要专用传感器。论文希望利用商用手机和手表已有的振动马达与惯性传感器，在自然交互中获得兼顾实用性和抗攻击性的持续身份信息。

## 方法

VIP 由双终端振动马达主动产生激励，并用加速度计、陀螺仪和磁力计采集手部—腕部传播响应。系统从多轴信号中提取能反映个体组织结构与微动态行为的差异特征。作者设计 TouchFormer，对方向敏感特征进行建模，并通过动态对齐和关键时刻的时间补偿整合不同设备上的异步响应，形成跨设备认证表示。

## 实验与结果

作者在真实场景下构建了包含 30 名用户的多设备数据集。相较已有方法，VIP 的平均认证准确率提升 5.65%；在模拟攻击和重放攻击下，误接受率分别为 1.55% 和 2.71%，平均比对比方法低 0.61 和 0.28 个百分点。实验还显示系统在不同品牌设备和不同认证场景下保持较稳定的表现。

## 贡献与局限

论文将手腕结构差异、触摸微动态与手机—手表协同传感结合起来，提出了无需额外专用硬件的振动认证方案，并通过 TouchFormer 解决跨设备信号对齐问题。局限在于当前人群规模和生理分布仍有限，振动刺激的长期隐蔽性以及用户生理状态变化造成的分布漂移仍需研究；未来还需要验证多终端扩展和高风险操作中的持续再认证。

---
DOI: 10.1109/TDSC.2026.3700835
