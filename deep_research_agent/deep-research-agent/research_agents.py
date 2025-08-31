import os
from tavily import TavilyClient

def rate_source_quality(url):
    url = url.lower()
    if url.endswith('.gov') or url.endswith('.edu') or url.endswith('.org'):
        return "High"
    elif url.endswith('.com'):
        return "Medium"
    else:
        return "Low"

class ResearchAgent:
    def __init__(self):
        tavily_key = os.getenv("TAVILY_API_KEY")
        if not tavily_key:
            raise ValueError("TAVILY_API_KEY missing from .env")
        self.tavily_client = TavilyClient(api_key=tavily_key)

    def search(self, question):
        print(f"[ResearchAgent] Searching for: {question}")
        response = self.tavily_client.search(query=question, max_results=3)
        findings = []
        sources = []
        for r in response.get("results", []):
            summary = r["content"][:400].strip().replace('\n', ' ')
            findings.append(f"{summary} [{r['url']}] (Quality: {rate_source_quality(r['url'])})")
            sources.append(r["url"])
        if not findings:
            findings = ["No relevant research found."]
        return {
            "question": question,
            "findings": findings,
            "sources": sources
        }
