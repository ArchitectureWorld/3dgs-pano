---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-25T10:45:09Z
window_end_utc: 2026-11-26T10:17:23Z
generated_at_utc: 2026-11-26T10:17:23Z
item_count: 71
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-26

**统计窗口：** 2026-11-25T10:45:09Z — 2026-11-26T10:17:23Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **71** 项去重后的有效线索：真正新增论文 **6** 项、实质论文修订 **2** 项、代码/版本/项目更新 **62** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models](https://arxiv.org/abs/2611.34223v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References](https://arxiv.org/abs/2611.34932v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T18:59:45Z
- **更新判定：** 真正新增
- **核心内容：** We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels. The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. Although common in real captures, large and fast motion poses a challenge that dynamic Gaussian splatting methods usually overlook. To ac…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34939v1

### [AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models](https://arxiv.org/abs/2611.34223v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T11:47:58Z
- **更新判定：** 真正新增
- **核心内容：** Real cameras are not pinholes, yet most dynamic Gaussian splatting assumes they are. Footage is therefore undistorted first, losing field of view or detail, especially with wide-angle and fisheye cameras. Static Gaussian splatting has largely solved this with ray-based rendering, which suits any camera. Native 4D Gaussians, which model motion in space-time, cannot use it directly: each Gaussian's orientation and size cannot be recovered reliably from its covariance. We present AnyCam4D, which trains native 4D Gaussians on original footage by ray-based rasterization, preserving field of view and resolution at about the per-step cost of standard projection. Our key contribution is a numerically stable way to obtain orientation and size: we condition a square root of the 4D covariance. Trained models render through other cameras, with rolling shutter, depth of field or chromatic aberration. With a synthetic 170-degree fisheye camera, training on original images improves peak signal-to-no…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34223v1

### [WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T17:58:06Z
- **更新判定：** 真正新增
- **核心内容：** Constructing complete 3D worlds from a single panorama is challenging because large portions of the scene remain unobserved. Existing panoramic-video methods expand spatial coverage through dense sequential generation, but neighboring frames contain substantial redundancy, long trajectories accumulate errors, and independently generated directions may be inconsistent. We present WorldExpand, which formulates single-panorama world expansion as the generation of sparse, complementary, and high-resolution panoramic observations. This representation concentrates the generation budget on informative scene regions and preserves the fine-grained details required for 3D construction. WorldExpand addresses two key challenges: where to observe and how to synthesize. Our Coverage-Guided View Selection identifies informative target locations using scene-adaptive quadrants and warp-based coverage scores, while our Joint Panoramic Diffusion uses Gaussian-splatting-based geometric warps to jointly s…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34810v1

### [OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T10:49:40Z
- **更新判定：** 真正新增
- **核心内容：** Recent advances in Gaussian splatting have enabled efficient underwater reconstruction, but sparse observations, light attenuation, and backscatter still leave scene regions underconstrained and cause novel-view artifacts. We present OceanFix, a reference-guided framework for sparse-view underwater 3D reconstruction that combines diffusion-based view repair with Gaussian scene refinement. Our repair model follows a two-stage training strategy that separates underwater appearance adaptation from geometric refinement. The first stage learns underwater appearance from reference observations and estimated medium features. The second uses camera poses and reference depth to align reference features, with relative-depth supervision guiding structural repair without requiring target-view depth at inference. We further propose medium-aware distillation that transfers repaired views into the 3D scene according to geometric repair demand and channel-specific optical observability. Through itera…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34155v1

### [Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T14:43:03Z
- **更新判定：** 真正新增
- **核心内容：** Path-traced rendering shows CT and MR volumes with realistic lighting, but it restarts after every change of view, clipping plane or transfer function (TF), the map from voxel intensity to colour and opacity, which limits the frame rate. Feed-forward Gaussian splatting models such as RenderFM predict the Gaussians directly from the volume instead of fitting them to each scan, and are fast. RenderFM, however, handles only CT, runs its network again after every TF edit, has no clipping operator, and places its Gaussians on a uniform 3-mm grid that blurs organ boundaries and cut faces. We present RenderFM-Next, a feed-forward model that addresses these limits. One network handles both CT and MR. Its Gaussians are predicted once per volume: a new TF needs no pass of this network, and a clipping plane cuts them exactly, using operators from prior work. The model predicts coarse 3-mm Gaussians for the whole volume and refines them to 1.5 mm only where refinement improves the image. A small…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34478v1

### [GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T13:50:27Z
- **更新判定：** 实质修订
- **核心内容：** Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate geometric reconstruction. It performs tracking and mapping in the spherical domain and uses tracked visual features in regions without LiDAR coverage to improve pose estimation. To address insufficient coverage of newly observed surfaces and floating artifacts during incremental mapping, we introduce Depth-Aware Map Extension and Pruning (DAEP). To enable broader evaluation, we collect a new dataset, WHOLE, using a UAV platform across Weak-geometry, High-dynamic, Omnidirectional, Low-light, and Easy scenarios. Extensive experiments on public benchmarks and WHOLE demonstrate competi…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.32335v2

### [Large-Scale Gaussian Splatting with a Multi-GPU PyTorch Backend](https://arxiv.org/abs/2606.11390v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T17:37:02Z
- **更新判定：** 实质修订
- **核心内容：** Gaussian splatting methods have become increasingly popular for neural reconstruction of the real world. However, they are often limited in scale and resolution due to compute and memory constraints. We present a multi-GPU Gaussian splatting approach that scales reconstruction to higher resolutions and larger scenes while abstracting away the code complexity typically associated with distributing a model. We demonstrate city-scale reconstructions with street-level detail consisting of over 1 billion Gaussian splats. To accomplish this, we propose a PyTorch backend that distributes parameters and operators across GPUs via CUDA unified memory, with optional NVLink support. Because distribution occurs at the operator level, the model code requires no explicit cross-device communication. More broadly, the backend exposes multiple GPUs as an aggregate asynchronous PyTorch device and supports a broad set of PyTorch operators enabling the distribution of general PyTorch workloads.
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.11390v2

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T07:41:44Z
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
- **发布时间/更新时间：** 2026-11-26T05:32:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [Lab-of-AI-and-Robotics/LEGO-SLAM](https://github.com/Lab-of-AI-and-Robotics/LEGO-SLAM)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T04:45:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Lab-of-AI-and-Robotics/LEGO-SLAM

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:05:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting in Blender: train 3D Gaussian Splats from your Blender scene with LichtFeld Studio and import splats from the LichtFeld Portal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [MarcelRogge/occlusion-aware-3dgs](https://github.com/MarcelRogge/occlusion-aware-3dgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T16:56:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Occlusion-Aware Densification for 3D Gaussian Splatting (ACCV 2026).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MarcelRogge/occlusion-aware-3dgs

### [MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References](https://arxiv.org/abs/2611.34932v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-25T18:59:23Z
- **更新判定：** 真正新增
- **核心内容：** Robots operating in previously mapped spaces must localize accurately despite moving people and rearranged objects. Most localization pipelines match the query against a sparse set of captured reference images retrieved by appearance, which is brittle under scene change and repeating structures. We present MERLoc, which turns a single metric 3D Gaussian Splatting scan into a dense Functional Reference Memory. Reference views are sampled over the navigable space for the robot's morphology and sensors at a target density and rendered offline. Pre-encoding them for the chosen off-the-shelf localizer removes the reference encoder from inference. A pose-based retrieval strategy then selects references by spatial proximity and viewing direction rather than appearance, sidestepping visual ambiguities whenever a prior exists. Across one classical and four learned localizers in simulated and real dynamic scenes, pose-based retrieval matches or outperforms appearance retrieval in most cases, ev…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.34932v1

### [solipsist-studios/cumuli](https://github.com/solipsist-studios/cumuli)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T18:43:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 4D volumetric human capture pipeline: GoPro footage → Camera pose estimation → Diffuman4D → Brush 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli

### [royorel/MEMO](https://github.com/royorel/MEMO)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T05:09:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MEMO: A Mesh for Every Moment. Dynamic Gaussian splatting with a watertight mesh at every time step.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/royorel/MEMO

### [Vexlc/road-hazard-reconstruction](https://github.com/Vexlc/road-hazard-reconstruction)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T01:49:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible stereo, RGB-D and procedural road-hazard assets with dynamic 3DGS scene insertion and selectable visualizations.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Vexlc/road-hazard-reconstruction

### [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T15:34:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a 3DGS(3D Gaussian Splatting) viewer built on Three.js, with features for marking, measurements, preset-lod rendering, etc.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reall3d-com/Reall3dViewer

### [jo-chemla/3dtiled-to-3dtiles](https://github.com/jo-chemla/3dtiled-to-3dtiles)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T07:18:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [coopersimpson101-debug/splatweb](https://github.com/coopersimpson101-debug/splatweb)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:31:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splatting renderer in WebGPU: EWA projection, GPU radix sort, streaming .ply/.splat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/coopersimpson101-debug/splatweb

### [animu-sphere/hydra-merlin](https://github.com/animu-sphere/hydra-merlin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T16:21:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A lightweight, host-neutral raster renderer for USD Hydra, powered by Vulkan and Metal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/hydra-merlin

### [NicolasDrum/splat-repair](https://github.com/NicolasDrum/splat-repair)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:45:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Editor for Gaussian splats with a repair brush: paint over what should go and the surface is rebuilt.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NicolasDrum/splat-repair

### [zxn2023/GeoPE-GS](https://github.com/zxn2023/GeoPE-GS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T04:46:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for GeoPE-GS: Geometry-Conditioned Pseudo-Enhancement for Low-Light 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zxn2023/GeoPE-GS

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T00:08:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [lightfallpriest/ApolloSplat-Py](https://github.com/lightfallpriest/ApolloSplat-Py)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:54:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting–augmented photogrammetry on Apollo 17 imagery with novel-view synthesis and mesh fidelity analysis.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lightfallpriest/ApolloSplat-Py

### [ZhangAoCanada/3Dviewer](https://github.com/ZhangAoCanada/3Dviewer)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:51:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** just another 3D viewer for popular 3D representations, including 3DGS, mesh, point cloud, ...
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhangAoCanada/3Dviewer

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T07:26:50Z
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
- **发布时间/更新时间：** 2026-11-26T10:12:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, MVS, visual-inertial SLAM, 3D Gaussian Splatting and map-based localization in Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [darshmenon/rosnav](https://github.com/darshmenon/rosnav)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:23:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Full-stack ROS 2 autonomous navigation: Nav2, SLAM Toolbox, RTAB-Map & ORB-SLAM3 VSLAM, Gazebo Harmonic, Docker, multi-robot fleet coordination, collaborative loop closure, coordinated frontier exploration, MPPI controller, behavior trees, waypoint following & Gaussian Splatting capture on Humble/Jazzy.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/darshmenon/rosnav

### [NVIDIA/NuRec](https://github.com/NVIDIA/NuRec)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T17:21:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NVIDIA Omniverse NuRec provides neural reconstruction APIs and libraries to reconstruct and render interactive simulations from real-world data.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NVIDIA/NuRec

### [M4A1TasteGood/ArgsWorld](https://github.com/M4A1TasteGood/ArgsWorld)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:35:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for "ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/M4A1TasteGood/ArgsWorld

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:46:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [ady95/open-reality-view-tutorial](https://github.com/ady95/open-reality-view-tutorial)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:49:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Example code for the WikiDocs book 'Tesla Reality View Follow-along' — open-source 3DGS, feed-forward reconstruction and generative driving video on a single RTX 3090
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ady95/open-reality-view-tutorial

### [song-0608/traceform-project](https://github.com/song-0608/traceform-project)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:52:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** TraceForm — cultural-heritage capture, 3D Gaussian Splatting reconstruction, and versioned digital restoration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/song-0608/traceform-project

### [enhansome/enhansome-NeRF-and-3DGS-SLAM](https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T05:07:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:49:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Reconstruction of UCLA Gateway Plaza from unstaged outdoor scene video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS

### [thaianh20021/drive2sim](https://github.com/thaianh20021/drive2sim)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:49:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** drive2sim: driving-scene reconstruction (3D Gaussian Splatting) with Studio, built on DriveStudio. Install: npx github:thaianh20021/drive2sim
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thaianh20021/drive2sim

### [davdbrns/3dgs-cslam-viewer](https://github.com/davdbrns/3dgs-cslam-viewer)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:03:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/davdbrns/3dgs-cslam-viewer

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:10:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Semantic Guidance Enhances Sparse View Three Dimensional Industrial Reconstruction](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6b08073e9e00446ab079b90d6b6c9312&url=https%3a%2f%2fbioengineer.org%2fsemantic-guidance-enhances-sparse-view-three-dimensional-industrial-reconstruction%2f&c=14349938949878794463&mkt=en-us)

- **主题：** SLAM与重建
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-25T16:00:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** A semantic-guided three-dimensional Gaussian splatting framework combines uncalibrated stereo pose estimation and foundation model segmentation to reconstruct complex industrial environments from ...
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:35:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/GaussianSplattingWorkbench

### [AsakaTigar/dentsplat-web](https://github.com/AsakaTigar/dentsplat-web)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:24:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zero-install browser 3D Gaussian Splatting prototype for dental data: FDI semantics inside the container, shader-level clipping, auditable measurements.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AsakaTigar/dentsplat-web

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T10:17:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source web graphics engine built on WebGPU and WebGL2
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:19:53Z
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
- **发布时间/更新时间：** 2026-11-26T05:55:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository tracks the latest advancements in 3D Gaussian Splatting from Arxiv, with daily automated updates. Stay up-to-date with cutting-edge research in this exciting field!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/longxiang-ai/awesome-gaussians

### [playcanvas/splat-transform](https://github.com/playcanvas/splat-transform)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T13:56:07Z
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
- **发布时间/更新时间：** 2026-11-26T03:58:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [CVEO/dsh-digital-earth](https://github.com/CVEO/dsh-digital-earth)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:02:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 数字地球：DSH 三维地球插件，浏览、量测、分析 3D Tiles 与 3DGS，Agent 可读写场景
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CVEO/dsh-digital-earth

### [DisplayXR/displayxr-demo-gaussiansplat](https://github.com/DisplayXR/displayxr-demo-gaussiansplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:58:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** DisplayXR demo — real-time 3D Gaussian Splatting viewer for glasses-free 3D displays (OpenXR + Vulkan, Windows & macOS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DisplayXR/displayxr-demo-gaussiansplat

### [smojjofy/AAI3001_Computer-Vision-Deep-Learning_Group27](https://github.com/smojjofy/AAI3001_Computer-Vision-Deep-Learning_Group27)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T07:06:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Computer Vision & Deep Learning Project based on improving existing Gaussian Splatting workflows and Depth Estimation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/smojjofy/AAI3001_Computer-Vision-Deep-Learning_Group27

### [Linhta013/3d-gaussian-splatting-experiments](https://github.com/Linhta013/3d-gaussian-splatting-experiments)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:32:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Baselines and comparative experiments on 3D Gaussian Splatting, SplatFormer, MVSGaussian and Difix3D+ for novel view synthesis
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Linhta013/3d-gaussian-splatting-experiments

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T23:50:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [Artemarius/pocketsplat](https://github.com/Artemarius/pocketsplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T18:39:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Vulkan 1.3 3D Gaussian Splatting viewer for Android phones, measured like-for-like against web and native renderers
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Artemarius/pocketsplat

### [MicroPasts/splat-viewer](https://github.com/MicroPasts/splat-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T10:13:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A small gaussian splat viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MicroPasts/splat-viewer

### [InkMind-AI/CausalSplat](https://github.com/InkMind-AI/CausalSplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:37:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for CausalSplat: Hierarchical Reasoning in 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/InkMind-AI/CausalSplat

### [HYNCM/web-3DGS](https://github.com/HYNCM/web-3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:49:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/HYNCM/web-3DGS

### [Well-Made/ComfyUI-SHARP-Gaussian-Stereo](https://github.com/Well-Made/ComfyUI-SHARP-Gaussian-Stereo)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:22:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A standalone ComfyUI extension for Apple SHARP, bringing single-image 3D Gaussian Splatting and an interactive stereo viewer with adjustable depth, splat size, and camera controls.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Well-Made/ComfyUI-SHARP-Gaussian-Stereo

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T06:39:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T03:08:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Seanwilliam2077/3dgs-collision](https://github.com/Seanwilliam2077/3dgs-collision)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T02:57:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Collision for 3D Gaussian splat scenes: voxel shell for characters, camera volume, UE walk tests
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Seanwilliam2077/3dgs-collision

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T19:28:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [stevenhuynh87/khanhnam-3dgs-nav](https://github.com/stevenhuynh87/khanhnam-3dgs-nav)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T16:38:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Đề tài phát triển giải thuật và mô hình học máy cho planning an toàn trên bản đồ 3D Gaussian Splatting có nhãn ngữ nghĩa, chỉ dùng simulation trên GPU của trường (không robot, camera, LiDAR hay mua thiết bị).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/stevenhuynh87/khanhnam-3dgs-nav

### [Azure-d-source/SplatForge-Spatial-Studio](https://github.com/Azure-d-source/SplatForge-Spatial-Studio)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T08:55:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 灵境智绘 (SplatForge) · 面向受限空间的仿生蛇形 3DGS 实景重建、多视角点云补全与端云协同空间视觉仿真工作台
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Azure-d-source/SplatForge-Spatial-Studio

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T15:57:39Z
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
- **发布时间/更新时间：** 2026-11-26T02:42:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [cfahlgren1/idol-mlx](https://github.com/cfahlgren1/idol-mlx)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T15:36:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photo to 3D Gaussian splat in ~15 s on a Mac: Idol + Idol Turbo on Apple Silicon (unofficial)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cfahlgren1/idol-mlx

### [ZeshenTian/splatforge](https://github.com/ZeshenTian/splatforge)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T17:07:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Turn raw 3DGS into physics-ready scenes and objects.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZeshenTian/splatforge

### [5undura/3DGS](https://github.com/5undura/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T09:58:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/5undura/3DGS

### [Pero1031/3dgs-toy](https://github.com/Pero1031/3dgs-toy)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-26T01:57:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Pero1031/3dgs-toy

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T20:10:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [xiliu8006/3DGS-Enhancer-project](https://github.com/xiliu8006/3DGS-Enhancer-project)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T18:38:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xiliu8006/3DGS-Enhancer-project

### [TitanothereYik/VotionSplat-mockup](https://github.com/TitanothereYik/VotionSplat-mockup)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T15:17:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Votion 3DGS 2.0 clickable HTML dummy UI
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/TitanothereYik/VotionSplat-mockup

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 8 |
| GitHub | ok: 62 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 1 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 8/8 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

