from interfaces import Estilo
from utils import jogar_dados

class Classico(Estilo):
    def gerar_atributos(self):
        atributos = []
        for i in range(6):
            atributos.append(jogar_dados(3))
        return atributos