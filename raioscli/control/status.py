from raioscli.providers.hyperv import (
    get_vm_state,
    get_vm_network
)


def print_node(name, title=None):
    state = get_vm_state(name)

    if not state:
        state = "Not Deployed"

    print()
    print(title or name)
    print(f"  State : {state}")

    if state != "Not Deployed":
        result = get_vm_network(name)
        if result.stdout:
            print(result.stdout)


def region_status():

    print()
    print("RAIOS REGION STATUS")
    print("-" * 40)

    # Controlplane
    print_node("cp-1", "Controlplane")

    # Dataplanes
    for dp in ["dp-1", "dp-2", "dp-3"]:
        print_node(dp, f"Dataplane ({dp})")

    print()
