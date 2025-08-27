from bases import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__(
            habilidades={
                "movimento": 9,
                "infravisao": 0,
                "alinhamento": "qualquer"
            },
            bonus=["aprendizado", "adaptabilidade"]
        )