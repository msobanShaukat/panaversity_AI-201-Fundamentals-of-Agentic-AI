import asyncio
import inspect

from planning_agent import PlanningAgent
from synthesis_agent import SynthesisAgent
from report_writer import ReportWriter
import research_agents  # import module to avoid symbol shadowing


class DeepResearchSystem:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.planner = PlanningAgent()
        self.synthesizer = SynthesisAgent()
        self.writer = ReportWriter()

    def _derive_dynamic_mode(self, query: str) -> str:
        q = (query or "").lower()
        if "just links" in q:
            return "just_links"
        if "summarise" in q or "summarize" in q:
            return "summarise"
        if "deeper" in q or "deep" in q:
            return "deeper"
        return "default"

    async def parallel_research(self, sub_tasks, instructions: dict):
        # Verify the loaded class and its constructor to avoid shadowing issues
        assert hasattr(
            research_agents, "ResearchAgent"
        ), f"research_agents module missing ResearchAgent (module at {getattr(research_agents,'__file__','?')})"
        sig = inspect.signature(research_agents.ResearchAgent.__init__)
        assert "idx" in sig.parameters, f"Loaded ResearchAgent has unexpected __init__ signature: {sig}"

        async def fetch(idx, q):
            persona = instructions.get("persona", {})
            city = persona.get("city")
            topic = persona.get("topic")
            q_aug = q
            if city and "local" in q.lower():
                q_aug = f"{q} (focus on {city})"
            if topic and "impact on" in q.lower():
                q_aug = f"{q} (tie to {topic})"
            ra = research_agents.ResearchAgent(idx=idx + 1)
            return await ra.async_search(q_aug, instructions)

        tasks = [fetch(i, q) for i, q in enumerate(sub_tasks)]
        return await asyncio.gather(*tasks)

    def run(self, query):
        print(f"\n[Lead] USER: {self.user_profile}")
        print(f"[Lead] Main Question: {query}\n")

        mode = self._derive_dynamic_mode(query)
        instructions = {
            "persona": {
                "name": self.user_profile.get("name"),
                "city": self.user_profile.get("city"),
                "topic": self.user_profile.get("interest"),
                "style": self.user_profile.get("style", "concise"),
            },
            "mode": mode,
            "model": "gpt-4o-mini",
            "temperature": 0.3,
            "summary_max_tokens": 150 if mode != "summarise" else 90,
        }

        sub_tasks = self.planner.plan(query, user_profile=self.user_profile)
        print(f"[Planner] Sub-questions: {sub_tasks}\n")
        print("[Lead] Launching parallel researchers...\n")
        results = asyncio.run(self.parallel_research(sub_tasks, instructions))

        refs_map = self.writer.build_refs_map(results)
        synthesis, conflict_list, conflict_expl = self.synthesizer.synthesize(
            results, instructions=instructions, refs_map=refs_map
        )

        if conflict_list:
            print("[Lead] Conflict detected between findings!\n")
            for c in conflict_list:
                print(f"[Conflict] {c}\n")

        print("[Lead] Writing report...\n")
        report = self.writer.write_report(
            query,
            synthesis,
            results,
            conflict_list,
            user_profile=self.user_profile,
            conflict_explanations=conflict_expl,
            refs_map=refs_map,
            mode=mode,
        )
        print(report)
