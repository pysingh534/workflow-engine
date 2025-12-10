def extract_functions(state):
    code = state.get("code", "")
    functions = [line for line in code.split("\n") if line.strip().startswith("def ")]
    state["functions"] = functions
    return state

def check_complexity(state):
    funcs = state.get("functions", [])
    state["complexity"] = len(funcs) * 2
    return state

def detect_issues(state):
    state["issues"] = max(0, 5 - state.get("complexity", 0))
    return state

def suggest_improvements(state):
    issues = state.get("issues", 0)
    state["quality_score"] = 10 - issues
    return state

def loop_condition(state):
    return "suggest_improvements" if state["quality_score"] < state.get("threshold", 8) else None


WORKFLOW_A = {
    "nodes": {
        "extract": extract_functions,
        "complexity": check_complexity,
        "issues": detect_issues,
        "suggest_improvements": suggest_improvements
    },
    "edges": {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "suggest_improvements",
        "suggest_improvements": loop_condition
    },
    "start": "extract"
}
