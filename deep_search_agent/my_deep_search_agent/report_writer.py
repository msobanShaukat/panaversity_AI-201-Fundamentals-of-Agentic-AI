import re


class ReportWriter:
    def build_refs_map(self, results):
        refs, count = {}, 1
        for res in results or []:
            for url in res.get("sources", []):
                if url and url not in refs:
                    refs[url] = count
                    count += 1
        return refs

    def _inject_numeric_citations(self, text, refs_map):
        if not text or not refs_map:
            return text or ""
        def repl(m):
            url = m.group(1)
            n = refs_map.get(url)
            return f"[{n}]" if n else ""
        return re.sub(r"\[Source\]\(([^)]+)\)", repl, text)

    def write_report(
        self,
        main_question,
        synthesized_text,
        results=None,
        conflicts=None,
        user_profile=None,
        conflict_explanations="",
        refs_map=None,
        mode="default",
    ):
        header = "== Research Report ==\n"
        header += f"User: {user_profile}\n\n" if user_profile else ""
        header += f"Question: {main_question}\n\n"

        if conflicts:
            header += "**⚠️ Conflicts Detected:**\n"
            for conflict in conflicts:
                header += f"- {conflict}\n"
            header += "\n"

        if conflict_explanations:
            header += "**Conflict Explanations:**\n" + conflict_explanations + "\n\n"

        header += "=== Findings and Section Summaries ===\n"
        body = self._inject_numeric_citations(synthesized_text, refs_map or {})
        header += f"{body}\n"

        if mode == "just_links" and refs_map:
            header += "\n=== Just Links ===\n"
            for url, num in refs_map.items():
                header += f"- [{num}] {url}\n"

        if refs_map:
            header += "\n=== References ===\n"
            for url, num in refs_map.items():
                header += f"[{num}] {url}\n"

        header += "\n==== Summary ====\n"
        header += "Each section includes a synthesized, reader-friendly summary. Conflicts are explained above for decision maker insight.\n"
        return header
