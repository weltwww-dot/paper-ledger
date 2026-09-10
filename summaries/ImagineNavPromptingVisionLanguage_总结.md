# ImagineNav++: Prompting Vision-Language Models as Embodied Navigator Through Scene Imagination

## 基本信息

- **标题**：ImagineNav++: Prompting Vision-Language Models as Embodied Navigator Through Scene Imagination
- **作者**：Teng Wang、Xinxin Zhao、Wenzhe Cai、Changyin Sun
- **期刊 / 会议**：IEEE Transactions on Pattern Analysis and Machine Intelligence 2026
- **发表**：2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**：人工智能
- **DOI**：10.1109/tpami.2026.3688692
- **arXiv**：无
- **PDF**：[TPAMI_2026_ImagineNavPromptingVisionLanguage.pdf](papers/TPAMI_2026_ImagineNavPromptingVisionLanguage.pdf)

## 一句话概括

本文提出 ImagineNav++，利用人类导航示范学习未来视点、用新视角合成生成候选观察，再结合选择性渐进记忆和视觉语言模型选择最佳探索方向，在无需显式地图的开放词汇导航中兼顾成功率、路径效率和长期空间推理。

## 问题与动机

家庭服务机器人需要在陌生环境中寻找任意类别或特定实例，但传统地图式方法依赖定位、语义建图和持续维护，纯语言规划又难以表达空间占用、几何结构和远处的潜在目标。长时程导航还会遇到历史观察冗余、局部循环和上下文窗口受限的问题。论文希望仅使用机载 RGB/RGB-D 观察，让 VLM 不必直接回答复杂三维几何问题，而是从若干具有空间意义的候选未来视图中做最佳视点选择，并用紧凑记忆保持跨时间的空间一致性。

## 方法

系统由 Where2Imagine、未来视图合成、选择性渐进记忆、VLM 高层规划和 PointNav 低层控制组成。Where2Imagine 使用 ResNet-18 从 Habitat-Web 人类示范中预测下一候选视点的相对位姿；在六个当前视角上调用预训练 Polyoculus 新视角合成模型，生成候选未来图像。记忆模块以 DINOv2 特征的相邻帧相似度划分语义片段，选取接近片段中心的关键帧，并用近期、中期和远期不同阈值构造由密到疏的层级选择性记忆；在线版本通过流式压缩和“关键帧的关键帧”保持近似 O(1) 更新。GPT-4o-mini 接收目标、历史记忆和带选项标记的未来视图，输出 JSON 形式的选择与理由，再交由点目标导航控制器执行，循环直到找到目标。

## 实验与结果

作者在 Habitat v3.0 上评估 ObjectNav 和 Instance-Image-Goal Navigation，ObjectNav 覆盖 Gibson、HM3D、HSSD，InsINav 使用 HM3D；Where2Imagine 的示范来自 MP3D Habitat-Web。使用预测视点、T=11、ResNet-18 和 GPT-4o-mini 时，ObjectNav 在 Gibson、HM3D、HSSD 上的成功率分别达到 72.4%、58.5% 和 62.5%，HM3D 的 SPL 为 26.6%；使用真实候选视图的上限实验成功率分别为 77.1%、62.5% 和 67.5%。InsINav 的成功率为 52.4%，SPL 为 32.8%，在同类无地图方法中明显高于 PSL 的 23.0%/11.4%。HM3D 消融中，无记忆基线为 SR 56.0、SPL 24.3，统一关键帧记忆为 65.0/28.2，选择性记忆达到 67.0/30.4；在线增量记忆把单步更新延迟从 1.70 s 降至 0.16 s，平均长程记忆约 20 个关键帧。开源 VLM 实验中，Qwen3-VL-32B 和 Qwen3.5-27B 均取得 71.0% 成功率，说明系统并不必然依赖闭源云端 VLM。

## 贡献与局限

论文把人类导航偏好、未来视图想象、VLM 选择和层级视觉记忆组合成无需显式地图的开放词汇导航流程，并将复杂规划拆为一系列点目标导航子任务；消融结果明确显示想象和记忆对成功率与路径效率的互补作用。局限在于新视角合成仍会产生细节伪影，性能受预训练 NVS 质量影响；主要验证依赖 Habitat 仿真和固定任务协议，真实机器人中的传感器噪声、动态障碍、推理延迟与安全停止尚未充分覆盖。未来需要支持文本等更多目标形式、进一步降低实时推理成本，并研究长期在线适应。

---
DOI: 10.1109/tpami.2026.3688692
