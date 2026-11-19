# RAU: Sparsity-regularized residual addition unit for high-resolution spatiotemporal prediction 总结

## 基本信息
- **标题**: RAU: Sparsity-regularized residual addition unit for high-resolution spatiotemporal prediction
- **作者**: Fang Yuan、Chengcai Leng、Zhao Pei 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109886
- **发表**: 2026-11-10
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109886

## 一句话概括
RAU以显式残差增量更新和跨时空记忆流构造轻量循环单元，并对高层增量施加稀疏正则，在高分辨率预测中兼顾短期精度与计算效率。

## 问题与动机
高分辨率时空预测需要在空间细节、长期依赖和计算代价间权衡。复杂循环单元可加强记忆，却带来多重状态与门控成本；而下采样又可能丢失细节。作者研究能否用更简洁的状态演化机制，在保留较高空间分辨率时有效利用历史信息，并减少静态区域的冗余更新。

## 方法
残差加法单元（RAU）融合当前与前一时刻特征，经轻量更新门生成增量，再以残差方式更新状态。层间采用锯齿式时空记忆流：底层接收前一时刻顶层状态，高层则结合本层前一时刻状态，使不同语义层的历史信息参与预测。训练目标对高层增量而非特征本身施加稀疏正则，浅层保留纹理和边界更新。作者还分析了梯度传播，并在标准下降条件下讨论非光滑优化的渐近驻点性质。

## 实验与结果
在UCF Sports Action、1080×1920的TownCentreXVID和CloudCast三项任务上与ConvGRU、PredCNN、SimVP、TAU等方法比较，并报告消融和复杂度。UCF Sports Action预测第5帧时，RAU的PSNR为31.74 dB、SSIM为0.945、LPIPS为0.092；TownCentreXVID第5帧分别为37.21 dB、0.989、0.016，但较长预测时部分基线更强。CloudCast平均准确率83.39%、Brier分数0.0577，均优于表中对比方法。该数据集上RAU为3.21M参数、262.79G FLOPs。稀疏正则使TownCentreXVID第四层增量稀疏率由1.37%升至71.50%。

## 贡献与局限
RAU以加法增量和跨层记忆流扩展有效时序信息传播，稀疏约束则促使深层只在变化显著处更新。消融支持记忆流的贡献：移除后UCF Sports Action PSNR由28.01降至27.08 dB、CloudCast准确率由83.39%降至82.98%。局限是不同数据集与预测跨度的优势并不一致：TownCentreXVID长期预测中STAU、STRPM等方法表现更好；稀疏性收益也依赖正则施加层级和强度。因此结果体现的是高分辨率短期预测及效率的折中，而非各项指标全面领先。

---
DOI: 10.1016/j.neunet.2026.109886
