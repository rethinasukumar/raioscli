from pathlib import Path
import shutil
import pycdlib

from raioscli.cloudinit.controlplane import (
    generate_controlplane_user_data
)

from raioscli.cloudinit.dataplane import (
    generate_dataplane_user_data
)

CLOUDINIT_DIR = Path(".raios/cloudinit")


def generate_meta_data(node_name):
    return f"""instance-id: {node_name}
local-hostname: {node_name}
"""


def create_seed_iso(node_name):
    node_dir = CLOUDINIT_DIR / node_name

    if node_dir.exists():
        shutil.rmtree(node_dir)

    node_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy(
        f"{node_name}-user-data",
        node_dir / "user-data"
    )

    shutil.copy(
        f"{node_name}-meta-data",
        node_dir / "meta-data"
    )

    iso_file = (
        CLOUDINIT_DIR /
        f"{node_name}-seed.iso"
    )

    iso = pycdlib.PyCdlib()

    iso.new(
        vol_ident="CIDATA",
        joliet=True
    )

    iso.add_file(
        str(node_dir / "user-data"),
        iso_path="/USERDATA.;1",
        joliet_path="/user-data"
    )

    iso.add_file(
        str(node_dir / "meta-data"),
        iso_path="/METADATA.;1",
        joliet_path="/meta-data"
    )

    iso.write(str(iso_file))
    iso.close()

    print(
        f"[RAIOS] Generated {iso_file.name}"
    )

    return str(iso_file)


def generate_controlplane_seed():
    node_name = "cp-1"

    Path(
        f"{node_name}-user-data"
    ).write_text(
        generate_controlplane_user_data()
    )

    Path(
        f"{node_name}-meta-data"
    ).write_text(
        generate_meta_data(node_name)
    )

    print(
        f"[RAIOS] Generated {node_name}-user-data"
    )

    print(
        f"[RAIOS] Generated {node_name}-meta-data"
    )

    return create_seed_iso(node_name)


def generate_dataplane_seed(node_name):
    Path(
        f"{node_name}-user-data"
    ).write_text(
        generate_dataplane_user_data(node_name)
    )

    Path(
        f"{node_name}-meta-data"
    ).write_text(
        generate_meta_data(node_name)
    )

    print(
        f"[RAIOS] Generated {node_name}-user-data"
    )

    print(
        f"[RAIOS] Generated {node_name}-meta-data"
    )

    return create_seed_iso(node_name)


def generate_dataplane_seeds(count):
    seed_isos = []

    for index in range(1, count + 1):

        node_name = f"dp-{index}"

        seed_iso = generate_dataplane_seed(
            node_name
        )

        seed_isos.append(
            (node_name, seed_iso)
        )

    return seed_isos
