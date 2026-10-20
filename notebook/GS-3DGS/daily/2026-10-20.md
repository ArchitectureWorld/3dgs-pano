---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-19T07:10:43Z
window_end_utc: 2026-10-20T06:58:08Z
generated_at_utc: 2026-10-20T06:58:08Z
item_count: 75
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-20

**统计窗口：** 2026-10-19T07:10:43Z — 2026-10-20T06:58:08Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **75** 项去重后的有效线索：真正新增论文 **3** 项、实质论文修订 **3** 项、代码/版本/项目更新 **69** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](https://arxiv.org/abs/2610.26067v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision](https://arxiv.org/abs/2610.26508v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [sparkjsdev/spark v2.4.0](https://github.com/sparkjsdev/spark/releases/tag/v2.4.0) | 正式版本发布 | GitHub Release · sparkjsdev/spark | E2 | P0 |
| 5 | [ZipSplat: Fewer Gaussians, Better Splats](https://arxiv.org/abs/2606.05102v3) | 实质修订 | arXiv | R2/E0 | P1 |

## 分类详述

### [PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](https://arxiv.org/abs/2610.26067v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T09:25:55Z
- **更新判定：** 真正新增
- **核心内容：** Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces without per-object network training. To learn these subspaces without simulation trajectories, we develop a Physics-Informed Self-Supervised Learning strategy that combines skinning-field normalization with conflict-aware gradient correction, stabilizing joint optimization under physical and orthogonality constraints. The learned representation supports efficient reduced dynamics with user control and contact interactions, together with direct animation binding to meshes, point clouds, and 3D Gaussians. For prescribed rig animation, we further introduce a self-supervised comp…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.26067v1

### [Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision](https://arxiv.org/abs/2610.26508v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T14:44:16Z
- **更新判定：** 真正新增
- **核心内容：** Existing high-speed navigation systems for micro aerial vehicles (MAVs) commonly rely on depth cameras, stereo vision, or LiDAR to obtain explicit geometric information, while monocular cameras offer a lighter and lower-cost alternative. However, monocular flight remains challenging because RGB images offer no direct metric cues and visual appearance varies considerably across environments. We propose a geometry-aware monocular visual planning framework that predicts trajectories from two image frames, their relative pose, and the MAV state. Without explicitly reconstructing depth, the proposed method complements the downstream planning objective with feature-level geometric supervision by transferring the planning-relevant representation learned by a privileged depth expert to the RGB planner through cross-modal distillation. The framework first trains a depth-based geometric expert, then distills its planning features into a monocular branch using paired RGB-D observations, and fina…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.26508v1

### [sparkjsdev/spark v2.4.0](https://github.com/sparkjsdev/spark/releases/tag/v2.4.0)

- **主题：** 训练与优化
- **来源：** GitHub Release · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-20T04:13:18Z
- **更新判定：** 正式版本发布
- **核心内容：** ## 2.4.0 (Oct 19, 2026) Bug fixes and improvements ### Enhancements - Add SPZ v4 read support (#484) (@udwinj, @mrxz) - Decouple and abstract paged splat load logic from `PagedSplat` into `FetchSource` that retrieves data from in-memory file, URL or any other custom mechanism (#463) (@mrxz, @xohm , @oscarlorentzon) - Switch to `flate2` from `zlib-rs` backend for RAD deflate compression. ~50% faster compression, ~2-5% smaller outputs and ~20% faster decoding (#474) (@mrxz, @oscarlorentzon) - Replace `miniz_oxide` with `flate2` for Gzip (de)compression of SPZ files. Remove `miniz_oxide` as dependency (#485) (@mrxz) - Address stutter during animations. Skip unnecessary splat sortings if the splat buffer needs or has changed like for example when LoD levels change or splats animate / move (#347) (#460) (@oscarlorentzon, @mrxz) - Refactor `PagedSplats` into its own separate file (#462) (@mrxz) - Remove outdated Github workflows CI commands (#464) (@mrxz) - Add Rust linter (#414) (@mrxz) -…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [ZipSplat: Fewer Gaussians, Better Splats](https://arxiv.org/abs/2606.05102v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T14:30:39Z
- **更新判定：** 实质修订
- **核心内容：** Feed-forward 3D Gaussian Splatting reconstructs scenes from images in seconds. Pixel-aligned methods keep every Gaussian grounded in an observation, but produce redundant, potentially misaligned Gaussians across views. Token-based methods instead aggregate all views into a fixed set of learned tokens but lack explicit observation support and use a fixed reconstruction budget. We introduce ZipSplat, a method that predicts a compact, observation-grounded scene representation whose size is set at inference. It derives each scene token from an image patch rather than a learned query, and decodes it into freely placed 3D Gaussians. Tokens across views are merged into a compact set whose size is adjustable at inference. However, without geometric supervision, decoded Gaussians can drift from their source patch, and merging can mix tokens from different surfaces. We therefore introduce two geometric losses to ground and shape this representation. A cone loss ties each token's Gaussians to it…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.05102v3

### [TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation](https://arxiv.org/abs/2610.23050v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T16:38:57Z
- **更新判定：** 实质修订
- **核心内容：** Recent progress in 3D generation has motivated growing interest in compact generative representations of complex 3D scenes. For native 3D Gaussian scenes, however, learning such representations remains challenging due to widely varying primitive counts, nonuniform spatial density, and differences in geometry and appearance even among spatially neighboring primitives. In this work, we introduce TriFold, a native 3D Gaussian VAE that encodes Gaussian scenes into a fixed-layout triplane latent and jointly reconstructs their geometry and appearance. The key insight is to impose structural regularity on the latent space while preserving the spatial adaptivity of the underlying Gaussians. During encoding, we use cell-wise learned queries to aggregate projected Gaussians into multiple slots per cell, reducing the information loss caused by single-feature pooling. During decoding, occupancy prediction identifies active regions, where query-based set prediction and candidate selection reconstr…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.23050v2

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:55:41Z
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
- **发布时间/更新时间：** 2026-10-20T06:39:54Z
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
- **发布时间/更新时间：** 2026-10-20T06:56:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on openftgs-synth datasets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [shuta-ochiai/Splatelier](https://github.com/shuta-ochiai/Splatelier)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:48:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Capture, train and view 3D Gaussian Splats entirely on your iPhone.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/shuta-ochiai/Splatelier

### [anomalisfree/GS_Server](https://github.com/anomalisfree/GS_Server)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T05:52:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting Training Server - automated COLMAP + Brush pipeline
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/anomalisfree/GS_Server

### [areinot/gaussqueue](https://github.com/areinot/gaussqueue)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T21:05:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Folder-watching Gaussian splat training queue for macOS: drop captures in an (iCloud) inbox, Brush trains them, results land in an outbox. Localhost dashboard + iMessage progress.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/areinot/gaussqueue

### [Aryan241/Clean-Splate](https://github.com/Aryan241/Clean-Splate)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:03:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Training-free distractor removal for 3D Gaussian Splatting using SAM 2 masks and multi-view voting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Aryan241/Clean-Splate

### [liuqizi/3DGS-paper](https://github.com/liuqizi/3DGS-paper)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:19:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Dense-Prior-Guided Densification and Geometric Pruning for 3D Gaussian Splatting Scene Reconstruction
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/liuqizi/3DGS-paper

### [Soham-Gaonkar/Comparing-InstantNGP-and-3DGS](https://github.com/Soham-Gaonkar/Comparing-InstantNGP-and-3DGS)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T19:07:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Custom dataset of a static scene and comparison between instantngp models and 3d gaussian splatting models on reconstruction quality, rendering time , model size and training time
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Soham-Gaonkar/Comparing-InstantNGP-and-3DGS

### [deshengdesheng/tower-3dgs-fe-dynamics](https://github.com/deshengdesheng/tower-3dgs-fe-dynamics)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:33:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible source code for image-based 3DGS tower reconstruction, terrain processing, FE displacement registration, and dynamic visualization.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/deshengdesheng/tower-3dgs-fe-dynamics

### [Cyberyyc/HoloSplat-3DGS-Robot-Digital-Twin](https://github.com/Cyberyyc/HoloSplat-3DGS-Robot-Digital-Twin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T05:32:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting scene registration and ROS-driven mobile-manipulator digital twin modules for HoloLens spatial interaction.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Cyberyyc/HoloSplat-3DGS-Robot-Digital-Twin

### [Xget7/splatkit-ios](https://github.com/Xget7/splatkit-ios)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T05:11:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Metal Gaussian splatting SDK for iOS: Swift view, GPU visibility/radix, experimental LOD and hybrid tiles. MIT source and reproducible XCFramework.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit-ios

### [yimingjiang216-alt/sfm-3dgs-pipeline](https://github.com/yimingjiang216-alt/sfm-3dgs-pipeline)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T08:58:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Image -> COLMAP SfM -> 3D Gaussian Splatting -> novel view synthesis pipeline. Integration and environment debugging; COLMAP and 3DGS are upstream projects.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yimingjiang216-alt/sfm-3dgs-pipeline

### [SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T13:08:34Z
- **更新判定：** 真正新增
- **核心内容：** Recent advances in Gaussian splatting, 3D foundation models, and video-passthrough mixed reality offer unprecedented fidelity for capturing and blending physical and virtual worlds. However, established XR methods rely on polygon-based pipelines that treat physical and digital environments as separate domains, making seamless integration across recent novel representations difficult. Because splats lack explicit surface geometry, they impede standard graphics techniques necessary for cross-reality interactions, such as shadow or collision handling. Furthermore, while 3D foundation models can reconstruct physical objects on-the-fly into digital splats, current XR systems fall short of leveraging this capability for user experiences that transition seamlessly between physicality and virtuality. To address this, we organize XR as a multi-layered reality of interacting primitives, letting pixels and objects move across physical and digital boundaries. We contribute SplatXR, a Unity toolki…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.26338v1

### [GaussTrap: Stealthy Backdoor Attacks on 3D Gaussian Splatting for Targeted Scene Misperception](https://arxiv.org/abs/2504.20829v2)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-19T13:12:53Z
- **更新判定：** 实质修订
- **核心内容：** 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for real-time scene representation and novel view synthesis, gaining traction in safety-critical applications such as autonomous driving and AR/VR systems. However, the security vulnerabilities of 3DGS remain largely unexplored. In this paper, we conduct a comprehensive study of backdoor threats in 3DGS pipelines. We uncover an inherent security vulnerability in the adaptive density control mechanism of 3DGS, originally designed for detailed reconstruction, which enables attackers to induce localized gaussian proliferation, effectively embedding malicious backdoors into the scene geometry while remaining invisible from other viewpoints. To expose this threat, we propose GaussTrap, a novel stealthy poisoning framework tailored for 3DGS. GaussTrap operates in three stages (adversarial injection, geometric stabilization, and global fidelity restoration) to embed imperceptible yet adversarial Gaussian components into…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2504.20829v2

### [HwasikJeong/2Xplat](https://github.com/HwasikJeong/2Xplat)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:48:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of 2Xplat: Decoupling Geometry and Appearance Modeling for Feed-Forward 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/HwasikJeong/2Xplat

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T21:43:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 📚这个仓库是在arxiv上收集的有关VLN，VLA，World Model，SLAM，Gaussian Splatting,非线性优化等相关论文。每天都会自动更新！issue区域是最新10篇论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/luohongk/Embodied-AI-Daily

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T09:16:48Z
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
- **发布时间/更新时间：** 2026-10-20T06:38:36Z
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
- **发布时间/更新时间：** 2026-10-20T05:13:47Z
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
- **发布时间/更新时间：** 2026-10-19T14:45:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A photogrammetry pipeline for high-fidelity 3D object reconstruction from multi-view images.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Human-Augment-Analytics/porto-photogrammetry

### [lukhashka/AeroSplat-GIS](https://github.com/lukhashka/AeroSplat-GIS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T21:52:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** AeroSplat-GIS is a geospatial reconstruction and visualization framework designed for generating metrically accurate 3D terrain models from UAV imagery and simulation environments. The project combines traditional photogrammetry techniques with modern neural scene representations based on 3D Gaussian Splatting (3DGS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lukhashka/AeroSplat-GIS

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:46:38Z
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
- **发布时间/更新时间：** 2026-10-20T01:52:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [poiuyjie/water](https://github.com/poiuyjie/water)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:16:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 水下 3DGS 建图系统 · Time-to-Map：免离线 COLMAP，浑水边采集边建图，免 GT 米制化（ATE −65.5%）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/poiuyjie/water

### [LISA-VR/nola-posetraces](https://github.com/LISA-VR/nola-posetraces)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:34:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NoLa Aquarium / BelgianBeer posetrace videos and camera poses (Gaussian splatting)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/LISA-VR/nola-posetraces

### [imsquner/3dgs-reconstruction](https://github.com/imsquner/3dgs-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T13:50:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** RGB-D 3DGS reconstruction algorithms, reproducible adapters and interactive web viewer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/imsquner/3dgs-reconstruction

### [yfwang0824/mcsplat-project](https://github.com/yfwang0824/mcsplat-project)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:27:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes(NeurIPS2026 Poster)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yfwang0824/mcsplat-project

### [MisterE123/spark-tour-studio](https://github.com/MisterE123/spark-tour-studio)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:52:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Windows Gaussian splat tour editor and locally bundled WebXR viewer powered by Spark
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MisterE123/spark-tour-studio

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T05:20:03Z
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
- **发布时间/更新时间：** 2026-10-20T02:19:44Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Powerful web graphics runtime built on WebGL, WebGPU, WebXR and glTF
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [lueluelue12138/sharp-gui](https://github.com/lueluelue12138/sharp-gui)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:04:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A Beautiful 3D Spark GUI for apple ml-sharp
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lueluelue12138/sharp-gui

### [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T12:58:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 900 arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Xget7/splatkit](https://github.com/Xget7/splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:09:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time Gaussian splatting SDKs for Android/Vulkan, iOS/Metal and React Native, sharing a C++17 engine.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit

### [affromero/splattie-widget](https://github.com/affromero/splattie-widget)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T08:52:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive rigged 3D Gaussian Splatting web component - like Rive/Lottie for 3D.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/affromero/splattie-widget

### [Xget7/react-native-splatkit](https://github.com/Xget7/react-native-splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:20:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** React Native component for real-time Gaussian splatting: load an SPZ scene, pick a quality preset, and walk through it from JavaScript.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/react-native-splatkit

### [firefly1145141919810/cg-3dgs-baseline](https://github.com/firefly1145141919810/cg-3dgs-baseline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:56:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible original 3D Gaussian Splatting baseline and Chinese learning notes
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/firefly1145141919810/cg-3dgs-baseline

### [3XyzMedia/VIEWER](https://github.com/3XyzMedia/VIEWER)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:40:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Любительские модели 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3XyzMedia/VIEWER

### [Streetjk/landcros-forrestdale](https://github.com/Streetjk/landcros-forrestdale)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T05:44:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SiteNav 3D Gaussian Splat site viewer — Landcros Forrestdale demo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Streetjk/landcros-forrestdale

### [zjllllllllll/sharp-video](https://github.com/zjllllllllll/sharp-video)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:37:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Local RGB-D video to Gaussian splatting workbench and trajectory experiments.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zjllllllllll/sharp-video

### [kobingogo/spark-city-demo](https://github.com/kobingogo/spark-city-demo)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:35:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Spark City Demo · 3D Gaussian Splatting（three.js + Spark）三场景浏览
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kobingogo/spark-city-demo

### [thsdgsq/gs-merger](https://github.com/thsdgsq/gs-merger)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:05:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive multi-model 3D Gaussian Splatting alignment and merging using manual landmarks and Sim(3).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thsdgsq/gs-merger

### [kavehkamali/frontier-fieldnotes](https://github.com/kavehkamali/frontier-fieldnotes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:33:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Creative AI research, interactive ML explanations, and weekly publishing kits. 3D Gaussian splatting, video, voice and AI filmmaking.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kavehkamali/frontier-fieldnotes

### [santisiri/eternauta-online](https://github.com/santisiri/eternauta-online)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:20:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** El Eternauta Online — prototipo jugable en el navegador: Plaza de Mayo bajo la nevada mortal (Three.js + Gaussian splatting con Spark)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/santisiri/eternauta-online

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:02:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [Loppas/playcanvas-quake3](https://github.com/Loppas/playcanvas-quake3)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T01:40:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A port of ioquake to the Playcanvas engine with the added ability to render gaussian splat maps
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Loppas/playcanvas-quake3

### [christianandresramirezprieto-alt/cofre-electrico-3d](https://github.com/christianandresramirezprieto-alt/cofre-electrico-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T22:54:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Visor web 3D (Gaussian Splatting) de un cofre eléctrico de 50 kVA reconstruido a partir de video
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/christianandresramirezprieto-alt/cofre-electrico-3d

### [ahmeddoghri/splatgrade](https://github.com/ahmeddoghri/splatgrade)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T20:52:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splat artifact quality gate. Fixed a header-parsing crash and a silent-corruption bug where a truncated vertex row (missing opacity) was silently accepted as a clean, fully-opaque splat instead of being flagged.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ahmeddoghri/splatgrade

### [NhatMinh300306/3DGS-Spark-Vibe](https://github.com/NhatMinh300306/3DGS-Spark-Vibe)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T17:00:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NhatMinh300306/3DGS-Spark-Vibe

### [create3000/x_ite-spz-parser](https://github.com/create3000/x_ite-spz-parser)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T15:00:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS SPZ File Format Parser for X_ITE
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/create3000/x_ite-spz-parser

### [tykx1373/3DGS-Smart-System](https://github.com/tykx1373/3DGS-Smart-System)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T14:01:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS轻量化适配
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tykx1373/3DGS-Smart-System

### [create3000/x_ite-sog-parser](https://github.com/create3000/x_ite-sog-parser)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T13:57:23Z
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
- **发布时间/更新时间：** 2026-10-19T07:11:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [Add 2.4.0 version to changelog](https://github.com/sparkjsdev/spark/commit/561948f1200f41a4cd0dbc95de9ea125339deb62)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-20T04:04:54Z
- **更新判定：** 代码实质更新
- **核心内容：** Add 2.4.0 version to changelog
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Bump builds](https://github.com/sparkjsdev/spark/commit/c20276d8f81a62967194515d49e81fc1532ada26)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-10-20T04:04:27Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump builds
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [lukehollis/sphr](https://github.com/lukehollis/sphr)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T00:07:42Z
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
- **发布时间/更新时间：** 2026-10-20T06:42:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Mirror
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/egs

### [timfennell/blender-splat-patch](https://github.com/timfennell/blender-splat-patch)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:24:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Blender 5.3 extension to erase, clone stamp and heal 3D Gaussian splat scans
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timfennell/blender-splat-patch

### [yun-seo/PriSplat](https://github.com/yun-seo/PriSplat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T15:55:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of ECCV 2026 paper, PriSplat: Propagating Reliable Multi-view Information for Distractor-Free 3DGS.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yun-seo/PriSplat

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T07:51:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [JJleem/unreal-coin](https://github.com/JJleem/unreal-coin)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:56:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** UE 5.8 coin collecting demo on real-world 3D Gaussian Splatting scans
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JJleem/unreal-coin

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T06:23:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [AssassinHLQ/csust](https://github.com/AssassinHLQ/csust)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:21:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Godot 4.7 越肩射击 + 跑酷 + 期货交易沙盒《长沙理工：2067》：12 段 571 m 跑酷、暗网比纳、保证金/负债/强平经济、3D 高斯泼溅校园
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AssassinHLQ/csust

### [pstoebenau/guerrilla-worker](https://github.com/pstoebenau/guerrilla-worker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T04:20:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Standalone Gaussian splatting worker and pipeline for Guerrilla
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pstoebenau/guerrilla-worker

### [spoon-inoue/3dgs-demo](https://github.com/spoon-inoue/3dgs-demo)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:48:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/spoon-inoue/3dgs-demo

### [santi-raigoza/3dgs-satellite](https://github.com/santi-raigoza/3dgs-satellite)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T03:29:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/santi-raigoza/3dgs-satellite

### [lucylow/room-ai-interior-designer](https://github.com/lucylow/room-ai-interior-designer)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-20T02:50:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** (DONE figma redesign) (Home Value Prediction? )3D Gaussian Splatting Virtual real estate and property tours 3D Virtual Tours | 360 Real Estate Camera RE:ROOM AI - Interior Designer AI-Powered Interior Design, Augmented Reality, Spatial Intelligence, Shopping, and Construction Planning // https://canva.link/9bzdrduzd5rb8v0
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lucylow/room-ai-interior-designer

### [dohun1214/roomlens](https://github.com/dohun1214/roomlens)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T20:07:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** RoomLens - room 3D tour (Gaussian Splatting) and furniture layout simulator
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/dohun1214/roomlens

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T17:09:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-19T15:54:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

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

