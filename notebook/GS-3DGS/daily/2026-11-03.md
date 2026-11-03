---
schema: architectureworld/gs-intelligence/v1
window_start_utc: 2026-11-02T08:42:43Z
window_end_utc: 2026-11-03T08:53:38Z
generated_at_utc: 2026-11-03T08:53:38Z
item_count: 64
---

# Gaussian Splatting（GS/3DGS）技术情报｜2026-11-03

**统计窗口：** 2026-11-02T08:42:43Z — 2026-11-03T08:53:38Z  
**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。

## 执行摘要

本轮保留 **64** 项去重后的有效线索：真正新增论文 **2** 项、实质论文修订 **4** 项、代码/版本/项目更新 **56** 项。
排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。

## 今日最重要的5项更新

| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |
|---:|---|---|---|---|---|
| 1 | [GaussFlaw: Fine-Grained Perceptual Diagnosis for 3D Gaussian Splatting](https://arxiv.org/abs/2611.02767v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 2 | [3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields](https://arxiv.org/abs/2611.03114v1) | 真正新增 | arXiv | R1/E0 | P0 |
| 3 | [Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v4) | 实质修订 | arXiv | R2/E0 | P1 |
| 4 | [Aes3D: Aesthetic Assessment in 3D Gaussian Splatting](https://arxiv.org/abs/2605.05155v5) | 实质修订 | arXiv | R2/E0 | P1 |
| 5 | [EAvatar: Expression-Aware Head Avatar Reconstruction with Generative Geometry Priors](https://arxiv.org/abs/2508.13537v2) | 实质修订 | arXiv | R2/E0 | P1 |

## 分类详述

### [GaussFlaw: Fine-Grained Perceptual Diagnosis for 3D Gaussian Splatting](https://arxiv.org/abs/2611.02767v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T08:46:50Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) enables photorealistic novel- view synthesis with real-time rendering, yet fine-grained di- agnosis of its rendering artifacts remains challenging. These artifacts are typically spatially localized and exhibit diverse degradation patterns, making them difficult to character- ize using global quality metrics and image-level assessment benchmarks, which provide no explicit indication of where they occur or what types of artifacts they represent. To ad- dress this limitation, we introduce GaussFlaw-80K, the first large-scale dataset for fine-grained perceptual diagnosis in 3DGS. Constructed through a model-assisted human-in-the- loop pipeline, GaussFlaw-80K contains 80,049 artifact re- gions across 14,289 rendered images, each annotated with a pixel-level mask and one of eight flaw labels spanning ge- ometric, blending, and photometric degradations. These an- notations turn 3DGS artifact diagnosis into an explicit and measurable task. Building on this dataset…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.02767v1

### [3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields](https://arxiv.org/abs/2611.03114v1)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T13:32:48Z
- **更新判定：** 真正新增
- **核心内容：** 3D Gaussian Splatting (3DGS) has become a vital tool in novel view synthesis. 3D Gaussian functions with attributes like color, opacity, and scale are stacked together to explicitly model a radiance field. However, discrete 3D Gaussians usually produce poor depth with few geometry details but lots of floaters, which hinders the effective modeling of smooth radiance fields. To address this issue, we propose to learn a radiance field within a continuous view-dependent color field parameterized by neural networks. With continuous constraints in color, the bias on low-frequency signals of neural networks can highly encourage the geometry modeling to contribute to high-frequency color variations on images, getting rid of solely relying on the color attribute itself. Moreover, we impose a constraint to improve the Lipschitz continuity of the neural color field, making large changes of each Gaussian's color also match with large changes of its position in terms of a ratio. To this end, we ad…
- **成熟度：** R1/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2611.03114v1

### [EAvatar: Expression-Aware Head Avatar Reconstruction with Generative Geometry Priors](https://arxiv.org/abs/2508.13537v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T11:30:53Z
- **更新判定：** 实质修订
- **核心内容：** High-fidelity head avatar reconstruction plays a crucial role in AR/VR, gaming, and multimedia content creation. Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated effectiveness in modeling complex geometry with real-time rendering capability and are now widely used in high-fidelity head avatar reconstruction tasks. However, existing 3DGS-based methods still face significant challenges in capturing fine-grained facial expressions and preserving local texture continuity, especially in highly deformable regions. To mitigate these limitations, we propose a novel 3DGS-based framework termed EAvatar for head reconstruction that is both expression-aware and deformation-aware. Our method introduces a sparse expression control mechanism, where a small number of key Gaussians are used to influence the deformation of their neighboring Gaussians, enabling accurate modeling of local deformations and fine-scale texture transitions. Furthermore, we leverage high-quality 3D priors fro…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2508.13537v2

### [Octree-Context Gaussian Splatting with Multi-Order Propagation for Channel Knowledge Maps](https://arxiv.org/abs/2605.22961v2)

- **主题：** 训练与优化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T17:10:37Z
- **更新判定：** 实质修订
- **核心内容：** Channel knowledge maps (CKMs) can support environment-aware wireless communications by providing site-specific channel knowledge as a function of the transmitter position, the receiver position or both. Existing Gaussian splatting CKM methods can reduce the high training and inference costs of implicit neural methods yet represent all multipath interactions by one wireless radiance field. We propose octree-context Gaussian splatting (OctCGS), which anchors Gaussian primitives on an octree as virtual scattering nodes and decomposes multi-bounce propagation into orders by the number of node-level interactions along each path. Shared tree attention gives each node local context from neighboring octree cells and room-wide context from ancestor cells at a cost linear in the number of cells, and the order-wise scattering of each node is predicted from this context. The order-wise contributions of the power transported between the nodes are summed in power with a line-of-sight (LoS) term to…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2605.22961v2

### [DrDWatt/fvdb-docker](https://github.com/DrDWatt/fvdb-docker)

- **主题：** 训练与优化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T21:52:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Docker workflow for 3D Gaussian Splatting with fVDB - COLMAP processing, GPU training, rendering, and Omniverse integration
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/DrDWatt/fvdb-docker

### [CoGS: Compositional Dynamic Human-Object Scenes Gaussian Splatting from Monocular Video](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6ae9a122d3d8421baa625c2905b7ca9e&url=https%3a%2f%2fgithub.com%2fjerrinbright%2fCoGS&c=678555598042590161&mkt=en-us)

- **主题：** 训练与优化
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-02T18:12:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** Monocular human-object reconstruction is underconstrained because articulated body motion, rigid object motion, and the static scene share pixels but obey different dynamics. Without component-aware ...
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 适合进入训练速度、显存、收敛稳定性和画质的A/B基准。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [Aes3D: Aesthetic Assessment in 3D Gaussian Splatting](https://arxiv.org/abs/2605.05155v5)

- **主题：** 压缩与轻量化
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T14:12:46Z
- **更新判定：** 实质修订
- **核心内容：** As 3D Gaussian Splatting (3DGS) gains attention in immersive media and digital content creation, assessing the aesthetics of 3D scenes becomes important in helping creators build more visually compelling 3D content. However, existing evaluation methods for 3D scenes primarily emphasize reconstruction fidelity and perceptual realism, largely overlooking higher-level aesthetic attributes such as composition, harmony, and visual appeal. This limitation comes from two key challenges: (1) the absence of general 3DGS datasets with aesthetic annotations, and (2) the intrinsic nature of 3DGS as a low-level primitive representation, which makes it difficult to capture high-level aesthetic features. To address these challenges, we propose Aes3D, the first systematic framework for assessing the aesthetics of 3D neural rendering scenes. Aes3D includes Aesthetic3D, the first dataset dedicated to 3D scene aesthetic assessment, built on our proposed annotation strategy for 3D scene aesthetics. In ad…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2605.05155v5

### [reall3d-com/Reall3dViewer](https://github.com/reall3d-com/Reall3dViewer)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T04:24:13Z
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
- **发布时间/更新时间：** 2026-11-03T04:20:07Z
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
- **发布时间/更新时间：** 2026-11-03T08:35:45Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Utilities to convert HLOD tiled 3D formats (like ptc COPC, 3dgs RAD etc) to OGC-3D-tiles by reusing underlying hierarchy for faster reprocessing - purely translation of hierarchy metadata and underlying geometry)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jo-chemla/3dtiled-to-3dtiles

### [Xget7/splatkit-ios](https://github.com/Xget7/splatkit-ios)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T21:54:06Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Native Metal Gaussian splatting SDK for iOS: Swift view, GPU visibility/radix, experimental LOD and hybrid tiles. MIT source and reproducible XCFramework.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit-ios

### [Shinino07/Neural-network-model-for-3DGS-compression-and-decompression](https://github.com/Shinino07/Neural-network-model-for-3DGS-compression-and-decompression)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:16:09Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** A neural network for compressing & decompressing 3D Gaussian Splatting (3DGS) scenes. 3DGS .ply files are lowkey massive, with SH color coefficients eating most of the bytes. We dig into the data, cut the redundancy and shrink scenes down without the render quality taking an L.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Shinino07/Neural-network-model-for-3DGS-compression-and-decompression

### [Khriis-K/Fidelis](https://github.com/Khriis-K/Fidelis)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T01:22:53Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Multifidelity Reliability Estimation for Vision-Based Planetary Navigation: estimating the probability of navigation failure during simulated Martian descent using Gaussian splatting and uncertainty quantification.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Khriis-K/Fidelis

### [k-harikumar/PLS-GS](https://github.com/k-harikumar/PLS-GS)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T23:46:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Probabilistic Lidar Scaffolds for Compact, Surface-Aligned Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/k-harikumar/PLS-GS

### [adash963/3DGS_LRF_SH_Compression](https://github.com/adash963/3DGS_LRF_SH_Compression)

- **主题：** 压缩与轻量化
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T17:03:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** This repository is intended for the AIML Research for the LJMU University. This repository's work is done on top of Vanilla 3DGS repository published by Alexandre Lanvin @alanvinx. The purpose of this repository is purely for research and not for commercialising or any form of profiteering.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合评估Web、移动端、流传输、存储成本和LOD管线。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/adash963/3DGS_LRF_SH_Compression

### [Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v4)

- **主题：** 几何/材质/光照
- **来源：** arXiv
- **发布时间/更新时间：** 2026-11-02T09:01:18Z
- **更新判定：** 实质修订
- **核心内容：** 3D reconstruction for Digital Twins often relies on LiDAR-based methods, which provide accurate geometry but lack the semantics and textures naturally captured by cameras. Traditional LiDAR-camera fusion approaches require complex calibration and still struggle with certain materials like glass, which are visible in images but poorly represented in point clouds. We propose a camera-only pipeline that reconstructs scenes using 3D Gaussian Splatting from multi-view images, extracts semantic material masks via vision models, converts Gaussian representations to mesh surfaces with projected material labels, and assigns physics-based material properties for accurate sensor simulation in modern graphics engines and simulators. This approach combines photorealistic reconstruction with physics-based material assignment, providing sensor simulation fidelity comparable to LiDAR-camera fusion while eliminating hardware complexity and calibration requirements. We validate our camera-only method u…
- **成熟度：** R2/E0
- **是否开源：** 代码状态待核验
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。
- **论文原文：** https://arxiv.org/pdf/2511.20348v4

### [sakorman/3dgs-mesh-compare](https://github.com/sakorman/3dgs-mesh-compare)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T23:57:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 同一组真实照片，对比 3DGS 与传统 Stereo + Poisson Mesh 的重建效果、浏览器性能和资源成本。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sakorman/3dgs-mesh-compare

### [jesusluque/splat2mesh](https://github.com/jesusluque/splat2mesh)

- **主题：** 几何/材质/光照
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T04:17:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting → UV-textured USD mesh, automated (Apache-2.0)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jesusluque/splat2mesh

### [Water-aware photogrammetry and Gaussian splatting for shoreline structures](http://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=&tid=6ae9a122d3d8421baa625c2905b7ca9e&url=https%3a%2f%2fgithub.com%2flaurigates%2fshore-recon&c=9538051327784891226&mkt=en-us)

- **主题：** 几何/材质/光照
- **来源：** Bing News
- **发布时间/更新时间：** 2026-11-02T13:02:00Z
- **更新判定：** 行业/媒体动态
- **核心内容：** One drone or phone clip of a pier, shore or waterfront goes in; a textured mesh with its water plane and a Gaussian splat come out. Docker must be running: the segmentation model and OpenMVS run in ...
- **成熟度：** 二次来源
- **是否开源：** 不适用
- **开发价值：** 可用于提升表面、法线、材质、反射或重照明能力。
- **局限：** 属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。

### [luohongk/Embodied-AI-Daily](https://github.com/luohongk/Embodied-AI-Daily)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T00:20:25Z
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
- **发布时间/更新时间：** 2026-11-03T08:36:24Z
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
- **发布时间/更新时间：** 2026-11-03T08:52:20Z
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
- **发布时间/更新时间：** 2026-11-02T15:22:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 空間智能的跨 embodiment 手冊 —— 把 SLAM / VIO / 3D 表徵 / 感測器堆疊 / 部署坑 在 機械臂 / 無人機 / 自駕 / 人形 / 水下 之間橫向比較，底層共用 3DGS / VGGT / depth foundation。照見三冊 perception 端（VLA-Handbook + Physics-Controllable-Generation-Handbook 姊妹倉）。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/sou350121/Spatial-Intelligence-Handbook

### [NVIDIA/NuRec](https://github.com/NVIDIA/NuRec)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T16:21:35Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** NVIDIA Omniverse NuRec provides neural reconstruction APIs and libraries to reconstruct and render interactive simulations from real-world data.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/NVIDIA/NuRec

### [koroltony/UCLA_Gateway_Plaza_3DGS](https://github.com/koroltony/UCLA_Gateway_Plaza_3DGS)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:43:27Z
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
- **发布时间/更新时间：** 2026-11-03T03:56:43Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-NeRF-and-3DGS-SLAM

### [arthurlirui/AIRobotSim](https://github.com/arthurlirui/AIRobotSim)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T02:06:33Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS reconstruction-based robot swarm/comm/interaction research platform
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/arthurlirui/AIRobotSim

### [Oguzhan61-dilmac/360-vid2splat](https://github.com/Oguzhan61-dilmac/360-vid2splat)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T20:59:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 360° kamera veya telefon videosunu tarayıcıda WASD ile içinde yürünebilen fotogerçekçi 3D sahneye çeviren açık kaynak hat (COLMAP + Gaussian Splatting). Ücretsiz Colab GPU’su ve GitHub Pages ile çalışır.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Oguzhan61-dilmac/360-vid2splat

### [viam-labs/gaussian-splatting](https://github.com/viam-labs/gaussian-splatting)

- **主题：** SLAM与重建
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T20:30:36Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Viam module: drive any arm-mounted camera through a scan, upload posed images as a sequence dataset, and build a metric Gaussian splat with 3DGRUT
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合相机定位、在线建图、工程测绘和大场景重建验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/viam-labs/gaussian-splatting

### [InkMind-AI/ZeroSplat](https://github.com/InkMind-AI/ZeroSplat)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:39:14Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/InkMind-AI/ZeroSplat

### [nancywan1004/supersplat-viewer](https://github.com/nancywan1004/supersplat-viewer)

- **主题：** 编辑与生成
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T06:13:07Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** An advanced 3DGS viewer and editor.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 可用于对象提取、语义分层、内容编辑和生成式资产工作流。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nancywan1004/supersplat-viewer

### [Add SPZ_NIANTIC_georeference extension (#105) Add SPZ_NIANTIC_georeference extension (vendor ID 0x4E53) Stores a similarity transform (origin, unit quaternion, scale) from the asset's RUB frame into a geocentric CRS, given as AUTHORITY:CODE (e.g. EPSG:4978) or inline PROJJSON for non-Earth bodies, with an optional coordinate epoch. The library validates the record but never applies it. Adds SpzExtensionBase::isValid() (default true); saveSpz now fails if any extension is invalid. Includes Python/WASM bindings, docs and tests. Co-authored-by: Diego <diego@nianticspatial.com>](https://github.com/nianticlabs/spz/commit/83980b75bc008dda571fd2f98fed36fac6c6052e)

- **主题：** 实时渲染与展示
- **来源：** GitHub · NianticLabs/spz
- **发布时间/更新时间：** 2026-11-02T21:40:32Z
- **更新判定：** 代码实质更新
- **核心内容：** Add SPZ_NIANTIC_georeference extension (#105) Add SPZ_NIANTIC_georeference extension (vendor ID 0x4E53) Stores a similarity transform (origin, unit quaternion, scale) from the asset's RUB frame into a geocentric CRS, given as AUTHORITY:CODE (e.g. EPSG:4978) or inline PROJJSON for non-Earth bodies, with an optional coordinate epoch. The library validates the record but never applies it. Adds SpzExtensionBase::isValid() (default true); saveSpz now fails if any extension is invalid. Includes Python/WASM bindings, docs and tests. Co-authored-by: Diego <diego@nianticspatial.com>
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/NianticLabs/spz

### [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T04:31:42Z
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
- **发布时间/更新时间：** 2026-11-03T02:13:38Z
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
- **发布时间/更新时间：** 2026-11-03T03:19:47Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 1000+ arXiv-verified 3DGS methods · 15 AI agent skills · MCP server (34 tools) · open ebook — the AI-native entry to 3D Gaussian Splatting research
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/jaccen/Awesome-Gaussian-Skills

### [Xget7/splatkit](https://github.com/Xget7/splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T21:44:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Real-time Gaussian splatting SDKs for Android/Vulkan, iOS/Metal and React Native, sharing a C++17 engine.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/splatkit

### [changruizhu96/Unity-XR-3DGS-Toolkit](https://github.com/changruizhu96/Unity-XR-3DGS-Toolkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T17:27:48Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Unity toolkit for 3D Gaussian Splatting (3DGS) in VR and mixed reality (XR), with Meta Quest registration, passthrough interaction, and spatial anchors. Ongoing development from MR-Compare.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/changruizhu96/Unity-XR-3DGS-Toolkit

### [WilliamLiu-1997/3dgs-renderer-bench](https://github.com/WilliamLiu-1997/3dgs-renderer-bench)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T05:39:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3D Gaussian Splatting renderer benchmark: Spark, SuperSplat and Gaussian Splat Lite, with reproducible measurements and an interactive report
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/WilliamLiu-1997/3dgs-renderer-bench

### [Xget7/react-native-splatkit](https://github.com/Xget7/react-native-splatkit)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T21:54:15Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** React Native component for real-time Gaussian splatting: load an SPZ scene, pick a quality preset, and walk through it from JavaScript.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Xget7/react-native-splatkit

### [Archerkattri/Archerkattri](https://github.com/Archerkattri/Archerkattri)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:52:58Z
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
- **发布时间/更新时间：** 2026-11-03T08:29:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 受限采集下的稀疏视角 3DGS 文化遗产重建 + 多模态大模型·VQA-VL 流式视频问答与空间定位系统
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/aozi6666/Sparse-3DGS-heritage-VQA

### [yclen/splat-viewer](https://github.com/yclen/splat-viewer)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T07:39:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Browser viewer for Gaussian splat scans with orbit and fly controls (three.js + Spark)
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/yclen/splat-viewer

### [mercurio-develop/niflheim-studio](https://github.com/mercurio-develop/niflheim-studio)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T07:31:39Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** ▎ NIFLheim Studio is an open-source shot pipeline: design a character, drop in a concept painting, direct the camera and VFX in 3D, and LTX shoots it, then fly through your shot as a Gaussian splat. Open weights, one 16 GB GPU, built on the Comfy SDK.
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/mercurio-develop/niflheim-studio

### [nangokosu/viking-splatad](https://github.com/nangokosu/viking-splatad)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T04:53:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Repo for lidar-camera-radar SplatAD 3DGS of Viking Hills dataset
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/nangokosu/viking-splatad

### [Zhuo-Han-challenger/Zhuo-Han-challenger.github.io](https://github.com/Zhuo-Han-challenger/Zhuo-Han-challenger.github.io)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T02:53:27Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zhuo Han — Research Scientist at Huawei | 3D Gaussian Splatting and world models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Zhuo-Han-challenger/Zhuo-Han-challenger.github.io

### [trapple/spz-webxr-check](https://github.com/trapple/spz-webxr-check)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T02:36:46Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** WebXR page to measure Gaussian splat (SPZ) rendering on Android XR
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/trapple/spz-webxr-check

### [Zhuo-Han-challenger/zhuo-han](https://github.com/Zhuo-Han-challenger/zhuo-han)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T02:30:49Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Zhuo Han — Research Scientist at Huawei | 3D Gaussian Splatting and world models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Zhuo-Han-challenger/zhuo-han

### [samaust/openftgs-xr](https://github.com/samaust/openftgs-xr)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T23:29:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** VR/desktop player for openftgs models
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/samaust/openftgs-xr

### [ArchitectureWorld/3dgs-pano](https://github.com/ArchitectureWorld/3dgs-pano)

- **主题：** 实时渲染与展示
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T08:42:58Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 适合Web、移动端、VR/AR与实时Viewer的性能验证。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ArchitectureWorld/3dgs-pano

### [Update code owners in CODEOWNERS file (#108)](https://github.com/nianticlabs/spz/commit/11312e4ad836ed06e3da2f3d5b633688d17ebebb)

- **主题：** 其他
- **来源：** GitHub · NianticLabs/spz
- **发布时间/更新时间：** 2026-11-02T22:32:17Z
- **更新判定：** 代码实质更新
- **核心内容：** Update code owners in CODEOWNERS file (#108)
- **成熟度：** E2
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。
- **代码仓库：** https://github.com/NianticLabs/spz

### [timfennell/blender-splat-patch](https://github.com/timfennell/blender-splat-patch)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T04:35:30Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Blender 5.3 extension to erase, clone stamp and heal 3D Gaussian splat scans
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/timfennell/blender-splat-patch

### [animu-sphere/usd-3dgs-plugins](https://github.com/animu-sphere/usd-3dgs-plugins)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:50:43Z
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
- **发布时间/更新时间：** 2026-11-02T10:10:50Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 3DGS论文追踪器 - 实时追踪3D Gaussian Splatting最新论文
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/ZhaoRunRunRun/3dgs-tracker

### [lin278804-ops/lf-3dgs-datagen](https://github.com/lin278804-ops/lf-3dgs-datagen)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:45:25Z
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
- **发布时间/更新时间：** 2026-11-03T08:39:51Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/lin278804-ops/lf-3dgs-project

### [Primal555/3dgs-importance](https://github.com/Primal555/3dgs-importance)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T08:15:13Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Primal555/3dgs-importance

### [wkgreat/gsplatlab](https://github.com/wkgreat/gsplatlab)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T06:18:25Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** gaussian splat (3dgs) lab
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/wkgreat/gsplatlab

### [autumn119/3DGS-Survey](https://github.com/autumn119/3DGS-Survey)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T05:58:32Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** Project page for 3DGS Survey paper
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/autumn119/3DGS-Survey

### [oceanye/py_pipe_install](https://github.com/oceanye/py_pipe_install)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T03:45:37Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 基于CAD、双目视觉和安装顺序约束的管道安装状态识别与数字孪生项目
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/oceanye/py_pipe_install

### [t-bsouza/trabalho-nerf-3dgs](https://github.com/t-bsouza/trabalho-nerf-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-03T01:02:21Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/t-bsouza/trabalho-nerf-3dgs

### [enhansome/enhansome-3dgs](https://github.com/enhansome/enhansome-3dgs)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T20:30:11Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/enhansome/enhansome-3dgs

### [Zhangmingxu8/CNN-to-3DGS](https://github.com/Zhangmingxu8/CNN-to-3DGS)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T13:41:42Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 从 CNN 到 3DGS：一个月 AI 基础训练手册（6 个模块 · 30 个 Demo · 8 篇笔记）
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/Zhangmingxu8/CNN-to-3DGS

### [JeremyHo1123/drone-3dgs-nav](https://github.com/JeremyHo1123/drone-3dgs-nav)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T12:55:52Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/JeremyHo1123/drone-3dgs-nav

### [CDY88/3DGS-magic](https://github.com/CDY88/3DGS-magic)

- **主题：** 其他
- **来源：** GitHub Search
- **发布时间/更新时间：** 2026-11-02T10:55:18Z
- **更新判定：** 新项目/近期活跃
- **核心内容：** 近期活跃的GS相关仓库。
- **成熟度：** E1
- **是否开源：** 是
- **开发价值：** 作为相邻技术线索进入持续跟踪池。
- **局限：** 近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。
- **代码仓库：** https://github.com/CDY88/3DGS-magic

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 6 |
| GitHub | ok: 56 |
| Hugging Face | ok: 0 |
| Reddit | degraded: HTTPError: HTTP Error 403: Blocked |
| Bing News | ok: 2 |
| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |
| 论文原文 | ok: 6/6 |

## 去重与可信度说明

- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。
- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。
- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。
- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。

