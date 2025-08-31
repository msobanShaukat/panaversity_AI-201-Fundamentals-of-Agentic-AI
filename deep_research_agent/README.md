# 🔍 Deep Research Agentic System 🚀

[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Agentic AI](https://img.shields.io/badge/agentic%20AI-ready-brightgreen)](#)
[![Tavily](https://img.shields.io/badge/search-Tavily_API-ff69b4)](https://tavily.com/)

---

## 🎯 **Project Overview**

A sophisticated multi-agent AI research system that autonomously decomposes complex questions, conducts comprehensive web research, synthesizes findings from multiple perspectives, and generates professionally formatted reports with complete citations. Built with modular architecture for extensibility and performance.

---

## 🗂️ **System Architecture**

```
[User Question]
      │
      ▼
┌──────────────┐
│   Lead Agent │ (Orchestrates workflow)
└──────┬───────┘
       │
   Decomposes Question
       │
       ▼
┌───────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ PlanningAgent │ ───→ │ ResearchAgents  │ ───→ │ ResearchAgents  │
└──────┬────────┘      └─────────────────┘      └─────────────────┘
       │              (Parallel Research)      (Source Validation)
       │
       ▼
┌───────────────┐
│SynthesisAgent │ (Combines & Organizes Findings)
└──────┬────────┘
       │
       ▼
┌──────────────┐
│ ReportWriter │ (Professional Formatting)
└──────────────┘
       │
       ▼
[Final Research Report with Citations]
```

---

## 📁 **File Structure**

```
deep-research-system/
├── main.py                 # 🟢 Main entry point
├── deep_research_system.py # 🧠 Lead coordination agent
├── planning_agent.py       # 🗺️ Question decomposition
├── research_agents.py      # 🔎 Web research & fact-checking
├── synthesis_agent.py      # 🧩 Multi-perspective synthesis
├── report_writer.py        # 📝 Professional report generation
├── .env                    # 🔑 API keys (gitignored)
├── requirements.txt        # 📦 Python dependencies
├── pyproject.toml          # 🛠️ Project configuration
├── uv.lock                 # 🔒 Dependency locking
└── README.md               # 📚 This documentation
```

---

## ⚡ **Key Features**

- **🧩 Modular Multi-Agent Architecture** - Easily extensible agent system
- **🔍 Intelligent Web Research** - Real-time information retrieval with source validation
- **📊 Multi-Perspective Analysis** - Examines questions from environmental, economic, and technological viewpoints
- **📝 Professional Reporting** - Fully formatted reports with proper citations
- **⚡ Parallel Processing** - Efficient research across multiple sub-questions
- **🛡️ Source Quality Assessment** - Automatic evaluation of information credibility

---

## 🚀 **Quick Start**

### 1. **Installation & Setup**

```bash
# Clone the repository
git clone https://github.com/msobanShaukat/panaversity_AI-201-Fundamentals-of-Agentic-AI.git
cd deep_research_agent

# Install dependencies (using uv)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 2. **API Configuration**

Create a `.env` file with your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key_here
OPENAI_API_KEY=your_openai_api_key_optional
```

### 3. **Run the System**

```bash
# Basic execution
uv run python main.py

# With custom question
uv run python main.py "Your research question here"
```

---

## 📊 **Sample Output**

```
====== RESEARCH REPORT ======

== Research Report ==
Question: What is renewable energy?

### Environmental Impact Perspective
• Renewable energy sources have significant environmental considerations that stakeholders must evaluate
• Initial site assessments are crucial before renewable energy project implementation
• Compared to fossil fuels, renewables offer major advantages in reduced CO2 and GHG emissions

### Economic Perspective  
• Renewable energy creates domestic energy independence and reduces fossil fuel imports
• Economic potential represents the subset of technical potential where generation costs are competitive
• Renewable resources provide long-term economic stability due to their inexhaustible nature

### Technological Perspective
• Solar energy efficiency and affordability have dramatically improved in recent years
• Wind energy technology has seen significant advancements making it more viable
• Battery technology improvements have enhanced energy storage capabilities
• Green hydrogen and other emerging technologies promise future breakthroughs

### Sources
1. https://www.adecesg.com/resources/blog/environmental-impacts-of-renewable-energy-sources/
2. https://www.nrel.gov/gis/re-econ-potential
3. https://green.org/2024/03/07/unlocking-the-future-the-latest-advances-in-renewable-energy/
4. https://nap.nationalacademies.org/read/12987/chapter/6

=============================
```

---

## 🧠 **Agent Capabilities**

### **🤖 Lead Coordinator Agent**
- Orchestrates the entire research workflow
- Manages agent communication and task delegation
- Monitors research progress and quality control

### **🗺️ Planning Agent**
- Decomposes complex questions into researchable sub-questions
- Identifies key perspectives for comprehensive analysis
- Optimizes research strategy for efficiency

### **🔎 Research Agents**
- Conduct parallel web research across multiple sources
- Perform source credibility assessment and validation
- Extract relevant information with proper citation tracking

### **🧩 Synthesis Agent**
- Integrates findings from multiple research threads
- Identifies patterns, conflicts, and consensus across sources
- Organizes information into coherent thematic structures

### **📝 Report Writer**
- Generates professionally formatted research reports
- Ensures proper citation and source attribution
- Creates executive summaries and key findings sections

---

## 🧪 **Example Research Questions**

- **🌍** "What are the impacts of climate change on coastal cities?"
- **💡** "How is artificial intelligence transforming healthcare diagnostics?"
- **🚀** "What are the latest advancements in quantum computing?"
- **🌱** "Compare sustainable agriculture practices across different regions"
- **📱** "How will 6G technology differ from current 5G networks?"

---

## 🛠️ **Customization & Extension**

### **Agent Enhancements**
```python
# Add custom research agents
class CustomResearchAgent(BaseResearchAgent):
    def research(self, query: str) -> List[ResearchResult]:
        # Your custom research logic
        pass
```

### **Source Quality Rules**
```python
# Enhance source validation
def enhance_quality_assessment(url: str, content: str) -> QualityScore:
    # Add domain authority checking, fact-checking, etc.
    return quality_score
```

### **Parallel Processing**
```python
# Enable true parallelism
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(research_agent.research, sub_questions))
```

---

## 👨‍💻 **Development Team**

- **Muhammad Soban Shaukat** 

---

## 📄 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🆘 **Troubleshooting**

### **Common Issues**
1. **API Key Errors** - Ensure your Tavily API key is correctly set in the `.env` file
2. **Dependency Issues** - Use `uv sync` or `pip install -r requirements.txt`
3. **Network Problems** - Check your internet connection and firewall settings

### **Performance Tips**
- Use quality internet connection for faster research
- Consider API rate limits when making multiple requests
- Monitor system resources during extensive research tasks

---

## 🌟 **Future Enhancements**

- [ ] **Multi-language Support** - Research in various languages
- [ ] **Advanced Visualization** - Charts and graphs in reports
- [ ] **Real-time Collaboration** - Multiple users contributing to research
- [ ] **Domain-specific Agents** - Specialized agents for technical fields
- [ ] **Offline Capabilities** - Cached research for faster results

---

**Empowering research through intelligent agent collaboration!** 🎓✨

*For questions or contributions, please open an issue or submit a pull request.*

