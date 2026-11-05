# raioscli/agents/orchestrator.py

from datetime import datetime

from .controlplane import ControlPlaneAgent
from .dataplane import DataPlaneAgent


class Orchestrator:
    """
    RAIOS Agent Orchestrator

    Responsible for:
    - Agent lifecycle
    - Coordination
    - Planning
    - Event tracking
    - Runtime status
    """

    def __init__(self):
        self.controlplane = ControlPlaneAgent()
        self.dataplane = DataPlaneAgent()

        self.started = False
        self.started_at = None

        self.events = []
        self.plan = [
            "controlplane-check",
            "dataplane-check",
            "cluster-sync"
        ]

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def emit(self, event):
        timestamp = datetime.utcnow().isoformat()

        self.events.append({
            "time": timestamp,
            "event": event
        })

        print(
            f"[RAIOS][EVENT] "
            f"{timestamp} "
            f"{event}"
        )

    # --------------------------------------------------
    # Start
    # --------------------------------------------------

    def start(self):
        if self.started:
            print(
                "[RAIOS] Orchestrator already running."
            )
            return

        self.started = True
        self.started_at = datetime.utcnow()

        print()
        print("[RAIOS] Starting orchestrator...")
        print()

        self.emit("ORCHESTRATOR_START")

        print("[RAIOS] Running Controlplane Agent")
        self.controlplane.run()
        self.emit("CONTROLPLANE_COMPLETE")

        print()

        print("[RAIOS] Running Dataplane Agent")
        self.dataplane.run()
        self.emit("DATAPLANE_COMPLETE")

        print()

        self.emit("ORCHESTRATION_COMPLETE")

        print(
            "[RAIOS] Orchestration complete."
        )

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def status(self):
        print()
        print("RAIOS AGENT STATUS")
        print("-" * 40)

        print(
            f"Running      : "
            f"{self.started}"
        )

        print(
            f"Started At   : "
            f"{self.started_at}"
        )

        print(
            f"Plan Size    : "
            f"{len(self.plan)}"
        )

        print(
            f"Events       : "
            f"{len(self.events)}"
        )

        print()

        print("Current Plan")
        print("-" * 40)

        for step in self.plan:
            print(
                f" - {step}"
            )

        print()

        print("Recent Events")
        print("-" * 40)

        if not self.events:
            print("No events recorded.")
            return

        for event in self.events[-10:]:
            print(
                f"{event['time']} "
                f"{event['event']}"
            )

    # --------------------------------------------------
    # Stop
    # --------------------------------------------------

    def stop(self):
        if not self.started:
            print(
                "[RAIOS] Orchestrator not running."
            )
            return

        self.started = False

        self.emit("ORCHESTRATOR_STOP")

        print(
            "[RAIOS] Orchestrator stopped."
        )
