# YOTO++: Learning Long-Horizon Closed-Loop Bimanual Manipulation From One-Shot Human Video Demonstrations 总结

## 基本信息

- **标题**：YOTO++: Learning Long-Horizon Closed-Loop Bimanual Manipulation From One-Shot Human Video Demonstrations
- **作者**：Huayi Zhou, Ruixiang Wang, Yunxin Tai, Yueci Deng, Guiliang Liu, Kui Jia
- **期刊 / 年份**：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026
- **研究方向**：机器人操作、具身智能与计算机视觉
- **DOI**:10.1109/TPAMI.2026.3688078
- **PDF**：[TPAMI_2026_YOTOLongHorizonClosed.pdf](papers/TPAMI_2026_YOTOLongHorizonClosed.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

YOTO++ 从一次第三人称双目人类视频示范中提取双手运动，把其压缩为可执行关键帧，并通过示范扩增和双臂扩散策略学习长时程双臂技能；新增的预抓取视觉对齐使系统能在物体受扰时闭环修正，并可迁移到未见过的双臂机器人。

## 问题与动机

双臂机器人需要处理手臂间的时序协调、碰撞避免和高维动作空间，长时程任务因此很难通过少量数据稳定学习。传统分类/符号方案覆盖任务有限，遥操作示范又成本高、易包含抖动、冗余和时间不一致；直接使用从单目视频恢复的连续手轨迹也会受到左右手分类和深度估计不稳定的影响。论文的目标是把一次人类教学转化为可验证、可扩展且能跨形态执行的双臂训练数据与策略。

## 方法

系统用 WiLoR、MANO、接触检测和双目立体匹配得到左右手的 3D 轨迹、姿态与夹爪状态：先将手点投影到稳定的 2D 相机平面，再立体回投到 3D。通过状态变化或运动极值提取约 10 个关键帧，利用手眼标定将其注入机器人，并用 motion mask 表示左右臂在每个关键帧的移动/保持及异步或同步关系。示范扩增结合真实机器人 auto-rollout（一次准备好的示范约 6 小时可产生 300 次 rollout）与对物体点云及关键帧做受工作空间约束的几何变换，最终将每项任务数据扩展 100 倍、得到约 3K–24K 条轨迹。BiDP 使用任务相关物体点云、SIM(3)-equivariant 编码器和 DDPM 预测关键帧；BiDP++ 再用物体 mask 的质心与二阶矩估计预抓取阶段的平移/平面旋转偏差。

## 实验与结果

实验在固定基座的 Aubo i5 双臂平台上覆盖 10 个长时程任务，包含异步、同步、接触丰富和非抓取操作，并与 ACT、DP、DP3、EquiBot 比较；模型训练 500 或 1,000 个 epoch，每个物体通常评估 5 次、成对物体 2 次，工具任务评估 10 次。BiDP 与 BiDP++ 在十项任务上的平均成功率接近 66% 和 70%，均优于对比策略；在 pull drawer、uncover lid 的未见物体 OOD 测试中性能下降最少。对四项任务进行 1–5 次物体扰动的混合控制测试时，预抓取成功与最终成功率随扰动次数增加而下降但差距较小；在另一种 Estun ER7 类人双臂机器人上，unscrew bottle 和 pour water 均可无需重训练完成跨形态迁移。

## 贡献与局限

贡献包括：建立从一次双目人类示范到双臂关键帧动作的可解释注入流程；用真实 rollout 与点云几何变换低成本扩展示范；提出结合关键帧、motion mask、物体点云和扩散策略的 BiDP；以轻量视觉模块实现预抓取闭环并验证跨机器人迁移。局限是开放词汇分割与手轨迹感知对罕见或领域特定物体可能失效，固定工作台限制机动性，平行夹爪和视觉反馈难以进行力/触觉调节；当前仅在预抓取阶段闭环，抓取后的滑移、卡滞和更动态的任务仍需高频闭环控制、灵巧末端和触觉感知。
