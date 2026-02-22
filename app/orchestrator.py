from analysis.parser import parse_repository
from analysis.complexity import analyze_complexity
from agents.architecture_agent import ArchitectureAgent
from agents.smell_agent import SmellAgent

class Orchestrator:
    def __init__(self, repo_url):
        self.repo_url = repo_url

    def run(self):
        print("Cloning and parsing repository...")
        
        code_data = parse_repository(self.repo_url)
        
        print("Analyzing complexity...")
        complexity_report = analyze_complexity(code_data)
        
        print("Running architecture agent...")
        architecture_agent = ArchitectureAgent()
        architecture_agent.analyze(code_data)
        
        print("Running smell detection agent...")
        smell_agent = SmellAgent()
        smell_agent.detect(code_data)
        
        print("Analysis complete!")
