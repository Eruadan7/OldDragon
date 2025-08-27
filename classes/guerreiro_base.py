from bases import Classe
from abc import ABC, abstractmethod

class GuerreiroBase(Classe):
    @abstractmethod
    def __init__(self):
        super().__init__(
            estatisticas={
                "nivel": 1,
                "xp": 0,
                "pontos_vida": 10,
                "base_ataque": 1,
                "jogada_protecao": 5,
                "xp_especial" : 0
            },
            habilidades_classe= {
                "Aparar": 1,
                "maestria_arma": 1
            },
            limite_itens = {})

#lembrete: não esquecer de passar os valores que a classe-pai exige
#para poder iniciar, dentro do super().__init__(#)