"""Main research agent — search, extract, cite, and verify."""

from typing import Dict, List
from .safety import PromptInjectionDetector
from .citation import CitationManager


class ResearchAgent:
    """AI web research agent with safety controls."""

    def __init__(self):
        self.safety = PromptInjectionDetector()
        self.citations = CitationManager()

    def research(self, query: str, max_results: int = 5) -> Dict:
        """Research a topic and return cited results."""
        results = []
        pages = self._search(query, max_results)
        for page in pages:
            safety_check = self.safety.detect(page.get("content", ""))
            if safety_check["is_suspicious"]:
                continue
            citation = self.citations.add(url=page["url"], title=page["title"], snippet=page.get("content", "")[:200])
            results.append({"url": page["url"], "title": page["title"], "snippet": page.get("content", "")[:500], "citation": citation})
        return {"query": query, "results": results, "citations": self.citations.format_markdown(), "total_safe": len(results)}

    def _search(self, query: str, max_results: int) -> List[Dict]:
        """Search the web (placeholder — integrate with real search API)."""
        return [{"url": f"https://example.com/result{i}", "title": f"Result {i} for {query}", "content": f"Content about {query}..."} for i in range(max_results)]
