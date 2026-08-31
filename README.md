<div align="center">

# 🌐 Safe Browser Researcher

### *AI web research agent with safety controls, evidence citations, and malicious page detection*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-Browser-2EAD33?style=for-the-badge)](https://playwright.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**Search, extract, cite, and detect — responsible AI web research**

</div>

---

## 📖 What is this?

An AI scraper that respects boundaries. It searches the web, extracts information, cites sources, and **detects malicious pages** — all while following robots.txt and privacy rules.

1. 🔍 **Search** — Query web search engines
2. 📄 **Extract** — Parse pages using accessibility tree (not visual clicking)
3. 📎 **Cite** — Every answer includes source URLs and timestamps
4. 🛡️ **Safety** — Detects prompt injection attempts in web content
5. 🤖 **Robots.txt** — Respects website access rules
6. ✅ **Verification** — Cross-references claims across multiple sources

> **Why this matters:** The 2026 roadmap explicitly states: "An AI scraper that ignores authorisation, privacy and website restrictions is not an advanced project; it is a liability."

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Accessibility Tree** | Uses a11y tree instead of CSS selectors (more robust) |
| **Evidence Citations** | Every claim linked to source URL + timestamp |
| **Prompt Injection Detection** | Identifies malicious instructions hidden in web pages |
| **robots.txt Compliance** | Checks and respects website access rules |
| **Source Deduplication** | Avoids processing same page twice |
| **Cross-Reference** | Validates claims across multiple sources |
| **Human Approval** | Sensitive actions require confirmation |

---

## 🚀 Quick Start

```bash
git clone https://github.com/faizansk25/safe-browser-researcher.git
cd safe-browser-researcher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium

python -m core.researcher --query "Latest Python 3.13 features"
```

---

## 📁 Project Structure

```
safe-browser-researcher/
├── core/
│   ├── researcher.py         # Main research agent
│   ├── search.py             # Web search
│   ├── extractor.py          # Page content extraction
│   ├── safety.py             # Prompt injection detection
│   ├── citation.py           # Source citation management
│   └── robots.py             # robots.txt compliance
├── browser/
│   ├── engine.py             # Playwright browser management
│   └── a11y.py               # Accessibility tree parser
├── tests/
│   ├── test_safety.py
│   ├── test_extractor.py
│   └── test_citations.py
├── requirements.txt
└── README.md
```

---

## 📚 References

- [Playwright Documentation](https://playwright.dev/)
- [OWASP Prompt Injection Prevention](https://owasp.org/www-community/prompt-injection)
- [Robots.txt Specification](https://www.robotstxt.org/)

---

## 👨‍💻 Author

**Faizan Muktar Shaikh**
- 🔗 [LinkedIn](https://linkedin.com/in/faizansk25) | [GitHub](https://github.com/faizansk25)
