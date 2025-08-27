from bases import Estilo
from utils import jogar_dados, escolher_atributos

class Aventureiro(Estilo):
    def gerar_atributos(self):
        visualizar_valores = []
        atributos = []
        usados = []
        for i in range(6):
            n = jogar_dados(3)
            atributos.append(None)
            visualizar_valores.append(n)
        return escolher_atributos(visualizar_valores, atributos, usados)



    
