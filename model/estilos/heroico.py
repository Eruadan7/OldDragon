from model.bases import Estilo
import random

class Heroico(Estilo):
    def __init__(self):
        self.nome = "Heróico"
    
    def gerar_atributos(self):
        atributos = []
        for i in range(6):
            atributos.append(self.jogar_dados2(3))
        return atributos
    
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