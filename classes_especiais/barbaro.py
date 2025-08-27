from classes import GuerreiroBase
from abc import ABC, abstractmethod

class Barbaro(GuerreiroBase):
    def __init__(self):
        super().__init__(
        )
        self.habilidades_classe.update({
            "vigor_barbaro": 1,
            "talentos_selvagens": 3,
            "surpresa_selvagen": 6,
            "Forca_totem": 10
        })
        self.limite_itens.update({
            "armas": [None],
            "armaduras": ["Não-couro"],
            "magicos": ["todos"]
        })