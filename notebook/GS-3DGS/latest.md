---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-16T08:52:06Z
window_end_utc: 2026-11-17T09:58:05Z
generated_at_utc: 2026-11-17T09:58:05Z
item_count: 64
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-17

**统计窗口：** 2026-11-16T08:52:06Z — 2026-11-17T09:58:05Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **64** 项去重后的有效线索：真正新增论文 **2** 项、实质论文修订 **1** 项、代码/版本/项目更新 **60** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation](https://arxiv.org/abs/2611.21383v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting](https://arxiv.org/abs/2611.21253v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [X-GS: An Extensible Framework for Perceiving and Thinking with 3D Gaussian Splatting](https://arxiv.org/abs/2603.09632v6) | 实质修订 | arXiv | R2/E0 | P1 |
| 4 | [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation](https://arxiv.org/abs/2611.21383v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-16T16:44:07Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting enables object-level operations on Gaussian primitives, yet existing segmentation methods are largely trained and evaluated through rendered views. This mismatch can produce accurate rendered masks from incomplete 3D selections since alpha-blended feature supervision concentrates learning on dominant contributors while leaving occluded or low-contribution Gaussians weakly supervised. We propose VODA, a plug-and-play supervision objective that exploits local depth structure to group per-pixel contributors and directly supervises all Gaussians in selected depth clusters, bypassing contribution-weighted gradient delivery. To evaluate volumetric completeness, we introduce Removal-3D, a synthetic object-removal benchmark, and the Removal Depth Error (RDE), a metric comparing predicted and ground-truth depth changes. Across four rendering-based baselines, VODA consistently improves volumetric segmentation on Removal-3D while maintaining or improving performance on LERF…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.21383v1

### [QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting](https://arxiv.org/abs/2611.21253v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-16T15:28:51Z
- **更新判定：** 真正新增
- **核心内容：** Uncertainty quantification for novel view synthesis with 3D Gaussian Splatting (3DGS) assesses rendering reliability at unseen viewpoints. This reliability depends on the discrepancy between rendered and true colors, which cannot be measured without ground-truth images. We therefore quantify uncertainty in this unknown discrepancy through upper bounds on per-pixel RGB mean absolute error. However, learned bounds may underestimate these errors and overstate rendering reliability, motivating calibration to a prescribed coverage level. In this paper, we propose QuantileGS, a post-hoc framework that combines learned rendering-error quantiles with scale-normalized conformal calibration to produce spatially adaptive error bounds. The framework comprises three phases. Phase 1, Rendering-Error Computation, measures RGB mean absolute error between observed images and predictions from a frozen 3DGS model. Phase 2, Ordered Gaussian Quantile Fields, learns two scalar attributes per Gaussian to pr…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.21253v1

### [X-GS: An Extensible Framework for Perceiving and Thinking with 3D Gaussian Splatting](https://arxiv.org/abs/2603.09632v6)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-16T09:39:55Z
- **更新判定：** 实质修订
- **核心内容：** 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications. However, most existing 3DGS methods operate in isolation, focusing on specific domains. In this paper, we introduce X-GS, an extensible framework that integrates previously isolated 3DGS methods into the perception module of a VLM for spatial tasks, with two major components: the $\textit{Perceiver}$ and the $\textit{Thinker}$. The $\textit{Perceiver}$ performs online 3DGS-based SLAM with semantic distillation and outputs semantic Gaussians from unposed video streams. It leverages recent vision foundation models for stronger geometric priors, and we introduce three novel optimizations to improve semantic distillation efficiency. The $\textit{Thinker}$ interfaces diverse VLMs with these semantic Gaussians, unlocking spatial multimodal capabilities such as 3D visual grounding and scene captioning. Experimental results on diverse benchma…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2603.09632v6

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:15:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Train, inspect, edit, automate, and export 3D Gaussian Splatting scenes from a single native application.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/LichtFeld-Studio

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T06:03:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [ElenaViewSynthesis/4dgs](https://github.com/ElenaViewSynthesis/4dgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T07:54:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [MSc Thesis]: implementation of 4D Gaussian Splatting for real-time dynamic scene reconstruction, combining spatial-temporal Gaussian deformation fields, COLMAP-based camera/point-cloud preprocessing, training pipelines, rendering, and perceptual evaluation for novel-view synthesis from dynamic multi-view data.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ElenaViewSynthesis/4dgs

### [Benevision/SplatWork](https://github.com/Benevision/SplatWork)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:24:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Make, train, view and edit 3D Gaussian splats on your own Mac, iPhone and Linux GPU machines — native Metal trainer and renderer, CUDA worker, multi-device block training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Benevision/SplatWork

### [lifeiXiao/3dgs-studio](https://github.com/lifeiXiao/3dgs-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T16:21:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Local 3D Gaussian Splatting Studio: training, interactive rendering, replay and quality metrics
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lifeiXiao/3dgs-studio

### [IRIS-LAB-whu/Tortho-Gaussian-PlusPlus](https://github.com/IRIS-LAB-whu/Tortho-Gaussian-PlusPlus)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:42:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An advanced 3DGS training framework that suppresses geometric drift and floaters in UAV scenes and automatically prunes unreliable peripheral regions, coupled with a robust gravity-aligned TDOM rendering solution
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IRIS-LAB-whu/Tortho-Gaussian-PlusPlus

### [DrDWatt/fvdb-docker](https://github.com/DrDWatt/fvdb-docker)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:37:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Docker workflow for 3D Gaussian Splatting with fVDB - COLMAP processing, GPU training, rendering, and Omniverse integration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DrDWatt/fvdb-docker

### [Closed-Loop Optimization Adds Traceable Structural Interpretability to 3D Gaussian Splatting](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6afc253ae0ec4514af21dab79020fcea&url=https%3a%2f%2fbioengineer.org%2fclosed-loop-optimization-adds-traceable-structural-interpretability-to-3d-gaussian-splatting%2f&c=8271720182301691675&mkt=en-us)

- **主题：** 训练与优化
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-16T15:07:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** Researchers designed Regularity3DGS, a framework that abstracts recurring Gaussian anchor behaviors into structural regularities to guide densification and pruning while improving neural rendering.
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [AtlantixJJ/ARG-Avatar](https://github.com/AtlantixJJ/ARG-Avatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:37:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The code release of the ARG-Avatar paper.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AtlantixJJ/ARG-Avatar

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T13:22:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG, RAD and LCC2.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [jo-chemla/3dtiled-to-3dtiles](https://github.com/jo-chemla/3dtiled-to-3dtiles)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T00:29:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [quasar-gfx/QUASAR-gs](https://github.com/quasar-gfx/QUASAR-gs)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T22:17:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Stream rendered 3D Gaussian Splatting scenes to thin clients using the QUASAR framework! (Work in Progress)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/quasar-gfx/QUASAR-gs

### [Lab-PANbin/QuantileGS](https://github.com/Lab-PANbin/QuantileGS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T07:40:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Lab-PANbin/QuantileGS

### [NicolasDrum/splat-repair](https://github.com/NicolasDrum/splat-repair)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T21:46:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Editor for Gaussian splats with a repair brush: paint over what should go and the surface is rebuilt.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NicolasDrum/splat-repair

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T00:57:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 📚这个仓库是在arxiv上收集的有关VLN，VLA，World Model，SLAM，Gaussian Splatting,非线性优化等相关论文。每天都会自动更新！issue区域是最新10篇论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/luohongk/Embodied-AI-Daily

### [rsasaki0109/visloc-rs](https://github.com/rsasaki0109/visloc-rs)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:54:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, MVS, visual-inertial SLAM, 3D Gaussian Splatting and map-based localization in Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:18:25Z
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
- **发布时间/更新时间：** 2026-11-17T05:26:47Z
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
- **发布时间/更新时间：** 2026-11-17T05:06:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [YuebyYue/UltraVoxelGS-camera-ready](https://github.com/YuebyYue/UltraVoxelGS-camera-ready)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:38:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction. Code coming soon.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/YuebyYue/UltraVoxelGS-camera-ready

### [Kishore-suthersingh/3dgs-digital-twin](https://github.com/Kishore-suthersingh/3dgs-digital-twin)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:24:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Phone video -> COLMAP -> 3D Gaussian Splatting -> cleaned, web-viewable digital twin. Built on free Colab GPUs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kishore-suthersingh/3dgs-digital-twin

### [khanhhuyen-ops/3dgs-reconstruction](https://github.com/khanhhuyen-ops/3dgs-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T07:47:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/khanhhuyen-ops/3dgs-reconstruction

### [IK-Lv7/ShadowSplat](https://github.com/IK-Lv7/ShadowSplat)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T07:38:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Automated data loop for autonomous driving: edge OOD detection → CloudKit sync → 3D Gaussian Splatting reconstruction (OmniRe) → SegFormer fine-tuning → evaluation in CARLA and on real adverse-condition images.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IK-Lv7/ShadowSplat

### [Seanwilliam2077/phocoscan](https://github.com/Seanwilliam2077/phocoscan)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:22:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** phocoscan — iOS scanning and 3DGS reconstruction, with Android collaboration handoff
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Seanwilliam2077/phocoscan

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T03:04:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Khriis-K/kibo-splat](https://github.com/Khriis-K/kibo-splat)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T01:48:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian splat of ISS Kibo from NASA Astrobee footage: NASA ground-truth poses vs COLMAP
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Khriis-K/kibo-splat

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T10:56:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [zongwave/zongwave.github.io](https://github.com/zongwave/zongwave.github.io)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T10:36:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zong Wei - personal & 3D reconstruction projects (VGGT / 3DGS / NeRF)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zongwave/zongwave.github.io

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:53:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/GaussianSplattingWorkbench

### [xuannamservice-ui/Semantic-Aware](https://github.com/xuannamservice-ui/Semantic-Aware)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:31:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible pipeline and simulation data for Semantic-Aware Generative Error Concealment for Resilient Real-Time 3DGS over Turbulent FSO Backhaul
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xuannamservice-ui/Semantic-Aware

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T02:15:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source web graphics engine built on WebGPU and WebGL2
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:20:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [AndriiShramko/ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:32:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:58:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WHIK Studio: free node-based compositing and 3D for Windows and Linux. Keying, roto, tracking, 3D Gaussian splats (3DGS), 3D rendering, AI nodes on your own PC, live link with Maya, Blender and Unreal. Manual in Korean, English, Japanese and Chinese at whik.co.kr/manual.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/suin-park/Whik

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T20:59:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [alois-rive/rive_pixelart_gaussian_splat](https://github.com/alois-rive/rive_pixelart_gaussian_splat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T23:22:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An example of how to render pixel-art gaussian splat with Rive.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/alois-rive/rive_pixelart_gaussian_splat

### [vpx-ecnu/DReSG-website](https://github.com/vpx-ecnu/DReSG-website)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T06:44:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official project page for “DReSG: Diffusion Residuals for Stylized Gaussian Splatting” (Pacific Graphics 2026).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vpx-ecnu/DReSG-website

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T17:41:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T08:52:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [takago/EzRender](https://github.com/takago/EzRender)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:01:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Headless 3D model renderer for .glb / .obj files. Render still images from custom viewpoints via CLI.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/takago/EzRender

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:35:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VR/desktop player for openftgs models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs-xr

### [tardis7732/google-streetview-gaussian](https://github.com/tardis7732/google-streetview-gaussian)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:41:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Google Street View to Gaussian Splatting: month filtering, ground repair, panorama extraction and paired PNG capture
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tardis7732/google-streetview-gaussian

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T02:18:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Yunianan163/AncientBridge-Immersive-Scenes](https://github.com/Yunianan163/AncientBridge-Immersive-Scenes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T10:04:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 古桥数字场景 · 苏州双桥 / 贵州葛镜桥 / 文创共创体验 —— WebGL 与 3DGS 重建驱动的沉浸式数字展陈
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Yunianan163/AncientBridge-Immersive-Scenes

### [alexwang0529/gaussian-splatting-rtx5060](https://github.com/alexwang0529/gaussian-splatting-rtx5060)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:28:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting on Windows with RTX 5060 Laptop and CUDA 12.8. 中文配置教程、完整源码与训练辅助脚本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/alexwang0529/gaussian-splatting-rtx5060

### [lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11](https://github.com/lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:40:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 广工硕士中期检查全量材料：《动态环境下视觉语言模型辅助三维高斯语义建图与机器人目标导航》——26页答辩PPT(全页演讲者备注)+22页开题PPT+三件套表单+三端GPU实验(19次训练/可复跑/原始json)+近一年100篇文献能力矩阵差异分析
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T09:19:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official LichtFeld Studio Blender Plugin
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [yang498-Peter/cloudstudio-3dgs](https://github.com/yang498-Peter/cloudstudio-3dgs)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T10:25:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source 3D Gaussian Splatting pipeline for MVP S1 scan data
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yang498-Peter/cloudstudio-3dgs

### [Undo MultiOp's ops in reverse order (#1109)](https://github.com/playcanvas/supersplat/commit/f29e2b4a34ecee6e4e4886630d653324c5b07add)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-16T09:28:06Z
- **更新判定：** 代码实质更新
- **核心内容：** Undo MultiOp's ops in reverse order (#1109)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [lukehollis/sphr](https://github.com/lukehollis/sphr)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T23:21:14Z
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
- **发布时间/更新时间：** 2026-11-17T08:49:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [vpx-ecnu/DReSG](https://github.com/vpx-ecnu/DReSG)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T06:44:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [PG 2026] Official implementation of DReSG: Diffusion Residuals for Stylized Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vpx-ecnu/DReSG

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:05:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** OpenUSD file format and schema plugins for 3D Gaussian Splatting assets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/usd-3dgs-plugins

### [YueqiWeng/MoE-GS-main](https://github.com/YueqiWeng/MoE-GS-main)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T04:44:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a repo from a publication. It will be used for 3d gaussian splatting with GNN application.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/YueqiWeng/MoE-GS-main

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T09:49:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [xianMuuu/ExplorerGlobal](https://github.com/xianMuuu/ExplorerGlobal)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T08:51:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 探索全球 · ExplorerGlobal —— 国内可用的谷歌地球式三维数字地球（本地零依赖，双击启动）。以 3D 高斯建筑（3DGS）众包为核心愿景。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xianMuuu/ExplorerGlobal

### [VoroneTZ/DoriftoSamurai](https://github.com/VoroneTZ/DoriftoSamurai)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T05:57:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Racing Game based on Dorifto Samirai vk.com community
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/VoroneTZ/DoriftoSamurai

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T20:40:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [5undura/3DGS](https://github.com/5undura/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T16:33:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/5undura/3DGS

### [aktnk/splat-tour](https://github.com/aktnk/splat-tour)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T16:25:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** We can move freely within the 3DGS space, and freely place and display information within it.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aktnk/splat-tour

### [EurekaLi/3DGS](https://github.com/EurekaLi/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-16T10:56:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS研究
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/EurekaLi/3DGS

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 3 |
| GitHub | ok: 60 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 1 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 3/3 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

