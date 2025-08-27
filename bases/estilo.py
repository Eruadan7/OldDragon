from abc import ABC, abstractmethod

class Estilo(ABC):
    @abstractmethod
    def gerar_atributos(self):
        pass