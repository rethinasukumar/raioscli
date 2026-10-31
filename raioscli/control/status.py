from raioscli.providers.hyperv import (
    get_vm_state,
    get_vm_network
)


def region_status():

    cp_state = get_vm_state("cp-1")
    dp_state = get_vm_state("dp-1")

    if not cp_state:
        cp_state = "Not Deployed"

    if not dp_state:
        dp_state = "Not Deployed"

    print()
    print("RAIOS REGION STATUS")
    print("-" * 40)

    print()
    print("Controlplane")
    print(f"  State : {cp_state}")

    if cp_state != "Not Deployed":
        result = get_vm_network("cp-1")
        if result.stdout:
            print(result.stdout)

    print()
    print("Dataplane")
    print(f"  State : {dp_state}")

    if dp_state != "Not Deployed":
        result = get_vm_network("dp-1")
        if result.stdout:
            print(result.stdout)

    print()

