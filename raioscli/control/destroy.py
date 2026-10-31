from pathlib import Path

from raioscli.providers.hyperv import (
    delete_vm
)


def region_destroy():

    print()
    print("[RAIOS] Destroying region...")

    # ------------------------------------
    # Delete Controlplane
    # ------------------------------------

    print(
        "[RAIOS] Removing cp-1..."
    )

    delete_vm(
        "cp-1"
    )

    # ------------------------------------
    # Delete Dataplane
    # ------------------------------------

    print(
        "[RAIOS] Removing dp-1..."
    )

    delete_vm(
        "dp-1"
    )

    # ------------------------------------
    # Remove node disks
    # ------------------------------------

    cp_disk = Path(
        ".raios/images/cp-1.vhdx"
    )

    dp_disk = Path(
        ".raios/images/dp-1.vhdx"
    )

    if cp_disk.exists():

        cp_disk.unlink()

        print(
            "[RAIOS] Deleted cp-1.vhdx"
        )

    if dp_disk.exists():

        dp_disk.unlink()

        print(
            "[RAIOS] Deleted dp-1.vhdx"
        )

    print()
    print(
        "[RAIOS] Region destroyed."
    )
