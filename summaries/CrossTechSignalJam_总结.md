# Cross-Technology Signal Detection and Jamming Attack for Heterogeneous Internet of Things 总结

## 基本信息

- **标题**: Cross-Technology Signal Detection and Jamming Attack for Heterogeneous Internet of Things
- **作者**: Siru Wu, Wenchao Jiang, Demin Gao, Tian He
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3710528
- **arXiv**: 无
- **PDF**: [TDSC_2026_CrossTechSignalJam.pdf](papers/TDSC_2026_CrossTechSignalJam.pdf)

## 一句话概括

提出基于 CSI 的双分支 LSTM-Attention 检测与 LSTM-DQN 智能干扰框架，可在 2.4 GHz 异构物联网中高精度识别并显著压制 Wi-Fi 与 ZigBee/BLE 之间的跨技术通信。

## 问题与动机

随着物联网与 5G 发展，Wi-Fi、ZigBee、BLE 等异构协议在 2.4 GHz ISM 频段大量共存。跨技术通信（CTC）通过物理层仿真让 Wi-Fi 设备直接模拟 ZigBee/BLE 信号实现跨协议互操作，但多数 CTC 实现缺乏加密、认证与完整性校验，易被窃听、伪造消息注入或 DoS 攻击。论文指出，基于 RSSI 或能量检测的传统手段分辨率不足，难以区分协议指纹与隐蔽的 CTC 信号扰动；而 CSI 能细粒度刻画 OFDM 子载波的幅度与相位，可作为检测与操纵 CTC 的利器。然而现有工作很少研究攻击者如何利用细粒度 CSI 构造自适应、数据驱动的智能干扰攻击，实时处理高维 CSI、跨信道泛化以及能量与延迟约束下的干扰优化仍是开放难题。

## 方法

论文提出闭环智能干扰攻击框架，由监测检测与干扰决策两大模块组成。检测模块采用双分支 LSTM 网络并联处理 CSI 幅度与相位流，每支包含两层 LSTM 加全连接层输出子载波级特征，注意力模块对时间-频率相关性打分，融合层做多天线全局平均池化后经 Softmax 将信号分为原生 Wi-Fi、ZigBee/BLE、CTC 三类，精度超过 96%。干扰模块把干扰决策建模为以 1 ms 时隙划分的马尔可夫决策过程（MDP）：轻量 LSTM 依据历史 CSI 预测受害方下一时隙的传输概率，DQN 在 WAIT/JAM 两个动作间做能量与时隙最优的干扰决策，奖励区分成功干扰、多余干扰与漏干扰，采用经验回放与目标网络稳定训练。系统基于商用 Wi-Fi 硬件实现，采用定时与频控匹配的定制波形、以不低于 ZigBee 信号五倍的功率进行干扰，并在干扰后扣除已知干扰分量以判断 CTC 活动是否持续。

## 实验与结果

实验在真实 2.4 GHz 测试床完成：AC-1200 Wi-Fi 网卡（RTL8812AU）作为 CTC 发送端，在 IEEE 802.11n/802.11b 间切换以模拟 ZigBee/BLE 信号；TI CC2650 作为接收端；Intel AX210S 攻击端运行 PicoScenes 被动采集 CSI，PyTorch 环境执行检测与决策。数据集含 3,000 条 CSI 样本（1,000 CTC、1,000 普通 ZigBee/BLE、1,000 无 CTC），按 70%/30% 划分训练与测试，覆盖 LoS（3 m×20 m 走廊）、NLoS（10 m×10 m 室内）与室外空旷（至 50 m）三种场景。LSTM-Attention 检测取得 0.96 准确率、0.97 F1、0.97 精确率与 0.97 召回率，明显优于 DNN 基线（0.89）及 SVM/RF 浅层模型；距离增大时精度下降，如 LoS 下 ZigBee 从 2 m 的 96% 降至 12 m 的 87%，NLoS 下从 92% 降至 83%，室外 50 m 仍保持约 81%；增大包长可提升精度，LoS 下 ZigBee 最高达 98%。干扰实验中，正常阶段 ZigBee/BLE 吞吐接近 100%，干扰开始后 LSTM-DQN 使 ZigBee 吞吐下降超 60%、BLE 下降约 45%，优于随机干扰（约 40%/25%）；时隙命中率 HR 在 LoS 近距约 92%，随距离降至约 72%–84%，NLoS 下降更明显；PER 在 LoS 下 ZigBee 为 86%–74%，BER 维持在 5%–8%，说明干扰主要造成包级破坏。与 SamBee、LSTM 反应式干扰、随机干扰相比，本方法在 20 m 距离仍保持 PER 超 65%，且高负载下占空比低于 15%（SamBee 超过 70%）。在 AWGN、瑞利与莱斯信道下，高 SNR 时分类精度超 95%、命中率达 90%，AWGN 中 SNR 高于 4 dB 时精度超 95%；延迟方面检测推理为 0.86 ms、LSTM-DQN 最大推理 0.92 ms、参数更新峰值 0.9 ms，满足单时隙 1 ms 的实时性约束。

## 贡献与局限

主要贡献：一是提出首个基于 CSI 的 CTC 智能干扰完整框架，把检测与干扰决策统一为深度学习加强化学习方案；二是双分支 LSTM 加注意力机制实现超 96% 的多协议分类精度；三是将干扰建模为 1 ms 时隙 MDP，用 LSTM 预测加 DQN 优化实现能量高效、隐蔽的干扰；四是在真实商用硬件（AC1200、CC2650）与多种真实/合成信道上完成端到端验证，展示了亚毫秒级实时处理能力。局限方面：数据集仅 3,000 条来自自建测试床的 CSI 样本，设备局限于 RTL8812AU、CC2650、USRP 与 AX210S，作者承认这属于真实世界概念验证而非跨硬件平台的权威基准，尚未在不同 CSI 采集芯片与独立数据集上验证广义泛化；低 SNR（如 −6 dB 衰落信道）下检测与干扰性能明显下降。讨论部分还提出了传输时序随机化、动态信道切换、发射功率控制与 CSI 干扰源检测等防御方向。

---
DOI: 10.1109/tdsc.2026.3710528
