"""Page content extraction using accessibility tree."""

from typing import Dict, Optional


class ContentExtractor:
    """Extract clean content from web pages."""

    def extract_from_url(self, url: str) -> Dict:
        """Extract text content from a URL."""
        try:
            import requests
            from bs4 import BeautifulSoup
            resp = requests.get(url, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            for tag in soup(["script", "style", "nav", "footer"]):
                tag.decompose()
            return {"url": url, "title": soup.title.string if soup.title else "", "content": soup.get_text(strip=True)[:5000], "success": True}
        except Exception as e:
            return {"url": url, "title": "", "content": "", "success": False, "error": str(e)}

    def extract_text(self, html: str) -> str:
        """Extract clean text from HTML."""
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()
        return soup.get_text(strip=True)
