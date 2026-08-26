# GS / 3DGS Weekly Intelligence Automation

本程序负责真实运行 GS/3DGS 技术情报周报。

## 固定调度

- 每周一 09:00（Asia/Shanghai）
- GitHub Actions cron：`0 1 * * 1`
- 首次补跑基线：`2026-08-13T02:00:00Z`
- 后续窗口从上一份报告的 `window_end_utc` 开始

## 数据源

- arXiv Atom API
- GitHub 重点仓库 commits / releases
- GitHub 仓库搜索
- Hugging Face Models / Spaces
- Reddit public JSON
- Bing News RSS
- GitHub Models：用于中文综合研判；不可用时明确降级，不阻断报告

## 输出

仓库 notebook：

```text
notebook/GS-3DGS/
├── README.md
├── latest.md
└── weekly/YYYY-MM-DD.md
```

每次 GitHub Actions Artifact：

```text
report.md
raw.json
references.ris
papers/
├── manifest.json
├── SHA256SUMS.txt
└── 官方 arXiv PDF
```

每次成功运行还会创建或更新 GitHub Issue：

```text
GS/3DGS 技术情报｜YYYY-MM-DD
```

## 测试

```bash
python -m unittest discover \
  -s automation/gs-3dgs-intelligence/test \
  -p "test_*.py" \
  -v
```

## 说明

Zotero 云端写入不在本任务内伪造。只有在真正接入 Zotero Web API 或可写 Connector 后，才允许把报告状态标记为已同步 Zotero。
