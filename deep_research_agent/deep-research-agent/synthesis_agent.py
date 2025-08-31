class SynthesisAgent:
    def synthesize(self, research_results):
        full = []
        for res in research_results:
            full.append(f"\n### {res['question']}\n")
            for finding in res["findings"]:
                full.append("• " + finding)
        return "\n".join(full)
