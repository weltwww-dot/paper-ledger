# PASER: Patchified spectral representation learning for non-stationary and non-periodic user behavior sequence 总结

## 基本信息
- **标题**: PASER: Patchified spectral representation learning for non-stationary and non-periodic user behavior sequence
- **作者**: Hao Wang、Zhichao Chen、Yuan Lu 等
- **期刊 / 会议**: Artificial Intelligence 2026
- **卷期 / 文章号**: 362，文章号104646
- **发表**: 2026-10-29
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.artint.2026.104646

## 一句话概括
PASER将用户行为序列切分为重叠局部片段，在片段内加窗频谱滤波并重建序列，以兼顾兴趣变化与非周期行为。

## 问题与动机
基于FFT的序列推荐模型把整段行为压成全局频谱，隐含平稳、周期假设；用户兴趣会转移，有限行为序列也常不首尾相接，导致局部变化被抹平并产生频谱泄漏。论文希望保留频域滤波效率，同时改善下一行为预测。

## 方法
模型由行为与位置嵌入、多个patchified filtering block和点积打分器构成。每个块以长度N、步长H的重叠窗口切片，乘Hamming窗后对每片做FFT，用可学习复数滤波器逐频率调制，再经IFFT还原；重叠位置按窗权重归一化融合，接残差与层归一化。局部频谱刻画时变动态，窗边缘衰减减轻非周期截断造成的泄漏。

## 实验与结果
在Amazon Beauty、Sports、Toys及Yelp四个真实交互数据集上评估，按时间留出最近一次交互测试、倒数第二次验证，并与GRU4Rec、SASRec、FMLP等比较。Beauty上PASER的NDCG@10为0.3449，高于FMLP的0.3385；Yelp上HIT@5为0.6332，高于FMLP的0.6191。另做完整排序、消融、窗口函数及下游点击率实验。

## 贡献与局限
工作指出全局FFT用于非平稳、非周期行为序列的两类失配，并将短时傅里叶变换和Hamming加窗结合进推荐滤波层。总体结果支持该设计有效，但并非所有指标领先，例如Toys的HIT@5略低于FMLP。作者指出固定片长可能切断会话或跨越语义边界；收益仍需在更多序列域和线上场景检验。

---
DOI: 10.1016/j.artint.2026.104646
