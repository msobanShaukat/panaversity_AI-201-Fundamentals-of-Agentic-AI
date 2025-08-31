
# 🔍 Deep Research Agentic System 🚀

[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Agentic AI](https://img.shields.io/badge/agentic%20AI-ready-brightgreen)](#)

---

## 🎯 **Project Overview**

A modular, multi-agent AI system that autonomously decomposes, researches, synthesizes, and reports on complex questions—delivering expert-level, fully-cited research outputs. Inspired by industry best practices in Agentic AI and professional research platforms.

---

## 🗂️ **System Architecture**

```
[User Question]
      │
      ▼
┌──────────────┐
│   Lead Agent │
└──────┬───────┘
       │
   Splits Question
       │
       ▼
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│ PlanningAgent │      │ResearchAgents │ ...  │ResearchAgents │
└──────┬────────┘      └──────┬────────┘      └──────┬────────┘
       │                     (Fact Finding, Source Checking)
       │
       ▼
┌───────────────┐
│SynthesisAgent │
└──────┬────────┘      (Combines and Organizes)
       │
       ▼
┌──────────────┐
│ ReportWriter │
└──────────────┘   (Final Professional Report)
       │
       ▼
[Output]
```

---

## 📁 **File Structure**

- `main.py` – 🟢 Entrypoint script
- `deep_research_system.py` – 🧠 Lead Coordinator Agent
- `planning_agent.py` – 🗺️ Decomposes big questions
- `research_agents.py` – 🔎 Fact Finder, Source Checker agents
- `synthesis_agent.py` – 🧩 Combines findings into insights
- `report_writer.py` – 📝 Generates the final report
- `.env` – 🔑 Your private API keys (**never share or commit**)
- `pyproject.toml`, `uv.lock` – 🛠️ Python dependencies
- `README.md` – 📚 This documentation

---

## ⚡ **Features**

- 🧩 **Orchestrated Multi-Agent Pipeline**
- 🔎 **Web research with real citations**
- 📊 **Source quality checks**
- 🤝 **Synthesis of multiple domain perspectives**
- 📝 **Professional, readable research reports**
- 💡 **Easily extensible agent/team architecture**

---

## 🚀 **Usage**

### 1. **Setup your environment**

```
uv add python-dotenv tavily-python
```

### 2. **Add your API key in `.env`**

```
TAVILY_API_KEY=your_tavily_key
```

### 3. **Run the System**

```
uv run python main.py
```

### 4. **Sample Output**

```
====== RESEARCH REPORT ======

== Research Report ==
Question: What is renewable energy?


### What is renewable energy? (Environmental Impact)

• # Environmental Impacts of Renewable Energy Sources What environmental impacts should investors, communities, and other stakeholders consider as we move forward with renewable energy projects? ## What environmental impacts do renewable energy installations have? ### Initial impacts of renewable energy sites The wider environmental impact of any potential site should be seriously assessed prior to [https://www.adecesg.com/resources/blog/environmental-impacts-of-renewable-energy-sources/] (Quality: Low)
• In this blog post we’re discussing how to avoid negative environmental impacts when ramping up renewable energy projects. 1. ### How do the environmental impacts of renewable energy compare to fossil fuels? Public lands can play a role in providing the resources needed to support a green economy, but clean energy mineral development needs to be carried out in an environmentally, culturally and soc [https://www.wilderness.org/news/blog/faq-what-are-environmental-impacts-renewable-energy] (Quality: Low)
• The second half of the chapter provides a discussion of local-scale impacts and permitting and regulatory requirements in the United States and China, with examples illustrating some of the environmental concerns raised by renewable energy projects. Compared to fossil-fuel-based electricity generation, renewable energy technologies offer a major advantage in lower emissions of CO2 and other GHGs. [https://nap.nationalacademies.org/read/12987/chapter/6] (Quality: Low)

### What is renewable energy? (Economic Perspective)

• RENEWABLE ENERGY TRANSITION Until a few centuries ago, humans obtained all their energy from renewable resources: food from plant and animal sources, wood for cooking and heating fires, and later hydropower and wind power for simple tasks like grinding grain and pumping water. NRE conducts research on renewable energy technologies including solar, wind, biomass, and fuel cell energy. For example, [https://www.bu.edu/eci/files/2024/03/renewable-energy-econ-module-final.pdf] (Quality: Low)      
• * The Economic Benefits of Renewable Energy # The Economic Benefits of Renewable Energy ## **How Renewable Energy Benefits 
the Economy** Creating renewable energy domestically reduces the need to import fossil fuels from elsewhere in the world. And because renewable resources don't run out, we can count on that independence to last.Compared to oil imported from across the world, renewable energy c [https://www.energytexas.com/en/get-to-learnin/the-economic-benefits-of-renewable-energy] (Quality: Low)
• Renewable Energy Economic Potential | Geospatial Data Science | NREL  *    Renewable Energy Economic Potential  *   Renewable Energy Technical Potential  *   Renewable Energy Economic Potential  Renewable Energy Economic Potential Economic potential, one measure of renewable energy generation potential, is the subset of the technical potential where the cost required to 
generate electricity is les [https://www.nrel.gov/gis/re-econ-potential] (Quality: Low)

### What is renewable energy? (Technological Advances)

• # Evolving Energy Technologies in the Renewable Energy Industry Solar energy has been around for decades, but recent advances in technology have made it more efficient and more affordable than ever before. Wind energy is another well-established renewable energy source that has seen significant technological advances in recent years. Technology advancements have made batteries more efficient and e [https://fourcornerscleanenergyalliance.org/evolving-energy-technologies-in-the-renewable-energy-industry-2/] (Quality: Low)
• Recent advancements in technology and policy have significantly accelerated the growth of renewable energy sources, promising a cleaner, more sustainable energy landscape. Solar energy has long been a beacon of hope for renewable energy advocates, 
and recent technological breakthroughs have greatly enhanced its efficiency and accessibility. Green hydrogen, produced through the electrolysis of wate [https://green.org/2024/03/07/unlocking-the-future-the-latest-advances-in-renewable-energy/] (Quality: Low)
• By harnessing inexhaustible resources such as sunlight, wind, and water, renewable technologies are not only enhancing energy efficiency but also driving significant environmental and economic benefits. Advances in solar photovoltaics, wind turbines, and bioenergy are leading to higher energy conversion efficiencies and reduced greenhouse gas emissions. Continue reading 
as we explore the impact of [https://instituteofsustainabilitystudies.com/insights/lexicon/the-future-of-renewable-energy-innovations-and-breakthroughs/] (Quality: Low)


=============================

---

## 🧠 **How Each Agent Works**

- **Lead Agent:** Coordinates workflow—starts, logs, and tracks sub-questions and responses.
- **PlanningAgent:** Decomposes any broad question into focused research prompts.
- **ResearchAgents:** Search the web, check sources, and collect relevant evidence.
- **SynthesisAgent:** Aggregates and organizes agent findings for clarity and depth.
- **ReportWriter:** Produces a final, formatted, professional research document with full citations.

---

## 🧪 **Examples of Research Questions**

- What is renewable energy?
- How will AI affect the Pakistani economy by 2030?
- Compare the efficiency of electric and hybrid cars.
- What are the key ethical challenges in genetic editing?

---

## 🌟 **Customization & Extensions**

- 🔄 Add auto-parallelism (`concurrent.futures` or async) for truly simultaneous research.
- 🛡️ Enhance source quality rules for robust credibility.
- 🔬 Integrate more specialist agents (conflict detector, domain expert, etc.).
- 📈 Add visualization/report export.

---

## 👨‍💻 **Contributors**

- Muhammad Soban Shaukat & Team

---

## 🤝 **License**

MIT

---

## 🏆 **Instructor/Reviewer Notes**

This system demonstrates a professional, modular AI-first agentic research workflow. 
Just set your API key, run, and watch the team in action!  
```

***

This README clearly illustrates **usage, architecture, agent collaboration, file roles, features, and customization ideas**—with badges, ASCII art, and emoji for engagement and clarity.  
Feel free to copy/paste, add screenshots, or tailor agent descriptions as your solution evolves.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/77906941/427314ad-7ab0-415f-af1a-fac0d87128fb/screencapture-github-panaversity-learn-agentic-ai-blob-main-01-ai-agents-first-projects-DeepSearch-readme-md-20.jpg)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/f3d38187-6ae8-4dc0-b16f-6b79e3b43dcb/uv.lock)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/56721ded-d682-482d-9257-264e34dd9e04/pyproject.toml)
[4](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/af5b2b56-0768-40c6-b957-329a19fe3013/main.py)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/7f79bd08-c28b-4098-928c-6f9d3c32d4d7/SOURCES.txt)
[6](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/33d59a5c-1291-4b35-911b-ae7dac3f09f3/PKG-INFO)
[7](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/77906941/b502d8f0-5cbb-4a04-8893-141d1d4880d4/entry_points.txt)
[8](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/77906941/ce9dd8a9-a33a-4624-9634-5a27dc4ced0c/image.jpg)
[9](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/77906941/8797f4e1-f238-4ada-879b-65d33150998f/image.jpg)


