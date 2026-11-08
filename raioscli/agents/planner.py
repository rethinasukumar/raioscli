# raioscli/agents/planner.py

from pathlib import Path
import yaml

from raioscli.providers.hyperv import (
    get_vm_state
)


class Planner:
    """
    Converts desired state into executable actions.
    """

    def __init__(
        self,
        filename="region.yaml"
    ):
        self.filename = filename

    def desired_state(self):
        data = yaml.safe_load(
            Path(self.filename).read_text()
        )

        return {
            "controlplane": "cp-1",
            "dataplanes": [
                f"dp-{n}"
                for n in range(
                    1,
                    data["dataplanes"]["count"] + 1
                )
            ]
        }

    def actual_state(self):
        state = {}

        state["cp-1"] = (
            get_vm_state("cp-1")
        )

        for i in range(1, 100):
            name = f"dp-{i}"
            vm_state = get_vm_state(name)

            if not vm_state:
                continue

            state[name] = vm_state

        return state

    def create_plan(self):
        desired = self.desired_state()
        actual = self.actual_state()

        plan = []

        #
        # Controlplane heal
        #

        cp = desired["controlplane"]

        if actual.get(cp) != "Running":
            plan.append({
                "action": "heal",
                "node": cp
            })

        #
        # Dataplane reconcile
        #

        desired_dp = set(
            desired["dataplanes"]
        )

        actual_dp = {
            vm
            for vm in actual.keys()
            if vm.startswith("dp-")
        }

        #
        # Scale out
        #

        for node in sorted(
            desired_dp - actual_dp
        ):
            plan.append({
                "action": "scale_out",
                "node": node
            })

        #
        # Heal
        #

        for node in sorted(
            desired_dp & actual_dp
        ):
            if actual[node] != "Running":
                plan.append({
                    "action": "heal",
                    "node": node
                })

        #
        # Scale in
        #

        for node in sorted(
            actual_dp - desired_dp
        ):
            plan.append({
                "action": "scale_in",
                "node": node
            })

        return plan
