from pathlib import Path
import yaml

DEFAULT_REGION = {
    "region": {
        "name": "ap-sg-1"
    },
    "network": {
        "switch": "Default Switch"
    },
    "controlplane": {
        "memory": 2048
    },
    "dataplanes": {
        "count": 3,
        "memory": 2048
    }
}


def init_region(filename="region.yaml"):
    """
    Creates a default region.yaml file.
    """

    target = Path(filename)

    if target.exists():
        print(f"[RAIOS] {filename} already exists.")
        return

    with open(target, "w") as f:
        yaml.safe_dump(
            DEFAULT_REGION,
            f,
            sort_keys=False
        )

    print(f"[RAIOS] Created {filename}")


def show_region(filename="region.yaml"):
    """
    Displays region configuration.
    """

    target = Path(filename)

    if not target.exists():
        print(f"[RAIOS] {filename} not found.")
        return

    data = yaml.safe_load(
        target.read_text()
    )

    dp_count = data["dataplanes"]["count"]

    print()
    print("RAIOS REGION")
    print("-" * 40)

    print("Region:")
    print(
        f"  Name       : {data['region']['name']}"
    )

    print()
    print("Network:")
    print(
        f"  Switch     : {data['network']['switch']}"
    )

    print()
    print("Controlplane:")
    print("  Node       : cp-1")
    print(
        f"  Memory MB  : {data['controlplane']['memory']}"
    )

    print()
    print("Dataplanes:")
    print(
        f"  Count      : {dp_count}"
    )
    print(
        f"  Memory MB  : {data['dataplanes']['memory']}"
    )

    print("  Nodes:")
    for i in range(1, dp_count + 1):
        print(f"    - dp-{i}")

    print()
