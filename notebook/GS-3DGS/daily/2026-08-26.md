---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-08-13T02:00:00Z
window_end_utc: 2026-08-26T02:54:47Z
generated_at_utc: 2026-08-26T02:54:47Z
item_count: 174
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-08-26

**统计窗口：** 2026-08-13T02:00:00Z — 2026-08-26T02:54:47Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **174** 项去重后的有效线索：真正新增论文 **55** 项、实质论文修订 **21** 项、代码/版本/项目更新 **95** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](https://arxiv.org/abs/2608.16234v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2) | 真正新增 | arXiv | R1/E0 | P0 |
| 4 | [AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 5 | [QuARC-GS: Quantized Anchored Residual Coding for Compact Dynamic Scene Streaming with Gaussian Splatting](https://arxiv.org/abs/2608.18285v1) | 真正新增 | arXiv | R1/E0 | P0 |

## 分类详述

### [M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-23T15:44:39Z
- **更新判定：** 真正新增
- **核心内容：** High-fidelity free-viewpoint video (FVV) and interactive rendering increasingly rely on explicit Gaussian representations, yet practical deployment remains constrained by representation size, dynamic updates, and computational cost. Existing multi-view video benchmarks provide valuable real-captured content, but they make it difficult to isolate the effects of controlled camera geometry, representation efficiency, and temporal redundancy. We introduce M$^3$ISR, a controlled synthetic benchmark for 3D and 4D Gaussian Splatting (3DGS/4DGS). The benchmark contains 25 scenes from five indoor and outdoor scene groups, two camera/motion configurations, six synchronized 1080p views, and dense ground-truth annotations including RGB, camera parameters, depth, semantic and instance segmentation, and static--dynamic masks. The shared-center camera design intentionally isolates angular view variation and enables controlled evaluation of novel-view synthesis and representation efficiency. We organ…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22465v1

### [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-25T04:52:42Z
- **更新判定：** 真正新增
- **核心内容：** Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction failures. To overcome these limitations, we present NemoSplat, the first feed-forward 4D Gaussian Splatting framework tailored for media-aware dynamic reconstruction directly from uncalibrated marine videos. Beyond providing robust estimations of camera poses and dense scene depth, we devise a Promptable Dynamic Disentangler that utilizes a confidence-aware fusion strategy of learned dynamic probabilities and optional semantic text priors, effectively isolating massive transient entities. Further…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22888v2

### [AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T11:10:53Z
- **更新判定：** 真正新增
- **核心内容：** For full-body avatars, modeling surface dynamics is crucial for overcoming the uncanny valley and achieving perceptual realism. Person-agnostic methods recover static 3D avatars from monocular images, videos, or text prompts, but their skeleton-driven animations lack realistic surface dynamics such as clothing wrinkles. In contrast, person-specific methods achieve high-quality rendering and realistic dynamics, but require expensive multi-view captures for each individual. Recent generalizable dynamic avatar methods struggle to embed surface dynamics, leading to either limited multi-view consistency or dynamic expressiveness. To this end, we propose AvatarDynamizer, a generative method that transforms an off-the-shelf static 3D avatar into a controllable, realistic, and multi-view-consistent 4D avatar. We introduce a novel texture-space surface-dynamics embedding and formulate avatar dynamics modeling as conditional texture generation. Our encoder--decoder representation embeds pose-de…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.19900v1

### [QuARC-GS: Quantized Anchored Residual Coding for Compact Dynamic Scene Streaming with Gaussian Splatting](https://arxiv.org/abs/2608.18285v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T20:06:16Z
- **更新判定：** 真正新增
- **核心内容：** 3D scene representation techniques such as neural radiance fields (NeRFs) and Gaussian splatting have made substantial progress in novel view synthesis, achieving high-quality renderings from arbitrary view angles. More recently, such techniques have been extended to dynamic 3D scenes; however, achieving sustainable online free-viewpoint video (FVV) streaming remains challenging, especially for longer videos, due to significant storage demands of detailed scene representations and high reconstruction/rendering speed needs. To address these challenges, we propose Quantized Anchored Residual Coding Gaussian Streaming (QuARC-GS), a quantization-aware 4D scene optimization framework for online dynamic scene reconstruction that achieves ultra-high compression while maintaining reconstruction speed and quality. QuARC-GS represents a scene using a single canonical frame and highly compressed per-frame residuals. Specifically, we compress each residual through two complementary strategies tar…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.18285v1

### [AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T07:39:07Z
- **更新判定：** 真正新增
- **核心内容：** Recent monocular 3D Gaussian Splatting (3DGS) streaming reconstruction methods have achieved impressive performance by balancing reconstruction quality and efficiency. However, extending these frameworks to underwater scenes remains challenging due to severe visual degradation, such as light attenuation and scattering, which degrades camera pose tracking and distorts scene geometry. To address these challenges, we propose AquaFlow, a monocular Gaussian Splatting streaming reconstruction framework for efficient and high-fidelity underwater reconstruction. Specifically, AquaFlow fine-tunes a 3D vision foundation model on large-scale underwater data for robust pose and pointmap estimation, and introduces a medium-guided incremental Gaussian initialization strategy for streaming mapping. Furthermore, we develop a streaming-compatible hybrid scene representation that integrates structured, distance-conditioned neural Gaussians with a physics-inspired optical model to compensate for underwa…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22906v1

### [TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction](https://arxiv.org/abs/2608.20687v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-21T02:49:48Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting has achieved remarkable success in novel view synthesis. However, extracting high-fidelity surfaces directly from 3DGS remains challenging due to its discrete and unstructured nature. Existing 3DGS-based reconstruction methods typically rely on multi-view geometric consistency or local constraints. Without an explicit structured geometric prior during optimization, these methods often struggle to resolve structural ambiguities, leading to artifacts and floaters, particularly in textureless or occluded regions. To address this limitation, we propose TopoSurfel, a novel framework that closes the loop between Gaussian surfels and continuous meshes. Unlike recent methods that incorporate mesh extraction into the differentiable pipeline by introducing auxiliary neural networks or extra per-Gaussian parameters, we dynamically extract a continuous proxy mesh via a non-trainable differentiable iso-surfacing process. Leveraging this differentiable connection, we introduce…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.20687v1

### [Depth Anything V4: Dynamic 4D Scene Reconstruction via Riemannian Flow Matching on 4D Gaussian Splatting](https://arxiv.org/abs/2608.18388v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T09:04:46Z
- **更新判定：** 真正新增
- **核心内容：** We present Depth Anything V4 (DAV4), a framework for dynamic 4D scene reconstruction from monocular video. Our key contribution is the application of Riemannian Flow Matching (RFM) to 4D Gaussian Splatting parameters, defining probability paths directly on non-Euclidean manifolds (scale, rotation, opacity), ensuring all intermediate states are valid. Through controlled experiments, we isolate RFM's contribution from test-time optimization (TTO) and pre-training. A deterministic MLP baseline with the same data, architecture, and TTO achieves F-score 0.762; RFM achieves 0.806 - the +0.044 gain is RFM's isolated contribution. We provide corrected computational cost analysis: pre-training is 360 GPU-hours, amortizing for large-scale deployment (over 10,000 scenes). Uncertainty is quantified via Negative Gaussian Log-Likelihood and Expected Calibration Error. DAV4 outperforms prior Depth Anything models and per-scene 4D-GS on dynamic reconstruction and novel-view synthesis, while using no…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.18388v2

### [MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM](https://arxiv.org/abs/2608.15024v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-15T04:20:51Z
- **更新判定：** 真正新增
- **核心内容：** Current Vision-based SLAM systems fail catastrophically when motion blur corrupts the visual input, as they attempt the ill-posed inverse problem of recovering sharp content from degraded observations. We present MotionGS-SLAM, which fundamentally reimagines motion blur handling through a paradigm shift: rather than removing blur artifacts, we reformulate the challenge as a well-constrained forward problem that generatively models blur formation within the rendering pipeline. By leveraging event cameras' microsecond temporal resolution and immunity to motion blur, we introduce a novel event-modulated Gaussian kernel that dynamically adapts each Gaussian's rasterization based on precise motion cues. Our dual-modulation mechanism transforms 2D Gaussian projections from isotropic dots into anisotropic, motion-aligned elliptical brush strokes (spatial modulation) while adaptively varying exposure integral sampling density based on local velocity (temporal modulation). This physics-based a…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.15024v1

### [GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-25T15:34:13Z
- **更新判定：** 真正新增
- **核心内容：** World-Action Models (WAMs) jointly learn future visual prediction and action generation, using video dynamics as a representation-learning signal for robotic manipulation. However, their video latents are primarily optimized for visual prediction and are not explicitly encouraged to preserve cross-view geometric structure or spatially localized, object-relevant semantics. We propose \textbf{GaussianWAM}, a training-time representation-enhancement framework that organizes geometric and semantic supervision through a 3D Gaussian field. Given synchronized multi-view observations, frozen geometry and vision foundation models provide depth, camera parameters, and dense semantic features. GaussianWAM binds these heterogeneous signals to shared Gaussian primitives and renders spatially aligned semantic, depth, and coverage targets, which are distilled into the current-observation representations of the WAM. All teacher models, Gaussian components, and auxiliary prediction heads are removed a…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.24714v1

### [Physics-Integrated Operator Learning via Gaussian Splatting Representations](https://arxiv.org/abs/2608.24049v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-25T04:18:08Z
- **更新判定：** 真正新增
- **核心内容：** Neural operators provide efficient surrogates for spatiotemporal PDE systems, but purely data-driven formulations often accumulate substantial errors during long-horizon autoregressive prediction and may fail to exploit available governing-equation structure. Existing approaches incorporate physics primarily through residual-based training objectives or PDE-specific architectural constraints, which can introduce optimization difficulties or limit architectural generality. In this work, we introduce a representation-level approach to physics integration in which a feed-forward Gaussian splatting (FFGS) representation serves as a continuous interface between discretized solution fields and governing operators. The FFGS representation reconstructs the state as a continuous Gaussian field with closed-form spatial derivatives, allowing available physical PDE operators to be integrated directly within the learned evolution map without introducing a physics-residual loss. We evaluate the fra…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.24049v1

### [LagrangeGS: Non-Conservative Lagrangian System on Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2608.22773v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T03:51:21Z
- **更新判定：** 真正新增
- **核心内容：** Dynamic 3D Gaussian Splatting (3DGS) achieves photorealistic reconstruction of time-varying scenes, and recent physics-aware extensions improve extrapolation by explicitly predicting velocity fields. However, these extensions merely fit vector fields to visual deformations without satisfying Lagrangian mechanics, leading to three major issues: (i) physically inconsistent trajectories, (ii) lack of time-reversibility, and (iii) geometric collapse during long-term extrapolation. In this paper, we propose LagrangeGS, which formulates dynamic 3DGS as a non-conservative Lagrangian system. While this Lagrangian formulation fundamentally solves (i), a direct application of general LNNs to dynamic 3DGS requires a large velocity-Hessian inversion for millions of Gaussian particles. To overcome this computational bottleneck, we approximate the velocity-Hessian as an identity matrix, decoupling particle dynamics for computational tractability. For (ii), we restrict the non-conservative forces to…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22773v1

### [Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2608.22102v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-22T20:47:17Z
- **更新判定：** 真正新增
- **核心内容：** We present GCA (Gaussian Constitutive Alignment), a framework for learning implicit constitutive laws from monocular dynamic video of deformable objects represented by 3D Gaussians. Given a static multi-view scan for geometric initialization, our method learns intrinsic physical dynamics solely from a single fixed-viewpoint video of the moving object. Existing implicit methods often suffer from local minima under noisy supervision and lack physical interpretability, while explicit approaches rely on predefined constitutive equations, limiting generalizability and becoming unstable in monocular settings. To address these challenges, our framework unifies LoRA-based adaptation with two key alignment modules. First, we propose Rank-based Depth-Geometric Anchors (RDGA) to establish robust geometric constraints from monocular dynamic observations via scale-invariant rank-based depth alignment, reducing the reliance on unreliable pixel-level color supervision. Second, a Constitutive Prior R…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22102v1

### [Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T01:54:26Z
- **更新判定：** 真正新增
- **核心内容：** Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion. Recent bidirectional approaches address this problem using rewards signals built upon 3D Gaussian-Splatting reconstruction. However, a single rigid 3d reconstruction cannot model a dynamic scene, so this critic penalizes genuine object motion as reconstruction error and is maximized by freezing the video. This shortcut is especially detrimental in the AR setting, where each chunk can propagate an already-static configuration. In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards. To further guide motion magnitude and quality, we add a m…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.19556v1

### [GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation](https://arxiv.org/abs/2608.17988v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T16:33:49Z
- **更新判定：** 真正新增
- **核心内容：** Many scalable latent 3D generators operate on structured tensors, whereas pre-optimized 3D Gaussian Splatting (3DGS) reconstructions are unordered, spatially irregular, and vary widely in primitive count. We present GS-Voxel, a fitting-free structured latent framework, and evaluate it for large-scale aerial 3D Gaussian scene generation. GS-Voxel deterministically converts a compatible pre-optimized 3DGS reconstruction into sparse active voxels without additional per-scene optimization, retaining the sub-voxel positions and rendering attributes of the selected primitives. A GS-specific factorized VAE then separately encodes voxel geometry and local Gaussian attributes into sparse 3D latents whose size grows with the number of occupied voxels rather than being limited by a fixed scene-wide primitive count. We train image-conditioned flow models in the GS-Voxel latent space to generate aerial 3DGS scenes. A key application enabled by GS-Voxel is large-area scene generation: overlap-aware…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17988v1

### [SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T11:39:25Z
- **更新判定：** 真正新增
- **核心内容：** Animatable 3D Gaussian head avatars offer high-fidelity and flexible facial rendering, but typically require substantial storage and transmission costs for numerous Gaussian primitives. Existing Gaussian head avatar methods overlook the visual saliency of different head semantic regions for more appropriate Gaussian primitive allocation, as well as the efficient compression of trained head avatar sequences. To tackle this obstacle, we propose SACHA, a dynamic head avatar compression framework that leverages both semantic-aware density control and appearance-motion decomposition to achieve compact representation and high-quality novel-view rendering of head avatar sequences. Specifically, the semantic-aware density control guides the adaptive allocation of Gaussian primitives across different head regions with region-adaptive densification and pruning. In addition, the appearance-motion decomposed compression further reduces the temporal redundancy of the avatar sequence by transmittin…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.23133v1

### [Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T02:58:24Z
- **更新判定：** 真正新增
- **核心内容：** Generalizable 3D Gaussian Splatting (G-3DGS) has emerged as a promising approach for novel view synthesis undersparse-view settings. However, existing frameworks remain restricted by pixel-aligned Gaussian estimation, whichstruggles in partially observed or occluded regions and often leads to incomplete surfaces or structural collapse. Toaddress these challenges, we propose SeeU (Seeing the Unseen), a novel G-3DGS framework. We frame its core design asSemantic-in-Gaussian: semantic-conditioned refinement in Gaussian space. Specifically, we introduce a Cross-viewEntropy-Aware (CEA) module that aggregates multi-view semantic and geometric cues into compact embeddings. Theseembeddings guide the Conditional Gaussian Transformer, which applies residual updates to coarse Gaussians, helpingrecover under-constrained regions of partially observed structures while preserving surface consistency. Comprehensiveexperiments on multiple benchmarks demonstrate that SeeU consistently improves renderin…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22740v1

### [Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior](https://arxiv.org/abs/2608.22344v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-23T10:21:30Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) achieves state-of-the-art rendering quality at real-time speeds but suffers from "model bloat" - a large number of redundant, low-opacity Gaussians that inflate memory usage and training costs. This inefficiency stems from the standard "densify-then-prune" paradigm, which expands the model aggressively before relying on pruning to achieve compactness. To mitigate this problem, we present an efficient training framework that builds an intrinsically compact representation, replacing the conventional densify-then-prune cycle. Our method leverages a synergistic design: an L2 reconstruction loss to provide error-proportional gradients that stabilize optimization, and a novel Polarized Opacity Prior (POP) to actively manage the Gaussian population. POP steers informative primitives toward full opacity and uninformative ones toward transparency, enabling natural pruning and accelerating rendering through Early Ray Termination. Experiments on three public datasets…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.22344v1

### [GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-22T08:47:29Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) has achieved remarkable success in novel view synthesis; however, reconstructions under sparse views often exhibit noticeable artifacts. While recent video diffusion models provide strong spatio-temporal priors for 3DGS restoration, directly fine-tuning them for restoration is suboptimal, as they lack awareness of the underlying multi-camera geometry, resulting in multi-view inconsistencies. In this work, we propose a novel 3D-aware video restoration framework designed to enhance the quality of sparse 3DGS reconstruction. Specifically, we construct a large-scale 3DGS video dataset to enable specialized fine-tuning. To bridge the gap between 2D video generation and 3D multi-view constraints, we introduce a camera-conditioned geometric prior. By using the first and last frames as boundary anchors and encoding the corresponding camera relationships, we explicitly inject spatial structure into the video generation pipeline. This boundary-anchored, camera-aware…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.21849v1

### [4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://arxiv.org/abs/2608.20335v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T17:59:53Z
- **更新判定：** 真正新增
- **核心内容：** We present 4DAnyone, a framework for reconstructing 4D humans from an uncalibrated monocular video by generating reconstruction-grade multiview-consistent videos and lifting them into 4D Gaussian Splatting (4DGS). Existing camera-controlled video diffusion models synthesize plausible novel-view videos but fail to maintain consistency when scaled to the tens of target views required for 4DGS reconstruction. We identify this failure as a bounded-attention-context problem: when target views exceed the capacity of a single DiT forward pass, they must be split into groups, exposing two coupled bottlenecks. On the reference-context side, conditioning on all previously generated views grows as $O(N)$, weakening cross-view appearance guidance. On the target-context side, disjoint groups cannot directly exchange information, causing global structural drift. 4DAnyone addresses both bottlenecks with two complementary designs: Reference Context Packing (RCP) compresses growing reference views int…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.20335v1

### [Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T13:15:27Z
- **更新判定：** 真正新增
- **核心内容：** Sparse view 3D reconstruction is commonly addressed with neural implicit surfaces or dense point-based representations such as Gaussian splatting. Surface-aware splatting methods improve extracted geometry through oriented primitives and regularization, while RadiosityGS incorporates differentiable light transport through a radiosity inspired finite-element surfel formulation. We propose a differentiable point rendering method based on opacity-bearing beta surfels. An opacity explicit adjoint light transport formulation provides gradients for surfel geometry and appearance parameters, allowing physically based light transport to constrain reconstruction. Across five synthetic objects reconstructed from ten posed views, our method achieves the lowest mean symmetric Chamfer distance among the evaluated baselines and reduces mean Chamfer distance by 28.5% relative to the strongest point-based baseline while using only 267 surfels on average, approximately ~161 fewer primitives. Direction…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.20000v1

### [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T16:08:10Z
- **更新判定：** 真正新增
- **核心内容：** This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displacement of the camera mount can reduce the success rate on the LIBERO benchmark from about 90% to about 10% in the worst case. Prior approaches, such as large-scale fine-tuning or generative data augmentation, are computationally expensive and risk catastrophic forgetting. To address this, viewpoint shifts are reformulated as a localized novel-view synthesis problem. Under a Locality assumption, that camera perturbations remain within a small bounded region relative to the workspace, viewpoint norma…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.19066v1

### [USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes](https://arxiv.org/abs/2608.19036v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T15:29:06Z
- **更新判定：** 真正新增
- **核心内容：** Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic reconstruction is under-constrained while 3D detection lacks geometric grounding. To address this gap, we propose USR-Drive, a unified conditional generative framework that, given only posed multi-view driving videos, jointly recovers dense dynamic geometry and instance-level object layouts within a shared scene representation. Specifically, USR-Drive represents dense Gaussian primitives and sparse 3D bounding boxes as two aligned latent token streams and jointly denoises them with a unified multi…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.19036v1

### [CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T00:46:19Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting enables efficient novel view synthesis, but accurate mesh reconstruction remains difficult in weakly observed and occluded regions, where Gaussian primitives may grow into unstable or geometrically inconsistent structures. We propose CoMVS-GS, a general surface reconstruction framework that combines Multi-View Stereo with Gaussian splatting. CoMVS-GS initializes Gaussian primitives from dense multi-view stereo points with pre-flattened scales and normal-aligned orientations, providing stronger geometric priors than sparse structure-from-motion initialization and reducing ambiguity during early optimization. It further introduces PatchMatch-3DGS Mutual Supervision, where Gaussian-rendered depths and normals initialize PatchMatch refinement, and refined PatchMatch depths supervise Gaussian optimization to improve weakly constrained geometry. For surface extraction, CoMVS-GS replaces truncated signed distance field voxel fusion with a Delaunay graph-cut meshing pipe…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.18413v1

### [Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T11:55:58Z
- **更新判定：** 真正新增
- **核心内容：** Real-time novel view synthesis is dominated by rasterized explicit primitives. These projection-based pipelines provide high throughput but require specialized extensions for non-pinhole effects such as distortion, rolling shutter, and depth of field. Ray-based rendering expresses these effects naturally but is generally assumed too slow for competitive real-time rendering. We analyze the factors governing throughput in differentiable Voronoi ray tracing and identify traversal length, per-cell work, and memory locality as principal determinants. Guided by this, we introduce VoroTracing, which co-designs the scene representation, optimization, and GPU execution to reduce these costs. Compact octahedral appearance textures reduce memory traffic, while surface-concentrated opacity promotes early termination. The fixed-budget representation is optimized without pruning or densification and rendered with a GPU implementation designed for coherent traversal. On Mip-NeRF 360, VoroTracing ren…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17682v1

### [SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering](https://arxiv.org/abs/2608.17420v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T06:42:42Z
- **更新判定：** 真正新增
- **核心内容：** Driving scene reconstruction and rendering, especially with 3D Gaussian Splatting, has become an important component of autonomous driving simulation. However, rendered views often degrade under extrapolated ego trajectories and scene edits, producing blurry structures, temporal flicker, and foreground-background misalignment. Existing refinement methods are commonly designed for a specific setting, such as image-level novel-view repair or object-editing correction. In this paper, we introduce SPVC, a structured and panoptic video fixing framework for cross-dataset driving scene rendering. The name summarizes four design principles. (1) Structured fixing denotes the use of explicit spatial conditions, including camera pose, 3D bounding boxes, and HD maps, to guide the repair process and reduce uncontrolled hallucination. (2) Panoptic fixing refers to correcting both background rendering artifacts, such as distorted roads, buildings, and lanes, and foreground vehicle artifacts introduc…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17420v1

### [Scanline-Aware Animatable Gaussian Avatars from Rolling-Shutter Videos](https://arxiv.org/abs/2608.17314v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T03:08:33Z
- **更新判定：** 真正新增
- **核心内容：** Animatable human avatars are routinely reconstructed from multi-view video under a silent assumption: that every pixel of a frame observes the same instant of the body's motion. Rolling-shutter (RS) sensors expose image rows sequentially, so within one frame the head and the feet of a moving person are separated by tens of milliseconds of articulated motion, and every scanline sees a different pose. Feeding such video to a state-of-the-art avatar bakes the distortion into the canonical representation, where it survives as shear and wobble under novel views and novel poses. Worse, every camera in a rig follows its own readout schedule, so the multi-view consistency that drives the reconstruction is violated even when the geometry is correct. We present RS-Avatar, which reconstructs a sharp, undistorted, animatable 3D Gaussian avatar directly from RS video. The formulation is minimal: a motion-aware avatar already renders the body at several sub-frame instants, and where a blur model av…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17314v1

### [Geometry-Aware Online Mapping for 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2608.14902v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-14T21:20:16Z
- **更新判定：** 真正新增
- **核心内容：** Recent 3D Gaussian Splatting (3DGS) has enabled efficient photorealistic view synthesis and is rapidly being adopted in simultaneous localization and mapping (SLAM) systems for online mapping. In these systems, a Gaussian map must be expanded and refined incrementally while tracking runs in real time, so initialization and density control directly determine where limited computation and iterations are spent. This contrasts with offline 3DGS reconstruction, where such heuristics can be amortized over long optimization schedules. However, most 3DGS-SLAM pipelines inherit initialization and density-control heuristics from offline reconstruction, which can become brittle under the strict per-keyframe optimization budgets and incremental map growth of online SLAM. In this work, we revisit these heuristics in a decoupled 3DGS-SLAM setting and propose three geometry-aware methods that operate in the mapping thread: transmittance-preserving densification, camera-aware scale initialization fro…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.14902v1

### [HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-14T09:41:58Z
- **更新判定：** 真正新增
- **核心内容：** Octree-based anchor Gaussian Splatting has emerged as a scalable representation for city-scale novel view synthesis, where multi-level anchors adaptively capture scene content from coarse building structures to fine architectural details. However, we identify a fundamental limitation in existing methods: cross-level feature isolation, where each level's anchor features are optimized independently with no inter-level communication, causing color drift on building facades and over-smoothing in textured regions. We present HiCo-GS, a high-fidelity reconstruction framework with two complementary modules. Cross-Level Context Aggregation (CLCA) enables bidirectional hierarchical prior injection by leveraging the octree's spatial containment structure to aggregate per-level context vectors into parent-self-child triplets, fused via a lightweight MLP with residual connection. Coarse-level structural priors flow down to inform fine-level anchors, while fine-level detail statistics feed back to…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.14136v1

### [GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-13T17:29:53Z
- **更新判定：** 真正新增
- **核心内容：** Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations and camera poses. In this work, we propose a novel framework that reconstructs high-quality 3D scenes from a single SCI measurement by leveraging 3D Gaussian Splatting (3DGS) and the powerful priors of large-scale vision foundation models (VFMs). Our primary reconstruction combines measurement-derived 3D VFM initialization with SCI-aware Gaussian optimization. After coarse-stage convergence, an auxiliary 2D VFM provides pseudo-view supervision at synthesized viewpoints for local appearance ref…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.13502v1

### [Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://arxiv.org/abs/2608.13159v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-13T12:25:42Z
- **更新判定：** 真正新增
- **核心内容：** Cone-beam computed tomography (CBCT) enables volumetric reconstruction from X-ray projections, but suffers from severe artifacts--especially beam hardening--when imaging materials with high attenuation such as metals. These artifacts arise from the polychromatic nature of X-rays and are not properly addressed by conventional monochromatic reconstruction algorithms. While recent neural representation-based methods offer improved reconstruction quality, they are computationally expensive and often impractical for deployment. We propose a novel physics-inspired, self-calibrating metal artifact reduction method that efficiently reconstructs 3D CBCT volumes while correcting beam hardening artifacts. Our method integrates a polychromatic X-ray projection model, material-dependent attenuation profiles, and system response modeling into a Gaussian Splatting framework. Unlike prior work, we eliminate the need for manual metal masks or strong prior assumptions, and we optimize both reconstructi…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.13159v1

### [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-13T06:16:05Z
- **更新判定：** 真正新增
- **核心内容：** Vision-Language Navigation (VLN) for humanoid robots poses challenges existing benchmarks fail to address: bipedal locomotion imposes physical constraints absent from wheeled agents, humanoid morphologies vary across platforms, and egocentric observations are distorted by locomotion-induced camera dynamics. We present HumanoidVLN, a physics-grounded simulator and benchmark for VLN across diverse humanoid embodiments. Built on NVIDIA Isaac Sim, our platform supports an extensible set of humanoid configurations, demonstrated on four robots (Unitree G1, Unitree H1, Internal-A, Internal-B) spanning 10-12 lower-body DoF and heights from 1.17m to 1.80m, via a hierarchical control stack combining a reinforcement learning locomotion policy with interchangeable PD or MPC path trackers. New robots and VLN models integrate with minimal effort; we demonstrate compatibility with NaVILA, DualVLN, StreamVLN, and JanusVLN. Environments are drawn from artist-designed scenes and 3D Gaussian Splatting r…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.12860v1

### [Source-Face Authenticity Detection for 3D Gaussian Heads Reconstructed from a Single Portrait: A Benchmark and Dedicated Detector](https://arxiv.org/abs/2608.23984v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-25T02:24:16Z
- **更新判定：** 真正新增
- **核心内容：** Recent advances in single-image 3D Gaussian head reconstruction have enabled highly realistic and freely renderable digital heads from a single portrait. However, reconstruction and rendering can weaken the forgery traces in the source portrait, making the resulting 3D face difficult to classify whether its underlying face is real or fake, and thereby posing risks to identity authentication and face privacy. To study this problem, we introduce the first large-scale benchmark for this task by collecting real portraits and fake portraits from multiple sources and evaluate representative existing detectors on this benchmark, revealing their lack of explicit mechanisms for retaining fine-grained information and maintaining feature consistency across rendered views. To directly address these two limitations, we propose a detector trained with a two-stage strategy. In Stage I, masked autoencoding encourages the visual backbone to retain the fine-grained appearance information required for l…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.23984v1

### [FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T17:51:33Z
- **更新判定：** 真正新增
- **核心内容：** Rendering views using 3D scene representations such as Gaussian Splatting (3DGS), Neural Radiance Fields (NeRF), meshes, or even point clouds produces artifacts when input views are sparse or target views lie far from the input. Recent work mitigates these artifacts using diffusion-based generative priors, but is specialized to individual representations and require custom architectures or extensive retraining. We present FixAnything, a single model for fixing a wide range of rendering artifacts. It does so by repurposing a pretrained video generative model, leveraging its implicit multi-view priors with only minimal modification and lightweight finetuning. Our key insight is that even noisily-rendered sequences preserve camera motion and coarse scene structure, allowing cleanup to be formulated as video-to-video translation. To control what scene structure should be preserved, we introduce a binary mask denoting the clean pixels, enabling the model to anchor its output to high-qualit…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.23549v1

### [Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers](https://arxiv.org/abs/2608.23410v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T15:55:34Z
- **更新判定：** 真正新增
- **核心内容：** Photorealistic novel view synthesis of people remains challenging at high spatial resolutions and across multiple target cameras, where preserving identity, fine appearance details, and geometric coherence is critical. We build on the next-scale autoregressive paradigm and adapt it for human-centric view synthesis by enabling higher image resolutions, multi-view outputs and stronger cross-view consistency in a single forward pass. We train on a synthetic dataset of human faces spanning diverse identities and apparel. Contrary to diffusion models, this paradigm does not need 2D pre-training and, thanks to its next-scale architecture, it benefits from lower-resolution, general-purpose pre-trainings, with the full-sized purpose-specific images being used only in the last training stages. This enables our architecture to converge with a smaller amount of purpose-specific training data, allowing us to use a smaller but more realistic training dataset. The resulting model produces sharp and…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.23410v1

### [DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer](https://arxiv.org/abs/2608.18498v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T03:44:28Z
- **更新判定：** 真正新增
- **核心内容：** Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios. Existing dynamics modeling methods first compress reconstructed particle representations into sparse Key Points and model their evolution using locally constrained interactions, thereby discarding fine-grained local details and obscuring discriminative interaction modeling across spatial and temporal scales, leading to drifting trajectories and inaccurate appearance prediction. To tackle these issues, we propose DyG$^2$T, a dynamics modeling framework that infers object motion trajectories by spatially completing and temporally discriminating Key Point representations and modeling multi-scale interaction over particle graphs. Spatially, DyG$^2$T enriches each Key Point by aggregating neighboring raw particle positions to recover fine-grained local details, while explicitly encoding relative offsets among Key Points to…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.18498v1

### [LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting](https://arxiv.org/abs/2608.16324v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T09:29:12Z
- **更新判定：** 真正新增
- **核心内容：** We present LaGSplat (Latent Lagrangian Gaussian Splatting), a framework that infers interactive, physics-governed dynamics from one or a few monocular videos. At inference it lets a user push on the filmed object, rigid or deformable, with an external force that was never measured, annotated, or seen during training. This is possible because a low-dimensional latent state $\mathbf{q} \in \mathbb{R}^d$ plays two roles at once: it is the generalised coordinate of a learned dissipative Lagrangian and the conditioning variable of a Gaussian Splatting decoder. The inductive bias of this decoder, whose primitives are explicit points $μ_i(\mathbf{q})$ that move with the object, is what lets a force $f$ applied in the image pull back into a latent generalised force $J(\mathbf{q})^\top f$ and enter the equations of motion, which pixel-space (CNN) or neural-field (NeRF) decoders cannot do. We validate LaGSplat on test cases of increasing difficulty, from rigid to deformable and from autonomous…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16324v1

### [Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS](https://arxiv.org/abs/2608.16103v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T04:48:02Z
- **更新判定：** 真正新增
- **核心内容：** Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection. QAGaussian first learns query-conditioned multi-scale Gaussian slots as differentiable candidates whose receptive fields are shaped by the input expression. It then builds a relation-aware slot graph with language-conditioned edge weighting to propagate target-reference, attribute, part-whole, and contextual evidence. A granularity-adaptive router softly combines region-level, object-level, part-level, attribut…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16103v1

### [RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting](https://arxiv.org/abs/2608.15785v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-16T15:06:39Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) enables real-time novel-view synthesis but remains limited on GPUs at high resolutions. Through a stage-wise Roofline characterization, we identify two distinct hardware bottlenecks: global memory traffic dominates the front end, whereas instruction throughput limits rasterization. Guided by this analysis, we develop RoofGS, a rendering framework that applies bottleneck-specific optimizations rather than generic kernel acceleration. For the memory-bound front end, we design a resolution-adaptive quantized depth sorting key that compresses each key to 32 bits. For the compute-bound rasterizer, we introduce a range-aware bit-level fast exponential approximation tailored to the bounded exponent range after opacity culling, with a derived per-pixel error bound. These two core techniques are complemented by additional optimizations (kernel fusion, compact attribute storage, culling, dual-pixel evaluation) that additionally reduce memory traffic and improve inst…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.15785v1

### [Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats](https://arxiv.org/abs/2608.15651v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-16T09:43:50Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) represents 3D content with anisotropic primitives that jointly encode geometry and appearance. Fixed-budget encoders consume sampled observations of Gaussian assets, so the same object may be observed through different primitive realizations. Existing self-supervised methods mainly reconstruct masked Gaussian attributes, tying supervision to one sampled realization and requiring an input-space decoder. Latent prediction offers an alternative, but its application to Gaussian tokens requires targets that accommodate coupled attributes and heterogeneous spatial support. We introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context. An online encoder processes the context, while a shared exponential-moving-average encoder supplies stop-gradient features for multi-scale targets. Complementary target projections and feature-space grounding provide latent supervision without reconstructing Gaussian attributes. W…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.15651v1

### [3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T02:50:46Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting has made Gaussian primitives a highly efficient representation for real-time novel view synthesis, but its rasterisation-based formulation relies on screen-space approximations that limit accurate view-dependent ordering and the integration of secondary ray effects such as reflections, refractions, and shadows. Gaussian ray tracing addresses these limitations by evaluating explicit ray-primitive intersections, yet it remains costly to train. We observe that the main bottleneck is not ray traversal alone, but the pixel-centric backward propagation, where many threads concurrently accumulate gradients into the same primitive parameters, causing severe atomic contention and thread serialisation. We present 3DGART, a practical training framework for ray-traced Gaussian rendering. Our key idea is to reorganise backward propagation around primitives rather than pixels. Using conservative perspective-correct screen-space bounds, we build a compact intermediate buffer an…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17298v1

### [Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation](https://arxiv.org/abs/2608.23206v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-25T13:43:31Z
- **更新判定：** 真正新增
- **核心内容：** We study spherical occupancy profiles-the ray-wise occupancy probability profiles P(r) = T(r) o(r) distilled from multi-view 3D Gaussian reconstructions-as a unified intermediate representation for both discriminative and generative 3D reconstruction from images. On a 999-object subset of Google Scanned Objects with 48 turntable views each, we train (i) a discriminative per-ray decoder that injects global view-averaged and ray-specific image evidence into a FiLM-conditioned profile head, reaching median soft depth error 0.035 (normalized) on an independent 90-object test split, and (ii) a generative pipeline built on a profile VAE and a latent diffusion model, which supports unconditional sampling that matches the reconstruction manifold and image-conditioned multi-solution reconstruction whose per-object solution spread is quantifiable and tunable via classifier-free guidance. We further analyze the morphology of predicted profiles: post-hoc power sharpening and a learned sharpening…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.23206v2

### [NGS-Marker: Robust Native Watermarking for 3D Gaussian Splatting](https://arxiv.org/abs/2608.17447v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T07:28:18Z
- **更新判定：** 真正新增
- **核心内容：** With the rapid development and adoption of 3D Gaussian Splatting (3DGS), the need for effective copyright protection has become increasingly critical. Existing watermarking techniques for 3DGS mainly focus on protecting rendered images via pre-trained decoders, leaving the underlying 3D Gaussian primitives vulnerable to misuse. In particular, they are ineffective against Partial Infringement, where an adversary extracts and reuses only a subset of Gaussians. In this paper, we propose NGS-Marker, a novel native watermarking framework for 3DGS. It integrates a jointly trained watermark injector and message decoder, and employs a gradientbased progressive injection strategy to ensure full-scene coverage. This enables robust ownership decoding from any local region. We further extend NGS-Marker with hybrid protection (combining native and indirect watermarks) and support for multimodal watermarking. Extensive experiments demonstrate that NGS-Marker effectively defends against partial infr…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17447v1

### [LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning](https://arxiv.org/abs/2602.12314v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-14T14:12:25Z
- **更新判定：** 实质修订
- **核心内容：** We present LatentAM, an online 3D Gaussian Splatting (3DGS) mapping framework that builds scalable latent feature maps from streaming RGB-D observations for open-vocabulary robotic perception. Instead of distilling high-dimensional Vision-Language Model (VLM) embeddings using model-specific decoders, LatentAM proposes an online dictionary learning approach that is both model-agnostic and pretraining-free, enabling plug-and-play integration with different VLMs at test time. Specifically, our approach associates each Gaussian primitive with a compact query vector that can be converted into approximate VLM embeddings using an attention mechanism with a learnable dictionary. The dictionary is initialized efficiently from streaming observations and optimized online to adapt to evolving scene semantics under trust-region regularization. To scale to long trajectories and large environments, we further propose an efficient map management strategy based on voxel hashing, where optimization is…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2602.12314v2

### [GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T04:38:45Z
- **更新判定：** 实质修订
- **核心内容：** Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative priors to hallucinate missing content, yet naive integration frequently causes structural drift and temporal inconsistency due to the mismatch between stochastic 2D generation and deterministic 3D geometry. In this paper, we propose GeoRect4D, a novel unified framework for sparse-view dynamic reconstruction that couples explicit 3D consistency with generative refinement via a closed-loop optimization process. Specifically, GeoRect4D introduces a degradation-aware feedback mechanism that incorporates a robust anchor-based dynamic 3DGS substrate with a single-step diffusion rectifier to hallucinate high-fidelity details. This rectifier utilizes a structural locking mechanism and spatiotemporal coordinated attention, effectively preserving physical plausibility while restoring missing conten…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.20784v3

### [RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T09:51:13Z
- **更新判定：** 实质修订
- **核心内容：** Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve represe…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2607.15048v2

### [GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T01:32:04Z
- **更新判定：** 实质修订
- **核心内容：** Despite substantial progress in visual localization, from scene coordinate regression to direct camera pose regression, achieving both robust generalization and high accuracy remain challenging. This study introduces GS-CPE (Gaussian Splatting based Camera Pose Estimation), a coarse-to-fine framework for 6-DoF camera pose estimation that unifies geometry-based coarse pose estimation with robust 3D Gaussian Splatting (3DGS) warping based pose refinement. GS-CPE first estimates a coarse pose via retrieval-guided geometric pose estimation on a 3DGS scene representation, then refines it by minimizing a visibility aware masked RGB warping objective in a multi-scale optimization framework, with adaptive re-rendering. Extensive experiments on indoor and outdoor benchmarks including 7Scenes, Cambridge Landmarks, FAST-LIVO2 datasets, and a custom dataset demonstrate state-of-the-art performance, consistently outperforming in both accuracy and generalization.
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.10938v2

### [VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T16:24:21Z
- **更新判定：** 实质修订
- **核心内容：** Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restri…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.20531v2

### [Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-14T08:57:45Z
- **更新判定：** 实质修订
- **核心内容：** Accurate, site-specific channel information is crucial for optimizing next-generation wireless networks. Among various approaches, localized statistical channel modeling (LSCM), which models the channel multipath angular power spectrum (APS) from the reference signal received power (RSRP) measurement, has emerged as a state-of-the-art method tailored for efficient network optimization. However, despite its effectiveness, LSCM cannot predict APS at the vast majority of locations where no measurements are available, which significantly restricts its applicability in large-scale, real-world scenarios. To address this challenge, we present point-cloud-assisted tangent Gaussian splatting (PC-TGS), the first framework to extrapolate APS to unmeasured outdoor grids by integrating sparse radio measurements with dense LiDAR-based geometry. PC-TGS represents environmental scatterers as anisotropic 3D Gaussians, initialized and refined through a relaxed-mean reparameterization of the raw point c…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.18734v2

### [RobustGS: Unified Boosting of Feedforward 3D Gaussian Splatting under Low-Quality Conditions](https://arxiv.org/abs/2508.03077v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-24T06:15:04Z
- **更新判定：** 实质修订
- **核心内容：** Feedforward 3D Gaussian Splatting (3DGS) overcomes the limitations of optimization-based 3DGS by enabling fast and high-quality reconstruction without the need for per-scene optimization. However, existing feedforward approaches typically assume that input multi-view images are clean and high-quality. In real-world scenarios, images are often captured under challenging conditions such as noise, low light, or rain, resulting in inaccurate geometry and degraded 3D reconstruction. To address these challenges, we propose a general and efficient multi-view feature enhancement module, RobustGS, which substantially improves the robustness of feedforward 3DGS methods under various adverse imaging conditions, enabling high-quality 3D reconstruction. The RobustGS module can be seamlessly integrated into existing pretrained pipelines in a plug-and-play manner to enhance reconstruction robustness. Specifically, we introduce a novel component, Generalized Degradation Learner, designed to extract g…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2508.03077v2

### [GS-Net: Heterogeneous Vehicle Data Reuse via Generalizable Plug-and-Play 3DGS Module](https://arxiv.org/abs/2409.11307v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T09:50:55Z
- **更新判定：** 实质修订
- **核心内容：** End-to-end autonomous driving is increasingly data-driven, yet data reuse across vehicles remains limited. Each new vehicle often requires additional data collection and retraining because camera translation, orientation, and field of view differ across sensor layouts. Cross-sensor view synthesis offers a promising route for cross-platform data reuse by synthesizing images under novel sensor configurations from existing sensor data. To realize this goal, we propose GS-Net, a lightweight plug-and-play module that aggregates local geometric context from sparse Structure-from-Motion (SfM) point clouds and expands each point into multiple dense Gaussian primitives in a single forward pass, learning a cross-scene generalizable initialization for standard 3DGS that improves rendering quality for both interpolated views along the original sensor trajectories and extrapolated views at new sensor positions. In such settings, target camera viewpoints often lie beyond the convex hull of training…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2409.11307v2

### [REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074v4)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T13:12:39Z
- **更新判定：** 实质修订
- **核心内容：** Existing pruning methods for 3D Gaussian splatting (3DGS) suffer from either severe quality degradation or prohibitive computational overhead. In this paper, we propose REFINE, a highly accelerated 3DGS pruning framework centered on a novel rendering-free primitive importance metric. Our approach leverages an analytically approximated, rendering-aware Hessian field to quantify the expected perceptual error induced by the removal of individual primitives. By modeling the joint modulation of visibility, projection geometry and the content adaptive hyperparameter, we entirely bypass costly forward rendering passes and derive an anisotropic perceptual weight field that serves as a high-fidelity proxy for primitive importance. Extensive experiments across multiple benchmark datasets demonstrate that REFINE maintains highly competitive rendering quality while achieving a $3,000\times$ reduction in pruning-related computational complexity, translating to a practical $\sim 20\times$ speedup i…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2606.09074v4

### [GSBF: Gaussian Splatting for Environment-Aware Beamforming](https://arxiv.org/abs/2608.05896v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-16T03:49:53Z
- **更新判定：** 实质修订
- **核心内容：** Beamforming plays a key role in multiple-input-multiple-output (MIMO) communication systems. However, conventional beamforming design normally requires accurate instantaneous channel state information (CSI) and iterative optimization, which incur substantial pilot overhead and computational complexity. Recognizing that radio propagation is intrinsically governed by the physical geometry, we develop a 3D Gaussian splatting for environment-aware beamforming (GSBF) pipeline based on multi-modal data, which characterizes the environment through a persistent 3D Gaussian representation. Specifically, GSBF models the environmental scattering response with reciprocity-preserving bidirectional spherical Gaussian (Bi-SG) kernels and performs two-sided electromagnetic rasterization to render an angular propagator map. The rendered map is then aggregated through an over-complete array-manifold dictionary and projected to the constant-modulus beamformers, thereby synthesizing beams directly from t…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.05896v2

### [Reprojection-Guided 3D Gaussian Splatting Diffusion for Weakly Supervised Single-Image Normal Estimation](https://arxiv.org/abs/2508.05950v4)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-15T02:52:22Z
- **更新判定：** 实质修订
- **核心内容：** We propose CLONE, a Continuous Latent Optimization framework for Normal Estimation via 3D Gaussian splatting. The core idea is to construct an image-geometry-image consistency strategy that unifies explicit geometric representation with differentiable rendering, thereby enabling weakly supervised learning without normal ground truth. Specifically, CLONE comprises four components. First, by introducing a differentiable light interaction model with a learnable modulation kernel, we perform a unified reparameterization of the 3DGS parameter space. Second, the conditional single-step deterministic refinement network integrates denoising architectures with differentiable reprojection constraints to refine the initial normals, thereby adaptively recovering the high-frequency details erased by the inherently smooth Gaussian primitives. Third, the cross-domain gating fusion mechanism adaptively combines the two complementary normal estimates, reconciling the geometrically consistent yet over-…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2508.05950v4

### [OctoSplat: Hybrid OctoMap-Gaussian Splatting for Active Semantic Mapping and Phenotyping with Horticultural Robots](https://arxiv.org/abs/2601.12122v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-14T15:06:23Z
- **更新判定：** 实质修订
- **核心内容：** Semantic reconstruction of agricultural scenes plays a vital role in tasks such as phenotyping and yield estimation. However, traditional approaches based on manual scanning or fixed camera setups remain a major bottleneck, while active-mapping methods based solely on occupancy grids are too coarse for accurate trait estimation. To address this gap, we propose an active 3D reconstruction framework for horticultural environments using a mobile manipulator. The system integrates OctoMap with 3D Gaussian Splatting to enable accurate and efficient target-aware mapping. A low-resolution OctoMap provides probabilistic occupancy information for informative viewpoint selection and collision-free planning, while 3D Gaussian Splatting leverages geometric, photometric, and semantic information to optimize 3D Gaussians for high-fidelity scene reconstruction. We further introduce a robust mapping strategy that mitigates semantic segmentation and depth noise, together with a background pruning meth…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2601.12122v2

### [2Xplat: Decoupling Geometry and Appearance Modeling for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21064v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-19T02:46:16Z
- **更新判定：** 实质修订
- **核心内容：** Pose-free feed-forward 3D Gaussian Splatting (3DGS) has opened a new frontier for rapid 3D modeling, enabling high-quality Gaussian representations to be generated from uncalibrated multi-view images in a single forward pass. The dominant approach adopts unified monolithic architectures, often built on geometry-centric 3D foundation models, to jointly estimate camera poses and synthesize 3DGS representations within a single network, entangling geometric reasoning and appearance modeling within a shared representation. In this work, we introduce 2Xplat, a pose-free feed-forward 3DGS framework based on a two-experts design that explicitly separates geometry estimation from Gaussian generation: a dedicated geometry expert first predicts camera poses, which are then passed to an appearance expert that synthesizes 3D Gaussians. Despite its conceptual simplicity, and being largely underexplored in prior works, our two-experts pipeline outperforms prior pose-free feed-forward 3DGS approaches…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2603.21064v3

### [DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-15T16:17:44Z
- **更新判定：** 实质修订
- **核心内容：** Radiance field reconstruction aims to recover high-quality 3D representations from multi-view RGB images. Recent advances, such as 3D Gaussian splatting, enable real-time rendering with high visual fidelity on sufficiently powerful graphics hardware. However, efficient online transmission and rendering across diverse platforms requires drastic model simplification, reducing the number of primitives by several orders of magnitude. We introduce DiffSoup, a radiance field representation that employs a soup (i.e., a highly unstructured set) of a small number of triangles with neural textures and binary opacity. We show that this binary opacity representation is directly differentiable via stochastic opacity masking, enabling stable training without a mollifier (i.e., smooth rasterization). DiffSoup can be rasterized using standard depth testing, enabling seamless integration into traditional graphics pipelines and interactive rendering on consumer-grade laptops and mobile devices. Code is…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2603.27151v2

### [LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning](https://arxiv.org/abs/2604.16910v3)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-15T06:36:22Z
- **更新判定：** 实质修订
- **核心内容：** Low-altitude Gaussian splatting (LAGS) facilitates 3D scene reconstruction by aggregating aerial images from distributed drones. However, as LAGS prioritizes maximizing reconstruction quality over communication throughput, existing low-altitude resource allocation schemes become inefficient. This inefficiency stems from their failure to account for image diversity introduced by varying viewpoints. To fill this gap, we propose a groupwise heterogeneous graph neural network (GW-HGNN) for LAGS resource allocation. GW-HGNN explicitly models the non-uniform contribution of different image groups to the reconstruction process, thus automatically balancing data fidelity and transmission cost. The key insight of GW-HGNN is to transform LAGS losses and communication constraints into graph learning costs for dual-level message passing. Experiments on real-world LAGS datasets demonstrate that GW-HGNN significantly outperforms state-of-the-art benchmarks across key rendering metrics, including PS…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.16910v3

### [FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-23T11:59:36Z
- **更新判定：** 实质修订
- **核心内容：** Gaussian Splatting (GS) has emerged as a dominating technique for image rendering and has quickly been adapted for the X-ray Computed Tomography (CT) reconstruction task. However, despite its growing popularity, the benefits of GS are typically not substantial enough to motivate a transition from well-established reconstruction algorithms. This paper addresses the most significant remaining limitations of the GS-based approach by introducing FaCT-GS, a framework for fast and flexible CT reconstruction. Enabled by an in-depth optimization of the voxelization and rasterization pipelines, our new method is significantly faster than its predecessors and scales well with projection and output volume size. Furthermore, the improved voxelization enables rapid fitting of Gaussians to pre-existing volumes, which can serve as a prior for warm-starting the reconstruction, or simply as an alternative, compressed representation. FaCT-GS is over 4X faster than the State of the Art GS CT reconstruct…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.01844v2

### [P-WRFGS: Pruning 3D Gaussians for Efficient Wireless Radiance Field Construction](https://arxiv.org/abs/2605.15324v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-23T08:15:52Z
- **更新判定：** 实质修订
- **核心内容：** Wireless channel modeling is a key building block for next-generation wireless systems. Predicting the channel state information (CSI) across different transmitter locations can substantially reduce the pilot and feedback overhead of conventional channel estimation. We propose P-WRFGS, an efficient wireless radiance field modeling framework built upon 3D Gaussian splatting. P-WRFGS introduces a learnable mask for each 3D Gaussian primitive to indicate its importance, which guides the pruning of less significant primitives for more efficient rendering. The model is trained using a weighted combination of rendering and regularization losses, allowing a flexible trade-off between rendering quality and efficiency. Numerical results on the $\text{NeRF}^2$ dataset demonstrate that P-WRFGS achieves up to 100$\times$ storage reduction and 7$\times$ rendering speed-up with only mild degradation in SSIM and the achievable rate. Moreover, initializing the Gaussian primitives from a 3D point clou…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2605.15324v2

### [Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence](https://arxiv.org/abs/2603.21933v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T15:19:16Z
- **更新判定：** 实质修订
- **核心内容：** The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training pruning method for 3D Gaussian splats that relies solely on attribute-derived neighbourhood descriptors. As our primary contribution, we introduce a hybrid descriptor framework that captures structural and appearance consistency directly from the splat representation. Building on these descriptors, we formulate pruning as a statistical evidence estimation problem and introduce a Beta evidence model that quantifies per-splat reliability through a probabilistic confidence score. Experiments condu…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2603.21933v2

### [Compile kernels to MSL on macOS (#519) * Compile kernels to MSL on macOS Turns on burn-wgpu's `metal` feature, so on macOS cubecl emits Metal Shading Language instead of going through wgpu's WGSL frontend. The feature is inert elsewhere: cubecl-wgpu gates its objc2 dependencies on `target_vendor = "apple"`, so Linux, Windows and wasm builds are unaffected. This needs tracel-ai/cubecl#1525. `workgroup_uniform_load` is documented as a barrier plus a load, but only the WGSL backend actually synchronised, so on MSL the rasterizer read a tile's splat range before unit 0 published it and blended the wrong splats. Renders were nondeterministic on large scenes. The cubecl patch here carries that fix alongside the wasm one. 5000 steps on mipnerf360/garden, release build, same machine: 422.5s on WGSL against 395.7s on MSL, so roughly 6% end-to-end including the shared dataset load. Later repeat runs drifted (the machine came off AC), so treat the size as approximate; the direction held across every run and every synthetic bench. * Gate the metal feature to macOS Enabling it workspace-wide broke Linux: `metal` pulls in cubecl's msl path for the whole graph, and while the objc2 dependencies are gated on `target_vendor = "apple"`, the feature itself still changes codegen everywhere. WGSL then started emitting `vec4<u8>`, which is not a WGSL type, and elemwise_fuse failed to compile. Declaring it under `cfg(target_os = "macos")` in brush-cube keeps MSL on for macOS and off elsewhere. Verified with `cargo tree -e features`: cubecl-wgpu gets "msl" on the host and not for wasm32 or x86_64-linux. * TEMP: diagnostic to see what the CI GPU reports Deliberately panics with the adapter name and type support so the CI log tells us why native MSL is not being selected there. To be reverted. * TEMP: move the GPU diagnostic into the failing test binary cargo test stops at the first failing binary, so the diagnostic in brush-cube never ran. Tests within one binary all run, so put it here. * Revert the temporary GPU diagnostics They did their job: the CI runner reports "Apple Paravirtual device" with no u8 support and no plane Ops/Sync, so cubecl correctly refuses native MSL there and falls back to WGSL. * Pin bool tensors to u32 storage burn flips WgpuDevice's default bool storage to u8 the moment the metal feature is on, but cubecl picks the shader compiler at runtime: it wants MTLGPUFamily::Apple7 and a Metal compiler >= 3.2, and falls back to WGSL otherwise. CI's runner is an "Apple Paravirtual device" that fails that check, so it compiled WGSL against u8 bools and died on `vec4<u8>`. u32 bools are valid under both compilers, so pin them rather than depend on which one we land on. Costs 3 bytes an element on a handful of 1-D masks. This keeps MSL on real hardware and WGSL everywhere else, from one build config, so no feature flag and no CI changes. The pin is behind a Once: the setting is global, and calling it per device races with tests building tensors in parallel. * Make native MSL opt-in instead of pinning bool storage Reverts the u32 bool pin. It worked, but it relied on a global runtime setting that every device-creation path had to remember to call, and brush-c's FFI entry point duly missed it and failed CI. It also gave up u8 bool storage on Metal, which is the one place u8 actually works. Instead `brush-cube/metal` is an opt-in feature. Each build is then internally consistent: without it burn keeps u32 bools and WGSL compiles them, with it burn uses u8 bools and MSL has a u8 type to compile them with. CI drops --all-features, which would otherwise sweep the opt-in feature back in. debug-validation is named explicitly and still cascades from brush-app into render/train/process; tracy is profiling-only and not needed for tests. Run the native path with: cargo test --workspace --features brush-cube/metal](https://github.com/ArthurBrussee/brush/commit/362dc39417c0f9e4f02784c7d73f11204fc63390)

- **主题：** 训练与优化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-08-16T22:14:58Z
- **更新判定：** 代码实质更新
- **核心内容：** Compile kernels to MSL on macOS (#519) * Compile kernels to MSL on macOS Turns on burn-wgpu's `metal` feature, so on macOS cubecl emits Metal Shading Language instead of going through wgpu's WGSL frontend. The feature is inert elsewhere: cubecl-wgpu gates its objc2 dependencies on `target_vendor = "apple"`, so Linux, Windows and wasm builds are unaffected. This needs tracel-ai/cubecl#1525. `workgroup_uniform_load` is documented as a barrier plus a load, but only the WGSL backend actually synchronised, so on MSL the rasterizer read a tile's splat range before unit 0 published it and blended the wrong splats. Renders were nondeterministic on large scenes. The cubecl patch here carries that fix alongside the wasm one. 5000 steps on mipnerf360/garden, release build, same machine: 422.5s on WGSL against 395.7s on MSL, so roughly 6% end-to-end including the shared dataset load. Later repeat runs drifted (the machine came off AC), so treat the size as approximate; the direction held across e…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [Spring clean: latest burn/cubecl, drop the egui fork, merge render-bwd, autodiff via backend_extension (#517) * Update deps: burn/cubecl latest, wgpu 30, egui 0.35, rerun 0.34; migrate lpips weights to burnpack; hand-rolled Adam states replace OptimizerAdaptor * Drop redundant count_contributing_tiles walk in map_gaussians (pad from emitted count) * Take grad by reference in AdamScaled::step * Add COLMAP text-model loader tests and brush-cli arg tests * Bump itertools/safetensors, drop dep debuginfo in dev builds * Bump burn to 62ca8c58; patch cubecl family for wasm build fix * Update deps: latest burn, cubecl at the rev burn pins Advance burn to latest main (67dbe6ea) and move the cubecl patch to 5fce8a89 — upstream 088dd705, which is exactly the rev burn pins, with our two wasm fixes rebased on top. The fork branch was 38 commits behind that, so latest burn no longer built against it. Adapt to two cubecl API changes: - Vector insert/extract now take `#[comptime] index: usize`; bare integer literals defaulted to i32 and no longer satisfy the bound. - `Type::scalar` is now `Type::new`. Pin ureq/ureq-proto back a patch release: 3.4.0/0.6.1 switch to base64 0.23 while the rest of the tree is on 0.22, which trips the bans check. Note a plain `cargo update` re-floats both and reintroduces it. Skip spin and downcast-rs in deny.toml — both are upstream version mismatches we can't resolve locally (burn 0.11 vs cubecl 0.12; pliron 2 vs wayland-backend 1). * Reword PNGs -> PNG files to satisfy typos check typos parses "PNGs" as PN + Gs and suggests "ON", failing CI. Rewording the doc comment is cleaner than adding a global extend-words exception. * Drop the egui fork; move to upstream egui 0.36 egui 0.36 ships the wgpu-30 upgrade (emilk/egui#8289) that our fork existed to carry, so all ten egui-family patch entries are gone and the stack comes from crates.io again. The wgpu fork stays — subgroup ops and GPUDevice sharing are unrelated to this. Unblocks two crates that were pinned behind egui 0.35: - egui_tiles 0.16 -> 0.17 - rerun 0.34 -> 0.36 (needed ecolor/emath 0.36) No source changes were needed for 0.35 -> 0.36. The duplicate set shifts rather than shrinks: base64 is now forced by rerun's re_auth (0.23 vs 0.22 elsewhere) instead of by ureq, so the ureq/ureq-proto pins are no longer useful and are dropped — both are back on latest. pollster splits because eframe 0.36 moved to 1.0 while rfd (latest 0.17.2) still pins 0.4. Both are skipped in deny.toml. Verified: cargo build --workspace, cargo check -p brush-app -p brush-js --target wasm32-unknown-unknown (the fork's original reason for being), and cargo deny check bans all clean. * Merge brush-render-bwd into brush-render as a bwd module The backward path becomes `brush_render::bwd` instead of its own crate. Mechanically this is a move: git tracks every file as a rename, and the only edits are module paths (`brush_render::` -> `crate::`, and the crate's own `burn_glue`/`kernels` -> `crate::bwd::...`). Beyond dropping a crate, a manifest, and a dependency line from three callers, this unblocks the `Autodiff` arm of burn's `backend_extension`. The generated `impl SplatOps for Dispatch` lives in the crate defining `SplatOps` and calls the autodiff arm, so `impl SplatOps for Autodiff<..>` has to be visible from there. brush-render-bwd depended on brush-render, so that impl could never live in it — the orphan rule and the dependency direction both forbade it. Verified: cargo build --workspace and the CI wasm32 check both clean. * Dispatch the differentiable render through the Autodiff extension arm `SplatOps` now declares `#[backend_extension(Wgpu, Autodiff)]`, so the generated `Dispatch` impl routes autodiff tensors to a real `impl SplatOps for AutodiffMain` instead of `render_splats_with_pass` hand-rolling the unwrap/prepare/rewrap dance. Two consequences worth calling out: - `refine_weight` becomes a trait input. It was always a prepared autodiff node (the accumulator that catches the per-splat refinement gradient), just passed out of band; the extension trait has no way to see it otherwise. Concrete backends ignore it, and the inference path hands over a throwaway [1] zeros tensor. - Float aux (`visible`, `max_radius`, `projected_splats`) now rides back as untracked autodiff tensors rather than inner-backend ones, because the arm's output is uniformly `RenderOutput<Self>`. Int tensors share the inner primitive and are unchanged. Verified: 18/18 finite-diff and fuzz gradient tests pass, workspace builds clean. * Factor repeated fusion output-IR construction Eleven near-identical `TensorIr::uninit(client.create_empty_handle(), ..)` blocks collapse into two local helpers. Only shape and dtype ever varied. No behaviour change; the surrounding CustomOpIr/Operation structure stays as-is, since it already matches burn's own extension consumer (burn-vision) — there is no higher-level fusion helper in burn to move to. * Correct the stale rationale on AdamScaled The comment claimed burn only exposes optimizer state through host-side serialized records. That was true of `ModuleOptimizer`/`OptimizerAdaptor`, but burn's low-level `Optimizer` trait is now state-in/state-out with caller-owned `AdaptiveMomentumState` exposing live `time`/`moment_1`/ `moment_2` — structurally what we hold here. The hand-roll still stands: burn's Adam has neither the per-component LR scaling nor the second-moment reduction. Point the comment at those. * Fix backend mismatch from lifting render aux to autodiff Regression from the Autodiff extension arm. The arm's output is uniformly `RenderOutput<Self>`, so `visible` / `max_radius` came back as autodiff tensors and `SplatOutputDiff` handed them on. The trainer mixes those with inner-backend tensors, which trips burn-dispatch's same-backend assert — five training tests panicked in `float_add`. Unlift them at the `SplatOutputDiff` boundary instead: the trait keeps its uniform output, the public struct hands aux back on the inner backend exactly as before. They carry no gradient, so nothing is lost. Also fixes fuzz.rs, which calls `MainBackendBase::render` directly and needed the new `refine_weight` argument. Both slipped through because `cargo build --workspace` does not build test targets and only the finite-diff suite was run. `cargo check --workspace --all-targets` plus integration/finite_diff/fuzz all pass now. * Use cubecl FastDivmod for the tiles-per-row split `map_1d_to_2d` runs per pixel and splits a linear id into tile row and column with a runtime divide. `u.tile_bw` is a host-side uniform, so the magic numbers can be precomputed and the device-side divide becomes a multiply-and-shift. cubecl uses FastDivmod the same way for its tensor layout kernels. Scope is smaller than it looks. `map_gaussians` divides by `bb_w`, a per-splat bounding box width computed inside the kernel, so FastDivmod cannot apply there at all. The backward `tile_origin` divide is per-workgroup, not per-pixel, and not worth another launch argument. The `TILE_SIZE` divides are constant and already folded. Unmeasured: this is one divide per thread in a kernel that then loops over splats, so the effect is likely below noise, and the machine was on battery. Correctness verified — integration 9/9, finite_diff 18/18, fuzz 6/6. * cargo fmt * Use Self in the Autodiff SplatOps impl clippy::use_self, which CI runs with -D warnings. * Tighten up what the crate split was forcing open wgpu_kind! was #[macro_export] with the usual __wgpu_kind! forwarding dance, purely so brush-render-bwd could reach it. Nothing outside the crate uses it, so it collapses to one macro_rules! plus a pub(crate) use, and both macros leave the crate root. Same story for lift_to_autodiff, match_backend, SplatBwdOps, RasterizeGrads and SplatGrads: all public only because bwd lived elsewhere, none named outside the crate, all now pub(crate). * Drop the SplatOps supertrait from SplatBwdOps Nothing in the backward path needs it. Both implementors happen to implement SplatOps too, but the bound claimed you had to be renderable to have backward kernels, and the set is actually smaller: AutodiffMain and the generated Dispatch impl SplatOps and have no meaningful backward kernel. Say Backend instead, and write down why the two traits stay split. * Point cubecl at the upstreamed branch Same branch as before, now rebased onto current cubecl main for tracel-ai/cubecl#1524. Burn moves along with it to b6e27bd. Burn still pins cubecl 088dd705, so our patch now supplies a cubecl three commits newer than burn expects. Nothing breaks today, but that gap grows each time the PR gets rebased, so this stops being safe on its own once the two drift far enough. * Stop linking a now-private item from public docs lift_to_autodiff went pub(crate), which broke the intra-doc link from lift_splats_to_autodiff. CI documents with -D warnings, so it's fatal.](https://github.com/ArthurBrussee/brush/commit/3da02ecfe91aae9c011a8c8c482d82860b88eb1f)

- **主题：** 训练与优化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-08-14T22:27:41Z
- **更新判定：** 代码实质更新
- **核心内容：** Spring clean: latest burn/cubecl, drop the egui fork, merge render-bwd, autodiff via backend_extension (#517) * Update deps: burn/cubecl latest, wgpu 30, egui 0.35, rerun 0.34; migrate lpips weights to burnpack; hand-rolled Adam states replace OptimizerAdaptor * Drop redundant count_contributing_tiles walk in map_gaussians (pad from emitted count) * Take grad by reference in AdamScaled::step * Add COLMAP text-model loader tests and brush-cli arg tests * Bump itertools/safetensors, drop dep debuginfo in dev builds * Bump burn to 62ca8c58; patch cubecl family for wasm build fix * Update deps: latest burn, cubecl at the rev burn pins Advance burn to latest main (67dbe6ea) and move the cubecl patch to 5fce8a89 — upstream 088dd705, which is exactly the rev burn pins, with our two wasm fixes rebased on top. The fork branch was 38 commits behind that, so latest burn no longer built against it. Adapt to two cubecl API changes: - Vector insert/extract now take `#[comptime] index: usize`; bare…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [Add --invert-masks, and cut copies out of the image path (#521) Masks that mark "ignore" as white instead of black needed inverting by hand before training; --invert-masks (and a checkbox in the UI) does it at load time. While in there: - The mask is reduced to one channel right after decode, so a grayscale mask needs no conversion and the resize runs over 8bpp instead of 32. - Cached batches share their packed pixels behind a refcount, so a cache hit hands out a view instead of copying the whole image every step. - Premultiply + widen + pack are one pass over the image now, instead of three with two full-image allocations between them. - LOD boundaries keep the loader when the image scale didn't change, rather than dropping a warm cache and re-decoding the dataset.](https://github.com/ArthurBrussee/brush/commit/8b7f5c6c0638892204b540d9aced219f62fc2192)

- **主题：** 训练与优化
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-08-17T22:38:24Z
- **更新判定：** 代码实质更新
- **核心内容：** Add --invert-masks, and cut copies out of the image path (#521) Masks that mark "ignore" as white instead of black needed inverting by hand before training; --invert-masks (and a checkbox in the UI) does it at load time. While in there: - The mask is reduced to one channel right after decode, so a grayscale mask needs no conversion and the resize runs over 8bpp instead of 32. - Cached batches share their packed pixels behind a refcount, so a cache hit hands out a view instead of copying the whole image every step. - Premultiply + widen + pack are one pass over the image now, instead of three with two full-image allocations between them. - LOD boundaries keep the loader when the image scale didn't change, rather than dropping a warm cache and re-decoding the dataset.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [MrNeRF/LichtFeld-Studio](https://github.com/MrNeRF/LichtFeld-Studio)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T22:57:25Z
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
- **发布时间/更新时间：** 2026-08-25T19:52:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cross-vendor 3D Gaussian Splatting trainer - video to splat to mesh, Vulkan or CUDA.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/harry7557558/spirula-studio

### [usbunits-commits/NOESIS-AI](https://github.com/usbunits-commits/NOESIS-AI)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T17:48:22Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NOESIS AI is building an AI-native platform for 3D Gaussian Splat creation, editing, and optimization. We help creators transform real-world captures into clean, intelligent, production-ready 3D experiences—faster than ever before.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/usbunits-commits/NOESIS-AI

### [ddietz1/3DGS-Optimization-with-Stretch-3](https://github.com/ddietz1/3DGS-Optimization-with-Stretch-3)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T16:14:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A system for optimizing the creation of a 3D Gaussian Splatting model of a scene using a Hello Robot Stretch 3
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ddietz1/3DGS-Optimization-with-Stretch-3

### [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](https://arxiv.org/abs/2608.16234v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T08:12:56Z
- **更新判定：** 真正新增
- **核心内容：** Driving World Models (DWMs) have recently advanced rapidly with generative models, yet most existing methods mainly focus on conditional scene generation and lack explicit 3D scene understanding, language-grounded reasoning, and controllable 4D editing capabilities. Moreover, commonly used point cloud, occupancy, or BEV representations make it difficult to achieve fine-grained alignment between textual information and the underlying 3D scene structure. To address these limitations, we propose a foundation-feature Gaussian driving world model that unifies scene understanding, language-grounded reasoning, controllable 4D editing, and multi-modal generation within a single framework. Specifically, we introduce a foundation-feature Gaussian tokenizer that directly distills Qwen/SigLIP visual-language features into 3D Gaussian primitives, building a compact open-vocabulary Gaussian semantic field. We further design a geometry-aware Gaussian adapter that combines importance-aware hierarchic…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16234v1

### [Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction](https://arxiv.org/abs/2608.20602v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-20T22:47:42Z
- **更新判定：** 真正新增
- **核心内容：** Many consumer smartphones, stereo cameras, and light field cameras record multiple synchronized viewpoints in a single exposure event. However, novel view synthesis pipelines commonly use only a monocular stream and rely on camera motion or learned priors to obtain angular coverage. In this paper, we ask: why do we use only one viewpoint? We analyze sensor-limited multi-view, where one sensor trades off spatial and angular resolution, and exposure-limited multi-view, where multiple sensors on one commodity device observe each event simultaneously. We introduce a new dataset incorporating three types of commodity multi-view cameras, and evaluate sparse-view 3DGS and 4DGS baselines measuring reconstruction quality as a function of number of exposures and angle between extreme views. Our results demonstrate that using multiple cameras, even with a low baseline, significantly improves reconstruction quality in single-shot, few-shot, and casual video settings. In addition, under a fixed se…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.20602v1

### [Towards Alias-Free 4D Gaussian Representations with Motion-Aware Filtering](https://arxiv.org/abs/2608.21828v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-22T07:55:38Z
- **更新判定：** 真正新增
- **核心内容：** Novel-view synthesis of dynamic scenes, crucial for AR/VR applications, remains a challenging problem. Recent methods adapt representations like 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) for dynamic scenes by incorporating time as the fourth dimension (4D representations). These 4D representations still suffer from aliasing artifacts, especially when generating novel views from divergent viewpoints (zoom-in/zoom-out operations). While using 3D smoothing filters like those proposed in Mip-Splatting might seem like a possible solution, they fail to account for local motion and also exhibit aliasing. To address this, we propose a motion-aware 3D smoothing filter specifically designed for 4D representations. Our approach adapts the filter strength based on local motion information, effectively mitigating aliasing without compromising rendering quality. This is achieved by estimating the joint density function of time and focal-to-depth ratio using a non-parametric est…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.21828v1

### [DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion](https://arxiv.org/abs/2608.20759v1)

- **主题：** 动态与4D
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-21T05:46:52Z
- **更新判定：** 真正新增
- **核心内容：** Single-image 3D human reconstruction often suffers from over-smoothed textures and geometric inconsistencies. While diffusion models improve generative quality, their reliance on multi-view synthesis prior to 3D reconstruction is computationally expensive and prone to view inconsistency. We propose DiGS-Avatar, which reformulates this task as an efficient, diffusion-based UV-latent completion task, ensuring 3D consistency by design. To capture accurate spatial structure, we introduce a teacher-student framework where a multi-view teacher provides geometrically aligned pseudo-ground-truth latents to supervise a single-view diffusion student. Treating this inferred latent as a robust structural skeleton, our method injects high-level semantic features to accurately recover fine textural details without disrupting spatial integrity. The refined representation is then decoded into 3D Gaussian primitives. Extensive experiments demonstrate that DiGS-Avatar achieves state-of-the-art or highl…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.20759v1

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@ee94d1508efbfc4464ec1b14658606684baf6052/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/3f63aba028c899d0725b3b07349d897284f412ac)

- **主题：** 动态与4D
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:19:32Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@ee94d1508efbfc4464ec1b14658606684baf6052/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [pawel002/4dgs](https://github.com/pawel002/4dgs)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T21:30:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementation of my Master's Thesis: Temporal Gaussian Splatting (a.k.a. 4DGS)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pawel002/4dgs

### [solipsist-studios/cumuli](https://github.com/solipsist-studios/cumuli)

- **主题：** 动态与4D
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T17:18:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 4D volumetric human capture pipeline: GoPro footage → Camera pose estimation → Diffuman4D → Brush 3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于动态场景、Avatar、时序重建或可编辑运动表示预研。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/solipsist-studios/cumuli

### [GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2608.17535v1)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T08:55:52Z
- **更新判定：** 真正新增
- **核心内容：** Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phrase-based semantic queries. To this end, we propose GroupForward, an instance-grouped feed-forward Gaussian splatting model that reconstructs geometry, appearance, instance structure, and semantics from sparse, unposed, and uncalibrated multi-view images. Unlike existing methods that attach high-dimensional semantic features to each Gaussian, GroupForward learns compact instance embeddings that group Gaussians into cross-view consistent 3D instances, reformulating feed-forward semantic 3DGS from per-Gaussian semantic feature rendering to instance-level semantic aggregation and propagation. Building on these instance groups, we further…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.17535v1

### [OccamView: Object-Conditioned View Selection for Frame-Budgeted Active 3D Gaussian Reconstruction](https://arxiv.org/abs/2608.16499v1)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T12:38:56Z
- **更新判定：** 真正新增
- **核心内容：** Active 3D Gaussian reconstruction fundamentally relies on selecting informative next-best views under limited sensing budgets. Existing active 3DGS methods primarily plan viewpoints according to geometric information gain, treating object-induced hidden regions in the same manner as general unexplored space. Under tight frame budgets, such geometry-driven strategies may prioritize global scene coverage while leaving partially observed objects incompletely reconstructed. To address this limitation, we propose OccamView, an object-conditioned view-selection framework for frame-budgeted active 3D Gaussian reconstruction. Rather than predicting unseen object geometry or performing shape completion, OccamView maintains an online object memory from open-vocabulary detections grounded in measured RGB-D observations and represents unresolved local occupancy around detected objects as conservative hidden-region proxies. Candidate viewpoints are then evaluated using an occlusion-aware proxy-cov…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16499v1

### [TR-GS: High-Fidelity Sparse-View CT Volumetric Rendering via t-Distribution Gaussian Splatting and Ray-Confidence Modeling](https://arxiv.org/abs/2608.16042v1)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T03:11:28Z
- **更新判定：** 真正新增
- **核心内容：** High-fidelity 3D medical visualization supports applications such as clinical assessment and surgical planning. Sparse-view computed tomography (CT) can reduce projection requirements and associated radiation exposure, but limited observations may introduce structural artifacts and reconstruction uncertainty. Although 3D Gaussian Splatting (3DGS) provides an efficient explicit representation for volumetric rendering, existing CT methods based on standard Gaussian primitives may be sensitive to unreliable observations under sparse-view acquisition. We present TR-GS, a Gaussian-splatting framework for sparse view CT volumetric rendering. TR-GS replaces standard Gaussian primitives with projectable Student's t-distribution primitives and introduces a ray-confidence model that regulates their degrees of freedom according to local ray observability. Confidence-guided 3D wavelet regularization is further used to balance high-frequency detail preservation and noise suppression. This work is…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16042v1

### [ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting](https://arxiv.org/abs/2509.22225v3)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-22T09:14:10Z
- **更新判定：** 实质修订
- **核心内容：** Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge. Mainstream methods, built on an embedding paradigm, suffer from three key flaws: (i) geometry-semantic inconsistency, where points, rather than objects, serve as the semantic basis, limiting semantic fidelity; (ii) semantic bloat from injecting gigabytes of feature data into the geometry; and (iii) semantic rigidity, as one feature per Gaussian struggles to capture rich polysemy. To overcome these limitations, we introduce ExtrinSplat, a framework built on the extrinsic paradigm that decouples geometry from semantics. Instead of embedding features, ExtrinSplat clusters Gaussians into multi-granularity, overlapping 3D object groups. A Vision-Language Model (VLM) then interprets these groups to generate lightweight textual hypotheses, creating an extrinsic index layer that natively supports complex polysemy. By replacing costly feature embedding with lightweight indices, ExtrinSpla…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2509.22225v3

### [Use uploadU32DataTextureRows for LoD index uploads (#406) updateLodIndices duplicated the texSubImage2D path inline instead of calling the existing helper, and the inline copy did not save and restore the pixelStorei parameters. Leaving UNPACK_FLIP_Y_WEBGL at false desynchronises three.js's WebGLState cache: the cache still believes the value is true, so three skips the pixelStorei call before its own uploads and every subsequent texture is transferred flipped. uploadU32DataTextureRows already handles this. Fixes #405](https://github.com/sparkjsdev/spark/commit/ae19a64871133db5d9683aafe52d4e1f08bdd592)

- **主题：** 压缩与轻量化
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-25T22:30:28Z
- **更新判定：** 代码实质更新
- **核心内容：** Use uploadU32DataTextureRows for LoD index uploads (#406) updateLodIndices duplicated the texSubImage2D path inline instead of calling the existing helper, and the inline copy did not save and restore the pixelStorei parameters. Leaving UNPACK_FLIP_Y_WEBGL at false desynchronises three.js's WebGLState cache: the cache still believes the value is true, so three skips the pixelStorei call before its own uploads and every subsequent texture is transferred flipped. uploadU32DataTextureRows already handles this. Fixes #405
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [zqlin0521/GS4Buildings](https://github.com/zqlin0521/GS4Buildings)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:11:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Prior-guided Gaussian Splatting framework for robust and complete 3D building reconstruction using LoD2 semantic models.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zqlin0521/GS4Buildings

### [pengpeng-yu/CodecSplat](https://github.com/pengpeng-yu/CodecSplat)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T21:00:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Ultra-compact latent coding for feed-forward 3D Gaussian splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/pengpeng-yu/CodecSplat

### [orangewk/wigner-splat](https://github.com/orangewk/wigner-splat)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T14:51:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian splatting meets quantum optics: signed 3DGS-style splats and physical Gaussian-ket mixtures fitted to homodyne data for quantum state tomography -- with a complete, honest research log.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/orangewk/wigner-splat

### [WilliamLiu-1997/Gaussian-Splat-Lite](https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T13:49:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A lightweight Three.js Gaussian Splatting renderer with WebAssembly-accelerated sorting and raycasting, multi-Splat rendering, and high-precision GIS/ECEF coordinate support.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite

### [Simo264/gs-texture-compression](https://github.com/Simo264/gs-texture-compression)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T15:28:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting for texture compression
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Simo264/gs-texture-compression

### [SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis](https://arxiv.org/abs/2608.16863v1)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-17T17:45:57Z
- **更新判定：** 真正新增
- **核心内容：** Generating photorealistic novel views from unposed images requires both 3D geometric understanding and the ability to synthesize unseen content. A natural strategy combines feed-forward 3DGS reconstruction with multi-view diffusion. Yet prior pipelines extract at most one signal from the reconstruction, either pixel rendering or learned features, while none exploits per-Gaussian visibility for occlusion-aware reference selection. This *information disconnect* leaves renderable geometry, visibility cues, and learned features unused. SplatGuide closes this disconnect by reusing a single 3DGS scene across three complementary roles. Rendered images provide pixel-aligned geometric conditioning. Per-Gaussian source-view indices are rendered into a target-view voting map for occlusion-aware reference selection. Reconstruction tokens supply feature-level guidance via cross-attention. All three signals derive from the same reconstruction forward pass. Across RealEstate10K, DL3DV, Tanks-and-Tem…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.16863v1

### [Bump workspace version to 1.0.0 (#518) Fixes #515. The CLI surface changed incompatibly since v0.3.0 but the binary still reported 0.3.0, so wrappers had no way to detect which behavior they were talking to.](https://github.com/ArthurBrussee/brush/commit/fa5fd57f19cb21b2867508187b744a306c0b22d6)

- **主题：** 几何/材质/光照
- **来源：** GitHub · ArthurBrussee/brush
- **发布时间/更新时间：** 2026-08-15T09:32:05Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump workspace version to 1.0.0 (#518) Fixes #515. The CLI surface changed incompatibly since v0.3.0 but the binary still reported 0.3.0, so wrappers had no way to detect which behavior they were talking to.
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/ArthurBrussee/brush

### [Pass fileType to SplatPager when constructing SplatMesh (#365)](https://github.com/sparkjsdev/spark/commit/b4817a6b6a5c9ceadaf69efa17def0b0f1cf4dff)

- **主题：** 几何/材质/光照
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:21:27Z
- **更新判定：** 代码实质更新
- **核心内容：** Pass fileType to SplatPager when constructing SplatMesh (#365)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Handle preUpdate ahead of updating material uniforms to avoid 1 frame latency (#391)](https://github.com/sparkjsdev/spark/commit/c244e02bfb3e394465ddd374618624838f1da38a)

- **主题：** 几何/材质/光照
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:19:55Z
- **更新判定：** 代码实质更新
- **核心内容：** Handle preUpdate ahead of updating material uniforms to avoid 1 frame latency (#391)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [manycoretech/aholo-spatial-sdk](https://github.com/manycoretech/aholo-spatial-sdk)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T11:58:55Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SDK for the Aholo API — 3DGS reconstruction, generation, cloud rendering, and material/model creation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/manycoretech/aholo-spatial-sdk

### [MasonAndrewHarrison/SDF-Raymarching-Engine](https://github.com/MasonAndrewHarrison/SDF-Raymarching-Engine)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:45:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This is a demo of a Caustic Gaussian which is a modification of a Gaussian Splat.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/MasonAndrewHarrison/SDF-Raymarching-Engine

### [ml-matthew-lam/relightable-3dgs](https://github.com/ml-matthew-lam/relightable-3dgs)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T22:46:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ml-matthew-lam/relightable-3dgs

### [DesignAgent3D: Interactive 3D Scene Editing via Designer-like Multimodal Reasoning](https://arxiv.org/abs/2608.21438v1)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-18T01:16:13Z
- **更新判定：** 真正新增
- **核心内容：** Text guided 3D scene editing provides an intuitive interface for modifying reconstructed environments, but remains difficult because natural language design requests are often semantically underspecified and must be grounded in cluttered 3D scenes. Existing methods typically formulate the task as one-shot conditional generation from a single prompt, failing to resolve ambiguous user intents or achieve precise spatial grounding. Consequently, they suffer from severe object localization drift, tracking failure under occlusions, and the notorious multi-view "sticker effect." To overcome these limitations, we present DesignAgent3D, an interactive multimodal agentic framework that reformulates 3D scene editing as a designer-like Plan-Perceive-Act paradigm. The agent first plans by interacting with the user to clarify underspecified design goals, then perceives by grounding the intended edit to specific objects or regions in the 3D scene, and finally acts by applying controlled visual modif…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.21438v1

### [In-Situ Reconstruction of the International Space Station Using 3D Gaussian Splatting and Astrobee](https://arxiv.org/abs/2608.21685v1)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-21T23:20:16Z
- **更新判定：** 真正新增
- **核心内容：** This article presents a novel 3D reconstruction and mapping of the interior of the International Space Station (ISS) using 3D Gaussian Splatting (3DGS). Using existing grayscale images from the Astrobee free-flying robot dataset, we construct a full 3D splat of the ISS' Kibō or Japanese Experiment Module (JEM). 3DGS has in recent years shown promise in providing novel view synthesis of scenes captured from many images or videos, this article applies this approach to human spaceflight systems. We compare our 3DGS architecture to existing methods such as Nerfacto and TensoRF and show that reconstruction improves the state-of-the-art in both scene quality and rendering speed. We show that with as little as 500 in-situ images, a high-fidelity map can be constructed using Astrobee's Navigation Camera (NavCam) during free-flight in the JEM. These reconstructions could enable free-flyers to rapidly create and update interior maps for intra-vehicular habitats like the ISS.
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.21685v1

### [GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2608.14986v1)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-15T02:28:59Z
- **更新判定：** 真正新增
- **核心内容：** Long-horizon robotic manipulation fundamentally relies on persistent spatial memory. However, existing 3D memory systems function merely as passive recorders: they store observations using fixed, hand-crafted rules, treating every scene element--whether a critical grasp target or an irrelevant background wall--with equal importance. In this paper, we propose a paradigm shift from passive storage to active, task-driven spatial memory. We argue that a robot's memory should not simply record what it sees, but actively learn how to remember--discovering which objects to track precisely, how aggressively to update them, and what to discard, all learned end-to-end without hand-designed rules. Crucially, this active paradigm is realized by unifying memory update and readout as two sides of the same cognitive process, enabling bidirectional flow where task needs shape update strategies and vice versa. To instantiate this vision, we introduce GaussMemory, which leverages 3D Gaussian Splatting…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.14986v1

### [ProbSplat: Efficient Probabilistic Hardware for Gaussian Splatting in 3D Scene Reconstruction](https://arxiv.org/abs/2608.13143v1)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-13T12:16:37Z
- **更新判定：** 真正新增
- **核心内容：** This paper presents ProbSplat, a Compute-in-Memory (CIM)-inspired architecture based on programmable and energy efficient floating-gate inverter columns for probabilistic computing. Improving upon our prior work, ProbSplat programs and stores both means and variances of Gaussian mixture components, and evaluates log-likelihood for gaussian splatting during scene reconstruction with high energy efficiency, suitable for robotics and augmented/virtual reality (AR/VR) at the edge. Our proposed scheme enables independent control of both mean and variance via deterministic adjustment of floating-gate MOSFET threshold voltages, increasing the fidelity of hardware to program probability distributions. The design is simulated in 180nm CMOS on 1.8 V at 50 MHz and achieves mean-variance independence with <2.4% deviation during 3-D Gaussian mixture modeling. Compared to conventional digital implementations, ProbSplat significantly reduces compute complexity, memory footprint, and power consumptio…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.13143v1

### [DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416v4)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-21T07:17:11Z
- **更新判定：** 实质修订
- **核心内容：** Advances in radiance fields have enabled photorealistic novel view synthesis. In several domains, large-scale real-world datasets have been developed to support comprehensive benchmarking and to facilitate progress beyond scene-specific reconstruction. However, for distractor-free radiance fields, a large-scale dataset with clean and cluttered images per scene remains lacking, limiting the development. To address this gap, we introduce DF3DV-1K, a large-scale real-world dataset comprising 1,048 scenes, each providing clean and cluttered image sets for benchmarking. In total, the dataset contains 89,924 images captured using consumer cameras to mimic casual capture, spanning 128 distractor types and 161 scene themes across indoor and outdoor environments. A curated subset of 41 scenes, DF3DV-41, is systematically designed to evaluate the robustness of distractor-free radiance field methods under challenging scenarios. Using DF3DV-1K, we benchmark nine recent distractor-free radiance fi…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2604.13416v4

### [SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v2)

- **主题：** SLAM与重建
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-21T07:30:56Z
- **更新判定：** 实质修订
- **核心内容：** Pixel-aligned Gaussian splatting enables efficient and generalizable novel-view synthesis. However, high-resolution rendering faces a critical trade-off where increasing input resolution improves detail at the expense of quadratically rising network computational cost. Conversely, maintaining low-resolution inputs stabilizes this cost but results in insufficient Gaussian density and artifacts. To address this, we propose SubSplat, which introduces Sub-pixel Gaussian Reparameterizer(SPGR) to subdivide primary Gaussians into fine-grained primitives, restoring structural density directly from low-resolution features. We further enhance the reparameterization quality through feature aggregation, which effectively captures high-frequency details across multiple views. Experiments on RealEstate10K and ACID demonstrate that SubSplat achieves high-fidelity rendering with superior efficiency. Our results validate that the proposed framework successfully resolves the trade-off between reparamet…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2607.20813v2

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T17:07:15Z
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
- **发布时间/更新时间：** 2026-08-25T07:20:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A comprehensive list of Implicit Representations, NeRF and 3D Gaussian Splatting papers relating to SLAM/Robotics domain, including papers, videos, codes, and related websites
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM

### [darshmenon/rosnav](https://github.com/darshmenon/rosnav)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:37:05Z
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
- **发布时间/更新时间：** 2026-08-26T02:14:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T00:32:08Z
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
- **发布时间/更新时间：** 2026-08-25T23:41:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [Tirzst5779/ML-Sharp-QNN](https://github.com/Tirzst5779/ML-Sharp-QNN)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T19:37:38Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Run Apple's SHARP 3D Gaussian Splatting on Android via Qualcomm QNN HTP for instant, offline single-image 3D reconstruction on Snapdragon devices.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Tirzst5779/ML-Sharp-QNN

### [yagnasanhitjatangula-tech/spaltforge-360](https://github.com/yagnasanhitjatangula-tech/spaltforge-360)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T18:06:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** SplatForge — AI-powered 3D spatial reconstruction pipeline that converts video captures into interactive Gaussian Splat environments with real-time processing, live pipeline monitoring, and Unity-ready exports.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yagnasanhitjatangula-tech/spaltforge-360

### [emr81-ua/3d-gaussian-splatting-reconstruction](https://github.com/emr81-ua/3d-gaussian-splatting-reconstruction)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:28:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** One-command pipeline: from a set of photos to a real-time 3D model (COLMAP + 3D Gaussian Splatting). Bachelor's thesis project.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/emr81-ua/3d-gaussian-splatting-reconstruction

### [LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2608.12825v1)

- **主题：** 少视角与前馈
- **来源：** arXiv
- **发布时间/更新时间：** 2026-08-13T04:59:36Z
- **更新判定：** 真正新增
- **核心内容：** Recent query-based feed-forward 3DGS methods represent a scene using learnable queries, each aggregating multi-view evidence and decoding a group of Gaussians. Ideally, different queries should specialize in coherent local regions of the scene. However, we observe that Gaussians decoded from the same query often scatter across distant scene regions, resulting in weak query-level spatial coherence and poor alignment with the scene structure. We attribute this behavior to the purely latent representation of existing Gaussian queries. To address this limitation, we introduce LocusGS, which augments each Gaussian query with a 3D anchor state consisting of a center and a support radius. The anchor state is progressively refined across decoder layers and is used throughout query interaction, multi-view feature aggregation, and Gaussian generation. Specifically, an anchor-to-ray geometric bias guides each query toward spatially relevant image observations, while anchor-centered decoding orga…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2608.12825v1

### [OffTheGridGS/OffTheGrid](https://github.com/OffTheGridGS/OffTheGrid)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T17:28:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementation of the CVPR 2026 paper: "Off The Grid: Detection of Primitives for Feed-Forward Gaussian Splatting"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/OffTheGridGS/OffTheGrid

### [RitujaPawas/sparse-view-3dgs](https://github.com/RitujaPawas/sparse-view-3dgs)

- **主题：** 少视角与前馈
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T20:57:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Sparse view 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合减少采集成本、缩短建模周期或探索前馈式重建。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/RitujaPawas/sparse-view-3dgs

### [heshuting555/Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T08:15:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 【TPAMI 2026】A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/heshuting555/Awesome-3DGS-Applications

### [playcanvas/supersplat v2.32.5](https://github.com/playcanvas/supersplat/releases/tag/v2.32.5)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T13:27:50Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Update all npm dependencies by @renovate[bot] in https://github.com/playcanvas/supersplat/pull/1010 * Viewer export looping mode by @slimbuck in https://github.com/playcanvas/supersplat/pull/1011 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v2.32.4...v2.32.5
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [playcanvas/supersplat v2.32.4](https://github.com/playcanvas/supersplat/releases/tag/v2.32.4)

- **主题：** 实时渲染与展示
- **来源：** GitHub Release · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T10:31:25Z
- **更新判定：** 正式版本发布
- **核心内容：** ## What's Changed * Update all npm dependencies by @renovate[bot] in https://github.com/playcanvas/supersplat/pull/1008 * Use shared viewer settings from splat-transform's viewer-settings subpath by @slimbuck in https://github.com/playcanvas/supersplat/pull/1009 **Full Changelog**: https://github.com/playcanvas/supersplat/compare/v2.32.3...v2.32.4
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [feat(cameras): support FTheta FOV beyond 180 degrees: FTheta cameras with max_angle > pi/2 model more than 180 degrees of FOV, but forward projection previously rejected every ray with z <= 0. Remove that guard and determine validity from theta_full < max_angle and the image-bounds margin check. For max_angle <= pi/2, the validity flag remains unchanged. However, invalid rays now return their cone-clamped rim projection instead of the (0, 0) sentinel. Because the unscented transform includes invalid sigma points when require_all_sigma_points_valid is false, Gaussians straddling the camera plane now produce a more representative 2D footprint. Limit Euclidean near/far culling to LiDAR and FTheta, whose projection models accept rays with z <= 0. Pinhole, orthographic, and fisheye models retain camera-space z culling when global_z_order is false. Rendering the beyond-180-degree FTheta band requires global_z_order=false throughout the pipeline. This also uses Euclidean distance for depth sorting and the D/ED depth channel.](https://github.com/nerfstudio-project/gsplat/commit/96f18e762a6609e5ea80bf67f0501a08427511b5)

- **主题：** 实时渲染与展示
- **来源：** GitHub · nerfstudio-project/gsplat
- **发布时间/更新时间：** 2026-08-18T16:51:06Z
- **更新判定：** 代码实质更新
- **核心内容：** feat(cameras): support FTheta FOV beyond 180 degrees: FTheta cameras with max_angle > pi/2 model more than 180 degrees of FOV, but forward projection previously rejected every ray with z <= 0. Remove that guard and determine validity from theta_full < max_angle and the image-bounds margin check. For max_angle <= pi/2, the validity flag remains unchanged. However, invalid rays now return their cone-clamped rim projection instead of the (0, 0) sentinel. Because the unscented transform includes invalid sigma points when require_all_sigma_points_valid is false, Gaussians straddling the camera plane now produce a more representative 2D footprint. Limit Euclidean near/far culling to LiDAR and FTheta, whose projection models accept rays with z <= 0. Pinhole, orthographic, and fisheye models retain camera-space z culling when global_z_order is false. Rendering the beyond-180-degree FTheta band requires global_z_order=false throughout the pipeline. This also uses Euclidean distance for depth s…
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/nerfstudio-project/gsplat

### [playcanvas/engine](https://github.com/playcanvas/engine)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:35:34Z
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
- **发布时间/更新时间：** 2026-08-26T00:39:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository tracks the latest advancements in 3D Gaussian Splatting from Arxiv, with daily automated updates. Stay up-to-date with cutting-edge research in this exciting field!
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/longxiang-ai/awesome-gaussians

### [playcanvas/splat-transform](https://github.com/playcanvas/splat-transform)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T13:18:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** CLI tool and library for 3D Gaussian splat processing and conversion
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/playcanvas/splat-transform

### [ReconWorldLab/godot-gaussian-splatting](https://github.com/ReconWorldLab/godot-gaussian-splatting)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:04:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [GDGS] A real-time 3D Gaussian Splatting (3DGS) rendering plugin for the Godot Engine. Godot引擎的实时3DGS渲染插件
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ReconWorldLab/godot-gaussian-splatting

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@33a90507920b092d3cbade409c3e3b34f05ebdde/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/1be70d14e81db120f266371e6c84cdd46f158291)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-25T22:33:38Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@33a90507920b092d3cbade409c3e3b34f05ebdde/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Clamp splat RGB to positive in splatVertex, matching the reference rasterizer (#387) * Sanitize splat rgba when packing ExtSplats to match PackedSplats clamping * Move the clamp to splatVertex and only clamp RGB to positive](https://github.com/sparkjsdev/spark/commit/e01ae568934e98db1ebac8729f2c1e0c54281a4f)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-25T22:29:09Z
- **更新判定：** 代码实质更新
- **核心内容：** Clamp splat RGB to positive in splatVertex, matching the reference rasterizer (#387) * Sanitize splat rgba when packing ExtSplats to match PackedSplats clamping * Move the clamp to splatVertex and only clamp RGB to positive
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Viewer export looping mode (#1011)](https://github.com/playcanvas/supersplat/commit/ec1d623e9b2b7203d2ab6e8b5c9362d4c4bf45b8)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T13:26:18Z
- **更新判定：** 代码实质更新
- **核心内容：** Viewer export looping mode (#1011)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Use shared viewer settings from splat-transform's viewer-settings subpath (#1009)](https://github.com/playcanvas/supersplat/commit/926fc0b1bbc99c5755a3b88896d758747d018dfe)

- **主题：** 实时渲染与展示
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T10:00:03Z
- **更新判定：** 代码实质更新
- **核心内容：** Use shared viewer settings from splat-transform's viewer-settings subpath (#1009)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@0aad4249990ba18f94750b43535a502c4e0d87af/dist/spark.module.js)](https://github.com/sparkjsdev/spark/commit/6a254a241ac2eb0d11edb1bad69d3680e3ebc3e8)

- **主题：** 实时渲染与展示
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:24:37Z
- **更新判定：** 代码实质更新
- **核心内容：** Update main CDN URL. (https://cdn.jsdelivr.net/gh/sparkjsdev/spark@0aad4249990ba18f94750b43535a502c4e0d87af/dist/spark.module.js)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [zcq15/gsplat360](https://github.com/zcq15/gsplat360)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T02:54:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A gsplat-based rasterization designed for panoramic cameras, with support for 360-degree rendering for both 3DGS and 2DGS.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/zcq15/gsplat360

### [invitro-dampproofcourse822/TripoSplat](https://github.com/invitro-dampproofcourse822/TripoSplat)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T04:01:16Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Generate high-quality 3D Gaussians from a single 2D image for asset creation, AR, VR, and game development.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/invitro-dampproofcourse822/TripoSplat

### [Voluma-ai/vlam](https://github.com/Voluma-ai/vlam)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T09:54:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VLAM! - A WebGPU Gaussian Splat viewer for three.js
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Voluma-ai/vlam

### [uav4geo/Splat-Tools](https://github.com/uav4geo/Splat-Tools)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T21:11:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Convert 3DGS scenes to RAD for use with WebODM 🔨
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/uav4geo/Splat-Tools

### [kamyy/ai-gaussian-splatter](https://github.com/kamyy/ai-gaussian-splatter)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T00:54:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Upload multi-angle photos of a physical object, get back a real-time 3D Gaussian Splat viewable and shareable in-browser
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kamyy/ai-gaussian-splatter

### [ZhiyeTang/ProGS-Official](https://github.com/ZhiyeTang/ProGS-Official)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T15:36:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The official implementation of paper "ProGS: Towards Progressive Coding for 3D Gaussian Splatting"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhiyeTang/ProGS-Official

### [NickAcPT/vrchat-3d-capture](https://github.com/NickAcPT/vrchat-3d-capture)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T00:34:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An assortment of random bits and pieces that I use on my gaussian splatting workflow for VRChat.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NickAcPT/vrchat-3d-capture

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:54:25Z
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
- **发布时间/更新时间：** 2026-08-26T02:41:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Research portfolio — certified/calibrated ML systems: 3DGS confidence (AURA), splat registration (splatreg), certified planning (CERT-FLOW), diffusion caching (HiCache++), robot action-interface adaptation (ActionShift/ActionABI)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Archerkattri/Archerkattri

### [ilhamhakm/360-to-3DGS-on-ARM64](https://github.com/ilhamhakm/360-to-3DGS-on-ARM64)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:31:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** If you need to do photogrammetry on a ARM64(aarch64) environment. Given you took the videos on a drone with a 360 camera (Antigravity A1) and want a photorealistic 3d output.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ilhamhakm/360-to-3DGS-on-ARM64

### [mogmog-0110/gs-proxy-toon](https://github.com/mogmog-0110/gs-proxy-toon)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T02:23:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Cel shading on 3D Gaussian Splatting - separating the shading shape from appearance, with band-stability metrics
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mogmog-0110/gs-proxy-toon

### [frtkng/mini-3dgs](https://github.com/frtkng/mini-3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T21:42:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Educational minimal 3D Gaussian Splatting renderer (NumPy, CPU-only)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frtkng/mini-3dgs

### [Jingnan-Econ/quad](https://github.com/Jingnan-Econ/quad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T20:48:29Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The Illinois main quad rebuilt from public lidar, as a browsable gaussian splat
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Jingnan-Econ/quad

### [TangXu-Group/S2-GS](https://github.com/TangXu-Group/S2-GS)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T17:29:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Structure-Spreading Gaussian Splatting for Sparse Aerial Novel View Synthesis
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/TangXu-Group/S2-GS

### [8192K/master_seminar_3dgs](https://github.com/8192K/master_seminar_3dgs)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T17:08:28Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Master Seminar on 3D Gaussian Splatting during my Master's in Data Science at Fernuni Hagen
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/8192K/master_seminar_3dgs

### [mogmog-0110/realtime-gaussian-splatting](https://github.com/mogmog-0110/realtime-gaussian-splatting)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:36:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time 3D Gaussian Splatting viewer (DirectX 12) — MitiruEngine tech demo
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mogmog-0110/realtime-gaussian-splatting

### [iyamon-bbcf/render-splat-export](https://github.com/iyamon-bbcf/render-splat-export)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:25:01Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D render to Gaussian splat skip camera guessing
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/iyamon-bbcf/render-splat-export

### [GamageShakthi/NeRF-and-3DGS-From-Scratch](https://github.com/GamageShakthi/NeRF-and-3DGS-From-Scratch)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T13:54:23Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementing Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) from first principles in PyTorch, covering volumetric rendering, ray marching, and differentiable rasterization. (Ongoing))
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/GamageShakthi/NeRF-and-3DGS-From-Scratch

### [VISjudy/3dgs-paper-workbench](https://github.com/VISjudy/3dgs-paper-workbench)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T13:24:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** lidar-img-3DGS 论文 Review 工作台 (WorkBuddy 资料库配套)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/VISjudy/3dgs-paper-workbench

### [ecoartic/3dgs-pro-viewer](https://github.com/ecoartic/3dgs-pro-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T12:57:31Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ecoartic/3dgs-pro-viewer

### [CharlesJune/3dgs-ws](https://huggingface.co/CharlesJune/3dgs-ws)

- **主题：** 实时渲染与展示
- **来源：** Hugging Face 模型
- **发布时间/更新时间：** 2026-08-18T04:02:47Z
- **更新判定：** 模型更新
- **核心内容：** 近期更新的模型；标签：region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

### [rayanht/msplat](https://github.com/rayanht/msplat)

- **主题：** GPU与加速实现
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T23:34:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Metal-accelerated 3D Gaussian Splatting for Apple Silicon
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合在现有训练或渲染链路中直接做内核级基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/rayanht/msplat

### [yennster/synthetic-data-studio-playcanvas](https://github.com/yennster/synthetic-data-studio-playcanvas)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T14:37:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Synthetic Data Studio rebuilt on PlayCanvas with gaussian splat import & in-app creation for hyper-realistic synthetic data
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yennster/synthetic-data-studio-playcanvas

### [yang498-Peter/cloudstudio-3dgs](https://github.com/yang498-Peter/cloudstudio-3dgs)

- **主题：** 工业产品与平台
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-26T00:54:10Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Open-source 3D Gaussian Splatting pipeline for MVP S1 scan data
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于判断产品集成、交互体验和商业化成熟度。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yang498-Peter/cloudstudio-3dgs

### [[NV] Support FTheta FOV beyond 180 degrees (#1050) Added support for FTheta camera FOVs > 180 degrees](https://github.com/nerfstudio-project/gsplat/commit/90d7b4b349e379ccf9ee6a8cef76aa40f48bb32e)

- **主题：** 其他
- **来源：** GitHub · nerfstudio-project/gsplat
- **发布时间/更新时间：** 2026-08-20T20:42:33Z
- **更新判定：** 代码实质更新
- **核心内容：** [NV] Support FTheta FOV beyond 180 degrees (#1050) Added support for FTheta camera FOVs > 180 degrees
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/nerfstudio-project/gsplat

### [hbb1/2d-gaussian-splatting](https://github.com/hbb1/2d-gaussian-splatting)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T18:36:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** [SIGGRAPH'24] 2D Gaussian Splatting for Geometrically Accurate Radiance Fields
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/hbb1/2d-gaussian-splatting

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/33a90507920b092d3cbade409c3e3b34f05ebdde)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-25T22:33:38Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [2.32.5](https://github.com/playcanvas/supersplat/commit/e060989b202548848eb440a5005cd41a8b26f7db)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T13:27:25Z
- **更新判定：** 代码实质更新
- **核心内容：** 2.32.5
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [2.32.4](https://github.com/playcanvas/supersplat/commit/3886caaf3b9f049337aa58d83933c3bcc5f2fea7)

- **主题：** 其他
- **来源：** GitHub · playcanvas/supersplat
- **发布时间/更新时间：** 2026-08-25T10:22:22Z
- **更新判定：** 代码实质更新
- **核心内容：** 2.32.4
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/playcanvas/supersplat

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/0aad4249990ba18f94750b43535a502c4e0d87af)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:24:37Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Remove JS based splat file format decoders (#374) * Remove JS based splat file format decoders * Introduce writeSpz function to replace SpzWriter for splat-painter example](https://github.com/sparkjsdev/spark/commit/8a409c435b6c6a5a7cb518e8fd5574cf6cb2220f)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:20:46Z
- **更新判定：** 代码实质更新
- **核心内容：** Remove JS based splat file format decoders (#374) * Remove JS based splat file format decoders * Introduce writeSpz function to replace SpzWriter for splat-painter example
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Bump dist build](https://github.com/sparkjsdev/spark/commit/ee94d1508efbfc4464ec1b14658606684baf6052)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:19:32Z
- **更新判定：** 代码实质更新
- **核心内容：** Bump dist build
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Introduce AbortController in PagedSplats to abort ongoing fetches (#392)](https://github.com/sparkjsdev/spark/commit/ec209eab3e19d44759cf7fe37b8eaff19bd0aa80)

- **主题：** 其他
- **来源：** GitHub · sparkjsdev/spark
- **发布时间/更新时间：** 2026-08-24T16:16:20Z
- **更新判定：** 代码实质更新
- **核心内容：** Introduce AbortController in PagedSplats to abort ongoing fetches (#392)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/sparkjsdev/spark

### [Update v1.6.0 news](https://github.com/nerfstudio-project/gsplat/commit/1bfbe34480152f0bd0b761acf29ffaf0e4fc13a0)

- **主题：** 其他
- **来源：** GitHub · nerfstudio-project/gsplat
- **发布时间/更新时间：** 2026-08-14T19:22:04Z
- **更新判定：** 代码实质更新
- **核心内容：** Update v1.6.0 news
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/nerfstudio-project/gsplat

### [JaminYan/SplatMod-Video2Splat](https://github.com/JaminYan/SplatMod-Video2Splat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T15:34:17Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ConvertVideo to 3DSplat (3D Gaussian Splatting）with High performance and High quality
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JaminYan/SplatMod-Video2Splat

### [Functionhx/DecoupleGS](https://github.com/Functionhx/DecoupleGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T04:39:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Unofficial independent reimplementation of DecoupleGS (ECCV 2026) on HUGSIM for interactive 3DGS autonomous-driving simulation.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Functionhx/DecoupleGS

### [ZhaoRunRunRun/3dgs-tracker](https://github.com/ZhaoRunRunRun/3dgs-tracker)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T03:47:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [potato-bug/street-view-to-3dgs](https://huggingface.co/spaces/potato-bug/street-view-to-3dgs)

- **主题：** 其他
- **来源：** Hugging Face 交互演示
- **发布时间/更新时间：** 2026-08-24T04:41:49Z
- **更新判定：** 交互演示更新
- **核心内容：** 近期更新的交互演示；标签：gradio, region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

### [kurokaj/realestate-splat](https://github.com/kurokaj/realestate-splat)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T18:11:02Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Gaussian Splatting pipeline for real-estate use
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/kurokaj/realestate-splat

### [frtkng/mini-3dgs-connectivity-probe](https://github.com/frtkng/mini-3dgs-connectivity-probe)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T16:53:00Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/frtkng/mini-3dgs-connectivity-probe

### [elbuho12Jesus/2d-gaussian-splatting-modificate](https://github.com/elbuho12Jesus/2d-gaussian-splatting-modificate)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T12:44:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Add beta splatting into 2D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/elbuho12Jesus/2d-gaussian-splatting-modificate

### [Astroite/3DGS-AncientBuilding](https://github.com/Astroite/3DGS-AncientBuilding)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T11:39:24Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Astroite/3DGS-AncientBuilding

### [3DGS-Rebuild-NIR/3DGSFullProcessApp](https://github.com/3DGS-Rebuild-NIR/3DGSFullProcessApp)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T11:10:34Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** IR 强化 3DGS 全链路重建系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/3DGS-Rebuild-NIR/3DGSFullProcessApp

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T11:04:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [cnhaox/3DGS-HPC](https://github.com/cnhaox/3DGS-HPC)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T10:37:57Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementation of the ICML 2026 paper "3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification"
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/cnhaox/3DGS-HPC

### [sh1027/3dgs-tutorial](https://github.com/sh1027/3dgs-tutorial)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T05:27:26Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sh1027/3dgs-tutorial

### [legededaduzi/3dgs-with--LIVO](https://github.com/legededaduzi/3dgs-with--LIVO)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-25T02:04:12Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/legededaduzi/3dgs-with--LIVO

### [Jaanuszek/3DGS](https://github.com/Jaanuszek/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T21:09:05Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Implementation of 3D Gaussian Splatting.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Jaanuszek/3DGS

### [blacktheon/Track3DGS](https://github.com/blacktheon/Track3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T15:12:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** The project trying to reproduce the 3DGS environment from 360 video.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/blacktheon/Track3DGS

### [wbxbky/WB-3DGS](https://github.com/wbxbky/WB-3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T13:36:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Official implementation of WB-3DGS
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wbxbky/WB-3DGS

### [QuocKhanhLuong/3DGS](https://github.com/QuocKhanhLuong/3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-08-24T11:57:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/QuocKhanhLuong/3DGS

### [Aeonicc/lhm-3dgs](https://huggingface.co/spaces/Aeonicc/lhm-3dgs)

- **主题：** 其他
- **来源：** Hugging Face 交互演示
- **发布时间/更新时间：** 2026-08-20T18:48:59Z
- **更新判定：** 交互演示更新
- **核心内容：** 近期更新的交互演示；标签：gradio, region:us。
- **成熟度：** E1
- **是否开源：** 以页面许可为准
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 76 |
| GitHub | ok: 95 |
| Hugging Face | ok: 3 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 0 |
| GitHub Models | degraded: HTTPError: HTTP Error 410: Gone |
| 论文原文 | ok: 39/40 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

