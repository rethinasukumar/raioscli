# raioscli/control/scale.py

from pathlib import Path
import yaml

from raioscli.control.bootstrap import (
    bootstrap_dataplane
)


def scale_region(
    desired_count: int,
    filename: str = "region.yaml"
):
    target = Path(filename)

    if not target.exists():
        print("[RAIOS] region.yaml not found.")
        return

    data = yaml.safe_load(
        target.read_text()
    )

    current = data["dataplanes"]["count"]

    if desired_count <= current:
        print(
            f"[RAIOS] Already running {current} dataplanes."
        )
        return

    print()
    print("[RAIOS] Scaling dataplanes")
    print("-" * 40)

    for node in range(
        current + 1,
        desired_count + 1
    ):
        print(
            f"[RAIOS] Creating dp-{node}"
        )

        bootstrap_dataplane(
            name=f"dp-{node}"
        )

    data["dataplanes"]["count"] = desired_count

    target.write_text(
        yaml.safe_dump(
            data,
            sort_keys=False
        )
    )

    print()
    print(
        f"[RAIOS] Scale complete ({desired_count} nodes)"
    )
