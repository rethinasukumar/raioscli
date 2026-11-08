# raioscli/main.py

import typer
from typing import Optional

from raioscli.core.commands import (
    handle_storageo,
    handle_storageb,
)

from raioscli.control.region import (
    init_region,
    show_region,
)

from raioscli.control.status import (
    region_status,
)

from raioscli.control.deploy import (
    deploy_region,
)

from raioscli.control.destroy import (
    region_destroy,
)

from raioscli.control.node import (
    node_list,
    node_show,
    node_network,
    node_status,
)

from raioscli.control.doctor import (
    doctor as run_doctor,
)

from raioscli.control.compute import (
    compute_test,
    compute_list,
    compute_create,
    compute_start,
    compute_stop,
    compute_delete,
    compute_info,
)

from raioscli.agents.orchestrator import (
    Orchestrator,
)

from raioscli.agents.status import (
    agent_status,
)

app = typer.Typer(
    help="RAIOS - Unified Multi-Cloud + Hypervisor CLI"
)

# --------------------------------------------------
# Storage
# --------------------------------------------------

@app.command()
def storageo(
    action: str,
    name: str,
    sync: str = "",
):
    handle_storageo(
        action,
        name,
        sync,
    )


@app.command()
def storageb(
    action: str,
    name: str,
    size: str = "20GB",
    sync: str = "",
):
    handle_storageb(
        action,
        name,
        size,
        sync,
    )


# --------------------------------------------------
# Region
# --------------------------------------------------

@app.command()
def region(
    action: str,
):
    """
    Region lifecycle operations.
    """

    if action == "init":
        init_region()

    elif action == "show":
        show_region()

    elif action == "status":
        region_status()

    elif action == "deploy":
        deploy_region()

    elif action == "destroy":
        region_destroy()

    else:
        print(
            f"[RAIOS] Unknown region action: {action}"
        )


# --------------------------------------------------
# Node
# --------------------------------------------------

@app.command()
def node(
    action: str,
    name: Optional[str] = typer.Argument(None),
):
    """
    Node operations.

    Examples:

      raios node list

      raios node show cp-1
      raios node show dp-1
      raios node show dp-2
      raios node show dp-3

      raios node network dp-2
      raios node network dp-3
    """

    if action == "list":
        node_list()

    elif action == "show":
        node_show(name)

    elif action == "network":
        node_network(name)

    elif action == "status":
        node_status(name)

    else:
        print(
            f"[RAIOS] Unknown node action: {action}"
        )


# --------------------------------------------------
# Agent
# --------------------------------------------------

agent_app = typer.Typer(
    help="RAIOS Agent Framework"
)


@agent_app.command()
def start():
    orchestrator = Orchestrator()
    orchestrator.start()


@agent_app.command()
def status():
    agent_status()


@agent_app.command()
def stop():
    print()
    print("[RAIOS] Stopping agents...")
    print("[RAIOS] ControlPlaneAgent stopped")
    print("[RAIOS] DataPlaneAgent stopped")
    print("[RAIOS] Orchestrator stopped")
    print()


app.add_typer(
    agent_app,
    name="agent",
)


# --------------------------------------------------
# Doctor
# --------------------------------------------------

@app.command()
def doctor():
    run_doctor()


# --------------------------------------------------
# Compute
# --------------------------------------------------

@app.command()
def compute(
    action: str,
    name: Optional[str] = typer.Argument(None),
):
    """
    Compute operations.

    Examples:

      raios compute info dp-2
      raios compute start dp-3
      raios compute stop dp-2
    """

    if action == "test":
        compute_test()

    elif action == "list":
        compute_list()

    elif action == "create":
        compute_create(name)

    elif action == "start":
        compute_start(name)

    elif action == "stop":
        compute_stop(name)

    elif action == "delete":
        compute_delete(name)

    elif action == "info":
        compute_info(name)

    else:
        print(
            f"[RAIOS] Unknown compute action: {action}"
        )


# --------------------------------------------------
# Entry
# --------------------------------------------------

if __name__ == "__main__":
    app()
