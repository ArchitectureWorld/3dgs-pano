# GS / 3DGS Daily Intelligence Automation

该程序负责真实运行 GS/3DGS 技术情报增量任务。

## 固定调度

- 每天 10:00（Asia/Shanghai）
- GitHub Actions cron：`0 2 * * *`
- 首次补跑基线：`2026-08-13T02:00:00Z`
- 正常情况下每次分析过去24小时
- 发生停跑时，从上一份报告的 `window_end_utc` 连续补齐，不遗漏中间日期

## 数据源

- arXiv Atom API
- GitHub 重点仓库 commits / releases
- GitHub 新仓库与近期活跃项目搜索
- Hugging Face Models / Spaces
- Reddit public JSON
- Bing News RSS
- GitHub Models：用于中文综合研判；不可用时明确降级，不阻断基础报告

## 输出

仓库内 notebook：

```text
notebook/GS-3DGS/
├── README.md
├── latest.md
└── daily/YYYY-MM-DD.md
```

每次运行的 GitHub Actions Artifact：

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

## 可信度边界

- 原论文、正式 release 与可核验代码提交优先于媒体和社区转发。
- 数据源不可用会记录为 `degraded`，不会伪装成“今日无新增”。
- arXiv PDF 会校验文件头、体积和 SHA-256。
- RIS 只是 Zotero 的下游导入材料；没有真实 Zotero Web API 或可写 Connector 时，不得标记为“已同步 Zotero”。
