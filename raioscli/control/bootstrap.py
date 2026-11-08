from pathlib import Path
import shutil

from raioscli.images.amazonlinux import (
    ensure_image
)

from raioscli.providers.hyperv import (
    create_controlplane_vm,
    create_dataplane_vm,
    delete_vm,
    attach_vhdx,
    attach_seed_iso,
    disable_secure_boot,
    set_boot_disk_first,
    start_controlplane,
    start_dataplane,
    wait_for_vm,
)

# --------------------------------------------------
# Image Helpers
# --------------------------------------------------

def clone_image(
    source_image,
    node_name
):
    images_dir = Path(".raios/images")

    images_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    node_image = (
        images_dir /
        f"{node_name}.vhdx"
    )

    if node_image.exists():
        node_image.unlink()

    shutil.copy2(
        source_image,
        node_image
    )

    print(
        f"[RAIOS] Cloned image: {node_image}"
    )

    return str(node_image)


# --------------------------------------------------
# Seed Validation
# --------------------------------------------------

def validate_seed_iso(
    seed_iso
):
    if not seed_iso:
        return

    seed_path = Path(seed_iso)

    if not seed_path.exists():
        raise FileNotFoundError(
            f"[RAIOS] Seed ISO not found: {seed_path}"
        )


# --------------------------------------------------
# Controlplane
# --------------------------------------------------

def bootstrap_controlplane(
    node_name="cp-1",
    seed_iso=None
):
    validate_seed_iso(
        seed_iso
    )

    base_image = ensure_image()

    image = clone_image(
        base_image,
        node_name
    )

    delete_vm(
        node_name
    )

    create_controlplane_vm(
        name=node_name
    )

    attach_vhdx(
        node_name,
        image
    )

    disable_secure_boot(
        node_name
    )

    set_boot_disk_first(
        node_name
    )

    if seed_iso:
        attach_seed_iso(
            node_name,
            seed_iso
        )

    result = start_controlplane(
        node_name
    )

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr
        )

    if not wait_for_vm(
        node_name
    ):
        raise RuntimeError(
            f"{node_name} failed to reach Running state."
        )

    print(
        f"[RAIOS] {node_name} running."
    )


# --------------------------------------------------
# Dataplane
# --------------------------------------------------

def bootstrap_dataplane(
    node_name,
    seed_iso=None
):
    validate_seed_iso(
        seed_iso
    )

    base_image = ensure_image()

    image = clone_image(
        base_image,
        node_name
    )

    delete_vm(
        node_name
    )

    create_dataplane_vm(
        name=node_name
    )

    attach_vhdx(
        node_name,
        image
    )

    disable_secure_boot(
        node_name
    )

    set_boot_disk_first(
        node_name
    )

    if seed_iso:
        attach_seed_iso(
            node_name,
            seed_iso
        )

    result = start_dataplane(
        node_name
    )

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr
        )

    if not wait_for_vm(
        node_name
    ):
        raise RuntimeError(
            f"{node_name} failed to reach Running state."
        )

    print(
        f"[RAIOS] {node_name} running."
    )


# --------------------------------------------------
# Region
# --------------------------------------------------

def bootstrap_region(
    dataplane_count=3
):
    cp_seed = (
        ".raios/cloudinit/cp-1-seed.iso"
    )

    bootstrap_controlplane(
        "cp-1",
        cp_seed
    )

    for index in range(
        1,
        dataplane_count + 1
    ):
        node_name = (
            f"dp-{index}"
        )

        seed_iso = (
            f".raios/cloudinit/{node_name}-seed.iso"
        )

        bootstrap_dataplane(
            node_name,
            seed_iso
        )

    print()
    print(
        "[RAIOS] Region bootstrap complete."
    )
