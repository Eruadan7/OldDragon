from bases import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__(
            habilidades={
                "movimento": 6,
                "infravisao": 0,
                "alinhamento": "neutro"
            },
            bonus=["furtividade", "coragem", "pontaria", "baixa_estatura", "restricoes"]
        )