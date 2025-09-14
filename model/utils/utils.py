from abc import ABC, abstractmethod
import random

def jogar_dados(jogadas):
    atributo = 0
    for i in range(jogadas):
        atributo += random.randint(1, 6)
    return atributo