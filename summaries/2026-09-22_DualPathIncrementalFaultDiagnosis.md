# A broad learning model with dual-path feature encoding for robust and expedient incremental fault diagnosis 总结

## 基本信息
- **标题**: A broad learning model with dual-path feature encoding for robust and expedient incremental fault diagnosis
- **作者**: Shengjie Zhang、Baoyi Xu、Zeyun Yang 等
- **期刊 / 会议**: Neural Networks 2026（在线发表；正式版卷期标注 2027）
- **发表**: 2026-09-22
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109677
- **PDF**: [NN_2026_DualPathIncrementalFaultDiagnosis.pdf](papers/NN_2026_DualPathIncrementalFaultDiagnosis.pdf)

## 一句话概括
MHRSI-BLM 用双路径特征编码和宽度学习的快速更新机制，在工况变化时增量识别滚动轴承故障。

## 问题与动机
一次性训练的故障诊断模型往往假设数据分布固定，而实际机械设备会持续出现新工况。重新训练成本高，增量更新又可能丢失旧知识；研究希望在诊断稳定性与计算效率之间取得平衡。

## 方法
多尺度高分辨率路径提取细致的振动特征，辅助的源信息路径为后续更新提供相对稳定的特征锚点。宽度学习结构通过权重修正、伪逆更新和横向扩展接纳新样本，以减少重复训练的开销。

## 实验与结果
论文在 CWRU 与 PU 两套轴承数据上进行增量诊断实验，报告在连续更新时保持较高准确率和有竞争力的计算效率。组件分析支持多尺度编码与源路径各自的作用；不过作者明确说明，源路径稳定奇异值的解释主要是经验观察，尚非普适理论结论。

## 贡献与局限
贡献是把双路径表征与宽度模型的快速增量更新结合，用于变化工况下的诊断。多分支结构本身增加计算负担，长期横向扩展也可能受内存限制；结果主要基于振动信号和两套公开数据，仍需在更复杂的多模态工业场景验证。

---
DOI: 10.1016/j.neunet.2026.109677
