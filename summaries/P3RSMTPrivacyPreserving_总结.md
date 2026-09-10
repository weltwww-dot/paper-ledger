# P3RS-MT: Privacy-Preserving Personalized Recommendation Services in Medical Tourism 总结

## 基本信息

- **标题**: P3RS-MT: Privacy-Preserving Personalized Recommendation Services in Medical Tourism
- **作者**: Yan Xu, Yao Wang, Jie Cui, Hong Zhong
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/TDSC.2026.3699451
- **arXiv**: 无
- **PDF**: [TDSC_2026_P3RSMTPrivacyPreserving.pdf](papers/TDSC_2026_P3RSMTPrivacyPreserving.pdf)

## 一句话概括

本文提出 P3RS-MT，利用加权 Tanimoto 系数、CKKS 同态加密和密文上的 Newton 迭代，为医疗旅游推荐提供兼顾隐私、相似度精度与效率的个性化服务。

## 问题与动机

医疗旅游推荐通常需要比较患者医疗记录与历史服务样本，但直接上传病历会暴露高度敏感的信息。医疗特征又往往维度高、分布不均且稀疏，传统相似度方法在密文上执行时会面临效率和精度问题。尤其是加权 Tanimoto 系数包含除法，而 CKKS 同态加密原生支持加法和乘法，不直接支持密文除法；同时，医疗旅游服务商与密码服务商的协作过程也可能泄露中间相似度或用户特征。

## 方法

P3RS-MT 包含数据所有者、医疗旅游服务商 MTF、密码服务商 CSP 和用户四类实体，并在半诚实、互不串通的威胁模型下运行。用户先从匿名医疗记录中提取特征向量，再用 CKKS 加密；MTF 使用加权 Tanimoto 系数进行密文相似度计算，利用 CKKS 的 SIMD 槽和循环旋转并行聚合高维特征。针对分母除法，方案先做归一化和安全阈值处理，再用 Newton 迭代在密文上近似倒数，默认初值为 0.3。MTF 在请求 CSP 协助解密前加入随机噪声进行盲化，CSP 只看到无意义的盲化结果，MTF 去除噪声后再依据相似度阈值生成推荐。

## 实验与结果

在 WBCD 数据上，作者随机选取 100 条归一化记录并按临床重要性设置特征权重；Newton 迭代在三轮后误差已明显收敛，四轮后 RMSE 低于 0.5，最终选用三轮作为精度与效率折中。当相似度阈值为 0.65 时，误报遗漏率 FNR 为 0、召回率达到 100%；初值 0.30 时相似度误差稳定在小数点后三至四位，权重扰动 ±10% 时 Top-10 推荐集合的 Jaccard 相似度为 0.82–1.00。在运行开销方面，用户加密与上传约 19.02 ms、1.60 MB，MTF 密文相似度计算约 5.35 s、0.47 MB，CSP 协助解密约 2.77 ms、0.0078 KB，个性化推荐阶段用户解密约 1.3 s、MTF 加密约 0.03 s、通信约 54 KB。在稀疏 DARWIN 数据上，经过截断 SVD 和 10% 保留率稀疏化后，P3RS-MT 的 MAP@10 稳定接近 0.9。

## 贡献与局限

本文将适合稀疏特征的加权 Tanimoto 相似度、密文 Newton 倒数近似、CKKS 批处理和盲化协作解密组合为一套医疗旅游隐私推荐方案，并从半诚实安全、相似度精度、推荐效果和通信计算开销多方面验证。局限在于安全模型假设 MTF 与 CSP 不串通，且主要验证了半诚实行为，尚未覆盖恶意服务商、恶意用户或长期多次查询下的组合泄露；实验数据和临床权重仍是公开或处理后的数据，真实医疗部署还需要更大规模数据、访问控制和合规审计。

---
DOI: 10.1109/TDSC.2026.3699451
