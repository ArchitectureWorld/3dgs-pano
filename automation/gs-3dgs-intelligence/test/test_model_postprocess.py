from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROGRAM_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAM_DIR))

from model_postprocess import postprocess_report  # noqa: E402


BASE_REPORT = """---
window_start_utc: 2026-08-25T02:00:00Z
window_end_utc: 2026-08-26T02:00:00Z
---

# GS report

## 执行摘要

基础摘要。

## 分类详述

正文。

## 数据源状态

| 数据源 | 状态 |
|---|---|
| arXiv | ok: 2 |
| GitHub Models | skipped: --skip-ai |
"""

RAW_PAYLOAD = {
    "window_start_utc": "2026-08-25T02:00:00Z",
    "window_end_utc": "2026-08-26T02:00:00Z",
    "source_status": {
        "arXiv": "ok: 2",
        "GitHub Models": "skipped: --skip-ai",
    },
    "items": [
        {
            "title": "Paper A",
            "source": "arXiv",
            "url": "https://arxiv.org/abs/2608.99999v1",
            "timestamp": "2026-08-25T12:00:00Z",
            "update_type": "真正新增",
            "theme": "训练与优化",
            "maturity": "R1/E0",
            "open_source": "代码状态待核验",
            "summary": "A Gaussian Splatting method.",
            "score": 100,
        }
    ],
}


class ModelPostprocessTests(unittest.TestCase):
    def test_without_provider_marks_explicit_skip_and_never_calls_network(self) -> None:
        def forbidden_request(*args, **kwargs):
            raise AssertionError("network must not be called without provider configuration")

        report, raw, status = postprocess_report(
            report_text=BASE_REPORT,
            raw_payload=RAW_PAYLOAD,
            environ={},
            request_json=forbidden_request,
        )

        self.assertEqual(status, "skipped: 未配置兼容 OpenAI 的模型提供方")
        self.assertIn("| 模型综合研判 | skipped: 未配置兼容 OpenAI 的模型提供方 |", report)
        self.assertNotIn("## AI综合研判", report)
        self.assertNotIn("GitHub Models", raw["source_status"])
        self.assertEqual(raw["source_status"]["模型综合研判"], status)

    def test_with_provider_inserts_analysis_and_uses_chat_completions_endpoint(self) -> None:
        calls = []

        def fake_request(url, payload, headers):
            calls.append((url, payload, headers))
            return {
                "choices": [
                    {
                        "message": {
                            "content": "本轮重点是新训练方法，仍需等待代码与第三方复现。"
                        }
                    }
                ]
            }

        report, raw, status = postprocess_report(
            report_text=BASE_REPORT,
            raw_payload=RAW_PAYLOAD,
            environ={
                "GS_INTELLIGENCE_MODEL_BASE_URL": "https://example.test/v1/",
                "GS_INTELLIGENCE_MODEL_API_KEY": "secret",
                "GS_INTELLIGENCE_MODEL_NAME": "example-model",
            },
            request_json=fake_request,
        )

        self.assertEqual(status, "ok: example-model")
        self.assertEqual(len(calls), 1)
        url, payload, headers = calls[0]
        self.assertEqual(url, "https://example.test/v1/chat/completions")
        self.assertEqual(payload["model"], "example-model")
        self.assertEqual(headers["Authorization"], "Bearer secret")
        self.assertIn("## AI综合研判", report)
        self.assertLess(report.index("## AI综合研判"), report.index("## 分类详述"))
        self.assertIn("本轮重点是新训练方法", report)
        self.assertIn("| 模型综合研判 | ok: example-model |", report)
        self.assertEqual(raw["source_status"]["模型综合研判"], status)


if __name__ == "__main__":
    unittest.main()
