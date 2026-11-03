from raioscli.agents.controlplane import ControlPlaneAgent
from raioscli.agents.dataplane import DataPlaneAgent
from raioscli.agents.orchestrator import Orchestrator


def test_controlplane_agent(capsys):
    agent = ControlPlaneAgent()
    agent.run()

    captured = capsys.readouterr()
    assert "[RAIOS] Controlplane agent running" in captured.out


def test_dataplane_agent(capsys):
    agent = DataPlaneAgent()
    agent.run()

    captured = capsys.readouterr()
    assert "[RAIOS] Dataplane agent running" in captured.out


def test_orchestrator(capsys):
    orchestrator = Orchestrator()
    orchestrator.start()

    captured = capsys.readouterr()

    assert "[RAIOS] Controlplane agent running" in captured.out
    assert "[RAIOS] Dataplane agent running" in captured.out
