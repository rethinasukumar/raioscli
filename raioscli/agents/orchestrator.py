from .controlplane import ControlPlaneAgent
from .dataplane import DataPlaneAgent


class Orchestrator:
    def __init__(self):
        self.controlplane = ControlPlaneAgent()
        self.dataplane = DataPlaneAgent()

    def start(self):
        print("[RAIOS] Starting orchestrator")
        self.controlplane.run()
        self.dataplane.run()
        print("[RAIOS] All agents started")

    def status(self):
        print("[RAIOS] Controlplane : Active")
        print("[RAIOS] Dataplane    : Active")
