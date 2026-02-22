def analyze_complexity(code_data):
    print("Analyzing code complexity...")
    
    complexity_score = len(code_data["functions"]) * 5
    
    print(f"Estimated complexity score: {complexity_score}")
    
    return complexity_score
