# Automatic selection of protections to mitigate risks against software applications 总结

## 基本信息

- **标题**: Automatic selection of protections to mitigate risks against software applications
- **作者**: Daniele Canavese, Leonardo Regano, Bjorn De Sutter, Cataldo Basile
- **期刊 / 会议**: Computers & Security 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.cose.2026.104959
- **arXiv**: 无
- **PDF**: [COSE_2026_AutomaticSelectionProtectionsMitigate.pdf](papers/COSE_2026_AutomaticSelectionProtectionsMitigate.pdf)

## 一句话概括

本文把软件保护选择建模为攻防博弈，自动寻找兼顾抗攻击能力与运行开销的保护组合。

## 问题与动机

面对拥有软件和运行环境完全控制权的Man-at-the-End攻击者，开发者必须保护关键代码资产，同时不能让应用变得不可用。现有保护决策往往依赖人工经验，难以系统比较攻击路径、保护效果和性能代价。

## 方法

作者形式化代码工件、资产、安全需求、攻击和保护等决策要素，并以重复攻击场景建立博弈模型。防御方选择保护，攻击方寻找攻击路径；候选方案通过Software Protection Index按攻击路径效果、软件度量和专家评估比较。求解采用mini-max深度优先启发式，并用动态规划减少重复计算。

## 实验与结果

论文实现了概念验证工具，并在ASPIRE项目相关场景中进行专家评价。结果表明，自动化方案能在限制保护引入的开销的同时选择更有抵抗力的保护组合；全文没有给出可泛化的统一精度数字。

## 贡献与局限

贡献是提出面向攻击路径的保护指数和可计算的攻防选择框架，并给出原型验证。局限是模型依赖预先标注的资产、攻击路径、软件度量和专家判断，启发式求解的规模扩展及对未知攻击的适应性仍需研究。

---
DOI: 10.1016/j.cose.2026.104959
