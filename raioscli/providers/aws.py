import subprocess
from raioscli.providers.base import Provider

class AwsProvider(Provider):

    def create_storageo(self, name: str):
        subprocess.run(
            ["aws", "s3api", "create-bucket", "--bucket", name],
            shell=True
        )

    def create_storageb(self, name: str, size: str):
        gb = size.replace("GB", "")
        subprocess.run(
            ["aws", "ec2", "create-volume", "--size", gb, "--availability-zone", "ap-southeast-1a"],
            shell=True
        )

