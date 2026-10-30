from pathlib import Path

from raioscli.cloudinit.controlplane import (
    generate_controlplane_user_data
)

from raioscli.cloudinit.dataplane import (
    generate_dataplane_user_data
)


def generate_meta_data(node_name):

    return f"""instance-id: {node_name}
local-hostname: {node_name}
"""


def generate_controlplane_seed():

    Path("cp-1-user-data").write_text(
        generate_controlplane_user_data()
    )

    Path("cp-1-meta-data").write_text(
        generate_meta_data("cp-1")
    )

    print("[RAIOS] Generated cp-1-user-data")
    print("[RAIOS] Generated cp-1-meta-data")


def generate_dataplane_seed():

    Path("dp-1-user-data").write_text(
        generate_dataplane_user_data()
    )

    Path("dp-1-meta-data").write_text(
        generate_meta_data("dp-1")
    )

    print("[RAIOS] Generated dp-1-user-data")
    print("[RAIOS] Generated dp-1-meta-data")
