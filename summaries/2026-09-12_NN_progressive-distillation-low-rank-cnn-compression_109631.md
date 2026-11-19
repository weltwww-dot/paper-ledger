# A novel approach to lossless convolutional neural network compression via progressive knowledge distillation-incorporated low-rank compression 总结

## 基本信息
- **标题**: A novel approach to lossless convolutional neural network compression via progressive knowledge distillation-incorporated low-rank compression
- **作者**: Yaping He、Hao Wu、Weibo Liu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109631
- **发表**: 2026-09-12
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109631 | 📄 [NN_2026_progressive-distillation-low-rank-cnn-compression_109631.pdf](papers/NN_2026_progressive-distillation-low-rank-cnn-compression_109631.pdf)
- **PDF许可**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 一句话概括
论文提出 PKD-LRC，以 ResTucker-2 低秩分解、渐进式知识蒸馏和动态温度调节协同压缩 CNN，目标是在减少模型规模时保住甚至提升分类精度。

## 问题与动机
卷积层低秩分解可降低参数量与计算量，但截断会丢失残差信息并造成精度下降；单独蒸馏也未必能修复各层压缩误差。作者研究如何在压缩过程中逐步恢复学生网络表征，使压缩率与分类性能之间的折衷更有利。

## 方法
PKD-LRC 对卷积权重采用 ResTucker-2 分解，以残差式结构降低低秩近似造成的性能损失；随后以渐进学习规则逐步优化压缩学生网络，并用动态温度调整蒸馏强度，使学生适应教师输出与自身能力差异。论文将该组合与纯低秩分解及低秩加蒸馏等压缩方法比较，覆盖不同网络规模和图像分类数据集。

## 实验与结果
实验使用 MNIST、SVHN、CIFAR-10、CIFAR-100 和 ImageNet。CIFAR-100 上，VGG-16 压缩率为 7.75×时，PKD-LRC 的 Top-1 准确率比未压缩模型高 0.35 个百分点；ImageNet 上 ResNet-18 压缩率为 2.78×时，Top-1 高 0.20 个百分点。作者还报告 MobileNetV2 在 ImageNet 上达到 72.07% Top-1，并称其优于所比较的剪枝和低秩方法。

## 贡献与局限
工作整合残差补偿张量分解、渐进蒸馏和温度调节，在五个分类基准上实现压缩后精度恢复或略超基线。“无损”指报告任务中的分类表现，不代表权重数学重建无损；时延和能耗收益尚需在目标硬件测量。

---
DOI: 10.1016/j.neunet.2026.109631 | 📄 [NN_2026_progressive-distillation-low-rank-cnn-compression_109631.pdf](papers/NN_2026_progressive-distillation-low-rank-cnn-compression_109631.pdf)
