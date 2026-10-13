---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-12T08:23:24Z
window_end_utc: 2026-10-13T08:48:10Z
generated_at_utc: 2026-10-13T08:48:10Z
item_count: 67
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-13

**统计窗口：** 2026-10-12T08:23:24Z — 2026-10-13T08:48:10Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **67** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **67** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Fix f32 precision loss in ray/ellipsoid intersection (#469) * Evaluate ray/ellipsoid discriminant in f64 to avoid cancellation b^2 - ac in f32 loses precision when \|o\| >> 1 in the unit-sphere frame (small splats seen from far away), so raycast() rejects real hits or returns a wrong distance (about 40 cm off for a 5 mm splat at ~1.4 km in the new test). Use the Lagrange identity a - \|o x d\|^2 in f64. Refs #468 Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01AMz2xpnJWHh3D72Gy8NsRY * Make vec3 helpers generic over f32/f64 Address review: vec3_mul, vec3_dot and vec3_cross are now generic and used in the f64 ellipsoid branch instead of the hand-written arithmetic. No behavior change. Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> * Keep ray/ellipsoid discriminant in f32 The Lagrange identity alone fixes the cancellation; evaluating it in f64 gives no measurable gain because the remaining error comes from the f32 center subtraction and rotation. Revert the f64 conversion and generic helpers so the change is limited to the discriminant and the test. Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>](https://github.com/sparkjsdev/spark/commit/1df80ca7d903e0d3bfd4a66c88b4242ec79c1851) | 代码实质更新 | GitHub · sparkjsdev/spark | E2 | P2 |
| 2 | [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 3 | [playcanvas/engine](https://github.com/playcanvas/engine) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [Fix f32 precision loss in ray/ellipsoid intersection (#469) * Evaluate ray/ellipsoid discriminant in f64 to avoid cancellation b^2 - ac in f32 loses precision when |o| >> 1 in the unit-sphere frame (small splats seen from far away), so raycast() rejects real hits or returns a wrong distance (about 40 cm off for a 5 mm splat at ~1.4 km in the new test). Use the Lagrange identity a - |o x d|^2 in f64. Refs #468 Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01AMz2xpnJWHh3D72Gy8NsRY * Make vec3 helpers generic over f32/f64 Address review: vec3_mul, vec3_dot and vec3_cross are now generic and used in the f64 ellipsoid branch instead of the hand-written arithmetic. No behavior change. Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> * Keep ray/ellipsoid discriminant in f32 The Lagrange identity alone fixes the cancellation; evaluating it in f64 gives no measurable gain because the remaining error comes from the f32 center subtraction and rotation. Revert the f64 conversion and generic helpers so the change is limited to the discriminant and the test. Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>](https://github.com/sparkjsdev/spark/commit/1df80ca7d903e0d3bfd4a66c88b4242ec79c1851)

- **主题：** 训练与优化
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T21:40:55Z
- **更新判定：** 代码实质更新
- **核心内容：** Fix f32 precision loss in ray/ellipsoid intersection (#469) * Evaluate ray/ellipsoid discriminant in f64 to avoid cancellation b^2 - ac in f32 loses precision when |o| >> 1 in the unit-sphere frame (small splats seen from far away), so raycast() rejects real hits or returns a wrong distance (about 40 cm off for a 5 mm splat at ~1.4 km in the new test). Use the Lagrange identity a - |o x d|^2 in f64. Refs #468 Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> Claude-Session: https://claude.ai/code/session_01AMz2xpnJWHh3D72Gy8NsRY * Make vec3 helpers generic over f32/f64 Address review: vec3_mul, vec3_dot and vec3_cross are now generic and used in the f64 ellipsoid branch instead of the hand-written arithmetic. No behavior change. Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com> * Keep ray/ellipsoid discriminant in f32 The Lagrange identity alone fixes the cancellation; evaluating it in f64 gives no measurable gain because the remaining error comes…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:37:43Z
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
- **发布时间/更新时间：** 2026-10-13T06:21:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [Stop retrying a level of detail tree that failed (#477) A tree that failed to initialize raised an unhandled error, such as "Array buffer allocation failed", on every update and skipped the trees queued after it. The failure is now logged and the tree is not retried.](https://github.com/sparkjsdev/spark/commit/bdfe15f54f3469290606a25fe6c2a6457804d8c1)

- **主题：** 训练与优化
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T17:31:11Z
- **更新判定：** 代码实质更新
- **核心内容：** Stop retrying a level of detail tree that failed (#477) A tree that failed to initialize raised an unhandled error, such as "Array buffer allocation failed", on every update and skipped the trees queued after it. The failure is now logged and the tree is not retried.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [seemandhar/splatify](https://github.com/seemandhar/splatify)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:00:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SPLATIFY: Reproduce, Discover, Innovate! Multi-agent framework turning 3D Gaussian Splatting papers and ideas into trainable gsplat/nerfstudio code (arXiv 2610.09116)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/seemandhar/splatify

### [samaust/openftgs](https://github.com/samaust/openftgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:35:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on Neural3DV, ENeRF-Outdoor and SelfCap.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [Erant/b2ctrain](https://github.com/Erant/b2ctrain)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T03:41:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splat trainer and renderer for the b2crunner project.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Erant/b2ctrain

### [zju3dv/habitat-gs](https://github.com/zju3dv/habitat-gs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T05:33:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [ECCV 2026] Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zju3dv/habitat-gs

### [qherau/3DGS-Calib](https://github.com/qherau/3DGS-Calib)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:52:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Site for the paper "3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration".
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/qherau/3DGS-Calib

### [frenchtouchXR/ithaca-4dgs-unity](https://github.com/frenchtouchXR/ithaca-4dgs-unity)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T10:09:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time 4D Gaussian Splatting rendering and asset generation for Unity (URP), with full 3DGS/4DGS compatibility. Fork of aras-p/UnityGaussianSplatting, extended with temporal playback support.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frenchtouchXR/ithaca-4dgs-unity

### [iamkyledang/stag_gs](https://github.com/iamkyledang/stag_gs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:35:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of STAG-GS: Sparse Temporal Anchor Learning for Dynamic 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/iamkyledang/stag_gs

### [hijosubin/XR-Classroom](https://github.com/hijosubin/XR-Classroom)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:30:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A Real-World Dynamic Multi-View Classroom Dataset Captured with Heterogeneous RGB Cameras for 3D/4D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hijosubin/XR-Classroom

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:13:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG and RAD.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [animu-sphere/hydra-merlin](https://github.com/animu-sphere/hydra-merlin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T16:08:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A lightweight, host-neutral raster renderer for USD Hydra, powered by Vulkan and Metal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/hydra-merlin

### [Strawboardnationaldebtceiling9560/kakeya-3d](https://github.com/Strawboardnationaldebtceiling9560/kakeya-3d)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:18:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Formalizes the 3D Kakeya conjecture in Lean 4, proving every compact set with unit segments in all directions has Hausdorff dimension three.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Strawboardnationaldebtceiling9560/kakeya-3d

### [sivan7zZ/3DGS-COMPRESSION](https://github.com/sivan7zZ/3DGS-COMPRESSION)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T02:11:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sivan7zZ/3DGS-COMPRESSION

### [manycoretech/aholo-spatial-sdk](https://github.com/manycoretech/aholo-spatial-sdk)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:33:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SDK for the Aholo API — 3DGS reconstruction, generation, cloud rendering, and material/model creation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-spatial-sdk

### [Archerkattri/aura](https://github.com/Archerkattri/aura)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:01:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** AURA — Adaptive Unified Radiance Asset: the post-3DGS asset layer. Typed carriers (Gaussian/Beta), calibrated + certified per-carrier confidence exported in KHR_gaussian_splatting & OpenUSD 26.03, unified ray-query, relight preview.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/aura

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:59:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [cameornh/bardo](https://github.com/cameornh/bardo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T02:50:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A gaussian splatting / sdf physics sandbox
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cameornh/bardo

### [neelgajera/beta-splatting-showcase](https://github.com/neelgajera/beta-splatting-showcase)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T13:06:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Web gallery and studio for Beta/Gaussian splatting captures: real-time viewer with cinematic tour, plus a PlayCanvas studio with cast shadows, reflections and HDRI lighting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/neelgajera/beta-splatting-showcase

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:50:03Z
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
- **发布时间/更新时间：** 2026-10-13T08:37:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, visual-inertial SLAM, 3D Gaussian Splatting and localization in pure Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [sou350121/Spatial-Intelligence-Handbook](https://github.com/sou350121/Spatial-Intelligence-Handbook)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:58:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [Human-Augment-Analytics/porto-photogrammetry](https://github.com/Human-Augment-Analytics/porto-photogrammetry)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:48:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A photogrammetry pipeline for high-fidelity 3D object reconstruction from multi-view images.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Human-Augment-Analytics/porto-photogrammetry

### [Tirzst5779/ML-Sharp-QNN](https://github.com/Tirzst5779/ML-Sharp-QNN)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:15:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Run Apple's SHARP 3D Gaussian Splatting on Android via Qualcomm QNN HTP for instant, offline single-image 3D reconstruction on Snapdragon devices.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Tirzst5779/ML-Sharp-QNN

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:36:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Reconstruction of UCLA Gateway Plaza from unstaged outdoor scene video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS

### [sexya3624/InsertAny3D](https://github.com/sexya3624/InsertAny3D)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:17:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Insert 3D objects into Unity scenes via multi-view geometric alignment and generated Gaussian Splatting assets with accurate pose estimation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sexya3624/InsertAny3D

### [enhansome/enhansome-NeRF-and-3DGS-SLAM](https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T03:35:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [ada-zy2425/robust-sparse-3dgs](https://github.com/ada-zy2425/robust-sparse-3dgs)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T10:06:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Robust sparse-view 3D Gaussian Splatting reconstruction and private interactive evaluation
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ada-zy2425/robust-sparse-3dgs

### [kanehub/DIBR-GS](https://github.com/kanehub/DIBR-GS)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:08:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official repository for "Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kanehub/DIBR-GS

### [MisterE123/spark-tour-studio](https://github.com/MisterE123/spark-tour-studio)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T01:43:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows Gaussian splat tour editor and locally bundled WebXR viewer powered by Spark
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MisterE123/spark-tour-studio

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:23:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:28:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository tracks the latest advancements in 3D Gaussian Splatting from Arxiv, with daily automated updates. Stay up-to-date with cutting-edge research in this exciting field!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/longxiang-ai/awesome-gaussians

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@983a5770083ccdb7fbfa8544820170c4a46d19b0/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/753fc484ae9fa5005aa326d1055a47b7c6974310)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T21:43:43Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@983a5770083ccdb7fbfa8544820170c4a46d19b0/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@155a84cffafea2a061f07241e1068b135430ada7/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/80d919f87b147368f82d75da54c2a6b45dde307d)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T17:33:11Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@155a84cffafea2a061f07241e1068b135430ada7/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T15:44:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 图形学与3DGS、空间智能持续更新论文；AI Agent Skills for 3D Gaussian Splatting, NeRF & Computer Graphics Research. 800+ methods, 25categories, 12skills. OpenClaw / Claude Code compatible.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Archerkattri/splatreg](https://github.com/Archerkattri/splatreg)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:33:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Register Gaussian splats: align & merge two 3DGS scans into one SE(3)/Sim(3) frame — classical, learned, or zero-shot (BUFFER-X) seeds + splat-native refine. pip install splatreg.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/splatreg

### [Shawn100861224/web3d-lab](https://github.com/Shawn100861224/web3d-lab)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T17:41:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS 在线重建查看器 + 个人主页（郑州大学双足实验室 3D 方向考核作品）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Shawn100861224/web3d-lab

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T14:30:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [thunderheronight/splat-workshop](https://github.com/thunderheronight/splat-workshop)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:46:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GUI for the Arcturus Vision splat pipeline: pick, check and convert Steam Frame camera recordings and send them to the Gaussian XR gallery
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thunderheronight/splat-workshop

### [splat3d/splat-swift-sdk](https://github.com/splat3d/splat-swift-sdk)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:33:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Swift SDK for the Splat API — ARKit LiDAR capture + 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/splat3d/splat-swift-sdk

### [AndriiShramko/ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:29:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [jedrula/dji-waypoints](https://github.com/jedrula/dji-waypoints)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T15:04:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS capture mission planner for the DJI Mini 5 Pro — draw an area, get a flight, export a KMZ for DJI Fly
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jedrula/dji-waypoints

### [DisplayXR/displayxr-demo-gaussiansplat](https://github.com/DisplayXR/displayxr-demo-gaussiansplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:25:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** DisplayXR demo — real-time 3D Gaussian Splatting viewer for glasses-free 3D displays (OpenXR + Vulkan, Windows & macOS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DisplayXR/displayxr-demo-gaussiansplat

### [smartonTT/gsplat_tt](https://github.com/smartonTT/gsplat_tt)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:36:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Port of Gaussian Splatting to Tenstorrent
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/smartonTT/gsplat_tt

### [3XyzMedia/VIEWER](https://github.com/3XyzMedia/VIEWER)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:38:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Любительские модели 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3XyzMedia/VIEWER

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:30:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Kral-35/on-device-3d-scanner](https://github.com/Kral-35/on-device-3d-scanner)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:17:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Turn 8 photos into a 3D scan on-device, no cloud, LiDAR, or ARKit needed.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Kral-35/on-device-3d-scanner

### [Streetjk/landcros-forrestdale](https://github.com/Streetjk/landcros-forrestdale)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:59:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SiteNav 3D Gaussian Splat site viewer — Landcros Forrestdale demo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Streetjk/landcros-forrestdale

### [squoraishee/prototypes](https://github.com/squoraishee/prototypes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T06:20:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Small browser prototypes: The Luminous Basin (Gaussian splat landscape) and Snakephoria (party snake game)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/squoraishee/prototypes

### [yxyaxng/Remy3D-Android](https://github.com/yxyaxng/Remy3D-Android)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T05:03:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Android 移动端实景 3D 重建与 3DGS 高斯泼溅渲染演示工程 (Kotlin + Camera2 + ARCore + NDK + OpenGL ES 2.0)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yxyaxng/Remy3D-Android

### [forgrabbit/forgrabbit](https://github.com/forgrabbit/forgrabbit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:00:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Fei Xie | 3D vision, Gaussian Splatting, and real-time rendering.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/forgrabbit/forgrabbit

### [survive175/3dgs-learning](https://github.com/survive175/3dgs-learning)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T11:06:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/survive175/3dgs-learning

### [Mrzhouxf/3dgs-research-paper](https://github.com/Mrzhouxf/3dgs-research-paper)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T08:48:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mrzhouxf/3dgs-research-paper

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T08:23:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [SidoPillai/SplatGen](https://github.com/SidoPillai/SplatGen)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T02:28:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Turn a single photo into an explorable 3D Gaussian splat scene, entirely on device (macOS, SwiftUI + Metal)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SidoPillai/SplatGen

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T12:17:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/983a5770083ccdb7fbfa8544820170c4a46d19b0)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T21:43:43Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/155a84cffafea2a061f07241e1068b135430ada7)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-12T17:33:10Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [hh-hang/collider-forge](https://github.com/hh-hang/collider-forge)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T08:40:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Build collider .glb files from glTF / 3D Tiles / 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hh-hang/collider-forge

### [dwwwwwww7/my-3dgs](https://github.com/dwwwwwww7/my-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T10:46:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 本项目基于https://github.com/longxiang-ai/awesome-gaussians 修改，丰富了论文信息，增加摘要翻译和邮件发送功能，用于检索3DGS压缩最新论文。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dwwwwwww7/my-3dgs

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T09:10:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T07:11:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [pstoebenau/guerrilla-worker](https://github.com/pstoebenau/guerrilla-worker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T04:56:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Standalone Gaussian splatting worker and pipeline for Guerrilla
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pstoebenau/guerrilla-worker

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T19:59:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [Prowler0204/nir_feature-to-3dgs](https://github.com/Prowler0204/nir_feature-to-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-12T15:59:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Prowler0204/nir_feature-to-3dgs

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 0 |
| GitHub | ok: 67 |
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

