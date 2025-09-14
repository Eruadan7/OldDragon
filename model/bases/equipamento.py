from abc import ABC, abstractmethod

class Equipamento(ABC):
    @abstractmethod
    def __init__(self, atributos):
        self.atributos = atributos