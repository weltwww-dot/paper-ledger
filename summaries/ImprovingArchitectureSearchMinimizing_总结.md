# Improving Neural Architecture Search by Minimizing Worst-Case Validation Loss 总结

## 基本信息

- **标题**：Improving Neural Architecture Search by Minimizing Worst-Case Validation Loss
- **作者**：Haochen Zhang，Xuefeng Du，Ruisi Zhang，Pengtao Xie
- **期刊 / 年份**：IEEE Transactions on Artificial Intelligence，2026
- **研究方向**：神经架构搜索、鲁棒机器学习
- **DOI**:10.1109/tai.2026.3670777
- **PDF**：[TAI_2026_ImprovingArchitectureSearchMinimizing.pdf](papers/TAI_2026_ImprovingArchitectureSearchMinimizing.pdf)

- **内容状态**: 完整 · 已依据全文完成中文六段式总结

## 一句话概括

论文把神经架构搜索从只优化平均验证损失扩展为同时面对生成的最坏情况验证样本：tester 用深度生成模型制造会暴露 learner 弱点的验证数据，learner 再据此更新架构，从而改善少数困难样本和数据腐化下的表现。

## 问题与动机

传统 NAS 以固定验证集的平均损失选择架构，容易掩盖稀有类别或困难样本上的失效；在医疗等安全关键任务中，平均准确率高并不代表最坏情况可接受。已有 adversarial examiner 能识别固定模型的弱点，却没有把评估结果用于重新训练架构；基于固定数据集的 curriculum learning 也不能探索经验分布之外的新失败模式。

## 方法

方法构造一个四层 multilevel optimization（MLO）框架。第一层在架构暂定时训练 learner 权重；第二层训练 FQ-GAN 等深度生成模型生成输入和标签；第三层用辅助模型验证生成样本的语义有效性；第四层让 tester 最大化 learner 在生成验证集上的损失，同时让 learner 最小化该最坏损失，并用人工标注验证集约束生成样本的 meaningfulness、保持平均性能。架构、生成器及其超参数通过梯度式近似端到端更新，并通过低频超梯度更新、参数共享和正则化降低搜索成本。

## 实验与结果

实验使用 CIFAR-10、CIFAR-100、ImageNet、CIFAR-10-C 和 ImageNet-C，将框架分别应用到 DARTS、P-DARTS、PC-DARTS 和 PR-DARTS，并与 SPCL、DIHCL 比较。在 CIFAR-100 的 2000 个人工筛选最坏样本上，Ours-Pcdarts 的分类错误率为 24.92%，低于 Pcdarts 的 28.42%；Ours-Pdarts 为 25.51%，低于 27.93%。在 CIFAR-10-C 上，Ours-Pcdarts 的错误率为 19.8%，而 Pcdarts 为 23.0%；在 ImageNet-C 上，Ours-Pcdarts 的 mean Corruption Error 为 75.4，低于 78.8。对 CIFAR-100 生成图像的 Inception/FID 为 9.75/6.01，优于 FQ-GAN 的 9.59/7.42；平均情形性能未因最坏情形优化而牺牲。

## 贡献与局限

论文提出了面向 NAS 最坏情况评估与改进的通用 tester–learner 框架，并用辅助模型防止低质量或模式坍塌的生成样本误导架构搜索；多数据集结果显示其同时改善困难样本和常见腐化下的表现。局限是框架依赖可微架构参数，不能直接用于强化学习或进化算法等不可微 NAS；若生成样本保真度不足，仍可能导致架构学习意外错误，尤其需要在安全关键场景中谨慎验证。
