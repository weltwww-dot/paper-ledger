# Multimodal sentiment analysis with multi-level representation learning and global tri-modality unified fusion 总结

## 基本信息
- **标题**: Multimodal sentiment analysis with multi-level representation learning and global tri-modality unified fusion
- **作者**: Li Zelong、Lu Shuhua、Cui Fang 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 205，文章号109515
- **发表**: 2026-08-14
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结，正文在出版社页面获取
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109515

## 一句话概括
MLTM通过多层共享与私有表示学习、动态表示优化及三模态统一融合，在CMU-MOSI和CMU-MOSEI情感分析基准上优于多种比较配置。

## 问题与动机
文本、音频和视觉线索在语义层次、噪声和贡献上各异，单层表示或成对融合难以完整捕捉跨模态互补关系。

## 方法
模型分层提取并区分跨模态共享信息与模态私有信息，动态优化表示后，以全局三模态融合模块联合交互文本、音频和视觉特征。

## 实验与结果
在CMU-MOSI与CMU-MOSEI上与多模态情感分析模型比较，并开展表示层级、参数共享、损失项和融合模块消融；混合参数共享方案在两数据集上优于完全独立或完全共享配置，但最优层级深度随数据集变化（PDF 第 6、8–14 页）。

## 贡献与局限
以多层表示和统一三模态交互提高情感线索整合能力，消融支持混合共享和私有特征的作用；表现依赖数据集与层级设置，基准结果尚不能说明跨域稳定性。

---
DOI: 10.1016/j.neunet.2026.109515
