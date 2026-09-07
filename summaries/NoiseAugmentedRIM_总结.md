# Improving human motion generation based on a head-mounted display and its controllers via noise-augmented motion data and the recurrent inference model 总结

## 基本信息

- **标题**: Improving human motion generation based on a head-mounted display and its controllers via noise-augmented motion data and the recurrent inference model
- **作者**: Zihao Guo, Jingbo Zhao
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108918
- **arXiv**: 无
- **PDF**: [NN_2026_NoiseAugmentedRIM.pdf](papers/NN_2026_NoiseAugmentedRIM.pdf)

## 一句话概括

针对虚拟现实中头戴显示器（HMD）与手持控制器佩戴松动引入的运动噪声，本文提出 CVAE 噪声增强数据生成策略与循环推理模型 RIM，显著提升全身人体动作生成的精度与平滑性。

## 问题与动机

基于 HMD 与两只手持控制器的全身人体动作生成是 VR 游戏与社交等沉浸式体验的核心环节。但此前方法（如 AvatarPoser、HMD-NeMo、HMD-Poser 等）都假定设备与身体部位之间为刚性连接，而实际 VR 体验中设备往往松垮佩戴，其与身体部位坐标系之间存在非刚性平移与旋转变换，由此产生的运动噪声会显著降低模型性能。大规模动作捕捉数据集 AMASS 由光学追踪数据推断而来（属于不含此类噪声的"合成数据"），而真实设备数据集 FreeDancing 规模小、动作覆盖有限。为此本文提出两项改进：一是学习非刚性变换并合成噪声增强动作数据的生成式训练策略；二是新的全身动作生成模型 RIM。

## 方法

噪声增强策略基于条件变分自编码器（CVAE）：以头部与双手部位的位置、旋转作为条件，编码真实噪声序列，重构损失与 KL 散度加权训练后，在训练下游动作生成模型时对每一批 AMASS 合成数据实时施加由隐空间采样得到的非刚性位置/旋转噪声，使训练数据更接近真实 HMD 采集数据；并与直接（Direct）、微调（Fine-tuning）及加性（Additive，用 Faiss 从真实数据检索最近邻噪声）三种训练策略对比。RIM 包含四部分：(1) Model Initialization——以初始局部位姿与其前向运动学求得的全局位姿，经三层 MLP 为骨干中五个 LSTM 生成初始隐状态与细胞状态；(2) Body-Part Motion Embedding——用全连接层编码头、左右手及其在头坐标系下表示的位置、旋转、线速度与角速度；(3) Spatial-Temporal Backbone——每个部位先经单向 LSTM（隐维 512）建模时序，输出作为 token 由三层八头 transformer encoder 建模部位间空间依赖；(4) Temporal Regression——将各部位输出逐帧拼接后经共享 LSTM（隐维 2560）恢复时序，再由两个 header 输出 132 维局部位姿与 16 维 SMPL 形状参数。推理时每处理完一个长度为 40 的子序列即保留 LSTM 状态作为下一子序列的初始状态，形成跨子序列的循环推理；损失为局部/全局位姿、关节位置、根关节朝向、加速度与 SMPL 形状约束的加权 L1 损失。

## 实验与结果

训练采用 AMASS Protocol 1（约 300 万帧，60 Hz 重采样），在真实设备数据 FreeDancing（约 55 万帧）与 EMHI（约 300 万帧）上测试；策略对比时取 FreeDancing 随机 50%（约 28 万帧）训练、EMHI 测试，训练规模不足测试集 10% 以检验泛化。使用 MPJRE(°)、MPJPE(cm)、MPJVE(cm/s)、Jitter 及 H/U/L/R-PE 等八项指标；实现基于 PyTorch 1.11.0 与 RTX 4090，Adam、batch size 256，噪声模型训练 2 万次迭代（约 80 epoch），RIM 训练 20 epoch。无增强策略对比（Table 1/2）中，RIM 在 FreeDancing 上 MPJRE 7.13、MPJPE 9.56 为最优且 MPJVE 33.19 与 RPM（33.12）相当；在 EMHI 上 MPJRE 7.95、MPJPE 8.27、MPJVE 33.95、Jitter 9.49 均低于 AvatarPoser、AGRoL、HMD-Poser、RPM。计算开销上 RIM 参数量 89.32M、模型 375.44 MB、81.30 FPS，仍满足实时应用需求。四种训练策略对比（Table 4，EMHI）显示生成式策略整体最优，其中 RIM+生成式在几乎所有指标上取得全场最佳：MPJRE 7.72、MPJPE 7.69、MPJVE 32.44、Jitter 9.02，H/U/L/R-PE 分别为 7.79/4.53/12.26/5.78；微调易在单数据集上过拟合，加性策略只能采样有限噪声模式，而生成式策略可从隐空间采样更丰富的噪声。消融实验（Table 5）表明去掉 Model Initialization 或 Temporal Regression 中的 LSTM 均使误差与 Jitter 上升，而去掉该 LSTM 的子序列状态传递（w/o T States）使时序平滑性急剧恶化（FreeDancing+Direct 下 MPJVE 由 33.19 升至 226.52），证明循环推理对生成平滑动作至关重要。

## 贡献与局限

主要贡献：(1) 首个学习 VR 设备与身体部位间非刚性位置/旋转变换、并在训练期合成噪声增强动作数据的生成式数据增强策略，可从小规模真实噪声数据学习并泛化到大规模数据集，显著提升下游模型性能；(2) 提出融合 Model Initialization、Temporal Regression 与 Recurrent Inference 的 RIM，在离线与实时评测中取得 SOTA 效果；(3) 系统比较直接、微调、加性与生成式四种训练策略，证实生成式策略的优越性；(4) 代码已开源（github.com/vrlab561/RIM-release）。局限：噪声生成在训练中对每个 batch 都执行，给下游模型训练带来额外计算与资源开销。未来工作可探索基于扩散模型或归一化流的噪声生成器，并将该方法推广到 IMU 同样非刚性佩戴的惯性动作生成任务。

---
DOI: 10.1016/j.neunet.2026.108918
