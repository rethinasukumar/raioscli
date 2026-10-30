from rich.console import Console
from rich.table import Table

from raioscli.core.mapping import resolve_service
from raioscli.providers.aws import AwsProvider
from raioscli.providers.gcp import GcpProvider
from raioscli.providers.azure import AzureProvider
from raioscli.providers.raios import RaiosProvider

console = Console()

def parse_sync(sync: str):
    return [p.strip() for p in sync.split(",")] if sync else []

def get_provider(name: str):
    if name == "aws":
        return AwsProvider()
    if name == "gcp":
        return GcpProvider()
    if name == "azure":
        return AzureProvider()
    if name == "raios":
        return RaiosProvider()
    raise ValueError(f"Unknown provider: {name}")

def handle_storageo(action: str, name: str, sync: str):
    providers = parse_sync(sync)

    table = Table(title="StorageO Operation")
    table.add_column("Provider")
    table.add_column("Service")
    table.add_column("Status")

    for p in providers:
        provider = get_provider(p)
        service = resolve_service("storageo", p)

        if action == "create":
            provider.create_storageo(name)
            table.add_row(p, service, "[green]✔ created[/green]")

    console.print(table)

def handle_storageb(action: str, name: str, size: str, sync: str):
    providers = parse_sync(sync)

    table = Table(title="StorageB Operation")
    table.add_column("Provider")
    table.add_column("Service")
    table.add_column("Status")

    for p in providers:
        provider = get_provider(p)
        service = resolve_service("storageb", p)

        if action == "create":
            provider.create_storageb(name, size)
            table.add_row(p, service, "[green]✔ created[/green]")

    console.print(table)

