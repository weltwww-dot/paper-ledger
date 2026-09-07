# LMIRA: Load-Balanced Multi-Indicator Reputation and Authentication Security Blockchain Framework for Cross-Domain Vehicular Data Sharing 总结

## 基本信息

- **标题**: LMIRA: Load-Balanced Multi-Indicator Reputation and Authentication Security Blockchain Framework for Cross-Domain Vehicular Data Sharing
- **作者**: Rui Zhu, Zhenyu Xue, Quanzhou Hu, Weidong Xiong, Qing Ding, Zhi Jin, Sumi Helal, Yeting Chen
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-21
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 车联网与区块链安全
- **DOI**: 10.1109/TDSC.2026.3715693
- **arXiv**: 无
- **PDF**: [TDSC_2026_LMIRAVehicularBlockchain.pdf](papers/TDSC_2026_LMIRAVehicularBlockchain.pdf)

## 一句话概括

LMIRA 用边缘侧 Transformer 预测下一路侧单元域的交易负载，以多指标信誉评估车辆共享信息，并通过安全跨域认证提高车联网数据共享的吞吐和隐私保护能力。

## 问题与动机

车辆跨越不同路侧单元管理域时，车辆移动会导致区块链负载失衡、共享信息质量不可靠和认证效率下降，进而影响数据共享容量和隐私安全。静态区块链配置难以应对交易到达率、区块大小和车辆数量的持续变化。论文希望让跨域数据共享同时具备负载适应、信息可信评估和高效认证能力。

## 方法

LMIRA 首先利用边缘计算和 Transformer 预测下一个路侧单元域的交易到达率与区块大小，并据此进行负载调节。随后建立多指标车辆数据共享评价框架，从多个维度衡量共享信息质量和信誉；最后设计跨域认证机制，在保护车辆身份隐私的同时验证数据与参与方的可信性。系统在 Hyperledger Fabric、SUMO 和 Raspberry Pi 4B 实体平台上实现。

## 实验与结果

基于真实车辆轨迹的仿真和实体平台实验表明，LMIRA 相比现有方案吞吐量至少提高 3.6 倍，延迟稳定低于 0.6 秒，交易提交失败率至少降低 43.2%。结果显示，边缘预测和多指标信誉机制能改善跨域数据共享容量，认证流程也能在车辆移动和管理域切换时保持较好的适用性。

## 贡献与局限

论文将负载预测、信誉评估和跨域认证统一到面向车联网的区块链框架中，并同时进行仿真和树莓派实测。局限在于实验平台、交通轨迹和域规模仍有限，Transformer 预测误差、车辆恶意串谋、网络断连和跨链互操作可能影响实际效果；更大规模车路云协同与长期移动场景仍需验证。

---
DOI: 10.1109/TDSC.2026.3715693
