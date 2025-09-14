from model.bases import Raca

class Gnomo(Raca):
    def __init__(self):
        super().__init__(
            nome = "Gnomo",
            habilidades={
                "movimento": 6,
                "infravisao": 18,
                "alinhamento": "neutro"
            },
            bonus=["avaliacao", "sagacidade", "vigor", "restricoes"]
        )