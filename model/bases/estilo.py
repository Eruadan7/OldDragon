from abc import ABC, abstractmethod

class Estilo(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def gerar_atributos(self):
        pass