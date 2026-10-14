---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-13T08:48:10Z
window_end_utc: 2026-10-14T06:57:08Z
generated_at_utc: 2026-10-14T06:57:08Z
item_count: 74
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-14

**统计窗口：** 2026-10-13T08:48:10Z — 2026-10-14T06:57:08Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **74** 项去重后的有效线索：真正新增论文 **3** 项、实质论文修订 **2** 项、代码/版本/项目更新 **69** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [I2O2I-Nav: A Benchmark with a Modular Agent for Long-Horizon Indoor-to-Outdoor-to-Indoor Navigation](https://arxiv.org/abs/2610.18307v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [Back to the Future: Reverse-Consequence Modeling for Long-Horizon Particle Dynamics](https://arxiv.org/abs/2610.18168v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [CoTL: Compact Token Learning for 3D Scene Representation](https://arxiv.org/abs/2610.18446v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877v2) | 实质修订 | arXiv | R2/E0 | P1 |
| 5 | [Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v4) | 实质修订 | arXiv | R2/E0 | P1 |

## 分类详述

### [Back to the Future: Reverse-Consequence Modeling for Long-Horizon Particle Dynamics](https://arxiv.org/abs/2610.18168v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-13T11:12:54Z
- **更新判定：** 真正新增
- **核心内容：** Accurate prediction of object trajectories is fundamental to mechanical understanding and robotic control. However, autoregressive models inherently suffer from cumulative errors, leading to severe drift in long-horizon rollouts. Observing that in many physical systems with dissipative or convergence-to-rest behavior, the final states are often more predictable than transient dynamics (e.g., a sliding object resting under friction or a pendulum stabilizing at equilibrium), we propose ReStep, a cascaded approach that reverses the conventional forward-prediction paradigm. ReStep first employs a stochastic model to directly predict the final state, then leverages Anchored Diffusion to generate goal-conditioned intermediate trajectories. By conditioning on both ''boundary states'', it effectively constrains dynamics and reduces uncertainty, producing physically plausible and temporally coherent transitions. We further integrate ReStep dynamics as the physical engine within a 3D Gaussian S…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.18168v1

### [CoTL: Compact Token Learning for 3D Scene Representation](https://arxiv.org/abs/2610.18446v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-13T14:17:30Z
- **更新判定：** 真正新增
- **核心内容：** We present CoTL, a framework that learns a compact set of tokens that preserves scene geometry and appearance from unposed multi-view images. Our encoder compresses the input images into small per-view sets of latent tokens that aggregate information across views to form a view-consistent scene representation. Each additional view expands the representation with only a small, resolution-independent set of tokens, allowing its capacity to grow with the available observations. To force this compact bottleneck to retain sufficient scene information, a query-based Gaussian decoder uses scene-independent queries to attend to the learned tokens and recover an explicit, renderable set of 3D Gaussian primitives. Novel-view rendering supervision trains the compact representation end to end through the reconstructed Gaussian scene. Experiments on \retenk{} and ACID show that the resulting compact, unstructured token set supports competitive novel-view synthesis and can serve as the latent space…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.18446v1

### [Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v4)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-13T11:35:27Z
- **更新判定：** 实质修订
- **核心内容：** Drone-view geo-localization (DVGL) typically assumes access to satellite imagery during task-specific development. We study a late-arriving-gallery setting, where model development relies only on grouped source UAV observations and the target satellite gallery remains unavailable until the model is frozen. We propose \ours, Orbit Completion Learning, which uses source-side multi-view geometry as privileged training information while preserving image-only deployment. OCL reconstructs each source scene using structure-from-motion and 3D Gaussian Splatting, and renders canonical complementary views to complete its observation orbit. An exponential-moving-average teacher aggregates the completed orbit into a scene-level target, while a variable-cardinality student learns to recover this target from partial observations through distillation and contrastive learning. At inference, the frozen student independently encodes UAV queries and satellite gallery images using the same single-image p…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.01581v4

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:46:39Z
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
- **发布时间/更新时间：** 2026-10-13T22:08:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [samaust/openftgs](https://github.com/samaust/openftgs)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T22:01:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on Neural3DV, ENeRF-Outdoor and SelfCap.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [areinot/gaussqueue](https://github.com/areinot/gaussqueue)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T04:49:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Folder-watching Gaussian splat training queue for macOS: drop captures in an (iCloud) inbox, Brush trains them, results land in an outbox. Localhost dashboard + iMessage progress.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/areinot/gaussqueue

### [0xFEEDC0DE/industrial-digital-twin-mobile](https://github.com/0xFEEDC0DE/industrial-digital-twin-mobile)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T02:27:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mobile 3D scanning tool for creating industrial digital twins from device cameras with texture capture, Gaussian splatting, and AR/VR training capabilities
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/0xFEEDC0DE/industrial-digital-twin-mobile

### [DhruvDS2/gsplat](https://github.com/DhruvDS2/gsplat)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T23:43:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CPU-only renderer for pretrained 3D Gaussian Splatting scenes (CS 4361 final project)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DhruvDS2/gsplat

### [chalk-ai/gaussian-splatting](https://github.com/chalk-ai/gaussian-splatting)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T18:56:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Train 3D Gaussian Splatting live on one GPU with Chalk, watch it converge, and orbit the result in your browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chalk-ai/gaussian-splatting

### [qherau/3DGS-Calib](https://github.com/qherau/3DGS-Calib)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:52:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Site for the paper "3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration".
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/qherau/3DGS-Calib

### [iamkyledang/stag_gs](https://github.com/iamkyledang/stag_gs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T04:04:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of STAG-GS: Sparse Temporal Anchor Learning for Dynamic 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/iamkyledang/stag_gs

### [ANetResearch/ANet-Drone4D](https://github.com/ANetResearch/ANet-Drone4D)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T20:22:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-world 4D simulation for multi-agent drones: city-scale point-cloud digital twins, drone swarm simulation and swarm control, target perception and an interactive sandbox in the browser. PX4-style flight model; Gazebo Sim, LiDAR and 3DGS in development and research.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ANetResearch/ANet-Drone4D

### [MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877v2)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-13T12:48:29Z
- **更新判定：** 实质修订
- **核心内容：** 3D representations are fundamental for scene rendering, understanding, and interaction. Approaches like Neural Radiation Fields and 3D Gaussian Splatting achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into object level, requiring additional segmentation or grouping. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that re…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.03877v2

### [hhddiusd-cloud/Mobile-GS](https://github.com/hhddiusd-cloud/Mobile-GS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:18:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Deliver real-time Gaussian splatting for 3D rendering on mobile devices using CUDA for efficient and fast visual processing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hhddiusd-cloud/Mobile-GS

### [Coryimportant7727/efficient-gaussian-appearance](https://github.com/Coryimportant7727/efficient-gaussian-appearance)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:36:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Accelerate 3D Gaussian Splatting with compact neural appearance models for sharper, faster view-dependent rendering.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Coryimportant7727/efficient-gaussian-appearance

### [animu-sphere/hydra-merlin](https://github.com/animu-sphere/hydra-merlin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:29:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A lightweight, host-neutral raster renderer for USD Hydra, powered by Vulkan and Metal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/animu-sphere/hydra-merlin

### [UHD-World-Association/spatial-vivid-egsc](https://github.com/UHD-World-Association/spatial-vivid-egsc)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T04:55:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An efficient reference 3DGS codec for Spatial Vivid
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/UHD-World-Association/spatial-vivid-egsc

### [I2O2I-Nav: A Benchmark with a Modular Agent for Long-Horizon Indoor-to-Outdoor-to-Indoor Navigation](https://arxiv.org/abs/2610.18307v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-13T12:52:13Z
- **更新判定：** 真正新增
- **核心内容：** Service and delivery robots often need to complete long-horizon navigation missions spanning indoor and outdoor environments. Existing embodied navigation benchmarks primarily evaluate isolated stages or partial cross-domain journeys, providing limited support for assessing how heterogeneous navigation capabilities compose under continuous execution. We introduce I2O2I-Nav, a physics-enabled benchmark of 20 real-world composite scenes spanning over 115,000 square meters across multiple buildings and floors, with aligned 3DGS rendering and collision geometry. Its three-level evaluation progresses from independent primitives to two-stage compositions and complete four-stage I2O2I missions. Each stage starts from its predecessor's actual endpoint, while stage-conditional metrics track completion and localize failures along the mission. We further propose the MODULAR-Agent that coordinates frozen navigation policies through completion verification, stage handoffs, and bounded recovery. Ev…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.18307v1

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T10:45:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [2072508371/truck-3dgs-demo](https://github.com/2072508371/truck-3dgs-demo)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T02:30:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive 3D Gaussian Splatting demo with color, depth, and normal visualization.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/2072508371/truck-3dgs-demo

### [husmen8/bozkir](https://github.com/husmen8/bozkir)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T22:40:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Kilometres of terrain from a few square metres of captured Gaussian-splat ground, with materials placed by the shape of the land. Runs in the browser.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/husmen8/bozkir

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T21:52:15Z
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
- **发布时间/更新时间：** 2026-10-14T06:08:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SfM, visual-inertial SLAM, 3D Gaussian Splatting and localization in pure Rust
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rsasaki0109/visloc-rs

### [darshmenon/rosnav](https://github.com/darshmenon/rosnav)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:20:27Z
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
- **发布时间/更新时间：** 2026-10-14T02:23:13Z
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
- **发布时间/更新时间：** 2026-10-14T01:56:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [tobyje541/Complex-Valued_2D_Gaussian_Representation](https://github.com/tobyje541/Complex-Valued_2D_Gaussian_Representation)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:28:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Represent complex-valued 2D Gaussians to improve reconstruction quality and efficiency in computer-generated holography.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tobyje541/Complex-Valued_2D_Gaussian_Representation

### [e-mric/BeThereCentral](https://github.com/e-mric/BeThereCentral)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T21:33:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source Kotlin Multiplatform app for exploring and navigating shared buildings, with pixel-art maps, Gaussian splatting, QR checkpoints and cooperative treasure hunts. Built for a proposed BeCentral experience.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/e-mric/BeThereCentral

### [yfwang0824/yfwang-MCSplat](https://github.com/yfwang0824/yfwang-MCSplat)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:52:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes(NeurIPS2026 Poster)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yfwang0824/yfwang-MCSplat

### [warpgatelabs/gauss-cannon](https://github.com/warpgatelabs/gauss-cannon)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:46:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gauss Cannon is a suite of utilities for Gaussian Splat generation based on Blender scenes.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/warpgatelabs/gauss-cannon

### [LioQing/wgpu-3dgs-editor](https://github.com/LioQing/wgpu-3dgs-editor)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T14:06:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting Editor written in Rust using wgpu.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LioQing/wgpu-3dgs-editor

### [tedchao/ReparamGS-Palette](https://github.com/tedchao/ReparamGS-Palette)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:21:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Public code release for: Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing (SIGGRAPH Asia 2026) [Cheng-Kang Ted Chao, Yotam Gingold]
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tedchao/ReparamGS-Palette

### [MisterE123/spark-tour-studio](https://github.com/MisterE123/spark-tour-studio)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T23:18:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows Gaussian splat tour editor and locally bundled WebXR viewer powered by Spark
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MisterE123/spark-tour-studio

### [Harshtech1/GaussTwin-Semantic-3DGS-World-Model-for-Robotics](https://github.com/Harshtech1/GaussTwin-Semantic-3DGS-World-Model-for-Robotics)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T20:09:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Harshtech1/GaussTwin-Semantic-3DGS-World-Model-for-Robotics

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:08:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high performance 3DGS renderer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-viewer

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T02:39:15Z
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
- **发布时间/更新时间：** 2026-10-14T02:20:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [Visionary-Laboratory/visionary](https://github.com/Visionary-Laboratory/visionary)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T10:28:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Visionary-Laboratory/visionary

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T16:45:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 900 arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [LioQing/wgpu-3dgs-viewer](https://github.com/LioQing/wgpu-3dgs-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T15:33:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A 3D Gaussian Splatting Viewer written in Rust using wgpu.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LioQing/wgpu-3dgs-viewer

### [Archerkattri/splatreg](https://github.com/Archerkattri/splatreg)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T16:52:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Register Gaussian splats: align & merge two 3DGS scans into one SE(3)/Sim(3) frame — classical, learned, or zero-shot (BUFFER-X) seeds + splat-native refine. pip install splatreg.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/splatreg

### [LostBeard/SpawnScene](https://github.com/LostBeard/SpawnScene)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T01:26:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Create 3D gaussian splat scenes entirely in your browser.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LostBeard/SpawnScene

### [Shawn100861224/web3d-lab](https://github.com/Shawn100861224/web3d-lab)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T17:11:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS 在线重建查看器 + 个人主页（郑州大学双足实验室 3D 方向考核作品）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Shawn100861224/web3d-lab

### [LioQing/wgpu-3dgs-core](https://github.com/LioQing/wgpu-3dgs-core)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T13:30:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting Library written in Rust using wgpu.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LioQing/wgpu-3dgs-core

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T13:07:39Z
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
- **发布时间/更新时间：** 2026-10-13T11:38:37Z
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
- **发布时间/更新时间：** 2026-10-14T01:35:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Swift SDK for the Splat API — ARKit LiDAR capture + 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/splat3d/splat-swift-sdk

### [kumodot/splat-tools](https://github.com/kumodot/splat-tools)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:56:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Video to Gaussian Splat, then walk inside it on a Quest 3. SplatWalk (WebXR viewer) + SplatForge (video to PLY on Windows).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kumodot/splat-tools

### [gsmark36/complex-valued-quadratic-phase-gaussian](https://github.com/gsmark36/complex-valued-quadratic-phase-gaussian)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T01:08:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Code for Hologram Representation via Quadratic Phase Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gsmark36/complex-valued-quadratic-phase-gaussian

### [parodiniccolo/claude-3dgs-view](https://github.com/parodiniccolo/claude-3dgs-view)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T16:32:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Preview 3D Gaussian splats in a Claude Code pane: a mod rendering .ply/.spz/.splat scenes with Spark in headless Chrome, orbit with the mouse
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/parodiniccolo/claude-3dgs-view

### [biqiu993/3dgs-object-cleanup](https://github.com/biqiu993/3dgs-object-cleanup)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T13:47:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS toolkit for self-captured objects: removes floaters, black patches and needle artifacts
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/biqiu993/3dgs-object-cleanup

### [smartonTT/gsplat_tt](https://github.com/smartonTT/gsplat_tt)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:53:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Port of Gaussian Splatting to Tenstorrent
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/smartonTT/gsplat_tt

### [squoraishee/prototypes](https://github.com/squoraishee/prototypes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:50:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Small browser prototypes: The Luminous Basin (Gaussian splat landscape) and Snakephoria (party snake game)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/squoraishee/prototypes

### [Test5p1398/FCG](https://github.com/Test5p1398/FCG)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:35:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Develop a .NET REST API for user registration, JWT authentication, game catalog management, and user game library with PostgreSQL.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Test5p1398/FCG

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:28:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Streetjk/landcros-forrestdale](https://github.com/Streetjk/landcros-forrestdale)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:00:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SiteNav 3D Gaussian Splat site viewer — Landcros Forrestdale demo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Streetjk/landcros-forrestdale

### [kavehkamali/frontier-fieldnotes](https://github.com/kavehkamali/frontier-fieldnotes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T00:54:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Creative AI research, interactive ML explanations, and weekly publishing kits. 3D Gaussian splatting, video, voice and AI filmmaking.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kavehkamali/frontier-fieldnotes

### [3XyzMedia/VIEWER](https://github.com/3XyzMedia/VIEWER)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T23:21:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Любительские модели 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3XyzMedia/VIEWER

### [s0fargone/3DGS](https://github.com/s0fargone/3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T22:41:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/s0fargone/3DGS

### [JoshuaParfitt/gaussian-splatting-lab](https://github.com/JoshuaParfitt/gaussian-splatting-lab)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T22:06:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive 3D Gaussian splatting playground built with Three.js and custom GLSL shaders, featuring real-time rendering, adjustable Gaussian parameters, and point-based rendering comparisons.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JoshuaParfitt/gaussian-splatting-lab

### [Post-Secondary-Digital-Commons/psdc-media](https://github.com/Post-Secondary-Digital-Commons/psdc-media)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T21:24:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open media and spatial fabric for images, video, 3D, and Gaussian splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Post-Secondary-Digital-Commons/psdc-media

### [changying1/sparse-3dgs](https://github.com/changying1/sparse-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T15:51:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/changying1/sparse-3dgs

### [vrgiser/video-to-3dgs](https://github.com/vrgiser/video-to-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T11:02:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** video-to-3dgs
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/vrgiser/video-to-3dgs

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T08:48:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [lukehollis/sphr](https://github.com/lukehollis/sphr)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T04:54:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open, hackable 3d digital twin builder that supports 3d gaussian splatting, 360 images, and vfx
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lukehollis/sphr

### [manycoretech/egs](https://github.com/manycoretech/egs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T03:10:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [NikoRina/real2sim-eval](https://github.com/NikoRina/real2sim-eval)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T06:54:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 🤖 Evaluate real robot policies using Gaussian splatting for soft-body simulations, enhancing the understanding of robot interactions in complex environments.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NikoRina/real2sim-eval

### [BocchiSlice/Bocchi-Slice](https://github.com/BocchiSlice/Bocchi-Slice)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:40:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Browser-based 3D visualization for CT/MRI, 3D models including 3DGS — one HTML file, offline. ブラウザだけで動くCT・3Dモデル(3DGSを含む）の3Dビジュアライゼーションツール（ローカル・オフライン対応）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/BocchiSlice/Bocchi-Slice

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T09:28:36Z
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
- **发布时间/更新时间：** 2026-10-14T06:50:30Z
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
- **发布时间/更新时间：** 2026-10-14T06:22:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Standalone Gaussian splatting worker and pipeline for Guerrilla
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pstoebenau/guerrilla-worker

### [beichuchu/3dgs](https://github.com/beichuchu/3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-14T05:26:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/beichuchu/3dgs

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-13T17:47:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

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

