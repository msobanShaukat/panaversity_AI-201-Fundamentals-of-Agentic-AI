import os
import aiohttp
import asyncio
import logging
from tavily import TavilyClient

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

HIGH_QUALITY_DOMAINS = [
    ".gov", ".edu",
    "nytimes.com", "bbc.com", "reuters.com", "theguardian.com",
    "nature.com", "sciencedirect.com", "washingtonpost.com", "forbes.com",
    "wsj.com", "theatlantic.com", "cnn.com", "npr.org", "harvard.edu",
]

MEDIUM_QUALITY_DOMAINS = [
    ".org", "wikipedia.org", "medium.com", "forbes.com",
]


def rate_source_quality(url):
    url = (url or "").lower()
    for domain in HIGH_QUALITY_DOMAINS:
        if domain in url:
            return "High"
    for domain in MEDIUM_QUALITY_DOMAINS:
        if domain in url:
            return "Medium"
    return "Low"


def _quality_weight(q: str) -> int:
    return {"High": 5, "Medium": 3, "Low": 1}.get(q or "Low", 1)


def _maybe_filter_low(findings):
    non_low = [f for f in findings if (f.get("quality") or "Low") != "Low"]
    # Keep only non-low if we have at least 3 non-low; otherwise return all
    if len(non_low) >= 3:
        return non_low
    return findings


class ResearchAgent:
    def __init__(self, idx):
        self.idx = idx
        tavily_key = os.getenv("TAVILY_API_KEY")
        if not tavily_key:
            raise ValueError("TAVILY_API_KEY missing from environment variables or .env")
        self.client = TavilyClient(api_key=tavily_key)

    async def async_search(self, question, dynamic_instructions=None):
        logging.info(f"[ResearchAgent-{self.idx}] Searching: {question}")
        try:
            mode = (dynamic_instructions or {}).get("mode", "default")
            if mode == "deeper":
                max_results = 8
            elif mode == "summarise":
                max_results = 3
            elif mode == "just_links":
                max_results = 5
            else:
                max_results = 5

            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(
                None, lambda: self.client.search(query=question, max_results=max_results)
            )

            if not results.get("results"):
                logging.warning(f"[ResearchAgent-{self.idx}] No results for query: {question}")
                return {
                    "agent": self.idx,
                    "question": question,
                    "summaries": [],
                    "findings": [{"text": "No relevant findings found.", "url": "", "quality": "Low"}],
                    "sources": [],
                }

            findings, summaries, sources = [], [], []
            for r in results.get("results", []):
                url = r.get('url', '')
                snippet = (r.get('content') or '')[:500].replace('\n', ' ').strip()
                quality = rate_source_quality(url)
                logging.info(f"[RA-{self.idx}] {snippet} [{url}] [{quality}]")
                await asyncio.sleep(0.2)
                findings.append({"text": snippet, "url": url, "quality": quality})
                summaries.append(snippet)
                sources.append(url)

            # Sort by stronger weights then optionally filter low-quality
            findings.sort(key=lambda f: _quality_weight(f.get("quality")), reverse=True)
            findings = _maybe_filter_low(findings)

            if not findings:
                findings = [{"text": "No relevant findings found.", "url": "", "quality": "Low"}]

            return {
                "agent": self.idx,
                "question": question,
                "summaries": summaries,
                "findings": findings,
                "sources": sources,
            }

        except aiohttp.ClientError as e:
            logging.error(f"[ResearchAgent-{self.idx}] Network error: {str(e)}")
            return {
                "agent": self.idx,
                "question": question,
                "summaries": [],
                "findings": [{"text": f"Network error occurred: {str(e)}", "url": "", "quality": "Low"}],
                "sources": [],
            }
        except Exception as e:
            logging.error(f"[ResearchAgent-{self.idx}] Unexpected error: {str(e)}")
            return {
                "agent": self.idx,
                "question": question,
                "summaries": [],
                "findings": [{"text": "Unexpected error occurred.", "url": "", "quality": "Low"}],
                "sources": [],
            }
