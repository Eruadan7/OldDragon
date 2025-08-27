from bases import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__(
            habilidades={
                "movimento": 9,
                "infravisao": 18,
                "alinhamento": "neutro"
            },
            bonus=["percepcao_natural", "graciosidade", "arma_racial", "imunidades"]
        )