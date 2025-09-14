from model.bases import Raca

class MeioElfo(Raca):
    def __init__(self):
        super().__init__(
            nome = "Meio-Elfo",
            habilidades={
                "movimento": 9,
                "infravisao": 9,
                "alinhamento": "caos"
            },
            bonus=["aprendizado", "graciosidade", "vigor", "idioma_extra", "imunidades"]
        )