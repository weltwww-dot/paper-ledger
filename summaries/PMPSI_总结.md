# PMPSI: Privacy-Preserving Predicate-Supporting Multi-Party Private Set Intersection 总结

## 基本信息

- **标题**: PMPSI: Privacy-Preserving Predicate-Supporting Multi-Party Private Set Intersection
- **作者**: Chengzhi Gao, Yihan Bao, Chang Xu, Liehuang Zhu, Hongyi Liu, Kashif Sharif, Pengbo Wang
- **期刊 / 会议**: IEEE Transactions on Dependable and Secure Computing 2026
- **发表**: 2026-09-01
- **内容状态**: 完整 · 已基于机构授权全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1109/tdsc.2026.3704390
- **arXiv**: 无
- **PDF**: [TDSC_2026_PMPSI.pdf](papers/TDSC_2026_PMPSI.pdf)

## 一句话概括

本文提出谓词支持的多方隐私集合求交（PMPSI）原语与协议，使请求方只与属性满足其私有谓词的参与方秘密计算集合交集，同时隐藏谓词、属性与匹配状态。

## 问题与动机

传统多方隐私集合求交（MPSI）把参与者视为同质实体做无差别处理，无法满足请求方按参与方属性进行细粒度筛选的需求，例如只希望与医疗或 VIP 等级的成员合作。若用属性基加密（ABE）或谓词加密（PE）配合外部可信服务器先筛选、再执行 MPSI，则属性、谓词乃至匹配状态都可能泄露给该服务器。作者由此提出研究挑战：如何设计谓词约束下的 MPSI 协议，只在满足条件的参与方间求交，同时对属性、谓词和匹配状态提供可证明的隐私保证，其典型应用场景包括跨组织安全协作与移动网络中基于带宽资源的隐私保护共享。

## 方法

作者形式化定义新原语 PMPSI：请求方 Pn 定义内积型谓词（满足条件 iff v·x = 0，支持相等、合取与集合成员等编码），仅与属性满足谓词的客户端计算元素交集，并提供谓词隐藏、属性隐藏、元素隐藏与匹配状态隐藏四重隐私保证。具体协议在诚实但好奇（honest-but-curious）模型下，以加密逆布隆过滤器（EIBF，将多个比特打包进单一 TFHE 密文槽以降低通信量）为基座，结合门限部分同态加密 TPHE（Paillier）与门限全同态加密 TFHE（BGV）完成谓词求值与过滤。核心子协议为双模式不经意比较（DMOC）：它将 TPHE 谓词结果密文转换为过滤所需的 TFHE 指示密文，并提供无 CSP 的去中心化变体 bDMOC-DC（各客户端依序置换与再随机化，打破密文位置关联以抵御共谋）；另设修正机制处理“无客户端满足谓词”的退化情形，并由请求方与随机选中的客户端联合加扰动后门限解密。

## 实验与结果

作者用 C++ 实现原型：基于 OpenFHE（BGV）构建 TFHE、GMP 实现 TPHE，环维数 8192 并开启多方噪声泛洪模式，TPHE 主密钥长度 512 比特；布隆过滤器误报率控制在 1% 以下并按输入规模动态重算参数，仅集合求交步骤做了并行化。实验将流程分为 Setup、Step 1（属性加密与 EIBF 生成）、Step 2（加密谓词计算）、Step 3（集合交集计算）四个阶段，固定 predicate_size=16，考察元素数 element_num 与客户端数 client_num 的影响。结果表明：Step 3 占主导开销且随 client_num 与 element_num 近似线性增长，Setup 开销随客户端数近似线性增长；与唯一功能相近的 Bay 等 TMPSI 协议相比，PMPSI 元素规模较小时因 FHE 初始化与旋转密钥生成需更长启动时间，规模增大后表现更优，且 TMPSI 随用户数二次增长而 PMPSI 线性扩展；谓词大小对 Step 2 影响很小，通信开销经密文槽打包后显著低于逐比特加密，整体计算与通信复杂度随参与方数量呈线性。

## 贡献与局限

贡献包括：提出 PMPSI 新原语并给出兼顾功能与安全的形式化定义；给出整合 EIBF、TPHE/TFHE 与 DMOC 的具体构造，并提供基于 CSP 与去中心化 bDMOC-DC 两种部署变体；以模拟（simulation-based）论证在诚实但好奇模型下证明协议安全（对请求方、CSP、客户端分别构造模拟器，规约至 TPHE/TFHE 的 IND-CPA 安全性）。局限方面：协议仅针对半诚实敌手，尚未支持恶意安全模型；内积谓词不能直接表达任意非线性约束或通用布尔电路，更丰富谓词需更高开销；TA 参与设置阶段（可用分布式密钥生成去中心化但为清晰展示而保留），FHE 也带来较高计算与通信成本。未来工作将关注恶意安全、进一步的计算优化以及与通用安全计算框架（如 MPC 电路）的更广泛对比。

---
DOI: 10.1109/tdsc.2026.3704390
