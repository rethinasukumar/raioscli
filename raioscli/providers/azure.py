import subprocess
from raioscli.providers.base import Provider

class AzureProvider(Provider):

    def create_storageo(self, name: str):
        subprocess.run(
            ["az", "storage", "container", "create", "--name", name],
            shell=True
        )

    def create_storageb(self, name: str, size: str):
        gb = size.replace("GB", "")
        subprocess.run(
            ["az", "disk", "create", "--name", name, "--size-gb", gb],
            shell=True
        )

