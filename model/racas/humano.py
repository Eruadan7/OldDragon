from model.bases import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__(
            nome = "Humano",
            habilidades={
                "movimento": 9,
                "infravisao": 0,
                "alinhamento": "qualquer"
            },
            bonus=["aprendizado", "adaptabilidade"]
        )