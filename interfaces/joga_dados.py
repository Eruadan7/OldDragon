from abc import ABC, abstractmethod

class JogaDados(ABC):
    @abstractmethod
    def jogar_dados(self):
        pass