import typer

from raioscli.core.commands import (
    handle_storageo,
    handle_storageb
)

from raioscli.control.region import (
    init_region,
    show_region
)

app = typer.Typer(
    help="RAIOSCLI - Unified Multi-Cloud + Hypervisor CLI"
)

# ----------------------
# Storage
# ----------------------

@app.command()
def storageo(action: str, name: str, sync: str = ""):
    """
    Object storage operations
    """
    handle_storageo(action, name, sync)


@app.command()
def storageb(action: str, name: str, size: str = "20GB", sync: str = ""):
    """
    Block storage operations
    """
    handle_storageb(action, name, size, sync)


# ----------------------
# Region
# ----------------------

@app.command()
def region(action: str):
    """
    Region operations
    """

    if action == "init":
        init_region()

    elif action == "status":
        show_region()

    else:
        print(
            f"[RAIOS] Unknown region action: {action}"
        )


if __name__ == "__main__":
    app()
