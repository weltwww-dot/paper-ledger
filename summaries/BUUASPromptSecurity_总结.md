# Efficient Prompt Security Detection for LLM Service Deployment in Edge-Cloud Networks 总结

## 基本信息

- **标题**: Efficient Prompt Security Detection for LLM Service Deployment in Edge-Cloud Networks
- **作者**: Wenjing Chen, Jie Cui, Wenjie Huang, Jing Zhang, Lu Wei, Geyong Min
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-07-03
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 系统与网络安全
- **DOI**: 10.1109/TDSC.2026.3709894
- **arXiv**: 无
- **PDF**: [TDSC_2026_BUUASPromptSecurity.pdf](papers/TDSC_2026_BUUASPromptSecurity.pdf)

## 一句话概括

BUUAS 将贝叶斯式风险信念更新、用户感知的上下文多臂老虎机和边云协同结合起来，动态把提示注入检测资源优先分配给高风险请求。

## 问题与动机

LLM 服务容易受到提示注入攻击，但现有检测系统常把所有请求按同一策略处理，既没有充分利用边云协同，也忽略用户风险和负载差异，导致检测延迟、资源消耗和安全性之间难以平衡。论文希望在用户负载变化和恶意用户比例变化时，仍能快速识别高风险请求并提高整体服务吞吐。

## 方法

BUUAS 在边缘侧使用提示注入检测器，并为每个用户维护随反馈更新的风险信念。贝叶斯式更新模块根据用户行为和检测结果刷新风险先验；信念加权上下文多臂老虎机根据风险、上下文和资源代价选择检测动作，把有限边缘资源优先用于高风险请求，同时将其他任务交由云侧处理。论文还分析了调度策略的遗憾上界和不同检测架构的吞吐表现。

## 实验与结果

实验使用 jailbreak-classification、benign-malicious-prompt-classification 和 malicious-prompts 三个公开数据集，70% 建立向量索引、30% 用于测试，并比较 Qwen-4B、7B、14B 的云端与边云方案。边云协同吞吐分别从 86.97 提升到 108.73 token/s、从 69.49 提升到 88.44 token/s、从 50.32 提升到 53.13 token/s；在不同攻击模式、用户负载和检测器设置下，BUUAS 整体保持更好的准确率、召回率、F1 和资源效率。

## 贡献与局限

论文把用户风险建模与边云安全调度结合起来，形成面向 LLM 部署的动态检测框架，并用跨数据集、跨检测器和负载变化实验验证了适应性。局限在于风险信念依赖检测反馈，数据集与提示攻击类型仍有限，边缘检测器和向量库的维护也会带来额外开销；面对新型越狱、概念漂移和强对抗用户时，在线更新的稳定性仍需长期验证。

---
DOI: 10.1109/TDSC.2026.3709894
