from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

PROGRAM_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAM_DIR))

from gs_intel import (  # noqa: E402
    IntelItem,
    deduplicate_items,
    parse_arxiv_atom,
    render_report,
    resolve_window_start,
    safe_pdf_filename,
)


UTC = timezone.utc


class ResolveWindowStartTests(unittest.TestCase):
    def test_uses_latest_report_window_end_when_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            latest = Path(tmp) / "latest.md"
            latest.write_text(
                "---\nwindow_end_utc: 2026-08-20T02:00:00Z\n---\n# report\n",
                encoding="utf-8",
            )

            result = resolve_window_start(
                latest_report=latest,
                baseline=datetime(2026, 8, 13, 2, 0, tzinfo=UTC),
            )

        self.assertEqual(result, datetime(2026, 8, 20, 2, 0, tzinfo=UTC))

    def test_falls_back_to_baseline_when_latest_report_missing(self) -> None:
        result = resolve_window_start(
            latest_report=Path("/definitely/missing/latest.md"),
            baseline=datetime(2026, 8, 13, 2, 0, tzinfo=UTC),
        )
        self.assertEqual(result, datetime(2026, 8, 13, 2, 0, tzinfo=UTC))


class ArxivParsingTests(unittest.TestCase):
    def test_classifies_new_and_revised_papers_inside_window(self) -> None:
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>https://arxiv.org/abs/2608.99901v1</id>
            <updated>2026-08-25T04:00:00Z</updated>
            <published>2026-08-25T04:00:00Z</published>
            <title>  New Gaussian Splatting Method  </title>
            <summary>A new method for 3D Gaussian Splatting.</summary>
            <author><name>Alice Example</name></author>
            <category term="cs.CV" />
            <link title="pdf" href="https://arxiv.org/pdf/2608.99901v1" type="application/pdf" />
          </entry>
          <entry>
            <id>https://arxiv.org/abs/2501.00001v3</id>
            <updated>2026-08-24T03:00:00Z</updated>
            <published>2025-01-01T00:00:00Z</published>
            <title>Revised 3DGS Compression</title>
            <summary>Substantial revision with new compression experiments.</summary>
            <author><name>Bob Example</name></author>
            <category term="cs.GR" />
            <link title="pdf" href="https://arxiv.org/pdf/2501.00001v3" type="application/pdf" />
          </entry>
          <entry>
            <id>https://arxiv.org/abs/2401.00001v1</id>
            <updated>2026-07-01T03:00:00Z</updated>
            <published>2024-01-01T00:00:00Z</published>
            <title>Old paper</title>
            <summary>Outside the window.</summary>
          </entry>
        </feed>
        """

        items = parse_arxiv_atom(
            xml,
            window_start=datetime(2026, 8, 20, tzinfo=UTC),
            window_end=datetime(2026, 8, 26, tzinfo=UTC),
        )

        self.assertEqual([item.update_type for item in items], ["真正新增", "实质修订"])
        self.assertEqual(items[0].external_id, "arxiv:2608.99901")
        self.assertEqual(items[1].external_id, "arxiv:2501.00001")
        self.assertEqual(items[0].pdf_url, "https://arxiv.org/pdf/2608.99901v1")


class DeduplicationTests(unittest.TestCase):
    def test_prefers_higher_score_and_merges_source_names(self) -> None:
        low = IntelItem(
            source="News",
            source_kind="news",
            title="A Gaussian Splatting Breakthrough",
            url="https://example.com/repost",
            timestamp=datetime(2026, 8, 25, tzinfo=UTC),
            summary="Secondary coverage.",
            update_type="二次传播",
            score=25,
            external_id="title:a-gaussian-splatting-breakthrough",
        )
        high = IntelItem(
            source="arXiv",
            source_kind="paper",
            title="A Gaussian Splatting Breakthrough",
            url="https://arxiv.org/abs/2608.99902",
            timestamp=datetime(2026, 8, 25, tzinfo=UTC),
            summary="Primary paper.",
            update_type="真正新增",
            score=100,
            external_id="title:a-gaussian-splatting-breakthrough",
        )

        result = deduplicate_items([low, high])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].url, high.url)
        self.assertEqual(result[0].score, 100)
        self.assertEqual(result[0].related_sources, ["News", "arXiv"])


class ReportingTests(unittest.TestCase):
    def test_report_contains_top_five_source_status_and_machine_metadata(self) -> None:
        items = [
            IntelItem(
                source="arXiv",
                source_kind="paper",
                title=f"Paper {index}",
                url=f"https://arxiv.org/abs/2608.99{index:03d}",
                timestamp=datetime(2026, 8, 25, index, tzinfo=UTC),
                summary=f"Summary {index}",
                update_type="真正新增",
                score=100 - index,
                external_id=f"arxiv:2608.99{index:03d}",
                theme="训练与优化",
                maturity="R1/E0",
                open_source="未发现官方代码",
            )
            for index in range(1, 7)
        ]
        report = render_report(
            items=items,
            source_status={"arXiv": "ok", "Reddit": "degraded: HTTP 403"},
            window_start=datetime(2026, 8, 25, 2, 0, tzinfo=UTC),
            window_end=datetime(2026, 8, 26, 2, 0, tzinfo=UTC),
            generated_at=datetime(2026, 8, 26, 2, 0, tzinfo=UTC),
            ai_analysis=None,
        )

        self.assertIn("window_end_utc: 2026-08-26T02:00:00Z", report)
        self.assertIn("今日最重要的5项更新", report)
        self.assertIn("Paper 1", report)
        self.assertIn("Paper 5", report)
        self.assertNotIn("| 6 | Paper 6 |", report)
        self.assertIn("Reddit", report)
        self.assertIn("degraded: HTTP 403", report)

    def test_pdf_filename_is_cross_platform_safe(self) -> None:
        name = safe_pdf_filename("2608.99901v1", 'A/B: "Gaussian" <Test>?')
        self.assertEqual(name, "2608.99901v1_A_B_Gaussian_Test.pdf")


if __name__ == "__main__":
    unittest.main()
