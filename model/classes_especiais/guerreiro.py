from model.classes import GuerreiroBase
from abc import ABC, abstractmethod

class Guerreiro(GuerreiroBase):
    def __init__(self):
        self.nome = "Guerreiro"
        super().__init__(
            )
        self.habilidades_classe["ataque_extra"] = 6
        self.limite_itens.update({"armas": [None], 
                          "armaduras": [None],
                          "magicos": ["cajado","pergaminho"]})