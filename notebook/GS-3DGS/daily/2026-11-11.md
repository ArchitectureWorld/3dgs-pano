---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-10T09:02:02Z
window_end_utc: 2026-11-11T08:42:03Z
generated_at_utc: 2026-11-11T08:42:03Z
item_count: 65
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-11

**统计窗口：** 2026-11-10T09:02:02Z — 2026-11-11T08:42:03Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **65** 项去重后的有效线索：真正新增论文 **4** 项、实质论文修订 **1** 项、代码/版本/项目更新 **59** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Marrying Capacity and Precision for Efficient 2D Gaussian Image Representation](https://arxiv.org/abs/2611.13784v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors](https://arxiv.org/abs/2611.13772v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation](https://arxiv.org/abs/2611.13808v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [Where do we Jam? - The Impact of Real and Virtual XR Spaces on Musical Creativity, Co-Presence, Affect, and Flow](https://arxiv.org/abs/2611.14029v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [SplatLab: Autonomous Scientific Discovery for 3DGS Research](https://arxiv.org/abs/2610.30468v3) | 实质修订 | arXiv | R2/E0 | P1 |

## 分类详述

### [Marrying Capacity and Precision for Efficient 2D Gaussian Image Representation](https://arxiv.org/abs/2611.13784v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-10T09:21:35Z
- **更新判定：** 真正新增
- **核心内容：** 2D Gaussian representations provide an explicit and efficient way to represent images, but their rate-distortion performance under limited budgets depends critically on how Gaussian capacity and parameter precision are allocated. Existing methods typically optimize these two resources separately, overlooking content-dependent capacity demands and heterogeneous quantization sensitivity. We present CP-GS, a capacity-precision coupled Gaussian splatting framework for budget-aware 2D Gaussian image representation that jointly optimizes capacity allocation and attribute precision under a shared rate constraint. CP-GS first constructs a content-adaptive Gaussian representation by dynamically reallocating a fixed Gaussian budget from redundant regions to areas with higher representation demand. It then introduces hierarchical distortion-aware representation quantization, using efficient rendering-based calibration to allocate precision across Gaussian attributes and further refine it within…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.13784v1

### [RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors](https://arxiv.org/abs/2611.13772v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-10T09:11:01Z
- **更新判定：** 真正新增
- **核心内容：** 3D reflection removal is crucial in applications demanding high-fidelity visualization, such as museum exhibitions. In this work, we propose Reflection-Free 3D Gaussian Splatting (RF3DGS), a novel method for superior reflection removal. RF3DGS exclusively leverages a widely-adopted photometric prior for reflection removal: that the minimum pixel intensity across multi-view images corresponding to the same 3D point strongly correlates with reflection-free information. However, generalizing this principle to a 3D Gaussian Splatting within a multi-view context is non-trivial. To address this, RF3DGS first optimizes a vanilla 3DGS model using a geometric prior to estimate a coarse, reflection-free depth map for each view. Leveraging these depth maps and photometric prior, a 3D warping process aggregates reflection-free information from auxiliary views to construct a clean transmission pseudo-label for a given reference view. This pseudo-label provides a robust self-supervised signal for o…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.13772v1

### [FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation](https://arxiv.org/abs/2611.13808v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-10T09:39:33Z
- **更新判定：** 真正新增
- **核心内容：** Internet photos of a scene differ in exposure, illumination and transient objects such as passers-by, so one set of Gaussian colours cannot explain all photos (the in-the-wild setting). Recent in-the-wild Gaussian Splatting methods mostly report hours of per-scene optimization. We present FastWild-GS, which describes each photo by a 128-dimensional Photo Appearance Token and a per-channel transform, a scale and an offset applied to the rendered image (six parameters); a small MLP predicts the colour of each Gaussian from this token and a per-Gaussian feature, replacing the spherical-harmonics colour. The same transform is applied to the renders that score Gaussians for densification and pruning, so appearance differences between photos are not counted as reconstruction error. On PhotoTourism, FastWild-GS trains in 8.8 minutes per scene with the lowest LPIPS among the compared methods, 23x faster than AsymGS, the next best in LPIPS. On NeRF-OSR, it has the best average PSNR, SSIM and L…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.13808v1

### [Where do we Jam? - The Impact of Real and Virtual XR Spaces on Musical Creativity, Co-Presence, Affect, and Flow](https://arxiv.org/abs/2611.14029v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-10T12:59:19Z
- **更新判定：** 真正新增
- **核心内容：** Extended Reality (XR) technologies can place musicians in virtual, mixed, or real environments during networked music performance (NMP). To examine how NMP applications in XR should be positioned on the reality-virtuality continuum, we conducted a laboratory study (N = 28) comparing a simulated NMP experience in Virtual Reality (VR) with one in Augmented Reality (AR). In both conditions, musicians saw their remote partners in real time as 3D point clouds rendered with an optimized Gaussian Splatting shader. While VR allowed participants to select and customize fully virtual 3D environments, AR showed a pass-through view of the laboratory environment. We measured creativity support, flow, involvement, co-presence, and affect, and complemented these data with qualitative interviews on participants' preferences and requirements for creative environments. Our results show that participants felt significantly more involved by the immersive XR experience in VR than in AR. Positive affect, f…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.14029v1

### [SplatLab: Autonomous Scientific Discovery for 3DGS Research](https://arxiv.org/abs/2610.30468v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-10T12:24:58Z
- **更新判定：** 实质修订
- **核心内容：** Scientific discovery requires more than generating hypotheses: ideas must be grounded in prior work, translated into executable methods, experimentally validated, challenged by counterevidence, and communicated through reproducible findings. Despite recent advances in autonomous research agents, closing this entire loop remains challenging in rapidly evolving computer-vision fields with complex training pipelines and expensive evaluations. We introduce SplatLab, an autonomous scientific discovery system for 3D Gaussian Splatting (3DGS) that integrates literature understanding, hypothesis generation, implementation, experimental refinement, falsification, and manuscript writing into a unified research pipeline. Given a research prompt, a target-paper URL, or no input at all, SplatLab identifies research opportunities, proposes novel methods, trains and ablates candidates across Mip-NeRF 360 and LLFF, and produces manuscripts grounded in verifiable experimental evidence. Unlike prior sy…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.30468v3

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:50:04Z
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
- **发布时间/更新时间：** 2026-11-11T05:27:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:11:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [pouyasam1996/gaussian-slam](https://github.com/pouyasam1996/gaussian-slam)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T01:49:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SLAM with 3D Gaussian Splatting for training
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pouyasam1996/gaussian-slam

### [Mouad-Ze/3dgs-motion-analysis](https://github.com/Mouad-Ze/3dgs-motion-analysis)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T14:48:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mouad-Ze/3dgs-motion-analysis

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T08:29:59Z
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
- **发布时间/更新时间：** 2026-11-11T06:34:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [ZehuiWU2009/sgdc-objectgs](https://github.com/ZehuiWU2009/sgdc-objectgs)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:27:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official code for "Semantic-Guided Density Control for Compact Semantic 3D Gaussian Splatting" (Computers & Graphics), anchor-based instantiation on ObjectGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZehuiWU2009/sgdc-objectgs

### [sebastianobecchetti/bek](https://github.com/sebastianobecchetti/bek)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T12:43:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** BEK codec for 3DGS models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sebastianobecchetti/bek

### [Khriis-K/Fidelis](https://github.com/Khriis-K/Fidelis)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T08:03:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Multifidelity Reliability Estimation for Vision-Based Planetary Navigation: estimating the probability of navigation failure during simulated Martian descent using Gaussian splatting and uncertainty quantification.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Khriis-K/Fidelis

### [zju3dv/SplatAnything](https://github.com/zju3dv/SplatAnything)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T12:06:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SplatAnything: Gaussian Spacing Normalization for Feed-Forward 3DGS across Arbitrary Scenes
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zju3dv/SplatAnything

### [fenghuayumo/photara-studio](https://github.com/fenghuayumo/photara-studio)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T02:27:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** a powerful and efficient 3d spatial capture tool , video/image to splat to mesh ,cross-vendor, Vulkan or CUDA
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fenghuayumo/photara-studio

### [4321ba/GodotGaussianSplattingNodes](https://github.com/4321ba/GodotGaussianSplattingNodes)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T22:01:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Allows developers to use gaussian splatting objects as they would use a regular mesh + mesh instance.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/4321ba/GodotGaussianSplattingNodes

### [Jaykumaran/MeshSfM-SplatStudio](https://github.com/Jaykumaran/MeshSfM-SplatStudio)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T04:00:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MeshSfM SplatStudio: A mesh editor with Gaussian splat coexistence: generate, edit, align, annotate and drive road meshes and splats in the browser.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Jaykumaran/MeshSfM-SplatStudio

### [M-stars/Splat2Play](https://github.com/M-stars/Splat2Play)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T21:09:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 扫描现实,即刻可玩——把真实世界的 3DGS 扫描变成 Unity 里可玩的关卡:碰撞代理生成、NavMesh 桥接、近似动态光照、分块流送。(实境入戏 Splat2Play)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/M-stars/Splat2Play

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T05:52:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A comprehensive list of Implicit Representations, NeRF and 3D Gaussian Splatting papers relating to SLAM/Robotics domain, including papers, videos, codes, and related websites
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM

### [caiyuanhao1998/Open-DiffusionGS](https://github.com/caiyuanhao1998/Open-DiffusionGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T00:17:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction (ICCV 2025)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/Open-DiffusionGS

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:29:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [zdwww/Wheat-3DGS](https://github.com/zdwww/Wheat-3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T17:12:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zdwww/Wheat-3DGS

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T08:31:05Z
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
- **发布时间/更新时间：** 2026-11-11T02:50:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T03:13:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Oasis-spaces/OasisSpaces](https://github.com/Oasis-spaces/OasisSpaces)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T23:00:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Film a room, get an editable 3D model and a Gaussian splat: COLMAP + MoGe-2 + SAM 2.1 + Blender + OpenSplat, checked stage by stage by Claude
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Oasis-spaces/OasisSpaces

### [Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING](https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T16:37:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T05:53:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WHIK Studio: free node-based video compositing for Windows, with 3D Gaussian splat (3DGS) editing. Manual in Korean, English, Japanese and Chinese at whik.co.kr/manual. Preview, updated weekly.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/suin-park/Whik

### [Saqoosha/SplatShell](https://github.com/Saqoosha/SplatShell)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T05:34:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native macOS app for viewing and editing huge 3D Gaussian Splatting scenes, built around SuperSplat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Saqoosha/SplatShell

### [satyaba/gaussian-splatting](https://github.com/satyaba/gaussian-splatting)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T10:26:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SGDense-3DGS: segmentation-guided density control of 3D Gaussian Splatting (thesis work)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/satyaba/gaussian-splatting

### [Add render_view, layer instancing and generator layers to WebMCP (#1095)](https://github.com/playcanvas/supersplat/commit/89fb456f76f24961c5d99affcc6baedf56be40ba)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-10T10:51:23Z
- **更新判定：** 代码实质更新
- **核心内容：** Add render_view, layer instancing and generator layers to WebMCP (#1095)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Kiri-Innovation/3dgs-render-blender-addon](https://github.com/Kiri-Innovation/3dgs-render-blender-addon)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:42:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Render by KIRI Engine
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kiri-Innovation/3dgs-render-blender-addon

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:39:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high performance 3DGS renderer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-viewer

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T02:13:34Z
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
- **发布时间/更新时间：** 2026-11-10T22:12:12Z
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
- **发布时间/更新时间：** 2026-11-11T01:43:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Log-spaced sort keys and anti-aliased splat rendering (#1097)](https://github.com/playcanvas/supersplat/commit/1522a440c3c0bd0c39cb9c42db3382c191795687)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-10T13:27:13Z
- **更新判定：** 代码实质更新
- **核心内容：** Log-spaced sort keys and anti-aliased splat rendering (#1097)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Harden render_view capture and analysis values (#1096)](https://github.com/playcanvas/supersplat/commit/a51284e95baa83f82fcc0441ee9f366cd802ff3f)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-10T11:16:25Z
- **更新判定：** 代码实质更新
- **核心内容：** Harden render_view capture and analysis values (#1096)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Gatsby0916/OUGS](https://github.com/Gatsby0916/OUGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:21:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official GitHub repository for the EuroGraphics 2026 OUGS paper for 3D Gaussian Splatting, enabling object-aware view selection.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Gatsby0916/OUGS

### [MAdrid1011/SCARF](https://github.com/MAdrid1011/SCARF)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T03:32:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Generalized 3DGS Inference Accerlator
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MAdrid1011/SCARF

### [mateosss/isosplat](https://github.com/mateosss/isosplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T22:32:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Isometric Viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mateosss/isosplat

### [envision-projects/envision-flythrough](https://github.com/envision-projects/envision-flythrough)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T20:54:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photogrammetry / Gaussian splat fly-through of the EnVision Maker Studio (SuperSplat viewer)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/envision-projects/envision-flythrough

### [Artemarius/pocketsplat](https://github.com/Artemarius/pocketsplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T15:33:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Vulkan 1.3 3D Gaussian Splatting viewer for Android phones, measured like-for-like against web and native renderers
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Artemarius/pocketsplat

### [Mohith26/livedirt](https://github.com/Mohith26/livedirt)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T08:03:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A neural job site you can dig into: 3DGS capture + earthwork physics, grade control, simulated lidar/camera, autonomous trenching, MCAP export. Live: livedirt.mohithgajjela.com
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mohith26/livedirt

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:56:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [00DogeCubeGamer00/3dgs-texture-unpack](https://github.com/00DogeCubeGamer00/3dgs-texture-unpack)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T07:20:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Extracts and converts packed textures and sprite sheets from classic 3D Gamestudio (A5/A6) game archives into standard PNG images.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/00DogeCubeGamer00/3dgs-texture-unpack

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T01:41:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VR/desktop player for openftgs models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs-xr

### [shimansKim/sharp-gaussian-splatting-vr-toolkit](https://github.com/shimansKim/sharp-gaussian-splatting-vr-toolkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T00:28:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows toolkit for Apple SHARP Gaussian Splatting, Quest WebXR preview, and YouTube VR video workflows.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shimansKim/sharp-gaussian-splatting-vr-toolkit

### [vsolano9/splat-walk](https://github.com/vsolano9/splat-walk)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T19:30:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native three.js r186 WebGPU Gaussian splat explorer with Next.js, fly controls and raycast hotspots.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vsolano9/splat-walk

### [ellipticalcurves/alhiraoud](https://github.com/ellipticalcurves/alhiraoud)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T18:40:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** al hira oud website with gaussian splatting scroll through
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ellipticalcurves/alhiraoud

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T09:02:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [From Captured Spaces to CG Scenes — The Day Blender 5.3 Handles 3DGS Natively](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af42a66e177458097fcbb174a6abfe3&url=https%3a%2f%2fnote.com%2fa_courtyard%2fn%2fn1a3f1b5b4725%3fhl%3den&c=14474856957915300596&mkt=en-us)

- **主题：** 实时渲染与展示
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-10T18:05:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** On November 10, 2026, version 5.3 of the free 3DCG software Blender was released. This is the first version capable of importing and rendering 3D Gaussian Splatting (3DGS) without the need for ...
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T21:00:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official LichtFeld Studio Blender Plugin
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T16:37:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T02:45:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T10:04:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [Team-Ferrous/unity-3dgs](https://github.com/Team-Ferrous/unity-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T06:05:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** a plugin for using KIRI Engine 3dgs or general PLYs in UnityEngine
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Team-Ferrous/unity-3dgs

### [v-melkov/maf-3dgs-inventory](https://github.com/v-melkov/maf-3dgs-inventory)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-11T02:22:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/v-melkov/maf-3dgs-inventory

### [walidriachy/head-tracked-window](https://github.com/walidriachy/head-tracked-window)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T19:58:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Turn your screen into a window: a head-tracked, off-axis view into a 3D Gaussian splat corridor. One HTML file.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/walidriachy/head-tracked-window

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T18:15:14Z
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
- **发布时间/更新时间：** 2026-11-10T16:48:37Z
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
- **发布时间/更新时间：** 2026-11-10T13:39:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** We can move freely within the 3DGS space, and freely place and display information within it.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aktnk/splat-tour

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T09:53:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 5 |
| GitHub | ok: 59 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 2 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 5/5 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

