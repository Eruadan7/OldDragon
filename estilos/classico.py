from interfaces import JogaDados
from personagem import Personagem
import random

class Classico(Personagem, JogaDados):
    def __init__(self):
        super().__init__()
        for chave in self.atributos.keys():
            self.atributos[chave] = self.jogar_dados()

    def jogar_dados(self):
        atributo = 0
        for i in range(3):
            atributo += random.randint(1, 6)
        return atributo
