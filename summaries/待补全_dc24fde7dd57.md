# ShadowCode: Toward (Automatic) External Prompt Injection Attack Against Code LLMs 总结

## 基本信息

- **标题**: ShadowCode: Toward (Automatic) External Prompt Injection Attack Against Code LLMs
- **作者**: 待补全（本轮目录抓取未请求作者字段）
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 部分 · 已获取机器摘要，待人工六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3703498
- **arXiv**: 无
- **PDF**: 待探测

## 一句话概括

Recent advancements have led to the widespread adoption of code-oriented large language models (Code LLMs) for programming tasks. Despite their success in deployment, their security research is left far behind. This paper introduces a new attack paradigm: (automatic) external prompt injection against Code LLMs, where attackers generate concise, non-functionalinduced perturbationsand inject them within a victim's code context. These induced perturbations can be disseminated through commonly used dependencies (e.g., packages or RAG's knowledge base), manipulating Code LLMs to achieve malicious objectives during the code completion process. Compared to existing attacks, this method does not necessitate control over the model's training process, unlike backdoor attacks, and can achieve specific malicious objectives that are challenging for adversarial attacks. Furthermore, we proposeShadowCode, a simple yet effective method that automatically generates induced perturbations based on code simulation to achieve effective and stealthy external prompt injection.ShadowCodedesigns its perturbation optimization objectives by simulating the victim's code contexts and employs a greedy optimization approach with two enhancement modules: forward reasoning enhancement and keyword-based perturbation design. We evaluate our method across 13 distinct malicious objectives, generating 31 threat cases spanning three popular programming languages. Our results demonstrate thatShadowCodesuccessfully attacks three representative open-source Code LLMs (achieving up to a 97.9% attack success rate) and two mainstream commercial Code LLM-integrated applications (with over 90% attack success rate) across all threat cases, using only a 12-token non-functional induced perturbation. The code is available athttps://github.com/LianPing-cyber/ShadowCodeEPI.

## 问题与动机

待人工补全。

## 方法

待人工补全。

## 实验与结果

待人工补全。

## 贡献与局限

待人工补全。

---
DOI: 10.1109/tdsc.2026.3703498
