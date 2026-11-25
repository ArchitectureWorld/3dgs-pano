---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-24T11:53:16Z
window_end_utc: 2026-11-25T10:45:09Z
generated_at_utc: 2026-11-25T10:45:09Z
item_count: 75
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-25

**统计窗口：** 2026-11-24T11:53:16Z — 2026-11-25T10:45:09Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **75** 项去重后的有效线索：真正新增论文 **5** 项、实质论文修订 **5** 项、代码/版本/项目更新 **65** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T14:50:30Z
- **更新判定：** 真正新增
- **核心内容：** Feedforward 3D Gaussian Splatting (3DGS) pipelines reconstruct a scene from images in a single forward pass, representing it as real-time-renderable 3D Gaussians. However, the resulting representations contain far more Gaussians than are needed to render the scene faithfully, especially when there are many input views. This drastically increases memory and storage requirements. Existing pruning methods either require costly re-optimization, which defeats the purpose of a single forward pass, or rely on simple strategies that do not exploit all the available information. We present AnyPrune, a transformer-based, optimization-free pruning module designed to work on top of any feedforward 3DGS pipeline. To remove unnecessary Gaussians, AnyPrune learns and exploits pipeline-specific redundancy patterns through a short single-GPU training on the frozen target feedforward pipeline. AnyPrune achieves better rendering quality than existing optimization-free pruning methods in most settings an…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.32735v1

### [First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T17:25:53Z
- **更新判定：** 真正新增
- **核心内容：** Recent neural implicit and Gaussian splatting approaches have achieved impressive results in multi-view surface reconstruction. However, jointly optimizing geometry and appearance introduces ambiguities. A parametric appearance model can compensate for geometric errors, reproducing the input images accurately without an accurate surface. We demonstrate accurate neural implicit surface reconstruction using only multi-view patch photoconsistency with geometry-based visibility, without volumetric rendering or parametric appearance models. For each reference ray, sphere tracing computes the first surface intersection. Its position and normal define a local patch whose photoconsistency is evaluated across visible neighboring views using colors sampled directly from the input images. For efficient sphere tracing, we use a 1-Lipschitz multi-layer perceptron. We use a single photoconsistency loss, without foreground masks or auxiliary geometric regularization. Experiments show that our method…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.32998v1

### [Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T14:39:05Z
- **更新判定：** 真正新增
- **核心内容：** A small ground robot can carry one camera and a few watts of compute, but the depth foundation models that could turn that camera into a range sensor are vision transformers sized for GPUs. We bring one to a Raspberry Pi 5 with the Hailo-8L, an accelerator that runs every layer in integer arithmetic, attention included. Quantised for it, Depth Anything V2 loses large parts of the scene, and we measure why: at 449 tokens, 91% of softmax weights fall below one int8 step while carrying 17-33% of the attention mass. Our answer is to distil, not quantise. An attention-free ResNet-34 U-Net student of Depth Anything V2-Large (24.5M parameters) runs at 27.1 FPS on the chip, its int8 output matches its float twin (Pearson 0.99993), and on held-out scenes of its simulated yard it is the most accurate depth network on the chip (AbsRel 0.269 against 0.354-0.530). On 1,000 stereo-verified points of a real outdoor drive it is not resolvably different from the vendor's Depth Anything V2-Small build,…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.32718v1

### [Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T13:51:18Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) enables high-quality novel-view rendering, but its large scene representations are costly to transmit. Pruning and compression reduce file sizes, yet progressive delivery also requires usable reconstructions before the full scene arrives. Existing progressive representations provide partial scenes, but level-based updates are limited by predefined coding boundaries. This paper presents a progressive 3DGS codec that balances attribute fidelity with the image benefit of making Gaussians available earlier. Its single compact stream supports partial 3D reconstruction and adds newly decoded Gaussians as more bytes arrive. The stream supports fine-grained updates at arbitrary received-byte budgets, without separate encodings or later attribute refinement. At matched complete-file sizes and received bytes, completion-aware allocation improves 1/8 PSNR over attribute-only allocation by 0.48-1.43 dB. The proposed codec compresses original 3DGS representations by 62…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.32628v1

### [Beyond Primitive Bloat: High-Fidelity Gaussian Splatting via Coordinate-Convolution Neural Network](https://arxiv.org/abs/2512.12898v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T15:45:53Z
- **更新判定：** 实质修订
- **核心内容：** Gaussian Splatting (GS) has revolutionized Novel View Synthesis (NVS) with fast training and real-time rendering, yet pushing its fidelity to arbitrary high levels remains an open challenge. We theoretically explain this barrier by proving that discrete Gaussian representations require an exponentially increasing number of primitives to raise training PSNR, which inevitably triggers optimization issues and validation overfitting. To bypass this scaling limit without primitive bloat, we formulate detail recovery as a continuous neural field over coarse renderings and prove that monotonically reducing approximation risk to zero requires jointly leveraging low-fidelity signals, local neighborhood, and coordinate queries. Guided by this result, we augment splatted renderings with an existing Coordinate-Convolution Neural Network (CCNN) that jointly convolves rendered low-fidelity signals with 2D pixel coordinate queries to synthesize residuals. Integrating CCNN into five diverse Gaussian…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2512.12898v3

### [PhysSkin++: Generalizable Self-Supervised Neural Skinning for Real-Time Interactive Physics-Based Animation](https://arxiv.org/abs/2610.26067v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T13:23:25Z
- **更新判定：** 实质修订
- **核心内容：** Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces without per-object network training. To learn these subspaces without simulation trajectories, we develop a Physics-Informed Self-Supervised Learning strategy that combines skinning-field normalization with conflict-aware gradient correction, stabilizing joint optimization under physical and orthogonality constraints. The learned representation supports efficient reduced dynamics with user control and contact interactions, together with direct animation binding to meshes, point clouds, and 3D Gaussians. For prescribed rig animation, we further introduce a self-supervised comp…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.26067v2

### [FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T17:23:22Z
- **更新判定：** 实质修订
- **核心内容：** Fast quadrotor flight requires safe obstacle avoidance under tight onboard compute limits. While 3D Gaussian Splatting (3DGS) provides a continuous, geometry-aware scene representation for perception-driven navigation, existing 3DGS safety filters use reduced-order models such as single- and double-integrators that ignore actuator limits and assume commanded accelerations are realized instantaneously. Building on an analytic collision cone barrier for 3DGS, we introduce a nonlinear, actuator-aware safety filter enforced through the full quadrotor dynamics. We derive a high-relative-degree collision cone exponential CBF (ECBF) and a backup CBF whose forward-simulated backup policy provides a certified admissible fallback whenever the QP is infeasible under input constraints. Compared with a state-of-the-art 3DGS safety filter, our approach reduces trajectory jerk by 47% and runs 2.25 times faster. We demonstrate the ECBF in simulation and validate the backup CBF on hardware for real-ti…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2607.01200v2

### [OP2GS: Feature-Free Gaussian Splatting with Dual Opacity for 3D Instance Segmentation](https://arxiv.org/abs/2605.20044v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T14:07:16Z
- **更新判定：** 实质修订
- **核心内容：** 3D Gaussian Splatting (3DGS) provides an explicit and efficient scene representation, but its primitives do not naturally expose object-level identity. Existing methods either learn contrastive per-Gaussian features that need post-hoc clustering, or supervise identity encodings with view-consistent 2D masks. We propose OP2GS, a lightweight object-aware Gaussian representation that augments each primitive with an explicit instance label and a dedicated instance opacity $σ^{*}$, which serves as an instance occupancy field for object-mask rendering. This dual-opacity formulation decouples visual appearance from instance occupancy, so that $σ^{*}$ can be learned and the instance labels can be corrected without touching the appearance parameters $σ$ and $c$. We learn $σ^{*}$ with an instance occupancy loss that follows the standard transmittance-based visibility of 3DGS. A discrete regrouping step then corrects the instance labels using multi-view mask consensus. Since no high-dimensional…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2605.20044v2

### [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:38:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [MrNeRF/lichtfeld-blender-plugin](https://github.com/MrNeRF/lichtfeld-blender-plugin)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T21:45:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting in Blender: train 3D Gaussian Splats from your Blender scene with LichtFeld Studio and import splats from the LichtFeld Portal.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/lichtfeld-blender-plugin

### [Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T18:57:48Z
- **更新判定：** 真正新增
- **核心内容：** Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency.…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.33145v1

### [arrival-space/animated-sog](https://github.com/arrival-space/animated-sog)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:29:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Animated SOG (.asog): compact 4D Gaussian splat clips with motion, SH and sound - spec, Python encoder and flip-book pipeline, PlayCanvas and three.js players
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arrival-space/animated-sog

### [jamesdemon923/EmoTaG](https://github.com/jamesdemon923/EmoTaG)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:10:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [CVPR'26] EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jamesdemon923/EmoTaG

### [cuesplat/cuesplat.github.io](https://github.com/cuesplat/cuesplat.github.io)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T06:43:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for CUESPLAT: Learning to Schedule Sparse Deformation for Dynamic Gaussian Splatting on Edge Devices
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cuesplat/cuesplat.github.io

### [Vexlc/road-hazard-reconstruction](https://github.com/Vexlc/road-hazard-reconstruction)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T03:05:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Reproducible stereo, RGB-D and procedural road-hazard assets with dynamic 3DGS scene insertion and selectable visualizations.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Vexlc/road-hazard-reconstruction

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:07:38Z
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
- **发布时间/更新时间：** 2026-11-24T15:15:48Z
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
- **发布时间/更新时间：** 2026-11-24T18:39:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [coopersimpson101-debug/splatweb](https://github.com/coopersimpson101-debug/splatweb)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T04:23:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splatting renderer in WebGPU: EWA projection, GPU radix sort, streaming .ply/.splat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/coopersimpson101-debug/splatweb

### [When Variance Is Not an Error Map: Calibrated Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v5)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-24T17:34:36Z
- **更新判定：** 实质修订
- **核心内容：** Radiative Gaussian Splatting enables fast and high-quality reconstruction in sparse-view CT, but reliable localization of reconstruction errors within the imaged anatomy remains challenging. It is unclear whether current uncertainty maps can reliably indicate where the reconstruction is wrong. We investigate when uncertainty can serve as a spatial error map and present an error-localization system that predicts voxel-wise reconstruction error by combining predictive uncertainty with complementary reconstruction-derived information. Under fixed Gaussian geometry and independent rectified-Gaussian density variables, an exact closed-form predictive moment is derived in this work to enable direct computation of voxel-wise variance without repeated reconstruction sampling. The resulting uncertainty maps were evaluated over both the whole reconstruction volume and the object foreground. Experiments show that strong whole-volume uncertainty-error correspondence can conceal poor error ranking…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2607.13682v5

### [QuanJianji/SeaIceGS](https://github.com/QuanJianji/SeaIceGS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:07:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SeaIceGS is a research codebase for polar region 3D reconstruction from multi-view imagery. It adapts Gaussian Splatting-based surface reconstruction to polar scenes, where weak texture, high reflectance, and fragmented ice geometry make dense reconstruction difficult.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/QuanJianji/SeaIceGS

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:49:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [ZhangAoCanada/3Dviewer](https://github.com/ZhangAoCanada/3Dviewer)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:43:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** just another 3D viewer for popular 3D representations, including 3DGS, mesh, point cloud, ...
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhangAoCanada/3Dviewer

### [sepahead/relief-atlas](https://github.com/sepahead/relief-atlas)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T23:08:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** On-device generative pipeline (FLUX.2 → TRELLIS.2 → 3DGS) producing a 10,079-asset 3D mesh corpus for disaster-relief, humanitarian-aid and civil-protection simulation — with automated 10-lens turntable QA gates, content policy enforcement and dual .spz/.splat export.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sepahead/relief-atlas

### [IRIS-LAB-whu/SeaIceGS](https://github.com/IRIS-LAB-whu/SeaIceGS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:02:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SeaIceGS is a research codebase for polar region 3D reconstruction from multi-view imagery. It adapts Gaussian Splatting-based surface reconstruction to polar scenes, where weak texture, high reflectance, and fragmented ice geometry make dense reconstruction difficult.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/IRIS-LAB-whu/SeaIceGS

### [deshihito/scratch-ue5-pen-research](https://github.com/deshihito/scratch-ue5-pen-research)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:33:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research repository exploring Unreal Engine 5-level 3D graphics (Cook-Torrance PBR, Mini-Lumen SDF GI, Soft Shadows, Volumetric God Rays, ACES, 32-bit ARGB GPU Pen Bloom, Monte Carlo Path Tracing + SVGF-lite Denoiser, 3D Gaussian Splatting) in 100% Pure Vanilla Scratch 3.0 Pen (.sb3).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/deshihito/scratch-ue5-pen-research

### [chandimacbbandara/preflight-3d](https://github.com/chandimacbbandara/preflight-3d)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T06:14:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Pre-flight computer vision and ML quality analyzer that evaluates object capture videos for blur, lighting, texture, and viewpoint coverage before running 3D reconstruction (COLMAP / NeRF / 3DGS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/chandimacbbandara/preflight-3d

### [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:33:48Z
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
- **发布时间/更新时间：** 2026-11-25T10:39:24Z
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
- **发布时间/更新时间：** 2026-11-25T08:45:49Z
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
- **发布时间/更新时间：** 2026-11-24T16:37:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zdwww/Wheat-3DGS

### [M4A1TasteGood/ArgsWorld](https://github.com/M4A1TasteGood/ArgsWorld)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:52:25Z
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
- **发布时间/更新时间：** 2026-11-25T10:36:24Z
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
- **发布时间/更新时间：** 2026-11-25T05:27:20Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [ady95/open-reality-view-tutorial](https://github.com/ady95/open-reality-view-tutorial)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:09:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Example code for the WikiDocs book 'Tesla Reality View Follow-along' — open-source 3DGS, feed-forward reconstruction and generative driving video on a single RTX 3090
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ady95/open-reality-view-tutorial

### [thaianh20021/drive2sim](https://github.com/thaianh20021/drive2sim)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:29:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** drive2sim: driving-scene reconstruction (3D Gaussian Splatting) with Studio, built on DriveStudio. Install: npx github:thaianh20021/drive2sim
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/thaianh20021/drive2sim

### [sakorman/Text2Splat-Agent](https://github.com/sakorman/Text2Splat-Agent)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T03:06:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Text-to-3DGS agent with built-in MCP, free image-model adapters, and local COLMAP + Brush reconstruction. 造物方舟：文字驱动的本地 3DGS Agent。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/Text2Splat-Agent

### [RealMaker001/Jun-paper-tracker](https://github.com/RealMaker001/Jun-paper-tracker)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T01:04:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Daily arXiv paper tracker: 3DGS, Visual Localization, SLAM, Keypoint Detection, Target Tracking
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RealMaker001/Jun-paper-tracker

### [Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING](https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T16:56:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Natehc6002/3DGS-3D-RECONSTRUCTION-USING-GAUSSIAN-SPLATTING

### [ycgogogogogo/BSPC-GS](https://github.com/ycgogogogogo/BSPC-GS)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:21:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** BSPC-GS: Bidirectional Sparse Point Cloud Compensation for Sparse-View 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ycgogogogogo/BSPC-GS

### [alexzhenglong/Ortho-3DGS](https://github.com/alexzhenglong/Ortho-3DGS)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T12:30:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** True Digital Orthophoto Generation From Unmanned Aerial Vehicle Imagery Using the Depth-Regulated 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/alexzhenglong/Ortho-3DGS

### [fubukisama/GaussianSplattingWorkbench](https://github.com/fubukisama/GaussianSplattingWorkbench)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:00:19Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A native Windows workbench for Gaussian Splatting, photogrammetry, and 3D scene editing.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/fubukisama/GaussianSplattingWorkbench

### [AsakaTigar/dentsplat-web](https://github.com/AsakaTigar/dentsplat-web)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:50:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zero-install browser 3D Gaussian Splatting prototype for dental data: FDI semantics inside the container, shader-level clipping, auditable measurements.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AsakaTigar/dentsplat-web

### [splatslot/gs-editor](https://github.com/splatslot/gs-editor)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:07:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ブラウザだけで 3DGS（Gaussian Splatting）を開いて、掃除し、原点と向きを直して書き出すエディタ。インストール不要
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/splatslot/gs-editor

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:57:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source web graphics engine built on WebGPU and WebGL2
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/engine

### [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:58:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Curated list of papers and resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MrNeRF/awesome-3D-gaussian-splatting

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:57:37Z
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
- **发布时间/更新时间：** 2026-11-25T06:01:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository tracks the latest advancements in 3D Gaussian Splatting from Arxiv, with daily automated updates. Stay up-to-date with cutting-edge research in this exciting field!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/longxiang-ai/awesome-gaussians

### [lueluelue12138/sharp-gui](https://github.com/lueluelue12138/sharp-gui)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T04:16:30Z
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
- **发布时间/更新时间：** 2026-11-25T04:47:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [DisplayXR/displayxr-demo-gaussiansplat](https://github.com/DisplayXR/displayxr-demo-gaussiansplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:16:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** DisplayXR demo — real-time 3D Gaussian Splatting viewer for glasses-free 3D displays (OpenXR + Vulkan, Windows & macOS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DisplayXR/displayxr-demo-gaussiansplat

### [Artemarius/pocketsplat](https://github.com/Artemarius/pocketsplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T12:35:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Vulkan 1.3 3D Gaussian Splatting viewer for Android phones, measured like-for-like against web and native renderers
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Artemarius/pocketsplat

### [mtblck/blobscape](https://github.com/mtblck/blobscape)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:31:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Learn 3D Gaussian splats by taking them apart: hands-on lessons, a sandbox, and experiments on our own animated-splat engine for three.js.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mtblck/blobscape

### [WPCJATH/comp6704-3dgs-solvers](https://github.com/WPCJATH/comp6704-3dgs-solvers)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:53:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** First-order, adaptive and second-order solvers (SGD, Adam, L-BFGS, Levenberg-Marquardt) compared on 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WPCJATH/comp6704-3dgs-solvers

### [Seanwilliam2077/3dgs-collision](https://github.com/Seanwilliam2077/3dgs-collision)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:12:08Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Collision for 3D Gaussian splat scenes: voxel shell for characters, camera volume, UE walk tests
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Seanwilliam2077/3dgs-collision

### [tehMazz/Artifixers-3DGS](https://github.com/tehMazz/Artifixers-3DGS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:08:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/tehMazz/Artifixers-3DGS

### [AXERA-TECH/sharp-ax8860](https://github.com/AXERA-TECH/sharp-ax8860)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:09:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SHARP on AX8860: single image → 3D Gaussian Splatting in ~1.6 s (on-device NPU)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AXERA-TECH/sharp-ax8860

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T05:27:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T02:31:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [aozi6666/Sparse-3DGS-heritage-VQA](https://github.com/aozi6666/Sparse-3DGS-heritage-VQA)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T22:27:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 受限采集下的稀疏视角 3DGS 文化遗产重建 + 多模态大模型·VQA-VL 流式视频问答与空间定位系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aozi6666/Sparse-3DGS-heritage-VQA

### [KusMar00/camera-sonar-3dgs](https://github.com/KusMar00/camera-sonar-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T14:33:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/KusMar00/camera-sonar-3dgs

### [kaatarina1/gs-pc-viewer](https://github.com/kaatarina1/gs-pc-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T11:57:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** In-browser viewer for comparing up to 12 Gaussian splat models and point clouds side by side with a shared camera
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kaatarina1/gs-pc-viewer

### [ukkyz/polybrush-studio](https://github.com/ukkyz/polybrush-studio)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T07:56:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Polybrush PlayCanvas Gaussian Splat Studio
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ukkyz/polybrush-studio

### [xiliu8006/3DGS-Enhancer](https://github.com/xiliu8006/3DGS-Enhancer)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T21:41:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xiliu8006/3DGS-Enhancer

### [MapMindAI/EasyGaussianSplatting](https://github.com/MapMindAI/EasyGaussianSplatting)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T10:14:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** From insta360/DJI to Gaussian Splatting Easy and Direct
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MapMindAI/EasyGaussianSplatting

### [yangyf-works/GaussianCutSim](https://github.com/yangyf-works/GaussianCutSim)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:53:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting based machining simulation and visualization using Open3D.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yangyf-works/GaussianCutSim

### [TitanothereYik/VotionSplat-mockup](https://github.com/TitanothereYik/VotionSplat-mockup)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:40:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Votion 3DGS 2.0 clickable HTML dummy UI
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/TitanothereYik/VotionSplat-mockup

### [cfahlgren1/idol-mlx](https://github.com/cfahlgren1/idol-mlx)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T09:07:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Photo to 3D Gaussian splat in ~15 s on a Mac: Idol + Idol Turbo on Apple Silicon (unofficial)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cfahlgren1/idol-mlx

### [Waiitch/3DGS](https://github.com/Waiitch/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T08:32:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS code
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Waiitch/3DGS

### [ukkyz/office-vite-ref](https://github.com/ukkyz/office-vite-ref)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T06:57:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3d Gaussian Splat Reference
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ukkyz/office-vite-ref

### [surtecha/3d-gaussian-splatting](https://github.com/surtecha/3d-gaussian-splatting)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T06:04:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D gaussian splatting in python
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/surtecha/3d-gaussian-splatting

### [lin278804-ops/lf-3dgs-datagen](https://github.com/lin278804-ops/lf-3dgs-datagen)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T04:26:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lin278804-ops/lf-3dgs-datagen

### [lin278804-ops/lf-3dgs-project](https://github.com/lin278804-ops/lf-3dgs-project)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-25T04:26:04Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lin278804-ops/lf-3dgs-project

### [B2mbiczek/supersplat-3dgs-downloader](https://github.com/B2mbiczek/supersplat-3dgs-downloader)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T22:39:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A utility to download and convert SuperSplat 3DGS scenes to PLY format, bypassing UI restrictions where direct download is disabled.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/B2mbiczek/supersplat-3dgs-downloader

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-24T20:52:31Z
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
| arXiv | ok: 10 |
| GitHub | ok: 65 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 10/10 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

