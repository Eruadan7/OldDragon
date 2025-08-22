from abc import ABC, abstractmethod

class EscolhePontos(ABC):
    @abstractmethod
    def escolher_pontos(self):
        pass

    @abstractmethod
    def set_atributo_por_indice(self):
        pass