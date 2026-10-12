# WSymBERT: a weighted neuro-symbolic model for interpretable CVSS prediction 总结

## 基本信息
- **标题**: WSymBERT: a weighted neuro-symbolic model for interpretable CVSS prediction
- **作者**: Seyedeh Leili Mirtaheri、Amirhossein Majd、Reza Shahbazian、Georgios Spathoulas、Aida Akbarzadeh、Andrea Pugliese
- **期刊 / 会议**: International Journal of Information Security 2026
- **发表**: 2026-10-11
- **内容状态**: 完整 · 已依据出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1007/s10207-026-01342-x
- **PDF**: [IJIS_2026_WSymBERTCVSSPrediction.pdf](papers/IJIS_2026_WSymBERTCVSSPrediction.pdf)

## 一句话概括
WSymBERT 将语言模型表示与安全专家知识结合，从漏洞描述预测 CVSS v3.1 的八项基本指标，再用标准公式计算严重性分数，同时单独分析预测所依赖的文本证据。

## 问题与动机
人工漏洞评分难以跟上漏洞披露速度，延误补丁优先级判断。纯文本模型虽能自动预测，却可能依赖表面词语关联，且事后高亮词语不等于其决策符合安全领域逻辑。

## 方法
作者为八项指标分别训练独立 SBERT 模型，将专家决策树衍生词表与 KeyBERT 关键词转成符号权重，与学习得到的词元池化权重融合。没有符号命中时保留神经表示；模型之间不共享编码器，也不是一个联合多任务模型。解释性通过 Integrated Gradients 及扰动指标另行评估，不把池化权重当成因果解释。

## 实验与结果
在 NVD 与 Combine 两个漏洞语料上，采用去重后的随机分层80%/10%/10%划分，八项基本指标的平均准确率分别为96.2%和94.7%，报告值高于文中所评估基线。归因分析在指定协议下更关注安全相关词语；这些是单次运行的观察结果，不构成统计显著性或未来漏洞泛化的证明。

## 贡献与局限
论文提供了可追溯的领域知识注入机制，并将预测性能与解释质量分开检验。局限包括未采用时间划分，缺少多随机种子、配对显著性检验和组件消融；固定词表及权重对版本变化和恶意描述的适应性尚未验证。八个独立模型的训练成本也未系统比较，不能据此宣称效率优势。

---
DOI: 10.1007/s10207-026-01342-x | 📄 [PDF](papers/IJIS_2026_WSymBERTCVSSPrediction.pdf)
