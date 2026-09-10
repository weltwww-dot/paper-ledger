# Contrast sensitivity in multimodal large language models: A psychophysics-inspired evaluation 总结
## 基本信息
- **标题**: Contrast sensitivity in multimodal large language models: A psychophysics-inspired evaluation
- **作者**: Pablo Hernández-Cámara, Alexandra Gomez-Villa, Jose Manuel Jaén-Lorites, Jorge Vila-Tomás, Valero Laparra, Jesús Malo
- **期刊 / 会议**: Neural Networks 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1016/j.neunet.2026.108903
- **PDF**: [NN_2026_ContrastSensitivityMLLM.pdf](papers/NN_2026_ContrastSensitivityMLLM.pdf)
## 一句话概括
本文把多模态大语言模型当作端到端观察者，用心理物理学行为实验估计其对比敏感函数。
## 问题与动机
MLLM对低层视觉特征的处理尚未系统刻画，内部激活或训练分类器也不能直接代表最终感知行为，需要可解释的黑盒测量。
## 方法
模型观察经过特定空间频率滤波的噪声刺激，并以结构化提示给出二元回答；由心理测量函数得到对比阈值和CSF，再用滤波及对抗条件下的任务表现验证其预测性。
## 实验与结果
部分开源MLLM在形状或尺度上接近人类CSF，但没有模型同时捕捉两者。CSF对提示措辞高度敏感，并能预测频率过滤和对抗条件下的表现变化。
## 贡献与局限
贡献是建立不依赖内部激活的MLLM感知诊断。局限是结果受提示、刺激设计、模型版本和语言输出稳定性影响，行为CSF不能直接等同于视觉机制。
---
DOI: 10.1016/j.neunet.2026.108903
