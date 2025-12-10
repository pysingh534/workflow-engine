from typing import Dict, Callable, Any, List
import uuid

class WorkflowEngine:
    def __init__(self):
        self.graphs: Dict[str, Dict] = {}
        self.runs: Dict[str, Dict] = {}

    def create_graph(self, nodes: Dict[str, Callable], edges: Dict, start_node: str):
        graph_id = str(uuid.uuid4())
        self.graphs[graph_id] = {
            "nodes": nodes,
            "edges": edges,
            "start": start_node
        }
        return graph_id

    def run_graph(self, graph_id: str, state: Dict[str, Any]):
        run_id = str(uuid.uuid4())
        log: List[str] = []

        graph = self.graphs[graph_id]
        current = graph["start"]

        while current is not None:
            node_fn = graph["nodes"][current]
            state = node_fn(state)
            log.append(f"Executed: {current} | state={state}")

            nxt = graph["edges"].get(current)
            if callable(nxt):
                current = nxt(state)
            else:
                current = nxt

        self.runs[run_id] = {"state": state, "log": log}
        return run_id, state, log

    def get_state(self, run_id: str):
        return self.runs.get(run_id, {})
