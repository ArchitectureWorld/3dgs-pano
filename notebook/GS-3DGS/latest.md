---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-21T09:01:33Z
window_end_utc: 2026-11-22T09:10:19Z
generated_at_utc: 2026-11-22T09:10:19Z
item_count: 61
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-22

**统计窗口：** 2026-11-21T09:01:33Z — 2026-11-22T09:10:19Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **61** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **61** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Fix off-by-one in quantized PLY decoding (`/ 254` instead of `/ 255`) (#560) * Add a test for decoding compressed PLY SH bytes Byte 255 must decode to +4 and byte 128, which stores a coefficient of 0, to about 0, as in the PlayCanvas engine. The current decoder divides by 254 and fails: byte 255 gives 4.0315. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode compressed PLY SH bytes with / 255 Dividing by 254 decoded every byte from 127 up into the next quantization bin, so scenes from a SuperSplat .compressed.ply looked brighter or darker depending on the view direction. 255 matches the PlayCanvas engine (q * 8 / 255 - 4). Fixes #559 Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Add a test for decoding quantized PLY colors A uchar or ushort red/green/blue at its maximum must decode to 1.0. The current decoder divides by MAX - 1, so 255 gives 1.0039. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode quantized PLY colors with / MAX Same off-by-one as the SH decoding: dividing by MAX - 1 made full colour channels decode slightly above 1.0. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>](https://github.com/ArthurBrussee/brush/commit/8da360e87b9dbbde33de825bbfe3651d9fefbc40) | 代码实质更新 | GitHub · ArthurBrussee/brush | E2 | P2 |
| 2 | [Don't build rerun on iOS and Android (#561) Mobile apps embedding brush don't need rerun, and it pulls in analytics code and a lot of crates. Use the same no-op path as wasm there.](https://github.com/ArthurBrussee/brush/commit/9e36517ef24781e82e9083b2ffae6807adcc91b0) | 代码实质更新 | GitHub · ArthurBrussee/brush | E2 | P2 |
| 3 | [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T08:48:15Z
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
- **发布时间/更新时间：** 2026-11-22T08:24:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [fabianfreund/SplatCraft](https://github.com/fabianfreund/SplatCraft)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T06:51:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-platform Gaussian Splatting studio: drop photos/videos, align, train with live preview, export. Plugin-based, non-destructive.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fabianfreund/SplatCraft

### [CarlottaSeal/neural-rendering-cuda](https://github.com/CarlottaSeal/neural-rendering-cuda)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T06:35:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Neural rendering GPU kernels: optimized 3DGS rasterizer (sm_120), Instant-NGP and differentiable rasterization from scratch
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CarlottaSeal/neural-rendering-cuda

### [CyberAnomalo/ink2godot](https://github.com/CyberAnomalo/ink2godot)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T05:11:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pixel-art Gaussian splat rendering in Godot 4 — flat-disc splats, palette constraint dither, shader-driven per-splat VFX. No custom engine build.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CyberAnomalo/ink2godot

### [arrival-space/animated-sog](https://github.com/arrival-space/animated-sog)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T23:27:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Animated SOG (.asog): compact 4D Gaussian splat clips with motion, SH and sound - spec, Python encoder and flip-book pipeline, PlayCanvas and three.js players
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arrival-space/animated-sog

### [coolho1129/InstantHand](https://github.com/coolho1129/InstantHand)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T19:33:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of "InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image" (NeurIPS 2026)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/coolho1129/InstantHand

### [frenchtouchXR/ithaca-4dgs-unity](https://github.com/frenchtouchXR/ithaca-4dgs-unity)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T23:41:59Z
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
- **发布时间/更新时间：** 2026-11-21T23:41:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Ithaca 4DGS JS player (WebGL2): ITHACA 4D Gaussian Splatting videos as three.js / A-Frame objects for WebXR scenes and metaverses. MIT.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frenchtouchXR/ithaca-4dgs-js-player

### [c00lpeace/muse-avatar-splat](https://github.com/c00lpeace/muse-avatar-splat)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T07:58:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Muse avatar as a Gaussian Splat — web viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/c00lpeace/muse-avatar-splat

### [liming0724/Auto-RTL-4DGS-EDA](https://github.com/liming0724/Auto-RTL-4DGS-EDA)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T06:27:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Algorithm-Hardware Co-Design & Automated Formal Verification Framework targeting 4D Gaussian Splatting (4DGS) hardware acceleration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/liming0724/Auto-RTL-4DGS-EDA

### [CyberAnomalo/art-pipeline](https://github.com/CyberAnomalo/art-pipeline)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T05:11:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Bake ink-studio scenes into Gaussian .ply files (3DGS layout) with per-splat animation and a sidecar carrying camera, palette and centroid.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CyberAnomalo/art-pipeline

### [royorel/MEMO](https://github.com/royorel/MEMO)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T03:57:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MEMO: A Mesh for Every Moment. Dynamic Gaussian splatting with a watertight mesh at every time step.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/royorel/MEMO

### [CooperAndy/Semantic-Dynamic-3DGS-SLAM](https://github.com/CooperAndy/Semantic-Dynamic-3DGS-SLAM)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T13:36:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Source code and experiment configurations for Semantic Dynamic 3DGS-SLAM for Autonomous Driving.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CooperAndy/Semantic-Dynamic-3DGS-SLAM

### [Fix off-by-one in quantized PLY decoding (`/ 254` instead of `/ 255`) (#560) * Add a test for decoding compressed PLY SH bytes Byte 255 must decode to +4 and byte 128, which stores a coefficient of 0, to about 0, as in the PlayCanvas engine. The current decoder divides by 254 and fails: byte 255 gives 4.0315. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode compressed PLY SH bytes with / 255 Dividing by 254 decoded every byte from 127 up into the next quantization bin, so scenes from a SuperSplat .compressed.ply looked brighter or darker depending on the view direction. 255 matches the PlayCanvas engine (q * 8 / 255 - 4). Fixes #559 Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Add a test for decoding quantized PLY colors A uchar or ushort red/green/blue at its maximum must decode to 1.0. The current decoder divides by MAX - 1, so 255 gives 1.0039. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode quantized PLY colors with / MAX Same off-by-one as the SH decoding: dividing by MAX - 1 made full colour channels decode slightly above 1.0. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>](https://github.com/ArthurBrussee/brush/commit/8da360e87b9dbbde33de825bbfe3651d9fefbc40)

- **主题：** 压缩与轻量化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-21T09:04:22Z
- **更新判定：** 代码实质更新
- **核心内容：** Fix off-by-one in quantized PLY decoding (`/ 254` instead of `/ 255`) (#560) * Add a test for decoding compressed PLY SH bytes Byte 255 must decode to +4 and byte 128, which stores a coefficient of 0, to about 0, as in the PlayCanvas engine. The current decoder divides by 254 and fails: byte 255 gives 4.0315. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode compressed PLY SH bytes with / 255 Dividing by 254 decoded every byte from 127 up into the next quantization bin, so scenes from a SuperSplat .compressed.ply looked brighter or darker depending on the view direction. 255 matches the PlayCanvas engine (q * 8 / 255 - 4). Fixes #559 Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Add a test for decoding quantized PLY colors A uchar or ushort red/green/blue at its maximum must decode to 1.0. The current decoder divides by MAX - 1, so 255 gives 1.0039. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Decode quantized PLY colors with / MAX Same off-by-o…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [Don't build rerun on iOS and Android (#561) Mobile apps embedding brush don't need rerun, and it pulls in analytics code and a lot of crates. Use the same no-op path as wasm there.](https://github.com/ArthurBrussee/brush/commit/9e36517ef24781e82e9083b2ffae6807adcc91b0)

- **主题：** 压缩与轻量化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-21T09:48:32Z
- **更新判定：** 代码实质更新
- **核心内容：** Don't build rerun on iOS and Android (#561) Mobile apps embedding brush don't need rerun, and it pulls in analytics code and a lot of crates. Use the same no-op path as wasm there.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T03:48:11Z
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
- **发布时间/更新时间：** 2026-11-21T11:42:49Z
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
- **发布时间/更新时间：** 2026-11-21T16:59:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [NicolasDrum/splat-repair](https://github.com/NicolasDrum/splat-repair)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T22:33:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Editor for Gaussian splats with a repair brush: paint over what should go and the surface is rebuilt.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NicolasDrum/splat-repair

### [4321ba/GodotGaussianSplattingNodes](https://github.com/4321ba/GodotGaussianSplattingNodes)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T23:24:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Allows developers to use gaussian splatting objects as they would use a regular mesh + mesh instance.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/4321ba/GodotGaussianSplattingNodes

### [cameornh/bardo](https://github.com/cameornh/bardo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T06:15:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A gaussian splatting / sdf physics sandbox
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cameornh/bardo

### [h1bomb/qingming-pixel-splat](https://github.com/h1bomb/qingming-pixel-splat)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T05:32:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 清明上河图·虹桥夜渡 — Pixel-Art Gaussian Splatting 复现 (SDF → surface Gaussian splats → pixel-art resolve), based on Ink Studio by Silicon Jungle
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/h1bomb/qingming-pixel-splat

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T22:18:44Z
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
- **发布时间/更新时间：** 2026-11-22T09:01:29Z
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
- **发布时间/更新时间：** 2026-11-22T06:18:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Full-stack ROS 2 autonomous navigation: Nav2, SLAM Toolbox, RTAB-Map & ORB-SLAM3 VSLAM, Gazebo Harmonic, Docker, multi-robot fleet coordination, collaborative loop closure, coordinated frontier exploration, MPPI controller, behavior trees, waypoint following & Gaussian Splatting capture on Humble/Jazzy.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/darshmenon/rosnav

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T08:56:34Z
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
- **发布时间/更新时间：** 2026-11-22T03:13:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [MingChaoSun/MingChaoSun.github.io](https://github.com/MingChaoSun/MingChaoSun.github.io)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T02:24:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mingchao Sun (孙铭超) — Researcher at Alibaba Group (AMap). 3D reconstruction & generation, Gaussian Splatting, world models, embodied intelligence.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MingChaoSun/MingChaoSun.github.io

### [khanhhuyen-ops/3dgs-reconstruction](https://github.com/khanhhuyen-ops/3dgs-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T05:15:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/khanhhuyen-ops/3dgs-reconstruction

### [Cenvoil/semantic-railgauss-slam](https://github.com/Cenvoil/semantic-railgauss-slam)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T03:34:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Rail-specific semantic Gaussian-splatting SLAM on OSDaR23
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cenvoil/semantic-railgauss-slam

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T03:13:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING](https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:45:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING

### [lhamyuh/CUHKSZ-CV-Proj2](https://github.com/lhamyuh/CUHKSZ-CV-Proj2)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T13:17:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reconstruct an object and place it inGarden:A reconstruction can look convincing in a single photograph and still break down when the camera moves. In thisproject, you will use held-out photographs and moving viewpoints to find out where a 3D Gaussian Splatting (3DGS)reconstruction holds up, where it fails, and why.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lhamyuh/CUHKSZ-CV-Proj2

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T10:53:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [AaronNZH/LeGS](https://github.com/AaronNZH/LeGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T07:04:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [ICML 2026] Beyond Heuristics: Learnable Density Control for 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AaronNZH/LeGS

### [AndriiShramko/ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T20:28:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source browser FPV drone simulator for 3D Gaussian Splatting scans (SuperSplat): quadcopter physics with Betaflight rates and PID, swept voxel collision with real crashes, EdgeTX radio over WebHID, gamepad or touch. WebGPU + PlayCanvas. Fly: gsfpv.flyreelstudio.eu
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AndriiShramko/ShramkoGSFPV

### [affromero/splattie](https://github.com/affromero/splattie)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:59:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Generate rigged interactive 3D Gaussian assets for the web.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/affromero/splattie

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T21:58:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [waleedsworld/open-revisualizer](https://github.com/waleedsworld/open-revisualizer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T03:22:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Re-render reality from a car's surround cameras as 3D Gaussian splats, then drive through it like a video game. Open-source reality view with SDK.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/waleedsworld/open-revisualizer

### [Trans-cending/GSBFplus](https://github.com/Trans-cending/GSBFplus)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T02:37:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GSBF+: 3D Gaussian Splatting for Environment-Aware MIMO Beamforming. Code coming soon upon paper acceptance.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Trans-cending/GSBFplus

### [arissaelena/3dgs-decomposition](https://github.com/arissaelena/3dgs-decomposition)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T00:04:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arissaelena/3dgs-decomposition

### [wangguode/terra-world-travel](https://github.com/wangguode/terra-world-travel)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T14:34:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** TERRA-OASIS // 世界模型前沿学习知识图谱与浏览器端交互式 3D / 3DGS 实验沙盒 (World Models Research Hub & WebGL/SparkJS Sandbox)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wangguode/terra-world-travel

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T09:03:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T09:04:20Z
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
- **发布时间/更新时间：** 2026-11-22T08:53:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [jongseo3477/transparent-scene-rendering](https://github.com/jongseo3477/transparent-scene-rendering)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T02:43:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** OptiX-free novel-view rendering of transparent scenes with Gaussian splatting, depth-based rendering and optical flow.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jongseo3477/transparent-scene-rendering

### [ncubeeight/Splativerse-for-Meta-Quest](https://github.com/ncubeeight/Splativerse-for-Meta-Quest)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T01:53:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Meta Quest Gaussian splat viewer with a local scan library, immersive navigation and saved Views.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ncubeeight/Splativerse-for-Meta-Quest

### [Rock-Garden-Inc/twinbly-examples](https://github.com/Rock-Garden-Inc/twinbly-examples)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-22T00:23:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Twinbly Gaussian splatting API, CLI and local MCP examples, with a no-key connection check.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Rock-Garden-Inc/twinbly-examples

### [ferdinandl007/PrismSplat](https://github.com/ferdinandl007/PrismSplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T21:40:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-driven Gaussian splat rendering for Metal and Swift
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ferdinandl007/PrismSplat

### [YeeBy2019/head-tracked-3d](https://github.com/YeeBy2019/head-tracked-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:23:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 6DoF head tracking from a single webcam, driving a 1.9M-gaussian 3DGS room at 30 MB. Real parallax in the browser, no headset.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/YeeBy2019/head-tracked-3d

### [Karthik7259/3DGS](https://github.com/Karthik7259/3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:04:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Karthik7259/3DGS

### [gotoeasy/gsbox](https://github.com/gotoeasy/gsbox)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T15:10:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a cross-platform command-line tool for converting 3DGS (3D Gaussian Splatting) files, supporting conversions like PLY to .splat, PLY to .spx, PLY to .spz, PLY to .sog, and vice versa.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gotoeasy/gsbox

### [removed limits when reading images to allow 8k EXRs to be read (#532)](https://github.com/ArthurBrussee/brush/commit/52fda33d2f15955584d41dd318529eed16824697)

- **主题：** 其他
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-11-21T09:54:13Z
- **更新判定：** 代码实质更新
- **核心内容：** removed limits when reading images to allow 8k EXRs to be read (#532)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T14:58:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** OpenUSD file format and schema plugins for 3D Gaussian Splatting assets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/usd-3dgs-plugins

### [a13409512853-maker/splat-convert-desktop](https://github.com/a13409512853-maker/splat-convert-desktop)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T15:51:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 高斯泼溅ply大文件本地转换，绕开在线网页的体积与浏览器环境限制；免安装便携，图形界面轻松上手。支持 PLY 压缩为 SOG，以及多格式转换、合并与筛选。提供 Windows / macOS 版本，基于 PlayCanvas Splat Transform 的非官方桌面工具。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/a13409512853-maker/splat-convert-desktop

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T09:36:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [edencheung/3DGS-with-Depth-Priors](https://github.com/edencheung/3DGS-with-Depth-Priors)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T23:14:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/edencheung/3DGS-with-Depth-Priors

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:45:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [bala-skv/Topological-metric-of-3DGS-methods](https://github.com/bala-skv/Topological-metric-of-3DGS-methods)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T17:14:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/bala-skv/Topological-metric-of-3DGS-methods

### [aktnk/splat-tour](https://github.com/aktnk/splat-tour)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-21T12:39:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** We can move freely within the 3DGS space, and freely place and display information within it.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aktnk/splat-tour

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 0 |
| GitHub | ok: 61 |
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

