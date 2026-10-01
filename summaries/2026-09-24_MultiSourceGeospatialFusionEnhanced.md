# Multi-source geospatial fusion for enhanced visual geo-localization of unmanned aerial vehicles 总结

## 基本信息
- **标题**: Multi-source geospatial fusion for enhanced visual geo-localization of unmanned aerial vehicles
- **作者**: Xiong Qiu、Shouyi Liao、Dongfang Yang 等
- **期刊 / 会议**: Neural Networks 2026（在线发表；正式版卷期标注 2027）
- **发表**: 2026-09-24
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.109679
- **PDF**: [NN_2026_MultiSourceGeospatialFusionEnhanced.pdf](papers/NN_2026_MultiSourceGeospatialFusionEnhanced.pdf)

## 一句话概括
研究融合卫星影像和地形高程，以分层视觉匹配恢复无人机三维位置，减少对预先航拍建图的依赖。

## 问题与动机
卫星导航不可用时，跨视角检索常只能找到相似区域，预建三维模型又依赖预飞行与大量计算。作者希望在没有起飞点先验、存在斜视影像和大范围搜索的条件下完成重定位。

## 方法
离线阶段通过旋转和平移裁剪卫星影像，提取全局与局部描述子并保存高程；在线阶段先粗检索，再用 SuperPoint 和 LightGlue 匹配局部特征。分辨率自适应和匹配有效性检查过滤异常，最终结合高程与投影几何估计位置。

## 实验与结果
在覆盖 26.9×7.03 千米的两处飞行场景中，相较仅用卫星影像，加入高程后总体误差分别由 64.57 米降至 16.90 米、由 47.15 米降至 9.26 米。单幅定位约需 2.1 秒，实验同时涵盖俯视与约 45° 斜视。

## 贡献与局限
贡献是把检索、局部匹配、异常过滤与高程约束整合为可运行的三维定位流程。系统仍依赖预建且及时的卫星与高程数据库，地貌变化和影像差异会影响定位；目前两处场景及所用硬件的结果不足以保证跨季节或任意地区的实时可靠性。

---
DOI: 10.1016/j.neunet.2026.109679
