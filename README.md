# Multi-Agent Orchestrator

Coordination framework for autonomous AI agents with task decomposition, tool use, and inter-agent messaging.

## Architecture

```
Planner Agent → decomposes goal into subtasks
Worker Agents → execute subtasks with tools
Supervisor    → monitors progress, handles failures
Message Bus   → async pub/sub between agents
```

## Quick start

```bash
pip install -r requirements.txt
python -m orchestrator run --goal "Research and summarize distributed consensus"
```

## License

MIT
