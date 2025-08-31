from planning_agent import PlanningAgent
from research_agents import ResearchAgent
from synthesis_agent import SynthesisAgent
from report_writer import ReportWriter

class DeepResearchSystem:
    def __init__(self):
        self.planner = PlanningAgent()
        self.researcher = ResearchAgent()
        self.synthesizer = SynthesisAgent()
        self.writer = ReportWriter()

    def run(self, question):
        print("\n[Lead] Received main question:", question)
        sub_questions = self.planner.plan(question)
        print("[Lead] Broke into subquestions:", sub_questions)
        research_results = []
        for subq in sub_questions:
            print(f"[Lead] Assigning: {subq}")
            findings = self.researcher.search(subq)
            research_results.append(findings)
        print("[Lead] Synthesizing all findings...")
        insights = self.synthesizer.synthesize(research_results)
        print("[Lead] Writing final report...")
        report = self.writer.write_report(question, insights)
        print("\n====== RESEARCH REPORT ======\n")
        print(report)
        print("\n=============================\n")
