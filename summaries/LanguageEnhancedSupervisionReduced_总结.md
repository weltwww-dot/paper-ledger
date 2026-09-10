# A Language-Enhanced Supervision-Reduced Analysis Framework for Multibranching Vessels 总结

## 基本信息

- **标题**: A Language-Enhanced Supervision-Reduced Analysis Framework for Multibranching Vessels
- **作者**: Xi-Yao Ma, Shi-Qi Liu, Xiao-Liang Xie, Xiao-Hu Zhou, Zeng-Guang Hou, Xin-Kai Qu, Wen-Zheng Han, Ming Wang, Meng Song, Chu-Tian Zhang
- **期刊 / 会议**: IEEE Transactions on Artificial Intelligence 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 人工智能
- **DOI**: 10.1109/tai.2026.3681535
- **arXiv**: 无
- **PDF**: [TAI_2026_LanguageEnhancedSupervisionReduced.pdf](papers/TAI_2026_LanguageEnhancedSupervisionReduced.pdf)

## 一句话概括

本文提出由语言增强端点检测 LEED 和端点引导的 TS-Seg 组成的低监督冠状动脉多分支分析框架，在减少精细标注的同时定位血管端点、分割指定分支并生成辅助临床分析报告。

## 问题与动机

冠状动脉造影是介入规划和动脉粥样硬化评估的重要影像来源，但多分支血管的端点稀疏、分支定义不统一，逐像素标注成本高，现有方法往往只能分割所有血管或依赖大量专家标注。仅凭图像外观，模型还难以利用临床医生对投照角度、解剖位置和分支关系的语言知识。作者希望把临床语言先验引入端点定位，再用少量结构信息完成指定血管分支的分割，降低对密集分支标注的依赖，并为术前规划和术后评估提供更完整的分析结果。

## 方法

框架第一阶段是 LEED 跨模态语言增强端点检测网络：视觉特征与由临床知识构造的投照位置、端点描述等文本提示对齐，以增强多个端点之间的全局结构一致性。第二阶段是 TS-Seg，通过检测到的端点、灰度信息和点引导约束，结合边界与关键点信息提取目标血管分支，并抑制无关或冗余分支。推理时可以使用 LEED 预测端点；临床医生也可以手动补充新的端点，再单独运行 TS-Seg 分析此前未定义的分支。最终框架依据临床先验汇总血管分析结果，形成辅助报告。

## 实验与结果

实验使用两个内部端点数据集 RCAE（2,276 张图像、269 个病例）和 LCAE（3,225 张图像、219 个病例），并在公共 XCAD 的 XCAD-R 与 XCAD-L 子集上测试。LEED 采用 PCK（阈值 15 像素）和平均像素距离 APD 评价，在 RCAE 上取得平均 PCK `0.770`、APD `12.85`，在 LCAE 上取得 `0.818`、`7.78`；语言分支相对视觉基线分别带来 RCAE 上 3.7% PCK 和 0.74 APD、LCAE 上 3.9% PCK 和 1.81 APD 的改进。XCAD-R/XCAD-L 上 LEED 的 PCK/APD 分别为 `0.737/14.33` 和 `0.614/17.71`。使用真值端点时，TS-Seg 在 RCAE/LCAE 上的 mF1/mIoU 为 `0.845/0.736` 与 `0.879/0.785`；改用 LEED 预测端点后仍达到 `0.813/0.709` 与 `0.772/0.687`，总体优于多数监督式分割基线。

## 贡献与局限

贡献包括：用临床语言知识改善多端点定位；用端点和灰度结构实现较低监督成本的指定分支分割；允许新增端点后复用分割模块，并把结果组织成临床分析报告。局限是 LEED 的端点误差会传递到 TS-Seg，预测端点下的分割性能明显低于真值端点；XCAD 因未微调且图像质量较低，所有方法的性能都下降，LEED 仅取得左右冠脉的第二梯队结果。语言提示的收益还依赖投照角度和医学术语表达，复杂组合角度若描述不充分可能造成歧义；实际临床使用仍需更大规模、多中心数据和前瞻性验证。

---
DOI: 10.1109/tai.2026.3681535
