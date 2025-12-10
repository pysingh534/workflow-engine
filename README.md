# workflow-engine
A minimal agent workflow engine supporting state management, conditional branching, and looping.

## Features
- Node-based execution
- Shared state between nodes
- Conditional branching
- Looping based on state
- Simple tool registry
- FastAPI endpoints to create and run workflows

## Endpoints
### POST /graph/create
Creates the example workflow.

### POST /graph/run
Runs a graph using graph_id and initial state.

### GET /graph/state/{run_id}
Returns stored state of any run.

## Run Locally
bashpip install -r requirements.txt\
uvicorn app.main:app --reload\
Visit http://localhost:8000/docs for API documentation.
