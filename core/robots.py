"""robots.txt compliance checker."""

from urllib.parse import urlparse
from typing import Optional


class RobotsChecker:
    """Check robots.txt before accessing URLs."""

    def __init__(self):
        self._cache = {}

    def can_fetch(self, url: str, user_agent: str = "*") -> bool:
        """Check if we're allowed to access this URL."""
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        if robots_url not in self._cache:
            self._cache[robots_url] = self._fetch_robots(robots_url)
        rules = self._cache[robots_url]
        path = parsed.path
        for disallow in rules.get("disallow", []):
            if path.startswith(disallow):
                return False
        return True

    def _fetch_robots(self, robots_url: str) -> dict:
        """Fetch and parse robots.txt."""
        try:
            import requests
            resp = requests.get(robots_url, timeout=5)
            disallow = []
            for line in resp.text.split("\n"):
                if line.lower().startswith("disallow:"):
                    path = line.split(":", 1)[1].strip()
                    if path:
                        disallow.append(path)
            return {"disallow": disallow}
        except Exception:
            return {"disallow": []}
