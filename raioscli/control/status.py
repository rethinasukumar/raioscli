from raioscli.providers.hyperv import (
    get_vm_state
)


def region_status():

    print()
    print("RAIOS REGION STATUS")
    print("-" * 40)

    print()
    print("Controlplane")
    print(
        f"  State : {get_vm_state('cp-1')}"
    )

    print()

    print("Dataplane")
    print(
        f"  State : {get_vm_state('dp-1')}"
    )
