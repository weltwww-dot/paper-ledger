# JPEG Compatible Secret Sharing Scheme With Enhanced Performance 总结

## 基本信息

- **标题**: JPEG Compatible Secret Sharing Scheme With Enhanced Performance
- **作者**: Xiaotian Wu, Dingbin Chen, Yuyang Xiong et al.
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing · 2026
- **发表**: 2026-07-17
- **日期来源**: 出版社正式PDF第1页Date of publication；卷期及current version不替代首次在线日期
- **内容状态**: 完整
- **内容说明**: 已对照14页正式版复核方法、实验及边界，主agent亲自审定中文
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3714465
- **版本**: 出版社正式版（Version of Record），14页，卷/期/页23/5/11568-11581
- **PDF**: [TDSC_2026_JPEGCompatibleSecretSharing.pdf](papers/TDSC_2026_JPEGCompatibleSecretSharing.pdf)

## 一句话概括

针对JPEG秘密共享，分别处理DC与AC编码信息，减少影子图像暴露的特征，并解决DC系数溢出造成的格式不兼容。

## 问题与动机

已有方案的影子图像可能保留秘密图像的块结构，且共享后的DC系数可能超出合法范围。因而需要同时兼顾阈值恢复、影子隐私与标准JPEG解码兼容性。

## 方法

DC路径采用部分影子可调秘密共享（PSASS）和样本重算，再以DC平移与可逆数据隐藏处理剩余溢出；AC路径结合跨段和全局块置换，对附加位作阈值共享。DCA、ACA是所处理的编码数据，不应误当成算法名称（PDF第4—10页）。

## 实验与结果

测试使用从BOSSbase随机抽取并转换的10幅JPEG图像。(3,4)设置下任意3份影子可恢复秘密；所测影子的结构相似度接近0，AC块特征变化率接近100%，表III中DC溢出数及比例均为0。这些是指定测试范围内的结果，并非对所有输入的无条件保证（PDF第10—12页）。

## 贡献与局限

贡献是联合解决JPEG压缩域的影子特征泄露与DC溢出问题，兼顾恢复与格式兼容。实验规模有限，视觉与统计指标不等同于完整安全证明；当前采用固定(k,n)阈值，动态访问结构仍属后续方向（PDF第12—13页）。

---
DOI: 10.1109/tdsc.2026.3714465 | PDF: [TDSC_2026_JPEGCompatibleSecretSharing.pdf](papers/TDSC_2026_JPEGCompatibleSecretSharing.pdf)
