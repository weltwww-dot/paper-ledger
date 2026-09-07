# ITS-ShipFormer: An Informative Token Selection Former for SAR Ship Recognition 总结

## 基本信息

- **标题**: ITS-ShipFormer: An Informative Token Selection Former for SAR Ship Recognition
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Neural Networks and Learning Systems 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tnnls.2026.3661083
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

Ship automatic target recognition (ATR) in synthetic aperture radar (SAR) images plays a crucial role in maritime domain awareness. However, the sea clutter interference may make the model fail to focus on informative ship target regions for recognition. All existing SAR ship ATR models use the entire SAR ship image as input. But not all regions in SAR ship images contribute positively to recognition. However, the intraclass diversity and interclass similarity make the SAR ship ATR task more challenging. In this study, we propose a novel transformer-based architecture that addresses the two core challenges, named informative token selection former (ITS-ShipFormer). ITS-ShipFormer selects and guides the model's attention to the informative token of the ship target regions. The ITS-ShipFormer consists of the multihead dynamic local convolution (MHDLC) block in the early stages, transformer blocks equipped with a sea clutter suppression module (SCSM) in the latter stages, and a discriminative hybrid loss. SCSM automatically distinguishes the informative ship tokens and useless sea clutter tokens by two carefully designed strategies. In response to the other challenge, MHDLC is designed to enhance the feature extraction ability, and the hybrid discriminative loss is proposed to add constraints on the CLS token and the informative tokens simultaneously. The experimental results on benchmark datasets OpenSARShip and FUSAR-Ship jointly verify the effectiveness of our design. Different from previous works introducing the transformer structure in ITS-ShipFormer utilizes the overlooked innate and unique advantages of the transformer structure to address our challenge.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tnnls.2026.3661083
