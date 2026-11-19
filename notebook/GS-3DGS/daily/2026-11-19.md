---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-18T09:35:19Z
window_end_utc: 2026-11-19T09:42:41Z
generated_at_utc: 2026-11-19T09:42:41Z
item_count: 69
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-19

**统计窗口：** 2026-11-18T09:35:19Z — 2026-11-19T09:42:41Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **69** 项去重后的有效线索：真正新增论文 **2** 项、实质论文修订 **2** 项、代码/版本/项目更新 **65** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [RAPID: Reconstruction Accelerated by Polarization-Informed Depth for 2D Gaussian Splatting](https://arxiv.org/abs/2611.24404v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [Multi-Band Galaxy Novel-View Synthesis with Radiative Gaussian Fields](https://arxiv.org/abs/2611.24723v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690v2) | 实质修订 | arXiv | R2/E0 | P1 |
| 4 | [Spectral World Renderer: Unified 3D Hyperspectral Unmixing](https://arxiv.org/abs/2610.19520v2) | 实质修订 | arXiv | R2/E0 | P1 |
| 5 | [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [RAPID: Reconstruction Accelerated by Polarization-Informed Depth for 2D Gaussian Splatting](https://arxiv.org/abs/2611.24404v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-18T13:35:43Z
- **更新判定：** 真正新增
- **核心内容：** Efficient and accurate 3D surface reconstruction from multi-view images remains a fundamental challenge in Gaussian splatting. Many existing methods rely on sparse geometric initialization and iterative densification, resulting in substantial optimization overhead and difficulties in balancing rendering quality and geometric accuracy, particularly in reflective and weakly textured regions. To address these limitations, we propose RAPID, a geometry-first framework that uses multiview polarization cues to recover dense surface priors. We integrate surface normals into depth maps using sparse geometric anchors. These depth maps are then fused across views. Curvature-adaptive sampling and oriented Gaussian initialization then support efficient optimization. Experiments on the PISR dataset demonstrate an approximately \(5\times\) speedup over PhyGaP, which is a state-of-the-art Gaussian-based reconstruction method. RAPID reduces the average optimization time from approximately 21 minutes (…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.24404v1

### [Multi-Band Galaxy Novel-View Synthesis with Radiative Gaussian Fields](https://arxiv.org/abs/2611.24723v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-18T16:41:49Z
- **更新判定：** 真正新增
- **核心内容：** We propose a novel view synthesis tool for galaxies based on Gaussian Splatting (GS). Unlike RGB data, where GS has achieved success, galaxy observations consist of multi-band signals from a massive number of bodies, contain complex patterns of cross-band interactions, and capture light propagation in highly heterogeneous media. As a result, the underlying physical process poses great challenges in model representation and optimization, which have not been investigated in existing research. To this end, we propose a physically inspired Gaussian Splatting method, GalaxyGS, which is equipped with physically meaningful components that capture both the energy emission mechanism of different astronomical bodies and the light propagation between them. In the absence of directly comparable baseline methods, we adopt a wide range of possible alternative approaches. Comparisons conclusively demonstrate that GalaxyGS is better in accuracy and physical fidelity across datasets and metrics.
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.24723v1

### [Spectral World Renderer: Unified 3D Hyperspectral Unmixing](https://arxiv.org/abs/2610.19520v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-18T12:43:10Z
- **更新判定：** 实质修订
- **核心内容：** Hyperspectral images (HSI) preserve material evidence lost in RGB, yet 3D material identification from multi-view HSI faces two obstacles. Spectral Gaussian splatting reconstructs spectra accurately but leaves unmixing to per-pixel post-processing, while multi-view hyperspectral capture is costly and real datasets lack pixel-level material labels and sub-pixel proportions. We propose Spectral World Renderer (SWR), a material-aware explicit representation that unifies 3D spectral reconstruction and unmixing: it fits a Gaussian scaffold from RGB and decodes ray-Gaussian intersections into abundances over a shared endmember dictionary. Additionally, appearance guidance prevents spectrally similar materials from merging when intensity absorbs their brightness differences. Moreover, SWR requires no material-label supervision during training. To address the data gap, we further construct the SWR Benchmark (SWR-Bench): a coding-agent pipeline generates eight indoor and outdoor worlds from me…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.19520v2

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:21:02Z
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
- **发布时间/更新时间：** 2026-11-19T01:07:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [unclearness/cross3dgs](https://github.com/unclearness/cross3dgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T15:37:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross3DGS: Unified Vulkan-Based 3D Gaussian Splatting Training from Workstations to Mobile Devices (WACV 2027 Workshop EOF)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/unclearness/cross3dgs

### [Benevision/SplatWork](https://github.com/Benevision/SplatWork)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T14:41:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Make, train, view and edit 3D Gaussian splats on your own Mac, iPhone and Linux GPU machines — native Metal trainer and renderer, CUDA worker, multi-device block training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Benevision/SplatWork

### [asdfut/eb-floor2-gaussian-splatting](https://github.com/asdfut/eb-floor2-gaussian-splatting)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:23:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Whole-floor 3D Gaussian Splatting of building EB floor 2 from a mobile robot: FAST-LIO2 (Livox Mid-360) primary odometry, T265 auxiliary, ZED2 images, gsplat MCMC
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asdfut/eb-floor2-gaussian-splatting

### [thaianh20021/fisheye-fusion-lab](https://github.com/thaianh20021/fisheye-fusion-lab)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:22:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pinhole and multi-camera fisheye fusion with LiDAR-assisted 3D Gaussian Splatting and KITTI-360 Colab training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thaianh20021/fisheye-fusion-lab

### [KuoFengYuan/prior-pose-refine](https://github.com/KuoFengYuan/prior-pose-refine)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:02:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Refine prior camera poses, focal length and lens distortion with COLMAP, and prepare a metric 3DGS training dataset.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KuoFengYuan/prior-pose-refine

### [lemonbaby2/3dgs-gaussian-splatting-pipeline](https://github.com/lemonbaby2/3dgs-gaussian-splatting-pipeline)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T04:50:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting pipeline on WSL2 + RTX 50 series (sm_120): data prep, training, long-video rendering
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lemonbaby2/3dgs-gaussian-splatting-pipeline

### [ahpxna/HackPrinceton](https://github.com/ahpxna/HackPrinceton)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T04:17:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** HackPrinceton sunlight analysis, buyer assistant, and trained Gaussian splat walkthroughs
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ahpxna/HackPrinceton

### [caiyuanhao1998/HDR-GS](https://github.com/caiyuanhao1998/HDR-GS)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T03:23:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** "HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting" (NeurIPS 2024)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/HDR-GS

### [ShanghaiTech-IMPACT/4DRGS](https://github.com/ShanghaiTech-IMPACT/4DRGS)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T05:29:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [IPMI 2025 Oral] 4DRGS: 4D Radiative Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ShanghaiTech-IMPACT/4DRGS

### [JingyuanGao0919/Temporal-PhysIR-Splat](https://github.com/JingyuanGao0919/Temporal-PhysIR-Splat)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T02:33:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Temporal PhysIR-Splat: temporal thermal infrared Gaussian splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JingyuanGao0919/Temporal-PhysIR-Splat

### [AtlantixJJ/ARG-Avatar](https://github.com/AtlantixJJ/ARG-Avatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T01:11:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The code release of the ARG-Avatar paper.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AtlantixJJ/ARG-Avatar

### [musubi-interactive/Musubi-Motion](https://github.com/musubi-interactive/Musubi-Motion)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:59:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Browser-based Gaussian splat animation engine and editor built with Three.js and Spark. Maya-style controls, a customizable monochrome workspace, and portable .msb scenes.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/musubi-interactive/Musubi-Motion

### [Viiitoo/endomorph-gs](https://github.com/Viiitoo/endomorph-gs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T00:41:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Deformable Gaussian Splatting for Dynamic Endoscopic Scene Reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Viiitoo/endomorph-gs

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T06:24:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG, RAD and LCC2.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T06:02:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a 3DGS(3D Gaussian Splatting) viewer built on Three.js, with features for marking, measurements, preset-lod rendering, etc.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reall3d-com/Reall3dViewer

### [Skip tree chunking in case 0 valid splats remain, also exclude lodSplats with 0 splats in driveLod (#502)](https://github.com/sparkjsdev/spark/commit/1ac5112924ad3875011d08c39c4159c0e4676423)

- **主题：** 压缩与轻量化
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-18T17:58:46Z
- **更新判定：** 代码实质更新
- **核心内容：** Skip tree chunking in case 0 valid splats remain, also exclude lodSplats with 0 splats in driveLod (#502)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [jo-chemla/3dtiled-to-3dtiles](https://github.com/jo-chemla/3dtiled-to-3dtiles)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:33:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [vinayak-vc/UEPointForge](https://github.com/vinayak-vc/UEPointForge)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:56:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Unreal Engine 5.5 plugin for real-time 3D Gaussian Splatting and large-scale Point Cloud visualization, featuring GPU-accelerated rendering, Octree-based streaming, and Level of Detail (LOD) management.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vinayak-vc/UEPointForge

### [RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690v2)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-18T15:38:54Z
- **更新判定：** 实质修订
- **核心内容：** We present RPC-GS, the first Gaussian Splatting framework for satellite imagery that operates natively with Rational Polynomial Camera (RPC) models. The RPC model is the de facto standard for representing the complex imaging geometry of modern pushbroom satellite sensors. To simplify rendering, prior satellite Gaussian Splatting methods replace the RPC model with perspective or affine camera approximations, leading to geometric errors during reconstruction. RPC-GS avoids these approximations by projecting Gaussian means and covariances directly through the RPC model during the splatting process. We embed the RPC model in a chain of carefully selected geo-coordinate transformations representing a mapping from splatting-suitable scene coordinates to image coordinates. To map the Gaussian covariance matrices, we derive a numerically robust Jacobian-based covariance projection for the (partially nonlinear) coordinate transformations. Since RPCs lack an explicit notion of camera depth, we…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.06690v2

### [timfennell/vintage-click](https://github.com/timfennell/vintage-click)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T05:11:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 1970s 35 mm SLR photography game inside 3D Gaussian splat scans, for Apple silicon Macs. Lens optics made by the renderer, film stocks, tungsten lighting, a light table and loupe.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timfennell/vintage-click

### [danchar12138/scan3d-windows](https://github.com/danchar12138/scan3d-windows)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:09:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photos or phone video to Gaussian splat + textured mesh + collision mesh. Windows-native, one-click, web UI, runs locally (Spirula Studio + COLMAP).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/danchar12138/scan3d-windows

### [Joserin1991/UNSEEN](https://github.com/Joserin1991/UNSEEN)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:04:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** UNSEEN · 未见之境 — belief-map exploration under partial spatial information, plus 3DGS→voxel geometry experiments
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Joserin1991/UNSEEN

### [letmeshock-uae/street-wheel-v1](https://github.com/letmeshock-uae/street-wheel-v1)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:01:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS street rolled into a wheel — first version, no text, short seam
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/letmeshock-uae/street-wheel-v1

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T05:31:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A comprehensive list of Implicit Representations, NeRF and 3D Gaussian Splatting papers relating to SLAM/Robotics domain, including papers, videos, codes, and related websites
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM

### [rsasaki0109/visloc-rs](https://github.com/rsasaki0109/visloc-rs)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:40:55Z
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
- **发布时间/更新时间：** 2026-11-19T07:55:05Z
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
- **发布时间/更新时间：** 2026-11-18T17:59:53Z
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
- **发布时间/更新时间：** 2026-11-19T04:45:02Z
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
- **发布时间/更新时间：** 2026-11-19T04:14:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [Cenvoil/semantic-railgauss-slam](https://github.com/Cenvoil/semantic-railgauss-slam)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:24:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Rail-specific semantic Gaussian-splatting SLAM on OSDaR23
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cenvoil/semantic-railgauss-slam

### [Kishore-suthersingh/3dgs-digital-twin](https://github.com/Kishore-suthersingh/3dgs-digital-twin)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T07:53:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Phone video -> COLMAP -> 3D Gaussian Splatting -> cleaned, web-viewable digital twin. Built on free Colab GPUs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kishore-suthersingh/3dgs-digital-twin

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T03:21:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Farida-gaber44/sparse-view-3dgs-ablation](https://github.com/Farida-gaber44/sparse-view-3dgs-ablation)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T17:16:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Farida-gaber44/sparse-view-3dgs-ablation

### [jinshuming/canvas-3d-director](https://github.com/jinshuming/canvas-3d-director)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T04:00:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D director (World) on Viggle assets, with a natural-language agent and a text/picture to 3DGS scene generator
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jinshuming/canvas-3d-director

### [xuannamservice-ui/Semantic-Aware](https://github.com/xuannamservice-ui/Semantic-Aware)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T19:02:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible pipeline and simulation data for Semantic-Aware Generative Error Concealment for Resilient Real-Time 3DGS over Turbulent FSO Backhaul
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xuannamservice-ui/Semantic-Aware

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T02:53:29Z
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
- **发布时间/更新时间：** 2026-11-19T02:14:32Z
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
- **发布时间/更新时间：** 2026-11-19T02:56:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@eb536c491c5b31af0adb2c2dd71de62797c23c6c/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/233e6b2fe74f63f5105e89af2a94355b28e49724)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-18T18:01:23Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@eb536c491c5b31af0adb2c2dd71de62797c23c6c/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Compute rows for ordering array based on numSplats (#503)](https://github.com/sparkjsdev/spark/commit/929d77b5217fe4d527f54d5402748e00c1d3de90)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-18T17:59:11Z
- **更新判定：** 代码实质更新
- **核心内容：** Compute rows for ordering array based on numSplats (#503)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [kallr/osg_3dgs](https://github.com/kallr/osg_3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T06:18:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting osg qt viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kallr/osg_3dgs

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T20:36:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T00:14:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:23:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [mrnetwork0001/Holorra](https://github.com/mrnetwork0001/Holorra)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T08:46:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Browser studio that turns generated 3D into playable, directed scenes: Gaussian Splatting worlds, Lux3D part split, articulation and auto-rigged actors, built on the Manycore Aholo SDKs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mrnetwork0001/Holorra

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T07:45:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [ldphu1/3dgs-low-vram](https://github.com/ldphu1/3dgs-low-vram)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T02:08:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ldphu1/3dgs-low-vram

### [LSUDOKO/ReRoom](https://github.com/LSUDOKO/ReRoom)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T20:41:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Scan it. Remix it. Live in it. Redesign your real room in 3D with AI furniture that opens, built on Aholo World, Lux3D and the Aholo Viewer.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LSUDOKO/ReRoom

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:41:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official LichtFeld Studio Blender Plugin
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/eb536c491c5b31af0adb2c2dd71de62797c23c6c)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-18T18:01:23Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T02:39:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [MapMindAI/EasyGaussianSplatting](https://github.com/MapMindAI/EasyGaussianSplatting)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T07:43:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** From insta360/DJI to Gaussian Splatting Easy and Direct
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MapMindAI/EasyGaussianSplatting

### [Suzukeh/3DGS_Su](https://github.com/Suzukeh/3DGS_Su)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T21:02:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** AviUtl2 で 3DGS（3D Gaussian Splatting）の PLY / SOG をカメラ同期で表示するスクリプトと変換プラグイン
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Suzukeh/3DGS_Su

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T16:55:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** OpenUSD file format and schema plugins for 3D Gaussian Splatting assets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/usd-3dgs-plugins

### [songconmaisaix31-design/lux3D-engine](https://github.com/songconmaisaix31-design/lux3D-engine)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T09:33:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** AI-native 3D world runtime: 11-layer Rust engine + a deterministic embodied bench (CPU, spec_hash + per-episode fingerprints). 17 browser demos, Apache-2.0.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/songconmaisaix31-design/lux3D-engine

### [satyaba/SGDC-3DGS](https://github.com/satyaba/SGDC-3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T07:08:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/satyaba/SGDC-3DGS

### [W-nnnn/3DGS-test](https://github.com/W-nnnn/3DGS-test)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T07:02:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/W-nnnn/3DGS-test

### [LINYEANSHU/splat2blender](https://github.com/LINYEANSHU/splat2blender)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T05:01:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photo to 3DGS to Blender pipeline scripts | 实拍转 3D 高斯泼溅导入 Blender 工具链
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LINYEANSHU/splat2blender

### [MauroNico/gaussian_splat](https://github.com/MauroNico/gaussian_splat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T04:36:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Dioramas 3D interactivos con estetica Gaussian Splatting (250,000 splats, Three.js, Radix Sort)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MauroNico/gaussian_splat

### [AbelWang324/3dgs-](https://github.com/AbelWang324/3dgs-)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T02:34:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 三维重建demo，支持图片集和视频的高斯重建
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AbelWang324/3dgs-

### [in33/SpaceBrowser](https://github.com/in33/SpaceBrowser)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T01:57:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空间浏览器 SpaceBrowser.cn — 基于 Aholo 空间智能 API，用一句话或一组照片生成可漫游的高保真 3D 空间（3DGS / Lux3X）。纯 HTML+JS+CSS，浏览器即用。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/in33/SpaceBrowser

### [Zhao-hongxuan/campus-3dgs](https://github.com/Zhao-hongxuan/campus-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T21:58:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Zhao-hongxuan/campus-3dgs

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T19:03:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [Jing0505/suying-3dgs](https://github.com/Jing0505/suying-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T16:09:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Jing0505/suying-3dgs

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 4 |
| GitHub | ok: 65 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 4/4 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

