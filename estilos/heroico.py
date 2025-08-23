from interfaces import Estilo
from utils import escolher_atributos
import random

class Heroico(Estilo):
    def gerar_atributos(self):
        visualizar_valores = []
        atributos = []
        usados = []
        for i in range(6):
            n = self.jogar_dados2(4)
            atributos.append(None)
            visualizar_valores.append(n)
        return escolher_atributos(visualizar_valores, atributos, usados)
    
    def jogar_dados2(self, jogadas):
        atributo = 0
        menor = 0
        valores = []
        for i in range(4):
            valores.append(random.randint(1, 6))
        menor = valores.index(min(valores))
        valores.pop(menor) 
        atributo = sum(valores)
        return atributo