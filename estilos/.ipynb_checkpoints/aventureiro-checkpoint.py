from interfaces import JogaDados, EscolhePontos
from personagem import Personagem
import random

class Aventureiro(Personagem, JogaDados, EscolhePontos):
    def __init__(self):
        super().__init__()
        self.escolher_pontos()

    def jogar_dados(self):
        atributo = 0
        for i in range(3):
            atributo += random.randint(1, 6)
        return atributo

    def escolher_pontos(self):
        valores = []
        for i in range(6):
            n = self.jogar_dados()
            valores.append(n)
        for i in range(6):
            print("Você tem os seguintes valores:\n", *valores)
            self.mostrar_valores_atributos()
            self.set_atributo_por_indice(valores[i])
            valores[i] = 0

    def set_atributo_por_indice(self, valor):
        indice = int(input(f"\nPara qual atributo vai esse valor: {valor}\n")) - 1
        chave = list(self.atributos.keys())[indice]
        if self.atributos[chave] == None:   
            self.atributos[chave] = valor
            return
        print("Você deve escolher um novo atributo!")
        self.set_atributo_por_indice(valor)