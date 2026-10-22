---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-21T06:52:02Z
window_end_utc: 2026-10-22T06:55:38Z
generated_at_utc: 2026-10-22T06:55:38Z
item_count: 79
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-22

**统计窗口：** 2026-10-21T06:52:02Z — 2026-10-22T06:55:38Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **79** 项去重后的有效线索：真正新增论文 **4** 项、实质论文修订 **2** 项、代码/版本/项目更新 **72** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [playcanvas/supersplat v3.6.0](https://github.com/playcanvas/supersplat/releases/tag/v3.6.0) | 正式版本发布 | GitHub Release · playcanvas/supersplat | E2 | P1 |

## 分类详述

### [AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T10:05:23Z
- **更新判定：** 真正新增
- **核心内容：** High-fidelity 4D physical simulation requires accurate physical parameter assignments that align with diverse material properties. Previous methods struggle with critical bottlenecks: they either rely on computationally intensive per-scene optimization or predict parameters from purely visual inputs. The latter suffers from inherent ambiguity, e.g., the inability to distinguish the stiffness of rubber from its appearance alone. To bridge this gap, we propose AutoPhyX, a text-conditioned framework for predicting spatially-varying physical properties. Since training robust feed-forward models requires fine-grained supervision, we first introduce a novel part-controllable data generation pipeline that decomposes complex 3D assets into semantically distinct components and pairs them with physically plausible, diverse parameters and corresponding text descriptions. Leveraging this dataset, AutoPhyX employs a cross-modal modulation mechanism where text features dynamically modulate visual f…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.29517v1

### [ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T16:43:53Z
- **更新判定：** 真正新增
- **核心内容：** Language 3D Gaussian Splatting enables open-vocabulary scene understanding by associating Gaussian primitives with language features. These semantic attributes increase model storage, while most existing 3DGS compression methods are designed mainly to preserve RGB rendering quality. One straightforward approach is to apply sparsification and quantization sequentially. However, pruning based only on rendering quality can remove Gaussians that have small RGB contributions but are important for semantic prediction. Once removed, their semantic information cannot be recovered by later quantization. We propose ClunoGS, a compact framework for Language 3DGS that combines semantics-aware Gaussian sparsification and vector quantization in a unified constrained objective. Semantic supervision is used during sparsification, and the objective jointly considers rendering quality, semantic accuracy, and compactness. We optimize the unified objective with alternating primal, sparsification, quantiz…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.30013v1

### [AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T13:13:00Z
- **更新判定：** 真正新增
- **核心内容：** Large-scale aerial resources provide a foundation for learning navigation across diverse environments. However, existing resources remain limited in providing (1) densely sampled flight demonstrations for learning different policy formulations and (2) broad environment coverage for standardized closed-loop evaluation. To address these limitations, we introduce AirPlayground, a unified benchmark for training and evaluating aerial navigation policies across diverse environments. We first construct 94 photorealistic 3D Gaussian Splatting (3DGS) environments spanning indoor, urban outdoor, and vegetation settings, with aligned collision geometry. Building on these environments, we develop a scene-adaptive pipeline for automated expert flight collection, yielding 94K demonstrations and 46.5M synchronized observation-state-action samples at 50 Hz. We further provide an extensible API that supports training different policy formulations on this shared corpus and evaluating them under unified…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.29699v1

### [AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T08:02:14Z
- **更新判定：** 真正新增
- **核心内容：** Robots deployed in human-centered environments need maps that support both geometric navigation and open-vocabulary semantic queries beyond a fixed label set. A key challenge is enriching such maps with semantic information without relying on manually annotated segmentation masks or closed-set semantic categories. Existing geometry-driven active mapping maximizes coverage but treats semantics as a passive by-product of the collected trajectory, whereas active semantic mapping typically depends on supervised semantic segmentation. We present AOV-GS, an active 3D Gaussian mapping system that guides exploration using frozen foundation models. During coarse exploration, AOV-GS re-ranks geometrically promising candidate views according to CLIP mask-embedding novelty computed from SAM instance segmentation, biasing exploration toward semantically informative regions. Frozen SAM and CLIP provide instance masks and language-aligned embeddings throughout mapping, while a lightweight scene-spec…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.29374v1

### [NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T10:53:14Z
- **更新判定：** 实质修订
- **核心内容：** Training-free weighted aggregation is widely used to lift 2D semantic features onto 3D Gaussians for open-vocabulary scene understanding, yet its theoretical role remains insufficiently understood. Existing analyses typically justify this operation from the rendering side, treating Gaussian features as linearly composable Euclidean variables for reconstructing 2D feature maps. However, this view does not match downstream 3D usage, where each Gaussian is often queried independently in a cosine-based embedding space. We revisit feature lifting from the 3D side and formulate per-Gaussian assignment as a cosine alignment problem on the CLIP unit sphere. Under this objective, the $\ell_2$-normalized semantic back-projected feature emerges as the closed-form solution, providing a complementary interpretation of the standard lifting rule from the perspective of per-Gaussian semantic assignment. This solution is still a convex combination of the observed directions, so every lifted feature is…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2609.18898v2

### [Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis](https://arxiv.org/abs/2604.11685v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-21T11:06:25Z
- **更新判定：** 实质修订
- **核心内容：** 3D Gaussian Splatting (3DGS) has become a state-of-the-art framework for real-time, high-fidelity novel view synthesis. However, its substantial storage requirements and inherently unstructured representation pose challenges for deployment in streaming and resource-constrained environments. Existing Level-of-Detail (LOD) strategies, particularly those based on bottom-up construction, often introduce redundancy or lead to fidelity degradation. To overcome these limitations, we propose Iterative Gaussian Synopsis, a novel framework for compact and progressive rendering through a top-down "unfolding" scheme. Our approach begins with a full-resolution 3DGS model and iteratively derives coarser LODs using an adaptive, learnable mask-based pruning mechanism. This process constructs a multi-level hierarchy that preserves visual quality while improving efficiency. We integrate hierarchical spatial grids, which capture the global scene structure, with a shared Anchor Codebook that models local…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.11685v2

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T05:12:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [samaust/openftgs](https://github.com/samaust/openftgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T05:33:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on openftgs-synth datasets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [AbsoluteZer0527/Gaussian-Cake](https://github.com/AbsoluteZer0527/Gaussian-Cake)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T06:43:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A computer graphics project that uses optimal transport to morph model A into model B smoothly.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AbsoluteZer0527/Gaussian-Cake

### [DrDWatt/fvdb-docker](https://github.com/DrDWatt/fvdb-docker)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T02:21:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Docker workflow for 3D Gaussian Splatting with fVDB - COLMAP processing, GPU training, rendering, and Omniverse integration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DrDWatt/fvdb-docker

### [ZX-123155/us-3dgs-reproduction](https://github.com/ZX-123155/us-3dgs-reproduction)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T00:20:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Ultrasound 3D Gaussian Splatting reproduction on RTX 3060 Laptop 6GB: UltraGS (ICME 2026) and UltraG-Ray (MIDL 2026) - training logs, metrics, comparison renders
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZX-123155/us-3dgs-reproduction

### [reukem/viettel-ai-3dgs](https://github.com/reukem/viettel-ai-3dgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T23:24:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Viettel AI Race 2026 - Track 1: 3D Gaussian Splatting for Telecom BTS Digital Twin with Optical Center Shift & SOTA Optimization
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reukem/viettel-ai-3dgs

### [thepunisher746000-afk/3dgs-optimisation](https://github.com/thepunisher746000-afk/3dgs-optimisation)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T15:11:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thepunisher746000-afk/3dgs-optimisation

### [wMito/ColonSplat](https://github.com/wMito/ColonSplat)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T03:20:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ColonSplat: Reconstruction of Peristaltic Motion in Colonoscopy with Dynamic Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wMito/ColonSplat

### [SamueleMara/RigEuler3DGS](https://github.com/SamueleMara/RigEuler3DGS)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T00:55:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Dynamic RigEuler 3D Gaussian Splatting with joint motion estimation
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SamueleMara/RigEuler3DGS

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T11:46:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG and RAD.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [AndriiShramko/shramko-sog-lod-converter](https://github.com/AndriiShramko/shramko-sog-lod-converter)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T16:00:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Convert giant 3D Gaussian Splatting PLY (100M+ splats, 10+ GB) into a SuperSplat-ready Streamed SOG .zip with real LODs, in your browser on your own GPU (WebGPU). No upload, no install. By Andrii Shramko.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/shramko-sog-lod-converter

### [Xget7/splatkit-ios](https://github.com/Xget7/splatkit-ios)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T20:44:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Metal Gaussian splatting SDK for iOS: Swift view, GPU visibility/radix, experimental LOD and hybrid tiles. MIT source and reproducible XCFramework.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit-ios

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T11:44:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A comprehensive list of Implicit Representations, NeRF and 3D Gaussian Splatting papers relating to SLAM/Robotics domain, including papers, videos, codes, and related websites
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T05:18:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T02:08:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Reconstruction of UCLA Gateway Plaza from unstaged outdoor scene video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS

### [enhansome/enhansome-NeRF-and-3DGS-SLAM](https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T01:33:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [MingChaoSun/MingChaoSun.github.io](https://github.com/MingChaoSun/MingChaoSun.github.io)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T17:23:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mingchao Sun (孙铭超) — Researcher at Alibaba Group (AMap). 3D reconstruction & generation, Gaussian Splatting, world models, embodied intelligence.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MingChaoSun/MingChaoSun.github.io

### [BlueStylo/drone-gaussian-pipeline](https://github.com/BlueStylo/drone-gaussian-pipeline)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:33:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Drone video → Gaussian Splatting on Apple Silicon: reconstruction, validation, interactive viewer and public delivery.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/BlueStylo/drone-gaussian-pipeline

### [SuperInstance/splat-room](https://github.com/SuperInstance/splat-room)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:19:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ASCII-guided 3D Gaussian splatting for rapid room learning - ASCII/edge structure as the middle layer, audio mapping as depth sense
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SuperInstance/splat-room

### [KuoFengYuan/KuoFengYuan](https://github.com/KuoFengYuan/KuoFengYuan)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:03:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D reconstruction, Gaussian Splatting, and on-device AI.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KuoFengYuan/KuoFengYuan

### [ColinMacM/3DGS-maker](https://github.com/ColinMacM/3DGS-maker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T22:16:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** iPhone ARKit app that captures portrait JPEGs with matching camera poses for Metashape / 3D Gaussian Splatting, with a USB/Wi-Fi desktop receiver
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ColinMacM/3DGS-maker

### [gusgusr9s/3dgs-colmap-from-360camera](https://github.com/gusgusr9s/3dgs-colmap-from-360camera)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T16:46:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gusgusr9s/3dgs-colmap-from-360camera

### [zeinrachidi-svg/INSA-SLAM-3DGS-DATA-AUTOMATION](https://github.com/zeinrachidi-svg/INSA-SLAM-3DGS-DATA-AUTOMATION)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T10:37:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zeinrachidi-svg/INSA-SLAM-3DGS-DATA-AUTOMATION

### [shisyy/SemGuard](https://github.com/shisyy/SemGuard)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T23:04:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of "SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shisyy/SemGuard

### [changruizhu96/LEGO-SCD](https://github.com/changruizhu96/LEGO-SCD)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T21:03:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection. Code release in preparation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/changruizhu96/LEGO-SCD

### [takumanakata/gs-editor](https://github.com/takumanakata/gs-editor)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T08:50:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ブラウザだけで 3DGS（Gaussian Splatting）を開いて、掃除し、原点と向きを直して書き出すエディタ。インストール不要
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/takumanakata/gs-editor

### [playcanvas/supersplat v3.6.0](https://github.com/playcanvas/supersplat/releases/tag/v3.6.0)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-21T15:05:18Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Update all npm dependencies by @renovate[bot] in https://github.com/playcanvas/supersplat/pull/1074 * Support 2-point vertical alignment in the orient tool by @slimbuck in https://github.com/playcanvas/supersplat/pull/1075 * Update dependency @playcanvas/splat-transform to v3.10.2 by @renovate[bot] in https://github.com/playcanvas/supersplat/pull/1076 * Export the selected SH band count, zero-padding missing bands by @Yang-SyZng in https://github.com/playcanvas/supersplat/pull/1063 ## New Contributors * @Yang-SyZng made their first contribution in https://github.com/playcanvas/supersplat/pull/1063 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.5.2...v3.6.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T03:21:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high performance 3DGS renderer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-viewer

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T02:24:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository tracks the latest advancements in 3D Gaussian Splatting from Arxiv, with daily automated updates. Stay up-to-date with cutting-edge research in this exciting field!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/longxiang-ai/awesome-gaussians

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T02:23:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [playcanvas/splat-transform](https://github.com/playcanvas/splat-transform)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T19:08:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CLI tool and library for 3D Gaussian splat processing and conversion
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/splat-transform

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T03:07:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 900 arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Xget7/splatkit](https://github.com/Xget7/splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T20:31:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time Gaussian splatting SDKs for Android/Vulkan, iOS/Metal and React Native, sharing a C++17 engine.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit

### [Shawn100861224/web3d-lab](https://github.com/Shawn100861224/web3d-lab)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T09:20:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS 在线重建查看器 + 个人主页（郑州大学双足实验室 3D 方向考核作品）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Shawn100861224/web3d-lab

### [AndriiShramko/ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T16:21:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [Saqoosha/ghostline](https://github.com/Saqoosha/ghostline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T16:17:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Recover FPV flight paths from goggle DVR on a 3DGS scan, and replay them
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Saqoosha/ghostline

### [Xget7/react-native-splatkit](https://github.com/Xget7/react-native-splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T20:44:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** React Native component for real-time Gaussian splatting: load an SPZ scene, pick a quality preset, and walk through it from JavaScript.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/react-native-splatkit

### [ryanjosephkamp/splashery-experimental](https://github.com/ryanjosephkamp/splashery-experimental)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T06:53:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Experimental viewing tools and renderer work for Gaussian splat toys.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ryanjosephkamp/splashery-experimental

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:44:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Loppas/playcanvas-quake3](https://github.com/Loppas/playcanvas-quake3)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:34:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A port of ioquake to the Playcanvas engine with the added ability to render gaussian splat maps
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Loppas/playcanvas-quake3

### [tykx1373/3DGS-Smart-System](https://github.com/tykx1373/3DGS-Smart-System)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T04:29:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS轻量化适配
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tykx1373/3DGS-Smart-System

### [VAAN0524/off-axis-demo](https://github.com/VAAN0524/off-axis-demo)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T02:07:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 头部视差 · 离轴投影 3DGS 查看器（MediaPipe + Three.js WebGPU）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/VAAN0524/off-axis-demo

### [3XyzMedia/VIEWER](https://github.com/3XyzMedia/VIEWER)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T23:20:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Любительские модели 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3XyzMedia/VIEWER

### [STEVVVU/gaussian-splat-renderer](https://github.com/STEVVVU/gaussian-splat-renderer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T22:41:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WebGPU Gaussian splat renderer with covariance projection, GPU radix sorting, spherical harmonics, and pixel readback checks; based on UPenn CIS5650.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/STEVVVU/gaussian-splat-renderer

### [Yellow-Dog-Man/Splat.NET](https://github.com/Yellow-Dog-Man/Splat.NET)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T21:09:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** C# / .NET library for reading gaussian splat file formats (PLY, SPZ, GLB, SOG)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Yellow-Dog-Man/Splat.NET

### [seemandhar/SplatLab](https://github.com/seemandhar/SplatLab)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T21:02:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [NeurIPS 2026] SplatLab: Autonomous Scientific Discovery for 3DGS Research. From a one-line idea to reproduced baselines, real GPU experiments, and a compiled paper, driven by Claude Code.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/seemandhar/SplatLab

### [c2jxmrywdn-del/bloom-sense](https://github.com/c2jxmrywdn-del/bloom-sense)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T20:54:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 拈花 BloomSense · 摄像头手势驱动的 3DGS 实景花境 + Blender 程序化花卉交互系统 | Hand-gesture 3DGS flower garden (React Three Fiber · MediaPipe · Spark)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/c2jxmrywdn-del/bloom-sense

### [sxzhuang0613-stack/3dgs-cardiac](https://github.com/sxzhuang0613-stack/3dgs-cardiac)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T17:23:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sxzhuang0613-stack/3dgs-cardiac

### [aozi6666/Sparse-3DGS-heritage-VQA](https://github.com/aozi6666/Sparse-3DGS-heritage-VQA)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T11:36:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 受限采集下的稀疏视角 3DGS 文化遗产重建 + 多模态大模型·VQA-VL 流式视频问答与空间定位系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aozi6666/Sparse-3DGS-heritage-VQA

### [firefly1145141919810/cg-3dgs-baseline](https://github.com/firefly1145141919810/cg-3dgs-baseline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T10:59:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible original 3D Gaussian Splatting baseline and Chinese learning notes
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/firefly1145141919810/cg-3dgs-baseline

### [manishtandurkar/adaptive-3dgs](https://github.com/manishtandurkar/adaptive-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T09:48:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Resource-pressure-aware adaptive rendering for 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manishtandurkar/adaptive-3dgs

### [KusMar00/camera-sonar-3dgs](https://github.com/KusMar00/camera-sonar-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T08:58:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KusMar00/camera-sonar-3dgs

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T06:52:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [simontheuseful/gpu-pro26-3dgs](https://github.com/simontheuseful/gpu-pro26-3dgs)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T08:20:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/simontheuseful/gpu-pro26-3dgs

### [Add copy/paste to the transform and colors panels (#1077)](https://github.com/playcanvas/supersplat/commit/ebce8e6e3f3f41f3a816f35a0f4fe27beacaae53)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-21T20:51:53Z
- **更新判定：** 代码实质更新
- **核心内容：** Add copy/paste to the transform and colors panels (#1077)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Support 2-point vertical alignment in the orient tool (#1075)](https://github.com/playcanvas/supersplat/commit/c5b0cca4441c99d11bcbdcd8ddc26040178de232)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-21T14:32:28Z
- **更新判定：** 代码实质更新
- **核心内容：** Support 2-point vertical alignment in the orient tool (#1075)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [3.6.0](https://github.com/playcanvas/supersplat/commit/8c28d7219727c9e07be8ce8d818485e94d9206d5)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-21T15:03:04Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.6.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Export the selected SH band count, zero-padding missing bands (#1063)](https://github.com/playcanvas/supersplat/commit/0fa3bb58c4d228351475374db70d4dfce16d18a0)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-21T14:58:41Z
- **更新判定：** 代码实质更新
- **核心内容：** Export the selected SH band count, zero-padding missing bands (#1063)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [lukehollis/sphr](https://github.com/lukehollis/sphr)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T16:54:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open, hackable 3d digital twin builder that supports 3d gaussian splatting, 360 images, and vfx
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lukehollis/sphr

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T03:10:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [hh-hang/3dgs-weather](https://github.com/hh-hang/3dgs-weather)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T00:54:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS 天气系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hh-hang/3dgs-weather

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T07:31:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [cysc0286/FPGA43DGS](https://github.com/cysc0286/FPGA43DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T06:39:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Realize 3DGS by FPGA
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cysc0286/FPGA43DGS

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T06:09:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [weeeha/location-lab](https://github.com/weeeha/location-lab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-22T01:34:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Scout a real place as a Gaussian splat and export Seedance 2.0 reference packs
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/weeeha/location-lab

### [antoineMoPa/splatting-rs](https://github.com/antoineMoPa/splatting-rs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T19:41:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** My experiments with gaussian splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/antoineMoPa/splatting-rs

### [PrometheosFire/avsplat-sim-project-page](https://github.com/PrometheosFire/avsplat-sim-project-page)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T18:03:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for Photorealistic Closed-Loop Simulation for Autonomous Driving using 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/PrometheosFire/avsplat-sim-project-page

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T15:36:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [AssassinHLQ/csust](https://github.com/AssassinHLQ/csust)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T14:46:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Godot 4.7 越肩射击 + 跑酷 + 期货交易沙盒《长沙理工：2067》：12 段 571 m 跑酷、暗网比纳、保证金/负债/强平经济、3D 高斯泼溅校园
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AssassinHLQ/csust

### [glxy404310/my-3dgs](https://github.com/glxy404310/my-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T11:11:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/glxy404310/my-3dgs

### [knt0613pow/DCF-3DGS](https://github.com/knt0613pow/DCF-3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T10:06:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/knt0613pow/DCF-3DGS

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-21T09:11:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

### [Hammington/3dgs](https://huggingface.co/Hammington/3dgs)

- **主题：** 其他
- **来源：** Hugging Face 模型
- **发布时间/更新时间：** 2026-10-21T17:16:57Z
- **更新判定：** 模型更新
- **核心内容：** 近期更新的模型；标签：region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 6 |
| GitHub | ok: 72 |
| Hugging Face | ok: 1 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 6/6 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

