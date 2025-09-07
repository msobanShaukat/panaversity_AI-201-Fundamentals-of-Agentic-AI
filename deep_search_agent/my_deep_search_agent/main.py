from dotenv import load_dotenv
from deep_research_system import DeepResearchSystem

def main():
    load_dotenv()

    user_profile = {
        "name": "Muhammad Soban Shaukat",
        "city": "islamabad",
        "interest": "Agentic-AI",
        "style": "bullet-points",
    }

    # Try adding: "deeper", "summarise", or "just links" to test modes
    complex_query = (
        "Analyze the economic impact of remote work policies on small businesses vs large corporations, "
        "including productivity data and employee satisfaction trends"
    )

    system = DeepResearchSystem(user_profile)
    system.run(complex_query)

if __name__ == "__main__":
    main()
