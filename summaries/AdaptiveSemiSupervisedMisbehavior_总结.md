# Adaptive Semi-Supervised Learning-Based Misbehavior Detection in Vehicular Networks 总结

## 基本信息

- **标题**: Adaptive Semi-Supervised Learning-Based Misbehavior Detection in Vehicular Networks
- **作者**: Elnaz Limouchi, Francois Chan
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026年6月9日
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3702025
- **arXiv**: 无
- **PDF**: [TDSC_2026_AdaptiveSemiSupervisedMisbehavior.pdf](papers/TDSC_2026_AdaptiveSemiSupervisedMisbehavior.pdf)

## 一句话概括

论文提出根据前一轮 F1 分数自适应调整置信度阈值的半监督自训练框架，并结合超参数优化的 XGBoost 检测车联网中的恶意行为。

## 问题与动机

VANET 安全检测需要识别会影响交通安全和系统可靠性的恶意行为，但监督学习依赖大量难以获得的标注数据。半监督学习可以利用未标注样本，却容易因低质量伪标签传播而不稳定。论文用自适应阈值在精确率和召回率之间动态平衡，以适应不同的标注比例。

## 方法

方法在每轮自训练中根据上一轮 F1 分数更新伪标签置信度阈值，达到最低性能要求或停止条件后再进入下一轮。基础分类器采用 Logistic Regression 或 XGBoost，其中 XGBoost 的关键超参数通过随机搜索和验证集 F1 分数优化。数据预处理包括缺失值填补、数值归一化、类别编码、去重和仅在训练集使用 SMOTE；整体训练离线完成，轻量推理可部署到路侧单元。

## 实验与结果

论文使用 VeReMi 数据集，按 70%/15%/15% 划分训练、验证和测试集，并测试初始未标注比例 95%、90%、85% 和 75%，每项结果来自 5 次运行。自适应半监督 XGBoost 的准确率分别为 0.7552、0.7639、0.7846 和 0.8415，F1 分数分别为 0.8528、0.8592、0.8740 和 0.9123；优化后在 75% 未标注设置下准确率升至 0.8681、F1 升至 0.9403，在 95% 未标注设置下准确率为 0.7621、F1 为 0.8585。与同条件 SVMDformer 相比，75% 未标注时准确率、精确率、召回率和 F1 分数分别由 0.8341、0.8245、0.8673、0.8454 提升到 0.8681、0.9093、0.9735、0.9403。

## 贡献与局限

论文贡献在于把 F1 驱动的自适应阈值与梯度提升学习结合，降低半监督伪标签传播的不稳定性，并系统比较不同未标注比例和优化前后效果。局限是实验主要基于单一 VeReMi 基准和表格特征，XGBoost 与序列模型的复杂度不能直接等同比较；真实道路环境中的分布变化、在线更新成本和更复杂攻击仍需进一步评估。

---
DOI: 10.1109/tdsc.2026.3702025
