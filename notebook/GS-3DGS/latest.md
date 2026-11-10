---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-09T08:55:27Z
window_end_utc: 2026-11-10T09:02:02Z
generated_at_utc: 2026-11-10T09:02:02Z
item_count: 62
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-10

**统计窗口：** 2026-11-09T08:55:27Z — 2026-11-10T09:02:02Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **62** 项去重后的有效线索：真正新增论文 **0** 项、实质论文修订 **0** 项、代码/版本/项目更新 **60** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Fetch zlib 1.3.2 from zlib.net/fossils (#110) zlib.net only serves the latest release at the top level and moves older ones to /fossils/, so https://zlib.net/zlib-1.3.2.tar.gz now 404s and any build without a system zlib fails at configure time. Same tarball, so the URL_HASH is unchanged.](https://github.com/nianticlabs/spz/commit/855173912dee2a48cb539657f46c4ade775f48c9) | 代码实质更新 | GitHub · NianticLabs/spz | E2 | P2 |
| 2 | [[extension] Add Custom Attribute Extension via ZSTD Skippable Frames (#107) * first pass * fix wasm custom attribute conversion * decode filter * fix test number * update quantized bits to 16 * add test](https://github.com/nianticlabs/spz/commit/b56333f5135c7ce4026a1237fcb227d35f8a6557) | 代码实质更新 | GitHub · NianticLabs/spz | E2 | P2 |
| 3 | [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 4 | [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite) | 新项目/近期活跃 | GitHub Search | E1 | P2 |
| 5 | [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 新项目/近期活跃 | GitHub Search | E1 | P2 |

## 分类详述

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T05:16:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T09:01:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [junyoung6215/EvenSplat](https://github.com/junyoung6215/EvenSplat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T04:33:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Compact pose-free feed-forward 3D Gaussian splatting via stratified retention and pruning-aware fine-tuning.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/junyoung6215/EvenSplat

### [11qishiyi/3dgs-compression-density](https://github.com/11qishiyi/3dgs-compression-density)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T02:59:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code and data for 'Density Is a Symptom, Not a Lever: A Controlled Study of Lossy Input Compression in 3D Gaussian Splatting'
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/11qishiyi/3dgs-compression-density

### [chalk-ai/gaussian-splatting](https://github.com/chalk-ai/gaussian-splatting)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T18:35:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Train 3D Gaussian Splatting live on one GPU with Chalk, watch it converge, and orbit the result in your browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chalk-ai/gaussian-splatting

### [dvt3d/maplibre-three-plugin](https://github.com/dvt3d/maplibre-three-plugin)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T13:50:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** a bridge plugin that cleverly connects MapLibre GL JS with Three.js, enabling developers to implement 3D rendering and animation on maps.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dvt3d/maplibre-three-plugin

### [frenchtouchXR/ithaca-4dgs-unity](https://github.com/frenchtouchXR/ithaca-4dgs-unity)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T20:51:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time 4D Gaussian Splatting rendering and asset generation for Unity (URP), with full 3DGS/4DGS compatibility. Fork of aras-p/UnityGaussianSplatting, extended with temporal playback support.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frenchtouchXR/ithaca-4dgs-unity

### [OC-DEV74/Phase-DGS](https://github.com/OC-DEV74/Phase-DGS)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T03:51:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video (NeurIPS 2026)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/OC-DEV74/Phase-DGS

### [stechdrive/camera-frames](https://github.com/stechdrive/camera-frames)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T22:34:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Japanese animation layout, camera-frame composition, and export app for Gaussian Splat scenes.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/stechdrive/camera-frames

### [floodnet666/isabella-desktop](https://github.com/floodnet666/isabella-desktop)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T09:45:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive 3D Gaussian Splatting (3DGS) desktop companion for Windows 11 with WGPU GPU deformers, Win32 borderless transparency, and local multimodal voice pipeline.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/floodnet666/isabella-desktop

### [[extension] Add Custom Attribute Extension via ZSTD Skippable Frames (#107) * first pass * fix wasm custom attribute conversion * decode filter * fix test number * update quantized bits to 16 * add test](https://github.com/nianticlabs/spz/commit/b56333f5135c7ce4026a1237fcb227d35f8a6557)

- **主题：** 压缩与轻量化
- **来源：** GitHub · NianticLabs/spz
- **发布时间/更新时间：** 2026-11-09T19:48:05Z
- **更新判定：** 代码实质更新
- **核心内容：** [extension] Add Custom Attribute Extension via ZSTD Skippable Frames (#107) * first pass * fix wasm custom attribute conversion * decode filter * fix test number * update quantized bits to 16 * add test
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/NianticLabs/spz

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T05:53:18Z
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
- **发布时间/更新时间：** 2026-11-09T16:38:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [Hosi121/rangle](https://github.com/Hosi121/rangle)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T09:00:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** rangle = replay + angle. A free-viewpoint sports highlight platform with cloud ML and mobile Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Hosi121/rangle

### [Mario-Hero/3dgs-sog-converter](https://github.com/Mario-Hero/3dgs-sog-converter)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:08:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3dgs ply to compressed sog/ply converter
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mario-Hero/3dgs-sog-converter

### [k-harikumar/PLS-GS](https://github.com/k-harikumar/PLS-GS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T06:28:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Probabilistic Lidar Scaffolds for Compact, Surface-Aligned Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/k-harikumar/PLS-GS

### [sivan7zZ/3DGS-COMPRESSION](https://github.com/sivan7zZ/3DGS-COMPRESSION)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:29:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sivan7zZ/3DGS-COMPRESSION

### [fenghuayumo/photara-studio](https://github.com/fenghuayumo/photara-studio)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T02:58:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** a powerful and efficient 3d spatial capture tool , video/image to splat to mesh ,cross-vendor, Vulkan or CUDA
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fenghuayumo/photara-studio

### [timfennell/vintage-click](https://github.com/timfennell/vintage-click)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T02:31:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 1970s 35 mm SLR photography game inside 3D Gaussian splat scans, for Apple silicon Macs. Lens optics made by the renderer, film stocks, tungsten lighting, a light table and loupe.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timfennell/vintage-click

### [anticipate218/twin-studio](https://github.com/anticipate218/twin-studio)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:21:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 度量约束与证据驱动的城市三维建模工作台 | Gaussian Splatting, evidence-aware materials and procedural modeling.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/anticipate218/twin-studio

### [jesusluque/splat2mesh](https://github.com/jesusluque/splat2mesh)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T03:00:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting → UV-textured USD mesh, automated (Apache-2.0)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jesusluque/splat2mesh

### [SplatAnything Introduces Gaussian Spacing Normalization for 3D Reconstruction](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6af2ddb8184542e5b00154e1a75bc56a&url=https%3a%2f%2fblockchain.news%2fnews%2fsplatanything-gaussian-spacing-normalization&c=8266987965222904403&mkt=en-us)

- **主题：** 几何/材质/光照
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-09T18:48:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** SplatAnything applies Gaussian Spacing Normalization to enhance feed-forward 3D Gaussian Splatting across diverse scenes and viewpoints.
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [caiyuanhao1998/Open-DiffusionGS](https://github.com/caiyuanhao1998/Open-DiffusionGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T22:52:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction (ICCV 2025)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/caiyuanhao1998/Open-DiffusionGS

### [rsasaki0109/visloc-rs](https://github.com/rsasaki0109/visloc-rs)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:07:39Z
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
- **发布时间/更新时间：** 2026-11-10T06:42:15Z
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
- **发布时间/更新时间：** 2026-11-10T07:37:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [zdwww/Wheat-3DGS](https://github.com/zdwww/Wheat-3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T13:31:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zdwww/Wheat-3DGS

### [enhansome/enhansome-NeRF-and-3DGS-SLAM](https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T04:38:51Z
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
- **发布时间/更新时间：** 2026-11-10T03:51:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS Reconstruction of UCLA Gateway Plaza from unstaged outdoor scene video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS

### [Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING](https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T05:13:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T03:14:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [timeDNAtime/S2A-GS](https://github.com/timeDNAtime/S2A-GS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T11:59:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a project on 3D reconstruction of ceramics based on an improved 3DGS method.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timeDNAtime/S2A-GS

### [Farida-gaber44/sparse-view-3dgs-ablation](https://github.com/Farida-gaber44/sparse-view-3dgs-ablation)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T12:20:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Farida-gaber44/sparse-view-3dgs-ablation

### [suin-park/Whik](https://github.com/suin-park/Whik)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:54:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WHIK Studio: free node-based video compositing for Windows, with 3D Gaussian splat (3DGS) editing. Manual in Korean, English, Japanese and Chinese at whik.co.kr/manual. Preview, updated weekly.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/suin-park/Whik

### [satyaba/gaussian-splatting](https://github.com/satyaba/gaussian-splatting)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T08:20:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SGDense-3DGS: segmentation-guided density control of 3D Gaussian Splatting (thesis work)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/satyaba/gaussian-splatting

### [Fetch zlib 1.3.2 from zlib.net/fossils (#110) zlib.net only serves the latest release at the top level and moves older ones to /fossils/, so https://zlib.net/zlib-1.3.2.tar.gz now 404s and any build without a system zlib fails at configure time. Same tarball, so the URL_HASH is unchanged.](https://github.com/nianticlabs/spz/commit/855173912dee2a48cb539657f46c4ade775f48c9)

- **主题：** 实时渲染与展示
- **来源：** GitHub · NianticLabs/spz
- **发布时间/更新时间：** 2026-11-09T22:10:34Z
- **更新判定：** 代码实质更新
- **核心内容：** Fetch zlib 1.3.2 from zlib.net/fossils (#110) zlib.net only serves the latest release at the top level and moves older ones to /fossils/, so https://zlib.net/zlib-1.3.2.tar.gz now 404s and any build without a system zlib fails at configure time. Same tarball, so the URL_HASH is unchanged.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/NianticLabs/spz

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T06:36:31Z
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
- **发布时间/更新时间：** 2026-11-10T02:14:54Z
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
- **发布时间/更新时间：** 2026-11-09T13:25:07Z
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
- **发布时间/更新时间：** 2026-11-10T03:58:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [MAdrid1011/SCARF](https://github.com/MAdrid1011/SCARF)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T04:07:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Generalized 3DGS Inference Accerlator
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MAdrid1011/SCARF

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T07:10:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Mohith26/livedirt](https://github.com/Mohith26/livedirt)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T06:04:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A neural job site you can dig into: 3DGS capture + earthwork physics, grade control, simulated lidar/camera, autonomous trenching, MCAP export. Live: livedirt.mohithgajjela.com
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Mohith26/livedirt

### [simizar/3dgs-oauth-site](https://github.com/simizar/3dgs-oauth-site)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T04:45:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/simizar/3dgs-oauth-site

### [AlexiosBluffMara/isu-brain-visualizer](https://github.com/AlexiosBluffMara/isu-brain-visualizer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T02:47:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ISU Cortex / Brain Visualizer: educational 2D MRI, 3D MRI and Gaussian splat viewer, with 85 public FCD cases
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AlexiosBluffMara/isu-brain-visualizer

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T02:04:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VR/desktop player for openftgs models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs-xr

### [Markgatcha/idol-3d-objects](https://github.com/Markgatcha/idol-3d-objects)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T01:16:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Prompt -> 2K transparent PNG (Qwen Image 2.1 Turbo in ComfyUI) -> 3D Gaussian splat .ply (Idol). MIT code.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Markgatcha/idol-3d-objects

### [01110000/h3d](https://github.com/01110000/h3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T22:45:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** H3D: interactive 3D Gaussian Splatting torus viewer built with Dioxus Native (Windows, Linux, macOS, Android, iOS)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/01110000/h3d

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T08:55:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [Recover cleanly when the export GPU device is lost (#1094)](https://github.com/playcanvas/supersplat/commit/c061d0d6a56c730487f90e7683eee09422864e56)

- **主题：** GPU与加速实现
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-11-09T12:19:23Z
- **更新判定：** 代码实质更新
- **核心内容：** Recover cleanly when the export GPU device is lost (#1094)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [ViaChe78/Professional-3DGS-Studio](https://github.com/ViaChe78/Professional-3DGS-Studio)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T17:16:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Professional 3DGS Studio
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ViaChe78/Professional-3DGS-Studio

### [caiyuanhao1998/X-Gaussian](https://github.com/caiyuanhao1998/X-Gaussian)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T03:45:47Z
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
- **发布时间/更新时间：** 2026-11-09T14:17:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T09:45:13Z
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
- **发布时间/更新时间：** 2026-11-10T03:11:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [BrandonL00/3DGS-VPCC-Encoding](https://github.com/BrandonL00/3DGS-VPCC-Encoding)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T01:31:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/BrandonL00/3DGS-VPCC-Encoding

### [sssuer77/light-3dgs-system](https://github.com/sssuer77/light-3dgs-system)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-10T01:00:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sssuer77/light-3dgs-system

### [joezgao/seen-from-twelve-sides](https://github.com/joezgao/seen-from-twelve-sides)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T21:06:13Z
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
- **发布时间/更新时间：** 2026-11-09T21:05:07Z
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
- **发布时间/更新时间：** 2026-11-09T19:09:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/5undura/3DGS

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-09T09:53:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

### [Chole12/IEEE-3DGS-IQA-2](https://huggingface.co/Chole12/IEEE-3DGS-IQA-2)

- **主题：** 其他
- **来源：** Hugging Face 模型
- **发布时间/更新时间：** 2026-11-09T09:44:25Z
- **更新判定：** 模型更新
- **核心内容：** 近期更新的模型；标签：safetensors, internvl_chat, custom_code, region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | degraded: HTTPError: HTTP Error 429: Unknown Error |
| GitHub | ok: 60 |
| Hugging Face | ok: 1 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 1 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 0 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

