from bases import Classe
from abc import ABC, abstractmethod

class MagoBase(Classe):
    @abstractmethod
    def __init__(self):
        super().__init__(
            estatisticas={
                "nivel": 1,
                "xp": 0,
                "pontos_vida": 4,
                "base_ataque": 0,
                "jogada_protecao": 5,
                "xp_especial" : 0,
            },
            habilidades_classe= {
                "magias_arcanas": 6,
                "grimorio": [],
                "ler_magias": 1,
                "detectar_magias": 1
            },
            limite_itens = {})