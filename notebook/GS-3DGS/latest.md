---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-20T09:29:59Z
window_end_utc: 2026-11-21T09:01:33Z
generated_at_utc: 2026-11-21T09:01:33Z
item_count: 58
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-21

**统计窗口：** 2026-11-20T09:29:59Z — 2026-11-21T09:01:33Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **58** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **58** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Use native CubeCL Metal for macOS training (#565) * Use native CubeCL Metal for macOS training Bumps burn to bb4d9ddd and picks cubecl's default device on macOS, which is the native Metal runtime when the GPU supports it and wgpu otherwise. Other platforms and the UI stay on wgpu. * Patch cubecl and fix brush-c link and cargo-deny for CI - Patch cubecl to a fork branch at burn's pinned rev, with fixes for the wasm build and an abort at exit on macOS. - brush-c: look up _mh_execute_header at load time, so the dylib links. - cargo-deny: skip the new duplicate crates, bump rustls/tokio/zstd past their advisories, ignore unmaintained chrono and humantime. * Bump cubecl fork: fall back to wgpu on GPUs without Metal 3](https://github.com/ArthurBrussee/brush/commit/4e4e1f169a5416431eb885fc7f33bd644e906e9d) | 代码实质更新 | GitHub · ArthurBrussee/brush | E2 | P1 |
| 2 | [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 3 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [Use native CubeCL Metal for macOS training (#565) * Use native CubeCL Metal for macOS training Bumps burn to bb4d9ddd and picks cubecl's default device on macOS, which is the native Metal runtime when the GPU supports it and wgpu otherwise. Other platforms and the UI stay on wgpu. * Patch cubecl and fix brush-c link and cargo-deny for CI - Patch cubecl to a fork branch at burn's pinned rev, with fixes for the wasm build and an abort at exit on macOS. - brush-c: look up _mh_execute_header at load time, so the dylib links. - cargo-deny: skip the new duplicate crates, bump rustls/tokio/zstd past their advisories, ignore unmaintained chrono and humantime. * Bump cubecl fork: fall back to wgpu on GPUs without Metal 3](https://github.com/ArthurBrussee/brush/commit/4e4e1f169a5416431eb885fc7f33bd644e906e9d)

- **主题：** 训练与优化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-21T09:00:00Z
- **更新判定：** 代码实质更新
- **核心内容：** Use native CubeCL Metal for macOS training (#565) * Use native CubeCL Metal for macOS training Bumps burn to bb4d9ddd and picks cubecl's default device on macOS, which is the native Metal runtime when the GPU supports it and wgpu otherwise. Other platforms and the UI stay on wgpu. * Patch cubecl and fix brush-c link and cargo-deny for CI - Patch cubecl to a fork branch at burn's pinned rev, with fixes for the wasm build and an abort at exit on macOS. - brush-c: look up _mh_execute_header at load time, so the dylib links. - cargo-deny: skip the new duplicate crates, bump rustls/tokio/zstd past their advisories, ignore unmaintained chrono and humantime. * Bump cubecl fork: fall back to wgpu on GPUs without Metal 3
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T00:39:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T22:11:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Train, inspect, edit, automate, and export 3D Gaussian Splatting scenes from a single native application.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/LichtFeld-Studio

### [ASU-NEM-Labs/open4dgs-core](https://github.com/ASU-NEM-Labs/open4dgs-core)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T01:15:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Tools for preparing synchronized multi-camera captures, initializing dynamic Gaussian scenes, and exporting 4D reconstructions. Companion to Open4DGS-Trigs.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ASU-NEM-Labs/open4dgs-core

### [CarlottaSeal/neural-rendering-cuda](https://github.com/CarlottaSeal/neural-rendering-cuda)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T07:38:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Neural rendering GPU kernels: optimized 3DGS rasterizer (sm_120), Instant-NGP and differentiable rasterization from scratch
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CarlottaSeal/neural-rendering-cuda

### [pouyasam1996/gaussian-slam](https://github.com/pouyasam1996/gaussian-slam)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T05:39:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SLAM with 3D Gaussian Splatting for training
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pouyasam1996/gaussian-slam

### [solipsist-studios/cumuli-trainer](https://github.com/solipsist-studios/cumuli-trainer)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T22:33:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 4D Gaussian splatting trainer for the Cumuli pipeline (PolyForm Noncommercial)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli-trainer

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T14:14:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting in Blender: train 3D Gaussian Splats from your Blender scene with LichtFeld Studio and import splats from the LichtFeld Portal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [gayan957/3dgs-capture-check](https://github.com/gayan957/3dgs-capture-check)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T10:11:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Predict 3D Gaussian Splatting quality before you train. Checks camera movement, scene coverage and frame overlap in under a minute, then says what to re-shoot.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gayan957/3dgs-capture-check

### [solipsist-studios/cumuli](https://github.com/solipsist-studios/cumuli)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T07:16:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 4D volumetric human capture pipeline: GoPro footage → Camera pose estimation → Diffuman4D → Brush 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli

### [frenchtouchXR/ithaca-4dgs-unity](https://github.com/frenchtouchXR/ithaca-4dgs-unity)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T00:25:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time 4D Gaussian Splatting rendering and asset generation for Unity (URP), with full 3DGS/4DGS compatibility. Fork of aras-p/UnityGaussianSplatting, extended with temporal playback support.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frenchtouchXR/ithaca-4dgs-unity

### [frenchtouchXR/ithaca-4dgs-js-player](https://github.com/frenchtouchXR/ithaca-4dgs-js-player)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T00:23:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Ithaca 4DGS JS player (WebGL2): ITHACA 4D Gaussian Splatting videos as three.js / A-Frame objects for WebXR scenes and metaverses. MIT.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frenchtouchXR/ithaca-4dgs-js-player

### [garrytheemancipator/B2B-Middleware-for-Dynamic-scenes-](https://github.com/garrytheemancipator/B2B-Middleware-for-Dynamic-scenes-)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T04:05:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A repo to render dynamic scenes through temporal 3D Gaussian Splatting techniques & product showcase as a B2B middleware
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/garrytheemancipator/B2B-Middleware-for-Dynamic-scenes-

### [publioelon/Q3DGStream](https://github.com/publioelon/Q3DGStream)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T02:29:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Saliency-Driven Adaptive Streaming of Dynamic 3D Gaussian Splatting over QUIC
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/publioelon/Q3DGStream

### [solipsist-studios/cumuli-core](https://github.com/solipsist-studios/cumuli-core)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T22:28:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Shared Python components of the Cumuli 4D Gaussian splatting stack: the 4D...
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli-core

### [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T07:58:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a 3DGS(3D Gaussian Splatting) viewer built on Three.js, with features for marking, measurements, preset-lod rendering, etc.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reall3d-com/Reall3dViewer

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T23:29:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG, RAD and LCC2.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [FIRENESST/3dgs-mobile](https://github.com/FIRENESST/3dgs-mobile)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T04:12:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/FIRENESST/3dgs-mobile

### [keinnyne000/3DGS-vector-quantization-selection](https://github.com/keinnyne000/3DGS-vector-quantization-selection)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T00:03:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/keinnyne000/3DGS-vector-quantization-selection

### [danchar12138/scan3d-windows](https://github.com/danchar12138/scan3d-windows)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T15:39:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photos or phone video to Gaussian splat + textured mesh + collision mesh. Windows-native, one-click, web UI, runs locally (Spirula Studio + COLMAP).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/danchar12138/scan3d-windows

### [ZhangAoCanada/3Dviewer](https://github.com/ZhangAoCanada/3Dviewer)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T13:47:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** just another 3D viewer for popular 3D representations, including 3DGS, mesh, point cloud, ...
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhangAoCanada/3Dviewer

### [yimingjiang216-alt/mcp-3dgs](https://github.com/yimingjiang216-alt/mcp-3dgs)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T12:57:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MCP-3DGS: Model Context Protocol Server for 3D Gaussian Splatting Spatial Intelligence (Open-Vocab 3D Grounding, VLN View Imagination, 3DGS-ESDF Path Planning & Scene Editing on TUM RGB-D)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yimingjiang216-alt/mcp-3dgs

### [aryansdream/scene-rebuilder](https://github.com/aryansdream/scene-rebuilder)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T08:46:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Local 3D scene reconstruction from photos and video, with GPU Gaussian splatting, textured meshes, and object detection.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aryansdream/scene-rebuilder

### [cameornh/bardo](https://github.com/cameornh/bardo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T08:19:46Z
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
- **发布时间/更新时间：** 2026-11-20T23:20:30Z
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
- **发布时间/更新时间：** 2026-11-21T08:26:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, MVS, visual-inertial SLAM, 3D Gaussian Splatting and map-based localization in Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T04:30:13Z
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
- **发布时间/更新时间：** 2026-11-21T04:00:02Z
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
- **发布时间/更新时间：** 2026-11-21T07:40:05Z
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
- **发布时间/更新时间：** 2026-11-21T04:46:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reconstruct an object and place it inGarden:A reconstruction can look convincing in a single photograph and still break down when the camera moves. In thisproject, you will use held-out photographs and moving viewpoints to find out where a 3D Gaussian Splatting (3DGS)reconstruction holds up, where it fails, and why.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lhamyuh/CUHKSZ-CV-Proj2

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T03:12:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [chen-wu-129/TPS-3DGS](https://github.com/chen-wu-129/TPS-3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T16:19:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** > Code and field data for TPS-3DGS: altitude-adaptive ROI for small-target 3DGS reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chen-wu-129/TPS-3DGS

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T11:17:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T00:51:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WHIK Studio: free all-in-one video production for Windows and Linux. Timeline editing with captions, auto edit and sound, node compositing (keying, roto, tracking), 3D Gaussian splats (3DGS), 3D rendering, AI on your own PC, live link with Maya, Blender and Unreal. Manual in Korean, English, Japanese and Chinese at whik.co.kr/manual.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/suin-park/Whik

### [hasanfaesal/nvs](https://github.com/hasanfaesal/nvs)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T05:32:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS + open-vocabulary & click segmentation (SAGA, SAM, gsplat)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hasanfaesal/nvs

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T11:50:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high performance 3DGS renderer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-viewer

### [AndriiShramko/ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T07:45:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [CharlyX-Lee/GS-UVCE](https://github.com/CharlyX-Lee/GS-UVCE)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T05:56:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [ICRA 2026] GS-UVCE: Gaussian Splatting-Driven Unsupervised Visual Consistency Enhancement for Underwater 3D Scene Reconstructio
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CharlyX-Lee/GS-UVCE

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T23:16:58Z
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
- **发布时间/更新时间：** 2026-11-20T09:30:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T08:53:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T06:49:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [terranceh12/pixel-city-splat-test](https://github.com/terranceh12/pixel-city-splat-test)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T04:38:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3d gaussian splat pixel art
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/terranceh12/pixel-city-splat-test

### [ishandutta2007/Awesome-3D-Gaussian-Splatting-Spatial-Computing](https://github.com/ishandutta2007/Awesome-3D-Gaussian-Splatting-Spatial-Computing)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T04:19:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Top 3D Gaussian Splatting Spatial Computing (Opensource) Star if you like it!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ishandutta2007/Awesome-3D-Gaussian-Splatting-Spatial-Computing

### [Ky0y4/websplat](https://github.com/Ky0y4/websplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T02:34:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat viewer for vr browsers, mixed reality, drone controls, scalable splat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Ky0y4/websplat

### [Cachemarra/GaussianWorlds](https://github.com/Cachemarra/GaussianWorlds)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T02:25:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Testing Neon and Opus5.5 in procedural Gaussian Splatting worlds. The objectives are:
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cachemarra/GaussianWorlds

### [kazu107/3dgs-viewer](https://github.com/kazu107/3dgs-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T13:33:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kazu107/3dgs-viewer

### [philleer/realtime_3dvision](https://github.com/philleer/realtime_3dvision)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T11:53:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Realtime 3D Vision Project, Detection/DepthEstimation/3DGS included.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/philleer/realtime_3dvision

### [Karthik7259/3DGS](https://github.com/Karthik7259/3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T11:42:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Karthik7259/3DGS

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T13:53:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [uhhhci/Gsplat-unity-virtual-human](https://github.com/uhhhci/Gsplat-unity-virtual-human)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T09:00:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A Source-Agnostic Unity Toolkit for Rigging and Animating 3D Gaussian Splatting Virtual Humans
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/uhhhci/Gsplat-unity-virtual-human

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T08:59:38Z
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
- **发布时间/更新时间：** 2026-11-20T09:52:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [aktnk/splat-tour](https://github.com/aktnk/splat-tour)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T08:41:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** We can move freely within the 3DGS space, and freely place and display information within it.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aktnk/splat-tour

### [joezgao/seen-from-twelve-sides](https://github.com/joezgao/seen-from-twelve-sides)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T23:40:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 3D Gaussian Splatting fit written from scratch in NumPy, shown in the browser.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/joezgao/seen-from-twelve-sides

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T18:49:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [glxy404310/my-3dgs](https://github.com/glxy404310/my-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T12:25:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/glxy404310/my-3dgs

### [in33/SpaceBrowser](https://github.com/in33/SpaceBrowser)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-20T11:26:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空间浏览器 SpaceBrowser.cn — 基于 Aholo 空间智能 API，用一句话或一组照片生成可漫游的高保真 3D 空间（3DGS / Lux3X）。纯 HTML+JS+CSS，浏览器即用。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/in33/SpaceBrowser

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | degraded: HTTPError: HTTP Error 429: Unknown Error |
| GitHub | ok: 58 |
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

