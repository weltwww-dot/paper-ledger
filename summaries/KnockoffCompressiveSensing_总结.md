# Knockoff-Guided Compressive Sensing: A Statistical Machine Learning Framework for Support-Assured Signal Recovery 总结
## 基本信息
- **标题**: Knockoff-Guided Compressive Sensing: A Statistical Machine Learning Framework for Support-Assured Signal Recovery
- **作者**: Xiaochen Zhang、Haoyi Xiong
- **期刊 / 会议**: Machine Learning 2026
- **发表**: 2026-10-07
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07167-y
- **PDF**: [ML_2026_KnockoffCompressiveSensing.pdf](papers/ML_2026_KnockoffCompressiveSensing.pdf)

## 一句话概括
KnockoffCS 将 knockoff 变量筛选引入压缩感知，把“哪些信号分量非零”的支持集识别与系数估计分开，并在筛选阶段显式控制假发现率（FDR）。

## 问题与动机
压缩感知通常用 LASSO、贪心追踪等方法从少量测量恢复稀疏信号，但相关测量下支持集可能误选，且传统保证往往依赖较强的整体矩阵条件，难以直接约束假阳性比例。在医学成像、基因分析等场景，误报哪些分量“存在”本身就会影响后续结论，因此作者把支持集的统计可靠性置于核心位置（第2–3页）。

## 方法
框架先依据特征分布构造 model-X knockoff 测量，再比较原变量与其 knockoff 的重要性统计量，通过 knockoff filter 按目标 FDR 阈值选择支持集；随后只在选中分量上解带正则项的最小二乘问题，未选分量置零。系数估计与筛选分离，使 FDR 控制不必依赖估计步骤本身。理论部分在文中给定的信号稀疏、噪声、支持集可区分性及受限特征值/交叉相关条件下证明筛选和重建误差保证；它不意味着对任意测量矩阵都无条件恢复（第6–13页）。

## 实验与结果
合成实验改变稀疏度、测量数和噪声水平，测量矩阵采用块大小为5、块内相关系数0.6的结构，每种配置重复20次，目标 FDR 设为0.1，并与 LASSO、OMP 比较。论文报告在代表性的高信噪比设置下，KnockoffCS 的支持集检测 power 接近1且 FDR 低于0.02。真实数据实验覆盖八个领域数据集，并比较 LASSO、OMP、CLIME、Dantzig Selector 等重建后模型的预测效果；在56个模型—数据集组合中，KnockoffCS 有71.4%位列压缩感知方法前二，但相对直接使用压缩观测的收益依赖数据集和预测器，在 Yahoo! 排序数据的7种预测器中有5种低于压缩基线（第13–20页）。

## 贡献与局限
主要贡献是把可解释的 FDR 控制嵌入压缩感知支持集恢复，并进一步分析该筛选机制对信号重建误差的影响；合成与真实数据实验显示其统计筛选优势具有一定下游价值。局限是保证依赖明确的结构假设，真实任务上的预测排名并不稳定；任务无关的压缩和筛选误差也使恢复信号与未压缩数据仍有差距。后者与论文所用低测量率、任务无关感知的实验设计相符，不能据此推断所有下游任务都能获益（第11–13、20–21页）。

---
DOI: 10.1007/s10994-026-07167-y
