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

    node_dir = (
        CLOUDINIT_DIR /
        node_name
    )

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
        f"[RAIOS] Generated "
        f"{iso_file.name}"
    )

    return str(iso_file)


def generate_controlplane_seed():

    Path("cp-1-user-data").write_text(
        generate_controlplane_user_data()
    )

    Path("cp-1-meta-data").write_text(
        generate_meta_data("cp-1")
    )

    print("[RAIOS] Generated cp-1-user-data")
    print("[RAIOS] Generated cp-1-meta-data")

    return create_seed_iso("cp-1")


def generate_dataplane_seed():

    Path("dp-1-user-data").write_text(
        generate_dataplane_user_data()
    )

    Path("dp-1-meta-data").write_text(
        generate_meta_data("dp-1")
    )

    print("[RAIOS] Generated dp-1-user-data")
    print("[RAIOS] Generated dp-1-meta-data")

    return create_seed_iso("dp-1")
