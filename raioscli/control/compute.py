from raioscli.providers.hyperv import (
    provider_info,
    list_vms,
    create_vm,
    start_vm,
    stop_vm,
    delete_vm,
    get_vm_info
)


def compute_test():
    provider_info()


def compute_list():

    result = list_vms()

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def compute_create(name):

    if not name:
        print("[RAIOS] VM name required")
        return

    result = create_vm(name)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def compute_start(name):

    if not name:
        print("[RAIOS] VM name required")
        return

    result = start_vm(name)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def compute_stop(name):

    if not name:
        print("[RAIOS] VM name required")
        return

    result = stop_vm(name)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def compute_delete(name):

    if not name:
        print("[RAIOS] VM name required")
        return

    result = delete_vm(name)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)


def compute_info(name):

    if not name:
        print("[RAIOS] VM name required")
        return

    result = get_vm_info(name)

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)
