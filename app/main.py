from fastapi import FastAPI
from app.engine import WorkflowEngine
from app.workflows import WORKFLOW_A

app = FastAPI()
engine = WorkflowEngine()

@app.post("/graph/create")
def create_graph():
    graph_id = engine.create_graph(
        nodes=WORKFLOW_A["nodes"],
        edges=WORKFLOW_A["edges"],
        start_node=WORKFLOW_A["start"]
    )
    return {"graph_id": graph_id}

@app.post("/graph/run")
def run_graph(graph_id: str, state: dict):
    run_id, final_state, log = engine.run_graph(graph_id, state)
    return {"run_id": run_id, "state": final_state, "log": log}

@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return engine.get_state(run_id)
