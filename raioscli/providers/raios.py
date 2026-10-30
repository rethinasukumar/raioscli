from raioscli.providers.base import Provider

class RaiosProvider(Provider):

    def create_storageo(self, name: str):
        print(f"[RAIOS] StorageO bucket created: {name}")

    def create_storageb(self, name: str, size: str):
        print(f"[RAIOS] StorageB volume created: {name} ({size})")

