from model.bases import Raca

class Anao(Raca):
    def __init__(self):  
        super().__init__(
            nome = "Anão",
            habilidades={
                "movimento": 6,
                "infravisao": 18,
                "alinhamento": "ordem"
            },
            bonus=["mineracao", "vigor", "armas_grandes", "inimizade"]
        )