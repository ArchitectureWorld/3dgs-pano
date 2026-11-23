---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-22T09:10:19Z
window_end_utc: 2026-11-23T10:05:36Z
generated_at_utc: 2026-11-23T10:05:36Z
item_count: 62
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-23

**统计窗口：** 2026-11-22T09:10:19Z — 2026-11-23T10:05:36Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **62** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **62** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Implement SnugBox and AccuTile tile intersection rendering (#512) * Find a splat's tiles per row, not per tile Counting and emitting a splat's tiles tested every tile in its bbox against the ellipse. Work out the exact column range per tile row instead (the idea behind AccuTile in Speedy-Splat), from one helper both kernels share. Same tiles as before, so renders are unchanged. Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain> * Bump url to 2.5.9 for RUSTSEC-2026-0592 --------- Co-authored-by: Arthur Brussee <arthur.brussee@gmail.com> Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain>](https://github.com/ArthurBrussee/brush/commit/94ee1d8fdf540fcb2eae984ac993d9699cf6594b) | 代码实质更新 | GitHub · ArthurBrussee/brush | E2 | P2 |
| 2 | [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 3 | [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [MooreThreads/LiteGS](https://github.com/MooreThreads/LiteGS) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [MooreThreads/LiteGS](https://github.com/MooreThreads/LiteGS)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T06:51:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A refactored codebase for Gaussian Splatting. Training 3DGS in 50 seconds!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MooreThreads/LiteGS

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T00:12:35Z
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
- **发布时间/更新时间：** 2026-11-22T23:19:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [KashyapRajpal/Sabercat](https://github.com/KashyapRajpal/Sabercat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:16:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Render, train and relight 3D Gaussian splats on the GPU. Differentiable Vulkan engine with ray-traced shadows, a C ABI, a viewer and an editor.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KashyapRajpal/Sabercat

### [hazardcookie/splat-to-unreal](https://github.com/hazardcookie/splat-to-unreal)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T05:31:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photo registration, Gaussian splat training and viewing, and Blender-to-Unreal scene tools.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hazardcookie/splat-to-unreal

### [ryamabra/spatial-4d-gaussian-viewer](https://github.com/ryamabra/spatial-4d-gaussian-viewer)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:31:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Experimental 4D Gaussian splatting pipeline and local viewer with independent camera and time navigation
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ryamabra/spatial-4d-gaussian-viewer

### [ferdinandl007/PrismSplat](https://github.com/ferdinandl007/PrismSplat)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T16:31:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Metal and Swift renderer for 3D Gaussian splats and 4D Gaussian splat video on Apple Vision Pro, macOS, and iOS.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ferdinandl007/PrismSplat

### [zerokhong1/gs4d_viewer](https://github.com/zerokhong1/gs4d_viewer)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T09:32:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Browser viewer (viser) for 4D Gaussian Splatting results with a time slider
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zerokhong1/gs4d_viewer

### [liming0724/Auto-RTL-4DGS-EDA](https://github.com/liming0724/Auto-RTL-4DGS-EDA)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T05:38:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Algorithm-Hardware Co-Design & Automated Formal Verification Framework targeting 4D Gaussian Splatting (4DGS) hardware acceleration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/liming0724/Auto-RTL-4DGS-EDA

### [CooperAndy/Semantic-Dynamic-3DGS-SLAM](https://github.com/CooperAndy/Semantic-Dynamic-3DGS-SLAM)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T14:26:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Source code and experiment configurations for Semantic Dynamic 3DGS-SLAM for Autonomous Driving.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CooperAndy/Semantic-Dynamic-3DGS-SLAM

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:40:37Z
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
- **发布时间/更新时间：** 2026-11-23T02:25:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a 3DGS(3D Gaussian Splatting) viewer built on Three.js, with features for marking, measurements, preset-lod rendering, etc.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reall3d-com/Reall3dViewer

### [nff747/hyper-splat-engine](https://github.com/nff747/hyper-splat-engine)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T01:17:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zero-copy, virtualized WebGPU 3D Gaussian Splatting and spatial AI engine with distance LoD tile streaming and proactive VRAM paging.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nff747/hyper-splat-engine

### [animu-sphere/hydra-merlin](https://github.com/animu-sphere/hydra-merlin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T10:03:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A lightweight, host-neutral raster renderer for USD Hydra, powered by Vulkan and Metal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/hydra-merlin

### [keinnyne000/3DGS-vector-quantization-selection](https://github.com/keinnyne000/3DGS-vector-quantization-selection)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T22:21:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/keinnyne000/3DGS-vector-quantization-selection

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T03:36:57Z
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
- **发布时间/更新时间：** 2026-11-23T10:00:58Z
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
- **发布时间/更新时间：** 2026-11-23T06:31:03Z
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
- **发布时间/更新时间：** 2026-11-23T08:09:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [ramonamathias/SceneForge-3DGS](https://github.com/ramonamathias/SceneForge-3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T15:44:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SceneForge is a 3D scene reconstruction platform that transforms real-world videos into immersive 3D scenes using computer vision and 3D Gaussian Splatting. It automates the complete pipeline from video processing and camera reconstruction to Gaussian Splatting and interactive 3D visualization.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ramonamathias/SceneForge-3DGS

### [M4A1TasteGood/ArgsWorld](https://github.com/M4A1TasteGood/ArgsWorld)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T19:54:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for "ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/M4A1TasteGood/ArgsWorld

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T04:21:19Z
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
- **发布时间/更新时间：** 2026-11-23T03:44:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [arthurlirui/AIRobotSim](https://github.com/arthurlirui/AIRobotSim)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T01:43:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS reconstruction-based robot swarm/comm/interaction research platform
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arthurlirui/AIRobotSim

### [timeDNAtime/S2A-GS](https://github.com/timeDNAtime/S2A-GS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T08:15:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a project on 3D reconstruction of ceramics based on an improved 3DGS method.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timeDNAtime/S2A-GS

### [KCBtheone/video-to-print-reconstruction](https://github.com/KCBtheone/video-to-print-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T08:06:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reconstruct printable 3D portraits from video with Gaussian splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KCBtheone/video-to-print-reconstruction

### [saiKelkar/Property_Splats](https://github.com/saiKelkar/Property_Splats)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:42:17Z
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
- **发布时间/更新时间：** 2026-11-23T03:05:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [khanhhuyen-ops/3dgs-reconstruction](https://github.com/khanhhuyen-ops/3dgs-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T14:23:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/khanhhuyen-ops/3dgs-reconstruction

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T11:00:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [Junostr05/Sparse-View-3D-Gaussian-Splatting-for-Mac](https://github.com/Junostr05/Sparse-View-3D-Gaussian-Splatting-for-Mac)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T03:03:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Sparse-View 3D Gaussian Splatting for Mac
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Junostr05/Sparse-View-3D-Gaussian-Splatting-for-Mac

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:26:45Z
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
- **发布时间/更新时间：** 2026-11-23T08:47:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SGDense-3DGS: segmentation-guided density control of 3D Gaussian Splatting (thesis work)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/satyaba/gaussian-splatting

### [Implement SnugBox and AccuTile tile intersection rendering (#512) * Find a splat's tiles per row, not per tile Counting and emitting a splat's tiles tested every tile in its bbox against the ellipse. Work out the exact column range per tile row instead (the idea behind AccuTile in Speedy-Splat), from one helper both kernels share. Same tiles as before, so renders are unchanged. Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain> * Bump url to 2.5.9 for RUSTSEC-2026-0592 --------- Co-authored-by: Arthur Brussee <arthur.brussee@gmail.com> Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain>](https://github.com/ArthurBrussee/brush/commit/94ee1d8fdf540fcb2eae984ac993d9699cf6594b)

- **主题：** 实时渲染与展示
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-22T14:08:09Z
- **更新判定：** 代码实质更新
- **核心内容：** Implement SnugBox and AccuTile tile intersection rendering (#512) * Find a splat's tiles per row, not per tile Counting and emitting a splat's tiles tested every tile in its bbox against the ellipse. Work out the exact column range per tile row instead (the idea behind AccuTile in Speedy-Splat), from one helper both kernels share. Same tiles as before, so renders are unchanged. Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain> * Bump url to 2.5.9 for RUSTSEC-2026-0592 --------- Co-authored-by: Arthur Brussee <arthur.brussee@gmail.com> Co-authored-by: damanimc <dxm21@DESKTOP-61QNAKE.localdomain>
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:27:12Z
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
- **发布时间/更新时间：** 2026-11-23T02:16:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source web graphics engine built on WebGPU and WebGL2
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [Bump Rust to 1.100, rerun, glam and CI actions (#566) * Bump actions/checkout to v7 and cache-apt-pkgs-action to 1.6.3 * Bump Rust to 1.100, rerun to 0.43 and glam to 0.33 glam 0.33 needs a rerun that needs a newer Rust, so the three go together. The rest is what the new clippy and cargo lints asked for. * Use assert_matches! and cargo's build.warnings build.warnings also turns cargo's unused-dependency check into an error, so test-only dependencies move to dev-dependencies.](https://github.com/ArthurBrussee/brush/commit/d43bd1e6b232c4d85112bdf7ad1c317b3973915e)

- **主题：** 实时渲染与展示
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-22T15:18:39Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump Rust to 1.100, rerun, glam and CI actions (#566) * Bump actions/checkout to v7 and cache-apt-pkgs-action to 1.6.3 * Bump Rust to 1.100, rerun to 0.43 and glam to 0.33 glam 0.33 needs a rerun that needs a newer Rust, so the three go together. The rest is what the new clippy and cargo lints asked for. * Use assert_matches! and cargo's build.warnings build.warnings also turns cargo's unused-dependency check into an error, so test-only dependencies move to dev-dependencies.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [AaronNZH/LeGS](https://github.com/AaronNZH/LeGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T05:29:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [ICML 2026] Beyond Heuristics: Learnable Density Control for 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AaronNZH/LeGS

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T16:00:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [kubus-project/kubus-node](https://github.com/kubus-project/kubus-node)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T09:07:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Local Gaussian splatting + IPFS spatial archive node for art.kubus. Process spatial captures on your own GPU, use distributed GPU compute, and contribute storage to a decentralised public art network.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kubus-project/kubus-node

### [ZaychikLiu/tpu-rtx](https://github.com/ZaychikLiu/tpu-rtx)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T06:02:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** TPU-RTX: Zero-Copy RTX-Class Ray Tracing, Multi-Bounce Path Tracing, 3DGS, OpenUSD/Blender Compiler & Physical AI Rendering natively on Google Cloud TPU v5p
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZaychikLiu/tpu-rtx

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T00:02:47Z
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
- **发布时间/更新时间：** 2026-11-22T09:10:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [shlee929/virtual-village](https://github.com/shlee929/virtual-village)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T09:37:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Virtual village: 360/3DGS learning tour for Nepali Grade 2 (Tharu -> Nepali)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shlee929/virtual-village

### [zyhchn/learn-3dgs](https://github.com/zyhchn/learn-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T09:05:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zyhchn/learn-3dgs

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T08:22:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [abhi1kumar/qonvolution](https://github.com/abhi1kumar/qonvolution)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T05:08:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [2027 Submission] Beyond Primitive Bloat: High-Fidelity Gaussian Splatting with Coordinate-Convolution Neural Network
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/abhi1kumar/qonvolution

### [GenshinStar/spatial-airdrop](https://github.com/GenshinStar/spatial-airdrop)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T02:57:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 把照片变成可用手势探索的 3D 粒子空间。Local 3D Gaussian Splatting with hand gestures, particle effects and head-tracked parallax. Windows + macOS.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/GenshinStar/spatial-airdrop

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T02:47:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Goldwaterfung/apple_3dgs](https://github.com/Goldwaterfung/apple_3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T02:20:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is an independent learning repository created to study and reproduce synthetic 3D data workflows from Apple's 3D Gaussian Splatting research papers.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Goldwaterfung/apple_3dgs

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T17:40:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [AlinaLuuu/ascend-3dgs-viewer](https://github.com/AlinaLuuu/ascend-3dgs-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T14:01:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 昇腾 NPU 3D Gaussian Splatting 查看器：原生渲染、可调参数与稠密化对比。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AlinaLuuu/ascend-3dgs-viewer

### [yang498-Peter/cloudstudio-3dgs](https://github.com/yang498-Peter/cloudstudio-3dgs)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T06:31:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source 3D Gaussian Splatting pipeline for MVP S1 scan data
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yang498-Peter/cloudstudio-3dgs

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T07:26:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [DonghoLEE-CV/3dgs-sibr-analyzer](https://github.com/DonghoLEE-CV/3dgs-sibr-analyzer)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T08:23:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Analysis tool for 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DonghoLEE-CV/3dgs-sibr-analyzer

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T09:51:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [wook-exe/3DGS](https://github.com/wook-exe/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T06:24:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wook-exe/3DGS

### [Hauwoong/metaverse-map-bridging](https://github.com/Hauwoong/metaverse-map-bridging)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T04:18:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 끝점 조건 영상 생성으로 실사 3DGS 조각 맵 사이를 잇는 파이프라인 (메타버스컴퓨팅 기말 프로젝트)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Hauwoong/metaverse-map-bridging

### [aditano/tesla-dashcam-splat](https://github.com/aditano/tesla-dashcam-splat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-23T03:59:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Drop Tesla dashcam clips in your browser, read the SEI telemetry, and view the drive as a 3D Gaussian Splat scene.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aditano/tesla-dashcam-splat

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T18:01:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [Realkai1221/3DGS-with-Exposure-Compensation](https://github.com/Realkai1221/3DGS-with-Exposure-Compensation)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T15:23:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Realkai1221/3DGS-with-Exposure-Compensation

### [SileSnow/3DGS-UE5-AIdriven](https://github.com/SileSnow/3DGS-UE5-AIdriven)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T11:41:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SileSnow/3DGS-UE5-AIdriven

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 0 |
| GitHub | ok: 62 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 0 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

