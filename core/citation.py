"""Source citation management for research results."""

import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Citation:
    """A verified source citation."""
    url: str
    title: str
    accessed_at: str = field(default_factory=lambda: datetime.now().isoformat())
    snippet: str = ""
    reliability_score: float = 0.5
    domain: str = ""
    https: bool = False

    def __post_init__(self):
        if not self.domain:
            from urllib.parse import urlparse
            parsed = urlparse(self.url)
            self.domain = parsed.netloc
            self.https = parsed.scheme == "https"


class CitationManager:
    """
    Manages source citations for research results.

    Features:
    - Deduplication by URL
    - Reliability scoring
    - Export to various formats
    """

    def __init__(self):
        self._citations: Dict[str, Citation] = {}

    def add(self, url: str, title: str, snippet: str = "") -> Citation:
        """Add or update a citation."""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        if url_hash in self._citations:
            return self._citations[url_hash]

        citation = Citation(url=url, title=title, snippet=snippet)
        citation.reliability_score = self._score_reliability(citation)
        self._citations[url_hash] = citation
        return citation

    def get(self, url: str) -> Optional[Citation]:
        """Get citation by URL."""
        url_hash = hashlib.md5(url.encode()).hexdigest()
        return self._citations.get(url_hash)

    def list_all(self) -> List[Citation]:
        """Get all citations sorted by reliability."""
        return sorted(
            self._citations.values(),
            key=lambda c: c.reliability_score,
            reverse=True,
        )

    def format_markdown(self) -> str:
        """Format citations as markdown."""
        lines = ["## Sources\n"]
        for i, c in enumerate(self.list_all(), 1):
            lines.append(f"{i}. [{c.title}]({c.url})")
            if c.snippet:
                lines.append(f"   > {c.snippet[:200]}...")
            lines.append(f"   - Accessed: {c.accessed_at}")
            lines.append(f"   - Reliability: {c.reliability_score:.1%}")
            lines.append("")
        return "\n".join(lines)

    def _score_reliability(self, citation: Citation) -> float:
        """Score citation reliability (0-1)."""
        score = 0.5
        if citation.https:
            score += 0.1
        # Boost known reliable domains
        reliable_domains = [
            "arxiv.org", "github.com", "docs.python.org",
            "stackoverflow.com", "wikipedia.org", "nature.com",
        ]
        if any(d in citation.domain for d in reliable_domains):
            score += 0.2
        return min(score, 1.0)
