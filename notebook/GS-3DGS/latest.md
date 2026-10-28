---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-27T07:08:57Z
window_end_utc: 2026-10-28T07:47:52Z
generated_at_utc: 2026-10-28T07:47:52Z
item_count: 76
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-28

**统计窗口：** 2026-10-27T07:08:57Z — 2026-10-28T07:47:52Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **76** 项去重后的有效线索：真正新增论文 **7** 项、实质论文修订 **1** 项、代码/版本/项目更新 **67** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2610.37149v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats](https://arxiv.org/abs/2610.37406v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T08:51:00Z
- **更新判定：** 真正新增
- **核心内容：** Achieving high-quality reconstruction and responsive camera tracking remains challenging for monocular RGB Gaussian splatting SLAM under a limited optimization budget. We present an online system that addresses this challenge by combining learned geometric priors with explicit geometric camera tracking, which can substantially outperform learned camera prediction in terms of tracking accuracy. A frozen streaming 3D foundation model serves as a virtual RGB-D sensor, providing depth estimation from monocular video. An explicit geometric solver then estimates camera motion through feature reprojection, and a streaming Gaussian mapper integrates the resulting observations into a dense scene representation. We further show that geometric tracking improves camera pose accuracy across representative streaming geometry backbones, demonstrating the broader applicability of our approach. Extensive experiments on indoor and outdoor datasets show that our method significantly improves reconstruct…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.36853v1

### [CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats](https://arxiv.org/abs/2610.37406v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T15:21:01Z
- **更新判定：** 真正新增
- **核心内容：** Photorealistic volume rendering of computed tomography (CT) may convey anatomy intuitively, but it needs the CT data, dedicated software and a powerful graphics processor. Three-dimensional Gaussian splatting (3DGS) displays photorealistic scenes in real time on less powerful devices, but existing medical approaches train each scene for minutes to hours. We aimed to convert a CT volume rendering directly into a 3DGS model without training. Splats were placed on an adaptive octree of millimetre-sized cells. Their colour and opacity were computed on the graphics processor with the renderer's lighting, cell opacity was converted analytically into splat opacity, and faint splats were retained stochastically above the 1/255 opacity floor of standard 3DGS rasterisers. Six public CT scans (1.5-mm voxels) were converted with three transfer functions and compared with converged references by peak signal-to-noise ratio (PSNR), structural similarity and a learned perceptual metric. Two-million-s…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.37406v1

### [DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T12:58:16Z
- **更新判定：** 真正新增
- **核心内容：** The growing need for high-quality 3D content remains among the most prevalent challenges in virtual reality (VR). Recently, novel view synthesis techniques have enabled rapid content creation, with 3D Gaussian Splatting (3DGS) emerging as one of the most promising methods for generating high-fidelity 3D scenes. However, using 3DGS to reconstruct unbounded outdoor scenes can leave horizons incomplete due to missing data or a lack of distant geometric constraints. Such incompleteness can break immersion, compromising VR's core characteristic. A typical workaround in traditional VR systems is a textured cube (skybox) or sphere (skydome) surrounding the environment to create the illusion of a distant background. However, these approaches struggle to blend seamlessly with the reconstructed 3DGS geometry. To address these issues, we introduce the DomeGS framework, which incorporates the skydome concept not as a flat background shell, but as a part of the reconstructed Gaussian Splatting 3D…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.37172v1

### [GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting](https://arxiv.org/abs/2610.36760v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T07:15:03Z
- **更新判定：** 真正新增
- **核心内容：** Feed-forward Gaussian Splatting enables efficient novel view synthesis, but pixel-aligned prediction makes the primitive count grow with image resolution and view count, leading to substantial redundancy and increased computational cost. Non-pixel-aligned methods address this limitation by predicting a fixed number of Gaussians. Without explicit ray and depth constraints, these methods yield misplaced Gaussian centers, causing rendering artifacts under large viewpoint changes. To address this issue, we introduce GeoGSplat, a geometry-grounded feed-forward model that explicitly incorporates geometric priors into the non-pixel-aligned framework. A dual-branch encoder constructs Anchors and Triplane to capture coarse 3D structure and fine-grained scene features, respectively. Subsequently, a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives, enabling 3D reconstruction and novel view synthesis. GeoGSplat surpasses both state-of-the-art pixel-aligned and no…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.36760v1

### [LoBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T12:04:55Z
- **更新判定：** 实质修订
- **核心内容：** 3D Gaussian Splatting (3DGS) has established itself as an efficient representation for real-time, high-fidelity 3D scene reconstruction. However, scaling 3DGS to large and unbounded scenes such as city blocks remains difficult. Existing divide-and-conquer methods alleviate memory pressure by partitioning the scene into blocks and training on multiple, non-communicating GPUs, but introduce new bottlenecks: (i) partitions suffer from severe load imbalance since uniform or heuristic splits do not reflect actual computational demands, and (ii) coarse-to-fine pipelines fail to exploit the coarse stage efficiently, often reloading the entire model and incurring high overhead. In this work, we introduce LoBE-GS, a Load-Balanced and Efficient 3D Gaussian Splatting framework, that re-engineers the large-scale 3DGS pipeline. Specifically, LoBE-GS introduces a load-balanced KD-tree scene partitioning scheme with optimized cutlines that balance per-block camera counts. To accelerate preprocessing…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2510.01767v3

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:13:11Z
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
- **发布时间/更新时间：** 2026-10-28T06:16:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [OpenDriveLab/WorldEngine](https://github.com/OpenDriveLab/WorldEngine)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T15:39:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WorldEngine: Towards the Era of Post-Training for Autonomous Driving
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/OpenDriveLab/WorldEngine

### [XiaoBin2001/BoundedGS](https://github.com/XiaoBin2001/BoundedGS)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T09:52:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** BoundedGS: Memory-Efficient High-Resolution 3DGS Training
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/XiaoBin2001/BoundedGS

### [causcocharles/truck-3dgs-viewer](https://github.com/causcocharles/truck-3dgs-viewer)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:59:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive viewer for a trained Truck 3D Gaussian Splatting reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/causcocharles/truck-3dgs-viewer

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:30:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [22elix3r/TalkingHeadAvatar](https://github.com/22elix3r/TalkingHeadAvatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:29:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Audio-driven 3D Gaussian Splatting talking head avatar with FLAME, VHAP tracking, HuBERT motion, TTS, and virtual camera output.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/22elix3r/TalkingHeadAvatar

### [nff747/hyper-splat-engine](https://github.com/nff747/hyper-splat-engine)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:16:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zero-copy, virtualized WebGPU 3D Gaussian Splatting and spatial AI engine with distance LoD tile streaming and proactive VRAM paging.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nff747/hyper-splat-engine

### [PYGRASSREAL/pygrassreal-py3s-format](https://github.com/PYGRASSREAL/pygrassreal-py3s-format)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:05:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official Specification & Reference Codec for PyGrassReal .py3s (Unified 3D Gaussian Splatting + Collision Format)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/PYGRASSREAL/pygrassreal-py3s-format

### [Xget7/splatkit-ios](https://github.com/Xget7/splatkit-ios)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:13:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Metal Gaussian splatting SDK for iOS: Swift view, GPU visibility/radix, experimental LOD and hybrid tiles. MIT source and reproducible XCFramework.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit-ios

### [guanhaitingfengsheng/compact-event-3dgs](https://github.com/guanhaitingfengsheng/compact-event-3dgs)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T15:28:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Compact event-based 3D Gaussian reconstruction. Complete source code will be released upon acceptance of the associated manuscript.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/guanhaitingfengsheng/compact-event-3dgs

### [sivan7zZ/3DGS-COMPRESSION](https://github.com/sivan7zZ/3DGS-COMPRESSION)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T11:01:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sivan7zZ/3DGS-COMPRESSION

### [GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2610.37149v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T12:47:53Z
- **更新判定：** 真正新增
- **核心内容：** Open-vocabulary 3D occupancy prediction represents scene geometry and semantics in a unified voxel grid, enabling recognition beyond predefined categories. One approach reconstructs scenes with 3D Gaussians and converts them into voxel occupancy. However, Gaussian scale inflation and excessive overlap can distort voxel occupancy predictions, while semantic mixing can arise within Gaussians spanning multiple categories and during 3D--2D semantic feature alignment. We propose GCSR-OCC, which combines geometry calibration and multi-mode query-conditioned semantic routing for indoor occupancy prediction from a single RGB image. The Evidence-Conserving Gaussian-to-Occupancy operator (EC-G2O) uses kernel mass normalization, $p$-norm aggregation, and a learnable gain to suppress scale inflation and excessive local evidence accumulation while calibrating occupancy responses. Multi-mode Query-First Gaussian Semantic Routing (MM-QGSR) matches multiple semantic modes per Gaussian to text queries…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.37149v1

### [GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T11:11:48Z
- **更新判定：** 真正新增
- **核心内容：** Inserting virtual objects into scenes reconstructed via 2D or 3D Gaussian Splatting (2DGS/3DGS) is a key capability for content creation, AR, and synthetic data generation. However, realistic insertion requires the object to be seamlessly lit by the scene and, conversely, to cast physically plausible shadows onto it. Existing approaches either harmonize appearance in image space, sacrificing multi-view consistency, or approximate scene illumination with an environment map at the insertion point, which cannot represent near-field area lights such as windows and lamps that dominate indoor lighting. To address this, we present GraftRay, a unified method for physically consistent insertion of mesh objects into indoor scenes represented by either 2D or 3D Gaussians. We recover scene materials and surface normals with diffusion-based priors, and explicitly model spatially-extended emitters, solving their radiance in closed form. A hybrid renderer then jointly path-traces the scene Gaussians…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.37036v1

### [irisfreesiri/SSD-GS](https://github.com/irisfreesiri/SSD-GS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T00:48:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 🎉 Official code release of "SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting" (ICLR 2026).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/irisfreesiri/SSD-GS

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:02:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [sepahead/relief-atlas](https://github.com/sepahead/relief-atlas)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T04:44:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** On-device generative pipeline (FLUX.2 → TRELLIS.2 → 3DGS) producing a 10,079-asset 3D mesh corpus for disaster-relief, humanitarian-aid and civil-protection simulation — with automated 10-lens turntable QA gates, content policy enforcement and dual .spz/.splat export.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sepahead/relief-atlas

### [2072508371/truck-3dgs-demo](https://github.com/2072508371/truck-3dgs-demo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:13:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive 3D Gaussian Splatting demo with color, depth, and normal visualization.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/2072508371/truck-3dgs-demo

### [Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-27T09:19:15Z
- **更新判定：** 真正新增
- **核心内容：** The achievable gains of multiple-input multiple-output (MIMO) systems depend on channel state information (CSI), whose acquisition consumes pilot and feedback resources for every user in every coherence interval. Meanwhile, the propagation environment that shapes the channel persists. Exploiting such information will help to greatly reduce the overhead of CSI acquisition. This paper investigates the spatial MIMO channel rendering problem, which learns a latent beamspace channel scene from sparse observations and renders the long-term transmit and receive beam pair power map at unobserved user locations. Motivated by 3D Gaussian splatting in visual scene rendering, the proposed MIMO Gaussian splatting (MIMO-GS) represents the scene with pairs of receive and transmit 3D Gaussians, projects them from the user and base station onto the corresponding beam domains, and accumulates the beam associations through beam pair splatting. On a simulated urban scenario and measured indoor channels,…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.36880v1

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:15:29Z
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
- **发布时间/更新时间：** 2026-10-28T07:23:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, visual-inertial SLAM, 3D Gaussian Splatting and map-based localization in Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T06:08:24Z
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
- **发布时间/更新时间：** 2026-10-28T02:46:25Z
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
- **发布时间/更新时间：** 2026-10-28T02:20:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [Iloke-Alusala/Gaussian_Splatting_Localiser](https://github.com/Iloke-Alusala/Gaussian_Splatting_Localiser)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T06:12:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A pipeline designed to render and compare images derived from a pose within a 3DGS Map, and implement course and fine localisation implementations and assess viability for on-edge compute
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Iloke-Alusala/Gaussian_Splatting_Localiser

### [viruthshaan/ffgs](https://github.com/viruthshaan/ffgs)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T18:08:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page: Frame-Consistent Feed-Forward 3DGS (arXiv 2610.23039)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/viruthshaan/ffgs

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:33:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WHIK Studio: free node-based video compositing for Windows, with 3D Gaussian splat (3DGS) editing. Preview, updated weekly.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/suin-park/Whik

### [fubukisama/Gaussian-Scene-Workbench](https://github.com/fubukisama/Gaussian-Scene-Workbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:47:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/Gaussian-Scene-Workbench

### [MisterE123/spark-tour-studio](https://github.com/MisterE123/spark-tour-studio)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:21:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows Gaussian splat tour editor and locally bundled WebXR viewer powered by Spark
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MisterE123/spark-tour-studio

### [gyf0323/InstGuide-GS](https://github.com/gyf0323/InstGuide-GS)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T04:35:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Instance-guided open-vocabulary 3D semantic segmentation with Gaussian splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gyf0323/InstGuide-GS

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:16:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high performance 3DGS renderer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-viewer

### [playcanvas/splat-transform](https://github.com/playcanvas/splat-transform)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:06:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CLI tool and library for 3D Gaussian splat processing and conversion
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/splat-transform

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:59:23Z
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
- **发布时间/更新时间：** 2026-10-28T02:16:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:57:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Xget7/splatkit](https://github.com/Xget7/splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:00:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time Gaussian splatting SDKs for Android/Vulkan, iOS/Metal and React Native, sharing a C++17 engine.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit

### [thunderheronight/splat-workshop](https://github.com/thunderheronight/splat-workshop)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T17:22:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GUI for the Arcturus Vision splat pipeline: pick, check and convert Steam Frame camera recordings and send them to the Gaussian XR gallery
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thunderheronight/splat-workshop

### [Saqoosha/ghostline](https://github.com/Saqoosha/ghostline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T01:08:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Recover FPV flight paths from goggle DVR on a 3DGS scan, and replay them
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Saqoosha/ghostline

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T11:53:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [Loppas/playcanvas-quake3](https://github.com/Loppas/playcanvas-quake3)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:15:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A port of ioquake to the Playcanvas engine with the added ability to render gaussian splat maps
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Loppas/playcanvas-quake3

### [kamyy/ai-gaussian-splatter](https://github.com/kamyy/ai-gaussian-splatter)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T01:31:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Upload multi-angle photos of a physical object, get back a real-time 3D Gaussian Splat viewable and shareable in-browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kamyy/ai-gaussian-splatter

### [XiaoBin2001/ParetoGS](https://github.com/XiaoBin2001/ParetoGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T09:54:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ParetoGS: High-Quality Continuous-Budget 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/XiaoBin2001/ParetoGS

### [aozi6666/Sparse-3DGS-heritage-VQA](https://github.com/aozi6666/Sparse-3DGS-heritage-VQA)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T06:09:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 受限采集下的稀疏视角 3DGS 文化遗产重建 + 多模态大模型·VQA-VL 流式视频问答与空间定位系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aozi6666/Sparse-3DGS-heritage-VQA

### [xibihe/walk-into-memory](https://github.com/xibihe/walk-into-memory)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:52:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Walk into a photo on Apple Vision Pro: photo → Gaussian splat → SPZ → visionOS renderer with hand interactions
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xibihe/walk-into-memory

### [BoBoDai/3dgs-viewer](https://github.com/BoBoDai/3dgs-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:24:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/BoBoDai/3dgs-viewer

### [mercurio-develop/niflheim-studio](https://github.com/mercurio-develop/niflheim-studio)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:42:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ▎ NIFLheim Studio is an open-source shot pipeline: design a character, drop in a concept painting, direct the camera and VFX in 3D, and LTX shoots it, then fly through your shot as a Gaussian splat. Open weights, one 16 GB GPU, built on the Comfy SDK.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mercurio-develop/niflheim-studio

### [skye-cqu/long-night-inn](https://github.com/skye-cqu/long-night-inn)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:24:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 长夜驿站 · Aholo全球3D AI黑客松参赛作品——每晚你下潜的世界，由你昨天做过的事缝合而成（Aholo World API 生成七夜世界 + Lux3D 生成角色 + aholo-viewer 运行时）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/skye-cqu/long-night-inn

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:17:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [ellipticalcurves/alhiraoud](https://github.com/ellipticalcurves/alhiraoud)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T00:34:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** al hira oud website with gaussian splatting scroll through
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ellipticalcurves/alhiraoud

### [freddewitt/splatcam](https://github.com/freddewitt/splatcam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T22:57:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A cinema camera for Gaussian Splat scenes: real lenses, physical depth of field, shot timeline, 16-bit export. Local WebGPU app.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/freddewitt/splatcam

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T21:35:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [KusMar00/camera-sonar-3dgs](https://github.com/KusMar00/camera-sonar-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T14:12:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KusMar00/camera-sonar-3dgs

### [q760440238/vulkan-world-models](https://github.com/q760440238/vulkan-world-models)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:07:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Vulkan/wgpu ports: LingBot-World, HunyuanWorld-Mirror, 3D Gaussian Splatting (AMD Windows, no CUDA)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/q760440238/vulkan-world-models

### [kylinfires/gaussian-splatting-vulkan](https://huggingface.co/kylinfires/gaussian-splatting-vulkan)

- **主题：** GPU与加速实现
- **来源：** Hugging Face 模型
- **发布时间/更新时间：** 2026-10-28T02:29:40Z
- **更新判定：** 模型更新
- **核心内容：** 近期更新的模型；标签：rust, vulkan, wgpu, gaussian-splatting, 3dgs, vksplat, amd, no-cuda, zh, en, license:other, region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

### [gayan957/3dgs-capture-check](https://github.com/gayan957/3dgs-capture-check)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:20:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gayan957/3dgs-capture-check

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:11:59Z
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
- **发布时间/更新时间：** 2026-10-28T06:19:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** From insta360/DJI to Gaussian Splatting Easy and Direct
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MapMindAI/EasyGaussianSplatting

### [sid-gupta-007/3dgs](https://github.com/sid-gupta-007/3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T03:45:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sid-gupta-007/3dgs

### [AssassinHLQ/csust](https://github.com/AssassinHLQ/csust)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T16:56:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Godot 4.7 越肩射击 + 跑酷 + 期货交易沙盒《长沙理工：2067》：12 段 571 m 跑酷、暗网比纳、保证金/负债/强平经济、3D 高斯泼溅校园
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AssassinHLQ/csust

### [TitanothereYik/votion-3dgs-2-html](https://github.com/TitanothereYik/votion-3dgs-2-html)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T07:23:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Votion 3DGS 2.0 clickable HTML dummy UI
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/TitanothereYik/votion-3dgs-2-html

### [pawafa666-eng/3DGS-duibi](https://github.com/pawafa666-eng/3DGS-duibi)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T06:44:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pawafa666-eng/3DGS-duibi

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T06:30:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [wwwwwwcy/3dgs-view-count-study](https://github.com/wwwwwwcy/3dgs-view-count-study)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T05:19:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wwwwwwcy/3dgs-view-count-study

### [zzzhang1127/3dgs-mipnerf360-bonsai](https://github.com/zzzhang1127/3dgs-mipnerf360-bonsai)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T04:55:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible original 3D Gaussian Splatting on the Mip-NeRF 360 Bonsai scene
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zzzhang1127/3dgs-mipnerf360-bonsai

### [hq2048/GaussAV](https://github.com/hq2048/GaussAV)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-28T02:58:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is the official implementation of Saliency-Embedded 3D Gaussian Splatting Video with Spatial Audio.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hq2048/GaussAV

### [HHW9944/3dgs-auto-collider-urp](https://github.com/HHW9944/3dgs-auto-collider-urp)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T23:02:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** KU University 2026 Second Graduation Project(3192)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/HHW9944/3dgs-auto-collider-urp

### [T-Tatsuya-W/3dgs-experiments](https://github.com/T-Tatsuya-W/3dgs-experiments)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T21:21:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/T-Tatsuya-W/3dgs-experiments

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T16:01:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T13:58:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

### [autumn119/3DGS-Survey](https://github.com/autumn119/3DGS-Survey)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T12:52:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for 3DGS Survey paper
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/autumn119/3DGS-Survey

### [miaopasi677/3dgs-colab](https://github.com/miaopasi677/3dgs-colab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T12:39:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/miaopasi677/3dgs-colab

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 8 |
| GitHub | ok: 67 |
| Hugging Face | ok: 1 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 8/8 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

