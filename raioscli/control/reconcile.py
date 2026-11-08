# raioscli/control/reconcile.py

from pathlib import Path
import yaml

from raioscli.providers.hyperv import (
    get_vm_state
)

from raioscli.control.bootstrap import (
    bootstrap_controlplane,
    bootstrap_dataplane
)


def reconcile_region(
    filename="region.yaml"
):

    target = Path(filename)

    if not target.exists():
        print(
            "[RAIOS] region.yaml not found."
        )
        return

    desired = yaml.safe_load(
        target.read_text()
    )

    desired_dp_count = (
        desired["dataplanes"]["count"]
    )

    print()
    print("RAIOS RECONCILE")
    print("-" * 40)

    #
    # Controlplane
    #

    if get_vm_state("cp-1") != "Running":

        print(
            "[RAIOS] Reconciling cp-1"
        )

        bootstrap_controlplane()

    #
    # Dataplanes
    #

    for node in range(
        1,
        desired_dp_count + 1
    ):

        vm = f"dp-{node}"

        if get_vm_state(vm) != "Running":

            print(
                f"[RAIOS] Reconciling {vm}"
            )

            bootstrap_dataplane(
                name=vm
            )

    print()
    print(
        "[RAIOS] Desired state achieved."
    )
