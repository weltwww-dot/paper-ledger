# Depth map super resolution grounded in the multi-dimensional collaborative guidance 总结

## 基本信息
- **标题**: Depth map super resolution grounded in the multi-dimensional collaborative guidance
- **作者**: Xiaofei Zhou、Xiang Li、Qianyu Zhang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109551
- **发表**: 2026-08-29
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109551

## 一句话概括
MCGNet以净化后的RGB边缘、空间与频域跨模态融合及显式结构残差引导Mamba重建高分辨率深度图。

## 问题与动机
深度超分辨率需从低分辨率深度恢复几何细节，并借助高分辨率RGB图像。局部卷积全局一致性有限，Transformer处理高分辨率图像成本高；直接融合RGB纹理还会把颜色纹理误复制到深度图，造成边缘模糊或伪影。

## 方法
MCGNet由纹理校正引导、空间—频域协同融合、层次结构建模和Mamba空间重建组成。纹理校正模块联合RGB与深度梯度筛除不适合深度的纹理；SFCG在空间域及频域融合跨模态细节；LHM通过高分辨率与伪低分辨率特征差显式提供结构残差；Mamba重建模块汇聚多尺度线索并建模长程依赖。

## 实验与结果
在NYU-v2、Middlebury、Lu及RGB-D-D等基准评估不同放大倍率。NYU-v2的×8 RMSE为2.39厘米，低于SGNet的2.44和HCGNet的2.53；×16为4.32厘米，优于表列方法。Middlebury×8为1.60厘米，Lu×8为1.42厘米。消融中NYU-v2×8基线RMSE 3.68厘米，加入SFCG、LHM和TCGE后完整模型为2.39厘米；Mamba骨干在3090上推理0.3108秒，RMSE 2.39厘米，CNN为0.1601秒/RMSE 2.46，Transformer为0.5862秒/RMSE 2.53。

## 贡献与局限
方法将RGB纹理筛选、双域互补融合和结构残差先验连成一套重建流程，在×8、×16困难倍率多个基准上表现突出。作者讨论指出×4时并非所有数据集都占优；模型的运行时间受硬件与输入尺寸影响，且实验集中于配对RGB-D基准，跨传感器与错配场景的适用性仍需验证。

---
DOI: 10.1016/j.neunet.2026.109551
