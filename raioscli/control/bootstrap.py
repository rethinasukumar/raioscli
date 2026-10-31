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

    wait_for_vm
)


# --------------------------------------------------
# Image Helpers
# --------------------------------------------------

def clone_image(
    source_image,
    node_name
):

    images_dir = Path(
        ".raios/images"
    )

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
# Controlplane
# --------------------------------------------------

def bootstrap_controlplane():

    base_image = ensure_image()

    image = clone_image(
        base_image,
        "cp-1"
    )

    delete_vm(
        "cp-1"
    )

    create_controlplane_vm()

    attach_vhdx(
        "cp-1",
        image
    )

    disable_secure_boot(
        "cp-1"
    )

    set_boot_disk_first(
        "cp-1"
    )

    attach_seed_iso(
        "cp-1",
        ".raios/cloudinit/cp-1-seed.iso"
    )

    result = start_controlplane()

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr
        )

    if not wait_for_vm("cp-1"):
        raise RuntimeError(
            "cp-1 failed to reach Running state."
        )

    print(
        "[RAIOS] cp-1 running."
    )


# --------------------------------------------------
# Dataplane
# --------------------------------------------------

def bootstrap_dataplane():

    base_image = ensure_image()

    image = clone_image(
        base_image,
        "dp-1"
    )

    delete_vm(
        "dp-1"
    )

    create_dataplane_vm()

    attach_vhdx(
        "dp-1",
        image
    )

    disable_secure_boot(
        "dp-1"
    )

    set_boot_disk_first(
        "dp-1"
    )

    attach_seed_iso(
        "dp-1",
        ".raios/cloudinit/dp-1-seed.iso"
    )

    result = start_dataplane()

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr
        )

    if not wait_for_vm("dp-1"):
        raise RuntimeError(
            "dp-1 failed to reach Running state."
        )

    print(
        "[RAIOS] dp-1 running."
    )
