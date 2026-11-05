# DPDA: A dual-path domain adaptation method for cross-terrain real-time attack detection in mobile robots 总结

## 基本信息
- **标题**: DPDA: A dual-path domain adaptation method for cross-terrain real-time attack detection in mobile robots
- **作者**: Yu Wang、Zhitao He、Yongyi Chen 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206（2027），文章号109848
- **发表**: 2026-11-01
- **日期来源**: 出版社正式PDF Available online；2027仅为卷期年份
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109848
- **PDF**: [NN_2026_DPDARobotAttack.pdf](papers/NN_2026_DPDARobotAttack.pdf)

## 一句话概括
融合传感器时域与频域特征并对齐多个目标域，降低移动机器人跨地形攻击检测的分布偏移。

## 问题与动机
单一地形训练的检测器可能把正常地形扰动误报为攻击。仅对齐一个目标地形，又可能学习到地形特有噪声而非稳定攻击特征。

## 方法
DPDA设置时频双路径，用时频关联器与双向交叉注意力融合特征，再以互惠原型漂移机制推动两个目标域原型靠近。通过真实机器人平台及跨数据集实验比较跨地形适应。

## 实验与结果
表3中FT到GT与FT到ST的检测准确率分别为0.987、0.983，F1为0.984、0.980。CTAD与SPMD双向迁移也显示改进；这些数值对应所构造攻击和域适应协议，不是所有现实攻击的防护成功率（PDF第7—8页）。

## 贡献与局限
联合多模态特征与双目标域对齐，提供机器人实验。模型需要目标域数据参与适应，不能等同完全未知场景的零样本泛化；地形、平台和攻击生成范围限制外推，检测准确率也不直接保证闭环控制安全。

---
DOI: 10.1016/j.neunet.2026.109848 | PDF: [NN_2026_DPDARobotAttack.pdf](papers/NN_2026_DPDARobotAttack.pdf)
