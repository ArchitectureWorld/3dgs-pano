from __future__ import annotations

import argparse
import dataclasses
import email.utils
import hashlib
import html
import json
import math
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Sequence


UTC = timezone.utc
DEFAULT_BASELINE = datetime(2026, 8, 13, 2, 0, tzinfo=UTC)
DEFAULT_MODEL = "openai/gpt-4.1"

ARXIV_TERMS = (
    'all:"Gaussian Splatting" OR all:"3D Gaussian" OR all:"3DGS" '
    'OR all:"4D Gaussian Splatting" OR all:"2D Gaussian Splatting"'
)

GITHUB_WATCHLIST = (
    "graphdeco-inria/gaussian-splatting",
    "nerfstudio-project/gsplat",
    "playcanvas/supersplat",
    "sparkjsdev/spark",
    "NianticLabs/spz",
    "mkkellogg/GaussianSplats3D",
    "ArthurBrussee/brush",
    "huggingface/gsplat.js",
    "JonathonLuiten/Dynamic3DGaussians",
)

RELEVANCE_RE = re.compile(
    r"\b(gaussian splat(?:ting)?|3dgs|4dgs|2dgs|gaussian surfel|splatfacto|"
    r"gaussian avatar|gaussian map|gaussian reconstruction)\b",
    re.IGNORECASE,
)

BOT_OR_NOISE_RE = re.compile(
    r"\b(dependabot|renovate|bump (?:version|dependency|dependencies)|"
    r"update (?:all )?dependencies|chore: deps|merge branch)\b",
    re.IGNORECASE,
)

THEME_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("训练与优化", ("train", "optim", "densif", "prun", "mcmc", "gradient", "loss", "initializ")),
    ("动态与4D", ("dynamic", "4d", "deform", "motion", "temporal", "avatar", "animation")),
    ("压缩与轻量化", ("compress", "compact", "quant", "codec", "stream", "lod", "lightweight", "mobile")),
    ("几何/材质/光照", ("geometry", "surface", "mesh", "sdf", "normal", "material", "relight", "reflection", "lighting")),
    ("SLAM与重建", ("slam", "mapping", "reconstruction", "pose", "localization", "sfm", "colmap")),
    ("少视角与前馈", ("sparse-view", "few-view", "feed-forward", "feedforward", "two-view", "single-view")),
    ("编辑与生成", ("edit", "generation", "generative", "segment", "semantic", "object extraction", "language")),
    ("实时渲染与展示", ("render", "raster", "web", "viewer", "vr", "ar", "webgpu", "webgl", "realtime", "real-time")),
    ("GPU与加速实现", ("cuda", "kernel", "gpu", "accelerat", "triton", "metal", "vulkan", "wasm")),
    ("数据集与评测", ("dataset", "benchmark", "evaluation", "challenge")),
    ("工业产品与平台", ("product", "platform", "release", "studio", "cloud", "capture")),
)


@dataclass
class IntelItem:
    source: str
    source_kind: str
    title: str
    url: str
    timestamp: datetime
    summary: str
    update_type: str
    score: float
    external_id: str
    authors: list[str] = field(default_factory=list)
    theme: str = "其他"
    maturity: str = "待判断"
    open_source: str = "待核验"
    pdf_url: str | None = None
    repository: str | None = None
    related_sources: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.timestamp = ensure_utc(self.timestamp)
        self.title = normalize_whitespace(self.title)
        self.summary = normalize_whitespace(self.summary)
        if not self.related_sources:
            self.related_sources = [self.source]
        if not self.theme or self.theme == "其他":
            self.theme = classify_theme(f"{self.title} {self.summary}")

    def to_dict(self) -> dict[str, Any]:
        result = dataclasses.asdict(self)
        result["timestamp"] = iso_z(self.timestamp)
        return result


class HttpClient:
    def __init__(self, timeout: int = 45, retries: int = 3) -> None:
        self.timeout = timeout
        self.retries = retries
        self.user_agent = "ArchitectureWorld-GS-Intelligence/1.0"

    def request(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        data: bytes | None = None,
        method: str | None = None,
    ) -> bytes:
        merged = {"User-Agent": self.user_agent, "Accept": "*/*"}
        if headers:
            merged.update(headers)
        request = urllib.request.Request(url, data=data, headers=merged, method=method)
        last_error: Exception | None = None
        for attempt in range(self.retries):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return response.read()
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
                last_error = exc
                if isinstance(exc, urllib.error.HTTPError) and exc.code in {400, 401, 403, 404, 422}:
                    break
                if attempt + 1 < self.retries:
                    time.sleep(min(2**attempt, 4))
        assert last_error is not None
        raise last_error

    def get_text(self, url: str, headers: dict[str, str] | None = None) -> str:
        return self.request(url, headers=headers).decode("utf-8", errors="replace")

    def get_json(self, url: str, headers: dict[str, str] | None = None) -> Any:
        return json.loads(self.get_text(url, headers=headers))

    def post_json(self, url: str, payload: dict[str, Any], headers: dict[str, str]) -> Any:
        merged = {"Content-Type": "application/json", **headers}
        raw = self.request(
            url,
            headers=merged,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            method="POST",
        )
        return json.loads(raw.decode("utf-8", errors="replace"))


def normalize_whitespace(value: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def strip_html(value: str | None) -> str:
    return normalize_whitespace(re.sub(r"<[^>]+>", " ", value or ""))


def ensure_utc(value: datetime) -> datetime:
    return value.replace(tzinfo=UTC) if value.tzinfo is None else value.astimezone(UTC)


def parse_datetime(value: str | None) -> datetime:
    if not value:
        raise ValueError("datetime value is required")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return ensure_utc(datetime.fromisoformat(text))


def iso_z(value: datetime) -> str:
    return ensure_utc(value).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_title(value: str) -> str:
    text = normalize_whitespace(value).lower()
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text).strip("-")


def safe_pdf_filename(identifier: str, title: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]+', "_", normalize_whitespace(title))
    cleaned = re.sub(r"\s+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("._ ")[:120].rstrip("._ ")
    prefix = re.sub(r"[^A-Za-z0-9._-]+", "_", identifier).strip("._")
    return f"{prefix}_{cleaned}.pdf" if cleaned else f"{prefix}.pdf"


def resolve_window_start(latest_report: Path, baseline: datetime = DEFAULT_BASELINE) -> datetime:
    baseline = ensure_utc(baseline)
    try:
        text = latest_report.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return baseline
    match = re.search(r"(?m)^window_end_utc:\s*(\S+)\s*$", "\n".join(text.splitlines()[:40]))
    if not match:
        return baseline
    try:
        return max(parse_datetime(match.group(1)), baseline)
    except (TypeError, ValueError):
        return baseline


def classify_theme(text: str) -> str:
    lowered = normalize_whitespace(text).lower()
    for theme, terms in THEME_RULES:
        if any(term in lowered for term in terms):
            return theme
    return "其他"


def relevance_bonus(text: str) -> float:
    lowered = normalize_whitespace(text).lower()
    terms = (
        "training", "optimization", "compression", "slam", "4d", "dynamic",
        "geometry", "surface", "editing", "semantic", "webgpu", "mobile",
        "benchmark", "dataset", "release", "cuda", "kernel", "large-scale",
    )
    return min(sum(3.0 for term in terms if term in lowered), 24.0)


def parse_arxiv_atom(xml_text: str, window_start: datetime, window_end: datetime) -> list[IntelItem]:
    start, end = ensure_utc(window_start), ensure_utc(window_end)
    root = ET.fromstring(xml_text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    items: list[IntelItem] = []
    for entry in root.findall("atom:entry", ns):
        title = normalize_whitespace(entry.findtext("atom:title", default="", namespaces=ns))
        summary = normalize_whitespace(entry.findtext("atom:summary", default="", namespaces=ns))
        raw_id = normalize_whitespace(entry.findtext("atom:id", default="", namespaces=ns))
        published = parse_datetime(entry.findtext("atom:published", default="", namespaces=ns))
        updated = parse_datetime(entry.findtext("atom:updated", default="", namespaces=ns))
        event_time = max(published, updated)
        if event_time < start or event_time > end:
            continue
        match = re.search(r"(\d{4}\.\d{4,5})(v\d+)?$", raw_id)
        if not match:
            continue
        arxiv_id, version = match.group(1), match.group(2) or ""
        update_type = "真正新增" if published >= start else "实质修订"
        authors = [
            normalize_whitespace(author.findtext("atom:name", default="", namespaces=ns))
            for author in entry.findall("atom:author", ns)
        ]
        categories = [
            node.attrib["term"] for node in entry.findall("atom:category", ns) if node.attrib.get("term")
        ]
        pdf_url = next(
            (
                node.attrib.get("href")
                for node in entry.findall("atom:link", ns)
                if node.attrib.get("title") == "pdf" or node.attrib.get("type") == "application/pdf"
            ),
            None,
        ) or f"https://arxiv.org/pdf/{arxiv_id}{version}"
        score = (100.0 if update_type == "真正新增" else 78.0) + relevance_bonus(f"{title} {summary}")
        items.append(
            IntelItem(
                source="arXiv",
                source_kind="paper",
                title=title,
                url=f"https://arxiv.org/abs/{arxiv_id}{version}",
                timestamp=event_time,
                summary=summary,
                update_type=update_type,
                score=score,
                external_id=f"arxiv:{arxiv_id}",
                authors=[author for author in authors if author],
                maturity="R1/E0" if update_type == "真正新增" else "R2/E0",
                open_source="代码状态待核验",
                pdf_url=pdf_url,
                metadata={
                    "arxiv_id": arxiv_id,
                    "version": version,
                    "published": iso_z(published),
                    "updated": iso_z(updated),
                    "categories": categories,
                },
            )
        )
    return sorted(items, key=lambda item: item.timestamp, reverse=True)


def deduplicate_items(items: Sequence[IntelItem]) -> list[IntelItem]:
    groups: dict[str, tuple[IntelItem, list[str]]] = {}
    title_to_key: dict[str, str] = {}
    for item in items:
        title_key = normalize_title(item.title)
        key = item.external_id or f"title:{title_key}"
        if title_key in title_to_key:
            existing_key = title_to_key[title_key]
            existing = groups[existing_key][0]
            if {item.source_kind, existing.source_kind} & {"news", "community"}:
                key = existing_key
        if key not in groups:
            groups[key] = (item, list(dict.fromkeys(item.related_sources or [item.source])))
            title_to_key.setdefault(title_key, key)
            continue
        best, sources = groups[key]
        for source in item.related_sources or [item.source]:
            if source not in sources:
                sources.append(source)
        if item.score > best.score or (item.score == best.score and item.timestamp > best.timestamp):
            item.related_sources = sources
            groups[key] = (item, sources)
        else:
            best.related_sources = sources
            groups[key] = (best, sources)
    return sorted((best for best, _ in groups.values()), key=lambda item: (item.score, item.timestamp), reverse=True)


def github_headers(token: str | None) -> dict[str, str]:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def collect_arxiv(client: HttpClient, start: datetime, end: datetime) -> list[IntelItem]:
    collected: list[IntelItem] = []
    for offset in range(0, 500, 100):
        params = urllib.parse.urlencode(
            {
                "search_query": ARXIV_TERMS,
                "start": offset,
                "max_results": 100,
                "sortBy": "lastUpdatedDate",
                "sortOrder": "descending",
            }
        )
        xml_text = client.get_text(f"https://export.arxiv.org/api/query?{params}")
        page_items = parse_arxiv_atom(xml_text, start, end)
        collected.extend(page_items)
        root = ET.fromstring(xml_text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        updated_values = [
            parse_datetime(node.findtext("atom:updated", default="", namespaces=ns))
            for node in root.findall("atom:entry", ns)
        ]
        if len(updated_values) < 100 or (updated_values and min(updated_values) < start):
            break
        time.sleep(3)
    return deduplicate_items(collected)


def collect_github(client: HttpClient, start: datetime, end: datetime, token: str | None) -> list[IntelItem]:
    headers = github_headers(token)
    items: list[IntelItem] = []
    start_iso, end_iso = iso_z(start), iso_z(end)
    for repo in GITHUB_WATCHLIST:
        encoded = urllib.parse.quote(repo, safe="/")
        commits_url = f"https://api.github.com/repos/{encoded}/commits?" + urllib.parse.urlencode(
            {"since": start_iso, "until": end_iso, "per_page": 100}
        )
        try:
            commits = client.get_json(commits_url, headers)
        except Exception:
            commits = []
        for record in commits if isinstance(commits, list) else []:
            commit = record.get("commit") or {}
            message = normalize_whitespace(commit.get("message", "")).split("\n", 1)[0]
            if not message or BOT_OR_NOISE_RE.search(message):
                continue
            date_text = ((commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date"))
            if not date_text:
                continue
            stamp = parse_datetime(date_text)
            if not start <= stamp <= end:
                continue
            score = 56.0 + relevance_bonus(message)
            if re.search(r"\b(release|add|support|implement|perf|accelerat|fix)\b", message, re.I):
                score += 8.0
            sha = str(record.get("sha") or "")
            items.append(
                IntelItem(
                    source=f"GitHub · {repo}",
                    source_kind="code",
                    title=message,
                    url=record.get("html_url") or f"https://github.com/{repo}/commit/{sha}",
                    timestamp=stamp,
                    summary=message,
                    update_type="代码实质更新",
                    score=score,
                    external_id=f"github:{repo}:commit:{sha}",
                    repository=repo,
                    maturity="E2",
                    open_source="是",
                    metadata={"sha": sha, "repo": repo},
                )
            )
        try:
            releases = client.get_json(f"https://api.github.com/repos/{encoded}/releases?per_page=20", headers)
        except Exception:
            releases = []
        for release in releases if isinstance(releases, list) else []:
            date_text = release.get("published_at") or release.get("created_at")
            if not date_text:
                continue
            stamp = parse_datetime(date_text)
            if not start <= stamp <= end:
                continue
            title = normalize_whitespace(release.get("name") or release.get("tag_name") or "Release")
            body = strip_html(release.get("body", ""))
            items.append(
                IntelItem(
                    source=f"GitHub Release · {repo}",
                    source_kind="release",
                    title=f"{repo} {title}",
                    url=release.get("html_url") or f"https://github.com/{repo}/releases",
                    timestamp=stamp,
                    summary=body[:1800] or f"发布版本 {release.get('tag_name', title)}。",
                    update_type="正式版本发布",
                    score=92.0 + relevance_bonus(f"{title} {body}"),
                    external_id=f"github:{repo}:release:{release.get('id', release.get('tag_name', title))}",
                    repository=repo,
                    maturity="E2",
                    open_source="是",
                    metadata={"tag": release.get("tag_name"), "repo": repo},
                )
            )

    seen_repos = {repo.lower() for repo in GITHUB_WATCHLIST}
    for query in (f"gaussian-splatting pushed:>={start.date()}", f"3dgs pushed:>={start.date()}"):
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
            {"q": query, "sort": "updated", "order": "desc", "per_page": 50}
        )
        try:
            payload = client.get_json(url, headers)
        except Exception:
            continue
        for record in payload.get("items", []) if isinstance(payload, dict) else []:
            full_name = str(record.get("full_name") or "")
            if not full_name or full_name.lower() in seen_repos:
                continue
            text = f"{record.get('name', '')} {record.get('description', '')} {' '.join(record.get('topics') or [])}"
            if not RELEVANCE_RE.search(text):
                continue
            date_text = record.get("pushed_at") or record.get("updated_at")
            if not date_text:
                continue
            stamp = parse_datetime(date_text)
            if not start <= stamp <= end:
                continue
            stars = int(record.get("stargazers_count") or 0)
            items.append(
                IntelItem(
                    source="GitHub Search",
                    source_kind="project",
                    title=full_name,
                    url=record.get("html_url") or f"https://github.com/{full_name}",
                    timestamp=stamp,
                    summary=normalize_whitespace(record.get("description") or "近期活跃的GS相关仓库。"),
                    update_type="新项目/近期活跃",
                    score=38.0 + min(math.log10(stars + 1) * 8.0, 20.0),
                    external_id=f"github:repo:{full_name.lower()}",
                    repository=full_name,
                    maturity="E1",
                    open_source="是",
                    metadata={"stars": stars, "language": record.get("language")},
                )
            )
            seen_repos.add(full_name.lower())
    return items


def collect_huggingface(client: HttpClient, start: datetime, end: datetime) -> list[IntelItem]:
    items: list[IntelItem] = []
    for kind, endpoint in (("model", "https://huggingface.co/api/models"), ("space", "https://huggingface.co/api/spaces")):
        for query in ("gaussian splatting", "3dgs"):
            params = urllib.parse.urlencode({"search": query, "sort": "lastModified", "direction": "-1", "limit": 50})
            try:
                records = client.get_json(f"{endpoint}?{params}")
            except Exception:
                continue
            for record in records if isinstance(records, list) else []:
                date_text = record.get("lastModified") or record.get("createdAt")
                if not date_text:
                    continue
                stamp = parse_datetime(date_text)
                if not start <= stamp <= end:
                    continue
                record_id = str(record.get("id") or record.get("modelId") or "")
                tags = [str(tag) for tag in record.get("tags") or []]
                text = f"{record_id} {' '.join(tags)} {record.get('pipeline_tag', '')}"
                if not record_id or not RELEVANCE_RE.search(text):
                    continue
                likes, downloads = int(record.get("likes") or 0), int(record.get("downloads") or 0)
                kind_cn = "模型" if kind == "model" else "交互演示"
                items.append(
                    IntelItem(
                        source=f"Hugging Face {kind_cn}",
                        source_kind=f"hf_{kind}",
                        title=record_id,
                        url=f"https://huggingface.co/{'spaces/' if kind == 'space' else ''}{record_id}",
                        timestamp=stamp,
                        summary=f"近期更新的{kind_cn}；标签：{', '.join(tags[:12]) or '未提供'}。",
                        update_type=f"{kind_cn}更新",
                        score=36.0 + min(math.log10(likes + downloads + 1) * 4.0, 16.0),
                        external_id=f"huggingface:{kind}:{record_id.lower()}",
                        maturity="E1",
                        open_source="以页面许可为准",
                        metadata={"likes": likes, "downloads": downloads, "tags": tags},
                    )
                )
    return items


def collect_reddit(client: HttpClient, start: datetime, end: datetime) -> list[IntelItem]:
    params = urllib.parse.urlencode({"q": '"gaussian splatting" OR 3dgs', "sort": "new", "t": "month", "limit": 100, "raw_json": 1})
    payload = client.get_json(
        f"https://www.reddit.com/search.json?{params}",
        {"Accept": "application/json", "User-Agent": client.user_agent},
    )
    items: list[IntelItem] = []
    for child in (((payload or {}).get("data") or {}).get("children") or []):
        data = child.get("data") or {}
        stamp = datetime.fromtimestamp(float(data.get("created_utc") or 0), tz=UTC)
        title, body = normalize_whitespace(data.get("title", "")), normalize_whitespace(data.get("selftext", ""))
        if not start <= stamp <= end or not RELEVANCE_RE.search(f"{title} {body}"):
            continue
        permalink = data.get("permalink") or ""
        items.append(
            IntelItem(
                source=f"Reddit · r/{data.get('subreddit', 'unknown')}",
                source_kind="community",
                title=title,
                url=f"https://www.reddit.com{permalink}" if permalink else data.get("url", ""),
                timestamp=stamp,
                summary=body[:1200] or f"社区讨论；评论 {data.get('num_comments', 0)}。",
                update_type="社区线索",
                score=18.0 + min(int(data.get("score") or 0) / 20.0, 12.0),
                external_id=f"reddit:{data.get('id', normalize_title(title))}",
                maturity="线索",
                open_source="不适用",
                metadata={"reddit_score": data.get("score"), "comments": data.get("num_comments")},
            )
        )
    return items


def collect_bing_news(client: HttpClient, start: datetime, end: datetime) -> list[IntelItem]:
    items: list[IntelItem] = []
    for query in ('"Gaussian Splatting"', '"3DGS" rendering'):
        params = urllib.parse.urlencode({"q": query, "format": "rss"})
        root = ET.fromstring(client.get_text(f"https://www.bing.com/news/search?{params}"))
        for entry in root.findall("./channel/item"):
            title = normalize_whitespace(entry.findtext("title", default=""))
            description = strip_html(entry.findtext("description", default=""))
            date_text = entry.findtext("pubDate")
            stamp = ensure_utc(email.utils.parsedate_to_datetime(date_text)) if date_text else None
            if not stamp or not start <= stamp <= end or not RELEVANCE_RE.search(f"{title} {description}"):
                continue
            items.append(
                IntelItem(
                    source="Bing News",
                    source_kind="news",
                    title=title,
                    url=normalize_whitespace(entry.findtext("link", default="")),
                    timestamp=stamp,
                    summary=description[:1400],
                    update_type="行业/媒体动态",
                    score=26.0 + relevance_bonus(f"{title} {description}") / 2,
                    external_id=f"title:{normalize_title(title)}",
                    maturity="二次来源",
                    open_source="不适用",
                )
            )
    return items


def collect_all(client: HttpClient, start: datetime, end: datetime, token: str | None) -> tuple[list[IntelItem], dict[str, str]]:
    items: list[IntelItem] = []
    status: dict[str, str] = {}
    collectors: tuple[tuple[str, Callable[[], list[IntelItem]]], ...] = (
        ("arXiv", lambda: collect_arxiv(client, start, end)),
        ("GitHub", lambda: collect_github(client, start, end, token)),
        ("Hugging Face", lambda: collect_huggingface(client, start, end)),
        ("Reddit", lambda: collect_reddit(client, start, end)),
        ("Bing News", lambda: collect_bing_news(client, start, end)),
    )
    for name, collector in collectors:
        try:
            result = collector()
            items.extend(result)
            status[name] = f"ok: {len(result)}"
        except Exception as exc:
            status[name] = f"degraded: {type(exc).__name__}: {normalize_whitespace(str(exc))[:240]}"
    return deduplicate_items(items), status


def escape_md(value: str) -> str:
    return normalize_whitespace(value).replace("|", "\\|")


def short(value: str, limit: int) -> str:
    text = normalize_whitespace(value)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def engineering_assessment(item: IntelItem) -> tuple[str, str]:
    values = {
        "训练与优化": "适合进入训练速度、显存、收敛稳定性和画质的A/B基准。",
        "动态与4D": "可用于动态场景、Avatar、时序重建或可编辑运动表示预研。",
        "压缩与轻量化": "适合评估Web、移动端、流传输、存储成本和LOD管线。",
        "几何/材质/光照": "可用于提升表面、法线、材质、反射或重照明能力。",
        "SLAM与重建": "适合相机定位、在线建图、工程测绘和大场景重建验证。",
        "少视角与前馈": "适合减少采集成本、缩短建模周期或探索前馈式重建。",
        "编辑与生成": "可用于对象提取、语义分层、内容编辑和生成式资产工作流。",
        "实时渲染与展示": "适合Web、移动端、VR/AR与实时Viewer的性能验证。",
        "GPU与加速实现": "适合在现有训练或渲染链路中直接做内核级基准。",
        "数据集与评测": "可用于补齐内部验收集、指标和横向对比基线。",
        "工业产品与平台": "可用于判断产品集成、交互体验和商业化成熟度。",
    }
    value = values.get(item.theme, "作为相邻技术线索进入持续跟踪池。")
    if item.source_kind == "paper":
        limitation = "预印本结果需等待代码、第三方复现和不同场景独立验证；自动任务不会把作者自报结果视为生产结论。"
    elif item.source_kind in {"code", "release"}:
        limitation = "单次提交或版本说明不等于端到端收益，需在目标GPU、数据集和完整管线中复测。"
    elif item.source_kind in {"project", "hf_model", "hf_space"}:
        limitation = "近期活跃或可演示不代表工程稳定，应核对许可、测试、维护者活跃度和可复现性。"
    else:
        limitation = "属于二次来源或社区线索，只能作为发现入口，必须回查论文、代码或官方公告。"
    return value, limitation


def render_report(
    items: Sequence[IntelItem],
    source_status: dict[str, str],
    window_start: datetime,
    window_end: datetime,
    generated_at: datetime,
    ai_analysis: str | None,
) -> str:
    start, end, generated = ensure_utc(window_start), ensure_utc(window_end), ensure_utc(generated_at)
    ordered = sorted(items, key=lambda item: (item.score, item.timestamp), reverse=True)
    lines = [
        "---",
        "schema: architectureworld/gs-intelligence/v1",
        f"window_start_utc: {iso_z(start)}",
        f"window_end_utc: {iso_z(end)}",
        f"generated_at_utc: {iso_z(generated)}",
        f"item_count: {len(ordered)}",
        "---",
        "",
        f"# Gaussian Splatting（GS/3DGS）技术情报｜{generated.date().isoformat()}",
        "",
        f"**统计窗口：** {iso_z(start)} — {iso_z(end)}  ",
        "**运行方式：** 每日自动增量；如发生停跑，则从上一份报告末端连续补齐，不丢失中间日期。",
        "",
        "## 执行摘要",
        "",
    ]
    if ordered:
        new_count = sum(item.update_type == "真正新增" for item in ordered)
        revised = sum(item.update_type == "实质修订" for item in ordered)
        engineering = sum(item.source_kind in {"code", "release", "project"} for item in ordered)
        lines += [
            f"本轮保留 **{len(ordered)}** 项去重后的有效线索：真正新增论文 **{new_count}** 项、"
            f"实质论文修订 **{revised}** 项、代码/版本/项目更新 **{engineering}** 项。",
            "排序优先级为原始论文与正式发布，其次是实质代码更新；媒体与社区转发不会压过原始来源。",
            "",
        ]
    else:
        lines += [
            "本统计窗口内未检出可由原始论文、正式发布或代码记录核验的重大更新。",
            "下方仍保留数据源状态，以区分“确实无新增”和“数据源暂时不可用”。",
            "",
        ]

    lines += [
        "## 今日最重要的5项更新",
        "",
        "| 排名 | 内容 | 类型 | 来源 | 成熟度 | 工程优先级 |",
        "|---:|---|---|---|---|---|",
    ]
    if ordered:
        for index, item in enumerate(ordered[:5], 1):
            priority = "P0" if item.score >= 95 else ("P1" if item.score >= 70 else "P2")
            lines.append(
                f"| {index} | [{escape_md(item.title)}]({item.url}) | {escape_md(item.update_type)} | "
                f"{escape_md(item.source)} | {escape_md(item.maturity)} | {priority} |"
            )
    else:
        lines.append("| — | 今日无重大新增 | — | — | — | — |")
    lines.append("")

    if ai_analysis:
        lines += ["## AI综合研判", "", ai_analysis.strip(), ""]

    lines += ["## 分类详述", ""]
    themes: dict[str, list[IntelItem]] = {}
    for item in ordered:
        themes.setdefault(item.theme, []).append(item)
    for theme in [rule[0] for rule in THEME_RULES] + ["其他"]:
        for item in themes.get(theme, []):
            value, limitation = engineering_assessment(item)
            lines += [
                f"### [{item.title}]({item.url})",
                "",
                f"- **主题：** {theme}",
                f"- **来源：** {'、'.join(item.related_sources)}",
                f"- **发布时间/更新时间：** {iso_z(item.timestamp)}",
                f"- **更新判定：** {item.update_type}",
                f"- **核心内容：** {short(item.summary, 1000)}",
                f"- **成熟度：** {item.maturity}",
                f"- **是否开源：** {item.open_source}",
                f"- **开发价值：** {value}",
                f"- **局限：** {limitation}",
            ]
            if item.pdf_url:
                lines.append(f"- **论文原文：** {item.pdf_url}")
            if item.repository:
                lines.append(f"- **代码仓库：** https://github.com/{item.repository}")
            lines.append("")

    lines += ["## 数据源状态", "", "| 数据源 | 状态 |", "|---|---|"]
    for name, status in source_status.items():
        lines.append(f"| {escape_md(name)} | {escape_md(status)} |")
    lines += [
        "",
        "## 去重与可信度说明",
        "",
        "- arXiv ID、GitHub commit/release/repository ID、Hugging Face资源ID和Reddit ID作为首要去重键。",
        "- 标题一致时，原论文或正式发布优先于媒体、社区二次传播，并保留交叉来源名称。",
        "- 数据源故障明确记录为 `degraded`，不会被伪装成“今日没有更新”。",
        "- 未能核验的代码、产品和成熟度会明确标记，不生成虚构的开源状态或性能数字。",
        "",
    ]
    return "\n".join(lines)


def build_ai_prompt(items: Sequence[IntelItem], start: datetime, end: datetime) -> str:
    candidates = [
        {
            "title": item.title,
            "source": item.source,
            "url": item.url,
            "timestamp": iso_z(item.timestamp),
            "update_type": item.update_type,
            "theme": item.theme,
            "maturity": item.maturity,
            "open_source": item.open_source,
            "summary": short(item.summary, 1500),
            "score": item.score,
        }
        for item in sorted(items, key=lambda value: (value.score, value.timestamp), reverse=True)[:40]
    ]
    return (
        "你是Gaussian Splatting（GS/3DGS）技术情报分析员。仅依据给定候选JSON，用中文输出紧凑Markdown分析，"
        "不得补造论文、性能数字、代码状态、产品动态或链接。请：1）概括技术趋势；2）区分真正新增、实质修订与二次传播；"
        "3）对最多5项重点说明相对既有路线的变化、成熟度、开发价值与局限；4）没有重大新增时明确说明。"
        f"\n统计窗口：{iso_z(start)} — {iso_z(end)}\n候选JSON：\n"
        + json.dumps(candidates, ensure_ascii=False, indent=2)
    )


def call_github_models(
    client: HttpClient,
    token: str | None,
    items: Sequence[IntelItem],
    start: datetime,
    end: datetime,
    model: str,
) -> tuple[str | None, str]:
    if not token:
        return None, "skipped: GITHUB_TOKEN unavailable"
    if not items:
        return None, "skipped: no candidates"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "只做证据约束的中文技术情报分析，禁止虚构事实。"},
            {"role": "user", "content": build_ai_prompt(items, start, end)},
        ],
        "temperature": 0.1,
        "max_tokens": 6000,
    }
    try:
        result = client.post_json(
            "https://models.github.ai/inference/chat/completions",
            payload,
            {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        )
        content = (((result or {}).get("choices") or [{}])[0].get("message") or {}).get("content", "")
        return (str(content).strip(), f"ok: {model}") if normalize_whitespace(content) else (None, "degraded: empty response")
    except Exception as exc:
        return None, f"degraded: {type(exc).__name__}: {normalize_whitespace(str(exc))[:240]}"


def download_pdfs(client: HttpClient, items: Sequence[IntelItem], output_dir: Path, limit: int = 40) -> list[dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, Any]] = []
    for item in [value for value in items if value.source_kind == "paper" and value.pdf_url][:limit]:
        arxiv_id = str(item.metadata.get("arxiv_id") or item.external_id.removeprefix("arxiv:"))
        identifier = f"{arxiv_id}{item.metadata.get('version') or ''}"
        filename = safe_pdf_filename(identifier, item.title)
        record: dict[str, Any] = {
            "external_id": item.external_id,
            "title": item.title,
            "source_url": item.pdf_url,
            "filename": filename,
            "status": "failed",
        }
        try:
            data = client.request(item.pdf_url or "")
            if not data.startswith(b"%PDF-") or len(data) < 100_000:
                raise ValueError("response is not a valid scholarly PDF")
            (output_dir / filename).write_bytes(data)
            record.update({"status": "ok", "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {normalize_whitespace(str(exc))[:240]}"
        manifest.append(record)
        time.sleep(3)
    (output_dir / "manifest.json").write_text(json.dumps({"papers": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checksums = [f"{item['sha256']}  {item['filename']}" for item in manifest if item.get("status") == "ok"]
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(checksums) + ("\n" if checksums else ""), encoding="utf-8")
    return manifest


def write_ris(items: Sequence[IntelItem], path: Path) -> None:
    records: list[str] = []
    for item in items:
        lines = [f"TY  - {'JOUR' if item.source_kind == 'paper' else 'ELEC'}", f"TI  - {item.title}"]
        lines.extend(f"AU  - {author}" for author in item.authors)
        lines += [
            f"PY  - {item.timestamp.year}",
            f"DA  - {item.timestamp.date().isoformat()}",
            f"T2  - {item.source}",
            f"UR  - {item.url}",
            f"N1  - 更新判定：{item.update_type}；成熟度：{item.maturity}；开源：{item.open_source}",
            f"N1  - {item.summary}",
        ]
        if item.external_id.startswith("arxiv:"):
            lines.append(f"DO  - 10.48550/arXiv.{item.external_id.split(':', 1)[1]}")
        lines.extend(f"KW  - {keyword}" for keyword in (item.theme, "GS技术情报", item.update_type))
        lines.append("ER  -")
        records.append("\r\n".join(lines))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\r\n\r\n".join(records) + ("\r\n" if records else ""), encoding="utf-8")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect daily GS/3DGS technology intelligence.")
    parser.add_argument("--latest-report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--raw-json", type=Path, required=True)
    parser.add_argument("--papers-dir", type=Path, required=True)
    parser.add_argument("--ris", type=Path, required=True)
    parser.add_argument("--baseline", default=iso_z(DEFAULT_BASELINE))
    parser.add_argument("--window-end")
    parser.add_argument("--model", default=os.environ.get("GITHUB_MODELS_MODEL", DEFAULT_MODEL))
    parser.add_argument("--skip-ai", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    baseline = parse_datetime(args.baseline)
    end = parse_datetime(args.window_end) if args.window_end else datetime.now(tz=UTC)
    start = resolve_window_start(args.latest_report, baseline)
    if start >= end:
        start = max(baseline, end - timedelta(days=1))

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    client = HttpClient()
    items, status = collect_all(client, start, end, token)
    analysis = None
    if args.skip_ai:
        status["GitHub Models"] = "skipped: --skip-ai"
    else:
        analysis, status["GitHub Models"] = call_github_models(client, token, items, start, end, args.model)

    pdf_manifest = download_pdfs(client, items, args.papers_dir)
    ok_pdfs = sum(record.get("status") == "ok" for record in pdf_manifest)
    status["论文原文"] = f"ok: {ok_pdfs}/{len(pdf_manifest)}" if pdf_manifest else "ok: 0"

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        render_report(items, status, start, end, end, analysis) + "\n",
        encoding="utf-8",
    )
    args.raw_json.parent.mkdir(parents=True, exist_ok=True)
    args.raw_json.write_text(
        json.dumps(
            {
                "window_start_utc": iso_z(start),
                "window_end_utc": iso_z(end),
                "source_status": status,
                "items": [item.to_dict() for item in items],
                "pdf_manifest": pdf_manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    write_ris(items, args.ris)
    print(json.dumps({"window_start_utc": iso_z(start), "window_end_utc": iso_z(end), "items": len(items), "pdfs": ok_pdfs}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
