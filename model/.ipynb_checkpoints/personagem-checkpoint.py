from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self):   
        self.atributos = {
            "forca": None,
            "destreza": None,
            "constituicao": None,
            "inteligencia": None,
            "sabedoria": None,
            "carisma": None
        }

    def mostrar_valores_atributos(self):
        for i, (nome, valor) in enumerate(self.atributos.items(), start=1):
            print(f"{i}.{nome}: {'Vazio' if valor is None else valor}")
    








         

    

