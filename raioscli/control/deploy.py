from pathlib import Path
import yaml


def deploy_region(filename="region.yaml"):

    target = Path(filename)

    if not target.exists():
        print("[RAIOS] region.yaml not found.")
        return

    data = yaml.safe_load(target.read_text())

    print()
    print("RAIOS DEPLOYMENT PLAN")
    print("-" * 40)

    print()
    print("Controlplane")
    print("  Name   : cp-1")
    print(
        f"  Memory : {data['controlplane']['memory']} MB"
    )

    print()
    print("Dataplane")
    print("  Name   : dp-1")
    print(
        f"  Memory : {data['dataplanes']['memory']} MB"
    )

    print()
    print("Provider : Hyper-V")

    print()
    print("[RAIOS] Plan generated.")
