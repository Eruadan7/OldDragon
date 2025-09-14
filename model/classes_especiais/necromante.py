from model.classes import MagoBase
from abc import ABC, abstractmethod

class Necromante(MagoBase):
    def __init__(self):
        self.nome = "Necromante"
        super().__init__(
            )
        self.habilidades_classe.update({
            "grimorio": ["toque_sombrio",
                         "aterrorizar",
                         "criar_mortos_vivos",
                         "drenar_vida",
                         "magia_da_morte"]})
        self.limite_itens.update({"armas": ["grandes", "medias"], 
                          "armaduras": "todas",
                          "magicos": [None]})