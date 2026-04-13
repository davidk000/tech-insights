# HuggingFace 趋势简报 · 2026-04-13

> 数据来源：HuggingFace 趋势模型页 + HF Blog | 统计周期：2026-04-07 ~ 2026-04-13

---

## 一、下载量TOP模型

| 排名 | 模型 | 下载量 | 任务 | 参数量 | 更新 | 亮点 |
|:---:|------|--------|------|--------|------|------|
| 1 | **Qwen/Qwen3.5-27B** | 2.29M | Image-Text-to-Text | 28B | 28天前 | 通义千问旗舰，开源多模态顶流 |
| 2 | **unsloth/Qwen3.5-35B-A3B-GGUF** | 2.10M | Image-Text-to-Text | 35B | 19天前 | A3B稀疏架构+GGUF量化，社区微调首选 |
| 3 | **unsloth/Qwen3.5-9B-GGUF** | 1.31M | Image-Text-to-Text | 9B | 22天前 | GGUF格式，适合本地推理 |
| 4 | **deepseek-ai/DeepSeek-OCR-2** | 1.25M | Image-Text-to-Text | 3B | ~2026-02 | 深度求索OCR，多语言文档理解 |
| 5 | **Qwen/Qwen3-Coder-Next** | 1.25M | Text Generation | 80B | ~2026-02 | 代码生成专项，千问代码模型 |

---

## 二、多模态 & 视觉语言模型

### Gemma 4（Google DeepMind）⭐ 本周重磅
- **发布**：2026-04-02，Apache 2.0 许可（真正开源）
- **规模**：31B / 26B A4B / E4B / E2B
- **亮点**：
  - Shared KV Cache 减少冗余投影，提升推理效率
  - Vision Encoder 支持原始宽高比 + 多维 RoPE
  - Pareto 前沿级 Arena 得分，在同尺寸下性能领先
  - 支持 Transformers / llama.cpp / MLX / WebGPU 全平台
- **Benchmark 表现**：MMLU Pro 85.2%（31B）、LiveCodeBench 80.0%、AIME 2026 89.2%

### Microsoft Phi-4-Reasoning-Vision-15B（新增）
- **下载**：24k | **更新**：5天前
- **亮点**：推理+视觉双能力，CUA（计算机使用代理）任务强项；240 B200 GPU × 4天训练，数据驱动路线，专注可控性

### DeepSeek-OCR 系列（持续热门）
- `deepseek-ai/DeepSeek-OCR-2`：3B，1.25M 下载
- `deepseek-ai/DeepSeek-OCR`：3B，2.98M 下载（历史累计）
- 专注文档理解，多语言 OCR 场景落地首选

### NVIDIA Nemotron-3-Super-120B-A12B-NVFP4（本周新增）
- **下载**：869k | **更新**：8小时前
- **精度**：NVFP4（NVIDIA FP4量化），FP4精度训练推理
- 机构向，高效推理方案

---

## 三、开源大模型 · 新晋 / 突破

| 模型 | 参数量 | 下载量 | 更新 | 亮点 |
|------|--------|--------|------|------|
| **zai-org/GLM-5** 🆕 | 754B | 148k（24h内） | 17小时前 | 智谱GLM系列最大版本，含DSA架构+异步RL |
| **HauhauCS/Qwen3.5-122B-A10B-Uncensored** 🆕 | 122B | 32.6k | 2天前 | 无审查版，适合安全研究 |
| **HauhauCS/Qwen3.5-4B-Uncensored** | 4B | 138k | 21天前 | 小参数无审查，GGUF生态 |
| **Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-GGUF** 🆕 | 9B | 136k | 9天前 | 从Claude 4.6 Opus蒸馏推理能力，GGUF格式 |

---

## 四、量化 & 微调生态（GGUF热门）

量化/微调方向持续是 HF 社区最大增长引擎，Qwen3.5 衍生模型占据下载量前列：

- **unsloth** 主打高质量 GGUF 量化包（9B/35B-A3B），专注本地推理
- **GGUF** 格式成为小显存（≤24GB）部署标准
- LoRA 微调版本涌现：`Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-GGUF` 代表蒸馏+量化结合新范式
- `microsoft/Phi-4-reasoning-vision-15B` 同步支持 vLLM bf16 推理

---

## 五、社区 & 生态亮点

- **HF 总规模**：>2.5M 模型，13M 用户（2025年数据）
- **平均开源模型参数**：从2023年827M → 2025年20.8B，增长25倍
- **机器人学崛起**：LeRobot（HF开源机器人库）GitHub stars 近3倍增长
- **韩国力量**：2026年2月韩国3个模型同时进入 HF Trending；2026年3月韩国+美国占据趋势榜主导
- **个人开发者**：2025年新趋势模型第四大贡献者为个人用户（非机构）
- **中国主导**：2025年新晋趋势模型多数源自中国或基于中国模型衍生（Qwen/DeepSeek/GLM）

---

## 六、论文热点（2026-04-07~04-13）

| 论文 | 机构 | 方向 |
|------|------|------|
| **Gemma 4** | Google DeepMind | 设备端多模态智能 |
| **GLM-5** | 智谱AI | DSA架构+异步RL |
| **VOID** | Netflix | 视频物体删除（VLM+扩散） |
| **MuRF** | KAIST | 多尺度视觉基础模型 |
| **S2D2** | — | 扩散LLM自推测解码 |
| **FinMCP-Bench** | 阿里 | 金融LLM Agent评测 |

---

## 七、趋势研判

1. **Gemma 4 Apache 2.0 是今年最重大开源事件**——真正的开源许可+强力 benchmark 表现将重塑移动/端侧模型格局
2. **Qwen3.5 生态统治地位稳固**，衍生模型数量和下载量双领先，GGUF量化链路最成熟
3. **蒸馏+量化结合**（Opus Reasoning Distilled → GGUF）成为小参数高效推理新范式
4. **754B GLM-5** 若实际推理质量达标，将对标 GPT-4o / Claude-3.5 级别闭源模型
5. **机器人具身智能**成为 HF 增长最快子社区之一，LeRobot 生态正在复制当年 Transformers 的增长曲线

---

*报告生成：2026-04-13 14:00 CST | 数据截取自 HF 趋势页及公开 Blog*
