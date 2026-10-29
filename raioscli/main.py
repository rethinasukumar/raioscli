import typer
from typing import Optional

from raioscli.core.commands import (
    handle_storageo,
    handle_storageb
)

from raioscli.control.region import (
    init_region,
    show_region
)

from raioscli.control.doctor import doctor as run_doctor

from raioscli.control.deploy import deploy_region

from raioscli.control.compute import (
    compute_test,
    compute_list,
    compute_create,
    compute_start
)

app = typer.Typer(
    help="RAIOS - Unified Multi-Cloud + Hypervisor CLI"
)

# ----------------------------------
# Storage
# ----------------------------------

@app.command()
def storageo(
    action: str,
    name: str,
    sync: str = ""
):
    """
    Object storage operations
    """
    handle_storageo(action, name, sync)


@app.command()
def storageb(
    action: str,
    name: str,
    size: str = "20GB",
    sync: str = ""
):
    """
    Block storage operations
    """
    handle_storageb(action, name, size, sync)


# ----------------------------------
# Region
# ----------------------------------

@app.command()
def region(action: str):
    """
    Region operations
    """

    if action == "init":
        init_region()

    elif action == "status":
        show_region()

    elif action == "deploy":
        deploy_region()

    else:
        print(
            f"[RAIOS] Unknown region action: {action}"
        )


# ----------------------------------
# Doctor
# ----------------------------------

@app.command()
def doctor():
    """
    Environment validation
    """
    run_doctor()


# ----------------------------------
# Compute
# ----------------------------------

@app.command()
def compute(
    action: str,
    name: Optional[str] = typer.Argument(None)
):
    """
    Compute operations
    """

    if action == "test":
        compute_test()

    elif action == "list":
        compute_list()

    elif action == "create":
        compute_create(name)

    elif action == "start":
        compute_start(name)

    else:
        print(
            f"[RAIOS] Unknown compute action: {action}"
        )


if __name__ == "__main__":
    app()
