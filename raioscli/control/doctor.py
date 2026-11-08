from pathlib import Path
import shutil
import socket
import yaml

from raioscli.providers.hyperv import (
    is_available,
    get_vm_state,
    get_vm_ips,
)


# --------------------------------------------------
# Utilities
# --------------------------------------------------

def check_tool(tool_name):
    return shutil.which(tool_name) is not None


def check_ssh(ip, port=22, timeout=3):
    """
    Simple TCP-level SSH reachability test.
    """

    if not ip:
        return False

    try:
        sock = socket.create_connection(
            (ip, port),
            timeout=timeout
        )
        sock.close()
        return True
    except Exception:
        return False


def status_icon(result):
    return "✅" if result else "❌"


# --------------------------------------------------
# Region Loader
# --------------------------------------------------

def load_region():
    region_file = Path("region.yaml")

    if not region_file.exists():
        return None

    with open(region_file, "r") as f:
        return yaml.safe_load(f)


# --------------------------------------------------
# Node Health
# --------------------------------------------------

def node_health(node_name):
    state = get_vm_state(node_name)

    ip_addresses = []

    try:
        ips = get_vm_ips(node_name)

        if ips.stdout:
            ip_addresses = [
                x.strip()
                for x in ips.stdout.splitlines()
                if "." in x
            ]

    except Exception:
        pass

    primary_ip = (
        ip_addresses[0]
        if ip_addresses
        else None
    )

    ssh_ok = check_ssh(primary_ip)

    return {
        "name": node_name,
        "state": state,
        "ip": primary_ip,
        "ssh": ssh_ok,
    }


# --------------------------------------------------
# Doctor
# --------------------------------------------------

def doctor():

    print()
    print("RAIOS Environment Check")
    print("-" * 60)

    region = load_region()

    checks = {
        "Python": True,
        "AWS CLI": check_tool("aws"),
        "Azure CLI": check_tool("az"),
        "Google CLI": check_tool("gcloud"),
        "Hyper-V": is_available(),
        "Region Config": region is not None,
        "SSH Key": (
            Path(".raios/ssh/id_ed25519").exists()
            and Path(".raios/ssh/id_ed25519.pub").exists()
        ),
    }

    for name, result in checks.items():
        print(
            f"{name:<20} {status_icon(result)}"
        )

    if not region:
        print()
        print("[RAIOS] region.yaml not found.")
        return

    print()
    print("RAIOS Region")
    print("-" * 60)

    print(
        f"Region       : {region['region']['name']}"
    )

    print(
        f"Switch       : {region['network']['switch']}"
    )

    print(
        f"Dataplanes   : {region['dataplanes']['count']}"
    )

    # ------------------------------------------
    # Nodes
    # ------------------------------------------

    nodes = ["cp-1"]

    nodes.extend(
        [
            f"dp-{i}"
            for i in range(
                1,
                region["dataplanes"]["count"] + 1
            )
        ]
    )

    print()
    print("RAIOS Node Health")
    print("-" * 60)

    print(
        f"{'Node':<12}"
        f"{'State':<12}"
        f"{'IP':<18}"
        f"{'SSH'}"
    )

    print("-" * 60)

    running_nodes = 0

    for node in nodes:

        health = node_health(node)

        if health["state"] == "Running":
            running_nodes += 1

        print(
            f"{node:<12}"
            f"{health['state']:<12}"
            f"{str(health['ip']):<18}"
            f"{status_icon(health['ssh'])}"
        )

    print()

    expected_nodes = len(nodes)

    region_healthy = (
        running_nodes == expected_nodes
    )

    print(
        f"Running Nodes : "
        f"{running_nodes}/{expected_nodes}"
    )

    print(
        f"Region Health : "
        f"{status_icon(region_healthy)}"
    )

    print()
