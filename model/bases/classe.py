from abc import ABC, abstractmethod

class Classe(ABC):
    @abstractmethod
    def __init__(self, estatisticas, habilidades_classe, limite_itens):
        self.estatisticas = estatisticas
        self.habilidades_classe = habilidades_classe
        self.limite_itens = limite_itens