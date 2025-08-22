from interfaces import JogaDados, EscolhePontos
from personagem import Personagem
import random

class Heroico(Personagem, JogaDados, EscolhePontos):
    def __init__(self):
        super().__init__()
        self.escolher_pontos()

    def jogar_dados(self):
        atributo = 0
        menor = 0
        valores = []
        for i in range(4):
            valores.append(random.randint(1, 6))
        menor = valores.index(min(valores))
        print("Você tirou os valores: ",*valores, f"\nO valor {valores[menor]} foi eliminado")
        valores.pop(menor) 
        atributo = sum(valores)
        return atributo

    def escolher_pontos(self):
        for i in range(6):
            n = self.jogar_dados()
            print(f"Você tirou {n}...\n")
            self.mostrar_valores_atributos()
            self.set_atributo_por_indice(n) 

    def set_atributo_por_indice(self, valor):
        indice = int(input("\nPara qual atributo vai esse valor?\n")) - 1
        chave = list(self.atributos.keys())[indice]
        if self.atributos[chave] == None:   
            self.atributos[chave] = valor
            return
        print("Você deve escolher um novo atributo!")
        self.set_atributo_por_indice(valor)