from model.bases import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__(
            nome = "Halfling",
            habilidades={
                "movimento": 6,
                "infravisao": 0,
                "alinhamento": "neutro"
            },
            bonus=["furtividade", "coragem", "pontaria", "baixa_estatura", "restricoes"]
        )