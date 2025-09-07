# 🚀 AI-Powered Multi-Agent Research Assistant

🕵️‍♂️ Deep Research Agent System

https://img.shields.io/badge/python-3.10%252B-blue

https://img.shields.io/badge/License-MIT-yellow.svg

https://img.shields.io/badge/code%2520style-black-000000.svg

https://img.shields.io/badge/asyncio-ready-green

https://img.shields.io/badge/API-Gemini-FF6F00.svg

https://img.shields.io/badge/Search-Tavily-4A154B.svg


A sophisticated multi-agent framework for automated, in-depth research and personalized report generation 🔍✨

The Deep Research Agent System is a powerful AI-driven framework that performs comprehensive research on complex topics using a team of specialized autonomous agents. It plans research strategies, gathers real-time information from the web, and synthesizes findings into structured, citation-rich reports tailored to user preferences.

## 🌟 Overview
Welcome to the **AI-Powered Multi-Agent Research Assistant**! 
This is a sophisticated system that leverages a team of specialized AI agents to perform deep, multi-faceted research on complex topics. It automates the entire workflow from deconstructing a query to conducting parallel research, detecting and resolving informational conflicts, and compiling a final, comprehensive report.

This system is designed to handle ambiguity and provide nuanced insights that a single-pass search would miss.

## 🛠️ How to Set Up and Run Follow these steps to get your multi-agent research team up and running.

### **Prerequisites***   Python 3.13+
*   A package manager like `pip`
*   **Google API Key**: For accessing the Gemini API for synthesis and conflict resolution.
*   **Tavily API Key**: For the advanced web search capabilities of the research agents.

### **Installation & Setup**1.  **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd my_deep_search_agent
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    Create a `requirements.txt` file with the following content:
    ```
    python-dotenv
    google-generativeai
    sentence-transformers
    scikit-learn
    tavily-python
    aiohttp
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables**:
    Create a file named `.env` in the project root and add your API keys:
    ```env
    GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
    TAVILY_API_KEY="YOUR_TAVILY_API```Y"
    ```

### **Run the System**Execute the main script from your terminal:
```bash
python main.py
```
The system will then begin the research process, and a final markdown report will be saved in the project directory.

## 💡 Example Research Questions This system excels at handling complex, open-ended questions like:

*   "Compare the environmental impact of electric vs. hybrid vs. gas cars, considering their full lifecycle from manufacturing to disposal."
*   "Analyze the economic impact of remote work policies on small businesses versus large corporations, including productivity data and employee satisfaction trends."
*   "Investigate the role of agentic AI in the future of autonomous vehicles, focusing on safety, efficiency, and ethical considerations."

## 🤖 The Agent Team: What Each Agent Does The system's power comes from a team of specialized agents, each with a distinct role.

| Agent Name | Role | Description |
| :--- | :--- | :--- |
| 🎩 **Lead Agent** | **Orchestration** | Implicitly run from `deep_research_system.py`, it manages the entire workflow from receiving the user's query to delivering the final report. |
| 🗺️ **Planning Agent** | **Task Decomposition** | Takes the high-level user query and breaks it down into several detailed, researchable sub-questions to ensure comprehensive coverage. |
| 🕵️ **Research Agents** | **Information Gathering** | A team of agents that work in parallel. Each agent takes one sub-question and uses the Tavily API to perform an advanced web search, gathering relevant articles and data. |
| 🧩 **Synthesis Agent** | **Analysis & Conflict Detection** | Aggregates all findings from the research agents. It then uses semantic analysis to compare the pieces of information and identify potential contradictions or conflicts. |
| ⚖️ **Conflict Resolver** | **Intelligent Resolution** | When conflicts are detected, this agent takes the contradictory findings and uses the Gemini LLM to generate a new, synthesized statement that reconciles the disagreement. |
| ✍️ **Report Writer** | **Report Compilation** | Assembles all the processed information—including the original findings, conflict explanations, and reconciled statements—into a single, well-structured, and cited markdown report. |

## 🤝 How the Team Coordinates The agents follow a structured, sequential workflow to ensure a high-quality output.

1.  **Input & Planning**: The `main.py` script captures the user's complex query. The **Planning Agent** then deconstructs it into multiple, focused sub-questions.
2.  **Parallel Research**: The system launches multiple **Research Agents** simultaneously. Each agent is assigned one sub-question and works independently to find relevant information. User profile details (like interests and location) are used to personalize the search.
3.  **Aggregation & Synthesis**: The **Synthesis Agent** collects the findings from all researchers. It uses sentence transformers to perform semantic analysis, identifying pairs of findings that may be contradictory.
4.  **Conflict Resolution**: For each conflict detected, the **Conflict Resolver** is activated. It sends the two conflicting statements to the Gemini LLM and prompts it to generate a new, reconciled statement that bridges the gap between the two.
5.  **Final Reporting**: The **Report Writer** takes all the components—the original research findings, the list of detected conflicts, and the newly generated reconciled statements—and assembles them into the final `README.md` report, complete with source citations.










