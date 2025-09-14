from model.bases import Estilo
from model.utils.utils import jogar_dados

class Classico(Estilo):
    def __init__(self):
        self.nome = "Clássico"
    def gerar_atributos(self):
        atributos = []
        for i in range(6):
            atributos.append(jogar_dados(3))
        return atributos