# D-TICNN: A dual encoder network with simplified transformer-involution and U-Net-based decoder for enhanced polyp and skin cancer segmentation 总结

## 基本信息
- **标题**: D-TICNN: A dual encoder network with simplified transformer-involution and U-Net-based decoder for enhanced polyp and skin cancer segmentation
- **作者**: Yassine Oukdach、Anass Garbaz、Zakaria Kerkaou 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109642
- **发表**: 2026-09-17
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109642

## 一句话概括
D-TICNN 结合简化 Transformer、位置自适应 involution、卷积—involution 细化模块与 U-Net 解码器，用于息肉和皮肤病灶分割。

## 问题与动机
息肉和皮肤病灶形态、纹理及对比度多变，边缘模糊；卷积全局建模有限，标准自注意力计算开销大。研究目标是在控制复杂度时兼顾全局语义、位置特征与多尺度定位。

## 方法
简化 Transformer 以 LayerNorm、512/256单元 MLP 和残差连接进行交互，不用多头注意力；各级 involution 按空间位置生成核并跨通道共享。CIRA 细化多尺度特征，U-Net 式解码器恢复分辨率并预测掩膜，另汇入解码特征统计量。

## 实验与结果
评估五个息肉数据集及 ISIC 2016/2017。CVC-ClinicDB 上 Transformer 与 involution 联用的 mIoU/mDice 为0.8995/0.9348，Kvasir-SEG 为0.8695/0.8991。ISIC 2017 上 D-TICNN 为89.72%/92.21%，高于 LSCS-Net 的85.88%/91.17%；息肉对比中 TransFuse 仍领先约1和3个百分点。

## 贡献与局限
双路特征与轻量位置建模在多数据集离线分割中有竞争力，消融支持 Transformer 与 involution 联用。尚无临床部署验证，当前指标不能等同诊断效益。

---
DOI: 10.1016/j.neunet.2026.109642
