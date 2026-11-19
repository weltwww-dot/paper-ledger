# Image watermarking with adversarial attack on secret key networks: From zero-bit to semantic vectors 总结

## 基本信息
- **标题**: Image watermarking with adversarial attack on secret key networks: From zero-bit to semantic vectors
- **作者**: Feiyu Chen、Ziquan Liu、Wei Lin 等
- **期刊 / 会议**: Neural Networks 2026
- **卷期 / 文章号**: 206，文章号109894
- **发表**: 2026-11-11
- **日期来源**: 出版社正式 PDF 首页 Available online
- **内容状态**: 完整 · 已基于出版社正式版全文完成中文六段式总结
- **研究方向**: 信息安全
- **DOI**: 10.1016/j.neunet.2026.109894 | 📄 [NN_2026_secret-key-semantic-image-watermarking_109894.pdf](papers/NN_2026_secret-key-semantic-image-watermarking_109894.pdf)
- **PDF许可**: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## 一句话概括
该框架训练秘密密钥网络使自然图像响应服从标准正态分布，再将零比特检测扩展到可恢复消息和句子语义向量，并以统计检验验证水印。

## 问题与动机
零比特水印可检测图像是否带有标记，却不承载语义信息，并可能遭伪造或替换；传统多比特水印能传消息，但长度固定且单比特错误可能损坏整句。研究希望在保持图像水印隐蔽和可检测的基础上，引入私有密钥验证，并探索可恢复比特消息及语义句子的方式。

## 方法
方法训练秘密密钥网络（SKN），使未标记自然图像的输出接近标准多元正态分布；嵌入时以受限、动量式图像优化，使网络响应趋向私有签名向量（SKS）。检测通过响应长度与方向角的假设检验区分水印图像和自然图像。多比特方案用编码器—解码器把二进制消息映射至SKS表示；句子方案将CLIP句向量映射到水印空间，再由GPT-2解码恢复文本，绕过固定比特串的语义限制。

## 实验与结果
在MSCOCO及常见图像变换下评测零比特检测、图像质量、安全性和消息恢复。PSNR目标32时，SKN-M-32水印图像PSNR为32.56 dB、SSIM为0.9768；零比特组合检验在水印样本上的显著性水平0.05检测率为99.80%。伪造签名实验中，使用新模型生成假签名的错误通过率为5.08%，低于SSLWM的100%。但旋转或裁剪加重时该方法检测性能下降。句子向量恢复的语义相似度为0.8705（SKN-U-512），随机向量基线为0.5992。

## 贡献与局限
工作将统计密钥检测与消息级水印统一到SKN表示中：零比特验证依赖秘密模型与签名，多比特方案恢复二进制串，句子向量方案则直接保持语言语义。实验支持其在隐蔽性、伪造抵抗和部分常见失真下的有效性；句子水印比固定比特长度更灵活。局限是旋转和严重裁剪会削弱检测，生成式语义编辑对各方法都很具破坏性；多比特误码会随消息位数增长，结论也依赖SKN/SKS安全保存的假设，不能覆盖密钥泄漏情形。

---
DOI: 10.1016/j.neunet.2026.109894 | 📄 [NN_2026_secret-key-semantic-image-watermarking_109894.pdf](papers/NN_2026_secret-key-semantic-image-watermarking_109894.pdf)
