---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-10-26T07:16:58Z
window_end_utc: 2026-10-27T07:08:57Z
generated_at_utc: 2026-10-27T07:08:57Z
item_count: 78
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-10-27

**统计窗口：** 2026-10-26T07:16:58Z — 2026-10-27T07:08:57Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **78** 项去重后的有效线索：真正新增论文 **7** 项、实质论文修订 **5** 项、代码/版本/项目更新 **65** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2610.35224v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation](https://arxiv.org/abs/2610.35347v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [Complexity-guided Regularization for Generalizable Human Gaussian Splatting](https://arxiv.org/abs/2610.35152v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting](https://arxiv.org/abs/2610.35361v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T17:03:44Z
- **更新判定：** 真正新增
- **核心内容：** Recent advancements in text-guided 3D editing, particularly with 3D Gaussian Splatting (3DGS), have shown promise but still lag behind the flexibility of 2D editing tools. Existing methods face a critical trade-off between preserving multi-view consistency and allowing structural modifications. Image-based editors can also struggle to apply the intended edit to objects viewed from unusual angles. To address these limitations, we introduce VidEdit3D, a framework that reformulates 3D scene editing as a trajectory-based video editing task. By drawing a parallel between camera movement in static 3D scenes and temporal dynamics in video, we leverage the robust spatiotemporal priors of pre-trained Video Diffusion Models (VDMs) to encourage semantic and structural coherence across views. Specifically, we propose Trajectory-Guided Rendering (TGR) to select informative keyframes and construct smooth video clips aligned with VDM input requirements. To propagate edits from an anchor view to thes…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35756v1

### [GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2610.35224v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T11:14:09Z
- **更新判定：** 真正新增
- **核心内容：** We present GaussianSpline, a dynamic 4D Gaussian Splatting method that models per-Gaussian motion using adaptive, non-uniform piecewise cubic Bézier splines. Unlike approaches based on global deformations, fixed-order polynomials, or uniformly parameterized splines, GaussianSpline jointly learns the Bézier control points and the temporal partition of each Gaussian's trajectory. This adaptive representation allocates greater temporal capacity to highly dynamic regions while maintaining compact trajectories for near-static regions, enabling high-fidelity reconstruction of complex and rapidly changing motion. To jointly achieve globally smooth motion and local adaptivity, we enforce $G^1$ continuity between consecutive Bézier segments using a reflection-based constraint on their control points. This produces smooth, fully differentiable trajectories while preserving the flexibility of non-uniform temporal parameterization. Experiments on the Neural 3D Video benchmark, the Google Immersiv…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35224v1

### [CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation](https://arxiv.org/abs/2610.35347v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T12:39:58Z
- **更新判定：** 真正新增
- **核心内容：** Voronoi tessellations have recently emerged as an adaptive, space-partitioning discretization for shape and appearance reconstruction from multi-view images. However, the irregular cells they produce make the repeated reconstruction of the tessellation during optimization costly. We therefore explore adaptive centroidal Voronoi tessellations (CVTs), which extend standard CVTs with non-uniform cell sizes while preserving the regular, well-shaped cells that make them efficient to compute. In CVTSplat, cell size is modulated by the evolving signed distance field, concentrating sites near the zero level set while keeping cells nearly centroidal. This regularity lets us specialize the whole pipeline, with GPU algorithms for nearest-neighbor queries and approximate Voronoi construction, and a rasterizer tailored to small, nearly isotropic cells. Our Voronoi construction is 5 to 10 times faster than general-purpose alternatives in this regime. On DTU and BlendedMVS, CVTSplat reaches geometri…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35347v1

### [Complexity-guided Regularization for Generalizable Human Gaussian Splatting](https://arxiv.org/abs/2610.35152v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T10:18:03Z
- **更新判定：** 真正新增
- **核心内容：** Recent studies on generalizable human Gaussian splatting have achieved the notable progress in synthesizing novel views of unseen human subjects from multi-view images. Despite this progress, existing methods still struggle to represent fine-grained details of human subjects, which inherently involve high geometric and textural complexity. This is because previous methods do not impose a constraint on how densely Gaussians are placed, which often leads to blurry rendering results in complex regions. To address this problem, we propose a complexity-guided regularization scheme. The key idea is to leverage a complexity prior computed via the local entropy in geometric and textural characteristics of a clothed human. This effectively prevents Gaussians from being coarsely placed in complex regions, which facilitates the faithful reconstruction of intricate structures. Furthermore, we sample local patches predominantly from complex regions according to this complexity prior, which allows…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35152v1

### [SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting](https://arxiv.org/abs/2610.35361v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T12:50:21Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) has become a promising representation for real-time novel view synthesis and 3D scene reconstruction. For practical deployment, recent studies have explored pose-free feed-forward 3DGS, which reconstructs Gaussian representations directly from unposed input images. However, these methods remain sensitive to residual pose errors, which perturb canonical-space Gaussian transformation, introducing noisy supervision for geometry and attribute learning. To address this problem, we present SG-Splat, a pose-free feed-forward 3DGS framework that improves robustness to pose uncertainty and stabilizes the learning of Gaussian primitives. SG-Splat decouples geometry estimation and Gaussian attribute prediction into two dedicated branches, reducing error coupling between pose-sensitive geometry and Gaussian attributes. We further introduce a coarse-to-fine refinement pipeline, consisting of Flow-Guided Pose Refinement (FGPR) and Residual-Guided Geometry Correction (RG…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35361v1

### [DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction](https://arxiv.org/abs/2610.35002v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T08:14:00Z
- **更新判定：** 真正新增
- **核心内容：** Sparse-view 4D reconstruction is highly under-constrained when only a few cameras are available. Generative priors can recover missing appearances, but video models are computationally impractical for iterative reconstruction, whereas single-view models produce temporally inconsistent pseudo-observations. Moreover, directly absorbing uncertain generative outputs into Gaussian optimization often creates redundant primitives and floating artifacts. To address these challenges, we propose DUET4D, a self-corrective coupled guidance framework for sparse-view 4D Gaussian splatting. The core of our approach is a self-corrective framework where the 4D representation guides generative prior for spatio-temporal consistent supervisions. We first construct sequential alignments from current Gaussian evidence to steer the latent restoration. Then we use Sequential Fidelity Resampling to lift generative supervisions into Gaussian space to selectively distinguish repeatedly supported primitives. The…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35002v1

### [\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T14:19:45Z
- **更新判定：** 实质修订
- **核心内容：** This paper addresses the problem of dynamic scene surface reconstruction using Gaussian Splatting (GS), aiming to recover temporally consistent geometry. While existing GS-based dynamic surface reconstruction methods can yield superior reconstruction, they are typically limited to either a single object or objects with only small deformations, struggling to maintain temporally consistent surface reconstruction of large deformations over time. We propose ``\textit{4DSurf}'', a novel and unified framework for generic dynamic surface reconstruction that does not require specifying the number or types of objects in the scene, can handle large surface deformations and temporal inconsistency in reconstruction. The key innovation of our framework is the introduction of Gaussian deformations induced Signed Distance Function Flow Regularization that constrains the motion of Gaussians to align with the evolving surface. To handle large deformations, we introduce an Overlapping Segment Partition…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2603.28064v2

### [FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T14:08:55Z
- **更新判定：** 实质修订
- **核心内容：** Recent vision-language-action (VLA) models can generate plausible end-effector motions, yet they often fail in long-horizon, contact-rich tasks because the underlying hand-object interaction (HOI) structure is not explicitly represented. An embodiment-agnostic interaction representation that captures this structure would make manipulation behaviors easier to validate and transfer across robots. We propose FlowHOI, a two-stage flow-matching framework that generates semantically grounded, temporally coherent HOI sequences, comprising hand poses, object poses, and hand-object contact states, conditioned on an egocentric observation, a language instruction, and a 3D Gaussian splatting (3DGS) scene reconstruction. We decouple geometry-centric grasping from semantics-centric manipulation, conditioning the latter on compact 3D scene tokens and employing a motion-text alignment loss to semantically ground the generated interactions in both the physical scene layout and the language instructio…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2602.13444v2

### [Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects](https://arxiv.org/abs/2606.01950v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T16:21:46Z
- **更新判定：** 实质修订
- **核心内容：** World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. Using object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel temporal-spatial transformer architecture that predicts future rigid body motion from a history of object Gaussians and future actions. Objects are represented by Gaussians in an object-centric frame, which allows to describe object motion as a rigid body transformation. Our model is trained on reconstructions from multiple viewpoints, which requires the model to also handle partial observations of objects due to occlusions. We analyze prediction performance of our approach on synthetic datasets composed of typical household objects with multi-object dynamics and interactions by a robot end effector. We also evaluat…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.01950v2

### [Gaussians on Fire: High-Frequency Reconstruction of Flames](https://arxiv.org/abs/2511.22459v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T14:15:57Z
- **更新判定：** 实质修订
- **核心内容：** We propose a method to reconstruct dynamic fire in 3D from a limited set of camera views with a Gaussian-based spatiotemporal representation. Capturing and reconstructing fire and its dynamics is highly challenging due to its volatile nature, transparent quality, and multitude of high-frequency features. Despite these challenges, we aim to reconstruct fire from only three views, which consequently requires solving for under-constrained geometry. We solve this by separating the static background from the dynamic fire region by combining dense multi-view stereo images with monocular depth priors. The fire is initialized as a 3D flow field, obtained by fusing per-view dense optical flow projections. To capture the high-frequency features of fire, each 3D Gaussian encodes a lifetime and linear velocity to match the dense optical flow. To ensure sub-frame temporal alignment across cameras, we employ a custom hardware synchronization pattern -- allowing us to reconstruct fire with affordabl…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2511.22459v3

### [CleanGS: Pareto-Guided Post-Hoc Cleanup of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2601.00913v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T17:15:20Z
- **更新判定：** 实质修订
- **核心内容：** A pretrained 3D Gaussian Splatting (3DGS) reconstruction can reproduce its capture views well while retaining off-object structure that becomes visible under reframing. We present CleanGS, a post-hoc cleanup method that removes such structure without retraining the underlying representation. Given calibrated views and binary target masks, CleanGS scores candidate three-view subsets using mask reliability, camera baseline, viewing-direction diversity, and complementary sparse 3D support. Rather than collapsing these objectives a priori, it computes the exact Pareto front over subsets of the reduced candidate pool and selects a balanced on-dominated subset using weighted Chebyshev scalarization. The selected views then drive rasterization-aware two-of-three voting to retain a subset of the original Gaussians. We evaluate the exported asset directly and introduce a fixed-pose widened-field protocol that exposes structure outside the original framing. Across 18 scenes, CleanGS achieves 19…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2601.00913v2

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T07:05:24Z
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
- **发布时间/更新时间：** 2026-10-27T05:32:33Z
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
- **发布时间/更新时间：** 2026-10-27T04:37:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Independent clean-room implementation of FreeTimeGS (Wang et al., CVPR 2025) in PyTorch: 4D Gaussian splatting for dynamic multi-view video, written from the paper and a public spec, not affiliated with its authors. Apache-2.0. CLI ftgs converts, initializes, trains, renders and evaluates on openftgs-synth datasets.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs

### [asadrizvi64/3dgs-project](https://github.com/asadrizvi64/3dgs-project)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T05:23:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GPU-accelerated 3D Gaussian Splatting training: macro-tile differentiable rasterizer + bandwidth-lean optimizer
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/asadrizvi64/3dgs-project

### [AbsoluteZer0527/Gaussian-Cake](https://github.com/AbsoluteZer0527/Gaussian-Cake)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:37:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A computer graphics project that uses optimal transport to morph model A into model B smoothly.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AbsoluteZer0527/Gaussian-Cake

### [mlslabs/MLSLabsGaussianSplattingRenderer-UE](https://github.com/mlslabs/MLSLabsGaussianSplattingRenderer-UE)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:55:56Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A high-performance Unreal Engine 5 (UE5) plugin developed by MaLanShan Audio & Video Laboratory, designed for real-time visualization, management, and scalable rendering of 3D Gaussian Splatting (3DGS) and dynamic Volumetric Video (4DGS).
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mlslabs/MLSLabsGaussianSplattingRenderer-UE

### [22elix3r/TalkingHeadAvatar](https://github.com/22elix3r/TalkingHeadAvatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:27:54Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Audio-driven 3D Gaussian Splatting talking head avatar with FLAME, VHAP tracking, HuBERT motion, TTS, and virtual camera output.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/22elix3r/TalkingHeadAvatar

### [navisfint/3dgs-sparse-view-avatar](https://github.com/navisfint/3dgs-sparse-view-avatar)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T14:24:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Sparse-view (K=3) 3D Gaussian avatar reconstruction — surface-anchored prior + temporal regularization. Method and results only.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/navisfint/3dgs-sparse-view-avatar

### [Photogrammetry and Gaussian splatting bring plants into 4D digital life](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6ae04e17d97b4774b79547246c416f92&url=https%3a%2f%2fbioengineer.org%2fphotogrammetry-and-gaussian-splatting-bring-plants-into-4d-digital-life%2f&c=11978303815262526264&mkt=en-us)

- **主题：** 动态与4D
- **来源：** Bing News
- **发布时间/更新时间：** 2026-10-26T11:35:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** Researchers combined Structure-from-Motion photogrammetry with 3D Gaussian Splatting to build a 12-timepoint 4D fern growth sequence and an interactive 14-section digital twin of a tropical greenhouse ...
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:17:41Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** High performance 3D Gaussian Splatting (3DGS) renderer for Three.js. WebGPU and WebGL2. Supports PLY, SPZ, Streaming LOD including SOG and RAD.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [nff747/hyper-splat-engine](https://github.com/nff747/hyper-splat-engine)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T21:48:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zero-copy, virtualized WebGPU 3D Gaussian Splatting and spatial AI engine with distance LoD tile streaming and proactive VRAM paging.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nff747/hyper-splat-engine

### [Xget7/splatkit-ios](https://github.com/Xget7/splatkit-ios)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:38:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Metal Gaussian splatting SDK for iOS: Swift view, GPU visibility/radix, experimental LOD and hybrid tiles. MIT source and reproducible XCFramework.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit-ios

### [PYGRASSREAL/pygrassreal-py3s-format](https://github.com/PYGRASSREAL/pygrassreal-py3s-format)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T00:20:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official Specification & Reference Codec for PyGrassReal .py3s (Unified 3D Gaussian Splatting + Collision Format)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/PYGRASSREAL/pygrassreal-py3s-format

### [maviorgleam/Classical-Gardens-3DGS-Digital-Twin](https://github.com/maviorgleam/Classical-Gardens-3DGS-Digital-Twin)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T08:21:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Lightweight Reconstruction of Classical Gardens Based on 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/maviorgleam/Classical-Gardens-3DGS-Digital-Twin

### [Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies](https://arxiv.org/abs/2610.35626v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-10-26T15:40:03Z
- **更新判定：** 真正新增
- **核心内容：** Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment. This challenge is particularly severe in electronic-waste disassembly, where robots operate in cluttered assemblies of densely packed, visually similar components. Full digital-twin simulation is difficult because many parts are thin, reflective, or mechanically complex, making accurate object-level meshes and contact models difficult to obtain. In this work, we focus on pre-contact reaching and propose a 3D Gaussian Splatting (3DGS)-based data generation pipeline for wrist-camera VLA adaptation. Our method reconstructs the real workspace with 3DGS and renders diverse wrist-camera observations from robot-aligned poses. These observations are paired with smooth, structured reaching trajectories to provide robot-aligned visual-action supervision for VLA fine-tuning. We further augment…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2610.35626v1

### [PeizhiYan/gmesh](https://github.com/PeizhiYan/gmesh)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T23:55:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gmesh supports differentiable rendering of mixed 3D Gaussians and meshes within a single scene.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/PeizhiYan/gmesh

### [sepahead/melkor](https://github.com/sepahead/melkor)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T18:15:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** C++17 toolkit for 3D Gaussian splats: deterministic conversion, inspection, geometry-based scene completion and viewing across PLY, SPZ and glTF, with CPU/Metal and optional CUDA backends. v2 hardening in progress; no supported production binary release.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sepahead/melkor

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:49:41Z
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
- **发布时间/更新时间：** 2026-10-27T05:02:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Interactive 3D Gaussian Splatting demo with color, depth, and normal visualization.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/2072508371/truck-3dgs-demo

### [anidealeft/UrbanQGS](https://github.com/anidealeft/UrbanQGS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T01:47:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Large-Scale Urban Surface Reconstruction via Analytic Curvature Consistency in Quadratic Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/anidealeft/UrbanQGS

### [HyeonSung11/Geometry-Guided-3DGS](https://github.com/HyeonSung11/Geometry-Guided-3DGS)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T00:19:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official code for "Geometry-guided 3D Gaussian Splatting" (J. ICROS 2026) — SPFSplat + frozen UniDepthV2 metric-depth prior via zero-convolution injection
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/HyeonSung11/Geometry-Guided-3DGS

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T21:39:26Z
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
- **发布时间/更新时间：** 2026-10-26T08:30:32Z
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
- **发布时间/更新时间：** 2026-10-27T07:05:49Z
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
- **发布时间/更新时间：** 2026-10-27T05:31:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [xsj01/gavis](https://github.com/xsj01/gavis)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:53:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [CVPR 26] GAVIS: Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/xsj01/gavis

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:55:24Z
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
- **发布时间/更新时间：** 2026-10-27T02:07:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [yuhaowang774/xdu-south-campus-3dgs](https://github.com/yuhaowang774/xdu-south-campus-3dgs)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:32:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting reconstruction of Xidian University South Campus (SOG v2, 8.2M splats)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yuhaowang774/xdu-south-campus-3dgs

### [SHTAMU/Gaussian-Splatting](https://github.com/SHTAMU/Gaussian-Splatting)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T00:49:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Computer vision Gaussian reconstruction HW
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/SHTAMU/Gaussian-Splatting

### [Rain-604/3DGS-3D_mapping](https://github.com/Rain-604/3DGS-3D_mapping)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T23:10:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** use 3DGS to map out the building
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Rain-604/3DGS-3D_mapping

### [playcanvas/supersplat v3.7.0](https://github.com/playcanvas/supersplat/releases/tag/v3.7.0)

- **主题：** 编辑与生成
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-26T09:31:43Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Add copy/paste to the transform and colors panels by @slimbuck in https://github.com/playcanvas/supersplat/pull/1077 * Add a typed editor API over serialized selection commands by @slimbuck in https://github.com/playcanvas/supersplat/pull/1078 * Add native WebMCP tools for the editor by @slimbuck in https://github.com/playcanvas/supersplat/pull/1081 * Reject invalid editor commands and keep colour points apart by @slimbuck in https://github.com/playcanvas/supersplat/pull/1082 * Add radial sorting, Preferences tooltips and an About link by @slimbuck in https://github.com/playcanvas/supersplat/pull/1083 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v3.6.0...v3.7.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [DrawingProcess/RelateGS](https://github.com/DrawingProcess/RelateGS)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T04:35:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [WACV'27] RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DrawingProcess/RelateGS

### [jinyoonok2/3DCV-3D-Scene-Edit-with-3DGS](https://github.com/jinyoonok2/3DCV-3D-Scene-Edit-with-3DGS)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:31:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jinyoonok2/3DCV-3D-Scene-Edit-with-3DGS

### [manycoretech/aholo-viewer](https://github.com/manycoretech/aholo-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:47:10Z
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
- **发布时间/更新时间：** 2026-10-27T02:53:13Z
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
- **发布时间/更新时间：** 2026-10-27T02:22:19Z
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
- **发布时间/更新时间：** 2026-10-26T15:56:31Z
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
- **发布时间/更新时间：** 2026-10-27T01:12:58Z
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
- **发布时间/更新时间：** 2026-10-27T03:30:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time Gaussian splatting SDKs for Android/Vulkan, iOS/Metal and React Native, sharing a C++17 engine.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit

### [Saqoosha/ghostline](https://github.com/Saqoosha/ghostline)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T04:58:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Recover FPV flight paths from goggle DVR on a 3DGS scan, and replay them
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Saqoosha/ghostline

### [Loppas/playcanvas-quake3](https://github.com/Loppas/playcanvas-quake3)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:56:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A port of ioquake to the Playcanvas engine with the added ability to render gaussian splat maps
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Loppas/playcanvas-quake3

### [kamyy/ai-gaussian-splatter](https://github.com/kamyy/ai-gaussian-splatter)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T04:26:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Upload multi-angle photos of a physical object, get back a real-time 3D Gaussian Splat viewable and shareable in-browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kamyy/ai-gaussian-splatter

### [Xget7/react-native-splatkit](https://github.com/Xget7/react-native-splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:38:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** React Native component for real-time Gaussian splatting: load an SPZ scene, pick a quality preset, and walk through it from JavaScript.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/react-native-splatkit

### [bepar22-sudo/dsc-campus-3d](https://github.com/bepar22-sudo/dsc-campus-3d)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T07:02:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 대구과학대학교 3D 공간정보 - 캠퍼스 라이다 3D / 체육관 실사 3D(3DGS) 웹 뷰어
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/bepar22-sudo/dsc-campus-3d

### [reed-soul/gis-toolbox](https://github.com/reed-soul/gis-toolbox)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T04:22:59Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** GIS Toolbox — free browser-based GIS workbench: format & coordinate conversion, spatial analysis, 3D tiles/3DGS & hyperspectral viewers. All processing local, no upload.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/reed-soul/gis-toolbox

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:38:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [monstercameron/NeuralVisionRacer](https://github.com/monstercameron/NeuralVisionRacer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:36:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A Rust racing game through real-world Gaussian splat scans, with native wgpu and browser WebGPU builds.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/monstercameron/NeuralVisionRacer

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:26:40Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [RCL-Studio-X/GaussianSplats_UnityTemplate](https://github.com/RCL-Studio-X/GaussianSplats_UnityTemplate)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T21:15:03Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Get start with gaussian splatting in unity VR.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RCL-Studio-X/GaussianSplats_UnityTemplate

### [kavehkamali/frontier-fieldnotes](https://github.com/kavehkamali/frontier-fieldnotes)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T20:48:10Z
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
- **发布时间/更新时间：** 2026-10-26T20:36:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Любительские модели 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3XyzMedia/VIEWER

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T07:17:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [gayan957/3dgs-capture-check](https://github.com/gayan957/3dgs-capture-check)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T04:12:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/gayan957/3dgs-capture-check

### [Add radial sorting, Preferences tooltips and an About link (#1083)](https://github.com/playcanvas/supersplat/commit/efb6a8abceee997c9896c6b15d58026115a9cc4a)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-26T09:30:13Z
- **更新判定：** 代码实质更新
- **核心内容：** Add radial sorting, Preferences tooltips and an About link (#1083)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T19:17:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A growing curation of Text-to-3D, Diffusion-to-3D works.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yyeboah/Awesome-Text-to-3D

### [3.7.0](https://github.com/playcanvas/supersplat/commit/b89029dd20911fd18905b61de2701094ac390a73)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-10-26T09:31:12Z
- **更新判定：** 代码实质更新
- **核心内容：** 3.7.0
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [lukehollis/sphr](https://github.com/lukehollis/sphr)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T03:29:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open, hackable 3d digital twin builder that supports 3d gaussian splatting, 360 images, and vfx
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lukehollis/sphr

### [quixbrics/gausseous](https://github.com/quixbrics/gausseous)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T06:52:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gausseous — a 3D Gaussian Splatting manipulator and animator for the browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/quixbrics/gausseous

### [AssassinHLQ/csust](https://github.com/AssassinHLQ/csust)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T15:39:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Godot 4.7 越肩射击 + 跑酷 + 期货交易沙盒《长沙理工：2067》：12 段 571 m 跑酷、暗网比纳、保证金/负债/强平经济、3D 高斯泼溅校园
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/AssassinHLQ/csust

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T09:07:23Z
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
- **发布时间/更新时间：** 2026-10-27T02:46:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [izumi01-n/SGE-GS](https://github.com/izumi01-n/SGE-GS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T02:37:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of "Selective Geometric Enhancement for 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/izumi01-n/SGE-GS

### [miaopasi677/3dgs-colab](https://github.com/miaopasi677/3dgs-colab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-27T00:19:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/miaopasi677/3dgs-colab

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T16:59:25Z
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
- **发布时间/更新时间：** 2026-10-26T16:37:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

### [pawafa666-eng/3DGS-duibi](https://github.com/pawafa666-eng/3DGS-duibi)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-10-26T13:30:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pawafa666-eng/3DGS-duibi

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 12 |
| GitHub | ok: 65 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 1 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 12/12 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

