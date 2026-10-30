from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def create_storageo(self, name: str):
        pass

    @abstractmethod
    def create_storageb(self, name: str, size: str):
        pass

