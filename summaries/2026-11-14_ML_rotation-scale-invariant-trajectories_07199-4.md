# Advancing Rotation and Scale-Invariant Trajectory Representations for Maritime and Aviation Mobility Data Analysis 总结

## 基本信息
- **标题**: Advancing Rotation and Scale-Invariant Trajectory Representations for Maritime and Aviation Mobility Data Analysis
- **作者**: Cristiano Landi、Natalia Andrienko、Gennady Andrienko 等
- **期刊 / 会议**: Machine Learning 2026
- **卷期 / 文章号**: 115，文章号255
- **发表**: 2026-11-14
- **日期来源**: Springer 官网 citation_online_date
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1007/s10994-026-07199-4
- **PDF**: [ML_2026_rotation-scale-invariant-trajectories_07199-4.pdf](papers/ML_2026_rotation-scale-invariant-trajectories_07199-4.pdf)
- **开放许可**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) · 出版社原件，未经修改

## 一句话概括
RoSITa 通过相对 Hough 变换生成旋转与尺度不变的轨迹形状表示，在几何主导的分类基准上表现突出，并支持船舶与滑翔伞轨迹探索，但对运动学差异和噪声仍有限。

## 问题与动机
如何在方向、尺度和采样密度变化下比较海事与航空轨迹形状，并让聚类结果便于领域专家解释？

## 方法
RoSITa 将轨迹片段转换为相对 Hough 累加器，再聚合为旋转与尺度不变形状签名；表示扩展至二维和三维轨迹，并结合距离聚类、分类基准及人机协同可视分析。

## 实验与结果
作者通过合成轨迹敏感性分析、多个真实与合成分类数据集的表示基准，以及船舶监测和滑翔伞案例评估；RoSITa 在几何主导分类任务上有较强表现，例如车辆数据宏 F1 为 0.979，但在运动学主导任务上较弱；噪声增加通常使 F1 下降（PDF 第 15–28、32–37 页）。滑翔伞数据未公开，且表示本身不充分编码运动学。

## 贡献与局限
论文提出可解释的尺度与旋转不变轨迹形状表征，并展示其接入分类、聚类和可视分析的方式；几何相似不等于行为相同，需结合速度等运动学信息及领域判断。

---
DOI: 10.1007/s10994-026-07199-4 | PDF: [ML_2026_rotation-scale-invariant-trajectories_07199-4.pdf](papers/ML_2026_rotation-scale-invariant-trajectories_07199-4.pdf)
