# Perspicio: Safeguarding Against Non-Consensual Photo Sharing Over Social Networks 总结

## 基本信息

- **标题**: Perspicio: Safeguarding Against Non-Consensual Photo Sharing Over Social Networks
- **作者**: Xinyuan Qian、Hongwei Li、Guowen Xu et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于开放获取全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3705636
- **arXiv**: 无
- **PDF**: [TDSC_2026_Perspicio.pdf](papers/TDSC_2026_Perspicio.pdf)

## 一句话概括

Perspicio 识别照片中并未意识到自己被拍摄的人，并通过更细粒度的身份特征、动态权重与隐私授权协议降低社交网络中的非自愿照片分享风险。

## 问题与动机

社交网络让照片传播变得便捷，却可能在未经当事人同意时暴露其身份与活动。交互确认或静态访问策略通常只能管理上传者权限，难以判断照片中的其他人是否知情，因而无法在分享前提供针对性保护。

## 方法

系统整合更具个体区分力的特征，并根据拍摄场景和个人特征动态调整各特征权重，以识别照片中“不知情”的人物。随后，新协议把识别结果纳入授权与分享流程，在保持可用性的同时提高隐私保护等级。

## 实验与结果

与识别照片中不知情人物的先进方法相比，Perspicio 的预测准确率最高提高 13.2%。其在线阶段与离线阶段的处理速度分别提升 862 倍和 1,425 倍，说明方案不仅提高识别效果，也显著降低了实际部署的计算负担。

## 贡献与局限

贡献是把人物知情状态识别与照片分享授权连成完整防护链，并兼顾精度与效率。局限在于系统需处理人脸及个体特征，必须严格控制数据留存与误识别影响；遮挡、跨域场景及不愿注册用户下的公平性仍需验证。

---
DOI: 10.1109/tdsc.2026.3705636
