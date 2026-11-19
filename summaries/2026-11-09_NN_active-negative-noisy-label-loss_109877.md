# Active negative loss: A robust framework for learning with noisy labels 总结

## 基本信息
- **标题**: Active negative loss: A robust framework for learning with noisy labels
- **作者**: Xichen Ye、Yifan Wu、Yiqi Wang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109877
- **发表**: 2026-11-09
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109877 | 📄 [NN_2026_active-negative-noisy-label-loss_109877.pdf](papers/NN_2026_active-negative-noisy-label-loss_109877.pdf)
- **PDF许可**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

## 一句话概括
Active Negative Loss（ANL）通过重新构造损失函数，利用错误类别的互补信息，提升模型在标签噪声下的学习能力。论文给出归一化负损失的理论性质，并在图像分类和医学图像分割任务中检验其表现。

## 问题与动机
真实数据集的人工标签可能存在对称、类别相关、实例相关或自然噪声。常见被动损失虽能降低噪声样本的影响，却可能拟合能力不足；主动损失拟合较强，又易记住错误标注。作者希望构造兼顾鲁棒性与拟合能力的统一损失，并处理非对称噪声带来的类别分布偏斜。

## 方法
ANL将一般主动损失与归一化负损失函数（NNLF）结合：对真实标注类别以外的类别累积负向目标，通过归一化及“垂直翻转”构造与主动损失互补的被动形式。框架可与交叉熵或Focal Loss组合；另加入熵正则以缓解非对称噪声下预测类别失衡。论文以定理分析归一化负损失对错误标签梯度及噪声鲁棒性的性质，并通过L1正则抑制过拟合。

## 实验与结果
实验包括CIFAR-10/100合成及真实噪声、WebVision和Animal-10N分类，以及ISIC-2017、GlaS分割；表格报告三次随机运行均值与标准差。在WebVision训练的ResNet-50上，ANL-CE在干净ILSVRC12验证集准确率为65.12%，高于SCE的62.64%；WebVision验证集为67.42%，SCE为67.31%。CIFAR及分割实验还显示其在多种噪声率下具有竞争力，结果依数据集、噪声类型和损失变体而异。

## 贡献与局限
ANL提供可与多种主动损失组合的归一化负损失构造，并从理论上讨论其噪声鲁棒性；多数据集实验覆盖合成噪声、真实噪声和分割标注扰动。结果支持方法在多种条件下有效，但并非每一设置都由同一变体获胜；作者也指出标签分布不均衡仍需处理，噪声模式和数据任务会影响选择。

---
DOI: 10.1016/j.neunet.2026.109877 | 📄 [NN_2026_active-negative-noisy-label-loss_109877.pdf](papers/NN_2026_active-negative-noisy-label-loss_109877.pdf)
