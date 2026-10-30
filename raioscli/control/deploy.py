from pathlib import Path
import yaml

from raioscli.cloudinit.seed import (
    generate_controlplane_seed,
    generate_dataplane_seed
)


def deploy_region(filename="region.yaml"):

    target = Path(filename)

    if not target.exists():
        print("[RAIOS] region.yaml not found.")
        return

    data = yaml.safe_load(
        target.read_text()
    )

    print()
    print("[RAIOS] Generating CloudInit...")

    cp_seed_iso = (
        generate_controlplane_seed()
    )

    dp_seed_iso = (
        generate_dataplane_seed()
    )

    print()
    print("RAIOS DEPLOYMENT PLAN")
    print("-" * 40)

    print()
    print("Controlplane")
    print("  Name   : cp-1")
    print(
        f"  Memory : "
        f"{data['controlplane']['memory']} MB"
    )
    print(
        f"  Seed   : {cp_seed_iso}"
    )

    print()
    print("Dataplane")
    print("  Name   : dp-1")
    print(
        f"  Memory : "
        f"{data['dataplanes']['memory']} MB"
    )
    print(
        f"  Seed   : {dp_seed_iso}"
    )

    print()
    print("Provider : Hyper-V")

    print()
    print("[RAIOS] CloudInit generated.")
    print("[RAIOS] Plan generated.")
