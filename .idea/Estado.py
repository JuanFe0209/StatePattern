from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def usarPower(self, contexto):
        pass

    @abstractmethod
    def usarHome(self, contexto):
        pass
