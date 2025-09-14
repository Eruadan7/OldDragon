from model.bases import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__(
            nome = "Elfo",
            habilidades={
                "movimento": 9,
                "infravisao": 18,
                "alinhamento": "neutro"
            },
            bonus=["percepcao_natural", "graciosidade", "arma_racial", "imunidades"]
        )