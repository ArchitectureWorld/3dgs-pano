---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-19T09:42:41Z
window_end_utc: 2026-11-20T09:29:59Z
generated_at_utc: 2026-11-20T09:29:59Z
item_count: 75
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-20

**统计窗口：** 2026-11-19T09:42:41Z — 2026-11-20T09:29:59Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **75** 项去重后的有效线索：真正新增论文 **5** 项、实质论文修订 **1** 项、代码/版本/项目更新 **69** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Multi-View Transformer with Geometry-Guided Multi-Modal ControlNet for 3D Virtual Try-On](https://arxiv.org/abs/2611.25979v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [DfD-GS: Defocus Image Prior for Metric-Scale Single-View Depth Estimation and View Synthesis](https://arxiv.org/abs/2611.26072v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [PaveSplat: Resolution-Robust Feed-Forward Gaussian Splatting with Residually Corrected Surface-Aligned Covariances](https://arxiv.org/abs/2611.26045v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting](https://arxiv.org/abs/2611.26128v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting](https://arxiv.org/abs/2611.25934v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [Multi-View Transformer with Geometry-Guided Multi-Modal ControlNet for 3D Virtual Try-On](https://arxiv.org/abs/2611.25979v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T12:03:04Z
- **更新判定：** 真正新增
- **核心内容：** Editing a 3D Gaussian Splatting (3DGS) capture of a person so that they wear a new garment requires every rendered view to agree on the same garment details. Existing 3D virtual try-on (VTON) pipelines, however, edit training views largely independently and fuse them with hand-designed heuristics such as manually chosen reference views and fixed attention-blending weights. The resulting inconsistencies are baked into the 3D representation and surface as texture drift, blurred prints, and implausible geometry in novel views. We present GS-VTON-MVT, a three-stage framework that combines implicit and explicit 3D reasoning for consistent 3DGS try-on. (i) A multi-view inpainting transformer jointly edits a set of training views with full cross-view self-attention, so that cross-view correspondence is learned rather than imposed. (ii) A geometry-guided multi-modal ControlNet conditions the diffusion editor on the garment image together with depth and surface normals rendered from the curren…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.25979v1

### [PaveSplat: Resolution-Robust Feed-Forward Gaussian Splatting with Residually Corrected Surface-Aligned Covariances](https://arxiv.org/abs/2611.26045v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T12:55:04Z
- **更新判定：** 真正新增
- **核心内容：** We present PaveSplat, a feed-forward Gaussian splatting method that adds a learned residual to the analytic surface-aligned covariance, keeping surfels paving the visible surface across rendering resolutions. Pixel-aligned feed-forward Gaussian splatting predicts one primitive per pixel from a few images in a single pass, and its rendering quality depends on how well these primitives cover the surface. Recent surfel-based methods compute the surface-aligned covariance analytically from predicted depth. However, this covariance has no way to correct the surfel orientation where the depth-derived frame is ill-posed. The surfels then cover the surface loosely; at the training resolution each surfel's one-pixel minimum footprint covers the gaps, but they show up as holes when the same prediction is re-rendered at a higher resolution. To address this, we keep the analytic covariance as an initialization, with its axes aligned to the surface tangents, and add an identity-initialized unit-qu…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.26045v1

### [CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting](https://arxiv.org/abs/2611.26128v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T13:51:14Z
- **更新判定：** 真正新增
- **核心内容：** Single-particle cryo-electron microscopy (cryo-EM) determines macromolecular structures from noisy particle images. However, rare, transient compositional states and subtle, continuous conformational variation are difficult to resolve. We present CryoGaussian, a Gaussian splatting method for heterogeneous cryo-EM reconstruction that fits an explicit Gaussian density representation directly to the particle images through a differentiable rasterizer rendering orthographic line integrals modulated by the contrast transfer function. The Gaussians are initialized randomly, with their number derived from the estimated spatial support of the molecular density and their minimum size bounded by the Nyquist frequency of the particle images. To capture the compositional and conformational variation across particle images, we learn particle-image and per-Gaussian latents that jointly modulate the base position, amplitude, and scale of each Gaussian. Each structural state is then reconstructed by…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.26128v1

### [AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting](https://arxiv.org/abs/2611.25934v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T11:20:23Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis, but Gaussian rasterization attenuates fine-scale scene structure through the projected covariance of each primitive. We show that contracting these projected covariances at inference time can mitigate the effective bandwidth limitation induced by finite Gaussian footprints, motivating a multi-aperture rendering framework for super-resolution. Based on this insight, we propose AGSR (Aperture-Guided Super-Resolution), a lightweight inference-time framework that progressively fuses multi-aperture renderings using uncertainty-guided feature aggregation and geometric conditioning from transmittance and depth cues. AGSR operates as a plug-in enhancement for pre-trained 3DGS models. Experiments on the Mip-NeRF 360 benchmark show that AGSR outperforms lightweight image-space super-resolution baselines, with gains increasing as the underlying Gaussian representation deteriorates. The results provide evidence that covariance c…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.25934v1

### [GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting](https://arxiv.org/abs/2610.36760v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T11:07:50Z
- **更新判定：** 实质修订
- **核心内容：** Feed-forward Gaussian Splatting enables efficient novel view synthesis, but pixel-aligned prediction makes the primitive count grow with image resolution and view count, leading to substantial redundancy and increased computational cost. Non-pixel-aligned methods address this limitation by predicting a fixed number of Gaussians. Without explicit ray and depth constraints, these methods yield misplaced Gaussian centers, causing rendering artifacts under large viewpoint changes. To address this issue, we introduce GeoGSplat, a geometry-grounded feed-forward model that explicitly incorporates geometric priors into the non-pixel-aligned framework. A dual-branch encoder constructs Anchors and Triplane to capture coarse 3D structure and fine-grained scene features, respectively. Subsequently, a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives, enabling 3D reconstruction and novel view synthesis. GeoGSplat surpasses both state-of-the-art pixel-aligned and no…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.36760v2

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T09:27:25Z
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
- **发布时间/更新时间：** 2026-11-20T09:27:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [IRIS-LAB-whu/Tortho-Gaussian-PlusPlus](https://github.com/IRIS-LAB-whu/Tortho-Gaussian-PlusPlus)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T14:41:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An advanced 3DGS training framework that suppresses geometric drift and floaters in UAV scenes and automatically prunes unreliable peripheral regions, coupled with a robust gravity-aligned TDOM rendering solution
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IRIS-LAB-whu/Tortho-Gaussian-PlusPlus

### [Benevision/SplatWork](https://github.com/Benevision/SplatWork)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T03:01:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Make, train, view and edit 3D Gaussian splats on your own Mac, iPhone and Linux GPU machines — native Metal trainer and renderer, CUDA worker, multi-device block training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Benevision/SplatWork

### [dborrull/DBS_SplatTrain](https://github.com/dborrull/DBS_SplatTrain)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T09:26:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Nuke node that trains a Gaussian splat from a tracked shot with Brush and brings it back aligned to the track camera.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dborrull/DBS_SplatTrain

### [CarlottaSeal/neural-rendering-cuda](https://github.com/CarlottaSeal/neural-rendering-cuda)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T06:58:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Neural rendering GPU kernels: optimized 3DGS rasterizer (sm_120), Instant-NGP and differentiable rasterization from scratch
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CarlottaSeal/neural-rendering-cuda

### [jgunaratne/room-splat](https://github.com/jgunaratne/room-splat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T23:04:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** iPhone LiDAR capture streamed to a GPU for live, progressive Gaussian Splat training
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jgunaratne/room-splat

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T18:49:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting in Blender: train 3D Gaussian Splats from your Blender scene with LichtFeld Studio and import splats from the LichtFeld Portal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [Vexlc/road-hazard-reconstruction](https://github.com/Vexlc/road-hazard-reconstruction)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T02:01:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible stereo, RGB-D and procedural road-hazard assets with dynamic 3DGS scene insertion and selectable visualizations.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Vexlc/road-hazard-reconstruction

### [cia-mac/splatplayer](https://github.com/cia-mac/splatplayer)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T00:56:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source desktop app for playing temporal Gaussian Splat sequences as navigable 3D video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cia-mac/splatplayer

### [playcanvas/supersplat v3.9.1](https://github.com/playcanvas/supersplat/releases/tag/v3.9.1)

- **主题：** 压缩与轻量化
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T13:37:45Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Publish with LODs from 1M splats and drop the SH band sliders by @slimbuck in https://github.com/playcanvas/supersplat/pull/1114 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.9.0...v3.9.1
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Decode SOG in chunks to avoid wasm32 OOM on large files (fixes #490) (#491) * fix(sogs): decode SOG in chunks to avoid wasm32 OOM on large files The decoder kept the zip buffer, the compressed file cache, all decoded RGBA images and full-size f32 arrays alive at the same time, which exceeds the 4 GiB wasm32 limit on large files (~40M splats). - finish() moves the zip buffer into decode_sogs, dropped after preload - cache entries are removed on their last use - compressed bytes are dropped right after each image decode - splats are emitted in MAX_SPLAT_CHUNK blocks via set_batch, with reused buffers; shN centroids/labels are loaded once and decoded per block - tests: 70k-splat v1/v2 SOG zips with 3 SH bands, compared against a per-splat reference Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> * refactor(sogs): address review feedback Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>](https://github.com/sparkjsdev/spark/commit/0bca3ab50a4bf7db1c8f7b24aa7a0ecd874583cf)

- **主题：** 压缩与轻量化
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-19T18:51:10Z
- **更新判定：** 代码实质更新
- **核心内容：** Decode SOG in chunks to avoid wasm32 OOM on large files (fixes #490) (#491) * fix(sogs): decode SOG in chunks to avoid wasm32 OOM on large files The decoder kept the zip buffer, the compressed file cache, all decoded RGBA images and full-size f32 arrays alive at the same time, which exceeds the 4 GiB wasm32 limit on large files (~40M splats). - finish() moves the zip buffer into decode_sogs, dropped after preload - cache entries are removed on their last use - compressed bytes are dropped right after each image decode - splats are emitted in MAX_SPLAT_CHUNK blocks via set_batch, with reused buffers; shN centroids/labels are loaded once and decoded per block - tests: 70k-splat v1/v2 SOG zips with 3 SH bands, compared against a per-splat reference Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> * refactor(sogs): address review feedback Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 (1M context) <noreply…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T03:24:24Z
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
- **发布时间/更新时间：** 2026-11-19T15:59:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a 3DGS(3D Gaussian Splatting) viewer built on Three.js, with features for marking, measurements, preset-lod rendering, etc.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reall3d-com/Reall3dViewer

### [Publish with LODs from 1M splats and drop the SH band sliders (#1114)](https://github.com/playcanvas/supersplat/commit/e591645d895f6d521cac62eb2c6bc624ead1b608)

- **主题：** 压缩与轻量化
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T13:34:22Z
- **更新判定：** 代码实质更新
- **核心内容：** Publish with LODs from 1M splats and drop the SH band sliders (#1114)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [jo-chemla/3dtiled-to-3dtiles](https://github.com/jo-chemla/3dtiled-to-3dtiles)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T15:51:24Z
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
- **发布时间/更新时间：** 2026-11-20T08:55:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official code for "Semantic-Guided Density Control for Compact Semantic 3D Gaussian Splatting" (Computers & Graphics), anchor-based instantiation on ObjectGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZehuiWU2009/sgdc-objectgs

### [waveviewer/draco-gaussian](https://github.com/waveviewer/draco-gaussian)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T07:57:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Draco fork with 3D Gaussian splatting support: compress Gaussian .ply scenes to .drc and decode them back
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/waveviewer/draco-gaussian

### [vinayak-vc/UEPointForge](https://github.com/vinayak-vc/UEPointForge)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T05:32:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Unreal Engine 5.5 plugin for real-time 3D Gaussian Splatting and large-scale Point Cloud visualization, featuring GPU-accelerated rendering, Octree-based streaming, and Level of Detail (LOD) management.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vinayak-vc/UEPointForge

### [DfD-GS: Defocus Image Prior for Metric-Scale Single-View Depth Estimation and View Synthesis](https://arxiv.org/abs/2611.26072v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-19T13:14:56Z
- **更新判定：** 真正新增
- **核心内容：** Recovering metric-scale geometry from observations at a single viewpoint remains fundamentally ill-posed, limiting the reliability of novel view synthesis. Recent methods rely on learned monocular depth priors, which provide strong structural estimates but can suffer from scale ambiguity and dataset-dependent biases. We propose DfD-GS, a feed-forward framework that predicts a metric-scale 3D Gaussian scene representation from a single-view all-in-focus--defocused image pair. The key idea is to exploit defocus blur as a physical metric depth cue. DfD-GS first estimates a defocus-based metric disparity map from the all-in-focus--defocused image pair and the corresponding defocus strength. This estimate is used to align and refine a monocular depth prior to metric scale. Visible and hidden 3D Gaussians are then predicted for occlusion-aware novel view synthesis. Experiments on synthetic-defocus datasets constructed from Booster and Middlebury show that DfD-GS outperforms single-image bas…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.26072v1

### [ZhangAoCanada/3Dviewer](https://github.com/ZhangAoCanada/3Dviewer)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T07:02:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** just another 3D viewer for popular 3D representations, including 3DGS, mesh, point cloud, ...
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhangAoCanada/3Dviewer

### [cameornh/bardo](https://github.com/cameornh/bardo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T03:26:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A gaussian splatting / sdf physics sandbox
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cameornh/bardo

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T23:40:01Z
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
- **发布时间/更新时间：** 2026-11-20T09:24:54Z
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
- **发布时间/更新时间：** 2026-11-20T09:26:42Z
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
- **发布时间/更新时间：** 2026-11-20T04:36:19Z
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
- **发布时间/更新时间：** 2026-11-20T04:00:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [Kishore-suthersingh/3dgs-digital-twin](https://github.com/Kishore-suthersingh/3dgs-digital-twin)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:50:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Phone video -> COLMAP -> 3D Gaussian Splatting -> cleaned, web-viewable digital twin. Built on free Colab GPUs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kishore-suthersingh/3dgs-digital-twin

### [lhamyuh/CUHKSZ-CV-Proj2](https://github.com/lhamyuh/CUHKSZ-CV-Proj2)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:47:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reconstruct an object and place it inGarden:A reconstruction can look convincing in a single photograph and still break down when the camera moves. In thisproject, you will use held-out photographs and moving viewpoints to find out where a 3D Gaussian Splatting (3DGS)reconstruction holds up, where it fails, and why.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lhamyuh/CUHKSZ-CV-Proj2

### [saiKelkar/Property_Splats](https://github.com/saiKelkar/Property_Splats)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T06:35:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splatting pipelines for real estate: turning phone videos of rooms, interiors and buildings into interactive 3D tours. Built with COLMAP + Nerfstudio on Google Colab, by an architect exploring 3D vision for proptech.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/saiKelkar/Property_Splats

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T03:11:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [hj-jung-01/dual-lens-gs](https://github.com/hj-jung-01/dual-lens-gs)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T02:44:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Feed-Forward Gaussian Splatting from Asymmetric Dual-lens Stereo (IJCV 2026)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hj-jung-01/dual-lens-gs

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:11:58Z
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
- **发布时间/更新时间：** 2026-11-19T19:31:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible pipeline and simulation data for Semantic-Aware Generative Error Concealment for Resilient Real-Time 3DGS over Turbulent FSO Backhaul
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xuannamservice-ui/Semantic-Aware

### [playcanvas/supersplat v3.9.2](https://github.com/playcanvas/supersplat/releases/tag/v3.9.2)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T16:01:59Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Open the export dialog even when the saved export folder hangs by @slimbuck in https://github.com/playcanvas/supersplat/pull/1115 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.9.1...v3.9.2
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Fix packed covSplats accumulator throwing "Generator must be provided" (#471) * Fix SplatAccumulator: packed covSplats threw "Generator must be provided" With covSplats and without extSplats, a stray check after the packed covariance branch required a GsplatGenerator, so a covGenerator alone (which that branch already handles) always threw. Remove it. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01JtbHkmUpoNeo1EwbHiLihG * Split the covariance accumulator test by mode The test ran the packed and the extended accumulator inside one case named after the packed one. Each mode is now its own case, and the generator declares only its input and output types. --------- Co-authored-by: jesus luque <jesus.luque@lucab.co.uk> Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com> Co-authored-by: Oscar Lorentzon <oscarlorentzon@users.noreply.github.com>](https://github.com/sparkjsdev/spark/commit/8a665d14b779c6e4b5eafa188bb6569dc414342a)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-19T18:50:01Z
- **更新判定：** 代码实质更新
- **核心内容：** Fix packed covSplats accumulator throwing "Generator must be provided" (#471) * Fix SplatAccumulator: packed covSplats threw "Generator must be provided" With covSplats and without extSplats, a stray check after the packed covariance branch required a GsplatGenerator, so a covGenerator alone (which that branch already handles) always threw. Remove it. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01JtbHkmUpoNeo1EwbHiLihG * Split the covariance accumulator test by mode The test ran the packed and the extended accumulator inside one case named after the packed one. Each mode is now its own case, and the generator declares only its input and output types. --------- Co-authored-by: jesus luque <jesus.luque@lucab.co.uk> Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com> Co-authored-by: Oscar Lorentzon <oscarlorentzon@users.noreply.github.com>
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:35:34Z
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
- **发布时间/更新时间：** 2026-11-20T02:14:28Z
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
- **发布时间/更新时间：** 2026-11-20T09:18:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@b2e7bc02207f450fd84a54128455e6c8282f21de/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/f94964a712e217b7121ae642299fdac6041e5a12)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-19T18:53:52Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@b2e7bc02207f450fd84a54128455e6c8282f21de/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [schardong/flowing](https://github.com/schardong/flowing)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T15:39:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementation of "FLOWING 🌊: Implicit Neural Flows for Structure-Preserving Morphing", to appear on NeurIPS 2025
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/schardong/flowing

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T09:11:30Z
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
- **发布时间/更新时间：** 2026-11-20T07:34:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [Sadik00789/CinderGS](https://github.com/Sadik00789/CinderGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T20:40:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time, native 3D Gaussian Splatting (3DGS) rasterization & volumetric cage kinematics engine in pure Rust (CubeCL + WGPU).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Sadik00789/CinderGS

### [lifangyi911/GSPan](https://github.com/lifangyi911/GSPan)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:41:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GSPan: Arbitrary-Scale Pansharpening with Continuous 2D Gaussian Splatting (PyTorch)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lifangyi911/GSPan

### [RoboVLA/More-from-Less](https://github.com/RoboVLA/More-from-Less)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:22:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research code and project page for More from Less: sparse-demonstration bimanual manipulation with 3DGS digital twins.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RoboVLA/More-from-Less

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T23:58:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [Robusto1000/archviz-room-walkthrough](https://github.com/Robusto1000/archviz-room-walkthrough)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T09:10:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive Gaussian splat walkthrough of the bedroom and living room.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Robusto1000/archviz-room-walkthrough

### [Seanwilliam2077/3dgs-collision](https://github.com/Seanwilliam2077/3dgs-collision)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:28:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Collision for 3D Gaussian splat scenes: voxel shell for characters, camera volume, UE walk tests
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Seanwilliam2077/3dgs-collision

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T07:39:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [philleer/realtime_3dvision](https://github.com/philleer/realtime_3dvision)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T07:04:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Realtime 3D Vision Project, Detection/DepthEstimation/3DGS included.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/philleer/realtime_3dvision

### [aozi6666/Sparse-3DGS-heritage-VQA](https://github.com/aozi6666/Sparse-3DGS-heritage-VQA)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T06:29:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 受限采集下的稀疏视角 3DGS 文化遗产重建 + 多模态大模型·VQA-VL 流式视频问答与空间定位系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aozi6666/Sparse-3DGS-heritage-VQA

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T04:03:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [xeohyun/where-to-render](https://github.com/xeohyun/where-to-render)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T01:47:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Where to Render: 3DGS 지도만으로 고른 ACE 학습 시점 웹 데모
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xeohyun/where-to-render

### [Bang9634/bangpick](https://github.com/Bang9634/bangpick)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T02:52:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A virtual real estate tour platform that reconstructs indoor spaces from video using 3D Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Bang9634/bangpick

### [gayan957/3dgs-capture-check](https://github.com/gayan957/3dgs-capture-check)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T07:24:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gayan957/3dgs-capture-check

### [caiyuanhao1998/X-Gaussian](https://github.com/caiyuanhao1998/X-Gaussian)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T18:22:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** "Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis" (ECCV 2024)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/X-Gaussian

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/b2e7bc02207f450fd84a54128455e6c8282f21de)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-11-19T18:53:52Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [3.9.2](https://github.com/playcanvas/supersplat/commit/7912e1d78b7a98cff26f7c8c2820a784b537819e)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T16:01:33Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.9.2
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Open the export dialog even when the saved export folder hangs (#1115)](https://github.com/playcanvas/supersplat/commit/c3f92288eb471f92166cfb18308ef3ad04f748a2)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T15:58:47Z
- **更新判定：** 代码实质更新
- **核心内容：** Open the export dialog even when the saved export folder hangs (#1115)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [3.9.1](https://github.com/playcanvas/supersplat/commit/292f53b74ca3b4f19985ab8afc0c6533534fe269)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-19T13:37:16Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.9.1
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T02:46:40Z
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
- **发布时间/更新时间：** 2026-11-20T09:13:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** From insta360/DJI to Gaussian Splatting Easy and Direct
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MapMindAI/EasyGaussianSplatting

### [chunyang00000011/3DGS-maker](https://github.com/chunyang00000011/3DGS-maker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T08:58:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chunyang00000011/3DGS-maker

### [joezgao/seen-from-twelve-sides](https://github.com/joezgao/seen-from-twelve-sides)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T04:32:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 3D Gaussian Splatting fit written from scratch in NumPy, shown in the browser.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/joezgao/seen-from-twelve-sides

### [WhiteRott/splatlink](https://github.com/WhiteRott/splatlink)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T00:51:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SplatLink: turn videos and photos into 3D Gaussian splats on your own PC. Based on OOOSplat.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WhiteRott/splatlink

### [in33/SpaceBrowser](https://github.com/in33/SpaceBrowser)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T22:11:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空间浏览器 SpaceBrowser.cn — 基于 Aholo 空间智能 API，用一句话或一组照片生成可漫游的高保真 3D 空间（3DGS / Lux3X）。纯 HTML+JS+CSS，浏览器即用。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/in33/SpaceBrowser

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T19:09:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [Pero1031/3dgs-toy](https://github.com/Pero1031/3dgs-toy)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T13:48:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Pero1031/3dgs-toy

### [rafaelgscc/3dgs-pipeline-resources](https://github.com/rafaelgscc/3dgs-pipeline-resources)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-19T13:43:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Resources, codes and other stuff about Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rafaelgscc/3dgs-pipeline-resources

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 6 |
| GitHub | ok: 69 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 6/6 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

