from abc import ABC, abstractmethod

class Raca(ABC):
    @abstractmethod
    def __init__(self, habilidades, bonus):
        self.habilidades = habilidades
        self.bonus = bonus