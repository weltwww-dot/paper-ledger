# Vehicle-Side Lightweight Conditional Anonymous Double Authentication Framework With Password Robustness in VANETs

## 基本信息

- **标题**: Vehicle-Side Lightweight Conditional Anonymous Double Authentication Framework With Password Robustness in VANETs
- **作者**：Yangfan Liang、Zhiguo Wan、Yiming Chen、Zhiqiang Zhao、Gao Liu、Zhiquan Liu、Hong Sun、Yining Liu
- **期刊 / 会议**：IEEE Transactions on Dependable and Secure Computing 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：信息安全
- **DOI**：10.1109/tdsc.2026.3702678
- **arXiv**：无
- **PDF**：[TDSC_2026_VehicleSideLightweightConditional.pdf](papers/TDSC_2026_VehicleSideLightweightConditional.pdf)

## 一句话概括

本文提出面向车联网的 VLCADA 双层认证框架，在车辆侧同时处理驾驶员合法性和车辆—网络通信认证，并利用轻量匿名签名、密码恢复机制、PUF 与模糊提取器降低在线认证开销。

## 问题与动机

现有车联网条件匿名认证协议通常集中于消息匿名性和完整性，却较少同时覆盖人—车接入层的驾驶员合法性、车—网通信层的轻量认证、密码更新与找回，以及物理密钥泄露风险。车辆端资源有限，若把大量椭圆曲线运算放到在线阶段，会增加时延和通信负担。论文希望在可信机构可追踪匿名性的前提下，兼顾多因素认证、密码鲁棒性、前向/后向安全和车辆端的低计算开销。

## 方法

VLCADA 由轻量条件匿名签名方案 SLCAS 和基于门限秘密共享的密码管理方案 DPM 组成。驾驶员接入使用身份、密码和生物特征，并结合 PUF 与模糊提取器保护设备秘密；通信阶段把较重的运算预计算到离线阶段，在线车辆主要执行哈希与异或操作。协议为车辆和驾驶员生成条件匿名身份，可信机构可在需要时通过伪身份追踪真实身份。安全模型考虑 Dolev–Yao、CK、部分物理攻击以及最多泄露 `n−1` 个认证因素的场景，并假设可信机构本身可信。

## 实验与结果

密码学基准中，车辆签名生成约需 2 次哈希、耗时约 0.006 ms；路侧单元验证约需 2 次椭圆曲线标量乘、1 次点加和 4 次哈希，耗时约 1.481 ms；在论文假设下，单次通信开销为 124 字节。与对比方案相比，整体计算量最多降低约 48.55%，通信量最多降低约 32.61%。NS-3 与 SUMO 联合仿真采用嘉兴区域约 3×2.5 km 的道路场景，持续 318 s、包含 57 辆车；数据包投递率在 0–100 m 约为 0.82，在 400–500 m 约为 0.64，并随距离增加而下降。形式化安全分析和自动化工具检查支持其认证、匿名和密钥安全主张。

## 贡献与局限

论文把驾驶员—车辆接入和车辆—网络通信两层认证统一到一个轻量条件匿名框架中，并同时覆盖密码恢复、PUF 防护、可追踪匿名和在线计算减负。局限在于可信机构是强信任根，安全范围只覆盖最多 `n−1` 个认证因素泄露；投递率来自仿真，密码学耗时来自实验平台，尚不能直接等同于真实车辆环境的端到端时延。后续可验证真实车载设备和更大规模交通场景，并探索面向后量子密码的 ML-KEM、ML-DSA 等替代方案。

---
DOI: 10.1109/tdsc.2026.3702678
