# 3DGS Pano

本仓库承载全景影像到 Gaussian Splatting（GS/3DGS）的研发资料、流程实现与持续技术情报。

## 自动技术情报

- **运行时间：** 每天 10:00（Asia/Shanghai）
- **正常统计窗口：** 过去24小时
- **断档恢复：** 从上一份报告的结束时间连续补齐，不遗漏停跑期间内容
- **首次补跑基线：** 2026-08-13 10:00（北京时间）
- **报告入口：** [`notebook/GS-3DGS/latest.md`](notebook/GS-3DGS/latest.md)
- **日报归档：** [`notebook/GS-3DGS/daily/`](notebook/GS-3DGS/daily/)

自动任务覆盖：

- arXiv 新论文与实质修订；
- 主流 GS/3DGS 仓库 commit、release 与新项目；
- Hugging Face 模型和交互演示；
- Reddit 社区线索与 Bing News 行业动态；
- 自动去重、来源优先级、主题分类、成熟度与工程价值判断；
- 对收录的 arXiv 论文下载官方原文 PDF，并生成 SHA-256；
- 输出 Markdown 报告、原始 JSON、RIS 和论文原文 Artifact；
- 每次成功运行创建或更新一条 GitHub Issue 作为通知。

实现与测试位于 [`automation/gs-3dgs-intelligence/`](automation/gs-3dgs-intelligence/)。

> Zotero 云端写入必须以真实 Zotero Web API 或可写 Connector 为前提；当前自动任务不会把“生成 RIS”冒充为“已同步 Zotero”。
