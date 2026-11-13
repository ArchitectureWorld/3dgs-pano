---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-12T09:03:28Z
window_end_utc: 2026-11-13T08:57:31Z
generated_at_utc: 2026-11-13T08:57:31Z
item_count: 74
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-13

**统计窗口：** 2026-11-12T09:03:28Z — 2026-11-13T08:57:31Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **74** 项去重后的有效线索：真正新增论文 **2** 项、实质论文修订 **3** 项、代码/版本/项目更新 **69** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Kosmo-GFM: A Production-Ready Geometry Foundation Model](https://arxiv.org/abs/2611.16840v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [MuViRL: Multimodal View-Invariant Visual Speech Representation Learning via Calibrated View Aggregation](https://arxiv.org/abs/2611.16655v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing](https://arxiv.org/abs/2611.12038v2) | 实质修订 | arXiv | R2/E0 | P1 |
| 4 | [playcanvas/supersplat v3.8.1](https://github.com/playcanvas/supersplat/releases/tag/v3.8.1) | 正式版本发布 | GitHub Release · playcanvas/supersplat | E2 | P1 |
| 5 | [Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](https://arxiv.org/abs/2605.07351v3) | 实质修订 | arXiv | R2/E0 | P1 |

## 分类详述

### [Kosmo-GFM: A Production-Ready Geometry Foundation Model](https://arxiv.org/abs/2611.16840v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-12T14:17:22Z
- **更新判定：** 真正新增
- **核心内容：** We present Kosmo-GFM, a scene reconstruction system that integrates a geometry foundation model (GFM), a pose optimization engine (PoseEngine), and reconstruction-derived supervision from KosmoWorld. GFM predicts camera parameters, depth, cross-view correspondences, and dynamic 3D points from images and videos. PoseEngine combines these predictions with geometric optimization to recover scene-level camera poses and geometry for downstream 3D and 4D Gaussian Splatting. KosmoWorld generates images and geometric supervision from reconstructed real-world scenes to improve GFM's geometric predictions. On the Sparse and Medium subsets of SpatialBench, GFM achieves the lowest absolute relative depth error and the highest relative-pose AUC at 5 degrees among the compared methods. It also achieves the lowest mean endpoint errors for dynamic points and scene flow across the five evaluated datasets. Across 34 scenes completed by all compared reconstruction systems, PoseEngine achieves the highes…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.16840v1

### [MuViRL: Multimodal View-Invariant Visual Speech Representation Learning via Calibrated View Aggregation](https://arxiv.org/abs/2611.16655v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-12T11:31:59Z
- **更新判定：** 真正新增
- **核心内容：** Multimodal representation learning combines complementary signals to capture shared semantic information. For dynamic scenes, these representations need to remain consistent across views while preserving distinctions between temporal states. In visual speech representation learning, view variation changes the visibility and reliability of articulation cues, making it difficult to learn such representations from synchronized audio and video. To address this challenge, we propose MuViRL, a self-supervised framework for multimodal view-invariant visual speech representation learning via calibrated view aggregation. The framework combines synchronized 3D Gaussian view synthesis with multimodal self-supervision to learn consistent representations from real and synthesized data. A multimodal decision model learns relative view utility from teacher prediction losses, and its calibrated scores guide the aggregation of complementary information. Aggregation-to-Single Distillation transfers the…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.16655v1

### [DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing](https://arxiv.org/abs/2611.12038v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-12T13:35:40Z
- **更新判定：** 实质修订
- **核心内容：** This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Objects in dynamic motion remain a significant challenge for dense visual SLAM since dynamic observations can contaminate camera tracking and scene reconstruction. Although 3DGS (3D Gaussian splatting) enables efficient dense mapping, existing 3DGS-SLAM systems may exhibit instability when dynamic objects violate their underlying static-scene assumption. Excluding dynamic observations can reduce their influence on tracking and mapping, but may leave occluded static backgrounds missing or weakly constrained. Our proposed DPGS-SLAM is a monocular RGB SLAM framework that supports provisional representations of insufficiently observed static backgrounds through asynchronous diffusion-based background completion and provenance-aware Gaussian mapping. Dynamic regions are identified through optical-flow-based motion discovery and…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.12038v2

### [Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](https://arxiv.org/abs/2605.07351v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-12T15:40:35Z
- **更新判定：** 实质修订
- **核心内容：** While Gaussian Splatting-based Feature Fields (GSFFs) have shown promise for visual localization, this paper highlights that photometrically optimized GSFFs are inherently not suitable for 2D-3D matching. The volumetric extent of each Gaussian induces many-to-one pixel-to-point mappings that destabilize PnP-based pose estimation, while photometric optimization gives rise to superfluous Gaussians devoid of multi-view consistency. To address these issues, we propose SplitGS-Loc, a GSFFs construction framework for localization, which disambiguates 2D-3D correspondences by exploiting Gaussian attributes. Our key design, Mixture-of-Gaussians-based splitting, decomposes each Gaussian into smaller Gaussians, replacing ambiguous many-to-one with precise one-to-one correspondences. In parallel, we exploit composition weights from GS rasterization to select Gaussians that significantly and consistently contribute across multiple views and aggregate discriminative features through strong pixel-G…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2605.07351v3

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:06:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [bertaveira/mojosplat](https://github.com/bertaveira/mojosplat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T22:25:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting, training and rendering 100% implemented in 🔥Mojo - Exploring multi-vendor GPU performance
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/bertaveira/mojosplat

### [samaust/openftgs](https://github.com/samaust/openftgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:26:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on openftgs-synth datasets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T17:57:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [thaianh20021/fisheye-fusion-lab](https://github.com/thaianh20021/fisheye-fusion-lab)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:57:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pinhole and multi-camera fisheye fusion with LiDAR-assisted 3D Gaussian Splatting and KITTI-360 Colab training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thaianh20021/fisheye-fusion-lab

### [Benevision/SplatWork](https://github.com/Benevision/SplatWork)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:51:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Make, train, view and edit 3D Gaussian splats on your own Mac, iPhone and Linux GPU machines — native Metal trainer and renderer, CUDA worker, multi-device block training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Benevision/SplatWork

### [xmdcv/LeanGS](https://github.com/xmdcv/LeanGS)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:19:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** LeanGS: Compact 3D Gaussian Splatting with Attention-Weighted Pruning and Factored View-Dependent Color | ACM Multimedia 2026
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xmdcv/LeanGS

### [dinanirham/efficient-3dgs-for-underwater](https://github.com/dinanirham/efficient-3dgs-for-underwater)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T02:07:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research code for efficient underwater novel-view synthesis using 3D Gaussian Splatting. Extends SeaSplat with dense correspondence initialization, importance-based population simplification, and attribute vector quantization, and evaluates the storage–fidelity trade-off on SeaThru-NeRF.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dinanirham/efficient-3dgs-for-underwater

### [nixliuxin/Awesome-Gaussian-Splatting-Artists](https://github.com/nixliuxin/Awesome-Gaussian-Splatting-Artists)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T09:28:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Curated gallery of the world's best Gaussian Splatting, NeRF & 3D/4D capture artists. The Volumography movement.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nixliuxin/Awesome-Gaussian-Splatting-Artists

### [pareekshit28/person-to-4dgs](https://github.com/pareekshit28/person-to-4dgs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:22:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** RunPod UI for monocular human video to animated 4D Gaussian Splatting with 4DAnyone and FreeTimeGS.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pareekshit28/person-to-4dgs

### [Huangsir12/3D-model-skill](https://github.com/Huangsir12/3D-model-skill)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:26:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 将2～30张静态场景照片重建为3D Gaussian Splatting（3DGS），输出PLY、SOG、SPZ、独立HTML查看器、预览视频和质量报告。用于用户提出“几张图转3D高斯／3DGS”、“照片重建样板间、商品、店铺或小型场景”、“调用GPU重建API”、“检查3DGS重建输入或结果”时。支持AnySplat少图预览与后优化、COLMAP＋gsplat高质量后端。不要用于承诺照片未覆盖区域、精确测量、CAD／BIM、可制造模型或动态4D重建。 ---
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Huangsir12/3D-model-skill

### [jo-chemla/3dtiled-to-3dtiles](https://github.com/jo-chemla/3dtiled-to-3dtiles)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:09:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [dingZvel/cp4282-3dgs-compaction](https://github.com/dingZvel/cp4282-3dgs-compaction)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:39:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dingZvel/cp4282-3dgs-compaction

### [Khriis-K/Fidelis](https://github.com/Khriis-K/Fidelis)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T01:00:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Multifidelity Reliability Estimation for Vision-Based Planetary Navigation: estimating the probability of navigation failure during simulated Martian descent using Gaussian splatting and uncertainty quantification.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Khriis-K/Fidelis

### [MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging](https://arxiv.org/abs/2509.16806v5)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-12T18:27:15Z
- **更新判定：** 实质修订
- **核心内容：** Multi-modal three-dimensional (3D) medical imaging data, derived from ultrasound, magnetic resonance imaging (MRI), and computed tomography (CT), provide a widely adopted approach for non-invasive anatomical visualization. However, accurate modeling depends on surface reconstruction and frame-to-frame interpolation, where traditional methods often struggle with image noise and incomplete information between sparse frames. To address these challenges, we present \our{}, a novel framework based on Gaussian Splatting (GS) designed for high-fidelity 3D anatomical reconstruction. Uniquely, \our{} employs a multi-task architecture that simultaneously performs frame interpolation and segmentation using a unified geometric representation. By coupling these tasks, the model leverages dense signals from image synthesis to regularize the geometry, enabling high-quality surface extraction even from a limited number of input frames. Specifically, medical data are modeled as Folded-Gaussians with d…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2509.16806v5

### [fenghuayumo/photara-studio](https://github.com/fenghuayumo/photara-studio)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:18:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** a powerful and efficient 3d spatial capture tool , video/image to splat to mesh ,cross-vendor, Vulkan or CUDA
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fenghuayumo/photara-studio

### [zxn2023/GeoPE-GS](https://github.com/zxn2023/GeoPE-GS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T04:00:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for GeoPE-GS: Geometry-Conditioned Pseudo-Enhancement for Low-Light 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zxn2023/GeoPE-GS

### [timfennell/vintage-click](https://github.com/timfennell/vintage-click)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T00:21:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 1970s 35 mm SLR photography game inside 3D Gaussian splat scans, for Apple silicon Macs. Lens optics made by the renderer, film stocks, tungsten lighting, a light table and loupe.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timfennell/vintage-click

### [cameornh/bardo](https://github.com/cameornh/bardo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T05:27:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A gaussian splatting / sdf physics sandbox
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cameornh/bardo

### [M-stars/Splat2Play](https://github.com/M-stars/Splat2Play)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T09:11:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 扫描现实,即刻可玩——把真实世界的 3DGS 扫描变成 Unity 里可玩的关卡:碰撞代理生成、NavMesh 桥接、近似动态光照、分块流送。(实境入戏 Splat2Play)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/M-stars/Splat2Play

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:47:53Z
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
- **发布时间/更新时间：** 2026-11-13T00:12:01Z
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
- **发布时间/更新时间：** 2026-11-13T08:26:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [enhansome/enhansome-NeRF-and-3DGS-SLAM](https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:26:21Z
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
- **发布时间/更新时间：** 2026-11-13T02:17:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Reconstruction of UCLA Gateway Plaza from unstaged outdoor scene video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS

### [Kishore-suthersingh/3dgs-digital-twin](https://github.com/Kishore-suthersingh/3dgs-digital-twin)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:54:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Phone video -> COLMAP -> 3D Gaussian Splatting -> cleaned, web-viewable digital twin. Built on free Colab GPUs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kishore-suthersingh/3dgs-digital-twin

### [Oasis-spaces/OasisSpaces](https://github.com/Oasis-spaces/OasisSpaces)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T05:21:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Film a room, get an editable 3D model and a Gaussian splat: COLMAP + MoGe-2 + SAM 2.1 + Blender + OpenSplat, checked stage by stage by Claude
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Oasis-spaces/OasisSpaces

### [sudhanvad18/SpatialBuild](https://github.com/sudhanvad18/SpatialBuild)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T04:02:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Voice-guided room editing and Gaussian splat reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sudhanvad18/SpatialBuild

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:13:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [huitailang2001/RSP-GS](https://github.com/huitailang2001/RSP-GS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T02:48:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Regional Structure Prior-Guided Gaussian Splatting for Urban Scene Reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/huitailang2001/RSP-GS

### [khanhhuyen-ops/3dgs-reconstruction](https://github.com/khanhhuyen-ops/3dgs-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T13:30:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/khanhhuyen-ops/3dgs-reconstruction

### [cvlab-uos/ViewSplat](https://github.com/cvlab-uos/ViewSplat)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:06:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [ECCV 2026] ViewSplat: View-Adaptive 3D Gaussian Splatting for Feed-Forward Synthesis
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cvlab-uos/ViewSplat

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:39:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/GaussianSplattingWorkbench

### [satyaba/gaussian-splatting](https://github.com/satyaba/gaussian-splatting)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T16:22:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SGDense-3DGS: segmentation-guided density control of 3D Gaussian Splatting (thesis work)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/satyaba/gaussian-splatting

### [playcanvas/supersplat v3.8.1](https://github.com/playcanvas/supersplat/releases/tag/v3.8.1)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-12T14:45:06Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Name ?load= URL imports by their supplied filename by @slimbuck in https://github.com/playcanvas/supersplat/pull/1101 * docs: point coding agents at the llms.txt indexes by @willeastcott in https://github.com/playcanvas/supersplat/pull/1102 * Read true opacity from splat-transform and draw alpha above 1, update dependencies by @slimbuck in https://github.com/playcanvas/supersplat/pull/1103 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.8.0...v3.8.1
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:45:48Z
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
- **发布时间/更新时间：** 2026-11-13T02:13:06Z
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
- **发布时间/更新时间：** 2026-11-12T14:03:57Z
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
- **发布时间/更新时间：** 2026-11-13T02:26:26Z
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
- **发布时间/更新时间：** 2026-11-13T04:43:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [WilliamLiu-1997/3dgs-renderer-bench](https://github.com/WilliamLiu-1997/3dgs-renderer-bench)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T23:25:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting renderer benchmark: Spark, SuperSplat and Gaussian Splat Lite, with reproducible measurements and an interactive report
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/3dgs-renderer-bench

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T17:21:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [docie-rgb/bikeshare-station-3d](https://github.com/docie-rgb/bikeshare-station-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T08:15:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 서울 공공자전거 대여소 3D 복원 뷰어 (MapAnything + Gaussian Splat + Spark)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/docie-rgb/bikeshare-station-3d

### [jsseo0420/naebang-3d](https://github.com/jsseo0420/naebang-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:42:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splat viewer (three.js + Spark)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jsseo0420/naebang-3d

### [MultiDarkZen/BlueSplat](https://github.com/MultiDarkZen/BlueSplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:02:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is an open-source UI I dubbed BlueSplat, built for OpenSplat an open source gaussian splatting program.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MultiDarkZen/BlueSplat

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T06:55:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T06:38:25Z
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
- **发布时间/更新时间：** 2026-11-13T05:25:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows toolkit for Apple SHARP Gaussian Splatting, Quest WebXR preview, and YouTube VR video workflows.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shimansKim/sharp-gaussian-splatting-vr-toolkit

### [eduardoabreu81/idol-forge-neo](https://github.com/eduardoabreu81/idol-forge-neo)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:14:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Turn one picture into a 3D Gaussian splat with Idol inside Stable Diffusion WebUI Forge Neo: img2img, Idol Turbo, .ply, .spz and .glb export, and a 3D viewer.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/eduardoabreu81/idol-forge-neo

### [VladyslavDrahan/safe-at-home](https://github.com/VladyslavDrahan/safe-at-home)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T22:53:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Immersive fall-prevention learning experience for older adults: 3D Gaussian Splatting room, ML hazard detection, Unity Immersive Room
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/VladyslavDrahan/safe-at-home

### [ozten/3dgs-pixel-art](https://github.com/ozten/3dgs-pixel-art)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T17:44:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ozten/3dgs-pixel-art

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T09:03:44Z
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
- **发布时间/更新时间：** 2026-11-12T18:44:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/simontheuseful/gpu-pro26-3dgs

### [willeastcott/splat-fashion](https://github.com/willeastcott/splat-fashion)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T21:21:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The future of clothes shopping: captured outfits as Gaussian splats, rigged, labelled and morphing from one look to the next. Built with PlayCanvas.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/willeastcott/splat-fashion

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T14:53:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official LichtFeld Studio Blender Plugin
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [caiyuanhao1998/X-Gaussian](https://github.com/caiyuanhao1998/X-Gaussian)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T00:42:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** "Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis" (ECCV 2024)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/X-Gaussian

### [3.8.1](https://github.com/playcanvas/supersplat/commit/919f0e5d60a94470ed8ebcbc7353a29d0a4344f0)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-12T14:44:24Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.8.1
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T11:44:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [pgodlews/OSVplat](https://github.com/pgodlews/OSVplat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T23:04:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Raw DJI .OSV dual-fisheye → Gaussian splat. No stitch.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pgodlews/OSVplat

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T03:10:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** OpenUSD file format and schema plugins for 3D Gaussian Splatting assets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/usd-3dgs-plugins

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T09:53:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [SalisLv/FAST-LIVO2-RTK-Global-BA-3DGS](https://github.com/SalisLv/FAST-LIVO2-RTK-Global-BA-3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:58:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** FAST-LIVO2+RTK+BA+3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SalisLv/FAST-LIVO2-RTK-Global-BA-3DGS

### [Tzy18171202912/3DGS-Cropper-1.1.0](https://github.com/Tzy18171202912/3DGS-Cropper-1.1.0)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:45:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Tzy18171202912/3DGS-Cropper-1.1.0

### [xktkf147/room-3d-scene](https://github.com/xktkf147/room-3d-scene)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:35:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splat scene from a phone video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xktkf147/room-3d-scene

### [ChenHongshan333/cp4282-project](https://github.com/ChenHongshan333/cp4282-project)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T07:20:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is the repo for CS4282 (3D Gaussian Splatting, AY26/27 sem2), individual project
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ChenHongshan333/cp4282-project

### [cs184-fa26-gaussiansplatting/final-project-proposal](https://github.com/cs184-fa26-gaussiansplatting/final-project-proposal)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-13T06:09:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CS184 Final Project Proposal - 2D to 3D Gaussian Splatting pipeline
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cs184-fa26-gaussiansplatting/final-project-proposal

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T18:35:40Z
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
- **发布时间/更新时间：** 2026-11-12T16:55:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/5undura/3DGS

### [SileSnow/3DGS-UE5-AIdriven](https://github.com/SileSnow/3DGS-UE5-AIdriven)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T14:58:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SileSnow/3DGS-UE5-AIdriven

### [TitanothereYik/votion-3dgs-2-html](https://github.com/TitanothereYik/votion-3dgs-2-html)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-12T09:39:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Votion 3DGS 2.0 clickable HTML dummy UI
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/TitanothereYik/votion-3dgs-2-html

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 5 |
| GitHub | ok: 69 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 5/5 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

