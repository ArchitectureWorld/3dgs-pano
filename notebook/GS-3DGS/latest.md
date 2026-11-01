---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-31T07:51:09Z
window_end_utc: 2026-11-01T08:31:22Z
generated_at_utc: 2026-11-01T08:31:22Z
item_count: 54
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-01

**统计窗口：** 2026-10-31T07:51:09Z — 2026-11-01T08:31:22Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **54** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **54** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Add timeline and camera keyframe tools to WebMCP (#1090) * Add timeline and camera keyframe tools to WebMCP Agents can now inspect and edit the timeline through five new tools: get_timeline, set_timeline, set_keyframes, move_keyframe and delete_keyframes (29 tools in total). The commands live in a new EditorAPI module (editor-timeline.ts, exposed as editor.inspect.timeline and editor.timeline.*) and run in command queue slots like the other editor commands. Key edits are single AnimTrackEditOps, so each call is one undo step; timeline settings stay outside history, matching the timeline panel. Because the camera follows the animation, timeline results return the resulting camera and a fresh viewToken. sequence.idle lets playhead moves wait for a PLY sequence frame before reporting. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Port docs, seek fix, overwrite guard and tests from #1089 - Seeking to the current frame now re-evaluates the camera path, so a manually moved camera returns to the animation. - move_keyframe fails with key_exists on an occupied destination unless overwrite: true is passed. - A keyframe's frame defaults to the playhead, like Add Key. - get_scene includes a timeline summary. - docs/webmcp.md and the README describe the timeline tools, their undo semantics and the new error codes. - Tests: ordering against a queued UI undo, cancellation and busy checks, same-frame seek, playhead default, the PLY sequence wait, and a polling playback check in the browser suite. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>](https://github.com/playcanvas/supersplat/commit/4069712370df3425c386610f28a814403e835543) | 代码实质更新 | GitHub · playcanvas/supersplat | E2 | P2 |
| 2 | [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 3 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [playcanvas/engine](https://github.com/playcanvas/engine) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T02:41:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [shuta-ochiai/Splatelier](https://github.com/shuta-ochiai/Splatelier)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:54:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Capture, train and view 3D Gaussian Splats entirely on your iPhone.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shuta-ochiai/Splatelier

### [jgunaratne/room-splat](https://github.com/jgunaratne/room-splat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:50:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** iPhone LiDAR capture streamed to a GPU for live, progressive Gaussian Splat training
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jgunaratne/room-splat

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:17:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [Add timeline and camera keyframe tools to WebMCP (#1090) * Add timeline and camera keyframe tools to WebMCP Agents can now inspect and edit the timeline through five new tools: get_timeline, set_timeline, set_keyframes, move_keyframe and delete_keyframes (29 tools in total). The commands live in a new EditorAPI module (editor-timeline.ts, exposed as editor.inspect.timeline and editor.timeline.*) and run in command queue slots like the other editor commands. Key edits are single AnimTrackEditOps, so each call is one undo step; timeline settings stay outside history, matching the timeline panel. Because the camera follows the animation, timeline results return the resulting camera and a fresh viewToken. sequence.idle lets playhead moves wait for a PLY sequence frame before reporting. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Port docs, seek fix, overwrite guard and tests from #1089 - Seeking to the current frame now re-evaluates the camera path, so a manually moved camera returns to the animation. - move_keyframe fails with key_exists on an occupied destination unless overwrite: true is passed. - A keyframe's frame defaults to the playhead, like Add Key. - get_scene includes a timeline summary. - docs/webmcp.md and the README describe the timeline tools, their undo semantics and the new error codes. - Tests: ordering against a queued UI undo, cancellation and busy checks, same-frame seek, playhead default, the PLY sequence wait, and a polling playback check in the browser suite. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> --------- Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>](https://github.com/playcanvas/supersplat/commit/4069712370df3425c386610f28a814403e835543)

- **主题：** 动态与4D
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-31T22:22:34Z
- **更新判定：** 代码实质更新
- **核心内容：** Add timeline and camera keyframe tools to WebMCP (#1090) * Add timeline and camera keyframe tools to WebMCP Agents can now inspect and edit the timeline through five new tools: get_timeline, set_timeline, set_keyframes, move_keyframe and delete_keyframes (29 tools in total). The commands live in a new EditorAPI module (editor-timeline.ts, exposed as editor.inspect.timeline and editor.timeline.*) and run in command queue slots like the other editor commands. Key edits are single AnimTrackEditOps, so each call is one undo step; timeline settings stay outside history, matching the timeline panel. Because the camera follows the animation, timeline results return the resulting camera and a fresh viewToken. sequence.idle lets playhead moves wait for a PLY sequence frame before reporting. Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> * Port docs, seek fix, overwrite guard and tests from #1089 - Seeking to the current frame now re-evaluates the camera path, so a manually moved camer…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [solipsist-studios/comfyui-cumuli](https://github.com/solipsist-studios/comfyui-cumuli)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T04:31:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ComfyUI nodes taking one monocular video or a real multi-camera capture to a streamable .sogst 4D gaussian splat.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/comfyui-cumuli

### [BinGO620/RoGS-SLAM](https://github.com/BinGO620/RoGS-SLAM)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:04:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Robust Dynamic-Scene Gaussian Splatting SLAM via Reliability-Guided Weighting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/BinGO620/RoGS-SLAM

### [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T15:28:37Z
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
- **发布时间/更新时间：** 2026-11-01T07:56:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG and RAD.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [IRIS-LAB-whu/SemLite-GS](https://github.com/IRIS-LAB-whu/SemLite-GS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:22:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IRIS-LAB-whu/SemLite-GS

### [Khriis-K/Fidelis](https://github.com/Khriis-K/Fidelis)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:37:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Multifidelity Reliability Estimation for Vision-Based Planetary Navigation: estimating the probability of navigation failure during simulated Martian descent using Gaussian splatting and uncertainty quantification.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Khriis-K/Fidelis

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:12:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [api-evangelist/spaitial](https://github.com/api-evangelist/spaitial)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:13:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SpAItial — independent third-party profile of a public API surface, by API Evangelist. SpAItial (SpAItial Ltd, London) is a frontier spatial-AI lab building Echo, a world-model family that turns text prompts, images, and 360-degree panoramas into persistent, explorable 3D Gaussian Splat worlds (SPZ/SOG, plus mesh exports).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/api-evangelist/spaitial

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T20:40:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 📚这个仓库是在arxiv上收集的有关VLN，VLA，World Model，SLAM，Gaussian Splatting,非线性优化等相关论文。每天都会自动更新！issue区域是最新10篇论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/luohongk/Embodied-AI-Daily

### [darshmenon/rosnav](https://github.com/darshmenon/rosnav)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T19:30:39Z
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
- **发布时间/更新时间：** 2026-10-31T12:05:08Z
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
- **发布时间/更新时间：** 2026-11-01T02:41:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A photogrammetry pipeline for high-fidelity 3D object reconstruction from multi-view images.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Human-Augment-Analytics/porto-photogrammetry

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T02:50:49Z
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
- **发布时间/更新时间：** 2026-11-01T02:16:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [chu-jiaming/VGGT-Splat](https://github.com/chu-jiaming/VGGT-Splat)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:17:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Casual phone video → VGGT → 3D Gaussian Splatting, without COLMAP
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chu-jiaming/VGGT-Splat

### [Iloke-Alusala/Gaussian_Splatting_Localiser](https://github.com/Iloke-Alusala/Gaussian_Splatting_Localiser)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:17:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A pipeline designed to render and compare images derived from a pose within a 3DGS Map, and implement course and fine localisation implementations and assess viability for on-edge compute
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Iloke-Alusala/Gaussian_Splatting_Localiser

### [fadib12/capture-splat](https://github.com/fadib12/capture-splat)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T04:18:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** iPhone capture to 3D Gaussian Splatting with COLMAP and Vulkan/VkSplat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fadib12/capture-splat

### [piyush-2911/namaspace-spatial-engine](https://github.com/piyush-2911/namaspace-spatial-engine)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T20:17:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Indoor video reconstruction and local interactive 3D Gaussian splat viewer for Namma Space
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/piyush-2911/namaspace-spatial-engine

### [bhubbard/lyra-rs](https://github.com/bhubbard/lyra-rs)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:44:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pure Rust fork and high-performance engine for NVIDIA Project Lyra: Open Generative 3D World Models and Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/bhubbard/lyra-rs

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:09:32Z
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
- **发布时间/更新时间：** 2026-11-01T02:14:15Z
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
- **发布时间/更新时间：** 2026-11-01T00:44:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [affromero/splattie](https://github.com/affromero/splattie)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T15:28:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Generate rigged interactive 3D Gaussian assets for the web.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/affromero/splattie

### [chiou1203/ProFuse](https://github.com/chiou1203/ProFuse)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T03:35:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official Implementation of ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chiou1203/ProFuse

### [affromero/splattie-widget](https://github.com/affromero/splattie-widget)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T15:06:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive rigged 3D Gaussian Splatting web component - like Rive/Lottie for 3D.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/affromero/splattie-widget

### [szx-a/cli-web-3dgs](https://github.com/szx-a/cli-web-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:17:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3dgs训练
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/szx-a/cli-web-3dgs

### [janagor/vkgsplat](https://github.com/janagor/vkgsplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T19:32:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Vulkan-based rendering engine for 3D Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/janagor/vkgsplat

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:59:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [lzy021205/FocalGS](https://github.com/lzy021205/FocalGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:35:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for FocalGS: Adaptive Focal 3D Gaussian Splatting for Continuous Zoom Rendering
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lzy021205/FocalGS

### [kenrogermurro/splatmuseum](https://github.com/kenrogermurro/splatmuseum)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T05:50:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** IoT-assisted 3D Gaussian Splatting pipeline and web viewer for local artifacts
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kenrogermurro/splatmuseum

### [dtaddis/Lookaround](https://github.com/dtaddis/Lookaround)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T02:07:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Step into a photo: an AI video model films a 360° orbit, which becomes a Gaussian splat you can look around in a browser or VR.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dtaddis/Lookaround

### [parsabe/Vectra](https://github.com/parsabe/Vectra)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T20:44:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian splatting from text and image
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/parsabe/Vectra

### [create3000/x_ite-spz-parser](https://github.com/create3000/x_ite-spz-parser)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T10:28:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS SPZ File Format Parser for X_ITE
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/create3000/x_ite-spz-parser

### [create3000/x_ite-sog-parser](https://github.com/create3000/x_ite-sog-parser)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T10:25:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS sOG File Format Parser for X_ITE
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/create3000/x_ite-sog-parser

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T07:51:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [dwwwwwww7/my-3dgs](https://github.com/dwwwwwww7/my-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T04:31:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 本项目基于https://github.com/longxiang-ai/awesome-gaussians 修改，丰富了论文信息，增加摘要翻译和邮件发送功能，用于检索3DGS压缩最新论文。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dwwwwwww7/my-3dgs

### [YuhanChen2024/Dehaze-GaussianImage](https://github.com/YuhanChen2024/Dehaze-GaussianImage)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T19:13:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for the paper "Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/YuhanChen2024/Dehaze-GaussianImage

### [AssassinHLQ/csust](https://github.com/AssassinHLQ/csust)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T12:15:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Godot 4.7 越肩射击 + 跑酷 + 期货交易沙盒《长沙理工：2067》：12 段 571 m 跑酷、暗网比纳、保证金/负债/强平经济、3D 高斯泼溅校园
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AssassinHLQ/csust

### [askmgk/AdaGScale](https://github.com/askmgk/AdaGScale)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T11:30:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code and precomputed T_upper tables for AdaGScale, a viewpoint-adaptive Gaussian scaling method for 3D Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/askmgk/AdaGScale

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T08:28:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [ZEHUEI/RotorAI](https://github.com/ZEHUEI/RotorAI)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T07:52:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** just someone looking into 3DGS n NeRF : https://www.worldlabs.ai/ is my inspo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZEHUEI/RotorAI

### [james123wang5/memory-room](https://github.com/james123wang5/memory-room)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T07:11:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MemoryRoom — scan a room into 3D Gaussian Splats and pin memories to the objects inside. 房间会记得你：3D 高斯泼溅 + 可交互记忆空间。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/james123wang5/memory-room

### [oceanye/py_pipe_install](https://github.com/oceanye/py_pipe_install)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-01T06:50:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 基于CAD、双目视觉和安装顺序约束的管道安装状态识别与数字孪生项目
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/oceanye/py_pipe_install

### [a-elrawy/clad-3dgs](https://github.com/a-elrawy/clad-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T17:59:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/a-elrawy/clad-3dgs

### [gustavo-qss/laboratorio-radiologia-3dgs](https://github.com/gustavo-qss/laboratorio-radiologia-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T16:24:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Apresentação e acervo 3D de 3D Gaussian Splatting no Laboratório de Radiologia
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gustavo-qss/laboratorio-radiologia-3dgs

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T15:52:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [hous-lab/pansplat-trt-edge-orin](https://github.com/hous-lab/pansplat-trt-edge-orin)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T11:20:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** PanSplat panoramic 3DGS deployed as a 21-engine TensorRT chain on Jetson AGX Orin - 30 s/frame down to ~567 ms
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hous-lab/pansplat-trt-edge-orin

### [Cyclem/3dgs](https://github.com/Cyclem/3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T09:40:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cyclem/3dgs

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-31T08:48:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 0 |
| GitHub | ok: 54 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | degraded: ParseError: not well-formed (invalid token): line 1, column 41 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 0 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

