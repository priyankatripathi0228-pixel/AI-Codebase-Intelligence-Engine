from app.orchestrator import Orchestrator

def main():
    repo_url = input("Enter GitHub repository URL: ")
    
    orchestrator = Orchestrator(repo_url)
    orchestrator.run()

if __name__ == "__main__":
    main()
