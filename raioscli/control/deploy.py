# raioscli/control/deploy.py

from pathlib import Path
import yaml

from raioscli.control.ssh import (
    ensure_keypair
)

from raioscli.cloudinit.seed import (
    generate_controlplane_seed,
    generate_dataplane_seed
)

from raioscli.control.bootstrap import (
    bootstrap_controlplane,
    bootstrap_dataplane
)


def deploy_region(filename="region.yaml"):
    """
    Deploy a complete RAIOS region.

    Workflow:
    1. Validate region.yaml
    2. Ensure SSH keypair
    3. Generate Cloud-Init seed ISOs
    4. Provision Controlplane
    5. Provision Dataplane
    6. Print deployment summary
    """

    target = Path(filename)

    if not target.exists():
        print("[RAIOS] region.yaml not found.")
        return

    data = yaml.safe_load(
        target.read_text()
    )

    print()
    print("[RAIOS] Ensuring SSH keypair...")

    try:
        ensure_keypair()
    except Exception as exc:
        print(
            f"[RAIOS] SSH keypair failed: {exc}"
        )
        return

    print()
    print("[RAIOS] Generating CloudInit...")

    try:
        cp_seed_iso = generate_controlplane_seed()
        dp_seed_iso = generate_dataplane_seed()
    except Exception as exc:
        print(
            f"[RAIOS] CloudInit generation failed: {exc}"
        )
        return

    print()

    try:
        print(
            "[RAIOS] Provisioning Controlplane..."
        )

        bootstrap_controlplane()

        print(
            "[RAIOS] Controlplane ready."
        )

    except Exception as exc:
        print(
            f"[RAIOS] Controlplane failed: {exc}"
        )
        return

    print()

    try:
        print(
            "[RAIOS] Provisioning Dataplane..."
        )

        bootstrap_dataplane()

        print(
            "[RAIOS] Dataplane ready."
        )

    except Exception as exc:
        print(
            f"[RAIOS] Dataplane failed: {exc}"
        )
        return

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

    print("Network")
    print(
        f"  Switch : "
        f"{data['network']['switch']}"
    )

    print()
    print("Provider : Hyper-V")
    print()

    print("[RAIOS] Region deployed.")
