from raioscli.providers.hyperv import (
    list_vms,
    get_vm_info,
    get_vm_network,
    get_vm_state
)

# --------------------------------------------------
# Node List
# --------------------------------------------------

def node_list():
    result = list_vms()

    if result.stdout:
        print()
        print("RAIOS NODES")
        print("-" * 40)
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


# --------------------------------------------------
# Node Show
# --------------------------------------------------

def node_show(name):
    if not name:
        print("[RAIOS] Node name required")
        return

    result = get_vm_info(name)

    if result.stdout:
        print()
        print("RAIOS NODE")
        print("-" * 40)
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


# --------------------------------------------------
# Node Network
# --------------------------------------------------

def node_network(name):
    if not name:
        print("[RAIOS] Node name required")
        return

    result = get_vm_network(name)

    if result.stdout:
        print()
        print("RAIOS NODE NETWORK")
        print("-" * 40)
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


# --------------------------------------------------
# Node Status
# --------------------------------------------------

def node_status(name):
    if not name:
        print("[RAIOS] Node name required")
        return

    print()
    print("RAIOS NODE STATUS")
    print("-" * 40)
    print(f"Node  : {name}")
    print(f"State : {get_vm_state(name)}")


# --------------------------------------------------
# Convenience Helpers
# --------------------------------------------------

# Controlplane

def controlplane_show():
    node_show("cp-1")


def controlplane_network():
    node_network("cp-1")


def controlplane_status():
    node_status("cp-1")


# Dataplane 1

def dataplane_show():
    node_show("dp-1")


def dataplane_network():
    node_network("dp-1")


def dataplane_status():
    node_status("dp-1")


# Dataplane 2

def dataplane2_show():
    node_show("dp-2")


def dataplane2_network():
    node_network("dp-2")


def dataplane2_status():
    node_status("dp-2")


# Dataplane 3

def dataplane3_show():
    node_show("dp-3")


def dataplane3_network():
    node_network("dp-3")


def dataplane3_status():
    node_status("dp-3")

