from classes import MagoBase
from abc import ABC, abstractmethod

class Mago(MagoBase):
    def __init__(self):
        super().__init__(
            )
        self.habilidades_classe.update({
            "magias_arcanas" : 9, 
            "grimorio": ["3 magias arcanas de primeiro círculo"]})
        self.limite_itens.update({"armas": ["grandes", "medias"], 
                          "armaduras": "todas",
                          "magicos": [None]})