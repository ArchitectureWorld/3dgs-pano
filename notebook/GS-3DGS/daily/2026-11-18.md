---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-17T09:58:05Z
window_end_utc: 2026-11-18T09:35:19Z
generated_at_utc: 2026-11-18T09:35:19Z
item_count: 84
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-18

**统计窗口：** 2026-11-17T09:58:05Z — 2026-11-18T09:35:19Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **84** 项去重后的有效线索：真正新增论文 **5** 项、实质论文修订 **2** 项、代码/版本/项目更新 **77** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting](https://arxiv.org/abs/2611.22805v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2611.23054v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [You Only Encode Once: Sub-Pixel-Shifted Frames for Arbitrary-Scale Remote Sensing Super-Resolution with 2D Gaussian Splatting](https://arxiv.org/abs/2611.22898v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [GaussianMamba: Geometric and Relational State Space Scanning of 3D Gaussian Primitives](https://arxiv.org/abs/2611.22742v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](https://arxiv.org/abs/2611.22691v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting](https://arxiv.org/abs/2611.22805v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T14:00:20Z
- **更新判定：** 真正新增
- **核心内容：** Traditional Gaussian Splatting (GS) methods use in-core training, i.e. assuming that GPU memory is large enough to accommodate all the primitives. This assumption breaks down when the primitives exceed the capacity of GPU memory, e.g. GS on large environments. Recent out-of-core training research starts to address this issue, but is limited to static scenes. Unlike static GS, dynamic GS primitives move in space and time, breaking common assumptions held in existing out-of-core research and impose new challenges in memory management and training. To this end, we propose Dynamic Out-of-core Optimization for Massive Gaussian Splatting (DOOM-GS), the first out-of-core optimization method designed specifically for massive-scale dynamic GS. DOOM-GS is equipped with novel memory management strategies that optimize caching for spatio-temporal primitives, and a fast learning method for large numbers of primitives. Due to the lack of suitable datasets for large-scale dynamic GS, we also contrib…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.22805v1

### [ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2611.23054v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T16:47:43Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) enables photorealistic scene reconstruction. Existing 3DGS color transfer and interactive editing methods are guided by reference images and user-specified color adjustments. However, in many applications, users simply want aesthetically guided color enhancement that automatically makes the scene more visually appealing while maintaining consistent colors and tones across viewpoints. We present ReTouchGS, to our knowledge the first framework for reference-free aesthetic color enhancement of pretrained 3DGS models. It predicts a scene-level color lookup table (LUT) from the model and its associated camera parameters. ReTouchGS also supports reference-guided color transfer by fitting a scene-level LUT using one edited view of the same scene and its corresponding original render. A shared blend-aware color refinement network with only 44.7K parameters refines an analytic color update to realize either color mapping without rendering. It preserves geometry and…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.23054v1

### [You Only Encode Once: Sub-Pixel-Shifted Frames for Arbitrary-Scale Remote Sensing Super-Resolution with 2D Gaussian Splatting](https://arxiv.org/abs/2611.22898v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T15:05:58Z
- **更新判定：** 真正新增
- **核心内容：** Arbitrary-scale super-resolution (ASSR) of remote sensing images remains challenging due to the limited high-frequency information in a single low-resolution (LR) observation. While multi-frame SR can exploit complementary sub-pixel information, existing approaches often require real multi-frame training sequences and repeated feature encoding, increasing data acquisition demands and computational costs. To address these limitations, we propose SPS-GS (Sub-Pixel-Shifted Gaussian Splatting), an encode-once framework that learns from multi-phase LR observations synthesized from individual high-resolution images, without requiring real multi-frame training sequences. Specifically, Phase-Coherent Aliasing Demodulation (PCAD) exploits shift-dependent aliasing through Fourier-based alignment, phase-aware residual fusion, and least-squares aliasing estimation, enabling multi-frame information to be integrated before a single deep encoding pass. Gaussian Projection Alignment (GPA) then iterat…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.22898v1

### [Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](https://arxiv.org/abs/2611.22691v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T12:39:42Z
- **更新判定：** 真正新增
- **核心内容：** World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and the ego visual observations. We propose a closed-loop interactive WM that couples behavior modeling and visual rendering. First, imitation-learned background-vehicle (BV) policies are fine-tuned with multi-agent reinforcement learning in the closed loop against an end-to-end ego planner that reacts to the rendered images, so that their interaction behaviors match those in real logs. Second, the viewpoints exposed by these interactions guide a per-Gaussian diagnosis of each 3D Gaussian vehicle asset, which attenuates view-dependent colors on under-observed Gaussians and fills never-observed surfaces with generated Gaussians, while preserving the observed appearance. Third, sig…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.22691v1

### [SSA-3DGS: Unsupervised Removal of Screen-Space Artifacts for 3D Gaussian Splatting](https://arxiv.org/abs/2607.05598v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T11:17:07Z
- **更新判定：** 实质修订
- **核心内容：** Novel View Synthesis (NVS) methods, such as 3D Gaussian Splatting (3DGS), rely on the assumption of clean, multi-view consistent, posed input images. Real-world captures can violate this assumption due to \textbf{screen-space artifacts}---static occlusions fixed to the 2D image plane rather than to the 3D world. Common examples include physical sensor defects, environmental obstructions (such as rain or mud on the lens enclosure), capture obstructions (such as a thumb over the camera sensor or a dashboard visible in dashcam footage), and digital overlays (such as watermarks or UI elements). When present, they are erroneously baked into the 3D geometry as ``floaters'' or near-camera artifacts, degrading the quality of novel-view rendering. In this work, we propose \textit{SSA-3DGS}, an unsupervised framework that jointly optimizes a 3D scene and a learnable 2D overlay to recover a clean 3D scene and the corrupting artifacts. By exploiting geometric consensus across views, our method ef…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2607.05598v3

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T07:32:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Train, inspect, edit, automate, and export 3D Gaussian Splatting scenes from a single native application.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/LichtFeld-Studio

### [Benevision/SplatWork](https://github.com/Benevision/SplatWork)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:21:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Make, train, view and edit 3D Gaussian splats on your own Mac, iPhone and Linux GPU machines — native Metal trainer and renderer, CUDA worker, multi-device block training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Benevision/SplatWork

### [fabianfreund/SplatCraft](https://github.com/fabianfreund/SplatCraft)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:33:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-platform Gaussian Splatting studio: drop photos/videos, align, train with live preview, export. Plugin-based, non-destructive.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fabianfreund/SplatCraft

### [KuoFengYuan/prior-pose-refine](https://github.com/KuoFengYuan/prior-pose-refine)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:07:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Refine prior camera poses, focal length and lens distortion with COLMAP, and prepare a metric 3DGS training dataset.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KuoFengYuan/prior-pose-refine

### [kali23041/3d-gsplat](https://github.com/kali23041/3d-gsplat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T06:58:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Web portal for a Gaussian Splatting 2D-to-3D reconstruction project: Firebase auth with user/admin roles, project uploads, training and quality dashboards. React + Vite.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kali23041/3d-gsplat

### [asdfut/eb-floor2-gaussian-splatting](https://github.com/asdfut/eb-floor2-gaussian-splatting)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T03:50:50Z
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
- **发布时间/更新时间：** 2026-11-18T02:24:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pinhole and multi-camera fisheye fusion with LiDAR-assisted 3D Gaussian Splatting and KITTI-360 Colab training.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thaianh20021/fisheye-fusion-lab

### [gardner-luke/synthgen-3d](https://github.com/gardner-luke/synthgen-3d)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T01:30:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** One photo of a part to a 3D Gaussian splat, a labeled synthetic dataset and a trained YOLO detector on Databricks (serverless GPU, Unity Catalog, MLflow, AppKit)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gardner-luke/synthgen-3d

### [caiyuanhao1998/HDR-GS](https://github.com/caiyuanhao1998/HDR-GS)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:53:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** "HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting" (NeurIPS 2024)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/HDR-GS

### [solipsist-studios/cumuli](https://github.com/solipsist-studios/cumuli)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T03:40:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 4D volumetric human capture pipeline: GoPro footage → Camera pose estimation → Diffuman4D → Brush 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli

### [nixliuxin/Awesome-Gaussian-Splatting-Artists](https://github.com/nixliuxin/Awesome-Gaussian-Splatting-Artists)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T03:55:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Curated gallery of the world's best Gaussian Splatting, NeRF & 3D/4D capture artists. The Volumography movement.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nixliuxin/Awesome-Gaussian-Splatting-Artists

### [AtlantixJJ/ARG-Avatar](https://github.com/AtlantixJJ/ARG-Avatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:07:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The code release of the ARG-Avatar paper.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AtlantixJJ/ARG-Avatar

### [USTC-iVC-3D-Group/HPC](https://github.com/USTC-iVC-3D-Group/HPC)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T07:38:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [TCSVT 2026] HPC: Hierarchical Point-based Latent Representation for Streaming Dynamic Gaussian Splatting Compression
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/USTC-iVC-3D-Group/HPC

### [sanditya12/4d-construction-site-monitoring](https://github.com/sanditya12/4d-construction-site-monitoring)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T00:15:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repo turns photos of a construction site and reconstruct it into a 3D Gaussian Splat Reconstuction. This process is repeated over time and can be aligned, which enables 4D Monitoring (Spatiotemporal Understanding).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sanditya12/4d-construction-site-monitoring

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:34:47Z
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
- **发布时间/更新时间：** 2026-11-18T01:21:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [IRIS-LAB-whu/SemLite-GS](https://github.com/IRIS-LAB-whu/SemLite-GS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T02:05:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IRIS-LAB-whu/SemLite-GS

### [sivan7zZ/3DGS-COMPRESSION](https://github.com/sivan7zZ/3DGS-COMPRESSION)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T02:43:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sivan7zZ/3DGS-COMPRESSION

### [GaussianMamba: Geometric and Relational State Space Scanning of 3D Gaussian Primitives](https://arxiv.org/abs/2611.22742v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T13:11:52Z
- **更新判定：** 真正新增
- **核心内容：** 3D semantic occupancy prediction requires representing complex spatial structures and modeling contextual relationships across a scene. 3D Gaussian primitives provide a sparse and adaptive representation of scene geometry and semantics, while Mamba offers efficient sequence modeling for capturing dependencies among primitives. However, Gaussian primitives are irregular and unordered, making sequence construction challenging, as conventional spatial ordering may overlook their anisotropic geometry and feature-semantic relationships. In this paper, we present GaussianMamba, a dual-branch Mamba framework that explicitly incorporates Gaussian-specific geometric and feature-semantic relationships into complementary scanning strategies. The first branch refines a locality-preserving traversal using anisotropic Gaussian support derived from primitive scale and orientation. The second branch reorders spatially organized groups according to feature-semantic affinity and adjusts local features…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.22742v1

### [Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679v3)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-17T11:00:23Z
- **更新判定：** 实质修订
- **核心内容：** Mounted butterflies are among the most striking objects in natural history collections. However, their beauty is notoriously hard to digitize in 3D: they are small and fragile, with microscopic hairs and vein structures. Capturing them in sufficient detail, therefore, requires a macro lens, which has a very limited Depth of Field (DoF). Moreover, a camera body cannot be maneuvered beneath a pinned specimen to photograph its ventral surface. We introduce an end-to-end pipeline that resolves these challenges, turning such specimens into photorealistic 3D models viewable from every direction. It combines three ingredients: handheld focus stacking for all-in-focus macro capture without a tripod, a non-contact first-surface mirror system that exposes the ventral surface without touching the specimen, and a segmentation-free, mirror-aware 3D Gaussian Splatting extension. We validate the reconstructions and design decisions on nine diverse specimens.
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.31679v3

### [letmeshock-uae/street-wheel](https://github.com/letmeshock-uae/street-wheel)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T14:40:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Длинная 3DGS-улица, свёрнутая в колесо: скролл ведёт по кругу, детали собираются из частиц
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/letmeshock-uae/street-wheel

### [letmeshock-datum/street-wheel](https://github.com/letmeshock-datum/street-wheel)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T12:30:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Длинная 3DGS-улица, свёрнутая в колесо: скролл ведёт по кругу, детали собираются из частиц
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/letmeshock-datum/street-wheel

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T06:20:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A comprehensive list of Implicit Representations, NeRF and 3D Gaussian Splatting papers relating to SLAM/Robotics domain, including papers, videos, codes, and related websites
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T00:12:38Z
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
- **发布时间/更新时间：** 2026-11-18T09:05:23Z
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
- **发布时间/更新时间：** 2026-11-18T08:09:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Full-stack ROS 2 autonomous navigation: Nav2, SLAM Toolbox, RTAB-Map & ORB-SLAM3 VSLAM, Gazebo Harmonic, Docker, multi-robot fleet coordination, collaborative loop closure, coordinated frontier exploration, MPPI controller, behavior trees, waypoint following & Gaussian Splatting capture on Humble/Jazzy.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/darshmenon/rosnav

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T07:59:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [voyager-so/vauss](https://github.com/voyager-so/vauss)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:26:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Fast Gaussian splat reconstruction for Blender, agents, and reusable 3D worlds
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/voyager-so/vauss

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T04:53:09Z
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
- **发布时间/更新时间：** 2026-11-18T04:27:22Z
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
- **发布时间/更新时间：** 2026-11-18T03:06:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Huhu32321/stone-by-stone](https://github.com/Huhu32321/stone-by-stone)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T00:36:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Per-stone digital twin of a rubble masonry wall from handheld photos: SfM, 3D Gaussian Splatting, 3D stone segmentation and a clickable web viewer.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Huhu32321/stone-by-stone

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T11:41:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [Farida-gaber44/sparse-view-3dgs-ablation](https://github.com/Farida-gaber44/sparse-view-3dgs-ablation)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T21:38:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Farida-gaber44/sparse-view-3dgs-ablation

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:14:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/GaussianSplattingWorkbench

### [Neocvsu-commits/Blender-GSEditor](https://github.com/Neocvsu-commits/Blender-GSEditor)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T18:27:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Blender 5.3+ 高斯泼溅（3DGS）点云编辑插件：擦除、还原，以及吸附到表面的矩形面片覆盖
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Neocvsu-commits/Blender-GSEditor

### [xuannamservice-ui/Semantic-Aware](https://github.com/xuannamservice-ui/Semantic-Aware)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T14:22:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible pipeline and simulation data for Semantic-Aware Generative Error Concealment for Resilient Real-Time 3DGS over Turbulent FSO Backhaul
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xuannamservice-ui/Semantic-Aware

### [playcanvas/supersplat v3.9.0](https://github.com/playcanvas/supersplat/releases/tag/v3.9.0)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-17T17:35:53Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Review mixed multi-file imports, and make the drop target obvious by @slimbuck in https://github.com/playcanvas/supersplat/pull/1107 * Load GSAF files as timeline sequences, and play several sequences at once by @slimbuck in https://github.com/playcanvas/supersplat/pull/1108 * Undo MultiOp's ops in reverse order by @SwastikTripathi in https://github.com/playcanvas/supersplat/pull/1109 * Mode strip, shared toolbar vocabulary and markers that follow X-Ray by @slimbuck in https://github.com/playcanvas/supersplat/pull/1110 * Stop timeline playback on the last frame when loop is off by @SwastikTripathi in https://github.com/playcanvas/supersplat/pull/1111 ## New Contributors * @SwastikTripathi made their first contribution in https://github.com/playcanvas/supersplat/pull/1109 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.8.1...v3.9.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T02:15:37Z
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
- **发布时间/更新时间：** 2026-11-18T03:20:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Mode strip, shared toolbar vocabulary and markers that follow X-Ray (#1110)](https://github.com/playcanvas/supersplat/commit/30b5a42c6a90f46e4b698356a7b597290fb9fea1)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-17T15:26:19Z
- **更新判定：** 代码实质更新
- **核心内容：** Mode strip, shared toolbar vocabulary and markers that follow X-Ray (#1110)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Saqoosha/ghostline](https://github.com/Saqoosha/ghostline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T16:44:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Recover FPV flight paths from goggle DVR on a 3DGS scan, and replay them
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Saqoosha/ghostline

### [kyowon1108/gsplat-onthefly-nvs-study](https://github.com/kyowon1108/gsplat-onthefly-nvs-study)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T04:38:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting based real-time NVS research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kyowon1108/gsplat-onthefly-nvs-study

### [KBLLR/3dmodel-splats-stager](https://github.com/KBLLR/3dmodel-splats-stager)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T03:01:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A modern, high-performance 3D object stager specializing in Gaussian Splatting models, built with Three.js and Vite. This application enables advanced visualization of 3D models with sophisticated post-processing effects and real-time parameter adjustment.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KBLLR/3dmodel-splats-stager

### [QROST/aholo3d-rhino](https://github.com/QROST/aholo3d-rhino)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T02:32:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Aholo3D for Rhino: World and Lux3D creation, Gaussian splat viewing, USD exchange and cloud rendering.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/QROST/aholo3d-rhino

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T22:29:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [ldphu1/3dgs-low-vram](https://github.com/ldphu1/3dgs-low-vram)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:18:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ldphu1/3dgs-low-vram

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:17:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [willeastcott/gaussian-evil](https://github.com/willeastcott/gaussian-evil)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:14:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A Gaussian splat capture of two people, in the dark and the rain, relit in real time by a torch. A homage to the greatest horror game of all time. Built on PlayCanvas.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/willeastcott/gaussian-evil

### [LSUDOKO/ReRoom](https://github.com/LSUDOKO/ReRoom)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T09:11:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Scan it. Remix it. Live in it. Redesign your real room in 3D with AI furniture that opens, built on Aholo World, Lux3D and the Aholo Viewer.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LSUDOKO/ReRoom

### [leeyang1990/pixel-splat-game-assets-skill](https://github.com/leeyang1990/pixel-splat-game-assets-skill)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:57:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Codex skill and playable examples for reusable 3D pixel-art Gaussian splat game assets
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/leeyang1990/pixel-splat-game-assets-skill

### [skygaul/my-open-space-3d](https://github.com/skygaul/my-open-space-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T08:19:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Silver mirror statue 3D Gaussian splat viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/skygaul/my-open-space-3d

### [IQRAASGHAR1999/3dgs-garden-object-removal](https://github.com/IQRAASGHAR1999/3dgs-garden-object-removal)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T07:51:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IQRAASGHAR1999/3dgs-garden-object-removal

### [terranceh12/pixel-city-splat-test](https://github.com/terranceh12/pixel-city-splat-test)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T05:11:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3d gaussian splat pixel art
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/terranceh12/pixel-city-splat-test

### [Streetjk/landcros-forrestdale](https://github.com/Streetjk/landcros-forrestdale)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T04:47:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SiteNav 3D Gaussian Splat site viewer — Landcros Forrestdale demo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Streetjk/landcros-forrestdale

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T03:20:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VR/desktop player for openftgs models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs-xr

### [xibihe/garage-library-four-seasons](https://github.com/xibihe/garage-library-four-seasons)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T01:43:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An interactive Gaussian splat artwork by xibihe
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xibihe/garage-library-four-seasons

### [anandhupvr/SplatScope](https://github.com/anandhupvr/SplatScope)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T23:11:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Minimal 3D Gaussian Splatting Viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/anandhupvr/SplatScope

### [T-64/T-64](https://github.com/T-64/T-64)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T22:42:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zhaoqing Tan — ML & systems engineer. M.Sc. INFOTECH @ Uni Stuttgart. Ads serving, GPU inference (3DGS), LLM apps.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/T-64/T-64

### [kaclark219/controllable-npr-3dgs](https://github.com/kaclark219/controllable-npr-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T22:05:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kaclark219/controllable-npr-3dgs

### [JacksonTao888/cadfree-3dgs-part-recognition](https://github.com/JacksonTao888/cadfree-3dgs-part-recognition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T12:57:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JacksonTao888/cadfree-3dgs-part-recognition

### [amrutha206/NeRF-3DGS](https://github.com/amrutha206/NeRF-3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T12:29:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NeRF and 3D Gaussian Splatting Research Project
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/amrutha206/NeRF-3DGS

### [amrutha206/nerf-3dgs-research](https://github.com/amrutha206/nerf-3dgs-research)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T12:19:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NeRF and 3D Gaussian Splatting Research Project
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/amrutha206/nerf-3dgs-research

### [Azure-Samples/3DGS-accelerator](https://github.com/Azure-Samples/3DGS-accelerator)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T21:33:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Containerized Rust service for processing multi-view video captures into 3D Gaussian Splatting models - videos to splats
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Azure-Samples/3DGS-accelerator

### [lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11](https://github.com/lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T17:44:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 广工硕士中期检查全量材料：《动态环境下视觉语言模型辅助三维高斯语义建图与机器人目标导航》——26页答辩PPT(全页演讲者备注)+22页开题PPT+三件套表单+三端GPU实验(19次训练/可复跑/原始json)+近一年100篇文献能力矩阵差异分析
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lemonbaby2/vlm-3dgs-nav-thesis-midterm-2026-11

### [IshaanM05/blur-robust-3dgs](https://github.com/IshaanM05/blur-robust-3dgs)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T18:29:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CS 663 project: blur-robust 3D Gaussian Splatting via joint per-view blur-kernel estimation
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IshaanM05/blur-robust-3dgs

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T12:44:31Z
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
- **发布时间/更新时间：** 2026-11-17T22:53:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** "Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis" (ECCV 2024)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/X-Gaussian

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T11:28:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [3.9.0](https://github.com/playcanvas/supersplat/commit/8b6af56d0b589095b8ab56a1c52444c1f84582af)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-17T17:35:06Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.9.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Stop timeline playback on the last frame when loop is off (#1111)](https://github.com/playcanvas/supersplat/commit/b79a292b005cdccecdc8740b5cd5c11514104bb3)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-17T17:26:01Z
- **更新判定：** 代码实质更新
- **核心内容：** Stop timeline playback on the last frame when loop is off (#1111)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Suzukeh/3DGS_Su](https://github.com/Suzukeh/3DGS_Su)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T16:54:40Z
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
- **发布时间/更新时间：** 2026-11-18T02:45:09Z
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
- **发布时间/更新时间：** 2026-11-17T11:23:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [wzh-baby/3DGS](https://github.com/wzh-baby/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-18T06:41:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 用3DGS还原物体和场景
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wzh-baby/3DGS

### [Cryptilliumus/3dgs-site](https://github.com/Cryptilliumus/3dgs-site)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T20:29:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cryptilliumus/3dgs-site

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T19:23:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [xianMuuu/ExplorerGlobal](https://github.com/xianMuuu/ExplorerGlobal)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T13:36:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 探索全球 · ExplorerGlobal —— 国内可用的谷歌地球式三维数字地球（本地零依赖，双击启动）。以 3D 高斯建筑（3DGS）众包为核心愿景。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xianMuuu/ExplorerGlobal

### [Mugen3DDev/3dgs-interactive-visual-content](https://github.com/Mugen3DDev/3dgs-interactive-visual-content)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-17T11:11:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A technical perspective on 3D Gaussian Splatting for interactive visual
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mugen3DDev/3dgs-interactive-visual-content

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 7 |
| GitHub | ok: 77 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | degraded: ParseError: not well-formed (invalid token): line 1, column 41 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 7/7 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

