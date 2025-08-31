from dotenv import load_dotenv
from deep_research_system import DeepResearchSystem

def main():
    load_dotenv()
    system = DeepResearchSystem()
    system.run("What is renewable energy?")

if __name__ == "__main__":
    main()
