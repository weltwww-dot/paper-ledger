# SignMamba: Sparse spatial–temporal state-space modeling for continuous sign language recognition 总结

## 基本信息
- **标题**: SignMamba: Sparse spatial–temporal state-space modeling for continuous sign language recognition
- **作者**: Xu-Hua Yang、Gang Wang、Hong-Xiang Hu 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109530
- **发表**: 2026-08-19
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109530

## 一句话概括
SignMamba利用手脸运动显著性与关键帧稀疏采样，把连续手语中稀疏的空间和时间语义交由状态空间模型建模，在降低计算量的同时改善词错误率。

## 问题与动机
连续手语视频的有效信息主要集中在手、脸及少数动作时刻，静态背景、停顿和缓慢过渡带来大量冗余。密集建模既浪费计算，也可能稀释关键动作线索；仅靠局部时间建模又难捕获长程依赖。

## 方法
空间MotionVSS根据相邻帧特征差生成运动重要性图，选取Top-K显著位置并用双向S6状态空间块传播，再与深度卷积提取的静态纹理残差融合。时间TemporalVSS先以相邻帧构造的空间权重聚合局部动态，再从时间熵引导的稀疏策略中选关键帧，以顺序扫描和跳跃扫描建模长程关系，最后插值恢复序列。

## 实验与结果
在PHOENIX14、PHOENIX14-T及CSL-Daily上以词错误率评估，并与识别基线比较。ResNet34配置在PHOENIX14测试集WER为17.3%，PHOENIX14-T测试集为18.2%；CSL-Daily开发/测试集分别为25.8%和24.9%。PHOENIX14-T稀疏采样约保留25%帧，测试WER 18.8%、延迟1.8 ms；表中均匀采样同为约25%帧时WER为19.8%。

## 贡献与局限
论文将手语的空间与时间语义稀疏性直接纳入网络结构，并用双向状态空间扫描兼顾全局上下文与效率。作者指出评估主要来自背景受控的棚拍数据，真实动态背景、照明变化及移动设备实测尚未覆盖；无障碍沟通的实际延迟还需用户研究。

---
DOI: 10.1016/j.neunet.2026.109530
