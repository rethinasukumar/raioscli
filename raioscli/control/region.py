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
        "count": 1,
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

    print()
    print("RAIOS REGION")
    print("-" * 30)

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
    print(
        f"  Memory MB  : {data['controlplane']['memory']}"
    )

    print()
    print("Dataplanes:")
    print(
        f"  Count      : {data['dataplanes']['count']}"
    )
    print(
        f"  Memory MB  : {data['dataplanes']['memory']}"
    )
