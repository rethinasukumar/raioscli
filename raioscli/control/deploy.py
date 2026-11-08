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


def _verify_seed(seed_iso: str):
    """
    Verify that a generated seed ISO exists.
    """
    if not seed_iso:
        raise RuntimeError(
            "Seed generation returned no path."
        )

    if not Path(seed_iso).exists():
        raise RuntimeError(
            f"Seed ISO not found: {seed_iso}"
        )

    print(
        f"[RAIOS] Verified seed: {seed_iso}"
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
        #
        # Controlplane Seed
        #
        cp_seed_iso = generate_controlplane_seed()

        _verify_seed(cp_seed_iso)

        #
        # Dataplane Seeds
        #
        dp_count = data["dataplanes"]["count"]

        dp_seed_isos = []

        for index in range(1, dp_count + 1):

            node_name = f"dp-{index}"

            seed_iso = generate_dataplane_seed(
                node_name
            )

            _verify_seed(seed_iso)

            dp_seed_isos.append(
                (
                    node_name,
                    seed_iso
                )
            )

    except Exception as exc:
        print(
            f"[RAIOS] CloudInit generation failed: {exc}"
        )
        return

    print()

    #
    # Controlplane
    #
    try:
        print(
            "[RAIOS] Provisioning Controlplane..."
        )

        bootstrap_controlplane(
            "cp-1",
            cp_seed_iso
        )

        print(
            "[RAIOS] Controlplane ready."
        )

    except Exception as exc:
        print(
            f"[RAIOS] Controlplane failed: {exc}"
        )
        return

    print()

    #
    # Dataplanes
    #
    for node_name, seed_iso in dp_seed_isos:

        try:
            print(
                f"[RAIOS] Provisioning {node_name}..."
            )

            bootstrap_dataplane(
                node_name,
                seed_iso
            )

            print(
                f"[RAIOS] {node_name} ready."
            )

        except Exception as exc:
            print(
                f"[RAIOS] {node_name} failed: {exc}"
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
    print("Dataplanes")
    print()

    for node_name, seed_iso in dp_seed_isos:

        print(
            f"  Name   : {node_name}"
        )
        print(
            f"  Memory : "
            f"{data['dataplanes']['memory']} MB"
        )
        print(
            f"  Seed   : {seed_iso}"
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
