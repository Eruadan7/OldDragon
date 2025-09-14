from bases import Equipamento

class Adaga(Equipamento):
    def __init__(self):
        super().__init__(
            atributos={
                "nome": "adaga",
                "dano": "id4", 
                "carga": 1,
                "descricao": "Pequena, Perfurante, Arremesso (9)", 
                "custo":"2 p o"}
            )