from pathlib import Path

from raioscli.providers.hyperv import (
    delete_vm
)


def region_destroy():
    print()
    print("[RAIOS] Destroying region...")

    # ------------------------------------
    # Nodes
    # ------------------------------------

    nodes = [
        "cp-1",
        "dp-1",
        "dp-2",
        "dp-3",
    ]

    for node in nodes:
        print(
            f"[RAIOS] Removing {node}..."
        )

        delete_vm(
            node
        )

    # ------------------------------------
    # Remove node disks
    # ------------------------------------

    for node in nodes:
        disk = Path(
            f".raios/images/{node}.vhdx"
        )

        if disk.exists():
            disk.unlink()

            print(
                f"[RAIOS] Deleted {node}.vhdx"
            )

    print()
    print(
        "[RAIOS] Region destroyed."
    )
