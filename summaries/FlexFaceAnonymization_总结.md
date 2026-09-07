# Flex-Face: Privacy-Protect Face Recognition via Flexible Identity-Consistent Face Anonymization 总结

## 基本信息

- **标题**: Flex-Face: Privacy-Protect Face Recognition via Flexible Identity-Consistent Face Anonymization
- **作者**: Ruiying Lu, Yupeng Lai, Ruimin Hu, Chunlei Peng, Nannan Wang, Xinbo Gao
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-06-16
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3704001
- **arXiv**: 无
- **PDF**: [TDSC_2026_FlexFaceAnonymization.pdf](papers/TDSC_2026_FlexFaceAnonymization.pdf)

## 一句话概括

Flex-Face 通过分层注入可识别身份信息和身份一致的人脸匿名化，在保护原始身份隐私的同时保留表情、姿态等非身份属性，并支持用户选择不同的匿名身份。

## 问题与动机

人脸识别有助于公共安全和服务系统，但普遍摄像会暴露个人面部数据，形成识别效用与隐私保护之间的矛盾。现有隐私保护图像常在视觉质量、识别准确率和匿名身份可控性之间牺牲一项或多项。论文希望生成既能被系统准确识别、又不直接泄露真实身份且更符合用户偏好的保护图像。

## 方法

框架包含可识别人脸匿名化模块和身份一致的人脸匿名化方法。前者通过分层方式将身份信息融入隐私保护图像，并与身份识别网络协同工作，以维持可识别性；后者允许选择多种用户偏好的目标身份，同时保持表情、姿态等非身份属性。整体方案围绕身份信息注入、隐私保护和视觉质量之间的平衡设计，并支持更加灵活的匿名控制。

## 实验与结果

作者在多种人脸图像数据集以及不同识别和隐私泄露场景下进行定量与定性实验。实验结果显示，Flex-Face 相较隐私保护人脸识别和可识别人脸匿名化方法具有更好的综合表现，在保持视觉质量和识别准确率的同时支持多种目标匿名身份。摘要未给出统一的具体数值，因此不补充未在摘要中明确的数字。

## 贡献与局限

论文提出了面向隐私保护人脸识别的可控匿名化范式，把身份识别效用、视觉质量和匿名身份选择统一到一个框架中。其局限在于不同人群、真实部署环境和长期身份变化下的隐私泄露风险仍需更充分验证；用户偏好与匿名身份之间的可解释控制也有进一步研究空间。

---
DOI: 10.1109/TDSC.2026.3704001
