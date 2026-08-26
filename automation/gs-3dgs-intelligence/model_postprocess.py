from __future__ import annotations

import argparse
import copy
import json
import os
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence


RequestJson = Callable[[str, dict[str, Any], dict[str, str]], dict[str, Any]]


@dataclass(frozen=True)
class ProviderConfig:
    base_url: str
    api_key: str
    model: str

    @property
    def endpoint(self) -> str:
        base = self.base_url.rstrip("/")
        if base.endswith("/chat/completions"):
            return base
        return f"{base}/chat/completions"


def resolve_provider_config(environ: Mapping[str, str]) -> ProviderConfig | None:
    base_url = environ.get("GS_INTELLIGENCE_MODEL_BASE_URL", "").strip()
    api_key = environ.get("GS_INTELLIGENCE_MODEL_API_KEY", "").strip()
    model = environ.get("GS_INTELLIGENCE_MODEL_NAME", "").strip()
    if not (base_url and api_key and model):
        return None
    return ProviderConfig(base_url=base_url, api_key=api_key, model=model)


def _shorten(value: Any, limit: int = 1600) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def build_prompt(raw_payload: Mapping[str, Any]) -> str:
    items = list(raw_payload.get("items") or [])
    items.sort(
        key=lambda item: (
            float(item.get("score") or 0),
            str(item.get("timestamp") or ""),
        ),
        reverse=True,
    )
    candidates = []
    for item in items[:40]:
        candidates.append(
            {
                "title": item.get("title"),
                "source": item.get("source"),
                "source_kind": item.get("source_kind"),
                "url": item.get("url"),
                "timestamp": item.get("timestamp"),
                "update_type": item.get("update_type"),
                "theme": item.get("theme"),
                "maturity": item.get("maturity"),
                "open_source": item.get("open_source"),
                "summary": _shorten(item.get("summary")),
                "score": item.get("score"),
            }
        )
    return (
        "你是 Gaussian Splatting（GS/3DGS）技术情报分析员。仅依据给定候选 JSON，"
        "用中文输出紧凑的 Markdown 分析，不得补造论文、数字、代码状态、产品动态或链接。"
        "请完成：1）概括统计窗口内最重要的技术趋势；2）区分真正新增、实质修订与二次传播；"
        "3）对最多5项重点分别说明相对既有路线的变化、成熟度、工程价值与局限；"
        "4）若没有重大新增，明确说明。不要重复完整候选清单。"
        f"\n统计窗口：{raw_payload.get('window_start_utc')} — {raw_payload.get('window_end_utc')}"
        "\n候选 JSON：\n"
        + json.dumps(candidates, ensure_ascii=False, indent=2)
    )


def default_request_json(
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
) -> dict[str, Any]:
    merged_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "ArchitectureWorld-GS-Intelligence/1.0",
        **headers,
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=merged_headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def _extract_content(response: Mapping[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return ""
    message = (choices[0] or {}).get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, Mapping) and isinstance(part.get("text"), str):
                parts.append(part["text"])
        return "\n".join(parts).strip()
    return ""


def _table_safe(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def _replace_model_status(report_text: str, status: str) -> str:
    replacement = f"| 模型综合研判 | {_table_safe(status)} |"
    lines = report_text.splitlines()
    found = False
    for index, line in enumerate(lines):
        if line.startswith("| GitHub Models |") or line.startswith("| 模型综合研判 |"):
            lines[index] = replacement
            found = True
    if not found:
        marker = "## 去重与可信度说明"
        insert_at = next((index for index, line in enumerate(lines) if line == marker), len(lines))
        addition = ["", "## 模型综合研判状态", "", replacement, ""]
        lines[insert_at:insert_at] = addition
    return "\n".join(lines) + ("\n" if report_text.endswith("\n") else "")


def _insert_analysis(report_text: str, analysis: str) -> str:
    if not analysis:
        return report_text
    section = f"## AI综合研判\n\n{analysis.strip()}\n\n"
    if "## AI综合研判" in report_text:
        start = report_text.index("## AI综合研判")
        marker = "## 分类详述"
        end = report_text.find(marker, start)
        if end >= 0:
            return report_text[:start] + section + report_text[end:]
        return report_text[:start] + section
    marker = "## 分类详述"
    if marker in report_text:
        return report_text.replace(marker, section + marker, 1)
    return report_text.rstrip() + "\n\n" + section


def postprocess_report(
    report_text: str,
    raw_payload: Mapping[str, Any],
    environ: Mapping[str, str],
    request_json: RequestJson = default_request_json,
) -> tuple[str, dict[str, Any], str]:
    raw = copy.deepcopy(dict(raw_payload))
    source_status = dict(raw.get("source_status") or {})
    source_status.pop("GitHub Models", None)
    config = resolve_provider_config(environ)

    if config is None:
        status = "skipped: 未配置兼容 OpenAI 的模型提供方"
        source_status["模型综合研判"] = status
        raw["source_status"] = source_status
        return _replace_model_status(report_text, status), raw, status

    payload = {
        "model": config.model,
        "messages": [
            {
                "role": "system",
                "content": "只做证据约束的中文技术情报分析，禁止虚构事实。",
            },
            {"role": "user", "content": build_prompt(raw)},
        ],
        "temperature": 0.1,
        "max_tokens": 6000,
    }
    headers = {"Authorization": f"Bearer {config.api_key}"}
    try:
        response = request_json(config.endpoint, payload, headers)
        analysis = _extract_content(response)
        if not analysis:
            raise ValueError("模型返回内容为空")
        status = f"ok: {config.model}"
        report = _insert_analysis(report_text, analysis)
    except Exception as exc:
        message = " ".join(str(exc).split())[:240]
        status = f"degraded: {type(exc).__name__}: {message}"
        report = report_text

    source_status["模型综合研判"] = status
    raw["source_status"] = source_status
    return _replace_model_status(report, status), raw, status


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Optionally add model-assisted Chinese synthesis to a GS intelligence report."
    )
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--raw-json", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    report_text = args.report.read_text(encoding="utf-8")
    raw_payload = json.loads(args.raw_json.read_text(encoding="utf-8"))
    report, raw, status = postprocess_report(
        report_text=report_text,
        raw_payload=raw_payload,
        environ=os.environ,
    )
    args.report.write_text(report, encoding="utf-8")
    args.raw_json.write_text(
        json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"model_analysis": status}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
