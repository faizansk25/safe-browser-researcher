"""Playwright browser engine for web research."""

from typing import Dict, Optional


class BrowserEngine:
    """Manages Playwright browser sessions."""

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser = None

    async def start(self):
        """Start browser session."""
        try:
            from playwright.async_api import async_playwright
            self.pw = await async_playwright().start()
            self.browser = await self.pw.chromium.launch(headless=self.headless)
        except Exception as e:
            print(f"Browser start failed: {e}")

    async def navigate(self, url: str) -> Dict:
        """Navigate to URL and return page content."""
        if not self.browser:
            return {"error": "Browser not started"}
        page = await self.browser.new_page()
        await page.goto(url)
        content = await page.content()
        title = await page.title()
        await page.close()
        return {"url": url, "title": title, "content": content[:5000]}

    async def stop(self):
        """Stop browser session."""
        if self.browser:
            await self.browser.close()
        if hasattr(self, "pw"):
            await self.pw.stop()
