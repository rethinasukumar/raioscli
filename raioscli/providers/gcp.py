import subprocess
from raioscli.providers.base import Provider

class GcpProvider(Provider):

    def create_storageo(self, name: str):
        subprocess.run(
            ["gsutil", "mb", f"gs://{name}"],
            shell=True
        )

    def create_storageb(self, name: str, size: str):
        gb = size.replace("GB", "")
        subprocess.run(
            ["gcloud", "compute", "disks", "create", name, "--size", gb],
            shell=True
        )

