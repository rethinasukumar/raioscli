# raioscli/control/heal.py

from raioscli.providers.hyperv import (
    get_vm_state
)

from raioscli.control.bootstrap import (
    bootstrap_controlplane,
    bootstrap_dataplane
)


def heal_region():

    print()
    print("RAIOS HEAL")
    print("-" * 40)

    cp_state = get_vm_state("cp-1")

    if cp_state != "Running":
        print(
            "[RAIOS] Controlplane unhealthy"
        )

        bootstrap_controlplane()

    else:
        print(
            "[RAIOS] Controlplane healthy"
        )

    dp_state = get_vm_state("dp-1")

    if dp_state != "Running":
        print(
            "[RAIOS] Dataplane unhealthy"
        )

        bootstrap_dataplane()

    else:
        print(
            "[RAIOS] Dataplane healthy"
        )

    print()
    print("[RAIOS] Heal completed")
