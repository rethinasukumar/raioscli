# agents/agent.py

import typer
from raioscli.agents.orchestrator import Orchestrator

agent_app = typer.Typer()

@agent_app.command()
def start():
    Orchestrator().start()

@agent_app.command()
def status():
    print("[RAIOS] Agent status")

@agent_app.command()
def stop():
    print("[RAIOS] Agent stopped")
