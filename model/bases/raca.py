from abc import ABC, abstractmethod

class Raca(ABC):
    @abstractmethod
    def __init__(self, nome, habilidades, bonus):
        self.nome = nome
        self.habilidades = habilidades
        self.bonus = bonus