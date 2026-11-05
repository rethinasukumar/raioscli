# raioscli/agents/status.py

from pathlib import Path


def agent_status():
    print()
    print("RAIOS AGENT STATUS")
    print("-" * 40)

    components = [
        "controlplane.py",
        "dataplane.py",
        "orchestrator.py",
        "planner.py",
        "executor.py",
        "memory.py",
        "events.py",
    ]

    base_dir = Path(__file__).parent

    print()
    for component in components:
        status = "Ready" if (base_dir / component).exists() else "Missing"
        print(f"{component:<20} {status}")
